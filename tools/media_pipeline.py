#!/usr/bin/env python3
"""
media_pipeline.py  —  Version: V1  (12 Nov 2026)

Turns the downloaded Ather media library into responsive, self-hosted images
for the Pillai Auto site.

    python tools/media_pipeline.py --lib "D:\\Website\\downloaded_media\\atherenergy.com"
    python tools/build_site.py
    python tools/sync_partials.py

What it does
  1. Finds every https://media.atherenergy.com/<file> the site uses
     (tools/site_data.py, tools/build_site.py, partials/*.html).
  2. Matches each one to a file in the library (media_catalog.json, then by name).
  3. Writes WebP copies in several widths to assets/media/ — phones download a
     small one, laptops a large one (srcset).
  4. Finds the matching phone-shaped version (…-m.webp, …mob.webp, …Mob.webp)
     where Ather made one, so tall phone screens get a portrait crop.
  5. Makes tight 4:3 crops of the studio shots for the model cards, and trims
     empty transparent margins so cut-outs fill their frame.
  6. Writes assets/media/manifest.json. build_site.py reads it: anything listed
     there is served locally; anything not listed still loads from Ather.

Re-running is cheap: files that already exist are skipped (use --force to redo).
Needs: pip install pillow
"""
import argparse, json, os, re, sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "assets", "media")
MANIFEST = os.path.join(OUT_DIR, "manifest.json")
SCAN = ["tools/site_data.py", "tools/build_site.py", "partials/nav.html", "partials/footer.html"]
URL_RE = re.compile(r'(?:M\s*\+\s*"|\{M\}|https://media\.atherenergy\.com/)([^"\'\s<>]+?\.(?:webp|png|jpe?g|avif))', re.I)

QUALITY = 78
WIDTHS = {                       # widths generated per kind (capped at the source width)
    "full":   [480, 800, 1200, 1600, 2000],
    "mobile": [480, 720, 960, 1280],
    "card":   [400, 640, 800, 1200],
}

# Site file name -> library file name, where Ather's URL and the saved file differ.
ALIASES = {
    "rizta-red-super-matte (1).webp": "Rizta-Red-Super-Matte_(1).webp",
    "rizta-terracotta-red-duo-new-1.webp": "Ather-Rizta-Terracotta-Red-Dual-Sep15.webp",
}
# Desktop file -> phone file, where the names don't follow a pattern.
MOBILE = {
    "pdpkvdesktop.webp": "PDPKVMob.webp",
    "homepagekv.webp": "PDPKVMob.webp",
    "easy-on-ather-desktop.webp": None,
    "3-quartz-white-desk.webp": "4-Quartz-White-mob.webp",   # Ather numbered these two differently
    "4-majestic-grey-desk.webp": "3-Majestic-Grey-mob.webp",
}
# Card crops: fractions (left, top, right, bottom) for images whose background
# isn't plain enough to auto-trim. Everything else is trimmed automatically.
CARD_BOX = {
    "1-celestial-gold-desk.webp": (0.14, 0.06, 0.88, 0.99),
}
# Files used on model cards — they get a tight 4:3 crop as "<file>#card".
CARD_FILES_FROM_DATA = True


def key(name):
    return unquote(name).strip().lower()


def slug(name):
    base = os.path.splitext(unquote(name))[0]
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")


def find_used():
    used = set()
    for rel in SCAN:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            used |= {unquote(m) for m in URL_RE.findall(open(p, encoding="utf-8").read())}
    cards = set()
    if CARD_FILES_FROM_DATA:
        sys.path.insert(0, os.path.join(ROOT, "tools"))
        import site_data
        for m in site_data.MODELS:
            if m.get("card"):
                cards.add(unquote(m["card"].rsplit("/", 1)[-1]))
    return used, cards


def index_library(lib):
    by_name = {}
    cat_path = os.path.join(lib, "media_catalog.json")
    if os.path.exists(cat_path):
        for it in json.load(open(cat_path, encoding="utf-8")):
            rel = it["path"].replace("\\", "/").split("atherenergy.com/", 1)[-1]
            full = os.path.join(lib, rel)
            for u in it.get("urls", []):
                by_name.setdefault(key(u.rsplit("/", 1)[-1]), full)
            by_name.setdefault(key(it["file"]), full)
    for d, _, files in os.walk(os.path.join(lib, "images")):     # anything not in the catalogue
        for f in files:
            if not f.startswith(("thumbnail_", "small_", "medium_", "large_")):
                by_name.setdefault(key(f), os.path.join(d, f))
    return by_name


def openable(path):
    from PIL import Image
    try:
        with Image.open(path) as im:
            im.load()
        return True
    except Exception:
        return False


def mobile_candidates(name):
    n = unquote(name)
    stem, ext = os.path.splitext(n)
    c = []
    for a, b in (("-d", "-m"), ("-desk", "-mob"), ("-desktop", "-mobile"), ("Desktop", "Mob"), ("desk", "mob"), ("_desk", "_mob")):
        if stem.endswith(a):
            c.append(stem[: -len(a)] + b + ext)
    c += [stem + "-m" + ext, stem + "mob" + ext, stem + "-mob" + ext]
    return c


def find_mobile(name, lib_index):
    k = key(name)
    if k in MOBILE:
        m = MOBILE[k]
        return lib_index.get(key(m)) if m else None
    for cand in mobile_candidates(name):
        p = lib_index.get(key(cand))
        if p:
            return p
    return None


def card_crop(im, name):
    """Tight 4:3 crop around the scooter, padded with the backdrop colour."""
    from PIL import Image, ImageChops
    W, H = im.size
    box = CARD_BOX.get(key(name))
    if box:
        return im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bbox = im.getchannel("A").point(lambda v: 255 if v > 16 else 0).getbbox()   # the scooter's outline
    else:
        rgb = im.convert("RGB")
        bg = rgb.getpixel((3, 3))
        bbox = ImageChops.difference(rgb, Image.new("RGB", rgb.size, bg)).convert("L") \
                         .point(lambda v: 255 if v > 28 else 0).getbbox()
    if not bbox:
        return im
    x0, y0, x1, y1 = bbox
    cw, ch = (x1 - x0) * 1.14, (y1 - y0) * 1.14    # breathing room around the scooter
    if cw / ch > 4 / 3:
        ch = cw * 3 / 4
    else:
        cw = ch * 4 / 3
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2 - ch * 0.01
    L, T = int(cx - cw / 2), int(cy - ch / 2)
    canvas = studio_backdrop(int(cw), int(ch))
    if im.mode == "RGBA":
        canvas.paste(im, (-L, -T), im)              # alpha keeps the edges clean
    else:
        canvas.paste(im.convert("RGB"), (-L, -T))
    return canvas


def trim_transparent(im):
    """Cut-outs with wide empty margins: trim to the scooter so it fills its frame."""
    if im.mode not in ("RGBA", "LA", "P"):
        return im
    rgba = im.convert("RGBA")
    bbox = rgba.getchannel("A").point(lambda v: 255 if v > 16 else 0).getbbox()
    if not bbox:
        return im
    W, H = rgba.size
    x0, y0, x1, y1 = bbox
    if (x1 - x0) * (y1 - y0) > 0.75 * W * H:
        return im
    px, py = int((x1 - x0) * 0.06), int((y1 - y0) * 0.06)
    return rgba.crop((max(0, x0 - px), max(0, y0 - py), min(W, x1 + px), min(H, y1 + py)))


def studio_backdrop(w, h):
    """Light seamless-paper backdrop, same tones as the card frame in main.css."""
    from PIL import Image
    top, mid, floor = (241, 241, 239), (228, 228, 225), (238, 238, 236)
    col = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / max(1, h - 1)
        a, b, u = (top, mid, t / .72) if t < .72 else (mid, floor, (t - .72) / .28)
        col.putpixel((0, y), tuple(round(a[i] + (b[i] - a[i]) * u) for i in range(3)))
    return col.resize((w, h))


def write_variants(im, base, widths, force):
    from PIL import Image
    im = im.convert("RGBA") if im.mode in ("P", "LA") else im
    W, H = im.size
    ws = sorted({w for w in widths if w < W} | {min(W, max(widths))})
    out = []
    for w in ws:
        fn = f"{base}-{w}.webp"
        path = os.path.join(OUT_DIR, fn)
        if force or not os.path.exists(path):
            h = round(H * w / W)
            im.resize((w, h), Image.LANCZOS).save(path, "WEBP", quality=QUALITY, method=6)
        out.append((f"assets/media/{fn}", w))
    return {"w": W, "h": H, "variants": out}


def main():
    ap = argparse.ArgumentParser(description="Build responsive media for the Pillai Auto site")
    ap.add_argument("--lib", default=os.environ.get("PILLAI_MEDIA_LIB", r"D:\Website\downloaded_media\atherenergy.com"),
                    help="folder that holds media_catalog.json and images/")
    ap.add_argument("--force", action="store_true", help="regenerate files that already exist")
    args = ap.parse_args()
    if not os.path.isdir(os.path.join(args.lib, "images")):
        sys.exit(f"Media library not found at {args.lib} — pass --lib <folder>")
    from PIL import Image

    os.makedirs(OUT_DIR, exist_ok=True)
    lib = index_library(args.lib)
    used, cards = find_used()
    manifest, missing = {}, []

    for name in sorted(used | cards):
        k = key(name)
        src = lib.get(key(ALIASES.get(k, name)))
        if not src or not openable(src):
            missing.append(name)
            continue
        with Image.open(src) as im:
            entry = write_variants(trim_transparent(im), slug(name), WIDTHS["full"], args.force)
            if name in cards:
                crop = card_crop(im, name)
                manifest[k + "#card"] = write_variants(crop, slug(name) + "-card", WIDTHS["card"], args.force)
        mob = find_mobile(ALIASES.get(k, name), lib)
        if mob and openable(mob) and os.path.abspath(mob) != os.path.abspath(src):
            with Image.open(mob) as mi:
                entry["m"] = write_variants(mi, slug(os.path.basename(mob)) + "-mob", WIDTHS["mobile"], args.force)
        manifest[k] = entry

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, sort_keys=True)

    # remove files no longer used by any image (old picks, renamed sources)
    keep = {os.path.basename(p) for e in manifest.values() for p, _ in e["variants"] + (e.get("m") or {"variants": []})["variants"]}
    for fn in os.listdir(OUT_DIR):
        if fn.endswith(".webp") and fn not in keep:
            os.remove(os.path.join(OUT_DIR, fn))

    size = sum(os.path.getsize(os.path.join(OUT_DIR, f)) for f in os.listdir(OUT_DIR))
    print(f"{len(manifest)} images ready ({sum(1 for v in manifest.values() if v.get('m'))} with phone versions), "
          f"{len(os.listdir(OUT_DIR)) - 1} files, {size / 1e6:.1f} MB in assets/media")
    if missing:
        print("Still loading from Ather (not in the library or unreadable):")
        for n in missing:
            print("  -", n)


if __name__ == "__main__":
    main()
