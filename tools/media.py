#!/usr/bin/env python3
"""
media.py  —  Version: V2  (12 Nov 2026: guide images sized for the article column)

Used by build_site.py. Rewrites every https://media.atherenergy.com/<file>
image in a finished page to the self-hosted responsive copies listed in
assets/media/manifest.json (made by tools/media_pipeline.py):

  * src  -> local file, plus srcset (several widths) and sizes, so a phone
            downloads a ~480 px image and a laptop a ~1600 px one
  * width/height set to the real proportions, so the page doesn't jump
  * <picture> with the phone-shaped version where Ather made one, for the
    full-width photos (model heroes, the Konarc banner, the colour picker)
  * colour-picker buttons get data-srcset / data-srcset-m for main.js
  * video posters and og:image switch to local copies

Anything not in the manifest is left exactly as it was (still loads from Ather).
"""
import json, os, re
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MANIFEST = None
PHONE = "(max-width: 767px)"

# How wide each kind of frame is on screen — tells the browser which file to fetch.
SIZES = {
    "card":      "(max-width: 700px) calc(100vw - 48px), (max-width: 1240px) calc(50vw - 48px), 400px",
    "card2":     "(max-width: 860px) calc(100vw - 48px), 600px",
    "full":      "(max-width: 1260px) calc(100vw - 32px), 1220px",
    "colours":   "(max-width: 940px) calc(100vw - 48px), 900px",
    "bleed":     "100vw",
    "guide":     "(max-width: 1260px) calc(100vw - 32px), 1220px",
}
# Context markers, nearest one before the <img> wins.
MARKERS = [
    ("model-card__media", "card"), ("card--media", "card"), ("model-hero", "full"),
    ("statement__media", "full"), ("colours__stage", "colours"), ("hero__media", "bleed"),
    ("media--wide", "card"), ("halo__media", "full"), ("guide__media", "guide"),
]
ART_DIRECTED = {"full", "colours", "bleed"}      # these get the phone-shaped version
EAGER = {"model-hero"}                            # above the fold: load first

IMG_RE = re.compile(r"<img\b[^>]*>", re.S)
REMOTE = "https://media.atherenergy.com/"


def manifest():
    global _MANIFEST
    if _MANIFEST is None:
        p = os.path.join(ROOT, "assets", "media", "manifest.json")
        _MANIFEST = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    return _MANIFEST


def _key(url):
    return unquote(url.rsplit("/", 1)[-1]).strip().lower()


def _srcset(entry, P):
    return ", ".join(f"{P}{path} {w}w" for path, w in entry["variants"])


def _default(entry, P, target=1200):
    best = min(entry["variants"], key=lambda v: abs(v[1] - target))
    return P + best[0]


def _context(html, pos):
    window = html[max(0, pos - 1600):pos]
    best, kind, marker = -1, "full", ""
    for m, k in MARKERS:
        i = window.rfind(m)
        if i > best:
            best, kind, marker = i, k, m
    if kind == "card" and window.rfind("grid--2") > window.rfind("grid--3"):
        kind = "card2"
    return kind, marker


def _attr(tag, name):
    m = re.search(rf'\s{name}="([^"]*)"', tag)
    return m.group(1) if m else None


def _set(tag, name, value):
    if value is None:
        return re.sub(rf'\s{name}="[^"]*"', "", tag)
    if re.search(rf'\s{name}="[^"]*"', tag):
        return re.sub(rf'(\s{name}=")[^"]*(")', lambda m: m.group(1) + value + m.group(2), tag)
    return tag[:-1].rstrip("/").rstrip() + f' {name}="{value}">'


def _rewrite_img(tag, html, pos, P, mf):
    src = _attr(tag, "src") or ""
    if not src.startswith(REMOTE):
        return tag
    kind, marker = _context(html, pos)
    k = _key(src)
    entry = mf.get(k + "#card") if kind in ("card", "card2") and "model-card" in marker else None
    entry = entry or mf.get(k)
    if not entry:
        return tag
    t = _set(tag, "src", _default(entry, P))
    t = _set(t, "srcset", _srcset(entry, P))
    t = _set(t, "sizes", SIZES[kind])
    t = _set(t, "width", str(entry["w"]))
    t = _set(t, "height", str(entry["h"]))
    t = _set(t, "data-alt", None)                 # local file is known-good; no remote backups needed
    if marker in EAGER:
        t = _set(t, "loading", "eager")
        t = _set(t, "fetchpriority", "high")
    mob = entry.get("m")
    if kind in ART_DIRECTED and mob:
        return (f'<picture><source media="{PHONE}" srcset="{_srcset(mob, P)}" sizes="100vw" '
                f'width="{mob["w"]}" height="{mob["h"]}">{t}</picture>')
    return t


def rewrite(html, P, domain):
    mf = manifest()
    if not mf:
        return html
    out, last = [], 0
    for m in IMG_RE.finditer(html):
        out.append(html[last:m.start()])
        out.append(_rewrite_img(m.group(0), html, m.start(), P, mf))
        last = m.end()
    out.append(html[last:])
    html = "".join(out)

    # colour-picker buttons: desktop + phone srcsets for main.js
    def swatch(m):
        tag, url = m.group(0), m.group(1)
        e = mf.get(_key(url))
        if not e:
            return tag
        tag = _set(tag, "data-img", _default(e, P))
        tag = _set(tag, "data-srcset", _srcset(e, P))
        if e.get("m"):
            tag = _set(tag, "data-srcset-m", _srcset(e["m"], P))
        return tag
    html = re.sub(r'<button\b[^>]*\sdata-img="(' + re.escape(REMOTE) + r'[^"]+)"[^>]*>', swatch, html)

    # video posters
    def poster(m):
        e = mf.get(_key(m.group(1)))
        return f'poster="{_default(e, P, 1600)}"' if e else m.group(0)
    html = re.sub(r'poster="(' + re.escape(REMOTE) + r'[^"]+)"', poster, html)

    # social preview image: absolute URL to our own copy
    def og(m):
        e = mf.get(_key(m.group(2)))
        return m.group(1) + domain + "/" + _default(e, "", 1200) + '"' if e else m.group(0)
    html = re.sub(r'(<meta (?:property|name)="(?:og|twitter):image" content=")(' + re.escape(REMOTE) + r'[^"]+)"', og, html)
    return html
