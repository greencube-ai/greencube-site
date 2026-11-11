/* /get: the clickable GreenCube window (Hector 11 Nov). No AI runs here: it replays example answers so a visitor can
   feel how the app works. Slides are the app's own drawings: every box, font and colour exported from the app's slide
   renderer in all 15 styles (demo/slides.json). The picture and the diagram are real GreenCube outputs. */
(() => {
  const root = document.getElementById('gd');
  if (!root) return;
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
      const box = 'left:' + X(i.x) + ';top:' + Y(i.y) + ';width:' + X(i.w) + ';height:' + Y(i.h) + ';' + (i.rotate ? 'transform:rotate(' + i.rotate + 'deg);' : '');
      if (i.k !== 't') {
        h += '<span style="' + box + 'background:' + (i.fill ? '#' + i.fill : 'transparent') + ';opacity:' + (i.opacity ?? 1) + ';border-radius:' +
          (i.k === 'e' ? '50%' : i.radius ? pt(i.radius * 72) : '0') + ';' + (i.ol ? 'box-shadow:inset 0 0 0 ' + pt(i.ol[0]) + ' #' + i.ol[1] + ';' : '') + '"></span>';
        continue;
      }
      const lines = (i.l || []).filter((x) => x.trim());
      h += '<div style="' + box + 'display:flex;flex-direction:column;justify-content:' + (i.valign === 'middle' ? 'center' : i.valign === 'bottom' ? 'flex-end' : 'flex-start') +
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

  const QUIZ = [
    { q: 'Which title does Macbeth already hold when the witches first greet him?', o: ['Thane of Glamis', 'Thane of Cawdor', 'Prince of Cumberland', 'King of Scotland'], a: 0 },
    { q: 'Who does Duncan name Prince of Cumberland, his heir?', o: ['Banquo', 'Macduff', 'Malcolm', 'Fleance'], a: 2 },
    { q: 'Who pushes Macbeth to murder Duncan when he hesitates?', o: ['The witches', 'Lady Macbeth', 'Banquo', 'Ross'], a: 1 },
    { q: 'What does Macbeth see floating before him just before the murder?', o: ['A crown', 'A ghost', 'A dagger', 'A raven'], a: 2 },
    { q: 'Whose ghost appears at the banquet in Act 3?', o: ['Duncan', 'Banquo', 'Lady Macduff', 'Fleance'], a: 1 },
  ];
  const CARDS = [
    ['GDP', 'The total value of all final goods and services a country produces in a year.'],
    ['Inflation', 'The general rise in prices over time, so the same money buys less.'],
    ['Fiscal policy', 'The government using taxes and spending to steer the economy.'],
    ['Monetary policy', 'The central bank changing interest rates and the money supply.'],
    ['Opportunity cost', 'The value of the best option you give up when you choose another.'],
  ];
  const JOBS = {
    slides: { chip: 'Slides', prompt: 'deck on the causes of ww1 for my history presentation', recent: 'Causes of World War I', kind: 'Slides', title: 'Causes of World War I', icon: '🖼️', meta: '7 slides · saves as PowerPoint',
      say: 'Here’s your deck: a cover, five slides and an ending, ready to present or save as PowerPoint.',
      follow: [['less text, I have to read it out', 'short'], ['try the Night colours', 'night'], ['try the Chalkboard style', 'chalkboard']] },
    quiz: { chip: 'Quiz', prompt: 'can u test me on macbeth acts 1-3, mcq', recent: 'Macbeth Acts 1–3 quiz', kind: 'Quiz', title: 'Macbeth Acts 1–3', icon: '❓', meta: '5 questions',
      say: 'Five questions on Acts 1 to 3. Pick your answers and I’ll mark them.', follow: [] },
    cards: { chip: 'Flashcards', prompt: 'econ flashcards: gdp, inflation, fiscal policy, monetary policy, opportunity cost', recent: 'Economics flashcards', kind: 'Flashcards', title: 'Economics basics', icon: '🃏', meta: '5 cards',
      say: 'Five cards. Click a card to flip it.', follow: [] },
    picture: { chip: 'Image', prompt: 'a cozy wooden cabin in a snowy pine forest at night, warm glowing windows, northern lights', recent: 'Cabin under the northern lights', kind: 'Image', title: 'Cabin under the northern lights', icon: '🎨', meta: 'Made on your PC',
      say: 'Here’s your image.', follow: [] },
    diagram: { chip: 'Diagram', prompt: 'explain the parts of a plant cell with a drawing', recent: 'Plant cell explained', follow: [] },
  };
  let busy = false, job = 'slides', style = 'comic', deckName = 'full', theme = 'wisteria', started = false, typer = null, data = null;
  const loadData = () => data || (data = fetch('/demo/slides.json').then((r) => r.json()));
  const deck = async () => (await loadData()).decks[deckName + '|' + theme + '|' + style] || [];

  function typeInto(text) {
    clearInterval(typer); let i = 0; input.classList.remove('ph');
    typer = setInterval(() => { i++; input.innerHTML = esc(text.slice(0, i)) + '<span class="cur"></span>'; if (i >= text.length) clearInterval(typer); }, 24);
  }
  function choose(k) { job = k; chips.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.job === k))); typeInto(JOBS[k].prompt); }
  function bubble(cls, html) { const d = document.createElement('div'); d.className = 'gd-msg ' + cls; d.innerHTML = html; chat.appendChild(d); chat.scrollTop = chat.scrollHeight; return d; }
  async function reply(html, ms) {
    const d = bubble('a', '<span class="gd-dots"><i></i><i></i><i></i></span>');
    await wait(ms || 1100); d.innerHTML = html; chat.scrollTop = chat.scrollHeight; return d;
  }
  function followChips(list) {
    if (!list.length) return;
    const f = document.createElement('div'); f.className = 'gd-follow';
    f.innerHTML = list.map(([t, v]) => '<button type="button" data-follow="' + v + '">' + esc(t) + '</button>').join('');
    chat.appendChild(f); chat.scrollTop = chat.scrollHeight;
  }
  const cardHtml = (k) => { const J = JOBS[k]; return '<button class="gd-card" type="button" data-open="' + k + '"><span class="ic" aria-hidden="true">' + J.icon + '</span><span><small>' + J.kind + '</small><b>' + esc(J.title) +
    '</b><em>' + J.meta + '</em></span><span class="open">Open ›</span></button><div class="gd-note">AI-generated — double-check important details</div>'; };

  async function run(k) {
    if (busy) return; busy = true; send.disabled = true;
    if (!started) { started = true; const h = $('.gd-hello'); if (h) h.remove(); }
    const J = JOBS[k];
    bubble('u', '<span>' + esc(J.prompt) + '</span>');
    input.innerHTML = 'Message GreenCube…'; input.classList.add('ph'); clearInterval(typer);
    const r = document.createElement('div'); r.className = 'gd-r on'; r.textContent = J.recent; r.dataset.done = k;
    recents.querySelectorAll('.gd-r').forEach((x) => x.classList.remove('on')); recents.prepend(r);
    if (k === 'slides') { deckName = 'full'; theme = 'wisteria'; style = 'comic'; delete root.dataset.used; await loadData(); }
    if (k === 'picture') {
      const d = bubble('a', '<div class="gd-paint"><span class="gd-turtle" aria-hidden="true">🐢</span><div><b>Painting your image…</b><div class="gd-bar2"><i></i></div><small>On a 16 GB laptop this takes about 2 minutes. Sped up here.</small></div></div>');
      await wait(3200); d.innerHTML = '<div>' + esc(J.say) + '</div>' + cardHtml(k);
    } else if (k === 'diagram') {
      await reply('<div>A plant cell is the basic unit of a plant. The main parts:</div><ul class="gd-ul"><li><b>Cell wall:</b> a stiff outer layer that gives the cell its shape.</li><li><b>Chloroplasts:</b> where photosynthesis turns light into food.</li><li><b>Central vacuole:</b> stores water and keeps the cell firm.</li><li><b>Nucleus:</b> holds the DNA and controls the cell.</li></ul>' +
        '<figure class="gd-fig"><img src="/demo/plant-cell.webp" width="782" height="478" alt="A labelled plant cell drawn by GreenCube: cell wall, membrane, nucleus, chloroplasts, vacuole and more" loading="lazy"/><figcaption>Drawn by GreenCube’s own code, labels included.</figcaption></figure>', 1300);
    } else {
      await reply('<div>' + esc(J.say) + '</div>' + cardHtml(k));
    }
    if (k !== 'diagram') await open(k);
    followChips(J.follow);
    busy = false; send.disabled = false;
    const next = Object.keys(JOBS).find((x) => !root.querySelector('.gd-r[data-done="' + x + '"]'));
    if (next) setTimeout(() => { if (!busy) choose(next); }, 900);
  }
  async function follow(v, btn) {
    if (busy) return; busy = true; btn.parentElement.remove();
    bubble('u', '<span>' + esc(btn.textContent) + '</span>');
    if (v === 'short') { deckName = 'short'; await reply('Done: the same deck with fewer, shorter points.'); }
    else if (v === 'night') { theme = 'night'; await reply('Switched the deck to the Night colours. Same slides, new palette.'); }
    else { style = v; await reply('Switched to the Chalkboard style. Every style is under <b>Style</b>.'); }
    await open('slides');
    root.dataset.used = (root.dataset.used || '') + ' ' + v;
    followChips(JOBS.slides.follow.filter(([, x]) => !(root.dataset.used || '').includes(x)));
    busy = false;
  }
  async function stylePicker() {
    const d = await loadData(), moods = ['Clean', 'Bold', 'Fun', 'School', 'Dark'];
    styles.innerHTML = moods.map((m) => '<div class="gd-mood"><small>' + m + '</small><div class="gd-looks">' + d.styles.filter((s) => s[2] === m).map(([id, name]) =>
      '<button type="button" data-style="' + id + '" class="gd-look' + (id === style ? ' on' : '') + '">' + scene((d.decks[deckName + '|' + theme + '|' + id] || [])[0] || { bg: 'fff', it: [] }) + '<span>' + esc(name) + '</span></button>').join('') + '</div></div>').join('');
  }
  async function open(k) {
    panel.classList.add('on'); styles.classList.remove('on');
    styleBtn.hidden = k !== 'slides'; $('.gd-save').hidden = k !== 'slides';
    const J = JOBS[k]; pKind.textContent = J.kind; pTitle.textContent = J.title;
    if (k === 'slides') body.innerHTML = (await deck()).map((sc) => scene(sc)).join('');
    else if (k === 'quiz') body.innerHTML = '<div class="qz-score">0/5 answered</div>' + QUIZ.map((q, i) => '<div class="qz" data-q="' + i + '"><p>' + (i + 1) + '. ' + esc(q.q) + '</p>' +
      q.o.map((o, j) => '<button type="button" data-a="' + j + '"><i>' + 'ABCD'[j] + '</i>' + esc(o) + '</button>').join('') + '</div>').join('');
    else if (k === 'cards') body.innerHTML = CARDS.map(([f, b]) => '<div class="fc" role="button" tabindex="0"><div><div class="f">' + esc(f) + '<small>Click to flip</small></div><div class="b">' + esc(b) + '</div></div></div>').join('');
    else body.innerHTML = '<figure class="gd-pic"><img src="/demo/cabin.webp" width="512" height="512" alt="A cozy wooden cabin in a snowy pine forest at night under the northern lights, made by GreenCube"/>' +
      '<figcaption>Made by GreenCube on a 16 GB laptop with Intel graphics, in about 2 minutes. No internet, no credits.</figcaption></figure>';
    body.scrollTop = 0;
  }

  { const h = new Date().getHours(), el = root.querySelector('.gd-hello h3');
    if (el) el.textContent = (h < 5 ? 'Working late' : h < 12 ? 'Good morning' : h < 19 ? 'Good afternoon' : 'Good evening') + ', Hector.'; }
  chips.innerHTML = Object.entries(JOBS).map(([k, J]) => '<button type="button" data-job="' + k + '">' + J.chip + '</button>').join('');
  chips.addEventListener('click', (e) => { const b = e.target.closest('button'); if (b && !busy) choose(b.dataset.job); });
  send.addEventListener('click', () => run(job));
  input.addEventListener('click', () => { if (!busy) run(job); });
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (!busy) run(job); } });
  root.addEventListener('click', async (e) => {
    const c = e.target.closest('[data-open]'); if (c) { open(c.dataset.open); return; }
    const f = e.target.closest('[data-follow]'); if (f) { follow(f.dataset.follow, f); return; }
    const s = e.target.closest('[data-style]'); if (s) { style = s.dataset.style; await open('slides'); await stylePicker(); styles.classList.add('on'); return; }
    if (e.target.closest('.gd-style')) { if (!styles.classList.contains('on')) await stylePicker(); styles.classList.toggle('on'); return; }
    if (e.target.closest('.gd-ph .x')) { panel.classList.remove('on'); return; }
    if (e.target.closest('.gd-save')) { const b = e.target.closest('.gd-save'), o = b.textContent; b.textContent = 'In the app, this saves a real .pptx'; setTimeout(() => (b.textContent = o), 2200); return; }
    const a = e.target.closest('.qz button');
    if (a) {
      const box = a.closest('.qz'); if (box.dataset.done) return; box.dataset.done = 1;
      const q = QUIZ[+box.dataset.q], pick = +a.dataset.a;
      box.querySelectorAll('button').forEach((b, j) => { if (j === q.a) b.classList.add('ok'); else if (j === pick) b.classList.add('no'); });
      const done = body.querySelectorAll('.qz[data-done]'), right = [...done].filter((x) => !x.querySelector('.no')).length;
      body.querySelector('.qz-score').textContent = done.length + '/5 answered, ' + right + ' correct';
      return;
    }
    const fc = e.target.closest('.fc'); if (fc) fc.classList.toggle('flip');
  });
  root.addEventListener('keydown', (e) => { const fc = e.target.closest('.fc'); if (fc && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); fc.classList.toggle('flip'); } });
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((es) => { if (es.some((x) => x.isIntersecting)) { io.disconnect(); loadData(); if (!started) choose('slides'); } }, { threshold: 0.35 });
    io.observe(root);
  } else choose('slides');
})();
