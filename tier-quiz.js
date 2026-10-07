// The two-question tier check, as it runs on the home page (EN and ES).
// Same cards, same rule and same reveal as what-you-get.html; the words follow
// <html lang>. The tier rule mirrors perf_tier_from in the app (docs/TIERS.md).
(() => {
  const game = document.getElementById('game');
  if (!game) return;
  const es = document.documentElement.lang === 'es';

  const T = es ? {
    about: (v) => 'unos ' + v + ' GB', builtIn: 'integrada',
    miss: 'No está en nuestra lista. ¿Cuánta memoria tiene?', noIdea: 'Ni idea',
    guessedRam: 'RAM que tuvimos que adivinar', ram: (n) => n + ' GB de RAM',
    withMem: (card, extra, mem) => '<b>' + card + '</b>' + extra + ', con <b>' + mem + '</b>.',
    sized: (v) => ', unos ' + v + ' GB',
    none: (mem) => '<b>Sin tarjeta gráfica aparte</b>, con <b>' + mem + '</b>.',
    guessed: (mem) => 'Supusimos <b>sin tarjeta gráfica</b>, con <b>' + mem + '</b>. Si tienes una, irá mejor que esto.',
    builtInSpec: (mem) => '<b>Gráficos integrados</b>, con <b>' + mem + '</b>.',
    mac: 'Eso es lo que sería tu Mac. Hoy GreenCube es solo para Windows; la versión para Mac está en camino.',
    feels: { seed: 'Lenta, pero llega.', sprout: 'Va bien. No es rápida.', bloom: 'Dejas de notar la espera.', thrive: 'El único límite es tu ordenador.' }
  } : {
    about: (v) => 'about ' + v + ' GB', builtIn: 'built in',
    miss: 'Not on our list. How much memory does it have?', noIdea: 'No idea',
    guessedRam: 'RAM we had to guess at', ram: (n) => n + ' GB of RAM',
    withMem: (card, extra, mem) => '<b>' + card + '</b>' + extra + ', with <b>' + mem + '</b>.',
    sized: (v) => ', about ' + v + ' GB',
    none: (mem) => '<b>No separate graphics card</b>, with <b>' + mem + '</b>.',
    guessed: (mem) => 'We assumed <b>no graphics card</b>, with <b>' + mem + '</b>. If you do have one, it is better than this.',
    builtInSpec: (mem) => '<b>Built-in graphics</b>, with <b>' + mem + '</b>.',
    mac: 'That is what a Mac of yours would be. GreenCube is Windows only today, and the Mac version is on the way.',
    feels: { seed: 'Slow, but it gets there.', sprout: 'Works well. Not fast.', bloom: 'You stop noticing the wait.', thrive: 'Your computer is the only limit.' }
  };

  // Graphics cards with their memory. Coarse buckets are all the tier needs
  // (under 4 GB, 4 to 7, 8 and up); anything missing can be entered by size.
  const CARDS = [
    ['GeForce GT 1030', 2], ['GeForce GTX 750 Ti', 2], ['GeForce GTX 950', 2],
    ['GeForce GTX 960', 2], ['GeForce GTX 970', 4], ['GeForce GTX 980', 4],
    ['GeForce GTX 980 Ti', 6], ['GeForce GTX 1050', 2], ['GeForce GTX 1050 Ti', 4],
    ['GeForce GTX 1060', 6], ['GeForce GTX 1070', 8], ['GeForce GTX 1070 Ti', 8],
    ['GeForce GTX 1080', 8], ['GeForce GTX 1080 Ti', 11],
    ['GeForce GTX 1630', 4], ['GeForce GTX 1650', 4], ['GeForce GTX 1650 Super', 4],
    ['GeForce GTX 1660', 6], ['GeForce GTX 1660 Super', 6], ['GeForce GTX 1660 Ti', 6],
    ['Titan Xp', 12], ['Titan V', 12], ['Titan RTX', 24],
    ['GeForce RTX 2050', 4], ['GeForce RTX 2060', 6], ['GeForce RTX 2060 Super', 8],
    ['GeForce RTX 2070', 8], ['GeForce RTX 2070 Super', 8], ['GeForce RTX 2080', 8],
    ['GeForce RTX 2080 Super', 8], ['GeForce RTX 2080 Ti', 11],
    ['GeForce RTX 2060 Laptop', 6], ['GeForce RTX 2070 Laptop', 8], ['GeForce RTX 2080 Laptop', 8],
    ['GeForce RTX 3050', 8], ['GeForce RTX 3050 Laptop', 4], ['GeForce RTX 3050 Ti Laptop', 4],
    ['GeForce RTX 3060', 12], ['GeForce RTX 3060 Laptop', 6], ['GeForce RTX 3060 Ti', 8],
    ['GeForce RTX 3070', 8], ['GeForce RTX 3070 Laptop', 8], ['GeForce RTX 3070 Ti', 8],
    ['GeForce RTX 3080', 10], ['GeForce RTX 3080 Laptop', 8], ['GeForce RTX 3080 Ti', 12],
    ['GeForce RTX 3080 Ti Laptop', 16], ['GeForce RTX 3090', 24], ['GeForce RTX 3090 Ti', 24],
    ['GeForce RTX 4050 Laptop', 6], ['GeForce RTX 4060', 8], ['GeForce RTX 4060 Laptop', 8],
    ['GeForce RTX 4060 Ti', 8], ['GeForce RTX 4070', 12], ['GeForce RTX 4070 Laptop', 8],
    ['GeForce RTX 4070 Super', 12], ['GeForce RTX 4070 Ti', 12], ['GeForce RTX 4070 Ti Super', 16],
    ['GeForce RTX 4080', 16], ['GeForce RTX 4080 Laptop', 12], ['GeForce RTX 4080 Super', 16],
    ['GeForce RTX 4090', 24], ['GeForce RTX 4090 Laptop', 16],
    ['GeForce RTX 5050', 8], ['GeForce RTX 5060', 8], ['GeForce RTX 5060 Ti', 16],
    ['GeForce RTX 5070', 12], ['GeForce RTX 5070 Ti', 16], ['GeForce RTX 5080', 16],
    ['GeForce RTX 5090', 32],
    ['Quadro P1000', 4], ['Quadro P2000', 5], ['Quadro RTX 4000', 8], ['Quadro RTX 5000', 16],
    ['NVIDIA T600', 4], ['NVIDIA T1000', 8], ['NVIDIA RTX A2000', 12], ['NVIDIA RTX A4000', 16],
    ['NVIDIA RTX A5000', 24], ['NVIDIA RTX A6000', 48], ['NVIDIA RTX 4000 Ada', 20],
    ['NVIDIA RTX 5000 Ada', 32], ['NVIDIA RTX 6000 Ada', 48],
    ['Radeon R9 380', 4], ['Radeon R9 390', 8], ['Radeon RX 550', 4], ['Radeon RX 560', 4],
    ['Radeon RX 570', 8], ['Radeon RX 580', 8], ['Radeon RX 590', 8],
    ['Radeon RX Vega 56', 8], ['Radeon RX Vega 64', 8], ['Radeon VII', 16],
    ['Radeon RX 5500 XT', 8], ['Radeon RX 5600 XT', 6], ['Radeon RX 5700', 8], ['Radeon RX 5700 XT', 8],
    ['Radeon RX 6400', 4], ['Radeon RX 6500 XT', 4], ['Radeon RX 6600', 8], ['Radeon RX 6600 XT', 8],
    ['Radeon RX 6650 XT', 8], ['Radeon RX 6700', 10], ['Radeon RX 6700 XT', 12],
    ['Radeon RX 6750 XT', 12], ['Radeon RX 6800', 16], ['Radeon RX 6800 XT', 16],
    ['Radeon RX 6900 XT', 16], ['Radeon RX 6950 XT', 16],
    ['Radeon RX 7600', 8], ['Radeon RX 7600 XT', 16], ['Radeon RX 7700 XT', 12],
    ['Radeon RX 7800 XT', 16], ['Radeon RX 7900 GRE', 16], ['Radeon RX 7900 XT', 20],
    ['Radeon RX 7900 XTX', 24],
    ['Radeon RX 9060 XT', 8], ['Radeon RX 9070', 16], ['Radeon RX 9070 XT', 16],
    ['Radeon RX 6600M', 8], ['Radeon RX 6700M', 10], ['Radeon RX 6800M', 12],
    ['Radeon RX 7600M XT', 8], ['Radeon RX 7700S', 8],
    ['Intel Arc A310', 4], ['Intel Arc A380', 6], ['Intel Arc A550M', 8], ['Intel Arc A580', 8],
    ['Intel Arc A750', 8], ['Intel Arc A770', 16], ['Intel Arc B570', 10], ['Intel Arc B580', 12],
    ['Intel HD Graphics (built in)', 0], ['Intel UHD Graphics (built in)', 0],
    ['Intel Iris Plus (built in)', 0], ['Intel Iris Xe (built in)', 0],
    ['Intel Arc Graphics, laptop chip (built in)', 0],
    ['AMD Radeon Vega, in a Ryzen chip (built in)', 0],
    ['AMD Radeon 660M / 680M (built in)', 0], ['AMD Radeon 760M / 780M (built in)', 0],
    ['AMD Radeon 860M / 890M (built in)', 0],
    // Apple silicon is tiered on total RAM only (-1 marks it): a Mac reports 75%
    // of its memory as graphics memory, which would call an 8 GB MacBook fast.
    ['Apple M1', -1], ['Apple M1 Pro', -1], ['Apple M1 Max', -1], ['Apple M1 Ultra', -1],
    ['Apple M2', -1], ['Apple M2 Pro', -1], ['Apple M2 Max', -1], ['Apple M2 Ultra', -1],
    ['Apple M3', -1], ['Apple M3 Pro', -1], ['Apple M3 Max', -1], ['Apple M3 Ultra', -1],
    ['Apple M4', -1], ['Apple M4 Pro', -1], ['Apple M4 Max', -1],
    ['Apple silicon, M5 or newer', -1]
  ].map(([name, vram]) => ({ name, vram, key: name.toLowerCase() }));

  const TIERS = {
    seed:   { name: 'Seed',   mk: '#FAE289' },
    sprout: { name: 'Sprout', mk: '#8EA674' },
    bloom:  { name: 'Bloom',  mk: '#FA9F75' },
    thrive: { name: 'Thrive', mk: '#8EABE1' }
  };

  const $ = (id) => document.getElementById(id);
  const steps = { ram: $('s-ram'), gpu: $('s-gpu'), rev: $('s-rev') };
  const state = { ram: null, card: null, vram: 0, guessed: false };

  function show(key) {
    Object.values(steps).forEach((s) => s.classList.remove('on'));
    steps[key].classList.add('on');
  }

  function ramGb() {
    if (state.ram === '8') return 8;
    if (state.ram === '16') return 16;
    if (state.ram === '32') return 32;
    // "No idea": the browser only glimpses this, so it never lands on the top tier.
    const dm = navigator.deviceMemory || 0;
    const cores = navigator.hardwareConcurrency || 0;
    return (dm >= 8 || cores >= 8) ? 16 : 8;
  }

  function tierFor(gb, vram) {
    if (vram === -1) {
      if (gb >= 24) return 'thrive';
      if (gb >= 12) return 'bloom';
      return 'seed';
    }
    if (vram >= 8 && gb >= 24) return 'thrive';
    if (vram >= 8 && gb >= 8) return 'bloom';
    if (vram >= 4 && gb >= 16) return 'bloom';
    if (gb >= 12 || (vram >= 4 && gb >= 8)) return 'sprout';
    return 'seed';
  }

  const input = $('gpu-in');
  const hits = $('hits');
  let cursor = -1, shown = [];

  function search(q) {
    const words = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    return CARDS.filter((c) => words.every((w) => c.key.includes(w))).slice(0, 7);
  }

  function paint() {
    if (shown.length) {
      hits.innerHTML = shown.map((c, i) =>
        '<button class="hit' + (i === cursor ? ' cursor' : '') + '" type="button" data-i="' + i + '">' +
        '<span class="h-n">' + c.name + '</span>' +
        '<span class="h-v">' + (c.vram > 0 ? T.about(c.vram) : c.vram === 0 ? T.builtIn : '') + '</span>' +
        '</button>').join('');
    } else if (input.value.trim().length >= 2) {
      hits.innerHTML = '<div class="miss"><b>' + T.miss + '</b><div class="sizes">' +
        [2, 4, 6, 8, 12, 16, 24].map((v) => '<button type="button" data-v="' + v + '">' + v + ' GB</button>').join('') +
        '<button type="button" data-v="0">' + T.noIdea + '</button></div></div>';
    } else {
      hits.innerHTML = '';
    }
    input.setAttribute('aria-expanded', String(hits.innerHTML !== ''));
  }

  function escapeHtml(s) { return s.replace(/[&<>"']/g, (c) => '&#' + c.charCodeAt(0) + ';'); }

  function choose(c) { state.card = c.name; state.vram = c.vram; state.guessed = false; reveal(); }

  input.addEventListener('input', () => { shown = search(input.value); cursor = shown.length ? 0 : -1; paint(); });
  input.addEventListener('keydown', (e) => {
    if (!shown.length) return;
    if (e.key === 'ArrowDown') { e.preventDefault(); cursor = (cursor + 1) % shown.length; paint(); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); cursor = (cursor - 1 + shown.length) % shown.length; paint(); }
    else if (e.key === 'Enter') { e.preventDefault(); if (shown[cursor]) choose(shown[cursor]); }
  });
  hits.addEventListener('click', (e) => {
    const hit = e.target.closest('.hit');
    if (hit) { choose(shown[+hit.getAttribute('data-i')]); return; }
    const size = e.target.closest('[data-v]');
    if (size) {
      const v = +size.getAttribute('data-v');
      state.card = escapeHtml(input.value.trim());
      state.vram = v;
      state.guessed = v === 0;
      reveal();
    }
  });

  $('gpu-none').addEventListener('click', () => { state.card = 'none'; state.vram = 0; state.guessed = false; reveal(); });
  $('gpu-dunno').addEventListener('click', () => { state.card = null; state.vram = 0; state.guessed = true; reveal(); });

  function reveal() {
    const gb = ramGb();
    const key = tierFor(gb, state.vram);
    const t = TIERS[key];

    game.style.setProperty('--mk', t.mk);
    game.classList.add('lit');
    $('r-name').textContent = t.name;
    $('r-feels').textContent = T.feels[key];

    const mem = state.ram === 'unsure' ? T.guessedRam : T.ram(state.ram);
    let spec;
    if (state.vram === -1) spec = T.withMem(state.card, '', mem);
    else if (state.vram > 0) spec = T.withMem(state.card, T.sized(state.vram), mem);
    else if (state.card === 'none') spec = T.none(mem);
    else if (state.guessed) spec = T.guessed(mem);
    else spec = T.builtInSpec(mem);
    $('r-spec').innerHTML = spec;

    const note = $('r-note');
    note.textContent = T.mac;
    note.hidden = state.vram !== -1;

    // light up the matching tier card just below
    document.querySelectorAll('.tier-card, .flat-tier').forEach((c) => {
      const h = c.querySelector('h3');
      c.classList.toggle('yours', !!h && h.textContent.trim() === t.name);
    });

    show('rev');
    const n = $('r-name');
    n.style.animation = 'none'; void n.offsetWidth; n.style.animation = '';
  }

  $('back-ram').addEventListener('click', () => show('ram'));
  $('again').addEventListener('click', () => {
    state.ram = null; state.card = null; state.vram = 0; state.guessed = false;
    input.value = ''; shown = []; paint();
    game.classList.remove('lit');
    document.querySelectorAll('.tier-card.yours, .flat-tier.yours').forEach((c) => c.classList.remove('yours'));
    game.style.setProperty('--mk', '#8EA674');
    show('ram');
  });

  document.querySelectorAll('#game [data-ram]').forEach((b) => {
    b.addEventListener('click', () => {
      state.ram = b.getAttribute('data-ram');
      show('gpu');
      setTimeout(() => input.focus({ preventScroll: true }), 240);
    });
  });
})();
