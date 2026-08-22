#!/usr/bin/env python3
"""
sync_partials.py  —  Version: V1  (Pillai Auto / Ather 450 site) - push partials/*.html into every page between marker comments.

Run from the project root:

    python tools/sync_partials.py
    python tools/sync_partials.py --check     # report drift, change nothing

Markers in each page look like:

    <!-- @nav:start -->
    ...replaced...
    <!-- @nav:end -->

Everything between the markers is regenerated. Never hand-edit inside a block.
Per-page <title>, description, canonical and OG tags sit OUTSIDE the markers
and are left untouched.

The script also:
  - rewrites relative asset paths by folder depth (services/ pages get ../)
  - marks the current page's nav link with aria-current and .is-active
  - reports pages that have no markers instead of silently skipping them
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTIALS = ROOT / "partials"
SKIP_DIRS = {"partials", "tools", ".git", "node_modules", "assets"}

# paths inside partials that need depth-aware rewriting
PATH_ATTR = re.compile(r'((?:href|src)=")(?!https?:|mailto:|tel:|#|/)([^"]+)(")')


def load_partials():
    found = {}
    for name in ("head", "nav", "footer"):
        path = PARTIALS / f"{name}.html"
        if path.exists():
            found[name] = path.read_text(encoding="utf-8").strip()
    if not found:
        sys.exit(f"No partials found in {PARTIALS}. Nothing to sync.")
    return found


def html_files():
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS:
            continue
        yield path


def reprefix(block: str, depth: int) -> str:
    """Prepend ../ per level of nesting to relative hrefs and srcs."""
    if depth == 0:
        return block
    prefix = "../" * depth
    return PATH_ATTR.sub(lambda m: f"{m.group(1)}{prefix}{m.group(2)}{m.group(3)}", block)


NAV_LIST = re.compile(r'(<ul[^>]*class="[^"]*site-nav__list[^"]*"[^>]*>)(.*?)(</ul>)', re.DOTALL)


def mark_active(nav: str, page: Path, depth: int) -> str:
    """Flag the nav link pointing at this page. Scoped to the link list so the
    logo and skip link are left alone."""
    rel = page.relative_to(ROOT).as_posix()
    target = ("../" * depth) + rel if depth else rel

    def flag(match):
        tag = match.group(0)
        if f'href="{target}"' not in tag:
            return tag
        if "aria-current" in tag:
            return tag
        tag = tag.replace("<a ", '<a aria-current="page" ', 1)
        if 'class="' in tag:
            tag = tag.replace('class="', 'class="is-active ', 1)
        else:
            tag = tag.replace("<a ", '<a class="is-active" ', 1)
        return tag

    def within_list(match):
        return match.group(1) + re.sub(r"<a\b[^>]*>", flag, match.group(2)) + match.group(3)

    if NAV_LIST.search(nav):
        return NAV_LIST.sub(within_list, nav)
    return re.sub(r"<a\b[^>]*>", flag, nav)


def sync(check_only=False):
    partials = load_partials()
    changed, skipped, missing = [], [], []

    for page in html_files():
        original = page.read_text(encoding="utf-8")
        text = original
        depth = len(page.relative_to(ROOT).parts) - 1
        hits = 0

        for name, raw in partials.items():
            pattern = re.compile(
                rf"(<!--\s*@{name}:start\s*-->)(.*?)(<!--\s*@{name}:end\s*-->)",
                re.DOTALL,
            )
            if not pattern.search(text):
                continue
            block = reprefix(raw, depth)
            if name == "nav":
                block = mark_active(block, page, depth)
            text = pattern.sub(
                lambda m: f"{m.group(1)}\n{block}\n  {m.group(3)}", text, count=1
            )
            hits += 1

        rel = page.relative_to(ROOT).as_posix()
        if hits == 0:
            missing.append(rel)
        elif text != original:
            changed.append(rel)
            if not check_only:
                page.write_text(text, encoding="utf-8")
        else:
            skipped.append(rel)

    verb = "would update" if check_only else "updated"
    print(f"{len(changed)} {verb}, {len(skipped)} already current, {len(missing)} without markers")
    for rel in changed:
        print(f"  ~ {rel}")
    for rel in missing:
        print(f"  ! no markers: {rel}")

    if check_only and changed:
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    sync(check_only=parser.parse_args().check)
