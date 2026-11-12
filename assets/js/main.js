/* ==========================================================================
   Pillai Auto — Ather dealership website
   File: assets/js/main.js
   Version: V4
   Last updated: 12 November 2026 (V4: colour picker swaps responsive srcsets;
   home video loads on tablets/laptops only, still photo on phones.
   V3: image fallback tries data-alt backups)
   --------------------------------------------------------------------------
   No dependencies, no build step. Every module below is optional: if its
   markup is missing the module exits quietly, so this same file can be
   reused on the legal pages without throwing.
   JS only enhances — nothing on the page depends on it to be readable.
   ========================================================================== */
(function () {
  'use strict';

  var $  = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ----------------------------------------------------------------------
     0. Config — the only place that knows business details.
     ---------------------------------------------------------------------- */
  var CONFIG = {
    whatsapp: '918925815877',        // digits only, no + and no spaces
    phone:    '+918925815877'
  };

  /* ----------------------------------------------------------------------
     1. Helpers
     ---------------------------------------------------------------------- */
  function rupees(n) {
    return '₹' + Math.round(n).toLocaleString('en-IN');
  }

  function onView(el, cb, opts) {
    if (!('IntersectionObserver' in window)) { cb(el); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { cb(e.target); io.unobserve(e.target); }
      });
    }, opts || { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    io.observe(el);
  }

  /* ----------------------------------------------------------------------
     2. Mobile nav toggle
     ---------------------------------------------------------------------- */
  (function navToggle() {
    var btn  = $('.site-nav__toggle');
    var list = $('#nav-list');
    if (!btn || !list) return;

    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      list.classList.toggle('is-open', !open);
    });

    list.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        btn.setAttribute('aria-expanded', 'false');
        list.classList.remove('is-open');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && list.classList.contains('is-open')) {
        btn.setAttribute('aria-expanded', 'false');
        list.classList.remove('is-open');
        btn.focus();
      }
    });
  }());

  /* ----------------------------------------------------------------------
     3. Sub-nav scrollspy
     ---------------------------------------------------------------------- */
  (function scrollspy() {
    var links = $$('#subnav-links a');
    if (!links.length || !('IntersectionObserver' in window)) return;

    var map = {};
    var sections = [];
    links.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      var sec = document.getElementById(id);
      if (sec) { map[id] = a; sections.push(sec); }
    });
    if (!sections.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove('is-current'); a.removeAttribute('aria-current'); });
        var a = map[e.target.id];
        if (a) { a.classList.add('is-current'); a.setAttribute('aria-current', 'true'); }
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

    sections.forEach(function (s) { io.observe(s); });
  }());

  /* ----------------------------------------------------------------------
     4. Scroll reveal
     ---------------------------------------------------------------------- */
  (function reveal() {
    var items = $$('.reveal');
    if (!items.length) return;
    if (REDUCED || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    items.forEach(function (el) {
      onView(el, function (t) { t.classList.add('is-in'); });
    });
  }());

  /* ----------------------------------------------------------------------
     5. Animated stat counters
     ---------------------------------------------------------------------- */
  (function counters() {
    $$('[data-count]').forEach(function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var unit = el.querySelector('span');
      var suffix = unit ? unit.outerHTML : '';
      if (REDUCED) { el.innerHTML = target + suffix; return; }

      onView(el, function () {
        var start = null;
        var dur = 1100;
        function step(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.innerHTML = Math.round(target * eased) + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    });
  }());

  /* ----------------------------------------------------------------------
     6. Remote media failure fallback
     Every framed asset lives inside [data-media]. If the remote file is
     blocked or offline we show the striped placeholder instead of a
     broken-image icon.
     ---------------------------------------------------------------------- */
  (function mediaFallback() {
    function fail(node) {
      // V3: try the next backup image in data-alt="url1|url2" before giving up
      var alts = node.getAttribute && node.getAttribute('data-alt');
      if (alts) {
        var list = alts.split('|');
        var next = list.shift();
        if (list.length) node.setAttribute('data-alt', list.join('|'));
        else node.removeAttribute('data-alt');
        if (next) { node.src = next; return; }
      }
      var frame = node.closest('[data-media]');
      if (frame) frame.classList.add('has-error');
    }
    $$('[data-media] img').forEach(function (img) {
      img.addEventListener('error', function () { fail(img); });
      if (img.complete && img.naturalWidth === 0 && img.getAttribute('src')) fail(img);
    });
    $$('[data-media] video').forEach(function (v) {
      v.addEventListener('error', function () {
        // V4: if a still photo sits under the video, keep showing it
        var still = v.parentNode.querySelector('img');
        if (still && still.naturalWidth) { v.style.display = 'none'; return; }
        fail(v);
      }, true);
    });
  }());

  /* ----------------------------------------------------------------------
     7. Lazy videos — load only when scrolled into view, pause when out
     ---------------------------------------------------------------------- */
  (function lazyVideos() {
    var vids = $$('video[data-lazy-video]');
    if (!vids.length) return;

    function load(v) {
      if (v.dataset.loaded) return;
      v.src = v.dataset.src;
      v.dataset.loaded = '1';
      v.load();
    }

    if (!('IntersectionObserver' in window)) { vids.forEach(load); return; }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) {
          load(v);
          if (!REDUCED) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        } else if (!v.paused) {
          v.pause();
        }
      });
    }, { rootMargin: '200px 0px', threshold: 0.2 });

    vids.forEach(function (v) { io.observe(v); });
  }());

  /* ----------------------------------------------------------------------
     8. Hero video play / pause control
     ---------------------------------------------------------------------- */
  (function heroVideo() {
    var v = $('#hero-video');
    var btn = $('#hero-video-toggle');
    if (!v || !btn) return;

    var PAUSE_ICON = '<svg width="14" height="14" viewBox="0 0 14 14" fill="currentColor" aria-hidden="true"><rect x="2" y="1" width="3.4" height="12" rx="1"/><rect x="8.6" y="1" width="3.4" height="12" rx="1"/></svg>';
    var PLAY_ICON  = '<svg width="14" height="14" viewBox="0 0 14 14" fill="currentColor" aria-hidden="true"><path d="M3 1.6 12 7l-9 5.4Z"/></svg>';

    function sync() {
      var paused = v.paused;
      btn.innerHTML = paused ? PLAY_ICON : PAUSE_ICON;
      btn.setAttribute('aria-pressed', String(paused));
      btn.setAttribute('aria-label', paused ? 'Play background video' : 'Pause background video');
    }

    // V4: only fetch the video on wider screens without data-saver; phones keep the still photo
    var conn = navigator.connection || {};
    var minW = parseInt(v.dataset.minWidth || '0', 10);
    function load() {
      if (v.dataset.loaded || !v.dataset.src) return;
      v.src = v.dataset.src; v.dataset.loaded = '1'; v.load();
    }
    function start() { load(); var p = v.play(); if (p && p.catch) p.catch(function () {}); }
    v.addEventListener('playing', function () { v.classList.add('is-playing'); });
    if (!REDUCED && !conn.saveData && window.innerWidth >= minW) start();

    btn.addEventListener('click', function () {
      if (v.paused) { start(); }
      else { v.pause(); }
      sync();
    });
    v.addEventListener('play', sync);
    v.addEventListener('pause', sync);
    sync();
  }());

  /* ----------------------------------------------------------------------
     9. Generic tab controller (used by the dash and cruise sections)
     ---------------------------------------------------------------------- */
  function initTabs(listSel, onSelect) {
    var list = $(listSel);
    if (!list) return;
    var tabs = $$('.tab', list);

    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (onSelect) onSelect(tab);
    }

    tabs.forEach(function (t, i) {
      t.tabIndex = t.getAttribute('aria-selected') === 'true' ? 0 : -1;
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('keydown', function (e) {
        var next = null;
        if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
        if (e.key === 'ArrowLeft')  next = tabs[(i - 1 + tabs.length) % tabs.length];
        if (e.key === 'Home')       next = tabs[0];
        if (e.key === 'End')        next = tabs[tabs.length - 1];
        if (next) { e.preventDefault(); select(next); next.focus(); }
      });
    });
  }

  /* 9a. Dash of smarts — swap the dashboard screenshot */
  initTabs('#smart-tabs', function (tab) {
    var img = $('#dash-image');
    if (!img || !tab.dataset.img) return;
    var frame = img.closest('[data-media]');
    if (frame) frame.classList.remove('has-error');
    img.style.opacity = '0';
    var next = new Image();
    next.onload = function () {
      img.src = tab.dataset.img;
      img.alt = tab.dataset.alt || '';
      img.style.opacity = '1';
    };
    next.onerror = function () {
      img.style.opacity = '1';
      if (frame) frame.classList.add('has-error');
    };
    next.src = tab.dataset.img;
  });

  /* 9b. Cruise modes — swap the demo video */
  initTabs('#cruise-tabs', function (tab) {
    var v = $('#cruise-video');
    if (!v || !tab.dataset.video) return;
    var frame = v.closest('[data-media]');
    if (frame) frame.classList.remove('has-error');
    v.dataset.src = tab.dataset.video;
    v.src = tab.dataset.video;
    v.dataset.loaded = '1';
    v.load();
    if (!REDUCED) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  });

  /* ----------------------------------------------------------------------
     10. Traction-control mode pills — slow auto rotate
     ---------------------------------------------------------------------- */
  (function modePills() {
    var pills = $$('.mode-pill');
    if (pills.length < 2 || REDUCED) return;
    var i = 0;
    setInterval(function () {
      pills.forEach(function (p) { p.classList.remove('is-on'); });
      i = (i + 1) % pills.length;
      pills[i].classList.add('is-on');
    }, 2600);
  }());

  /* ----------------------------------------------------------------------
     11. Colour switcher
     Markup-driven: the swatch buttons are rendered server-side, each one
     carrying data-img and data-name. This just swaps the stage image.
     ---------------------------------------------------------------------- */
  (function colours() {
    var stage = $('[data-colour-stage]');
    var wrap = $('[data-colour-swatches]');
    if (!stage || !wrap) return;
    var img = $('img', stage);
    var buttons = $$('.swatch', wrap);
    if (!img || !buttons.length) return;

    var model = (document.querySelector('h1') || {}).textContent || 'Scooter';

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
        stage.classList.remove('has-error');
        img.classList.add('is-swapping');

        var source = $('source', stage);
        var pre = new Image();
        if (btn.dataset.srcset) { pre.sizes = img.sizes; pre.srcset = btn.dataset.srcset; }
        pre.onload = function () {
          // V4: swap the whole responsive set, phone version included
          if (btn.dataset.srcset) img.srcset = btn.dataset.srcset;
          if (source) {
            if (btn.dataset.srcsetM) source.srcset = btn.dataset.srcsetM;
            else source.removeAttribute('srcset');
          }
          img.src = btn.dataset.img;
          img.alt = model.trim() + ' in ' + btn.dataset.name;
          img.classList.remove('is-swapping');
        };
        pre.onerror = function () {
          img.classList.remove('is-swapping');
          stage.classList.add('has-error');
        };
        pre.src = btn.dataset.img;
      });
    });
  }());

  /* ----------------------------------------------------------------------
     12. Gallery — arrows plus lightbox
     ---------------------------------------------------------------------- */
  (function gallery() {
    var scroller = $('#gallery-scroller');
    if (!scroller) return;

    var items = $$('.gallery__item', scroller);
    var prev = $('#gal-prev'), next = $('#gal-next');

    function step(dir) {
      var w = scroller.firstElementChild ? scroller.firstElementChild.getBoundingClientRect().width + 16 : 400;
      scroller.scrollBy({ left: dir * w, behavior: REDUCED ? 'auto' : 'smooth' });
    }
    if (prev) prev.addEventListener('click', function () { step(-1); });
    if (next) next.addEventListener('click', function () { step(1); });

    var lb = $('#lightbox'), lbImg = $('#lightbox-img');
    if (!lb || !lbImg) return;
    var index = 0, lastFocus = null;

    function show(i) {
      index = (i + items.length) % items.length;
      var src = items[index].dataset.full;
      lbImg.src = src;
      lbImg.alt = ($('img', items[index]) || {}).alt || 'Ather 450 gallery image';
    }
    function open(i) {
      lastFocus = document.activeElement;
      show(i);
      lb.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      $('#lb-close').focus();
    }
    function close() {
      lb.classList.remove('is-open');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    }

    items.forEach(function (it, i) {
      it.addEventListener('click', function () { open(i); });
    });
    $('#lb-close').addEventListener('click', close);
    $('#lb-prev').addEventListener('click', function () { show(index - 1); });
    $('#lb-next').addEventListener('click', function () { show(index + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowRight') show(index + 1);
      if (e.key === 'ArrowLeft') show(index - 1);
    });
  }());

  /* ----------------------------------------------------------------------
     13. FAQ accordion
     ---------------------------------------------------------------------- */
  (function faq() {
    $$('.faq__q').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        var open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!open));
        if (panel) panel.hidden = open;
      });
    });
  }());

  /* ----------------------------------------------------------------------
     14. EMI calculator
     ---------------------------------------------------------------------- */
  (function emi() {
    var price  = $('#emi-price');
    if (!price) return;
    var down   = $('#emi-down');
    var tenure = $('#emi-tenure');
    var rate   = $('#emi-rate');

    function calc() {
      var P = +price.value;
      var D = Math.min(+down.value, P - 10000);
      if (+down.value > P - 10000) { down.value = D; }
      down.max = Math.max(0, P - 10000);

      var L = P - D;
      var n = +tenure.value;
      var r = (+rate.value) / 12 / 100;
      var emiVal = r > 0
        ? (L * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1)
        : L / n;
      var total = emiVal * n;

      $('#emi-price-out').textContent  = rupees(P);
      $('#emi-down-out').textContent   = rupees(D);
      $('#emi-tenure-out').textContent = n + ' months';
      $('#emi-rate-out').textContent   = (+rate.value).toFixed(2).replace(/\.00$/, '') + '%';

      $('#emi-out').innerHTML   = rupees(emiVal) + '<small>/mo</small>';
      $('#emi-loan').textContent     = rupees(L);
      $('#emi-interest').textContent = rupees(total - L);
      $('#emi-total').textContent    = rupees(total);

      var cta = $('#emi-cta');
      if (cta) {
        cta.dataset.emi = rupees(emiVal);
        cta.dataset.tenure = n;
      }
    }

    [price, down, tenure, rate].forEach(function (el) {
      el.addEventListener('input', calc);
    });

    var modelSel = $('#emi-model');
    if (modelSel) {
      modelSel.addEventListener('change', function () {
        var p = +modelSel.selectedOptions[0].dataset.price;
        if (!p) return;
        price.value = Math.min(Math.max(p, +price.min), +price.max);
        calc();
      });
      modelSel.dispatchEvent(new Event('change'));
    }

    calc();
  }());

  /* ----------------------------------------------------------------------
     15. Running-cost bars animate into view
     ---------------------------------------------------------------------- */
  (function costBars() {
    var wrap = $('#cost-bars');
    if (!wrap) return;
    onView(wrap, function () {
      $$('.cost-bar', wrap).forEach(function (bar, i) {
        var fill = $('.cost-bar__fill', bar);
        var pct = bar.dataset.pct || '0';
        setTimeout(function () { fill.style.width = pct + '%'; }, REDUCED ? 0 : i * 180);
      });
    });
  }());

  /* ----------------------------------------------------------------------
     16. Enquiry forms -> WhatsApp
     Any <form data-wa-form> is handled here. There is no backend: the form
     composes a click-to-chat message on the visitor's own device. Nothing is
     stored and nothing is sent until they press send in WhatsApp.

     Mark up a form like this:
       <form data-wa-form data-intro="I'd like to book a test ride.">
         <input name="Name" required data-label="Name">
         <input name="Phone" type="tel" data-phone required>
         <select name="Showroom" data-wa-select> ... <option data-wa="9188...">
     Every named control is appended to the message as "Label: value".
     A <select data-wa-select> also decides WHICH branch number receives it.
     ---------------------------------------------------------------------- */
  (function waForms() {
    var forms = $$('form[data-wa-form]');
    if (!forms.length) return;

    function setError(input, msg) {
      var holder = input.closest('.field') || input.parentNode;
      var existing = holder.querySelector('.field-error');
      if (existing) existing.remove();
      if (!msg) { input.removeAttribute('aria-invalid'); return; }
      var s = document.createElement('span');
      s.className = 'field-error';
      s.textContent = msg;
      holder.appendChild(s);
      input.setAttribute('aria-invalid', 'true');
    }

    function labelFor(el) {
      if (el.dataset.label) return el.dataset.label;
      var f = el.closest('.field');
      var span = f && f.querySelector('span');
      return (span ? span.textContent : el.name).replace(/\s*\*\s*$/, '').trim();
    }

    forms.forEach(function (form) {
      // Preselect a model/branch when arriving from a "?model=" style link
      var params = new URLSearchParams(window.location.search);
      ['model', 'branch', 'service'].forEach(function (key) {
        var val = params.get(key);
        if (!val) return;
        var sel = form.querySelector('select[name="' + key + '"], select[data-param="' + key + '"]');
        if (!sel) return;
        Array.prototype.forEach.call(sel.options, function (o) {
          if (o.value.toLowerCase() === val.toLowerCase()) sel.value = o.value;
        });
      });

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var status = form.querySelector('.form-status');
        var ok = true;
        var firstBad = null;

        // required text fields
        $$('[required]', form).forEach(function (el) {
          if (el.hasAttribute('data-phone')) return;
          if (!el.value.trim()) {
            setError(el, 'This field is required.');
            ok = false; firstBad = firstBad || el;
          } else setError(el, '');
        });

        // phone
        var phone = form.querySelector('[data-phone]');
        var digits = '';
        if (phone) {
          digits = phone.value.replace(/\D/g, '');
          if (!/^[6-9]\d{9}$/.test(digits)) {
            setError(phone, 'Enter a 10-digit Indian mobile number.');
            ok = false; firstBad = firstBad || phone;
          } else setError(phone, '');
        }

        if (!ok) {
          if (status) { status.dataset.state = 'error'; status.textContent = 'Please fix the highlighted fields.'; }
          if (firstBad) firstBad.focus();
          return;
        }

        var lines = ['Hi Pillai Auto, ' + (form.dataset.intro || 'I have an enquiry about an Ather scooter.'), ''];
        $$('input[name], select[name], textarea[name]', form).forEach(function (el) {
          if (el.type === 'hidden' && !el.value) return;
          var v = el.value.trim();
          if (!v) return;
          if (el.hasAttribute('data-phone')) v = '+91 ' + digits;
          lines.push(labelFor(el) + ': ' + v);
        });
        if (form.dataset.page) lines.push('Page: ' + form.dataset.page);

        // which branch gets it
        var number = CONFIG.whatsapp;
        var branchSel = form.querySelector('select[data-wa-select]');
        if (branchSel && branchSel.selectedOptions.length && branchSel.selectedOptions[0].dataset.wa) {
          number = branchSel.selectedOptions[0].dataset.wa;
        }

        var url = 'https://wa.me/' + number + '?text=' + encodeURIComponent(lines.join('\n'));
        if (status) {
          status.dataset.state = 'ok';
          status.textContent = 'Opening WhatsApp with your details… if nothing happens, call ' + CONFIG.phone + '.';
        }
        window.open(url, '_blank', 'noopener');
      });
    });

    // "Enquire — 450X" style links preselect the model on the target form
    $$('[data-prefill]').forEach(function (a) {
      a.addEventListener('click', function () {
        var sel = $('select[name="model"]');
        if (sel) {
          Array.prototype.forEach.call(sel.options, function (o) {
            if (o.value === a.dataset.prefill) sel.value = o.value;
          });
        }
      });
    });
  }());

  /* ----------------------------------------------------------------------
     17. Back to top
     ---------------------------------------------------------------------- */
  (function toTop() {
    var btn = $('#to-top');
    if (!btn) return;
    var ticking = false;

    function update() {
      btn.classList.toggle('is-visible', window.scrollY > window.innerHeight * 0.9);
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });

    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: REDUCED ? 'auto' : 'smooth' });
    });
    update();
  }());

  /* ----------------------------------------------------------------------
     18. Gentle parallax on tagged media
     ---------------------------------------------------------------------- */
  (function parallax() {
    var els = $$('[data-parallax]');
    if (!els.length || REDUCED) return;
    var ticking = false;

    function update() {
      var vh = window.innerHeight;
      els.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var img = el.querySelector('img');
        if (!img) return;
        var progress = (r.top + r.height / 2 - vh / 2) / vh;
        var amount = parseFloat(el.dataset.parallax) || 0.1;
        img.style.transform = 'translate3d(0,' + (-progress * amount * 100).toFixed(2) + 'px,0) scale(1.08)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }());

  /* ----------------------------------------------------------------------
     19. Nav dropdowns — one open at a time, close on outside click / Escape
     The markup is <details>, so with JS off every menu still opens and
     closes on its own. This only tidies the behaviour.
     ---------------------------------------------------------------------- */
  (function navMenus() {
    var menus = $$('.site-nav .menu');
    if (!menus.length) return;
    var desktop = function () { return window.innerWidth >= 900; };

    menus.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (!d.open || !desktop()) return;
        menus.forEach(function (o) { if (o !== d) o.open = false; });
      });
    });

    document.addEventListener('click', function (e) {
      if (!desktop()) return;
      menus.forEach(function (d) {
        if (d.open && !d.contains(e.target)) d.open = false;
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      menus.forEach(function (d) {
        if (d.open) { d.open = false; var s = d.querySelector('summary'); if (s) s.focus(); }
      });
    });
  }());

  /* ----------------------------------------------------------------------
     20. On-road price estimator (price-chennai.html)
     Rates are held in data attributes on the form so they can be corrected
     without touching this file.
     ---------------------------------------------------------------------- */
  (function onRoad() {
    var root = $('#onroad');
    if (!root) return;

    var model = $('#or-model');
    var out = {
      ex:   $('#or-ex'), rto: $('#or-rto'), ins: $('#or-ins'),
      acc:  $('#or-acc'), sub: $('#or-sub'), total: $('#or-total')
    };
    var accInput = $('#or-accessories');
    var accOut = $('#or-acc-out');

    function calc() {
      var opt = model.selectedOptions[0];
      var ex = +opt.dataset.price;
      var rtoRate = +root.dataset.rto || 0;      // fraction of ex-showroom
      var insRate = +root.dataset.ins || 0;
      var subsidy = +opt.dataset.subsidy || 0;
      var acc = +accInput.value;

      var rto = Math.round(ex * rtoRate);
      var ins = Math.round(ex * insRate);
      var total = ex + rto + ins + acc - subsidy;

      out.ex.textContent    = rupees(ex);
      out.rto.textContent   = rupees(rto);
      out.ins.textContent   = rupees(ins);
      out.acc.textContent   = rupees(acc);
      if (out.sub) out.sub.textContent = subsidy ? '− ' + rupees(subsidy) : '—';
      out.total.textContent = rupees(total);
      if (accOut) accOut.textContent = rupees(acc);

      var cta = $('#or-cta');
      if (cta) cta.textContent = 'Written quote — ' + opt.text.split(' — ')[0];
    }

    model.addEventListener('change', calc);
    accInput.addEventListener('input', calc);
    calc();
  }());

  /* ----------------------------------------------------------------------
     21. Launch countdown (Konarc)
     ---------------------------------------------------------------------- */
  (function countdown() {
    var el = $('#countdown');
    if (!el) return;
    var target = new Date(el.dataset.target).getTime();
    if (isNaN(target)) return;

    var units = [['days', 86400000], ['hours', 3600000], ['minutes', 60000]];

    function tick() {
      var diff = target - Date.now();
      if (diff <= 0) {
        el.innerHTML = '<p class="lede" style="margin:0 auto">The Konarc has launched. ' +
          'Call us on ' + CONFIG.phone + ' for prices and availability.</p>';
        return;
      }
      el.innerHTML = units.map(function (u) {
        var v = Math.floor(diff / u[1]);
        diff -= v * u[1];
        return '<div class="soon__unit"><b>' + v + '</b><span>' + u[0] + '</span></div>';
      }).join('');
    }
    tick();
    setInterval(tick, 30000);
  }());

  /* ----------------------------------------------------------------------
     22. Comparison table — highlight the column under the cursor
     ---------------------------------------------------------------------- */
  (function compareTable() {
    var table = $('.compare-table');
    if (!table) return;
    table.addEventListener('mouseover', function (e) {
      var cell = e.target.closest('td, th');
      if (!cell) return;
      var i = cell.cellIndex;
      $$('col', table).forEach(function (c, n) { c.classList.toggle('is-hot', n === i); });
    });
  }());

}());
