/* Where a visitor came from, carried to the purchase, so we can tell which pages and which AI answers bring buyers.
   Nothing is stored on the device (no cookie, no localStorage): the source travels in the links themselves.
   - On arrival, the source is ?utm_source (ChatGPT adds utm_source=chatgpt.com), or ?src, or the site that linked here.
   - Every link to greencube.app or blog.greencube.app on the page gets ?src=…&lp=… (lp = the page they first landed on).
   - On /buy, the checkout button sends both to Stripe as client_reference_id, which shows on each payment.
   Values are only a site name and a path, never anything about the person. */
(function () {
  var ours = /(^|\.)greencube\.app$/;
  var p = new URLSearchParams(location.search);
  var src = p.get('src') || p.get('utm_source');
  if (!src && document.referrer) {
    try {
      var h = new URL(document.referrer).hostname.replace(/^www\./, '');
      if (!ours.test(h)) src = h;
    } catch (e) {}
  }
  if (!src) return;
  var clean = function (s, n) { return String(s).toLowerCase().replace(/[^a-z0-9./-]/g, '').slice(0, n); };
  src = clean(src, 40);
  var lp = clean(p.get('lp') || location.pathname, 80);
  window.GC_SRC = { src: src, lp: lp };
  function carry() {
    [].forEach.call(document.querySelectorAll('a[href]'), function (a) {
      try {
        var u = new URL(a.getAttribute('href'), location.href);
        if (!ours.test(u.hostname) || u.protocol.indexOf('http') !== 0) return;
        if (u.pathname === location.pathname && u.hostname === location.hostname) return;  // same-page anchors stay as they are
        u.searchParams.set('src', src);
        u.searchParams.set('lp', lp);
        a.setAttribute('href', u.toString());
      } catch (e) {}
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', carry); else carry();
})();

/* How far people read and what they try, counted the same cookie-free way as visits.
   Each moment below shows in Cloudflare Web Analytics as its own page: the page's address plus /~name
   (/~s50 = scrolled half the page, /es/buy/~click-download, ...). The address is swapped in and straight back with
   replaceState, the way /buy and /get count their steps, so Back, links and sharing are unchanged.
   Nothing is stored and nothing about the person is sent: only "this page, this moment", once per page view.
   - s25 s50 s75 s100: how far down the page they got
   - t30 t120: 30 s / 2 min with the page on screen
   - demo, demo-run, demo-chip-*, demo-open-*, demo-tab-*, demo-flip, demo-quiz, demo-style, demo-image, demo-follow, demo-save
   - click-buy, click-download, click-get, click-checkout: links they clicked (best effort, the next page may load first)
   Read them with ~/greencube-bench/gsc/cf_events.py. */
(function () {
  if (!window.history || !history.replaceState) return;
  var done = {}, queue = [], busy = true;  // held until Cloudflare's counter has loaded (below)
  function page() { return location.pathname.replace(/\/~[a-z0-9-]+$/, '').replace(/\/+$/, ''); }
  function flush() {
    if (busy || !queue.length) return;
    busy = true;
    var ev = queue.shift(), here = location.pathname + location.search + location.hash, st = history.state;
    try {
      history.replaceState(st, '', page() + '/~' + ev + location.search);
      history.replaceState(st, '', here);
    } catch (e) {}
    setTimeout(function () { busy = false; flush(); }, 1200);  // spaced out so the counter sees each one
  }
  function mark(ev) {
    ev = String(ev).toLowerCase().replace(/[^a-z0-9-]/g, '').slice(0, 40);
    if (!ev || done[ev]) return;
    done[ev] = 1; queue.push(ev); flush();
  }
  window.gcMark = mark;

  // how far down
  var steps = [25, 50, 75, 100], ticking = false;
  function depth() {
    ticking = false;
    var d = document.documentElement, h = Math.max(d.scrollHeight, document.body ? document.body.scrollHeight : 0);
    if (h < 1) return;
    var pct = (window.scrollY + window.innerHeight) / h * 100;
    for (var i = 0; i < steps.length; i++) if (pct >= (steps[i] === 100 ? 97 : steps[i])) mark('s' + steps[i]);
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(depth); } }, { passive: true });

  // time with the page on screen
  var seen = 0, clock = setInterval(function () {
    if (document.visibilityState !== 'visible') return;
    seen++;
    if (seen === 30) mark('t30');
    if (seen === 120) { mark('t120'); clearInterval(clock); }
  }, 1000);

  // what they click: the demo window and the links that matter
  document.addEventListener('click', function (e) {
    var t = e.target && e.target.closest ? e.target : null;
    if (!t) return;
    var demo = t.closest('#gd');
    if (demo) {
      mark('demo');
      var x;
      if ((x = t.closest('[data-job]'))) mark('demo-chip-' + x.getAttribute('data-job'));
      else if (t.closest('.gd-send, .gd-input')) mark('demo-run');
      else if ((x = t.closest('[data-tab]'))) mark('demo-tab-' + x.getAttribute('data-tab'));
      else if ((x = t.closest('[data-open]'))) mark('demo-open-' + x.getAttribute('data-open'));
      else if (t.closest('.fd-card, [data-fc]')) mark('demo-flip');
      else if (t.closest('.qz button')) mark('demo-quiz');
      else if (t.closest('[data-style], .gd-style')) mark('demo-style');
      else if (t.closest('[data-ipick], .gi-go, .gi-in')) mark('demo-image');
      else if (t.closest('[data-follow]')) mark('demo-follow');
      else if (t.closest('.gd-save')) mark('demo-save');
      return;
    }
    var a = t.closest('a[href]');
    if (!a) return;
    try {
      var u = new URL(a.getAttribute('href'), location.href), p = u.pathname.replace(/\/+$/, '');
      if (/(^|\.)stripe\.com$/.test(u.hostname)) mark('click-checkout');
      else if (/(^|\.)greencube\.app$/.test(u.hostname)) {
        if (/(^|\/)buy$/.test(p)) mark('click-buy');
        else if (/(^|\/)download$/.test(p)) mark('click-download');
        else if (/(^|\/)get(\/[ab])?$/.test(p)) mark('click-get');
      }
    } catch (e2) {}
  }, true);

  function start() { depth(); setTimeout(function () { busy = false; flush(); }, 3000); }
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);
})();
