/* ==========================================================================
   GRUPUL VATRA · TORINO NORD — interacțiuni v4.0
   Fără dependențe. Dacă JavaScript-ul nu rulează, pagina rămâne completă:
   textele sunt vizibile, tabelul e întreg, galeria se vede normal.
   ========================================================================== */
(function () {
  'use strict';
  var root = document.querySelector('.vtn-page');
  if (!root || root.dataset.vtnReady === '1') return;
  root.dataset.vtnReady = '1';

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) root.classList.add('vtn-anim');

  /* --- 1. apariție la derulare ------------------------------------------ */
  var revealables = root.querySelectorAll('.vtn-rv');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('vtn-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    Array.prototype.forEach.call(revealables, function (el) { io.observe(el); });
  } else {
    Array.prototype.forEach.call(revealables, function (el) { el.classList.add('vtn-in'); });
  }

  /* --- 2. cifrele din hero, numărate ------------------------------------ */
  var counters = root.querySelectorAll('[data-vtn-count]');
  function runCounter(el) {
    var target = parseFloat(el.getAttribute('data-vtn-count'));
    var suffix = el.getAttribute('data-vtn-suffix') || '';
    var t0 = null, dur = 1100;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('ro-RO') + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if (!reduce && counters.length && 'IntersectionObserver' in window) {
    var ioc = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { runCounter(e.target); ioc.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    Array.prototype.forEach.call(counters, function (el) { ioc.observe(el); });
  }

  /* --- 3. bara de progres ------------------------------------------------ */
  var bar = root.querySelector('.vtn-progress i');
  var topBtn = root.querySelector('.vtn-top');
  var nav = root.querySelector('.vtn-nav');
  var navLinks = Array.prototype.slice.call(root.querySelectorAll('.vtn-nav a'));
  var sections = navLinks.map(function (a) { return root.querySelector(a.getAttribute('href')); });
  var ticking = false;

  function onScroll() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    var y = window.pageYOffset || h.scrollTop;
    if (bar) bar.style.width = (max > 0 ? (y / max) * 100 : 0) + '%';
    if (topBtn) topBtn.classList.toggle('vtn-show', y > 700);

    var offset = (nav ? nav.offsetHeight : 0) + 12;
    var active = -1;
    for (var i = 0; i < sections.length; i++) {
      var s = sections[i];
      if (s && s.getBoundingClientRect().top - offset <= 1) active = i;
    }
    navLinks.forEach(function (a, i) { a.classList.toggle('vtn-on', i === active); });
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  if (topBtn) topBtn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
  });

  /* --- 4. filtrarea cursurilor ------------------------------------------ */
  var courseBar = root.querySelector('[data-vtn-coursefilters]');
  if (courseBar) {
    var courseBtns = Array.prototype.slice.call(courseBar.querySelectorAll('.vtn-filter'));
    var courses = Array.prototype.slice.call(root.querySelectorAll('[data-vtn-audience]'));
    var courseCount = root.querySelector('[data-vtn-coursecount]');
    courseBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var want = btn.getAttribute('data-vtn-for');
        courseBtns.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle('vtn-on', on);
          b.setAttribute('aria-pressed', String(on));
        });
        var n = 0;
        courses.forEach(function (c) {
          var vis = want === 'toate' ||
            c.getAttribute('data-vtn-audience').split(' ').indexOf(want) > -1;
          c.hidden = !vis;
          if (vis) n++;
        });
        if (courseCount) {
          courseCount.textContent = n === 1 ? 'Un curs afișat.' : n + ' cursuri afișate.';
        }
      });
    });
  }

  /* --- 5. filtrarea orarului pe zile ------------------------------------ */
  var dayBar = root.querySelector('[data-vtn-dayfilters]');
  if (dayBar) {
    var dayBtns = Array.prototype.slice.call(dayBar.querySelectorAll('.vtn-filter'));
    var rows = Array.prototype.slice.call(root.querySelectorAll('[data-vtn-day]'));
    var heads = Array.prototype.slice.call(root.querySelectorAll('.vtn-row-head'));
    var dayCount = root.querySelector('[data-vtn-daycount]');
    dayBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var want = btn.getAttribute('data-vtn-for');
        dayBtns.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle('vtn-on', on);
          b.setAttribute('aria-pressed', String(on));
        });
        var n = 0;
        rows.forEach(function (r) {
          var vis = want === 'all' ||
            r.getAttribute('data-vtn-day').split(' ').indexOf(want) > -1;
          r.hidden = !vis;
          if (vis) n++;
        });
        heads.forEach(function (h) {
          h.hidden = want !== 'all' && h.getAttribute('data-vtn-head') !== want;
        });
        if (dayCount) {
          dayCount.textContent = n === 1 ? 'O grupă afișată.' : n + ' grupe afișate.';
        }
      });
    });
  }

  /* --- 6. galeria cu lupă ------------------------------------------------ */
  var lb = root.querySelector('.vtn-lb');
  if (lb) {
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('figcaption');
    var triggers = Array.prototype.slice.call(root.querySelectorAll('.vtn-lbbtn'));
    var current = 0, lastFocus = null;

    function show(i) {
      current = (i + triggers.length) % triggers.length;
      var t = triggers[current];
      lbImg.src = t.getAttribute('data-vtn-src');
      lbImg.alt = t.getAttribute('data-vtn-alt') || '';
      lbCap.textContent = t.getAttribute('data-vtn-cap') || '';
    }
    function open(i) {
      lastFocus = document.activeElement;
      show(i);
      lb.classList.add('vtn-open');
      lb.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.vtn-lb__close').focus();
    }
    function close() {
      lb.classList.remove('vtn-open');
      lb.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    }
    triggers.forEach(function (t, i) {
      t.addEventListener('click', function () { open(i); });
    });
    lb.querySelector('.vtn-lb__close').addEventListener('click', close);
    lb.querySelector('.vtn-lb__prev').addEventListener('click', function () { show(current - 1); });
    lb.querySelector('.vtn-lb__next').addEventListener('click', function () { show(current + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('vtn-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }

  /* --- 7. derulare lină către ancore, cu compensarea navigației ---------- */
  root.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#vtn-"]') : null;
    if (!a) return;
    var target = root.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    var offset = (nav ? nav.offsetHeight : 0) + 8;
    var y = target.getBoundingClientRect().top + window.pageYOffset - offset;
    window.scrollTo({ top: y, behavior: reduce ? 'auto' : 'smooth' });
  });
})();
