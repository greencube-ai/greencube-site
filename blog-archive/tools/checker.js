/* "Can my PC run AI?" checker. Runs only in the browser: nothing about the PC is sent anywhere.
   pc_pages.py fills in D (the card list and every measured PC) when the blog is built, so every number shown here
   comes from blog-archive/data/pcs.json. A card we have not measured gets no speed of its own: we show the cards
   we did measure, and say so. */
(function () {
  var D = /*DATA*/null;
  var es = D.lang === 'es';
  var box = document.getElementById('chk');
  if (!box) return;
  var sel = document.getElementById('chk-card'), vbox = document.getElementById('chk-vram'), rbox = document.getElementById('chk-ram');
  var out = document.getElementById('chk-out'), det = document.getElementById('chk-detect');
  var cards = [];
  D.groups.forEach(function (g) { g.cards.forEach(function (c) { cards.push({ vendor: g.vendor, kind: g.kind, model: c[0], vrams: c[1] }); }); });
  var state = { card: null, vram: null, ram: null };

  function n(x) { return es ? String(x).replace('.', ',') : String(x); }
  function rng(r, approx) { var s = r[0] === r[1] ? n(r[0]) : n(r[0]) + '–' + n(r[1]); return approx ? (es ? 'unos ' : 'about ') + s : s; }
  function secs(r) {
    var mm = function (t) { return Math.floor(t / 60) + ':' + ('0' + t % 60).slice(-2); };
    if (r[1] < 90) return r[0] === r[1] ? r[0] + ' s' : r[0] + '–' + r[1] + ' s';
    return r[0] === r[1] ? mm(r[0]) + ' min' : mm(r[0]) + '–' + mm(r[1]) + ' min';
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function a(m) { return '<a href="' + m.url + '">' + esc(m.name) + '</a>'; }
  function tag(m) { return m.test ? (es ? ' (prueba de arranque)' : ' (startup test)') : ''; }
  function speed(m) { return rng(m.writes, m.approx) + (es ? ' tokens por segundo' : ' tokens a second') + tag(m); }

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
  var raw = renderer(), name = clean(raw), builtin = /intel|radeon\(tm\) graphics|radeon graphics|vega \d+ graphics|apple|mali|adreno/i;
  if (name) {
    var i = match(name);
    var vague = /or similar/i.test(raw);
    if (/apple/i.test(name)) {
      det.innerHTML = es ? 'Tu navegador dice que tienes un Mac. GreenCube es para PCs con Windows, así que este comprobador no te sirve aún.'
                         : 'Your browser says this is a Mac. GreenCube is for Windows PCs, so this checker can\'t help yet.';
    } else if (i >= 0 && !vague) {
      det.innerHTML = (es ? 'Tu navegador dice que tienes: <strong>' : 'Your browser says your graphics are: <strong>') + esc(name) + '</strong>. '
        + (es ? '¿No es la tuya? Elígela abajo.' : 'Not right? Pick yours below.');
      choose(i);
    } else if (builtin.test(name) && !vague && !/arc a|arc b/i.test(name)) {
      det.innerHTML = (es ? 'Tu navegador solo ve gráficos integrados: <strong>' : 'Your browser only sees built-in graphics: <strong>') + esc(name) + '</strong>. '
        + (es ? 'Muchos portátiles gaming enseñan aquí el chip integrado aunque también tengan tarjeta. Si la tuya tiene, elígela abajo.'
              : 'Many gaming laptops show the built-in chip here even when they also have a gaming card. If yours has one, pick it below.');
      choose(cards.length - 1);
    } else {
      det.innerHTML = (es ? 'Tu navegador no deja ver qué tarjeta tienes' : 'Your browser hides which card you have')
        + (name && !vague ? ' (' + (es ? 'dice' : 'it says') + ' <strong>' + esc(name) + '</strong>)' : '') + '. ' + (es ? 'Elígela abajo.' : 'Pick it below.');
    }
  } else {
    det.innerHTML = es ? 'Elige tu tarjeta gráfica y tu RAM.' : 'Pick your graphics card and your RAM.';
  }

  /* ---------- picking ---------- */
  function choose(i) {
    sel.value = String(i);
    state.card = cards[i];
    var v = state.card.vrams;
    state.vram = v.length === 1 ? v[0] : null;
    vbox.hidden = v.length === 1;
    vbox.querySelector('.chk-opts').innerHTML = v.map(function (x) { return '<button type="button" data-v="' + x + '">' + x + ' GB</button>'; }).join('');
    show();
  }
  sel.addEventListener('change', function () { if (sel.value !== '') choose(+sel.value); else { state.card = null; show(); } });
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
    // chat and study
    if (gpu && v >= 6) out.push(['yes', es ? 'Chatear y estudiar' : 'Chat and study',
      es ? E.e4b.name + ' (' + n(E.e4b.gb) + ' GB) cabe entera en tu tarjeta de ' + v + ' GB, con sitio para la conversación. Eso es lo que hace que vaya rápido. La pequeña, ' + E.e2b.name + ', también cabe.'
         : E.e4b.name + ' (' + n(E.e4b.gb) + ' GB) fits whole on your ' + v + ' GB card, with room for the conversation. That is what makes chat fast. The smaller ' + E.e2b.name + ' fits too.']);
    else if (gpu) out.push(['part', es ? 'Chatear y estudiar' : 'Chat and study',
      (es ? E.e4b.name + ' ocupa ' + n(E.e4b.gb) + ' GB, algo más de lo que cabe en tu tarjeta de ' + v + ' GB, así que una parte va en la RAM y va más lenta que en una tarjeta más grande. La pequeña, ' + E.e2b.name + ' (' + n(E.e2b.gb) + ' GB), cabe entera en la tarjeta.'
          : E.e4b.name + ' is ' + n(E.e4b.gb) + ' GB, a little more than your ' + v + ' GB card holds, so part of it runs from RAM and it is slower than on a bigger card. The smaller ' + E.e2b.name + ' (' + n(E.e2b.gb) + ' GB) fits on the card whole.')
      + (R <= 8 ? (es ? ' Con 8 GB de RAM, cierra otras apps mientras la usas.' : ' With 8 GB of RAM, close other apps while you use it.') : '')]);
    else if (R >= 16) out.push(['yes', es ? 'Chatear y estudiar' : 'Chat and study',
      (c.kind !== 'none' ? (es ? 'Tu tarjeta de ' + v + ' GB es demasiado pequeña para la IA, así que funciona en el procesador. ' : 'Your ' + v + ' GB card is too small to hold the AI, so it runs on your processor. ')
                         : (es ? 'No hace falta tarjeta: la IA funciona en tu procesador, con ayuda de los gráficos integrados para leer. ' : 'No card needed: the AI runs on your processor, with the built-in graphics helping it read. '))
      + (es ? 'Van tanto ' + E.e2b.name + ' como la más grande, ' + E.e4b.name + '; la E2B es la más rápida.'
            : 'Both ' + E.e2b.name + ' and the bigger ' + E.e4b.name + ' work; E2B is the quicker one.')]);
    else out.push(['part', es ? 'Chatear y estudiar' : 'Chat and study',
      es ? 'Funciona con la IA pequeña, ' + E.e2b.name + ', en tu procesador, despacio. Cierra otras apps antes: con 8 GB, los demás programas le dejan poco sitio.'
         : 'It works with the smaller ' + E.e2b.name + ' on your processor, slowly. Close other apps first: with 8 GB, other programs leave the AI little room.']);
    // speed
    if (m) out.push(['yes', es ? 'Velocidad (medida)' : 'Speed (measured)',
      (es ? 'Medido en una ' + esc(m.name) + ' real: ' : 'Measured on a real ' + esc(m.name) + ': ') + speed(m) + (es ? ' con ' : ' with ') + m.engine + '. '
      + (es ? 'Tú lees unos 8. ' : 'You read about 5. ') + '<a href="' + m.url + '">' + (es ? 'Ver la prueba completa' : 'See the full test') + ' &rarr;</a>']);
    else if (gpu) {
      var p = peers(v);
      out.push(['maybe', es ? 'Velocidad (aún sin medir)' : 'Speed (not measured yet)',
        (es ? 'Aún no hemos medido tu tarjeta. ' : 'We haven\'t measured your card yet. ')
        + (p.same ? (es ? 'Tarjetas de ' + v + ' GB que sí medimos: ' : 'Cards with ' + v + ' GB we did measure: ') : (es ? 'Las tarjetas medidas más parecidas: ' : 'The closest cards we measured: '))
        + p.list.map(function (x) { return a(x) + (p.same ? '' : ' (' + x.vram + ' GB)') + ', ' + speed(x); }).join('; ') + '. '
        + (es ? 'La velocidad depende de lo nueva que sea la tarjeta, no solo de su memoria, así que no nos inventamos un número para la tuya.'
              : 'Speed depends on how new the card is, not just its memory, so we won\'t guess a number for yours.')
        + (c.kind === 'laptop' ? (es ? ' La versión para portátil de una tarjeta suele ir más lenta que la de sobremesa con el mismo nombre.' : ' The laptop version of a card is usually slower than the desktop one with the same name.') : '')]);
    } else {
      var l = laptopFor(R);
      out.push(['maybe', es ? 'Velocidad' : 'Speed',
        (es ? 'Lo más parecido que medimos: un ' : 'The closest PC we measured: the ') + a(l) + (es ? ' (' + l.ram + ' GB de RAM, sin tarjeta) escribía ' : ' (' + l.ram + ' GB of RAM, no card) wrote ')
        + speed(l) + (es ? ' con ' : ' with ') + l.engine + '. ' + (es ? 'Tú lees unos 8.' : 'You read about 5.')]);
    }
    // the bigger AI
    var big = D.big;
    if (gpu && v >= D.bigFloor) out.push(['yes', es ? 'La IA más grande (' + E['12b'].name + ')' : 'The bigger AI (' + E['12b'].name + ')',
      es ? 'Ocupa ' + n(E['12b'].gb) + ' GB y tu tarjeta tiene ' + v + ', así que cabe con sitio para chats largos. GreenCube la propone con tarjetas de ' + D.bigFloor + ' GB o más. Aún no la hemos medido con una tarjeta de ' + v + ' GB.'
         : 'It is ' + n(E['12b'].gb) + ' GB and your card has ' + v + ', so it fits with room for long chats. GreenCube suggests it on cards with ' + D.bigFloor + ' GB or more. We haven\'t measured it on a ' + v + ' GB card yet.']);
    else if (gpu && v >= 8 && big) out.push(['part', es ? 'La IA más grande (' + E['12b'].name + ')' : 'The bigger AI (' + E['12b'].name + ')',
      es ? 'Solo para chats cortos. En una ' + a(big.pc) + ' de 8 GB escribía ' + rng(big.writes) + ' tokens por segundo, y se colgó cuando el chat se hizo largo. GreenCube solo la propone con tarjetas de ' + D.bigFloor + ' GB o más.'
         : 'Short chats only. On an 8 GB ' + a(big.pc) + ' it wrote ' + rng(big.writes) + ' tokens a second, then crashed once the chat got long. GreenCube only suggests it on cards with ' + D.bigFloor + ' GB or more.']);
    else out.push(['no', es ? 'La IA más grande (' + E['12b'].name + ')' : 'The bigger AI (' + E['12b'].name + ')',
      es ? 'Necesita una tarjeta gráfica de ' + D.bigFloor + ' GB o más.' : 'It needs a graphics card with ' + D.bigFloor + ' GB or more.']);
    // pictures
    var P = es ? 'Imágenes' : 'Pictures';
    if (m && m.pic) out.push(['yes', P, (es ? 'Medido en una ' + esc(m.name) + ' real: una imagen en ' : 'Measured on a real ' + esc(m.name) + ': one picture in ') + secs(m.pic)
      + (m.first ? (es ? ' (la primera tardó ' + m.first + ' s mientras cargaba).' : ' (the first took ' + m.first + ' s while it loaded).') : '.')]);
    else if (!gpu && R <= 8) out.push(['no', P, es ? 'La IA de imágenes necesita unos 7 GB de memoria para ella sola, más de lo que puede liberar un PC de 8 GB.' : 'The picture AI needs about 7 GB of memory to itself, more than an 8 GB PC can free up.']);
    else if (R <= 8) out.push(['maybe', P, es ? 'No lo hemos probado en un PC con 8 GB de RAM: la IA de imágenes necesita unos 7 GB de memoria mientras carga.' : 'Not tested on a PC with 8 GB of RAM: the picture AI needs about 7 GB of memory while it loads.']);
    else if (gpu && v >= 8 && D.pics8) out.push(['yes', P, es ? 'En las ' + D.pics8.n + ' tarjetas de 8 GB o más que cronometramos, una imagen tardó entre ' + D.pics8.lo + ' y ' + D.pics8.hi + ' s.'
                                                         : 'On the ' + D.pics8.n + ' cards with 8 GB or more we timed, a picture took ' + D.pics8.lo + ' to ' + D.pics8.hi + ' s.']);
    else if (gpu && v >= 6 && D.pics6) out.push(['part', P, es ? 'En una ' + a(D.pics6.pc) + ' de 6 GB una imagen tardó ' + secs(D.pics6.t) + '. En otra tarjeta de 6 GB no quedaba sitio, así que GreenCube la hizo con el procesador, que tarda minutos.'
                                                          : 'On a 6 GB ' + a(D.pics6.pc) + ' a picture took ' + secs(D.pics6.t) + '. On another 6 GB card there was no room left, so GreenCube made it on the processor instead, which takes minutes.']);
    else if (gpu) out.push(['maybe', P, es ? 'Aún no lo hemos cronometrado en una tarjeta de ' + v + ' GB. Si la tarjeta está llena, GreenCube hace la imagen con el procesador, que tarda minutos.'
                                           : 'Not timed on a ' + v + ' GB card yet. If the card is full, GreenCube makes the picture on the processor instead, which takes minutes.']);
    else if (D.picLaptop) out.push(['part', P, es ? 'Sí, despacio: en nuestro portátil de 16 GB una imagen tardó ' + secs(D.picLaptop.chip) + ' con los gráficos Intel integrados y ' + secs(D.picLaptop.cpu) + ' solo con el procesador.'
                                                  : 'Yes, slowly: on our 16 GB laptop a picture took ' + secs(D.picLaptop.chip) + ' with the built-in Intel graphics and ' + secs(D.picLaptop.cpu) + ' on the processor alone.']);
    return out;
  }

  var ICON = { yes: '✓', part: '~', no: '✗', maybe: '?' };
  function show() {
    pressed();
    if (!state.card || state.vram === null || !state.ram) {
      out.innerHTML = state.card && state.vram === null ? '<p class="chk-wait">' + (es ? '¿Cuánta memoria tiene tu tarjeta?' : 'How much memory does your card have?') + '</p>'
                    : state.card && !state.ram ? '<p class="chk-wait">' + (es ? 'Ahora elige tu RAM.' : 'Now pick your RAM.') + '</p>' : '';
      return;
    }
    var r = rows(state.card, state.vram, state.ram);
    out.innerHTML = '<p class="chk-head">' + (es ? 'Sí, tu PC puede usar IA.' : 'Yes, your PC can run AI.') + '</p>'
      + '<ul class="chk-rows">' + r.map(function (x) {
          return '<li class="chk-' + x[0] + '"><span class="chk-ico" aria-hidden="true">' + ICON[x[0]] + '</span><div><h4>' + x[1] + '</h4><p>' + x[2] + '</p></div></li>';
        }).join('') + '</ul>'
      + '<p class="chk-send">' + (es ? '¿Ya usas GreenCube? Mándanos tu registro a <a href="mailto:support@greencube.app">support@greencube.app</a> y añadimos tu PC a las pruebas, con su propia página si es una tarjeta nueva.'
                                     : 'Already using GreenCube? Send your log to <a href="mailto:support@greencube.app">support@greencube.app</a> and we\'ll add your PC to the tests, with its own page if it\'s a new card.') + '</p>';
  }
  show();
})();
