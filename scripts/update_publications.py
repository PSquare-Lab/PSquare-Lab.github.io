#!/usr/bin/env python3
"""
Update _bibliography/papers.bib from a Google Scholar profile — SAFELY.

What it does
------------
* Reads your Scholar profile (id from _config.yml: `scholar_userid`, or --id).
* Compares against the entries already in papers.bib (by cite-key AND by
  normalised title).
* For papers NOT already present, appends a properly-formatted BibTeX *stub*
  that matches this repo's conventions (cite-key `lastnameYEARword`, `keywords`,
  `bibtex_show={true}`, `arxiv`/`url`).
* It ONLY appends. It never edits or reorders existing entries, so any
  hand-curated tags you added (`selected`, `preview`, `pdf`, `abbr`, fixed
  venue/authors) are preserved.

Every appended entry is marked with a `% AUTO-ADDED … REVIEW` comment so you can
find them, fix the venue/authors, set the right `keywords`, and add
`selected`/`preview`/`pdf` before committing. Review the diff, then commit.

Why local (not a GitHub Action)
--------------------------------
Google Scholar has no API and blocks datacenter IPs (CI runners). Running from
your own machine is far more reliable. If you still get blocked, rerun later or
route scholarly through a proxy (see scholarly docs: ProxyGenerator).

Usage
-----
    pip install -r scripts/requirements.txt
    python scripts/update_publications.py             # fetch + append new stubs
    python scripts/update_publications.py --dry-run    # print, write nothing
    python scripts/update_publications.py --since 2024 # only papers from 2024 onward
    python scripts/update_publications.py --id XXXX    # override Scholar id

Note: papers.bib is whatever YOU have curated. Anything on Scholar but not in
papers.bib is reported as "new" — including old papers. Use --since to focus on
recent work, or do one full import (then later runs go quiet).
"""

from __future__ import annotations

import argparse
import datetime as _dt
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
BIB_PATH = REPO_ROOT / "_bibliography" / "papers.bib"
CONFIG_PATH = REPO_ROOT / "_config.yml"

STOPWORDS = {"a", "an", "the", "on", "of", "for", "to", "in", "and", "with", "via", "towards"}


def scholar_id_from_config() -> str | None:
    if not CONFIG_PATH.exists():
        return None
    m = re.search(r"^scholar_userid:\s*([A-Za-z0-9_-]+)", CONFIG_PATH.read_text(), re.M)
    return m.group(1) if m else None


def normalise_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def load_existing(bibtext: str):
    """Return (set_of_keys, set_of_normalised_titles) already in the file."""
    keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibtext))
    titles = {
        normalise_title(t)
        for t in re.findall(r"title\s*=\s*[\{\"](.+?)[\}\"]\s*,?", bibtext, re.S | re.I)
    }
    return keys, titles


def surname(name: str) -> str:
    name = name.strip()
    if "," in name:                       # already "Last, First"
        return name.split(",")[0].strip()
    parts = name.split()
    return parts[-1] if parts else name


def to_last_first(name: str) -> str:
    """'Parikshit Pareek' -> 'Pareek, Parikshit'. Leaves 'Last, First' as-is."""
    name = name.strip()
    if not name or "," in name:
        return name
    parts = name.split()
    if len(parts) == 1:
        return parts[0]
    return f"{parts[-1]}, {' '.join(parts[:-1])}"


def format_authors(raw: str) -> str:
    authors = [a.strip() for a in re.split(r"\s+and\s+", raw) if a.strip()]
    return " and ".join(to_last_first(a) for a in authors)


def make_key(authors_raw: str, year: str, title: str, used: set[str]) -> str:
    last = re.sub(r"[^a-z]", "", surname(authors_raw.split(" and ")[0]).lower()) or "anon"
    word = ""
    for w in normalise_title(title).split():
        if w not in STOPWORDS:
            word = w
            break
    base = f"{last}{year or 'xxxx'}{word}"
    key, n = base, 0
    while key in used:
        n += 1
        key = base + chr(ord("a") + n - 1)
    used.add(key)
    return key


def detect_arxiv(*urls: str) -> str | None:
    for u in urls:
        if not u:
            continue
        m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", u)
        if m:
            return m.group(1)
    return None


def build_stub(bib: dict, urls: dict, key: str, today: str) -> str:
    title = (bib.get("title") or "").strip().rstrip(".")
    authors = format_authors(bib.get("author", ""))
    year = str(bib.get("pub_year", "")).strip()
    venue = (bib.get("journal") or bib.get("venue") or bib.get("citation") or "").strip()
    arxiv = detect_arxiv(urls.get("eprint_url", ""), urls.get("pub_url", ""))
    pub_url = urls.get("pub_url") or urls.get("eprint_url") or ""

    lines = [
        f"% AUTO-ADDED {today} from Google Scholar — REVIEW: venue/authors/keywords, add selected/preview/pdf if wanted",
        f"@article{{{key},",
        f"  title={{{title}}},",
        f"  author={{{authors}}},",
        f"  journal={{{venue}}},",
        f"  year={{{year}}},",
        "  keywords={submitted},",
        "  bibtex_show={true},",
    ]
    if arxiv:
        lines.append(f"  arxiv={{{arxiv}}},")
        lines.append(f"  url={{https://arxiv.org/abs/{arxiv}}}")
    elif pub_url:
        lines.append(f"  url={{{pub_url}}}")
    else:
        lines.append("  note={Add a url or arxiv id}")
    lines.append("}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Append new Google Scholar papers to papers.bib")
    ap.add_argument("--id", default=scholar_id_from_config(), help="Google Scholar user id")
    ap.add_argument("--dry-run", action="store_true", help="print new entries, write nothing")
    ap.add_argument("--since", type=int, default=None, metavar="YEAR",
                    help="only consider papers from YEAR onward (e.g. --since 2024)")
    args = ap.parse_args()

    if not args.id:
        print("No Scholar id (set scholar_userid in _config.yml or pass --id).", file=sys.stderr)
        return 2

    try:
        from scholarly import scholarly
    except ImportError:
        print("Missing dependency. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        return 2

    bibtext = BIB_PATH.read_text() if BIB_PATH.exists() else ""
    existing_keys, existing_titles = load_existing(bibtext)

    print(f"Fetching Scholar profile {args.id} …")
    try:
        author = scholarly.search_author_id(args.id)
        author = scholarly.fill(author, sections=["publications"])
    except Exception as exc:  # noqa: BLE001 — Scholar blocking surfaces here
        print(f"\nScholar fetch failed ({exc}).", file=sys.stderr)
        print("Scholar likely rate-limited this IP. Wait and retry, or use a proxy.", file=sys.stderr)
        return 1

    pubs = author.get("publications", [])
    print(f"  profile lists {len(pubs)} publications; checking which are new …")

    today = _dt.date.today().isoformat()
    used_keys = set(existing_keys)
    new_entries, skipped, skipped_year = [], 0, 0

    for pub in pubs:
        title = (pub.get("bib", {}).get("title") or "").strip()
        if not title or normalise_title(title) in existing_titles:
            skipped += 1
            continue
        # Cheap year filter before the expensive per-paper fetch, when year is already known.
        prelim_year = str(pub.get("bib", {}).get("pub_year", "")).strip()
        if args.since and prelim_year.isdigit() and int(prelim_year) < args.since:
            skipped_year += 1
            continue
        try:
            filled = scholarly.fill(pub)            # extra request — only for NEW papers
        except Exception as exc:  # noqa: BLE001
            print(f"  ! could not fill '{title[:50]}…' ({exc}); skipping", file=sys.stderr)
            continue
        bib = filled.get("bib", {})
        year = str(bib.get("pub_year", "")).strip()
        if args.since and year.isdigit() and int(year) < args.since:
            skipped_year += 1
            continue
        key = make_key(bib.get("author", ""), year, title, used_keys)
        urls = {"pub_url": filled.get("pub_url", ""), "eprint_url": filled.get("eprint_url", "")}
        new_entries.append(build_stub(bib, urls, key, today))
        existing_titles.add(normalise_title(title))
        print(f"  + NEW [{year or '????'}]: {title[:66]}")

    summary = f"{skipped} already in papers.bib"
    if args.since:
        summary += f", {skipped_year} older than {args.since}"
    if not new_entries:
        print(f"\nNothing to add. ({summary}.)")
        return 0
    print(f"\n{len(new_entries)} to add ({summary}).")

    block = "\n\n" + f"% ===== {len(new_entries)} new entr{'y' if len(new_entries)==1 else 'ies'} added {today} — review & tag =====" + "\n\n" + "\n\n".join(new_entries) + "\n"

    if args.dry_run:
        print("\n----- DRY RUN (not written) -----\n")
        print(block)
        return 0

    with BIB_PATH.open("a") as fh:
        fh.write(block)
    print(f"\nAppended {len(new_entries)} stub(s) to {BIB_PATH.relative_to(REPO_ROOT)}.")
    print("Next: review the diff, fix venue/authors/keywords, add selected/preview/pdf, then commit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
