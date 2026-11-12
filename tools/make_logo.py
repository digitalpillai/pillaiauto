#!/usr/bin/env python3
"""
make_logo.py  —  Version: V1  (12 Nov 2026)

Builds every logo file the site uses from the company logo image
(assets/brand/pillai-auto-logo-source.jpg). Run it again only if the logo
changes; the generated files are committed, so normal site builds don't need it.

    python tools/make_logo.py

Needs: Pillow, numpy, the `potrace` command (vector tracing) and Playwright
(for the social-preview image).

Writes
  assets/brand/logo-paths.json        traced vector paths (used by the partials)
  assets/img/logo-mark.svg            colour mark: black + green, transparent
  assets/img/logo-mark-on-dark.svg    for dark backgrounds: off-white + green
  assets/img/favicon.svg              browser tab icon (cream tile)
  assets/img/favicon-32.png, apple-touch-icon.png, icon-192.png, icon-512.png
  assets/img/og-default.png           1200 x 630 image used when pages are shared
  site.webmanifest                    home-screen icon details for Android
"""
import json, os, re, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "brand", "pillai-auto-logo-source.jpg")
IMG = os.path.join(ROOT, "assets", "img")
BRAND = os.path.join(ROOT, "assets", "brand")

GREEN = "#41F130"        # sampled from the logo
BLACK = "#000000"
CREAM = "#FCF1C9"        # the logo's background
ON_DARK = "#F2F4F5"      # site text colour on dark (--c-ink)
SITE_BG = "#08090A"      # site background (--c-bg)


def trace():
    import numpy as np
    from PIL import Image
    im = np.array(Image.open(SRC).convert("RGB")).astype(int)
    r, g, b = im[..., 0], im[..., 1], im[..., 2]
    masks = {"black": (r < 90) & (g < 90) & (b < 90),
             "green": (g > 150) & (r < 160) & (b < 120)}
    ys, xs = np.where(masks["black"] | masks["green"])
    x0, y0, x1, y1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
    H = im.shape[0]
    paths = {}
    with tempfile.TemporaryDirectory() as tmp:
        for name, m in masks.items():
            pbm, svg = os.path.join(tmp, name + ".pbm"), os.path.join(tmp, name + ".svg")
            Image.fromarray(np.where(m, 0, 255).astype("uint8")).save(pbm)
            subprocess.run(["potrace", pbm, "-s", "-o", svg, "--turdsize", "20",
                            "--alphamax", "1.0", "--opttolerance", "0.2", "-u", "1"], check=True)
            paths[name] = " ".join(re.findall(r'<path d="([^"]+)"', open(svg).read(), re.S)).replace("\n", " ")
    # potrace draws upside down (y up); the group transform below flips it back
    side = max(x1 - x0, y1 - y0)
    pad = round(side * 0.04)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = [round(cx - side / 2) - pad, round(cy - side / 2) - pad, side + 2 * pad, side + 2 * pad]
    return {"viewBox": " ".join(map(str, vb)), "flip": H, "black": paths["black"], "green": paths["green"]}


def svg(p, top, bottom=GREEN, bg=None, radius=0.22, size=None, label="Pillai Auto"):
    vb = list(map(float, p["viewBox"].split()))
    tile = ""
    if bg:
        r = vb[2] * radius
        tile = f'<rect x="{vb[0]}" y="{vb[1]}" width="{vb[2]}" height="{vb[3]}" rx="{r:.0f}" fill="{bg}"/>'
    wh = f' width="{size}" height="{size}"' if size else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{p["viewBox"]}"{wh} role="img" aria-label="{label}">'
            f'{tile}<g transform="translate(0 {p["flip"]}) scale(1 -1)">'
            f'<path fill="{top}" d="{p["black"]}"/><path fill="{bottom}" d="{p["green"]}"/></g></svg>')


def tile_svg(p, bg, scale=0.72):
    """Mark centred on a rounded square, smaller than the tile (for icons)."""
    vb = list(map(float, p["viewBox"].split()))
    s = vb[2]
    inner = s * scale
    off = (s - inner) / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s:.0f} {s:.0f}" role="img" aria-label="Pillai Auto">'
            f'<rect width="{s:.0f}" height="{s:.0f}" rx="{s * 0.22:.0f}" fill="{bg}"/>'
            f'<svg x="{off:.1f}" y="{off:.1f}" width="{inner:.1f}" height="{inner:.1f}" viewBox="{p["viewBox"]}">'
            f'<g transform="translate(0 {p["flip"]}) scale(1 -1)">'
            f'<path fill="{BLACK}" d="{p["black"]}"/><path fill="{GREEN}" d="{p["green"]}"/></g></svg></svg>')


def render_pngs(files):
    """files: [(svg_markup_or_html, out_path, w, h)] rendered with Playwright."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for markup, out, w, h in files:
            pg = b.new_page(viewport={"width": w, "height": h})
            html = markup if markup.lstrip().startswith("<!doctype") else \
                f'<!doctype html><html><body style="margin:0">{markup.replace("<svg ", f"<svg width={w} height={h} ", 1)}</body></html>'
            pg.set_content(html)
            pg.screenshot(path=out, omit_background=True)
            pg.close()
        b.close()


def og_html(p):
    mark = svg(p, ON_DARK)
    return f"""<!doctype html><html><head><style>
body{{margin:0;width:1200px;height:630px;background:{SITE_BG};font-family:Inter,sans-serif;color:{ON_DARK};
display:flex;align-items:center;gap:64px;padding:0 96px;box-sizing:border-box;overflow:hidden;position:relative}}
.m{{width:300px;height:300px;flex:none}} .m svg{{width:100%;height:100%}}
h1{{font-size:76px;letter-spacing:.02em;margin:0 0 14px;font-weight:700}}
p{{margin:0;font-size:30px;color:#9ba3ab;line-height:1.35}}
.k{{display:inline-block;margin-top:28px;padding:10px 20px;border-radius:999px;background:{GREEN};color:{SITE_BG};font-weight:700;font-size:24px}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:10px;background:{GREEN}}}
</style></head><body><div class="m">{mark}</div><div><h1>PILLAI AUTO</h1>
<p>Authorised Ather dealer<br>Chennai · Chengalpattu · Puducherry · Chidambaram</p>
<span class="k">Sales · Service · Test rides</span></div><div class="bar"></div></body></html>"""


def main():
    p = trace()
    with open(os.path.join(BRAND, "logo-paths.json"), "w") as f:
        json.dump(p, f)
    head = "<!-- {} — Version: V1 — generated by tools/make_logo.py from the Pillai Auto logo -->\n"
    out = {
        "logo-mark.svg": svg(p, BLACK),
        "logo-mark-on-dark.svg": svg(p, ON_DARK),
        "favicon.svg": tile_svg(p, CREAM, 0.8),
    }
    for fn, s in out.items():
        with open(os.path.join(IMG, fn), "w") as f:
            f.write(head.format("assets/img/" + fn) + s + "\n")
    icon = tile_svg(p, CREAM, 0.74)
    render_pngs([(tile_svg(p, CREAM, 0.86), os.path.join(IMG, "favicon-32.png"), 32, 32),
                 (icon, os.path.join(IMG, "apple-touch-icon.png"), 180, 180),
                 (icon, os.path.join(IMG, "icon-192.png"), 192, 192),
                 (icon, os.path.join(IMG, "icon-512.png"), 512, 512),
                 (og_html(p), os.path.join(IMG, "og-default.png"), 1200, 630)])
    manifest = {"name": "Pillai Auto — Authorised Ather Dealer", "short_name": "Pillai Auto",
                "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                          {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}],
                "theme_color": SITE_BG, "background_color": SITE_BG, "display": "browser", "start_url": "/"}
    with open(os.path.join(ROOT, "site.webmanifest"), "w") as f:
        json.dump(manifest, f, indent=2)
    print("logo files written; viewBox", p["viewBox"],
          f"; path data {len(p['black']) + len(p['green'])} chars")


if __name__ == "__main__":
    main()
