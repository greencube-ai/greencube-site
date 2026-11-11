/* The clickable GreenCube window (/get and the home page, every language). No AI runs here: it replays example answers
   so a visitor can feel how the app works. Words come from demo/i18n/<lang>.json. Slides are the app's own drawings:
   every box, font and colour exported from the app's slide renderer in all 15 styles (demo/slides-<lang>.json).
   The pictures and the diagram are real GreenCube outputs. */
(() => {
  const root = document.getElementById('gd');
  if (!root) return;
  const LANGS = ['es', 'pt', 'fr', 'de', 'it', 'nl', 'pl', 'tr', 'ru', 'uk', 'ar', 'hi', 'id', 'vi', 'th', 'ja', 'ko', 'zh', 'zh-tw'];
  const seg = location.pathname.split('/')[1] || '', lang = LANGS.includes(seg) ? seg : 'en';
  const box = root.closest('.gd-home, .gd') || document;
  const $ = (s) => root.querySelector(s);
  const chat = $('.gd-chat'), input = $('.gd-input'), send = $('.gd-send'), chips = $('.gd-chips'), panel = $('.gd-panel');
  const pTitle = $('.gd-ph b'), pKind = $('.gd-ph small'), body = $('.gd-pb'), styleBtn = $('.gd-style'), styles = $('.gd-styles'), recents = $('.gd-recents');
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  const FONTS = { Georgia: 'Georgia,"Times New Roman",serif', Arial: 'Arial,Helvetica,sans-serif', 'Arial Black': '"Arial Black","Arial Bold",Arial,sans-serif',
    'Palatino Linotype': '"Palatino Linotype",Palatino,Georgia,serif', 'Trebuchet MS': '"Trebuchet MS","Segoe UI",sans-serif', Bahnschrift: 'Bahnschrift,"DIN Alternate","Segoe UI",sans-serif',
    'Segoe UI': '"Segoe UI",-apple-system,Arial,sans-serif', Consolas: 'Consolas,"SF Mono",Menlo,monospace', 'Ink Free': '"Ink Free","Segoe Print","Bradley Hand","Comic Sans MS",cursive',
    'Segoe Print': '"Segoe Print","Bradley Hand","Comic Sans MS",cursive', Impact: 'Impact,"Arial Black",sans-serif', 'Bahnschrift Condensed': '"Bahnschrift Condensed","Arial Narrow",sans-serif' };
  const PW = 10, PH = 5.625, pt = (n) => `calc(${n} * 100cqw / 720)`, X = (n) => (n / PW * 100) + '%', Y = (n) => (n / PH * 100) + '%';

  // one slide, drawn from the app's exported scene exactly like the app's own slide view
  function scene(sc, cls) {
    let h = '<div class="scn' + (cls ? ' ' + cls : '') + '" style="background:#' + sc.bg + '">';
    for (const i of sc.it) {
      const b = 'left:' + X(i.x) + ';top:' + Y(i.y) + ';width:' + X(i.w) + ';height:' + Y(i.h) + ';' + (i.rotate ? 'transform:rotate(' + i.rotate + 'deg);' : '');
      if (i.k !== 't') {
        h += '<span style="' + b + 'background:' + (i.fill ? '#' + i.fill : 'transparent') + ';opacity:' + (i.opacity ?? 1) + ';border-radius:' +
          (i.k === 'e' ? '50%' : i.radius ? pt(i.radius * 72) : '0') + ';' + (i.ol ? 'box-shadow:inset 0 0 0 ' + pt(i.ol[0]) + ' #' + i.ol[1] + ';' : '') + '"></span>';
        continue;
      }
      const lines = (i.l || []).filter((x) => x.trim());
      h += '<div style="' + b + 'display:flex;flex-direction:column;justify-content:' + (i.valign === 'middle' ? 'center' : i.valign === 'bottom' ? 'flex-end' : 'flex-start') +
        ';font-family:' + (FONTS[i.font] || i.font).replace(/"/g, "'") + ';font-size:' + pt(i.size) + ';font-weight:' + (i.bold ? 700 : 400) + ';font-style:' + (i.italic ? 'italic' : 'normal') +
        ';color:#' + i.color + ';text-align:' + (i.align || 'left') + ';' + (i.spacing ? 'letter-spacing:' + pt(i.spacing) + ';' : '') + 'line-height:' + 1.2 * (i.lineSpacing || 1) + ';overflow-wrap:break-word">';
      lines.forEach((ln, n) => {
        h += '<div style="' + (n < lines.length - 1 && i.gap ? 'margin-bottom:' + pt(i.gap) + ';' : '') + (i.bullet ? 'padding-left:' + pt(i.size * 1.4) + ';text-indent:calc(-1 * ' + pt(i.size * 1.4) + ');' : '') + '">' +
          (i.bullet ? '<span style="display:inline-block;width:' + pt(i.size * 1.4) + ';text-indent:0">' + esc(i.bullet) + '</span>' : '') + esc(ln) + '</div>';
      });
      h += '</div>';
    }
    return h + '</div>';
  }

  let T = null, U = null, JOBS = null;
  const ICON = { slides: '🖼️', quiz: '❓', cards: '🃏' }, IMG_FILES = ['09', '01', '02', '03', '05', '08', '10', '12'];
  let picked = false, busy = false, job = 'slides', style = 'comic', deckName = 'full', theme = 'wisteria', started = false, typer = null, data = null, ready = null;
  const loadData = () => data || (data = fetch('/demo/slides-' + lang + '.json').then((r) => r.json()));
  const deck = async () => (await loadData()).decks[deckName + '|' + theme + '|' + style] || [];

  function typeInto(text) {
    clearInterval(typer); let i = 0; input.classList.remove('ph');
    typer = setInterval(() => { i++; input.innerHTML = esc(text.slice(0, i)) + '<span class="cur"></span>'; if (i >= text.length) clearInterval(typer); }, 24);
  }
  function choose(k) { job = k; chips.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.job === k))); typeInto(T.jobs[k].prompt); }
  function bubble(cls, html) { const d = document.createElement('div'); d.className = 'gd-msg ' + cls; d.innerHTML = html; chat.appendChild(d); chat.scrollTop = chat.scrollHeight; return d; }
  async function reply(html, ms) {
    const d = bubble('a', '<span class="gd-dots"><i></i><i></i><i></i></span>');
    await wait(ms || 1100); d.innerHTML = html; chat.scrollTop = chat.scrollHeight; return d;
  }
  const FOLLOW_IDS = ['short', 'night', 'chalkboard'];
  function followChips() {
    const used = root.dataset.used || '', list = FOLLOW_IDS.map((v, i) => [T.jobs.slides.follow[i], v]).filter(([, v]) => !used.includes(v));
    if (!list.length) return;
    const f = document.createElement('div'); f.className = 'gd-follow';
    f.innerHTML = list.map(([t, v]) => '<button type="button" data-follow="' + v + '">' + esc(t) + '</button>').join('');
    chat.appendChild(f); chat.scrollTop = chat.scrollHeight;
  }
  const cardHtml = (k) => '<button class="gd-card" type="button" data-open="' + k + '"><span class="ic" aria-hidden="true">' + ICON[k] + '</span><span><small>' + esc(U.kinds[k]) + '</small><b>' + esc(T.jobs[k].title) +
    '</b><em>' + esc(U.metas[k]) + '</em></span><span class="open">' + esc(U.open) + '</span></button><div class="gd-note">' + esc(U.ai_note) + '</div>';

  async function run(k) {
    if (busy) return; busy = true; send.disabled = true; picked = false;
    root.querySelector('.gd-click')?.remove();
    if (!started) { started = true; const h = $('.gd-hello'); if (h) h.remove(); }
    const J = T.jobs[k];
    bubble('u', '<span>' + esc(J.prompt) + '</span>');
    input.innerHTML = esc(U.placeholder); input.classList.add('ph'); clearInterval(typer);
    const r = document.createElement('div'); r.className = 'gd-r on'; r.textContent = J.recent; r.dataset.done = k;
    recents.querySelectorAll('.gd-r').forEach((x) => x.classList.remove('on')); recents.prepend(r);
    showView('chat'); addArt(k);
    if (k === 'slides') { deckName = 'full'; theme = 'wisteria'; style = 'comic'; delete root.dataset.used; await loadData(); }
    if (k === 'diagram') {
      await reply('<div>' + esc(J.intro) + '</div><ul class="gd-ul">' + J.parts.map(([a, b]) => '<li><b>' + esc(a) + ':</b> ' + esc(b) + '</li>').join('') + '</ul>' +
        '<figure class="gd-fig"><img src="/demo/plant-cell.webp" width="782" height="478" alt="' + esc(J.alt) + '" loading="lazy"/><figcaption>' + esc(J.caption) + '</figcaption></figure>', 1300);
    } else {
      await reply('<div>' + esc(J.say) + '</div>' + cardHtml(k));
      await open(k);
    }
    if (k === 'slides') followChips();
    busy = false; send.disabled = false;
    const next = JOBS.find((x) => !root.querySelector('.gd-r[data-done="' + x + '"]'));
    if (next) setTimeout(() => { if (!busy && !picked) choose(next); }, 900);
  }
  async function follow(v, btn) {
    if (busy) return; busy = true; btn.parentElement.remove();
    bubble('u', '<span>' + esc(btn.textContent) + '</span>');
    const S = T.jobs.slides;
    if (v === 'short') { deckName = 'short'; await reply(esc(S.reply_short)); }
    else if (v === 'night') { theme = 'night'; await reply(esc(S.reply_night)); }
    else { style = v; await reply(S.reply_chalk.split(/(<b>|<\/b>)/).map((x) => (x === '<b>' || x === '</b>') ? x : esc(x)).join('')); }
    await open('slides');
    root.dataset.used = (root.dataset.used || '') + ' ' + v;
    followChips();
    busy = false;
  }
  async function stylePicker() {
    const d = await loadData(), moods = ['Clean', 'Bold', 'Fun', 'School', 'Dark'];
    styles.innerHTML = moods.map((m) => '<div class="gd-mood"><small>' + esc(U.moods[m]) + '</small><div class="gd-looks">' + d.styles.filter((s) => s[2] === m).map(([id]) =>
      '<button type="button" data-style="' + id + '" class="gd-look' + (id === style ? ' on' : '') + '">' + scene((d.decks[deckName + '|' + theme + '|' + id] || [])[0] || { bg: 'fff', it: [] }) + '<span>' + esc(U.style_names[id] || id) + '</span></button>').join('') + '</div></div>').join('');
  }
  async function open(k) {
    panel.classList.add('on'); styles.classList.remove('on');
    styleBtn.hidden = k !== 'slides'; $('.gd-save').hidden = k !== 'slides';
    pKind.textContent = U.kinds[k]; pTitle.textContent = T.jobs[k].title;
    if (k === 'slides') body.innerHTML = (await deck()).map((sc) => scene(sc)).join('');
    else if (k === 'quiz') body.innerHTML = '<div class="qz-score">' + esc(U.quiz_start) + '</div>' + T.quiz.map((q, i) => '<div class="qz" data-q="' + i + '"><p>' + (i + 1) + '. ' + esc(q.q) + '</p>' +
      q.o.map((o, j) => '<button type="button" data-a="' + j + '"><i>' + 'ABCD'[j] + '</i>' + esc(o) + '</button>').join('') + '</div>').join('');
    else if (k === 'cards') { fc = { at: 0, flip: false, order: T.cards.map((_, i) => i) }; fcRender(); }
    body.scrollTop = 0;
  }

  // flashcards: one card at a time, question on the page colour, answer on the cover colour, like the app
  let fc = { at: 0, flip: false, order: [0, 1, 2, 3, 4] };
  function fcRender() {
    const n = T.cards.length, [f, b] = T.cards[fc.order[fc.at]], size = (t) => t.length <= 40 ? 'xl' : t.length <= 90 ? 'l' : 'm';
    body.innerHTML = '<div class="fd"><div class="fd-card' + (fc.flip ? ' flip' : '') + '" role="button" tabindex="0" aria-label="' + esc(U.fc_flip) + '"><div class="fd-in">' +
      '<div class="fd-f"><i></i><div class="fd-top"><span>' + esc(U.fc_question) + '</span><span>' + (fc.at + 1) + ' / ' + n + '</span></div><div class="fd-txt ' + size(f) + '">' + esc(f) + '</div><div class="fd-hint">' + esc(U.fc_hint) + '</div></div>' +
      '<div class="fd-b"><div class="fd-top"><span>' + esc(U.fc_answer) + '</span><span>' + (fc.at + 1) + ' / ' + n + '</span></div><div class="fd-rule"></div><div class="fd-txt ' + size(b) + '">' + esc(b) + '</div></div></div></div>' +
      '<div class="fd-prog"><i style="width:' + ((fc.at + 1) / n * 100) + '%"></i></div>' +
      '<div class="fd-ctl"><button type="button" class="fd-r" data-fc="shuffle" title="' + esc(U.fc_shuffle) + '" aria-label="' + esc(U.fc_shuffle) + '">⇄</button><button type="button" class="fd-r" data-fc="prev" aria-label="' + esc(U.fc_prev) + '"' + (fc.at ? '' : ' disabled') + '>←</button>' +
      '<button type="button" class="fd-show" data-fc="flip">' + esc(fc.flip ? U.fc_show_question : U.fc_show_answer) + '</button><button type="button" class="fd-r" data-fc="next" aria-label="' + esc(U.fc_next) + '"' + (fc.at < n - 1 ? '' : ' disabled') + '>→</button>' +
      '<button type="button" class="fd-r" data-fc="first" aria-label="' + esc(U.fc_first) + '"' + (fc.at ? '' : ' disabled') + '>↺</button></div></div>';
  }
  function fcAct(a) {
    const n = T.cards.length;
    if (a === 'flip') { fc.flip = !fc.flip; root.querySelector('.fd-card').classList.toggle('flip', fc.flip); root.querySelector('.fd-show').textContent = fc.flip ? U.fc_show_question : U.fc_show_answer; return; }
    if (a === 'shuffle') { for (let i = n - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [fc.order[i], fc.order[j]] = [fc.order[j], fc.order[i]]; } fc.at = 0; }
    if (a === 'prev') fc.at = Math.max(0, fc.at - 1);
    if (a === 'next') fc.at = Math.min(n - 1, fc.at + 1);
    if (a === 'first') fc.at = 0;
    fc.flip = false; fcRender();
  }
  // Artifacts: everything made in this demo stays, like the app's Artifacts screen
  const ARTS = [];
  function addArt(k) { if (ARTS.includes(k)) return; ARTS.unshift(k); root.querySelector('.gd-count').textContent = ARTS.length; }
  async function artThumb(k) {
    if (k === 'slides') { const d = await loadData(); return scene(d.decks['full|wisteria|comic'][0]); }
    if (k.startsWith('img')) return '<img src="/demo/img-' + IMG_FILES[+k.slice(4)] + '.webp" alt="" loading="lazy"/>';
    if (k === 'diagram') return '<img src="/demo/plant-cell.webp" alt="" loading="lazy"/>';
    return '<span class="gd-big">' + ICON[k] + '</span>';
  }
  const artInfo = (k) => k.startsWith('img') ? [U.kinds.image, T.images[+k.slice(4)][0]] : [U.kinds[k], T.jobs[k].title];
  async function renderArts() {
    const v = root.querySelector('.gd-arts');
    let h = '<div class="gd-vh"><h3>' + esc(U.arts_title) + '</h3><p>' + esc(U.arts_sub) + '</p></div>';
    if (!ARTS.length) h += '<div class="gd-empty">' + esc(U.arts_empty) + '</div>';
    else { h += '<div class="gd-agrid">'; for (const k of ARTS) h += '<button type="button" class="gd-art" data-art="' + k + '"><span class="th">' + await artThumb(k) + '</span><small>' + esc(artInfo(k)[0]) + '</small><b>' + esc(artInfo(k)[1]) + '</b></button>'; h += '</div>'; }
    v.innerHTML = h;
  }
  // Images tab, like the app's: describe a picture, GreenCube draws it on the PC, every picture stays in the library.
  // All 8 were made by GreenCube's picture engine on a 16 GB laptop (about 2 minutes each).
  const made = []; let imgPick = 0, drawing = false, imgTyper = null;
  function renderImages() {
    const v = root.querySelector('.gd-imgs'), I = T.images;
    v.innerHTML = '<div class="gi-top"><div class="gd-vh"><h3>' + esc(U.imgs_title) + '</h3><p>' + esc(U.imgs_sub) + '</p></div>' +
      '<div class="gi-lib">' + (made.length ? made.map((i) => '<button type="button" class="gi-th" data-big="' + i + '"><img src="/demo/img-' + IMG_FILES[i] + '.webp" alt="' + esc(I[i][0]) + '"/></button>').join('')
        : '<div class="gd-empty">' + esc(U.imgs_empty) + '</div>') + '</div></div>' +
      '<div class="gi-bottom"><div class="gi-opts" role="group" aria-label="' + esc(U.imgs_options) + '">' + I.map((x, i) => '<button type="button" data-ipick="' + i + '"' + (made.includes(i) ? ' class="done"' : '') + '>' + esc(x[0]) + '</button>').join('') + '</div>' +
      '<div class="gd-compose gi-compose"><div class="gd-input gi-in" role="button" tabindex="0" aria-label="' + esc(U.draw) + '"></div><div class="gd-bar"><span class="gd-plus" title="' + esc(U.start_from) + '" aria-hidden="true">+</span><span class="gd-eng">□ ' + esc(U.square) + '</span><button class="gd-send gi-go" type="button" aria-label="' + esc(U.draw) + '">↑</button></div></div>' +
      '<div class="gd-foot">' + esc(U.imgs_foot) + '</div></div>';
    pickImage(made.length < I.length ? I.findIndex((_, i) => !made.includes(i)) : 0);
  }
  function pickImage(i) {
    imgPick = i; clearInterval(imgTyper); const b = root.querySelector('.gi-in'); if (!b) return;
    const text = T.images[i][1]; let n = 0; b.classList.remove('ph');
    imgTyper = setInterval(() => { n++; b.innerHTML = esc(text.slice(0, n)) + '<span class="cur"></span>'; if (n >= text.length) clearInterval(imgTyper); }, 18);
  }
  async function drawImage() {
    if (drawing) return; drawing = true; clearInterval(imgTyper);
    const i = imgPick, lib = root.querySelector('.gi-lib');
    lib.querySelector('.gd-empty')?.remove();
    const slot = document.createElement('div'); slot.className = 'gi-th gi-drawing';
    slot.innerHTML = '<span class="gd-turtle" aria-hidden="true">🐢</span><b>' + esc(U.drawing) + '</b><div class="gd-bar2"><i></i></div><small>' + esc(U.drawing_note) + '</small>';
    lib.prepend(slot); const b = root.querySelector('.gi-in'); b.textContent = U.describe; b.classList.add('ph');
    await wait(3100);
    if (!made.includes(i)) made.unshift(i);
    addArt('img:' + i); drawing = false; renderImages(); bigImage(i);
  }
  function bigImage(i) {
    const v = root.querySelector('.gd-imgs'); if (!v) return;
    let o = v.querySelector('.gi-big'); if (!o) { o = document.createElement('div'); o.className = 'gi-big'; v.appendChild(o); }
    o.innerHTML = '<button type="button" class="gi-x">' + esc(U.back) + '</button><img src="/demo/img-' + IMG_FILES[i] + '.webp" width="512" height="512" alt="' + esc(T.images[i][0] + ', ' + U.made_by) + '"/>' +
      '<div class="gi-meta"><b>' + esc(T.images[i][0]) + '</b><p>“' + esc(T.images[i][1]) + '”</p><small>' + esc(U.made_note) + '</small></div>';
  }
  function showView(name) {
    const chatOn = name === 'chat';
    ['.gd-chat', '.gd-chips', '.gd-compose', '.gd-foot'].forEach((q) => { root.querySelector(q).hidden = !chatOn; });
    root.querySelector('.gd-arts').hidden = name !== 'artifacts';
    root.querySelector('.gd-imgs').hidden = name !== 'images';
    root.querySelectorAll('.gd-nav[data-tab]').forEach((b) => b.classList.toggle('on', b.dataset.tab === name));
    if (!chatOn) panel.classList.remove('on');
    if (name === 'artifacts') renderArts();
    if (name === 'images') renderImages();
  }

  // the words of the window itself, in the page's language
  function dress() {
    const set = (q, t, scope) => { const e = (scope || root).querySelector(q); if (e) e.textContent = t; };
    const h = new Date().getHours();
    set('.gd-hello h3', U.greet[h < 5 ? 0 : h < 12 ? 1 : h < 19 ? 2 : 3] + ', ' + U.name + '.');
    set('.gd-hello p', U.hello_sub); set('.gd-foot', U.foot); set('.gd-new', U.new_chat); set('.gd-rec', U.recents);
    set('.gd-nav:not([data-tab])', U.search); set('.gd-style', U.style); set('.gd-save', U.save);
    root.querySelector('[data-tab=images]').textContent = U.images;
    root.querySelector('[data-tab=artifacts]').innerHTML = esc(U.artifacts) + ' <span class="gd-count">' + ARTS.length + '</span>';
    const navs = root.querySelectorAll('.gd-side .gd-nav'); navs[navs.length - 1].textContent = U.settings;
    root.querySelectorAll('.gd-recents .gd-r').forEach((r, i) => { if (U.recent_seed[i]) r.textContent = U.recent_seed[i]; });
    if (input.classList.contains('ph')) input.textContent = U.placeholder;
    send.setAttribute('aria-label', U.send); root.querySelector('.gd-ph .x').setAttribute('aria-label', U.close);
    set('.gd-hint span', U.hint, box); set('.gd-label', U.label, box);
    chips.innerHTML = JOBS.map((k) => '<button type="button" data-job="' + k + '">' + esc(U.chips[k]) + '</button>').join('');
    if (!root.querySelector('.gd-click')) { const c = document.createElement('span'); c.className = 'gd-click'; c.innerHTML = '<b>' + esc(U.click_here) + '</b><img src="/img/turtle.svg" alt="" width="54" height="54"/>'; send.closest('.gd-compose').appendChild(c); }
  }
  ready = fetch('/demo/i18n/' + lang + '.json').then((r) => r.json()).catch(() => fetch('/demo/i18n/en.json').then((r) => r.json())).then((t) => {
    T = t; U = t.ui; JOBS = ['slides', 'quiz', 'cards', 'diagram']; dress();
  });

  chips.addEventListener('click', (e) => { const b = e.target.closest('button'); if (b && !busy) { picked = true; choose(b.dataset.job); } });
  send.addEventListener('click', () => { if (T) run(job); });
  input.addEventListener('click', () => { if (T && !busy) run(job); });
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (T && !busy) run(job); } });
  root.addEventListener('click', async (e) => {
    if (!T) return;
    const tb = e.target.closest('[data-tab]'); if (tb) { showView(tb.dataset.tab); return; }
    const ip = e.target.closest('[data-ipick]'); if (ip) { if (!drawing) pickImage(+ip.dataset.ipick); return; }
    if (e.target.closest('.gi-go, .gi-in')) { drawImage(); return; }
    const bg = e.target.closest('[data-big]'); if (bg) { bigImage(+bg.dataset.big); return; }
    if (e.target.closest('.gi-x')) { root.querySelector('.gi-big')?.remove(); return; }
    const ar = e.target.closest('[data-art]'); if (ar) { const k = ar.dataset.art; if (k.startsWith('img')) { showView('images'); bigImage(+k.slice(4)); return; } showView('chat'); if (k === 'diagram') { const f = root.querySelector('.gd-fig'); if (f) f.scrollIntoView({ block: 'nearest' }); return; } open(k); return; }
    const fb = e.target.closest('[data-fc]'); if (fb) { fcAct(fb.dataset.fc); return; }
    if (e.target.closest('.fd-card')) { fcAct('flip'); return; }
    const c = e.target.closest('[data-open]'); if (c) { open(c.dataset.open); return; }
    const f = e.target.closest('[data-follow]'); if (f) { follow(f.dataset.follow, f); return; }
    const s = e.target.closest('[data-style]'); if (s) { style = s.dataset.style; await open('slides'); await stylePicker(); styles.classList.add('on'); return; }
    if (e.target.closest('.gd-style')) { if (!styles.classList.contains('on')) await stylePicker(); styles.classList.toggle('on'); return; }
    if (e.target.closest('.gd-ph .x')) { panel.classList.remove('on'); return; }
    if (e.target.closest('.gd-save')) { const b = e.target.closest('.gd-save'), o = b.textContent; b.textContent = U.save_msg; setTimeout(() => (b.textContent = o), 2200); return; }
    const a = e.target.closest('.qz button');
    if (a) {
      const q0 = a.closest('.qz'); if (q0.dataset.done) return; q0.dataset.done = 1;
      const q = T.quiz[+q0.dataset.q], pick = +a.dataset.a;
      q0.querySelectorAll('button').forEach((b, j) => { if (j === q.a) b.classList.add('ok'); else if (j === pick) b.classList.add('no'); });
      const done = body.querySelectorAll('.qz[data-done]'), right = [...done].filter((x) => !x.querySelector('.no')).length;
      body.querySelector('.qz-score').textContent = U.quiz_score.replace('{n}', done.length).replace('{r}', right);
    }
  });
  root.addEventListener('keydown', (e) => { if (!e.target.closest('.fd-card')) return; if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fcAct('flip'); } else if (e.key === 'ArrowRight') fcAct('next'); else if (e.key === 'ArrowLeft') fcAct('prev'); });
  const start = () => ready.then(() => { loadData(); if (!started) choose('slides'); });
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((es) => { if (es.some((x) => x.isIntersecting)) { io.disconnect(); start(); } }, { threshold: 0.35 });
    io.observe(root);
  } else start();
})();
