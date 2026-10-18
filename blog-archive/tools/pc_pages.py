"""One page per measured PC, and the speed table in the "Can my PC run AI?" test, written from blog-archive/data/pcs.json.

build_blog.py calls pages() and table(). Every sentence that holds a number is written here from the data, so a
corrected number changes everywhere at once. A PC with no measured speed gets no page.
"""
import json, os, html

SRC = os.path.join(os.path.dirname(__file__), '..')
DATA = json.load(open(f'{SRC}/data/pcs.json', encoding='utf-8'))
ENG, METHODS = DATA['engines'], DATA['methods']
PCS = DATA['pcs']
HUB = {'en': 'can-my-pc-run-ai', 'es': 'ia-en-mi-pc'}
BIG = '12b'
BIG_FLOOR = 10      # GB of VRAM GreenCube asks for before it suggests the 12B
SLOW = 20           # tokens a second: below this, a card that holds the whole AI is "slow at AI"
ANSWER, DOC = 400, 5000  # tokens in a normal answer, and in a long document (about 7 pages)
READ_URL = 'https://doi.org/10.1016/j.jml.2019.104047'

def esc(s): return html.escape(s, quote=True)
def pick(lang, en, es): return en if lang == 'en' else es
def mid(r): return (r[0] + r[1]) / 2

def num(x, lang):
    s = f'{int(x):,}' if x == int(x) else f'{x:,.1f}'
    return s.translate(str.maketrans(',.', '.,')) if lang == 'es' else s

def rng(r, lang, approx=False):
    s = num(r[0], lang) if r[0] == r[1] else f'{num(r[0], lang)}–{num(r[1], lang)}'
    return pick(lang, 'about ', 'unos ') + s if approx else s

def rw(r, lang, approx=False):
    """The same range in whole numbers, for titles and sentences."""
    return rng([round(r[0]), round(r[1])], lang, approx)

def hl(pc, lang):
    """A PC's headline speed in whole numbers."""
    h = headline(pc)
    return rw(h['writes'], lang, h.get('approx'))

def secs(r, lang):
    """8–9 s, 28 s, 2:02–2:38 min"""
    r = [round(r[0]), round(r[1])]
    if r[1] < 90:
        return f'{r[0]} s' if r[0] == r[1] else f'{r[0]}–{r[1]} s'
    mm = lambda t: f'{t // 60}:{t % 60:02d}'
    return f'{mm(r[0])} min' if r[0] == r[1] else f'{mm(r[0])}–{mm(r[1])} min'

def times(tokens, speeds, lang):
    """How long `tokens` take at a measured speed range: the slow end of the speed gives the long time."""
    return secs([tokens / speeds[1], tokens / speeds[0]], lang)

def date(d, lang):
    y, m = d[:4], int(d[5:7])
    if lang == 'es':
        mes = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'][m - 1]
        return f'{int(d[8:10])} de {mes} de {y}' if len(d) > 7 else f'{mes} de {y}'
    mon = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][m - 1]
    return f'{int(d[8:10])} {mon} {y}' if len(d) > 7 else f'{mon} {y}'

def name(pc, lang, art=False):
    n = pc.get('name', {}).get(lang, pc['gpu'])
    return f'{pc["art"][lang]} {n}' if art else n

def label(pc, lang):
    return pc.get('label', {}).get(lang) or f'{pc["vendor"]} {pc["gpu"]}, {pc["vram"]} GB'

def an(n): return 'an' if str(n).startswith(('8', '11', '18')) else 'a'
def text_runs(pc): return [r for r in pc['runs'] if 'engine' in r]
def pictures(pc): return [r for r in pc['runs'] if 'picture' in r]
RANK = {'app': 2, 'bench': 2, 'app-test': 1}

def headline(pc):
    """The speed a person gets: real chats or the full benchmark before the short startup test; never the 12B or a second tester."""
    runs = [r for r in text_runs(pc) if r['engine'] != BIG and not r.get('second')]
    return max(runs, key=lambda r: (RANK[r['method']], r['writes'][0])) if runs else None

def card_vs_cpu(pc):
    """(card run, processor run) measured the same way on the same engine, or None."""
    for c in text_runs(pc):
        for p in text_runs(pc):
            if c['on'] == 'card' and p['on'] == 'cpu' and c['engine'] == p['engine'] and c['method'] == p['method']:
                return c, p
    return None

def times_x(cv, lang):
    x = mid(cv[0]['writes']) / mid(cv[1]['writes'])
    return num(round(x) if x >= 10 else round(x, 1), lang)

def method(r, lang): return METHODS[r['method']][lang].replace(' {v}', f' {r["v"]}' if r.get('v') else '')

W = {
    'en': dict(on={'card': 'graphics card', 'cpu': 'processor only', 'chip': 'built-in Intel graphics', 'split': 'graphics card, overflowing into RAM'},
               kind={'desktop': 'Desktop', 'laptop': 'Laptop'}, tps='tokens a second', writes='writing', reads='reading',
               pic='Picture (512×512)', first='the first took {f} s while it loaded',
               h_feel='What that means in practice', h_meas='What we measured', h_mean='What it means', h_cmp='How it compares',
               h_pc='The test PC', h_check='Check your own PC', h_more='Other PCs we measured',
               th=('What', 'Ran on', 'Result', 'Measured'), th_feel=('Task', 'Time on this PC'), how='How each number was measured:',
               ranges='Where we have several runs we show the range: speeds move a little between runs on the same PC.',
               spec=('Graphics', 'Graphics memory (VRAM)', 'RAM', 'Processor'), none='none (no separate graphics card)',
               all='All {n} PCs in one table, and what your PC will feel like', hub_t='Can my PC run AI?',
               q_run='Can {a} run AI locally?', q_pic='Can {a} make AI pictures?', q_cpu='Is AI faster on the {n} or on the processor?',
               q_big='Can {a} run Gemma 4 12B?'),
    'es': dict(on={'card': 'tarjeta gráfica', 'cpu': 'solo procesador', 'chip': 'gráficos Intel integrados', 'split': 'tarjeta gráfica, desbordando a la RAM'},
               kind={'desktop': 'Sobremesa', 'laptop': 'Portátil'}, tps='tokens por segundo', writes='escribiendo', reads='leyendo',
               pic='Imagen (512×512)', first='la primera tardó {f} s mientras cargaba',
               h_feel='Qué significa en la práctica', h_meas='Lo que medimos', h_mean='Qué significa', h_cmp='Cómo se compara',
               h_pc='El PC de la prueba', h_check='Mira tu propio PC', h_more='Otros PCs que medimos',
               th=('Qué', 'Dónde', 'Resultado', 'Medido'), th_feel=('Tarea', 'Tiempo en este PC'), how='Cómo se midió cada número:',
               ranges='Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC.',
               spec=('Gráfica', 'Memoria gráfica (VRAM)', 'RAM', 'Procesador'), none='ninguna (sin tarjeta gráfica aparte)',
               all='Los {n} PCs en una tabla, y cómo irá el tuyo', hub_t='¿Puedo usar IA en mi PC?',
               q_run='¿Puede {a} ejecutar IA en local?', q_pic='¿Puede {a} crear imágenes con IA?', q_cpu='¿La IA va más rápido en la {n} o en el procesador?',
               q_big='¿Puede {a} ejecutar Gemma 4 12B?'),
}

def where_phrase(pc, lang):
    """'a desktop with an NVIDIA RTX 5060 (8 GB) and 32 GB of RAM'"""
    if pc['kind'] == 'laptop':
        return pick(lang, f'a laptop with no graphics card ({pc["chip"]}) and {pc["ram"]} GB of RAM',
                    f'un portátil sin tarjeta gráfica ({pc["chip"]}) y {pc["ram"]} GB de RAM')
    return pick(lang, f'a desktop with an {pc["vendor"]} {pc["gpu"]} ({pc["vram"]} GB) and {pc["ram"]} GB of RAM',
                f'un sobremesa con una {pc["vendor"]} {pc["gpu"]} ({pc["vram"]} GB) y {pc["ram"]} GB de RAM')

def answer(pc, lang):
    h = headline(pc)
    sp = hl(pc, lang)
    eng = ENG[h['engine']]['name']
    lo = h['writes'][0]
    if lang == 'en':
        tail = ('You read about 5, so answers come out faster than you can read them.' if lo > 6 else
                'You read about 5, so answers come out at about reading speed.')
        return f'Yes. On {where_phrase(pc, lang)}, {eng} wrote {sp} tokens a second. {tail}'
    tail = 'Más rápido de lo que lees.' if lo > 9 else 'Más o menos a tu ritmo de lectura.'
    return f'Sí. En {where_phrase(pc, lang)}, {eng} escribía {sp} tokens por segundo. {tail}'

def picture_sentence(pc, lang):
    pics = pictures(pc)
    if pics:
        parts = []
        for r in pics:
            t = secs(r['picture'], lang)
            first = f' ({W[lang]["first"].format(f=r["first"])})' if r.get('first') else ''
            where = {'card': ('the graphics card', 'la tarjeta gráfica'), 'cpu': ('the processor alone', 'solo el procesador'),
                     'chip': ('the built-in Intel graphics', 'los gráficos Intel integrados')}[r['on']]
            parts.append(pick(lang, f'{t} on {where[0]}{first}', f'{t} con {where[1]}{first}'))
        return pick(lang, 'Yes. One picture (512×512) took ' + ', and '.join(parts) + '.',
                    'Sí. Una imagen (512×512) tardó ' + ', y '.join(parts) + '.')
    if pc['kind'] == 'laptop' and pc['ram'] <= 8:
        return pick(lang, f'No. The picture AI needs about 7 GB of memory to itself, more than {an(pc["ram"])} {pc["ram"]} GB laptop can free up. Chat and study work fine.',
                    f'No. La IA de imágenes necesita unos 7 GB de memoria para ella sola, más de lo que puede liberar un portátil de {pc["ram"]} GB. Chatear y estudiar sí funcionan.')
    return pick(lang, 'Very likely, but we haven\'t timed a picture on this card yet. When we do, the number goes here.',
                'Muy probablemente, pero aún no hemos cronometrado una imagen con esta tarjeta. Cuando lo hagamos, el número irá aquí.')

def big_sentence(pc, lang):
    """What we know about the 12B on this PC, or None for laptops."""
    if pc['kind'] != 'desktop': return None
    b = ENG[BIG]
    big = [r for r in text_runs(pc) if r['engine'] == BIG]
    if big and big[0].get('crash'):
        r = big[0]
        return pick(lang, f'Only for short chats. The bigger {b["name"]} ({num(b["gb"], lang)} GB) wrote {rng(r["writes"], lang)} tokens a second on a short question, but once the chat reached {num(r["crash"], lang)} tokens (a long conversation) it crashed, with the card almost full. That is why GreenCube only suggests the 12B on cards with {BIG_FLOOR} GB or more.',
                    f'Solo para chats cortos. La más grande, {b["name"]} ({num(b["gb"], lang)} GB), escribía {rng(r["writes"], lang)} tokens por segundo con una pregunta corta, pero cuando el chat llegó a {num(r["crash"], lang)} tokens (una conversación larga) se colgó, con la tarjeta casi llena. Por eso GreenCube solo propone la 12B con tarjetas de {BIG_FLOOR} GB o más.')
    if pc['vram'] >= BIG_FLOOR:
        return pick(lang, f'It should. {b["name"]} is a {num(b["gb"], lang)} GB file and this card has {pc["vram"]} GB, which leaves room for a long conversation too. We haven\'t measured it on this card yet.',
                    f'Debería. {b["name"]} ocupa {num(b["gb"], lang)} GB y esta tarjeta tiene {pc["vram"]}, así que queda sitio también para una conversación larga. Aún no la hemos medido con esta tarjeta.')
    ref = next((p for p in PCS if any(r['engine'] == BIG and r.get('crash') for r in text_runs(p))), None)
    tail = pick(lang, f' On an 8 GB {ref["vendor"]} {ref["gpu"]} it answered short questions, then crashed in a long chat.',
                f' En una {ref["vendor"]} {ref["gpu"]} de 8 GB respondió preguntas cortas y luego se colgó en un chat largo.') if ref else ''
    return pick(lang, f'Not comfortably. GreenCube suggests the bigger {b["name"]} only on cards with {BIG_FLOOR} GB or more of VRAM, and this one has {pc["vram"]}.{tail}',
                f'No con holgura. GreenCube solo propone la más grande, {b["name"]}, con tarjetas de {BIG_FLOOR} GB de VRAM o más, y esta tiene {pc["vram"]}.{tail}')

def page_path(pc, lang): return f'/blog/{pc["slug"]["en"]}' if lang == 'en' else f'/blog/es/{pc["slug"]["es"]}'
def link(pc, lang): return f'<a href="{page_path(pc, lang)}">{esc(name(pc, lang))}</a>'
def with_page(): return [p for p in PCS if p.get('slug') and headline(p)]
def ranked(): return sorted(with_page(), key=lambda p: -mid(headline(p)['writes']))
def the(pc, lang):
    """'la RX 6600' / 'el portátil con…' / 'the RX 6600'"""
    return pick(lang, 'the', 'el' if pc['kind'] == 'laptop' else 'la')

def insights(pc, lang):
    """(tint, heading, html) cards, each built from a rule and the numbers."""
    out = []
    h = headline(pc)
    e = ENG[h['engine']]
    hs = hl(pc, lang)
    cv = card_vs_cpu(pc)
    if cv:
        c, p = cv
        out.append(('g', pick(lang, 'The graphics card does the work', 'La tarjeta gráfica hace el trabajo'),
            pick(lang, f'Same PC, same AI ({ENG[c["engine"]]["name"]}): {rng(p["writes"], lang)} tokens a second on the processor alone, {rng(c["writes"], lang)} on the graphics card, about <strong>{times_x(cv, lang)} times faster</strong>. A graphics card is built to do thousands of small sums at once for games, and running an AI is mostly that same kind of maths. GreenCube times both when it starts and uses the faster one.',
                 f'Mismo PC, misma IA ({ENG[c["engine"]]["name"]}): {rng(p["writes"], lang)} tokens por segundo solo con el procesador y {rng(c["writes"], lang)} con la tarjeta gráfica, unas <strong>{times_x(cv, lang)} veces más rápido</strong>. Una gráfica está hecha para hacer miles de cuentas pequeñas a la vez para los juegos, y una IA es sobre todo ese mismo tipo de cálculo. GreenCube cronometra las dos al arrancar y usa la más rápida.')))
    if h['on'] == 'card' and h['writes'][0] >= SLOW:
        out.append(('b', pick(lang, 'The whole AI fits on the card', 'La IA entera cabe en la tarjeta'),
            pick(lang, f'{e["name"]} is a {num(e["gb"], lang)} GB file and the card has {pc["vram"]} GB of its own memory (VRAM). All of it fits, with room left for the conversation, so the card never waits for the slower memory in the rest of the PC. That is the biggest reason it runs this fast.',
                 f'{e["name"]} ocupa {num(e["gb"], lang)} GB y la tarjeta tiene {pc["vram"]} GB de memoria propia (VRAM). Cabe entera, con sitio de sobra para la conversación, así que la tarjeta nunca espera a la memoria más lenta del resto del PC. Esa es la razón principal de que vaya tan rápido.')))
    elif h['on'] == 'card':
        peers = [p for p in ranked() if p is not pc and p['vram'] == pc['vram'] and p['kind'] == 'desktop']
        cmp = pick(lang, ' For comparison, other {v} GB cards we measured write {l} with the same AI.', ' Para comparar, otras tarjetas de {v} GB que medimos escriben {l} con la misma IA.').format(
            v=pc['vram'], l=', '.join(f'{hl(p, lang)} ({link(p, lang)})' for p in peers[:3])) if peers else ''
        out.append(('b', pick(lang, 'It fits, but this card is slow at AI', 'Cabe, pero esta tarjeta es lenta para IA'),
            pick(lang, f'{e["name"]} ({num(e["gb"], lang)} GB) fits whole in the card\'s {pc["vram"]} GB, yet it writes only {hs} tokens a second. Older cards are much slower at this kind of maths, and more memory does not change that.{cmp} It still writes faster than you read, so chat and study work; it just feels slower than a newer card.',
                 f'{e["name"]} ({num(e["gb"], lang)} GB) cabe entera en los {pc["vram"]} GB de la tarjeta, y aun así solo escribe {hs} tokens por segundo. Las tarjetas antiguas son mucho más lentas en este tipo de cálculo, y tener más memoria no lo arregla.{cmp} Sigue escribiendo más rápido de lo que lees, así que chatear y estudiar funcionan; solo se nota más lenta que una tarjeta nueva.')))
    elif h['on'] == 'split':
        rd = h.get('reads')
        swing = pick(lang, f' Reading what you paste swung between {num(rd[0], lang)} and {num(rd[1], lang)} tokens a second from one day to the next, most likely because the card was full.',
                     f' La lectura de lo que pegas osciló entre {num(rd[0], lang)} y {num(rd[1], lang)} tokens por segundo de un día a otro, seguramente porque la tarjeta estaba llena.') if rd and rd[0] != rd[1] else ''
        out.append(('b', pick(lang, 'Not all of it fits on the card', 'No cabe entera en la tarjeta'),
            pick(lang, f'{e["name"]} is a {num(e["gb"], lang)} GB file and the card has {pc["vram"]} GB, so it does not fit whole and part of it sits in the normal memory (RAM). Every word it writes has to reach that part over a much slower path, so speed drops and moves around. It still writes {hs} tokens a second.{swing}',
                 f'{e["name"]} ocupa {num(e["gb"], lang)} GB y la tarjeta tiene {pc["vram"]}, así que no cabe entera y una parte queda en la memoria normal (RAM). Cada palabra que escribe tiene que llegar a esa parte por un camino mucho más lento, así que la velocidad baja y varía. Aun así escribe {hs} tokens por segundo.{swing}')))
    else:
        other = [r for r in text_runs(pc) if r['engine'] != h['engine'] and r['on'] == h['on'] and r['method'] == h['method']]
        cmp = pick(lang, f' The bigger {ENG[other[0]["engine"]]["name"]} works too, at {rng(other[0]["writes"], lang)}: smarter, but you will feel the wait on long answers.',
                   f' La más grande, {ENG[other[0]["engine"]]["name"]}, también funciona, a {rng(other[0]["writes"], lang)}: más lista, pero en respuestas largas se nota la espera.') if other else ''
        chip = [r for r in text_runs(pc) if r['on'] == 'chip' and r['engine'] == h['engine']]
        cpu_t = [r for r in text_runs(pc) if r['on'] == 'cpu' and r['engine'] == h['engine'] and chip and r['method'] == chip[0]['method']]
        chip_s = pick(lang, f' GreenCube\'s startup test also tried the built-in Intel graphics for writing: {rng(chip[0]["writes"], lang)}, against {rng(cpu_t[0]["writes"], lang)} on the processor, so it writes on the processor here.',
                      f' La prueba de arranque de GreenCube también probó a escribir con los gráficos Intel integrados: {rng(chip[0]["writes"], lang)}, frente a {rng(cpu_t[0]["writes"], lang)} con el procesador, así que aquí escribe con el procesador.') if chip and cpu_t else ''
        out.append(('b', pick(lang, 'No graphics card? It still works', '¿Sin tarjeta gráfica? Funciona igual'),
            pick(lang, f'With no graphics card, the AI runs on the processor. It is slower than on a gaming PC, but the smaller {e["name"]} still writes {hs} tokens a second, enough to study, summarise and write with.{cmp}{chip_s}',
                 f'Sin tarjeta gráfica, la IA funciona en el procesador. Va más lenta que en un PC gaming, pero la pequeña, {e["name"]}, escribe {hs} tokens por segundo, suficiente para estudiar, resumir y escribir.{cmp}{chip_s}')))
    for r in text_runs(pc):
        if r.get('second'):
            short = pick(lang, ' Most of its answers were short, and short answers measure slower than long ones: its longest came near the top of that range.',
                         ' La mayoría de sus respuestas fueron cortas, y las respuestas cortas salen más lentas que las largas: la más larga quedó cerca del máximo.') if r.get('short') else ''
            reads = pick(lang, f', and read at {rng(r["reads"], lang)}', f' y leía a {rng(r["reads"], lang)}') if r.get('reads') else ''
            out.append(('g', pick(lang, 'A second PC with the same card', 'Un segundo PC con la misma tarjeta'),
                pick(lang, f'Another tester\'s {pc["gpu"]} ran {ENG[r["engine"]]["name"]} in GreenCube {r.get("v", "")}: it wrote {rng(r["writes"], lang)} tokens a second{reads}.{short}',
                     f'La {pc["gpu"]} de otro tester usó {ENG[r["engine"]]["name"]} en GreenCube {r.get("v", "")}: escribía {rng(r["writes"], lang)} tokens por segundo{reads}.{short}')))
    bs = big_sentence(pc, lang)
    if bs:
        out.append(('y', pick(lang, f'The bigger {ENG[BIG]["name"]}', f'La más grande, {ENG[BIG]["name"]}'), esc(bs)))
    why = pick(lang, ' A picture uses its own AI of about 6 GB and far more maths than a chat answer, so the graphics matter even more here.',
               ' Una imagen usa su propia IA, de unos 6 GB, y muchas más cuentas que una respuesta de chat, así que aquí los gráficos importan todavía más.')
    out.append(('p', pick(lang, 'Pictures', 'Imágenes'), esc(picture_sentence(pc, lang)) + (why if pictures(pc) or pc['kind'] == 'desktop' else '')))
    return out

def feel(pc, lang):
    """Task -> time on this PC, worked out from the measured speeds."""
    h = headline(pc)
    rows = [(pick(lang, f'Write a normal answer ({ANSWER} tokens, about 300 words)', f'Escribir una respuesta normal ({ANSWER} tokens, media página)'), times(ANSWER, h['writes'], lang))]
    if h.get('reads'):
        rows.append((pick(lang, f'Read a long document you give it ({num(DOC, lang)} tokens, about 7 pages)', f'Leer un documento largo que le das ({num(DOC, lang)} tokens, unas 6 páginas)'), times(DOC, h['reads'], lang)))
    for r in pictures(pc):
        on = pick(lang, {'card': '', 'cpu': ', processor alone', 'chip': ', built-in graphics'}[r['on']], {'card': '', 'cpu': ', solo procesador', 'chip': ', gráficos integrados'}[r['on']])
        rows.append((pick(lang, f'Make a picture (512×512{on})', f'Crear una imagen (512×512{on})'), secs(r['picture'], lang) + (pick(lang, f' (first: {r["first"]} s)', f' (la primera: {r["first"]} s)') if r.get('first') else '')))
    L = W[lang]
    t = ('<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{x}</th>' for x in L['th_feel']) + '</tr></thead>\n<tbody>\n'
         + '\n'.join(f'<tr><td>{esc(a)}</td><td><b>{esc(b)}</b></td></tr>' for a, b in rows) + '\n</tbody>\n</table></div>\n')
    return t + pick(lang,
        f'<p>Worked out from the speeds measured on this PC: time is length divided by speed, and a real answer also spends a moment getting started. For scale, most people read about 4 words a second (<a href="{READ_URL}" rel="noopener">Brysbaert, 2019</a>), so a {ANSWER}-token answer takes you over a minute just to read.</p>\n',
        f'<p>Calculado a partir de las velocidades medidas en este PC: el tiempo es la longitud dividida entre la velocidad, y una respuesta real tarda además un momento en arrancar. Para hacerte una idea, una persona lee unas 4 palabras por segundo (<a href="{READ_URL}" rel="noopener">Brysbaert, 2019</a>), así que solo leer una respuesta de {ANSWER} tokens te lleva más de un minuto.</p>\n')

def measured_table(pc, lang):
    L = W[lang]
    methods = []
    for r in pc['runs']:
        if r['method'] not in methods: methods.append(r['method'])
    rows = []
    for r in pc['runs']:
        if 'engine' in r:
            res = f'<b>{rng(r["writes"], lang, r.get("approx"))}</b> {L["tps"]} {L["writes"]}'
            if r.get('reads'):
                res += f' &middot; {rng(r["reads"], lang)} {L["reads"]}'
            what = ENG[r['engine']]['name'] + (pick(lang, ' (second PC)', ' (segundo PC)') if r.get('second') else '') + ('*' if r.get('short') else '')
        else:
            res = f'<b>{secs(r["picture"], lang)}</b>' + (f' ({L["first"].format(f=r["first"])})' if r.get('first') else '')
            what = L['pic']
        sup = f' <sup>{methods.index(r["method"]) + 1}</sup>' if len(methods) > 1 else ''
        rows.append(f'<tr><td>{what}</td><td>{L["on"][r["on"]]}</td><td>{res}</td><td>{date(r["date"], lang)}{sup}</td></tr>')
    def versions(m):  # every GreenCube version behind one method on this page
        vs = list(dict.fromkeys(r['v'] for r in pc['runs'] if r['method'] == m and r.get('v')))
        return {'method': m, 'v': pick(lang, ' and ', ' y ').join(vs)} if vs else {'method': m}
    how = ''.join(f'<li>{esc(method(versions(m), lang))}</li>' for m in methods)
    intro = pick(lang,
        '<p><strong>Writing</strong> is how fast the AI types its answer, in tokens a second; a token is about three quarters of an English word. <strong>Reading</strong> is how fast it takes in what you give it: your question, a pasted text or a PDF. Reading is always much faster than writing, because the AI can read many tokens at once but has to write them one by one.</p>\n',
        '<p><strong>Escribir</strong> es la velocidad a la que la IA teclea su respuesta, en tokens por segundo; un token es un trozo de palabra, y en español cada palabra suele ocupar uno o dos. <strong>Leer</strong> es lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Leer siempre es mucho más rápido que escribir, porque la IA puede leer muchos tokens a la vez pero tiene que escribirlos de uno en uno.</p>\n')
    return (intro + '<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in L['th']) + '</tr></thead>\n<tbody>\n'
            + '\n'.join(rows) + '\n</tbody>\n</table></div>\n'
            f'<p>{L["how"]}</p><ol class="src">{how}</ol>\n<p>{L["ranges"]}'
            + (pick(lang, ' * This tester mostly asked short questions, so answers under 100 tokens are counted too. Short answers measure a little slower.',
                    ' * Este tester hizo sobre todo preguntas cortas, así que también cuentan las respuestas de menos de 100 tokens. Las respuestas cortas salen algo más lentas.') if any(r.get('short') for r in pc['runs']) else '')
            + '</p>\n')

def compare(pc, lang):
    eng = headline(pc)['engine']
    order = [p for p in ranked() if headline(p)['engine'] == eng]
    k = order.index(pc)
    m = mid(headline(pc)['writes'])
    def faster(a, b):
        """'about 45% faster' / 'about 2.5 times as fast' / None when within 5%."""
        x = a / b
        if x >= 2: return pick(lang, f'about {num(round(x, 1), lang)} times as fast', f'unas {num(round(x, 1), lang)} veces más rápido')
        p = round((x - 1) * 20) * 5  # to the nearest 5%
        return pick(lang, f'about {p}% faster', f'un {p}% más rápido') if p >= 5 else None
    def tag(p):  # a speed from the short startup test is marked, since it is not the same test as real chats
        return pick(lang, ' (startup test)', ' (prueba de arranque)') if headline(p)['method'] == 'app-test' else ''
    e = ENG[eng]['name']
    parts = [pick(lang, f'Of the {len(order)} PCs we measured with {e}, this one is <strong>number {k + 1}</strong> for writing speed.',
                  f'De los {len(order)} PCs que medimos con {e}, este es el <strong>número {k + 1}</strong> en velocidad de escritura.')]
    if k > 0:
        up = order[k - 1]; f = faster(mid(headline(up)['writes']), m)
        parts.append(pick(lang, f'The {link(up, lang)} writes {hl(up, lang)}{tag(up)}, ' + (f'{f}.' if f else 'about the same.'),
                          f'{the(up, lang).capitalize()} {link(up, lang)} escribe {hl(up, lang)}{tag(up)}, ' + (f'{f}.' if f else 'más o menos lo mismo.')))
    if k + 1 < len(order):
        dn = order[k + 1]; f = faster(m, mid(headline(dn)['writes']))
        parts.append(pick(lang, f'The {link(dn, lang)} writes {hl(dn, lang)}{tag(dn)}, so this one is ' + (f'{f}.' if f else 'about as fast.'),
                          f'{the(dn, lang).capitalize()} {link(dn, lang)} escribe {hl(dn, lang)}{tag(dn)}, así que este va ' + (f'{f}.' if f else 'más o menos igual.')))
    out = '<p>' + ' '.join(parts) + '</p>\n'
    peers = [p for p in order if p['vram'] == pc['vram'] and p['kind'] == 'desktop']
    if pc['kind'] == 'desktop' and len(peers) >= 3:
        items = ''.join(f'<li>{link(p, lang) if p is not pc else "<strong>" + esc(name(p, lang)) + "</strong>"}: {hl(p, lang)} {W[lang]["tps"]}{tag(p)}</li>\n' for p in peers)
        out += pick(lang, f'<p>We measured {len(peers)} cards with {pc["vram"]} GB, and they are far apart:</p>\n<ul>\n{items}</ul>\n<p>Memory decides which AI fits. How new the card is decides how fast it runs.</p>\n',
                    f'<p>Medimos {len(peers)} tarjetas de {pc["vram"]} GB, y hay mucha diferencia entre ellas:</p>\n<ul>\n{items}</ul>\n<p>La memoria decide qué IA cabe. Lo nueva que sea la tarjeta decide lo rápido que va.</p>\n')
    return out

CHECK = {
    'en': '<ol class="steps">\n<li>Press <strong>Ctrl + Shift + Esc</strong> to open Task Manager.</li>\n<li>Go to <strong>Performance</strong>.</li>\n<li>Click <strong>Memory</strong>: the number at the top right is your RAM.</li>\n<li>Click <strong>GPU</strong>: the name at the top right is your card, and <strong>Dedicated GPU memory</strong> is your VRAM. Only see Intel or AMD graphics with no dedicated memory? Then you have no separate card.</li>\n</ol>\n',
    'es': '<ol class="steps">\n<li>Pulsa <strong>Ctrl + Mayús + Esc</strong> para abrir el Administrador de tareas.</li>\n<li>Ve a <strong>Rendimiento</strong>.</li>\n<li>Pulsa <strong>Memoria</strong>: el número de arriba a la derecha es tu RAM.</li>\n<li>Pulsa <strong>GPU</strong>: el nombre de arriba a la derecha es tu tarjeta, y <strong>Memoria de GPU dedicada</strong> es tu VRAM. ¿Solo ves gráficos Intel o AMD sin memoria dedicada? Entonces no tienes tarjeta aparte.</li>\n</ol>\n',
}

def pages(lang):
    """[(slug, meta, body)] for every measured PC in this language."""
    L = W[lang]
    out = []
    hub = f'/blog/{HUB["en"]}' if lang == 'en' else f'/blog/es/{HUB["es"]}'
    for pc in with_page():
        h = headline(pc)
        sp = hl(pc, lang)
        a = name(pc, lang, art=True)
        title = pick(lang, f'Can {a} run AI? Measured: {sp} tokens a second', f'¿Puede {a} ejecutar IA? Medido: {sp} tokens por segundo')
        ans = answer(pc, lang)
        pic = picture_sentence(pc, lang)
        desc = pick(lang, f'Real test: {ENG[h["engine"]]["name"]} wrote {sp} tokens a second on {where_phrase(pc, lang)}. What it means for chat, study and pictures.',
                    f'Prueba real: {ENG[h["engine"]]["name"]} escribía {sp} tokens por segundo en {where_phrase(pc, lang)}. Qué significa para chatear, estudiar e imágenes.')
        faq = [{'q': L['q_run'].format(a=a), 'a': ans}, {'q': L['q_pic'].format(a=a), 'a': pic}]
        cv = card_vs_cpu(pc)
        if cv:
            faq.append({'q': L['q_cpu'].format(n=name(pc, lang)),
                        'a': pick(lang, f'On the card, by far: {rng(cv[0]["writes"], lang)} tokens a second against {rng(cv[1]["writes"], lang)} on the processor, about {times_x(cv, lang)} times faster.',
                                  f'En la tarjeta, de largo: {rng(cv[0]["writes"], lang)} tokens por segundo frente a {rng(cv[1]["writes"], lang)} en el procesador, unas {times_x(cv, lang)} veces más rápido.')})
        if big_sentence(pc, lang):
            faq.append({'q': L['q_big'].format(a=a), 'a': big_sentence(pc, lang)})
        latest = max(r['date'] for r in pc['runs'])
        latest = latest if len(latest) > 7 else latest + '-01'
        meta = {'title': title[0].upper() + title[1:], 'description': desc, 'date': latest, 'lang': lang, 'kind': 'pc',
                'alt': pc['slug']['es' if lang == 'en' else 'en'], 'faq': faq}
        first, rest = ans.split(' ', 1)
        body = f'<div class="answer"><p><strong>{esc(first)}</strong> {esc(rest)}</p></div>\n'
        st = [('g', sp, pick(lang, f'tokens a second with {ENG[h["engine"]]["name"]}', f'tokens por segundo con {ENG[h["engine"]]["name"]}'))]
        if cv: st.append(('b', times_x(cv, lang) + '×', pick(lang, 'faster on the card than on the processor', 'más rápido en la tarjeta que en el procesador')))
        if pictures(pc): st.append(('p', secs(pictures(pc)[0]['picture'], lang), pick(lang, 'to make a picture', 'para crear una imagen')))
        for r in text_runs(pc):
            if len(st) < 3 and r['engine'] != h['engine'] and r['method'] == h['method'] and not r.get('second'):
                st.append(('y', rng(r['writes'], lang), pick(lang, f'with {ENG[r["engine"]]["name"]}', f'con {ENG[r["engine"]]["name"]}') + (pick(lang, ' (short chats only)', ' (solo chats cortos)') if r.get('crash') else '')))
        body += '<div class="stats">\n' + '\n'.join(f'<div class="stat {t}"><b>{esc(b)}</b><span>{esc(s)}</span></div>' for t, b, s in st[:3]) + '\n</div>\n'
        body += f'<h2>{L["h_feel"]}</h2>\n' + feel(pc, lang)
        body += f'<h2>{L["h_meas"]}</h2>\n' + measured_table(pc, lang)
        body += f'<h2>{L["h_mean"]}</h2>\n' + ''.join(f'<div class="card {t}">\n<h3>{esc(hd)}</h3>\n<p>{tx}</p>\n</div>\n' for t, hd, tx in insights(pc, lang))
        body += f'<h2>{L["h_cmp"]}</h2>\n' + compare(pc, lang)
        spec = (pick(lang, 'built-in Intel graphics only', 'solo gráficos Intel integrados') if pc['kind'] == 'laptop' else f'{pc["vendor"]} {pc["gpu"]}',
                L['none'] if not pc['vram'] else f'{pc["vram"]} GB', f'{pc["ram"]} GB', pc['cpu'].replace('threads', pick(lang, 'threads', 'hilos')))
        body += (f'<h2>{L["h_pc"]}</h2>\n<p>' + pick(lang, 'A real tester\'s own PC, used the way they normally use it, not a lab machine:', 'El PC de un tester real, usado como lo usa siempre, no una máquina de laboratorio:')
                 + f'</p>\n<ul>\n<li>{L["kind"][pc["kind"]]}</li>\n' + ''.join(f'<li><strong>{k}:</strong> {esc(v)}</li>\n' for k, v in zip(L['spec'], spec)) + '</ul>\n')
        body += (f'<h2>{L["h_check"]}</h2>\n' + pick(lang, '<p>Not sure what your PC has? It takes 30 seconds:</p>\n', '<p>¿No sabes qué tiene tu PC? Se mira en 30 segundos:</p>\n') + CHECK[lang]
                 + pick(lang, f'<p>Then find the closest card in <a href="{hub}">the full table</a>. The same card with more VRAM can fit a bigger AI; a newer card of the same size is usually faster.</p>\n',
                        f'<p>Después busca la tarjeta más parecida en <a href="{hub}">la tabla completa</a>. La misma tarjeta con más VRAM puede con una IA más grande; una tarjeta más nueva del mismo tamaño suele ir más rápido.</p>\n'))
        others = ''.join(f'<li>{link(o, lang)}: {hl(o, lang)} {L["tps"]} ({ENG[headline(o)["engine"]]["name"]})</li>\n' for o in ranked() if o is not pc)
        body += (f'<h2>{L["h_more"]}</h2>\n<ul>\n{others}</ul>\n'
                 f'<p><a href="{hub}">{L["hub_t"]}</a> {L["all"].format(n=count())}.</p>\n')
        out.append((pc['slug'][lang], meta, body))
    return out

def count(): return len([p for p in PCS if headline(p)])

def table(lang):
    """The speed table in the "Can my PC run AI?" test: one row per measured PC, fastest first, linked to its page."""
    L = W[lang]
    pcs = sorted([p for p in PCS if headline(p)], key=lambda p: -mid(headline(p)['writes']))
    top = max(headline(p)['writes'][1] for p in pcs)
    rows = []
    for p in pcs:
        h = headline(p)
        g = esc(label(p, lang))
        if p.get('slug'): g = f'<a href="{page_path(p, lang)}">{g}</a>'
        lo = '' if h['on'] in ('card', 'split') else ' lo'
        rows.append(f'<tr><td>{L["kind"][p["kind"]]}</td><td>{g}</td><td>{p["ram"]} GB</td><td>{ENG[h["engine"]]["name"]}</td>'
                    f'<td class="spd"><span class="bar{lo}" style="--w:{round(100 * h["writes"][1] / top)}%"></span><b>{hl(p, lang)}</b></td></tr>')
    head = pick(lang, ('PC', 'Graphics', 'RAM', 'AI model', 'Writes (tokens/s)'), ('PC', 'Gráfica', 'RAM', 'IA', 'Escribe (tokens/s)'))
    return ('<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in head) + '</tr></thead>\n<tbody>\n'
            + '\n'.join(rows) + '\n</tbody>\n</table></div>')

# ---------- the checker inside "Can my PC run AI?": picker + verdicts, all numbers from pcs.json ----------
GPUS = json.load(open(f'{SRC}/data/gpus.json', encoding='utf-8'))
JS = open(os.path.join(os.path.dirname(__file__), 'checker.js'), encoding='utf-8').read()

def checker(lang):
    """The checker's HTML and script for one language."""
    def whole(r): return [round(r[0]), round(r[1])]
    pcs = []
    for p in with_page():
        h = headline(p)
        pic = next((r for r in pictures(p) if r['on'] == 'card'), None)
        pcs.append({'vendor': p['vendor'], 'model': p['gpu'], 'vram': p['vram'], 'kind': p['kind'], 'ram': p['ram'],
                    'name': name(p, lang), 'url': page_path(p, lang), 'writes': whole(h['writes']), 'approx': bool(h.get('approx')),
                    'test': h['method'] == 'app-test', 'engine': ENG[h['engine']]['name'],
                    'pic': whole(pic['picture']) if pic else None, 'first': pic.get('first') if pic else None})
    ref = next((p for p in with_page() for r in text_runs(p) if r['engine'] == BIG and r.get('crash')), None)
    big = ({'pc': {'name': name(ref, lang), 'url': page_path(ref, lang)},
            'writes': whole(next(r for r in text_runs(ref) if r['engine'] == BIG)['writes'])} if ref else None)
    p8 = [(p, r) for p in with_page() if p['kind'] == 'desktop' and p['vram'] >= 8 for r in pictures(p) if r['on'] == 'card']
    p6 = [(p, r) for p in with_page() if p['kind'] == 'desktop' and 6 <= p['vram'] < 8 for r in pictures(p) if r['on'] == 'card']
    lap = next((p for p in with_page() if p['kind'] == 'laptop' and any(r['on'] == 'chip' for r in pictures(p))), None)
    data = {'lang': lang, 'groups': GPUS['groups'], 'pcs': pcs, 'engines': ENG, 'bigFloor': BIG_FLOOR, 'big': big,
            'pics8': {'n': len(p8), 'lo': min(r['picture'][0] for _, r in p8), 'hi': max(r['picture'][1] for _, r in p8)} if p8 else None,
            'pics6': {'pc': {'name': name(p6[0][0], lang), 'url': page_path(p6[0][0], lang)}, 't': p6[0][1]['picture']} if p6 else None,
            'picLaptop': {'chip': next(r['picture'] for r in pictures(lap) if r['on'] == 'chip'),
                          'cpu': next(r['picture'] for r in pictures(lap) if r['on'] == 'cpu')} if lap else None}
    opts = ''
    i = 0
    for g in GPUS['groups']:
        items = ''
        for model, _ in g['cards']:
            shown = GPUS['builtin'][lang] if g['kind'] == 'none' else f'{g["vendor"]} {model}'.replace('NVIDIA RTX', 'NVIDIA GeForce RTX').replace('NVIDIA GTX', 'NVIDIA GeForce GTX').replace('AMD RX', 'AMD Radeon RX').replace(' Laptop', pick(lang, ' Laptop', ' (portátil)'))
            items += f'<option value="{i}">{esc(shown)}</option>'
            i += 1
        opts += f'<optgroup label="{esc(g["label"][lang])}">{items}</optgroup>'
    T = pick(lang,
        dict(h='Will AI run on your PC?', lead='Pick your graphics card and RAM: you get what runs, how fast it ran on real PCs, and what we haven\'t measured yet.',
             card='Graphics card', choose='Pick your card…', vram='Card memory (VRAM)', ram='RAM', more='32 GB or more',
             help='Not sure what you have? <a href="#by-hand">Check in Task Manager</a>, it takes 30 seconds.',
             priv='This runs in your browser. Nothing about your PC is sent anywhere.', nojs='Turn on JavaScript to use the checker, or read the table below.'),
        dict(h='¿Funcionará la IA en tu PC?', lead='Elige tu tarjeta gráfica y tu RAM: verás qué funciona, a qué velocidad fue en PCs reales y qué no hemos medido aún.',
             card='Tarjeta gráfica', choose='Elige tu tarjeta…', vram='Memoria de la tarjeta (VRAM)', ram='RAM', more='32 GB o más',
             help='¿No sabes qué tienes? <a href="#by-hand">Míralo en el Administrador de tareas</a>, se tarda 30 segundos.',
             priv='Esto funciona en tu navegador. No se envía nada sobre tu PC a ningún sitio.', nojs='Activa JavaScript para usar el comprobador, o mira la tabla de abajo.'))
    return (f'<section class="chk" id="chk">\n<h2 id="checker">{T["h"]}</h2>\n<p class="chk-lead">{T["lead"]}</p>\n'
            f'<p class="chk-detect" id="chk-detect">{T["nojs"]}</p>\n'
            f'<div class="chk-q"><label for="chk-card">{T["card"]}</label><select id="chk-card"><option value="">{T["choose"]}</option>{opts}</select></div>\n'
            f'<div class="chk-q" id="chk-vram" hidden><span>{T["vram"]}</span><div class="chk-opts"></div></div>\n'
            f'<div class="chk-q" id="chk-ram"><span>{T["ram"]}</span><div class="chk-opts"><button type="button" data-ram="8">8 GB</button>'
            f'<button type="button" data-ram="16">16 GB</button><button type="button" data-ram="32">{T["more"]}</button></div></div>\n'
            f'<p class="chk-help">{T["help"]}</p>\n<div id="chk-out" aria-live="polite"></div>\n<p class="chk-priv">{T["priv"]}</p>\n</section>\n'
            '<script>' + JS.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False).replace('</', r'<\/')) + '</script>\n')
