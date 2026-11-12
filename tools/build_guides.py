#!/usr/bin/env python3
"""
build_guides.py  —  Version: V1  (12 Nov 2026)

Builds the "Ather guides" section: guides/index.html (the hub) and one page per
entry in tools/guides_*.py. Called from build_site.py's main(), so the pages
share the site shell and land in sitemap.xml.

Content is written in a small markup (see render()):
    blank line            new paragraph
    ### Heading           sub-heading inside a section
    - item                bullet list            1. item   numbered list
    | a | b |             table row (first row = header)
    > text                highlighted note
    **bold**  [text](@guide-slug)  [text](/scooters/ather-450x.html)  [text](https://…)

Every guide gets: breadcrumb, Article + FAQPage + BreadcrumbList structured
data, a quick-facts panel, showroom contacts, related guides and a test-ride
call to action. check() fails the build on duplicate titles, over-long titles or
descriptions, thin pages, broken internal links, or near-duplicate pages.
"""
import html as H
import re

from build_site import page, crumbs, crumb_ld, cta_band, B, TEL, PHONE, WA, M
from site_data import BRANCHES, by_slug
from guides_index import GUIDES, CLUSTERS, by_guide

UPDATED = "2026-11-12"
UPDATED_TEXT = "12 November 2026"


# ---------------------------------------------------------------------------
# markup -> HTML
# ---------------------------------------------------------------------------
def _link(m):
    text, target = m.group(1), m.group(2)
    if target.startswith("@"):
        if target[1:] not in by_guide:
            raise ValueError(f"unknown guide link @{target[1:]}")
        return f'<a href="{{P}}guides/{target[1:]}.html">{text}</a>'
    if target.startswith("/"):
        return f'<a href="{{P}}{target[1:]}">{text}</a>'
    return f'<a href="{target}" target="_blank" rel="noopener">{text}</a>'


def inline(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, s)


def render(text):
    out, para, lst, ltype, rows = [], [], [], None, []

    def flush():
        nonlocal para, lst, ltype, rows
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
        if lst:
            out.append(f"<{ltype}>" + "".join(f"<li>{inline(i)}</li>" for i in lst) + f"</{ltype}>")
        if rows:
            head, body = rows[0], rows[1:]
            out.append('<div class="table-scroll"><table class="guide-table"><thead><tr>'
                       + "".join(f"<th scope=\"col\">{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(
                           (f'<th scope="row">{inline(c)}</th>' if i == 0 else f"<td>{inline(c)}</td>")
                           for i, c in enumerate(r)) + "</tr>" for r in body)
                       + "</tbody></table></div>")
        para, lst, ltype, rows = [], [], None, []

    for raw in text.strip().splitlines():
        line = raw.strip()
        if not line:
            flush(); continue
        if line.startswith("### "):
            flush(); out.append(f"<h3>{inline(line[4:])}</h3>"); continue
        if line.startswith("> "):
            flush(); out.append(f'<p class="guide-note">{inline(line[2:])}</p>'); continue
        if line.startswith("|"):
            if para or lst: flush()
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
            continue
        m = re.match(r"^(-|\d+\.)\s+(.*)", line)
        if m:
            t = "ul" if m.group(1) == "-" else "ol"
            if para or rows or (lst and ltype != t): flush()
            ltype = t; lst.append(m.group(2)); continue
        if lst or rows: flush()
        para.append(line)
    flush()
    return "\n".join(out)


def plain(text):
    t = re.sub(r"<[^>]+>", " ", render(text))
    return re.sub(r"\s+", " ", H.unescape(t)).strip()


def words(g):
    return len((plain(g["lede"]) + " " + " ".join(plain(b) for _, b in g["body"])
                + " " + " ".join(q + " " + a for q, a in g.get("faqs", []))).split())


# ---------------------------------------------------------------------------
# page parts
# ---------------------------------------------------------------------------
def _json(s):
    return H.unescape(re.sub(r"<[^>]+>", "", s)).replace("\\", "\\\\").replace('"', '\\"')


def faq_block(g):
    faqs = g.get("faqs", [])
    if not faqs:
        return "", ""
    items = "".join(f"""
        <div class="faq__item">
          <h3 style="font-size:inherit;margin:0">
            <button class="faq__q" type="button" aria-expanded="false" aria-controls="gfaq-a{i}" id="gfaq-q{i}">
              {q}<span class="faq__icon" aria-hidden="true"></span>
            </button>
          </h3>
          <div class="faq__a" id="gfaq-a{i}" role="region" aria-labelledby="gfaq-q{i}" hidden><div><p>{inline(a)}</p></div></div>
        </div>""" for i, (q, a) in enumerate(faqs, 1))
    html = f"""
      <div class="guide-faq">
        <h2>Questions we get asked</h2>
        <div class="faq">{items}
        </div>
      </div>"""
    ld = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
                  % (_json(q), _json(inline(a))) for q, a in faqs)
    return html, '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ld + "]}"


def aside(g):
    facts = ""
    if g.get("facts"):
        rows = "".join(f"<div><dt>{k}</dt><dd>{inline(v)}</dd></div>" for k, v in g["facts"])
        facts = f'<div class="guide-box"><h2 class="guide-box__title">Quick facts</h2><dl class="guide-facts">{rows}</dl></div>'
    models = ""
    if g.get("models"):
        links = "".join(f'<li><a href="{{P}}scooters/{s}.html">{by_slug(s)["name"]}</a></li>' for s in g["models"])
        models = f'<div class="guide-box"><h2 class="guide-box__title">Scooters in this guide</h2><ul class="guide-links">{links}</ul></div>'
    first = g["models"][0] if g.get("models") else None
    q = f'?model={by_slug(first)["name"].replace(" ", "+")}' if first else ""
    shops = "".join(
        f'<li><a href="{{P}}locations/{b["slug"]}.html">{b["short"]}</a>'
        f'<span><a href="tel:{b["phone_e164"]}">Call</a> · '
        f'<a href="https://wa.me/{b["whatsapp"]}" target="_blank" rel="noopener">WhatsApp</a></span></li>'
        for b in BRANCHES)
    talk = f"""<div class="guide-box guide-box--accent">
          <h2 class="guide-box__title">Ride one before you decide</h2>
          <p>Free test rides at all four Pillai Auto showrooms.</p>
          <a class="btn" href="{{P}}test-ride.html{q}">Book a test ride</a>
          <ul class="guide-shops">{shops}</ul>
        </div>"""
    return f'<aside class="guide__aside" aria-label="Quick facts and showrooms">{facts}{talk}{models}</aside>'


def related_block(g):
    rel = [by_guide[s] for s in g.get("related", []) if s in by_guide][:3]
    if not rel:
        return ""
    cards = "".join(f"""
        <a class="card guide-card" href="{{P}}guides/{r['slug']}.html">
          <span class="eyebrow">{CLUSTERS[r['cluster']]['label']}</span>
          <h3 class="card__title">{r['h1']}</h3>
          <p class="card__text">{plain(r['lede'])[:150].rsplit(' ', 1)[0]}&hellip;</p>
        </a>""" for r in rel)
    return f"""
      <div class="guide-related">
        <h2>Keep reading</h2>
        <div class="grid grid--3">{cards}
        </div>
        <p class="guide-hub-link"><a href="{{P}}guides/index.html">All Ather guides &rarr;</a></p>
      </div>"""


def build_guide(g):
    cl = CLUSTERS[g["cluster"]]
    cr = [("Home", "{P}index.html"), ("Ather guides", "{P}guides/index.html"), (g["h1"], None)]
    mins = max(2, round(words(g) / 220))
    sections = "".join(f'\n<section class="guide-sec"><h2 id="s{i}">{h}</h2>\n{render(b)}\n</section>'
                       for i, (h, b) in enumerate(g["body"], 1))
    toc = "".join(f'<li><a href="#s{i}">{h}</a></li>' for i, (h, _) in enumerate(g["body"], 1))
    img = ""
    if g.get("img"):
        img = f"""
      <div class="media guide__media reveal" data-media>
        <img src="{g['img']}" alt="{H.escape(g.get('img_alt', g['h1']))}" width="1600" height="900" loading="lazy" decoding="async">
        <div class="media__fallback">{g['h1']}</div>
      </div>"""
    faq_html, faq_ld = faq_block(g)
    article_ld = ('{"@context":"https://schema.org","@type":"Article","headline":"%s","description":"%s",'
                  '"datePublished":"%s","dateModified":"%s","inLanguage":"en-IN",'
                  '"author":{"@type":"Organization","name":"Pillai Auto","url":"%s"},'
                  '"publisher":{"@type":"Organization","name":"Pillai Auto","url":"%s"},'
                  '"mainEntityOfPage":"%s/guides/%s.html"}'
                  % (_json(g["h1"]), _json(g["desc"]), UPDATED, UPDATED, B["domain"], B["domain"], B["domain"], g["slug"]))
    head = (crumb_ld(cr, 1) + f'\n<script type="application/ld+json">{article_ld}</script>'
            + (f'\n<script type="application/ld+json">{faq_ld}</script>' if faq_ld else ""))

    body = f"""
  {crumbs(cr)}

  <section class="page-hero guide-hero">
    <div class="container">
      <span class="eyebrow">{cl['label']}</span>
      <h1>{g['h1']}</h1>
      <p class="lede">{inline(g['lede'])}</p>
      <p class="guide-meta">Updated {UPDATED_TEXT} &middot; {mins} min read &middot; Pillai Auto, authorised Ather dealer</p>
    </div>
  </section>

  <section class="band-light guide-band">
    <div class="container">{img}
      <div class="guide">
        <article class="prose">
          <nav class="guide-toc" aria-label="On this page"><h2 class="guide-toc__title">On this page</h2><ol>{toc}</ol></nav>
          {sections}
          {faq_html}
        </article>
        {aside(g)}
      </div>
      {related_block(g)}
    </div>
  </section>
{cta_band(g.get('cta_title', 'See it in person'), g.get('cta_text', 'Test ride any Ather at our Chennai OMR, Chengalpattu, Puducherry or Chidambaram showroom.'))}
"""
    page(f"guides/{g['slug']}.html", g["title"], g["desc"], body, head_extra=head,
         og_img=None, version="V1")


def build_hub():
    cr = [("Home", "{P}index.html"), ("Ather guides", None)]
    groups = ""
    for key, cl in CLUSTERS.items():
        items = [g for g in GUIDES if g["cluster"] == key]
        if not items:
            continue
        cards = "".join(f"""
          <a class="card guide-card" href="{{P}}guides/{g['slug']}.html">
            <h3 class="card__title">{g['h1']}</h3>
            <p class="card__text">{plain(g['lede'])[:140].rsplit(' ', 1)[0]}&hellip;</p>
          </a>""" for g in items)
        groups += f"""
    <section class="{'band-light' if cl.get('light') else ''}" id="{key}">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">{len(items)} guides</span>
          <h2>{cl['label']}</h2>
          <p class="lede">{cl['intro']}</p>
        </div>
        <div class="grid grid--3">{cards}
        </div>
      </div>
    </section>"""
    jump = " · ".join(f'<a href="#{k}">{c["label"]}</a>' for k, c in CLUSTERS.items())
    body = f"""
  {crumbs(cr)}
  <section class="page-hero">
    <div class="container">
      <span class="eyebrow">Ather guides</span>
      <h1>Ather guides for Chennai, Chengalpattu, Puducherry and Chidambaram</h1>
      <p class="lede">Straight answers from the Pillai Auto team on choosing, charging, owning and riding an Ather in our part of Tamil Nadu and Puducherry &mdash; {len(GUIDES)} guides, checked against Ather's own specifications.</p>
      <p class="guide-meta">{jump}</p>
    </div>
  </section>
{groups}
{cta_band("Still deciding?", "Ride two scooters back to back at any of our four showrooms.")}
"""
    page("guides/index.html", "Ather Scooter Guides — Chennai & Puducherry | Pillai Auto",
         f"{len(GUIDES)} guides on choosing, charging and owning an Ather scooter in Chennai, Chengalpattu, Puducherry and Chidambaram, from your authorised dealer.",
         body, head_extra=crumb_ld(cr, 1), version="V1")


# ---------------------------------------------------------------------------
# quality gate
# ---------------------------------------------------------------------------
def _shingles(text, n=5):
    w = re.findall(r"[a-z0-9]+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def check(min_words=300, max_sim=0.25):
    problems, seen_t, seen_d, seen_h = [], {}, {}, {}
    for g in GUIDES:
        s = g["slug"]
        for f in ("title", "desc", "h1"):
            store = {"title": seen_t, "desc": seen_d, "h1": seen_h}[f]
            if g[f] in store:
                problems.append(f"{s}: same {f} as {store[g[f]]}")
            store[g[f]] = s
        if len(g["title"]) > 65:
            problems.append(f"{s}: title {len(g['title'])} chars (keep ≤ 65)")
        if not 70 <= len(g["desc"]) <= 160:
            problems.append(f"{s}: description {len(g['desc'])} chars (70–160)")
        n = words(g)
        if n < min_words:
            problems.append(f"{s}: only {n} words")
        for r in g.get("related", []):
            if r not in by_guide:
                problems.append(f"{s}: related guide '{r}' does not exist")
        for m in g.get("models", []):
            by_slug(m)
        try:
            for _, b in g["body"]:
                render(b)
            for _, a in g.get("faqs", []):
                inline(a)
        except ValueError as e:
            problems.append(f"{s}: {e}")
    texts = {g["slug"]: _shingles(" ".join(plain(b) for _, b in g["body"])) for g in GUIDES}
    slugs = list(texts)
    worst = (0, "", "")
    for i, a in enumerate(slugs):
        for b in slugs[i + 1:]:
            A, Bb = texts[a], texts[b]
            sim = len(A & Bb) / max(1, min(len(A), len(Bb)))
            worst = max(worst, (sim, a, b))
            if sim > max_sim:
                problems.append(f"{a} and {b} overlap {sim:.0%} — rewrite one")
    return problems, worst


def build_all():
    problems, worst = check()
    if problems:
        raise SystemExit("Guide quality check failed:\n  " + "\n  ".join(problems))
    for g in GUIDES:
        build_guide(g)
    build_hub()
    total = sum(words(g) for g in GUIDES)
    print(f"guides: {len(GUIDES)} pages + hub, {total:,} words, "
          f"closest pair {worst[1]} / {worst[2]} at {worst[0]:.0%} overlap")
