"""One page per measured PC, and the speed table in the "Can my PC run AI?" test, written from blog-archive/data/pcs.json.

build_blog.py calls pages() and table(). Every sentence that holds a number is written here from the data, so a
corrected number changes everywhere at once. A PC with no measured speed gets no page. The words for each language
live in words/<lang>.json (the same keys in every language); this file only decides which sentence fits and fills in
the numbers.
"""
import json, os, html, re

SRC = os.path.join(os.path.dirname(__file__), '..')
DATA = json.load(open(f'{SRC}/data/pcs.json', encoding='utf-8'))
ENG = DATA['engines']
PCS = DATA['pcs']
WORDS_DIR = os.path.join(os.path.dirname(__file__), 'words')
WD = {f[:-5]: json.load(open(os.path.join(WORDS_DIR, f), encoding='utf-8')) for f in sorted(os.listdir(WORDS_DIR)) if f.endswith('.json')}
HUB = {'en': 'can-my-pc-run-ai', 'es': 'ia-en-mi-pc'}  # other languages use the English slug
BIG = '12b'
BIG_FLOOR = 10      # GB of VRAM GreenCube asks for before it suggests the 12B
SLOW = 20           # tokens a second: below this, a card that holds the whole AI is "slow at AI"
ANSWER, DOC = 400, 5000  # tokens in a normal answer, and in a long document (about 7 pages)
READ_URL = 'https://doi.org/10.1016/j.jml.2019.104047'

def esc(s): return html.escape(s, quote=True)
# Plural rules for languages whose words change with the number ("1 токен, 2 токена, 5 токенов").
# A template picks a form with {x|one|few|many|other}: the word only, chosen from the number in {x}.
PLURAL = {'ru': 'east-slavic', 'uk': 'east-slavic'}

def plural(lang, v):
    """Which form a number takes: 0 one, 1 few, 2 many, 3 other (fractions). Uses the last number in v ('5–7', 'около 20')."""
    th, dec = WD[lang]['num_sep']
    nums = re.findall(r'\d+(?:' + re.escape(dec) + r'\d+)?', str(v).replace(th, ''))
    if not nums or dec in nums[-1]: return 3
    n = int(nums[-1])
    if n % 10 == 1 and n % 100 != 11: return 0
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return 1
    return 2

def fmt(lang, s, **f):
    """str.format, plus the {x|one|few|many|other} plural forms for languages in PLURAL."""
    if lang in PLURAL:
        s = re.sub(r'\{(\w+)\|([^{}]*)\}', lambda m: m[2].split('|')[plural(lang, f[m[1]])], s)
    out = s.format(**f)
    if s.startswith('{') and s.rstrip()[-1:] in '.?!':  # a sentence that opens with a name ('ноутбук с …') starts with a capital
        out = re.sub(r'^((?:<[^>]*>)*)([^\W\d_])', lambda m: m[1] + m[2].upper(), out, count=1)
    return out

def after(lang, n, s):
    """A word that follows a number ('tokens a second'), with {_|one|few|many|other} picked from that number."""
    return re.sub(r'\{_\|([^{}]*)\}', lambda m: m[1].split('|')[plural(lang, n)], s) if lang in PLURAL else s

def tx(lang, key, **f):
    s = WD[lang][key]
    return fmt(lang, s, **f) if f else s
def mid(r): return (r[0] + r[1]) / 2
def gb(lang): return WD[lang]['gb']  # 'GB', 'Go', 'ГБ'

def blog_path(lang, slug): return f'/blog/{slug}' if lang == 'en' else f'/blog/{lang}/{slug}'
def hub_path(lang): return blog_path(lang, HUB.get(lang, HUB['en']))

def num(x, lang):
    s = f'{int(x):,}' if x == int(x) else f'{x:,.1f}'
    th, dec = WD[lang]['num_sep']
    return ''.join({',': th, '.': dec}.get(c, c) for c in s)

def rng(r, lang, approx=False):
    s = num(r[0], lang) if r[0] == r[1] else f'{num(r[0], lang)}–{num(r[1], lang)}'
    return tx(lang, 'about', x=s) if approx else s

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
    s, m = WD[lang].get('units', ['s', 'min'])
    if r[1] < 90:
        return f'{r[0]} {s}' if r[0] == r[1] else f'{r[0]}–{r[1]} {s}'
    mm = lambda t: f'{t // 60}:{t % 60:02d}'
    return f'{mm(r[0])} {m}' if r[0] == r[1] else f'{mm(r[0])}–{mm(r[1])} {m}'

def times(tokens, speeds, lang):
    """How long `tokens` take at a measured speed range: the slow end of the speed gives the long time."""
    return secs([tokens / speeds[1], tokens / speeds[0]], lang)

def date(d, lang):
    """'2026-10-21' -> '21 October 2026'; '2026-10' -> 'October 2026', in the language's own order."""
    L, m = WD[lang], int(d[5:7])
    if len(d) > 7:
        return L['date_day'].format(d=int(d[8:10]), month=L['months'][m - 1], m=m, y=d[:4])
    return L['date_month'].format(month=L['months'][m - 1], m=m, y=d[:4])

def words_for(pc, lang): return WD[lang]['pcs'].get(pc['id'], {})

def name(pc, lang, art=False):
    n = words_for(pc, lang).get('name', pc['gpu'])
    if not art: return n
    a = words_for(pc, lang).get('art', WD[lang]['art'][pc['kind']])
    return f'{a} {n}' if a else n

def label(pc, lang):
    return words_for(pc, lang).get('label') or f'{pc["vendor"]} {pc["gpu"]}, {pc["vram"]} {gb(lang)}'

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

def method(r, lang): return WD[lang]['methods'][r['method']].replace(' {v}', f' {r["v"]}' if r.get('v') else '')

def where_phrase(pc, lang):
    """'a desktop with an NVIDIA RTX 5060 (8 GB) and 32 GB of RAM'"""
    if pc['kind'] == 'laptop':
        return tx(lang, 'where_laptop', chip=words_for(pc, lang).get('chip', pc['chip']), ram=pc['ram'])
    return tx(lang, 'where_desktop', vendor=pc['vendor'], gpu=pc['gpu'], vram=pc['vram'], ram=pc['ram'])

def answer(pc, lang):
    h = headline(pc)
    tail = tx(lang, 'answer_fast' if h['writes'][0] > WD[lang]['read_fast_above'] else 'answer_ok')
    return tx(lang, 'answer', where=where_phrase(pc, lang), eng=ENG[h['engine']]['name'], sp=hl(pc, lang), tail=tail)

def picture_sentence(pc, lang):
    pics = pictures(pc)
    if pics:
        parts = []
        for r in pics:
            first = f' ({WD[lang]["pc"]["first"].format(f=r["first"])})' if r.get('first') else ''
            parts.append(tx(lang, 'pic_part', t=secs(r['picture'], lang), where=WD[lang]['pic_where'][r['on']], first=first))
        return tx(lang, 'pic_yes', parts=WD[lang]['pic_join'].join(parts))
    if pc['kind'] == 'laptop' and pc['ram'] <= 8:
        return tx(lang, 'pic_no_laptop', an=an(pc['ram']), ram=pc['ram'])
    return tx(lang, 'pic_unknown')

def big_sentence(pc, lang):
    """What we know about the 12B on this PC, or None for laptops."""
    if pc['kind'] != 'desktop': return None
    b = ENG[BIG]
    big = [r for r in text_runs(pc) if r['engine'] == BIG]
    if big and big[0].get('crash'):
        r = big[0]
        return tx(lang, 'big_crash', name=b['name'], gb=num(b['gb'], lang), writes=rng(r['writes'], lang), crash=num(r['crash'], lang), floor=BIG_FLOOR)
    if pc['vram'] >= BIG_FLOOR:
        return tx(lang, 'big_fits', name=b['name'], gb=num(b['gb'], lang), vram=pc['vram'])
    ref = next((p for p in PCS if any(r['engine'] == BIG and r.get('crash') for r in text_runs(p))), None)
    tail = tx(lang, 'big_ref', ref=f'{ref["vendor"]} {ref["gpu"]}') if ref else ''
    return tx(lang, 'big_no', name=b['name'], floor=BIG_FLOOR, vram=pc['vram'], tail=tail)

def pc_slug(pc, lang): return pc['slug'].get(lang, pc['slug']['en'])
def page_path(pc, lang): return blog_path(lang, pc_slug(pc, lang))
def link(pc, lang): return f'<a href="{page_path(pc, lang)}">{esc(name(pc, lang))}</a>'
def with_page(): return [p for p in PCS if p.get('slug') and headline(p)]
def ranked(): return sorted(with_page(), key=lambda p: -mid(headline(p)['writes']))
def the(pc, lang):
    """'la RX 6600' / 'el portátil con…' / 'the RX 6600'"""
    return WD[lang]['the'][pc['kind']]

def insights(pc, lang):
    """(tint, heading, html) cards, each built from a rule and the numbers."""
    out = []
    h = headline(pc)
    e = ENG[h['engine']]
    hs = hl(pc, lang)
    cv = card_vs_cpu(pc)
    if cv:
        c, p = cv
        out.append(('g', tx(lang, 'ins_card_h'), tx(lang, 'ins_card', eng=ENG[c['engine']]['name'], cpu=rng(p['writes'], lang),
                                                       card=rng(c['writes'], lang), x=times_x(cv, lang))))
    if h['on'] == 'card' and h['writes'][0] >= SLOW:
        out.append(('b', tx(lang, 'ins_fits_h'), tx(lang, 'ins_fits', name=e['name'], gb=num(e['gb'], lang), vram=pc['vram'])))
    elif h['on'] == 'card':
        peers = [p for p in ranked() if p is not pc and p['vram'] == pc['vram'] and p['kind'] == 'desktop']
        cmp = tx(lang, 'ins_slow_cmp', v=pc['vram'], l=WD[lang]['list_sep'].join(f'{hl(p, lang)} ({link(p, lang)})' for p in peers[:3])) if peers else ''
        out.append(('b', tx(lang, 'ins_slow_h'), tx(lang, 'ins_slow', name=e['name'], gb=num(e['gb'], lang), vram=pc['vram'], hs=hs, cmp=cmp)))
    elif h['on'] == 'split':
        rd = h.get('reads')
        swing = tx(lang, 'ins_split_swing', lo=num(rd[0], lang), hi=num(rd[1], lang)) if rd and rd[0] != rd[1] else ''
        out.append(('b', tx(lang, 'ins_split_h'), tx(lang, 'ins_split', name=e['name'], gb=num(e['gb'], lang), vram=pc['vram'], hs=hs, swing=swing)))
    else:
        other = [r for r in text_runs(pc) if r['engine'] != h['engine'] and r['on'] == h['on'] and r['method'] == h['method']]
        cmp = tx(lang, 'ins_cpu_cmp', name=ENG[other[0]['engine']]['name'], writes=rng(other[0]['writes'], lang)) if other else ''
        chip = [r for r in text_runs(pc) if r['on'] == 'chip' and r['engine'] == h['engine']]
        cpu_t = [r for r in text_runs(pc) if r['on'] == 'cpu' and r['engine'] == h['engine'] and chip and r['method'] == chip[0]['method']]
        chip_s = tx(lang, 'ins_cpu_chip', chip=rng(chip[0]['writes'], lang), cpu=rng(cpu_t[0]['writes'], lang)) if chip and cpu_t else ''
        out.append(('b', tx(lang, 'ins_cpu_h'), tx(lang, 'ins_cpu', name=e['name'], hs=hs, cmp=cmp, chip=chip_s)))
    for r in text_runs(pc):
        if r.get('second'):
            short = tx(lang, 'ins_second_short') if r.get('short') else ''
            reads = tx(lang, 'ins_second_reads', reads=rng(r['reads'], lang)) if r.get('reads') else ''
            out.append(('g', tx(lang, 'ins_second_h'), tx(lang, 'ins_second', gpu=pc['gpu'], eng=ENG[r['engine']]['name'], v=r.get('v', ''),
                                                             writes=rng(r['writes'], lang), reads=reads, short=short)))
    bs = big_sentence(pc, lang)
    if bs:
        out.append(('y', tx(lang, 'ins_big_h', name=ENG[BIG]['name']), esc(bs)))
    why = tx(lang, 'ins_pic_why')
    out.append(('p', tx(lang, 'ins_pic_h'), esc(picture_sentence(pc, lang)) + (why if pictures(pc) or pc['kind'] == 'desktop' else '')))
    return out

def feel(pc, lang):
    """Task -> time on this PC, worked out from the measured speeds."""
    h = headline(pc)
    rows = [(tx(lang, 'feel_answer', n=ANSWER), times(ANSWER, h['writes'], lang))]
    if h.get('reads'):
        rows.append((tx(lang, 'feel_doc', n=num(DOC, lang)), times(DOC, h['reads'], lang)))
    for r in pictures(pc):
        rows.append((tx(lang, 'feel_pic', on=WD[lang]['feel_on'][r['on']]),
                     secs(r['picture'], lang) + (tx(lang, 'feel_first', f=r['first']) if r.get('first') else '')))
    L = WD[lang]['pc']
    t = ('<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{x}</th>' for x in L['th_feel']) + '</tr></thead>\n<tbody>\n'
         + '\n'.join(f'<tr><td>{esc(a)}</td><td><b>{esc(b)}</b></td></tr>' for a, b in rows) + '\n</tbody>\n</table></div>\n')
    return t + tx(lang, 'feel_note', url=READ_URL, n=ANSWER)

def measured_table(pc, lang):
    L = WD[lang]['pc']
    methods = []
    for r in pc['runs']:
        if r['method'] not in methods: methods.append(r['method'])
    rows = []
    for r in pc['runs']:
        if 'engine' in r:
            sp = rng(r["writes"], lang, r.get("approx"))
            res = f'<b>{sp}</b> {after(lang, sp, L["tps"])} {L["writes"]}'
            if r.get('reads'):
                res += f' &middot; {rng(r["reads"], lang)} {L["reads"]}'
            what = ENG[r['engine']]['name'] + (tx(lang, 'second_pc') if r.get('second') else '') + ('*' if r.get('short') else '')
        else:
            res = f'<b>{secs(r["picture"], lang)}</b>' + (f' ({L["first"].format(f=r["first"])})' if r.get('first') else '')
            what = L['pic']
        sup = f' <sup>{methods.index(r["method"]) + 1}</sup>' if len(methods) > 1 else ''
        rows.append(f'<tr><td>{what}</td><td>{L["on"][r["on"]]}</td><td>{res}</td><td>{date(r["date"], lang)}{sup}</td></tr>')
    def versions(m):  # every GreenCube version behind one method on this page
        vs = list(dict.fromkeys(r['v'] for r in pc['runs'] if r['method'] == m and r.get('v')))
        return {'method': m, 'v': WD[lang]['and'].join(vs)} if vs else {'method': m}
    how = ''.join(f'<li>{esc(method(versions(m), lang))}</li>' for m in methods)
    return (tx(lang, 'rw_intro') + '<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in L['th']) + '</tr></thead>\n<tbody>\n'
            + '\n'.join(rows) + '\n</tbody>\n</table></div>\n'
            f'<p>{L["how"]} <a href="{method_path(lang)}">{tx(lang, "more_how")}</a></p><ol class="src">{how}</ol>\n<p>{L["ranges"]}'
            + (tx(lang, 'short_note') if any(r.get('short') for r in pc['runs']) else '')
            + '</p>\n')

def compare(pc, lang):
    eng = headline(pc)['engine']
    order = [p for p in ranked() if headline(p)['engine'] == eng]
    k = order.index(pc)
    m = mid(headline(pc)['writes'])
    def faster(a, b):
        """'about 45% faster' / 'about 2.5 times as fast' / None when within 5%."""
        x = a / b
        if x >= 2: return tx(lang, 'times_as_fast', x=num(round(x, 1), lang))
        p = round((x - 1) * 20) * 5  # to the nearest 5%
        return tx(lang, 'pct_faster', p=p) if p >= 5 else None
    def tag(p):  # a speed from the short startup test is marked, since it is not the same test as real chats
        return tx(lang, 'startup_tag') if headline(p)['method'] == 'app-test' else ''
    parts = [tx(lang, 'cmp_rank', n=len(order), e=ENG[eng]['name'], k=k + 1)]
    if k > 0:
        up = order[k - 1]; f = faster(mid(headline(up)['writes']), m)
        parts.append(tx(lang, 'cmp_up' if f else 'cmp_up_same', The=the(up, lang).capitalize(), link=link(up, lang), hl=hl(up, lang), tag=tag(up), f=f))
    if k + 1 < len(order):
        dn = order[k + 1]; f = faster(m, mid(headline(dn)['writes']))
        parts.append(tx(lang, 'cmp_dn' if f else 'cmp_dn_same', The=the(dn, lang).capitalize(), link=link(dn, lang), hl=hl(dn, lang), tag=tag(dn), f=f))
    out = '<p>' + ' '.join(parts) + '</p>\n'
    peers = [p for p in order if p['vram'] == pc['vram'] and p['kind'] == 'desktop']
    if pc['kind'] == 'desktop' and len(peers) >= 3:
        items = ''.join(f'<li>{link(p, lang) if p is not pc else "<strong>" + esc(name(p, lang)) + "</strong>"}: {hl(p, lang)} {after(lang, hl(p, lang), WD[lang]["pc"]["tps"])}{tag(p)}</li>\n' for p in peers)
        out += tx(lang, 'cmp_peers', n=len(peers), v=pc['vram'], items=items)
    return out

def pages(lang):
    """[(slug, meta, body)] for every measured PC in this language."""
    L = WD[lang]['pc']
    out = []
    hub = hub_path(lang)
    for pc in with_page():
        h = headline(pc)
        sp = hl(pc, lang)
        a = name(pc, lang, art=True)
        eng = ENG[h['engine']]['name']
        title = tx(lang, 'pc_title', a=a, sp=sp)
        ans = answer(pc, lang)
        pic = picture_sentence(pc, lang)
        desc = tx(lang, 'pc_desc', eng=eng, sp=sp, where=where_phrase(pc, lang))
        faq = [{'q': L['q_run'].format(a=a), 'a': ans}, {'q': L['q_pic'].format(a=a), 'a': pic}]
        cv = card_vs_cpu(pc)
        if cv:
            faq.append({'q': L['q_cpu'].format(n=name(pc, lang)),
                        'a': tx(lang, 'faq_cpu', card=rng(cv[0]['writes'], lang), cpu=rng(cv[1]['writes'], lang), x=times_x(cv, lang))})
        if big_sentence(pc, lang):
            faq.append({'q': L['q_big'].format(a=a), 'a': big_sentence(pc, lang)})
        latest = max(r['date'] for r in pc['runs'])
        latest = latest if len(latest) > 7 else latest + '-01'
        meta = {'title': title[0].upper() + title[1:], 'description': desc, 'date': latest, 'lang': lang, 'kind': 'pc',
                'alt': pc['slug']['en'], 'faq': faq}
        first, rest = ans.split(' ', 1) if ' ' in ans else (ans, '')
        body = f'<div class="answer"><p><strong>{esc(first)}</strong> {esc(rest)}</p></div>\n'
        st = [('g', sp, tx(lang, 'stat_tps', eng=eng))]
        if cv: st.append(('b', times_x(cv, lang) + '×', tx(lang, 'stat_x')))
        if pictures(pc): st.append(('p', secs(pictures(pc)[0]['picture'], lang), tx(lang, 'stat_pic')))
        for r in text_runs(pc):
            if len(st) < 3 and r['engine'] != h['engine'] and r['method'] == h['method'] and not r.get('second'):
                st.append(('y', rng(r['writes'], lang), tx(lang, 'stat_with', eng=ENG[r['engine']]['name']) + (tx(lang, 'stat_short') if r.get('crash') else '')))
        body += '<div class="stats">\n' + '\n'.join(f'<div class="stat {t}"><b>{esc(b)}</b><span>{esc(s)}</span></div>' for t, b, s in st[:3]) + '\n</div>\n'
        body += f'<h2>{L["h_feel"]}</h2>\n' + feel(pc, lang)
        body += f'<h2>{L["h_meas"]}</h2>\n' + measured_table(pc, lang)
        body += f'<h2>{L["h_mean"]}</h2>\n' + ''.join(f'<div class="card {t}">\n<h3>{esc(hd)}</h3>\n<p>{x}</p>\n</div>\n' for t, hd, x in insights(pc, lang))
        body += f'<h2>{L["h_cmp"]}</h2>\n' + compare(pc, lang)
        spec = (tx(lang, 'spec_laptop') if pc['kind'] == 'laptop' else f'{pc["vendor"]} {pc["gpu"]}',
                L['none'] if not pc['vram'] else f'{pc["vram"]} {gb(lang)}', f'{pc["ram"]} {gb(lang)}', re.sub(r'(\d+) threads', lambda m: f"{m[1]} {after(lang, m[1], tx(lang, 'threads'))}", pc['cpu']))
        body += (f'<h2>{L["h_pc"]}</h2>\n<p>' + tx(lang, 'pc_lead')
                 + f'</p>\n<ul>\n<li>{L["kind"][pc["kind"]]}</li>\n' + ''.join(f'<li><strong>{k}:</strong> {esc(v)}</li>\n' for k, v in zip(L['spec'], spec)) + '</ul>\n')
        body += f'<h2>{L["h_check"]}</h2>\n' + tx(lang, 'check_lead') + WD[lang]['check_steps'] + tx(lang, 'check_tail', hub=hub)
        others = ''.join(f'<li>{link(o, lang)}: {hl(o, lang)} {after(lang, hl(o, lang), L["tps"])} ({ENG[headline(o)["engine"]]["name"]})</li>\n' for o in ranked() if o is not pc)
        body += (f'<h2>{L["h_more"]}</h2>\n<ul>\n{others}</ul>\n'
                 f'<p><a href="{hub}">{L["hub_t"]}</a> {fmt(lang, L["all"], n=count())}.</p>\n')
        out.append((pc_slug(pc, lang), meta, body))
    return out + [method_page(lang)]

def count(): return len([p for p in PCS if headline(p)])

def table(lang):
    """The speed table in the "Can my PC run AI?" test: one row per measured PC, fastest first, linked to its page."""
    L = WD[lang]['pc']
    pcs = sorted([p for p in PCS if headline(p)], key=lambda p: -mid(headline(p)['writes']))
    top = max(headline(p)['writes'][1] for p in pcs)
    rows = []
    for p in pcs:
        h = headline(p)
        g = esc(label(p, lang))
        if p.get('slug'): g = f'<a href="{page_path(p, lang)}">{g}</a>'
        lo = '' if h['on'] in ('card', 'split') else ' lo'
        rows.append(f'<tr><td>{L["kind"][p["kind"]]}</td><td>{g}</td><td>{p["ram"]} {gb(lang)}</td><td>{ENG[h["engine"]]["name"]}</td>'
                    f'<td class="spd"><span class="bar{lo}" style="--w:{round(100 * h["writes"][1] / top)}%"></span><b>{hl(p, lang)}</b></td></tr>')
    return ('<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in WD[lang]['table_head']) + '</tr></thead>\n<tbody>\n'
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
    data = {'lang': lang, 'groups': GPUS['groups'], 'method': method_path(lang), 'pcs': pcs, 'engines': ENG, 'bigFloor': BIG_FLOOR, 'big': big,
            'pics8': {'n': len(p8), 'lo': min(r['picture'][0] for _, r in p8), 'hi': max(r['picture'][1] for _, r in p8)} if p8 else None,
            'pics6': {'pc': {'name': name(p6[0][0], lang), 'url': page_path(p6[0][0], lang)}, 't': p6[0][1]['picture']} if p6 else None,
            'picLaptop': {'chip': next(r['picture'] for r in pictures(lap) if r['on'] == 'chip'),
                          'cpu': next(r['picture'] for r in pictures(lap) if r['on'] == 'cpu')} if lap else None,
            'builtin': WD[lang]['builtin'], 'T': WD[lang]['checker_js']}
    if 'units' in WD[lang]: data['U'] = WD[lang]['units']
    if lang in PLURAL: data['P'] = PLURAL[lang]
    T = WD[lang]['checker']
    return (f'<section class="chk" id="chk">\n<h2 id="checker">{T["h"]}</h2>\n<p class="chk-lead">{T["lead"]}</p>\n'
            f'<p class="chk-detect" id="chk-detect">{T["nojs"]}</p>\n'
            f'<div class="chk-q chk-q-card"><label for="chk-in">{T["card"]}</label>'
            f'<div class="chk-finder"><input type="text" id="chk-in" autocomplete="off" spellcheck="false" placeholder="{T["ph"]}" role="combobox" '
            f'aria-autocomplete="list" aria-expanded="false" aria-controls="chk-hits" /><div class="chk-hits" id="chk-hits" role="listbox"></div></div>'
            f'<button type="button" class="chk-quiet" id="chk-none">{T["none"]}</button></div>\n'
            f'<div class="chk-q" id="chk-vram" hidden><span>{T["vram"]}</span><div class="chk-opts"></div></div>\n'
            f'<div class="chk-q" id="chk-ram"><span>{T["ram"]}</span><div class="chk-opts"><button type="button" data-ram="8">8 {gb(lang)}</button>'
            f'<button type="button" data-ram="16">16 {gb(lang)}</button><button type="button" data-ram="32">{T["more"]}</button></div></div>\n'
            f'<p class="chk-help">{T["help"]}</p>\n<div id="chk-out" aria-live="polite"></div>\n<p class="chk-priv">{T["priv"]}</p>\n</section>\n'
            '<script>' + JS.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False).replace('</', r'<\/')) + '</script>\n')


# ---------- how we measure: the methods, every PC, the estimate test, and the data as a CSV ----------
METHOD_SLUG = {'en': 'how-we-measure-ai-speed', 'es': 'como-medimos-la-velocidad-de-la-ia'}  # other languages use the English slug
CSV_NAME = 'greencube-ai-speeds.csv'
SPECS_URL = 'https://www.techpowerup.com/gpu-specs/'
GOOD = 15  # %: estimates are good enough to show only if no hidden card is off by more than this

def method_path(lang): return blog_path(lang, METHOD_SLUG.get(lang, METHOD_SLUG['en']))

def holdout(skip=None):
    """Hide each card, predict its E4B writing speed from the others' speed per GB/s of memory bandwidth, compare."""
    pts = [(p, mid(headline(p)['writes'])) for p in with_page()
           if p.get('bw') and headline(p)['engine'] == 'e4b' and headline(p)['on'] == 'card' and p is not skip]
    rows = []
    for p, m in pts:
        eff = sum(o / q['bw'] for q, o in pts if q is not p) / (len(pts) - 1)
        rows.append((p, m, eff * p['bw'], (eff * p['bw'] - m) / m))
    rows.sort(key=lambda r: -r[1])
    def med(v):
        v = sorted(v)
        return v[len(v) // 2] if len(v) % 2 else (v[len(v) // 2 - 1] + v[len(v) // 2]) / 2
    errs = [abs(r[3]) for r in rows]
    worst = max(rows, key=lambda r: abs(r[3]))
    if skip: return dict(worst_pct=round(100 * max(errs)))
    rest = holdout(skip=worst[0])  # the same test run again without the worst card
    return dict(rows=rows, median=round(100 * med(errs)), worst=worst, worst_pct=round(100 * abs(worst[3])),
                rest_worst=rest['worst_pct'], good=100 * max(errs) <= GOOD)

def csv_text():
    """Every measured run, one row each."""
    import csv, io
    f = io.StringIO()
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['pc', 'kind', 'graphics', 'vram_gb', 'ram_gb', 'processor', 'ai_model', 'ran_on', 'writes_tok_s_low', 'writes_tok_s_high',
                'reads_tok_s_low', 'reads_tok_s_high', 'picture_s_low', 'picture_s_high', 'method', 'greencube_version', 'date', 'second_pc'])
    for p in PCS:
        for r in p['runs']:
            w.writerow([p['id'], p['kind'], p.get('chip') or f'{p["vendor"]} {p["gpu"]}', p['vram'], p['ram'], p['cpu'],
                        ENG[r['engine']]['name'] if 'engine' in r else 'Z-Image Turbo (pictures)', r['on'],
                        *(r.get('writes') or ['', '']), *(r.get('reads') or ['', '']), *(r.get('picture') or ['', '']),
                        r['method'], r.get('v', ''), r['date'], 'yes' if r.get('second') else ''])
    return f.getvalue()

def method_page(lang):
    M, L = WD[lang]['method'], WD[lang]['pc']
    pcs = ranked()
    dates = sorted(r['date'] for p in pcs for r in p['runs'])
    H = holdout()
    hub = hub_path(lang)
    nopic = [p for p in pcs if p['kind'] == 'desktop' and not pictures(p)]
    f = dict(n=count(), d0=date(dates[0], lang), d1=date(dates[-1], lang), med=H['median'], worst=H['worst_pct'], rest=H['rest_worst'],
             e2b=ENG['e2b']['name'], e2bgb=num(ENG['e2b']['gb'], lang), e4b=ENG['e4b']['name'], e4bgb=num(ENG['e4b']['gb'], lang),
             b12=ENG[BIG]['name'], b12gb=num(ENG[BIG]['gb'], lang), specs=SPECS_URL, csv=CSV_NAME, year=dates[-1][:4], hub=hub,
             worst_link=link(H['worst'][0], lang), pred=num(round(H['worst'][2]), lang), meas=num(round(H['worst'][1]), lang),
             nopic=WD[lang]['nopic_join'].join(link(p, lang) for p in nopic))
    b = f'<div class="answer"><p>{esc(fmt(lang, M["ans"], **f))}</p></div>\n'
    b += ('<div class="stats">\n' + f'<div class="stat g"><b>{count()}</b><span>{M["s1"]}</span></div>\n'
          + f'<div class="stat b"><b>{sum(len(p["runs"]) for p in PCS)}</b><span>{M["s2"]}</span></div>\n'
          + f'<div class="stat y"><b>{H["worst_pct"]}%</b><span>{M["s3"]}</span></div>\n</div>\n')
    b += f'<h2>{M["h_what"]}</h2>\n' + fmt(lang, M['what'], **f)
    b += f'<h2>{M["h_how"]}</h2>\n<p>{M["how_lead"]}</p>\n'
    for m, tint in (('app', 'g'), ('app-test', 'b'), ('bench', 'y'), ('picture', 'p')):
        on = ', '.join(link(p, lang) for p in pcs if any(r['method'] == m for r in p['runs']))
        b += (f'<div class="card {tint}">\n<h3>{M["names"][m]}</h3>\n<p>{esc(WD[lang]["methods"][m].replace(" {v}", ""))}</p>\n'
              + (f'<p>{M["used"]}: {on}.</p>\n' if on else '') + '</div>\n')
    b += M['how_tail']
    rows = ''.join(f'<tr><td>{link(p, lang)}</td><td>{L["kind"][p["kind"]]}</td><td>{str(p["vram"]) + " " + gb(lang) if p["vram"] else "–"}</td><td>{p["ram"]} {gb(lang)}</td>'
                   f'<td>{esc(M["names"][headline(p)["method"]])}</td><td>{headline(p).get("v", "–")}</td><td>{date(headline(p)["date"], lang)}</td><td><b>{hl(p, lang)}</b></td></tr>\n'
                   for p in pcs)
    b += (f'<h2>{M["h_pcs"]}</h2>\n<p>{M["pcs_lead"]}</p>\n<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in M['th_pcs'])
          + '</tr></thead>\n<tbody>\n' + rows + '</tbody>\n</table></div>\n')
    b += M['ranges']
    t_rows = ''.join(f'<tr><td>{link(p, lang)}</td><td>{p["bw"]} {gb(lang)}/{WD[lang].get("units", ["s"])[0]}</td><td>{num(round(m), lang)}</td><td>{num(round(pr), lang)}</td>'
                     f'<td><b>{"+" if er > 0 else "−"}{round(abs(er) * 100)}%</b></td></tr>\n' for p, m, pr, er in H['rows'])
    b += (f'<h2>{M["h_est"]}</h2>\n' + fmt(lang, M['est'], **f) + '<div class="tbl-wrap"><table>\n<thead><tr>' + ''.join(f'<th>{t}</th>' for t in M['th_est'])
          + '</tr></thead>\n<tbody>\n' + t_rows + '</tbody>\n</table></div>\n' + fmt(lang, M['est_res'], **f)
          + f'<p>{fmt(lang, M["good"] if H["good"] else M["bad"], **f)}</p>\n')
    b += fmt(lang, M['gaps'], **f) + fmt(lang, M['data'], **f)
    meta = {'title': M['title'], 'description': fmt(lang, M['desc'], **f), 'date': dates[-1], 'lang': lang, 'kind': 'pc',
            'alt': METHOD_SLUG['en'], 'faq': [{'q': q, 'a': fmt(lang, a, **f)} for q, a in M['faq']]}
    return METHOD_SLUG.get(lang, METHOD_SLUG['en']), meta, b
