/* "Can my PC run AI?" checker. Runs only in the browser: nothing about the PC is sent anywhere.
   pc_pages.py fills in D (the card list and every measured PC) when the blog is built, so every number shown here
   comes from blog-archive/data/pcs.json. A card we have not measured gets no speed of its own: we show the cards
   we did measure, and say so. */
(function () {
  var D = /*DATA*/null;
  var T = D.T;  // this language's words, from words/<lang>.json
  var U = D.U || ['s', 'min'];  // seconds and minutes, where a language abbreviates them differently
  // {x|one|few|many|other} picks the word form for the number in {x}, for languages whose words change with it
  function P(v) {
    var m = String(v).replace(/[  ]/g, '').match(/\d+(?:[.,]\d+)?/g);
    var ar = D.P === 'arabic';  // Arabic: one|two|few|many|other (1, 2, 3–10, 11–99, 100+ and fractions)
    if (!m || /[.,]/.test(m[m.length - 1])) return ar ? 4 : 3;
    var n = +m[m.length - 1];
    if (ar) return n === 1 ? 0 : n === 2 ? 1 : n % 100 >= 3 && n % 100 <= 10 ? 2 : n % 100 >= 11 ? 3 : 4;
    if (n % 10 === 1 && n % 100 !== 11) return 0;
    return n % 10 >= 2 && n % 10 <= 4 && !(n % 100 >= 12 && n % 100 <= 14) ? 1 : 2;
  }
  function F(k, o) {
    var s = D.P ? T[k].replace(/\{(\w+)\|([^{}]*)\}/g, function (_, x, w) { return w.split('|')[P(o[x])]; }) : T[k];
    return s.replace(/\{(\w+)\}/g, function (_, x) { return o[x]; });
  }
  var box = document.getElementById('chk');
  if (!box) return;
  var inp = document.getElementById('chk-in'), hits = document.getElementById('chk-hits'), noCard = document.getElementById('chk-none');
  var vbox = document.getElementById('chk-vram'), rbox = document.getElementById('chk-ram');
  var out = document.getElementById('chk-out'), det = document.getElementById('chk-detect');
  var cards = [];
  D.groups.forEach(function (g) { g.cards.forEach(function (c) { cards.push({ vendor: g.vendor, kind: g.kind, model: c[0], vrams: c[1] }); }); });
  var state = { card: null, vram: null, ram: null };
  function label(c) {  // the name people know: "NVIDIA GeForce RTX 3060", "AMD Radeon RX 6600", "RTX 4060 Laptop"
    if (c.kind === 'none') return D.builtin;
    if (c.model === 'other') return F('other_card', { v: c.vrams[0] });
    var m = c.kind === 'laptop' ? c.model.replace(' Laptop', T.laptop) : c.model;
    return { NVIDIA: 'NVIDIA GeForce ', AMD: 'AMD Radeon ', Intel: 'Intel ' }[c.vendor] + m;
  }
  function sizes(c) { return c.kind === 'none' ? '' : c.vrams.join(T.or) + ' ' + T.gb; }

  function n(x) { return String(x).replace('.', T.dec); }
  function rng(r, approx) { var s = r[0] === r[1] ? n(r[0]) : n(r[0]) + '–' + n(r[1]); return approx ? F('about', { x: s }) : s; }
  function secs(r) {
    var mm = function (t) { return Math.floor(t / 60) + ':' + ('0' + t % 60).slice(-2); };
    if (r[1] < 90) return r[0] === r[1] ? r[0] + ' ' + U[0] : r[0] + '–' + r[1] + ' ' + U[0];
    return r[0] === r[1] ? mm(r[0]) + ' ' + U[1] : mm(r[0]) + '–' + mm(r[1]) + ' ' + U[1];
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function a(m) { return '<a href="' + m.url + '">' + esc(m.name) + '</a>'; }
  function tag(m) { return m.test ? T.startup : ''; }
  function speed(m) { var s = rng(m.writes, m.approx); return s + (D.P ? T.tps.replace(/\{_\|([^{}]*)\}/, function (_, w) { return w.split('|')[P(s)]; }) : T.tps) + tag(m); }

  /* ---------- what the browser says the graphics are ---------- */
  function renderer() {
    try {
      var gl = document.createElement('canvas').getContext('webgl');
      if (!gl) return '';
      var ext = gl.getExtension('WEBGL_debug_renderer_info');
      return String(gl.getParameter(ext ? ext.UNMASKED_RENDERER_WEBGL : gl.RENDERER) || '');
    } catch (e) { return ''; }
  }
  function clean(r) {  // "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 (0x00002504) Direct3D11 vs_5_0 ps_5_0, D3D11)" -> "NVIDIA GeForce RTX 3060"
    var m = r.match(/ANGLE \([^,]*,\s*([^,]+?)(?:\s*\(0x[0-9a-f]+\))?(?:\s+Direct3D.*|\s+OpenGL.*|\s+Vulkan.*)?(?:,|\)$)/i);
    return (m ? m[1] : r).replace(/\((R|TM)\)/gi, '').replace(/\s+/g, ' ').trim();
  }
  function norm(s) { return ' ' + s.toLowerCase().replace(/geforce|radeon|nvidia|amd|\(r\)|\(tm\)|graphics/g, ' ').replace(/[^a-z0-9]+/g, ' ').trim() + ' '; }
  function match(name) {
    var t = norm(name), laptop = /laptop|mobile|max-q/i.test(name), best = -1, len = 0;
    cards.forEach(function (c, i) {
      if (c.kind === 'none') return;
      var k = norm(c.model.replace(' Laptop', ''));
      if (t.indexOf(k) >= 0 && (c.kind === 'laptop') === laptop && k.length > len) { best = i; len = k.length; }
    });
    return best;
  }
  /* ---------- picking: type to search, like the card finder on greencube.app ---------- */
  var found = [], cur = -1;
  function words(c) {  // what a search can match: the name, the vendor's other names, and the built-in chips
    var w = label(c) + ' ' + ({ NVIDIA: 'nvidia geforce', AMD: 'amd radeon', Intel: 'intel arc' }[c.vendor] || '');
    if (c.kind === 'none') w += ' intel iris xe uhd arc amd radeon vega built-in integrated integrada integrados none ninguna';
    if (c.kind === 'laptop') w += ' laptop portatil portátil notebook';
    return w.toLowerCase();
  }
  function search(q) {
    var t = q.toLowerCase().replace(/[^a-z0-9áéíóú]+/g, ' ').trim().split(' ').filter(Boolean);
    if (!t.length) return [];
    var wantLaptop = /laptop|port[aá]til|notebook/.test(q.toLowerCase());
    var r = [];
    cards.forEach(function (c, i) {
      if (c.model === 'other') return;
      var w = words(c), w2 = w.replace(/ /g, '');
      if (t.every(function (x) { return w.indexOf(x) >= 0 || w2.indexOf(x) >= 0; })) r.push(i);
    });
    // desktop or laptop as asked, then the closest name ("3060" before "3060 Ti"), then newest first
    r.sort(function (x, y) { return ((cards[x].kind === 'laptop') !== wantLaptop) - ((cards[y].kind === 'laptop') !== wantLaptop)
                                    || label(cards[x]).length - label(cards[y]).length || x - y; });
    return r.slice(0, 8);
  }
  function list(q) {
    found = search(q); cur = -1;
    if (!q.trim()) { hits.innerHTML = ''; }
    else if (found.length) {
      hits.innerHTML = found.map(function (i, k) {
        return '<button type="button" class="chk-hit" role="option" data-i="' + i + '"><span class="h-n">' + esc(label(cards[i])) + '</span><span class="h-v">' + sizes(cards[i]) + '</span></button>';
      }).join('');
    } else {
      hits.innerHTML = '<div class="chk-miss"><b>' + T.miss + '</b><div class="chk-sizes">'
        + [2, 4, 6, 8, 10, 12, 16, 20, 24].map(function (v) { return '<button type="button" data-other="' + v + '">' + v + ' ' + T.gb + '</button>'; }).join('') + '</div></div>';
    }
    inp.setAttribute('aria-expanded', hits.innerHTML ? 'true' : 'false');
  }
  inp.addEventListener('input', function () { list(inp.value); });
  inp.addEventListener('focus', function () { if (state.card && inp.value === label(state.card)) inp.select(); });
  inp.addEventListener('keydown', function (e) {
    var b = hits.querySelectorAll('.chk-hit');
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      if (!b.length) return;
      e.preventDefault();
      cur = (cur + (e.key === 'ArrowDown' ? 1 : -1) + b.length) % b.length;
      [].forEach.call(b, function (x, k) { x.classList.toggle('cursor', k === cur); });
    } else if (e.key === 'Enter') {
      if (found.length) { e.preventDefault(); choose(found[Math.max(cur, 0)]); }
    } else if (e.key === 'Escape') { hits.innerHTML = ''; inp.setAttribute('aria-expanded', 'false'); }
  });
  hits.addEventListener('click', function (e) {
    var b = e.target.closest('[data-i],[data-other]'); if (!b) return;
    if (b.getAttribute('data-other')) {
      cards.push({ vendor: '', kind: 'desktop', model: 'other', vrams: [+b.getAttribute('data-other')] });
      choose(cards.length - 1);
    } else choose(+b.getAttribute('data-i'));
  });
  document.addEventListener('click', function (e) { if (!e.target.closest || !e.target.closest('.chk-finder')) { hits.innerHTML = ''; inp.setAttribute('aria-expanded', 'false'); } });
  function chooseNone() { for (var i = 0; i < cards.length; i++) if (cards[i].kind === 'none') return choose(i); }
  noCard.addEventListener('click', chooseNone);
  function choose(i) {
    state.card = cards[i];
    inp.value = label(state.card);
    hits.innerHTML = ''; inp.setAttribute('aria-expanded', 'false');
    var v = state.card.vrams;
    state.vram = v.length === 1 ? v[0] : null;
    vbox.hidden = v.length === 1;
    vbox.querySelector('.chk-opts').innerHTML = v.map(function (x) { return '<button type="button" data-v="' + x + '">' + x + ' ' + T.gb + '</button>'; }).join('');
    show();
  }
  vbox.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    state.vram = +b.getAttribute('data-v'); show();
  });
  rbox.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    state.ram = +b.getAttribute('data-ram'); show();
  });
  function pressed() {
    [].forEach.call(vbox.querySelectorAll('button'), function (b) { b.setAttribute('aria-pressed', +b.getAttribute('data-v') === state.vram); });
    [].forEach.call(rbox.querySelectorAll('button'), function (b) { b.setAttribute('aria-pressed', +b.getAttribute('data-ram') === state.ram); });
    noCard.setAttribute('aria-pressed', !!state.card && state.card.kind === 'none');
  }

  /* ---------- the verdict, one row per thing you can do ---------- */
  function measured(c, v) {
    for (var k = 0; k < D.pcs.length; k++) { var m = D.pcs[k]; if (m.vendor === c.vendor && m.model === c.model && m.vram === v && c.kind === 'desktop') return m; }
    return null;
  }
  function peers(v) {  // measured desktop cards with the same memory, or the nearest sizes below and above
    var d = D.pcs.filter(function (m) { return m.kind === 'desktop'; });
    var same = d.filter(function (m) { return m.vram === v; });
    if (same.length) return { same: true, list: same };
    var lo = d.filter(function (m) { return m.vram < v; }).sort(function (x, y) { return y.vram - x.vram; })[0];
    var hi = d.filter(function (m) { return m.vram > v; }).sort(function (x, y) { return x.vram - y.vram; })[0];
    return { same: false, list: [lo, hi].filter(Boolean) };
  }
  function laptopFor(R) { return D.pcs.filter(function (m) { return m.kind === 'laptop'; }).sort(function (x, y) { return Math.abs(x.ram - R) - Math.abs(y.ram - R); })[0]; }

  function rows(c, v, R) {
    var E = D.engines, gpu = c.kind !== 'none' && v >= 4, out = [];
    var m = gpu ? measured(c, v) : null;
    var w = { v: v, e2b: E.e2b.name, e2bgb: n(E.e2b.gb), e4b: E.e4b.name, e4bgb: n(E.e4b.gb), floor: D.bigFloor };
    function f(k, o) { var x = {}, z; for (z in w) x[z] = w[z]; for (z in o || {}) x[z] = o[z]; return F(k, x); }
    // chat and study
    if (gpu && v >= 6) out.push(['yes', T.chat_h, f('chat_fits')]);
    else if (gpu) out.push(['part', T.chat_h, f('chat_part') + (R <= 8 ? T.chat_8gb : '')]);
    else if (R >= 16) out.push(['yes', T.chat_h, (c.kind !== 'none' ? f('chat_small_card') : T.chat_nocard) + f('chat_both')]);
    else out.push(['part', T.chat_h, f('chat_slow')]);
    // speed
    if (m) out.push(['yes', T.speed_m_h, f('speed_m', { name: esc(m.name), speed: speed(m), eng: m.engine, url: m.url })]);
    else if (gpu) {
      var p = peers(v);
      out.push(['maybe', T.speed_u_h, T.speed_u + (p.same ? f('speed_same') : T.speed_close)
        + p.list.map(function (x) { return a(x) + (p.same ? '' : ' (' + x.vram + ' ' + T.gb + ')') + (D.C || ', ') + speed(x); }).join(D.SC || '; ') + (D.ST || '. ')
        + f('speed_why', { url: D.method }) + (c.kind === 'laptop' ? T.speed_laptop : '')]);
    } else {
      var l = laptopFor(R);
      out.push(['maybe', T.speed_h, f('speed_lap', { link: a(l), ram: l.ram, speed: speed(l), eng: l.engine })]);
    }
    // the bigger AI
    var big = D.big, bh = f('big_h', { name: E['12b'].name }), bw = { gb: n(E['12b'].gb) };
    if (gpu && v >= D.bigFloor) out.push(['yes', bh, f('big_fits', bw)]);
    else if (gpu && v >= 8 && big) out.push(['part', bh, f('big_short', { link: a(big.pc), writes: rng(big.writes) })]);
    else out.push(['no', bh, f('big_no')]);
    // pictures
    var P = T.pic_h;
    if (m && m.pic) out.push(['yes', P, f(m.first ? 'pic_m_first' : 'pic_m', { name: esc(m.name), t: secs(m.pic), f: m.first })]);
    else if (!gpu && R <= 8) out.push(['no', P, T.pic_no8]);
    else if (R <= 8) out.push(['maybe', P, T.pic_maybe8]);
    else if (gpu && v >= 8 && D.pics8) out.push(['yes', P, f('pic_8', { n: D.pics8.n, lo: D.pics8.lo, hi: D.pics8.hi })]);
    else if (gpu && v >= 6 && D.pics6) out.push(['part', P, f('pic_6', { link: a(D.pics6.pc), t: secs(D.pics6.t) })]);
    else if (gpu) out.push(['maybe', P, f('pic_untimed')]);
    else if (D.picLaptop) out.push(['part', P, f('pic_laptop', { chip: secs(D.picLaptop.chip), cpu: secs(D.picLaptop.cpu) })]);
    return out;
  }

  var ICON = { yes: '✓', part: '~', no: '✗', maybe: '?' };
  function show() {
    pressed();
    if (!state.card || state.vram === null || !state.ram) {
      out.innerHTML = state.card && state.vram === null ? '<p class="chk-wait">' + T.wait_vram + '</p>'
                    : state.card && !state.ram ? '<p class="chk-wait">' + T.wait_ram + '</p>' : '';
      return;
    }
    var r = rows(state.card, state.vram, state.ram);
    out.innerHTML = '<p class="chk-head">' + T.head + '</p>'
      + '<ul class="chk-rows">' + r.map(function (x) {
          return '<li class="chk-' + x[0] + '"><span class="chk-ico" aria-hidden="true">' + ICON[x[0]] + '</span><div><h4>' + x[1] + '</h4><p>' + x[2].replace(/([。、！？：；）]) +/g, '$1') + '</p></div></li>';  // no space after Chinese or Japanese punctuation
        }).join('') + '</ul>'
      + '<p class="chk-send">' + T.send + '</p>';
  }
  var raw = renderer(), name = clean(raw), builtin = /intel|radeon\(tm\) graphics|radeon graphics|vega \d+ graphics|apple|mali|adreno/i;
  if (name) {
    var i = match(name);
    var vague = /or similar/i.test(raw);
    if (/apple/i.test(name)) {
      det.innerHTML = T.det_mac;
    } else if (i >= 0 && !vague) {
      det.innerHTML = F('det_found', { name: esc(name) });
      choose(i);
    } else if (builtin.test(name) && !vague && !/arc a|arc b/i.test(name)) {
      det.innerHTML = F('det_builtin', { name: esc(name) });
      chooseNone();
    } else {
      det.innerHTML = F('det_hidden', { said: name && !vague ? F('det_said', { name: esc(name) }) : '' });
    }
  } else {
    det.innerHTML = T.det_none;
  }

  show();
})();
