"""One page per measured PC, and the speed table in the "Can my PC run AI?" test, written from blog-archive/data/pcs.json.

build_blog.py calls pages() and table(); every sentence that holds a number is written here from the data, so a
corrected number changes everywhere at once. A PC with no measured speed (or no known model) gets no page.
"""
import json, os, html

SRC = os.path.join(os.path.dirname(__file__), '..')
DATA = json.load(open(f'{SRC}/data/pcs.json', encoding='utf-8'))
ENG, METHODS = DATA['engines'], DATA['methods']
PCS = DATA['pcs']
HUB = {'en': 'can-my-pc-run-ai', 'es': 'ia-en-mi-pc'}
BIG = '12b'
BIG_FLOOR = 10  # GB of VRAM GreenCube asks for before it suggests the 12B
READ = {'en': 5, 'es': 8}  # tokens a second a person reads (about 4 words; Spanish words take more tokens)

def esc(s): return html.escape(s, quote=True)

def num(x, lang):
    s = f'{int(x):,}' if x == int(x) else f'{x:,.1f}'
    return s.translate(str.maketrans(',.', '.,')) if lang == 'es' else s

def rng(r, lang, approx=False):
    s = num(r[0], lang) if r[0] == r[1] else f'{num(r[0], lang)}–{num(r[1], lang)}'
    return ({'en': 'about ', 'es': 'unos '}[lang] + s) if approx else s

def secs(r, lang):
    if r[1] < 90:
        return (f'{r[0]} s' if r[0] == r[1] else f'{r[0]}–{r[1]} s')
    mm = lambda t: f'{t // 60}:{t % 60:02d}'
    return f'{mm(r[0])} min' if r[0] == r[1] else f'{mm(r[0])}–{mm(r[1])} min'

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

def text_runs(pc): return [r for r in pc['runs'] if 'engine' in r]
def pictures(pc): return [r for r in pc['runs'] if 'picture' in r]

def headline(pc):
    """The speed a person gets in GreenCube: the fastest everyday engine, not the startup test or the 12B."""
    runs = [r for r in text_runs(pc) if r['method'] != 'app-test' and r['engine'] != BIG]
    return max(runs, key=lambda r: r['writes'][0]) if runs else None

def card_vs_cpu(pc):
    """(card run, processor run) measured the same way on the same engine, or None."""
    for c in text_runs(pc):
        for p in text_runs(pc):
            if c['on'] == 'card' and p['on'] == 'cpu' and c['engine'] == p['engine'] and c['method'] == p['method']:
                return c, p
    return None

def method(r, lang):
    return METHODS[r['method']][lang].replace('{v}', r.get('v', '')).replace('  ', ' ').replace(' ,', ',')

W = {
    'en': dict(on={'card': 'graphics card', 'cpu': 'processor only', 'chip': 'built-in Intel graphics', 'split': 'graphics card, overflowing into RAM'},
               kind={'desktop': 'Desktop', 'laptop': 'Laptop'}, tps='tokens a second', writes='writing', reads='reading',
               pic='picture (512×512)', first='the first took {f} s while it loaded',
               h_meas='What we measured', h_mean='What it means', h_pc='The test PC', h_more='Other PCs we measured',
               th=('What', 'Ran on', 'Result', 'Measured'), how='How we measured:',
               ranges='Where we have several runs we show the range: speeds move a little between runs on the same PC.',
               spec=('Graphics', 'Graphics memory (VRAM)', 'RAM', 'Processor'), none='none (no separate graphics card)',
               all='All {n} PCs side by side, and how to check yours', hub_t='Can my PC run AI?',
               q_run='Can {a} run AI locally?', q_pic='Can {a} make AI pictures?', q_cpu='Is AI faster on the {n} or on the processor?'),
    'es': dict(on={'card': 'tarjeta gráfica', 'cpu': 'solo procesador', 'chip': 'gráficos Intel integrados', 'split': 'tarjeta gráfica, desbordando a la RAM'},
               kind={'desktop': 'Sobremesa', 'laptop': 'Portátil'}, tps='tokens por segundo', writes='escribiendo', reads='leyendo',
               pic='imagen (512×512)', first='la primera tardó {f} s mientras cargaba',
               h_meas='Lo que medimos', h_mean='Qué significa', h_pc='El PC de la prueba', h_more='Otros PCs que medimos',
               th=('Qué', 'Dónde', 'Resultado', 'Medido'), how='Cómo lo medimos:',
               ranges='Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC.',
               spec=('Gráfica', 'Memoria gráfica (VRAM)', 'RAM', 'Procesador'), none='ninguna (sin tarjeta gráfica aparte)',
               all='Los {n} PCs juntos, y cómo mirar el tuyo', hub_t='¿Puedo usar IA en mi PC?',
               q_run='¿Puede {a} ejecutar IA en local?', q_pic='¿Puede {a} crear imágenes con IA?', q_cpu='¿La IA va más rápido en la {n} o en el procesador?'),
}

def where_phrase(pc, lang):
    """'a desktop with an NVIDIA RTX 5060 (8 GB) and 32 GB of RAM'"""
    if pc['kind'] == 'laptop':
        return {'en': f'a laptop with no graphics card ({pc["chip"]}) and {pc["ram"]} GB of RAM',
                'es': f'un portátil sin tarjeta gráfica ({pc["chip"]}) y {pc["ram"]} GB de RAM'}[lang]
    return {'en': f'a desktop with {"an" if pc["vendor"] in ("NVIDIA", "AMD", "Intel") else "a"} {pc["vendor"]} {pc["gpu"]} ({pc["vram"]} GB) and {pc["ram"]} GB of RAM',
            'es': f'un sobremesa con una {pc["vendor"]} {pc["gpu"]} ({pc["vram"]} GB) y {pc["ram"]} GB de RAM'}[lang]

def answer(pc, lang):
    h = headline(pc)
    sp = rng(h['writes'], lang, h.get('approx'))
    eng = ENG[h['engine']]['name']
    fast = h['writes'][0] > READ[lang]
    if lang == 'en':
        return (f'Yes. On {where_phrase(pc, lang)}, {eng} wrote {sp} tokens a second. '
                + ('You read about 5, so answers come out faster than you can read them.' if fast else 'That is about as fast as you read.'))
    return (f'Sí. En {where_phrase(pc, lang)}, {eng} escribía {sp} tokens por segundo. '
            + ('Más rápido de lo que lees.' if fast else 'Más o menos a tu ritmo de lectura.'))

def picture_sentence(pc, lang):
    pics = pictures(pc)
    if pics:
        parts = []
        for r in pics:
            t = secs(r['picture'], lang)
            on = W[lang]['on'][r['on']]
            first = f' ({W[lang]["first"].format(f=r["first"])})' if r.get('first') else ''
            parts.append({'en': f'{t} on the {on}{first}', 'es': f'{t} en {"la " if r["on"] == "card" else "el " if r["on"] == "cpu" else "los "}{on.replace("solo ", "")}{first}'}[lang])
        return {'en': 'Yes. One picture (512×512) took ' + ', and '.join(parts) + '.',
                'es': 'Sí. Una imagen (512×512) tardó ' + ', y '.join(parts) + '.'}[lang]
    if pc['kind'] == 'laptop' and pc['ram'] <= 8:
        return {'en': f'No. The picture AI needs about 7 GB of memory to itself, more than {"an" if str(pc["ram"]).startswith(("8", "11", "18")) else "a"} {pc["ram"]} GB laptop can free up. Chat and study work fine.',
                'es': f'No. La IA de imágenes necesita unos 7 GB de memoria para ella sola, más de lo que puede liberar un portátil de {pc["ram"]} GB. Chatear y estudiar sí funcionan.'}[lang]
    return {'en': 'We haven\'t timed pictures on this one yet. When we do, the number goes here.',
            'es': 'Aún no hemos cronometrado imágenes en este PC. Cuando lo hagamos, el número irá aquí.'}[lang]

def insights(pc, lang, by_id):
    """(tint, heading, text) cards, each built from a rule and the numbers."""
    out = []
    h = headline(pc)
    cv = card_vs_cpu(pc)
    if cv:
        c, p = cv
        x = c['writes'][1] / p['writes'][1]
        xs = num(round(x) if x >= 10 else round(x, 1), lang)
        out.append(('g', {'en': f'The card is {xs}× faster than the processor', 'es': f'La tarjeta va {xs} veces más rápido que el procesador'}[lang],
                    {'en': f'Same PC, same AI ({ENG[c["engine"]]["name"]}): {rng(p["writes"], lang)} tokens a second on the processor alone, {rng(c["writes"], lang)} on the graphics card. AI is the kind of maths graphics cards are built for.',
                     'es': f'Mismo PC, misma IA ({ENG[c["engine"]]["name"]}): {rng(p["writes"], lang)} tokens por segundo solo con el procesador y {rng(c["writes"], lang)} con la tarjeta gráfica. Una IA es justo el tipo de cálculo para el que están hechas las gráficas.'}[lang]))
    e = ENG[h['engine']]
    if h['on'] == 'card':
        out.append(('b', {'en': 'The whole AI fits on the card', 'es': 'La IA entera cabe en la tarjeta'}[lang],
                    {'en': f'{e["name"]} is a {num(e["gb"], lang)} GB file and the card has {pc["vram"]} GB of its own memory (VRAM), so all of it runs on the card. That is what makes it this fast.',
                     'es': f'{e["name"]} ocupa {num(e["gb"], lang)} GB y la tarjeta tiene {pc["vram"]} GB de memoria propia (VRAM), así que funciona entera en la tarjeta. Por eso va tan rápido.'}[lang]))
    elif h['on'] == 'split':
        rd = h.get('reads')
        swing = ({'en': f' Reading what you paste swung between {num(rd[0], lang)} and {num(rd[1], lang)} tokens a second from one day to the next, most likely because the card was full.',
                  'es': f' La lectura de lo que pegas osciló entre {num(rd[0], lang)} y {num(rd[1], lang)} tokens por segundo de un día a otro, seguramente porque la tarjeta estaba llena.'}[lang] if rd and rd[0] != rd[1] else '')
        out.append(('b', {'en': 'Not all of it fits on the card', 'es': 'No cabe entera en la tarjeta'}[lang],
                    {'en': f'{e["name"]} is a {num(e["gb"], lang)} GB file and the card has {pc["vram"]} GB, so it does not fit whole and part of it sits in the normal memory (RAM). It still writes {rng(h["writes"], lang, h.get("approx"))} tokens a second.{swing}',
                     'es': f'{e["name"]} ocupa {num(e["gb"], lang)} GB y la tarjeta tiene {pc["vram"]} GB, así que no cabe entera y una parte queda en la memoria normal del PC (RAM). Aun así escribe {rng(h["writes"], lang, h.get("approx"))} tokens por segundo.{swing}'}[lang]))
    else:
        other = [r for r in text_runs(pc) if r['engine'] != h['engine'] and r['on'] == h['on']]
        cmp = ({'en': f' The bigger {ENG[other[0]["engine"]]["name"]} works too, at {rng(other[0]["writes"], lang)}.',
                'es': f' La más grande, {ENG[other[0]["engine"]]["name"]}, también funciona, a {rng(other[0]["writes"], lang)}.'}[lang] if other else '')
        chip = [r for r in text_runs(pc) if r['on'] == 'chip' and r['engine'] == h['engine']]
        chip_s = ({'en': f' Running it on the built-in Intel graphics was slower here ({rng(chip[0]["writes"], lang)}), so the processor is the better place.',
                   'es': f' En los gráficos Intel integrados iba más lento ({rng(chip[0]["writes"], lang)}), así que es mejor el procesador.'}[lang] if chip else '')
        out.append(('b', {'en': 'No graphics card? It still works', 'es': '¿Sin tarjeta gráfica? Funciona igual'}[lang],
                    {'en': f'With no card, the AI runs on the processor. The smaller {e["name"]} wrote {rng(h["writes"], lang)} tokens a second.{cmp}{chip_s}',
                     'es': f'Sin tarjeta, la IA funciona en el procesador. La pequeña, {e["name"]}, escribía {rng(h["writes"], lang)} tokens por segundo.{cmp}{chip_s}'}[lang]))
    if pc['kind'] == 'desktop':
        big = [r for r in text_runs(pc) if r['engine'] == BIG]
        b = ENG[BIG]
        if big and big[0].get('crash'):
            r = big[0]
            out.append(('y', {'en': f'{b["name"]}: fast, then it crashed', 'es': f'{b["name"]}: rápida, y luego se colgó'}[lang],
                        {'en': f'The bigger {b["name"]} ({num(b["gb"], lang)} GB) wrote {rng(r["writes"], lang)} tokens a second on a short question. Once the chat reached {r["crash"]:,} tokens (a long conversation), it crashed, with the card almost full. That is why GreenCube only suggests the 12B on cards with {BIG_FLOOR} GB or more.',
                         'es': f'La más grande, {b["name"]} ({num(b["gb"], lang)} GB), escribía {rng(r["writes"], lang)} tokens por segundo con una pregunta corta. Cuando el chat llegó a {r["crash"]:,} tokens (una conversación larga), se colgó, con la tarjeta casi llena. Por eso GreenCube solo propone la 12B con tarjetas de {BIG_FLOOR} GB o más.'}[lang].replace(f'{r["crash"]:,}', f'{r["crash"]:,}'.replace(',', '.') if lang == 'es' else f'{r["crash"]:,}')))
        elif pc['vram'] >= BIG_FLOOR:
            out.append(('y', {'en': f'Room for {b["name"]}', 'es': f'Hay sitio para {b["name"]}'}[lang],
                        {'en': f'With {pc["vram"]} GB, the bigger {b["name"]} ({num(b["gb"], lang)} GB) should fit on this card too. We haven\'t measured it here yet.',
                         'es': f'Con {pc["vram"]} GB, la más grande, {b["name"]} ({num(b["gb"], lang)} GB), también debería caber en esta tarjeta. Aún no la hemos medido aquí.'}[lang]))
        else:
            ref = next((p for p in PCS if any(r['engine'] == BIG and r.get('crash') for r in text_runs(p))), None)
            link = f'<a href="{page_path(ref, lang)}">{ref["vendor"]} {ref["gpu"]}</a>' if ref else ''
            out.append(('y', {'en': f'{b["name"]} needs a bigger card', 'es': f'{b["name"]} necesita una tarjeta más grande'}[lang],
                        {'en': f'GreenCube suggests the bigger {b["name"]} only on cards with {BIG_FLOOR} GB or more.' + (f' On an 8 GB {link} it answered short questions, then crashed in a long chat.' if link else ''),
                         'es': f'GreenCube solo propone la más grande, {b["name"]}, con tarjetas de {BIG_FLOOR} GB o más.' + (f' En una {link} de 8 GB respondió preguntas cortas y luego se colgó en un chat largo.' if link else '')}[lang]))
    out.append(('p', {'en': 'Pictures', 'es': 'Imágenes'}[lang], picture_sentence(pc, lang)))
    return out

def page_path(pc, lang): return f'/blog/{pc["slug"]["en"]}' if lang == 'en' else f'/blog/es/{pc["slug"]["es"]}'
def with_page(): return [p for p in PCS if p.get('slug') and headline(p)]

def stats(pc, lang):
    h = headline(pc)
    out = [('g', rng(h['writes'], lang, h.get('approx')), {'en': f'tokens a second with {ENG[h["engine"]]["name"]}', 'es': f'tokens por segundo con {ENG[h["engine"]]["name"]}'}[lang])]
    cv = card_vs_cpu(pc)
    if cv:
        x = cv[0]['writes'][1] / cv[1]['writes'][1]
        out.append(('b', num(round(x) if x >= 10 else round(x, 1), lang) + '×', {'en': 'faster on the card than on the processor', 'es': 'más rápido en la tarjeta que en el procesador'}[lang]))
    pics = pictures(pc)
    if pics:
        r = pics[0]
        out.append(('p', secs(r['picture'], lang), {'en': 'to make a picture', 'es': 'para crear una imagen'}[lang]))
    for r in text_runs(pc):
        if len(out) >= 3: break
        if r['engine'] != h['engine'] and r['method'] != 'app-test':
            out.append(('y', rng(r['writes'], lang), {'en': f'with {ENG[r["engine"]]["name"]}', 'es': f'con {ENG[r["engine"]]["name"]}'}[lang]
                        + ({'en': ' (short chats only)', 'es': ' (solo chats cortos)'}[lang] if r.get('crash') else '')))
    return out[:3]

def measured_table(pc, lang):
    L = W[lang]
    rows = []
    for r in pc['runs']:
        if 'engine' in r:
            res = f'<b>{rng(r["writes"], lang, r.get("approx"))}</b> {L["tps"]} {L["writes"]}'
            if r.get('reads'):
                res += f' &middot; {rng(r["reads"], lang, r.get("approx_reads"))} {L["reads"]}'
            what = ENG[r['engine']]['name']
        else:
            res = f'<b>{secs(r["picture"], lang)}</b>' + (f' ({L["first"].format(f=r["first"])})' if r.get('first') else '')
            what = L['pic']
        mark = sorted({x['method'] for x in pc['runs']}).index(r['method']) + 1
        sup = f' <sup>{mark}</sup>' if len({x['method'] for x in pc['runs']}) > 1 else ''
        rows.append(f'<tr><td>{what}</td><td>{L["on"][r["on"]]}</td><td>{res}</td><td>{date(r["date"], lang)}{sup}</td></tr>')
    how = ''.join(f'<li value="{i}">{esc(method(next(r for r in pc["runs"] if r["method"] == m), lang))}</li>'
                  for i, m in enumerate(sorted({x['method'] for x in pc['runs']}), 1))
    return (f'<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in L['th']) + '</tr></thead>\n<tbody>\n'
            + '\n'.join(rows) + '\n</tbody>\n</table></div>\n'
            f'<p>{L["how"]}</p><ol class="src">{how}</ol>\n<p>{L["ranges"]}</p>\n')

def pages(lang):
    """[(slug, meta, body)] for every measured PC in this language."""
    L = W[lang]
    out = []
    pcs = with_page()
    for pc in pcs:
        h = headline(pc)
        sp = rng(h['writes'], lang, h.get('approx'))
        a = name(pc, lang, art=True)
        title = {'en': f'Can {a} run AI? Measured: {sp} tokens a second', 'es': f'¿Puede {a} ejecutar IA? Medido: {sp} tokens por segundo'}[lang]
        title = title[0].upper() + title[1:]
        ans = answer(pc, lang)
        pic = picture_sentence(pc, lang)
        desc = {'en': f'Real test: {ENG[h["engine"]]["name"]} wrote {sp} tokens a second on {where_phrase(pc, lang)}. What it means for chat, study and pictures.',
                'es': f'Prueba real: {ENG[h["engine"]]["name"]} escribía {sp} tokens por segundo en {where_phrase(pc, lang)}. Qué significa para chatear, estudiar e imágenes.'}[lang]
        faq = [{'q': L['q_run'].format(a=a), 'a': ans}, {'q': L['q_pic'].format(a=a), 'a': pic}]
        cv = card_vs_cpu(pc)
        if cv:
            x = cv[0]['writes'][1] / cv[1]['writes'][1]
            faq.append({'q': L['q_cpu'].format(n=name(pc, lang)),
                        'a': {'en': f'On the card, by far: {rng(cv[0]["writes"], lang)} tokens a second against {rng(cv[1]["writes"], lang)} on the processor, about {num(round(x) if x >= 10 else round(x, 1), lang)} times faster.',
                              'es': f'En la tarjeta, de largo: {rng(cv[0]["writes"], lang)} tokens por segundo frente a {rng(cv[1]["writes"], lang)} en el procesador, unas {num(round(x) if x >= 10 else round(x, 1), lang)} veces más rápido.'}[lang]})
        latest = max(r['date'] for r in pc['runs'])
        latest = latest if len(latest) > 7 else latest + '-01'
        meta = {'title': title, 'description': desc, 'date': latest, 'lang': lang, 'kind': 'pc', 'alt': pc['slug']['es' if lang == 'en' else 'en'], 'faq': faq}
        body = f'<div class="answer"><p><strong>{esc(ans.split(" ", 1)[0])}</strong> {esc(ans.split(" ", 1)[1])}</p></div>\n'
        body += '<div class="stats">\n' + '\n'.join(f'<div class="stat {t}"><b>{esc(b)}</b><span>{esc(s)}</span></div>' for t, b, s in stats(pc, lang)) + '\n</div>\n'
        body += f'<h2>{L["h_meas"]}</h2>\n' + measured_table(pc, lang)
        body += f'<h2>{L["h_mean"]}</h2>\n' + ''.join(f'<div class="card {t}">\n<h3>{esc(hd)}</h3>\n<p>{tx if "<a " in tx else esc(tx)}</p>\n</div>\n' for t, hd, tx in insights(pc, lang, None))
        spec = ({'en': 'built-in Intel graphics only', 'es': 'solo gráficos Intel integrados'}[lang] if pc['kind'] == 'laptop' else f'{pc["vendor"]} {pc["gpu"]}',
                L['none'] if not pc['vram'] else f'{pc["vram"]} GB', f'{pc["ram"]} GB', pc['cpu'].replace('threads', {'en': 'threads', 'es': 'hilos'}[lang]))
        body += f'<h2>{L["h_pc"]}</h2>\n<ul>\n<li>{L["kind"][pc["kind"]]}</li>\n' + ''.join(f'<li><strong>{k}:</strong> {esc(v)}</li>\n' for k, v in zip(L['spec'], spec)) + '</ul>\n'
        others = ''.join(f'<li><a href="{page_path(o, lang)}">{esc(label(o, lang))}</a>: {rng(headline(o)["writes"], lang, headline(o).get("approx"))} {L["tps"]}</li>\n'
                         for o in pcs if o is not pc)
        hub = f'/blog/{HUB["en"]}' if lang == 'en' else f'/blog/es/{HUB["es"]}'
        body += (f'<h2>{L["h_more"]}</h2>\n<ul>\n{others}</ul>\n'
                 f'<p><a href="{hub}">{L["hub_t"]}</a> {L["all"].format(n=count())}.</p>\n')
        out.append((pc['slug'][lang], meta, body))
    return out

def count(): return len([p for p in PCS if headline(p)])

def table(lang):
    """The speed table in the "Can my PC run AI?" test: one row per measured PC, fastest first, linked to its page."""
    L = W[lang]
    pcs = sorted([p for p in PCS if headline(p)], key=lambda p: -headline(p)['writes'][0])
    top = max(headline(p)['writes'][1] for p in pcs)
    rows = []
    for p in pcs:
        h = headline(p)
        g = esc(label(p, lang))
        if p.get('slug'): g = f'<a href="{page_path(p, lang)}">{g}</a>'
        lo = '' if h['on'] in ('card', 'split') else ' lo'
        rows.append(f'<tr><td>{L["kind"][p["kind"]]}</td><td>{g}</td><td>{p["ram"]} GB</td><td>{ENG[h["engine"]]["name"]}</td>'
                    f'<td class="spd"><span class="bar{lo}" style="--w:{round(100 * h["writes"][1] / top)}%"></span><b>{rng(h["writes"], lang, h.get("approx"))}</b></td></tr>')
    head = {'en': ('PC', 'Graphics', 'RAM', 'AI model', 'Writes (tokens/s)'), 'es': ('PC', 'Gráfica', 'RAM', 'IA', 'Escribe (tokens/s)')}[lang]
    return ('<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in head) + '</tr></thead>\n<tbody>\n'
            + '\n'.join(rows) + '\n</tbody>\n</table></div>')
