# Pillai Auto — Ather dealership website

Static site. Plain HTML, CSS and JavaScript. No build step, no framework, no npm install.
Open `index.html` in a browser and it runs.

25 pages, built 22 August 2026 and updated 10 November 2026, for the four Pillai Auto showrooms:
**Chennai (OMR) · Chengalpattu · Puducherry · Chidambaram.**

Content is deliberately narrow: vehicles, prices, test rides, finance, service, charging,
accessories and showrooms. No corporate pages, no investor or press sections, no blog.

---

## File versions

| File | Version | What it is |
|---|---|---|
| `assets/css/main.css` | **V2** | The only stylesheet |
| `assets/js/main.js` | **V2** | The only script |
| `partials/head.html` | **V2** | Shared `<head>` block |
| `partials/nav.html` | **V3** | Offer strip + header nav with dropdowns |
| `partials/footer.html` | **V3** | Footer with all four branches |
| `tools/site_data.py` | **V2** | Branch and model data — the single source of truth |
| `tools/build_site.py` | **V2** | Generates every HTML page from that data |
| `tools/sync_partials.py` | **V1** | Injects the partials into every page |
| all 25 `*.html` pages | **V2** | Generated output — this is what you deploy |
| `robots.txt` | **V1** | Crawler rules |
| `sitemap.xml` | **V2** | Crawler file (lastmod 2026-11-10) |
| `assets/img/og-default.png` | **V2** | Social share card (1200×630) |
| `assets/img/favicon.svg` | **V1** | Tab icon |

Bump a version in the file's header comment and in this table when you change it.

---

## Pages

```
index.html                      Home — the line-up, why buy here, showrooms, FAQ
scooters/index.html             All models, grouped by family
scooters/ather-450-apex.html
scooters/ather-450x.html
scooters/ather-450s.html
scooters/ather-rizta-z.html
scooters/ather-rizta-s.html
scooters/ather-konarc.html      Launched — see the Konarc note below
compare.html                    All six side by side
price-chennai.html              On-road price estimator + ex-showroom table
emi-calculator.html             EMI sliders + running-cost comparison
test-ride.html                  Booking form
service.html                    Service booking form
charging.html                   Home charging and Ather Grid
accessories.html                Genuine Ather accessories
halo-smart-helmet.html          Halo and Halo Bit
locations/index.html            All four showrooms
locations/chennai-omr.html
locations/chengalpattu.html
locations/pondicherry.html
locations/chidambaram.html
contact.html
privacy.html   terms.html   404.html
```

---

## How the site is put together

Two scripts, both optional once the HTML exists.

**`tools/site_data.py`** holds every branch and every model — addresses, phone numbers,
prices, specs, colours and the Ather media URLs. Change a price there, not in ten files.

**`tools/build_site.py`** turns that data into the HTML:

```bash
python tools/build_site.py     # rewrites all 25 pages
```

**`tools/sync_partials.py`** pushes `partials/nav.html` and `partials/footer.html` into
every page, between the `<!-- @nav:start -->` markers:

```bash
python tools/sync_partials.py           # write
python tools/sync_partials.py --check   # report drift only
```

Run them in that order. Never hand-edit inside a marker block — the next sync overwrites it.

If you would rather not touch Python at all, edit the `.html` files directly and just
don't run the generator again. The HTML is the deliverable; the scripts are a convenience.

---

## Before this goes live

Search the project for `TODO(client)`.

1. **Branch addresses.** Taken from public Ather dealer listings. Check each against the
   matching Google Business Profile, byte for byte — a mismatch is a common cause of weak
   local ranking. They live in `tools/site_data.py`.
2. **Branch phone numbers.** All four currently show `+91 89258 15877`. If Chengalpattu,
   Puducherry and Chidambaram have their own numbers, put them in `site_data.py`
   (`phone_display`, `phone_e164`, `whatsapp`) — the enquiry forms route to whichever
   branch the visitor picks, so this matters.
3. **Email address.** `sales@pillaiauto.in` is a placeholder.
4. **Opening hours.** Currently Mon–Sat 9:30–19:30, Sun 10:00–18:00, the same for all four.
5. **Grievance officer** in `privacy.html` — a named person and a working email address are
   a statutory requirement under the DPDP Act, 2023.
6. **On-road rates.** `price-chennai.html` carries `data-rto="0.04"` and `data-ins="0.055"`
   on the `#onroad` form. These are placeholders. Set them to the figures you actually
   quote, including any Tamil Nadu EV road-tax concession, and check Puducherry separately —
   its rates differ.
7. **Prices.** All in `site_data.py`, indicative ex-showroom as of 10 November 2026.
   Ather does not publish a 450 Apex price online, so ₹1,94,946 is carried over from August — confirm it.
8. **The offer strip** in `partials/nav.html` — currently the Konarc launch; change it when the introductory price ends.
9. **Legal drafts.** `privacy.html` and `terms.html` are starting drafts, not legal advice.

---

## The Ather Konarc page

The Konarc has launched. As of 10 November 2026 the page is a normal model page built
from Ather's published specification sheet for the **Konarc S** (2.1 / 2.7 / 3.5 kWh), at
Ather's **introductory price of ₹99,999** ex-showroom. The Konarc Z (touchscreen, AeBS,
MagicKey) is listed by Ather as coming soon — add it to `site_data.py` when it is priced.

When the introductory price ends, change `price` for the Konarc in `tools/site_data.py`,
update the offer strip in `partials/nav.html`, and re-run the two scripts.

### What changed on 10 November 2026

- Konarc: launched — full specs, four colours with Ather images, home-page launch band,
  first on the scooters page, offer strip and menu label updated.
- 450 and Rizta: larger battery is now 3.5 kWh (was listed as 3.7); TrueRange added;
  charging times from Ather's current sheets; Infinite Cruise on 450X/Apex; SkidControl,
  Crash Alert and Tamil dashboard on Rizta Z.
- 450S corrected: 5.4 kW / 22 Nm, no traction control, no Magic Twist, 15 km in 10 min.
- Prices: 450X ₹1,48,998 (was ₹1,52,498), Rizta S ₹1,21,999 (was ₹1,21,499).
- Battery warranty everywhere: 3 yr / 30,000 km standard, extendable up to 10 yr /
  1,00,000 km (replaces "up to 8 years / Eight70").
- Images: Konarc assets added; 450X Hyper Sand and the 450S colour switcher now use
  the filenames on Ather's current 450 page.

## Images and video

All product photography and video loads live from Ather's own servers
(`https://media.atherenergy.com/...`). 36 distinct files, every one checked against a real
Ather page. Two consequences:

- The site needs an internet connection to show them. Offline, each frame falls back to a
  labelled placeholder rather than a broken-image icon.
- If Ather renames a file, that one frame goes to its placeholder. Nothing else breaks.

To move to your own photography, put files in `assets/img/` and change the URLs in
`tools/site_data.py` — that is where nearly all of them live.

Videos are lazy-loaded: nothing downloads until the section scrolls into view, and each
clip pauses when it scrolls out.

---

## Enquiry forms

There is no backend. Every form composes a WhatsApp message on the visitor's own device
and opens `wa.me`. Nothing is stored on the site and nothing is sent until they press send.

Each form has a **"Nearest showroom"** dropdown, and the message goes to that branch's
WhatsApp number — set per branch in `tools/site_data.py`. Links like
`test-ride.html?model=Ather+450X` preselect the model.

If you later want enquiries in an inbox or CRM, Formspree, Basin or Web3Forms drop in with
a single `action` attribute on the `<form>` element.

---

## Deploying to GitHub Pages

1. Push the contents of this folder to the root of a repo.
2. Settings → Pages → Source: `main` branch, `/ (root)`.
3. Keep `.nojekyll`. Without it, Pages runs Jekyll and can drop assets.
4. For the custom domain, add a `CNAME` file containing `www.pillaiauto.in` and point the
   DNS `CNAME` record at `<username>.github.io`.
5. Canonical URLs and `sitemap.xml` assume `https://www.pillaiauto.in/`. If the domain
   differs, change `BUSINESS["domain"]` in `site_data.py` and rebuild.

All asset paths are relative, so the site also works from a subfolder
(`username.github.io/reponame/`) without changes.

---

## SEO wiring already in place

- Unique title and meta description on all 25 pages, all within length limits.
- Canonical, Open Graph and Twitter card tags per page.
- `AutoDealer` JSON-LD on the home page with all four branches as `department` entries,
  plus a separate `AutoDealer` block on each showroom page carrying its own address, geo
  and hours — that is what earns separate local rankings for Chengalpattu, Puducherry
  and Chidambaram.
- `Product` JSON-LD with offers on every model page.
- `BreadcrumbList` JSON-LD and visible breadcrumbs on every inner page.
- `FAQPage` JSON-LD on the home page.
- `sitemap.xml` and `robots.txt`.

---

## Pre-launch checklist

- [ ] Every `TODO(client)` resolved
- [ ] Branch phone numbers real, and each one dials from a phone
- [ ] WhatsApp routing tested from each branch dropdown option
- [ ] On-road RTO and insurance rates set to your actual figures
- [ ] Prices current
- [x] Konarc page updated after launch (10 Nov 2026)
- [ ] Opened on a real phone, not just a resized desktop window
- [ ] Google Business Profile name, address and phone match each showroom page exactly
- [ ] `sitemap.xml` submitted in Google Search Console
- [ ] Social preview checked by pasting a URL into WhatsApp

---

## Accessibility

Skip link, visible focus rings, a real `<button>` hamburger with `aria-expanded`, native
`<details>` dropdowns that work with JavaScript off, an accordion that toggles
`aria-expanded` and `hidden`, `aria-current` on the active nav link, breadcrumbs in a
labelled `<nav>`, and `prefers-reduced-motion` honoured throughout — animations, counters,
autoplaying video and smooth scrolling all stand down.

Nothing needs JavaScript to be readable. Script failure costs the calculators and the
colour switcher, not the content.

Verified headless at 1440px and 390px across all 25 pages: no console errors, no page
errors, no horizontal overflow, exactly one `<h1>` per page.
