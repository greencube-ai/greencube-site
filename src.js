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
