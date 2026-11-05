/* Magnetic buttons. When the mouse comes within 40 px of a button, the button leans toward it.
   Buy buttons (anything that leads to the buy page or checkout) lean up to 5 px sideways and 3 px up or down;
   every other button leans 60% as far. Mouse only, and off for anyone who asks their system for reduced motion.
   It moves buttons with the CSS `translate` property, so a button's own hover transform keeps working.
   Buy buttons also get --mx / --my, which a page can use to move the label a little further (see /get). */
(function () {
  if (!window.matchMedia || !matchMedia('(pointer: fine)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var R = 40, KX = 0.09, KY = 0.18, MAXX = 5, MAXY = 3, OTHER = 0.6;
  var SEL = 'button, [role="button"], .nav-cta, .buy-btn, .header-nav a, .lang, .scroll-cue, .cta-pill, .w-cta, .fit-cta, .dl-link, a[class*="btn"]';
  var buyPath = /^\/([a-z]{2}(-[a-z]{2})?\/)?(buy|get)\/?$/;

  function isBuy(el) {
    if (el.id === 'buy-btn' || el.classList.contains('buy-btn') || el.classList.contains('nav-cta') || el.classList.contains('fit-cta')) return true;
    var h = el.getAttribute('href');
    if (!h) return false;
    try {
      var u = new URL(h, location.href);
      return u.hostname === 'buy.stripe.com' || (u.hostname === location.hostname && buyPath.test(u.pathname));
    } catch (e) { return false; }
  }

  var items = [], seen = 0, mx = -1e4, my = -1e4, raf = 0;
  function collect() {
    var now = Date.now();
    if (now - seen < 1000) return;
    seen = now;
    var keep = [];
    [].forEach.call(document.querySelectorAll(SEL), function (el) {
      if (el.closest('[data-no-magnet]')) return;
      var p = el.parentElement && el.parentElement.closest(SEL);
      if (p) return;  // a button inside a button: only the outer one moves
      var old = null;
      for (var i = 0; i < items.length; i++) if (items[i].el === el) { old = items[i]; break; }
      keep.push(old || { el: el, k: isBuy(el) ? 1 : OTHER, buy: isBuy(el), x: 0, y: 0, tx: 0, ty: 0 });
    });
    items.forEach(function (it) { if (keep.indexOf(it) < 0) it.el.style.translate = ''; });
    items = keep;
  }
  function clamp(v, m) { return Math.max(-m, Math.min(m, v)); }

  function frame() {
    raf = 0;
    collect();
    var moving = false;
    for (var i = 0; i < items.length; i++) {
      var it = items[i], el = it.el, r = el.getBoundingClientRect();
      it.tx = it.ty = 0;
      if (r.width && !el.disabled && r.bottom > -R && r.top < innerHeight + R) {
        var dx = mx - (r.left + r.width / 2), dy = my - (r.top + r.height / 2);
        var out = Math.hypot(Math.max(0, Math.abs(dx) - r.width / 2), Math.max(0, Math.abs(dy) - r.height / 2));
        if (out <= R) { it.tx = clamp(dx * KX, MAXX) * it.k; it.ty = clamp(dy * KY, MAXY) * it.k; }
      }
      it.x += (it.tx - it.x) * 0.22;
      it.y += (it.ty - it.y) * 0.22;
      if (Math.abs(it.tx - it.x) < 0.02 && Math.abs(it.ty - it.y) < 0.02) { it.x = it.tx; it.y = it.ty; } else moving = true;
      el.style.translate = (it.x || it.y) ? it.x.toFixed(2) + 'px ' + it.y.toFixed(2) + 'px' : '';
      if (it.buy) { el.style.setProperty('--mx', it.x.toFixed(2) + 'px'); el.style.setProperty('--my', it.y.toFixed(2) + 'px'); }
    }
    if (moving) raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(frame); }
  addEventListener('pointermove', function (e) { mx = e.clientX; my = e.clientY; kick(); }, { passive: true });
  addEventListener('scroll', kick, { passive: true });
  document.documentElement.addEventListener('pointerleave', function () { mx = my = -1e4; kick(); });
})();
