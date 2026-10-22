"""Main-site translations. Every new language is built from the English page, using the Spanish page to find what
has to change: anything that differs between English and Spanish (text, attribute values, strings inside scripts)
is a "unit". Units that differ only by a language code or an /es/ path are rewritten by code; the rest are looked
up by their English text in i18n/<lang>.json, one shared dictionary per language for all pages.

  python i18n/i18n.py todo pt index.html buy.html   -> i18n/todo-pt.json: English (+ Spanish) still untranslated
  python i18n/i18n.py build pt index.html buy.html  -> pt/index.html, pt/buy.html
  python i18n/i18n.py switcher                      -> language menus + hreflang on every main page, all languages
  python i18n/i18n.py redirects                     -> vercel.json: send each browser language to its pages
"""
import difflib, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOK = re.compile(r'<script[^>]*>.*?</script>|<style[^>]*>.*?</style>|<!--.*?-->|<[^>]*>|[^<]+', re.S)
ATTR = re.compile(r'([\w:.-]+)(\s*=\s*)("[^"]*"|\'[^\']*\')')
STR = re.compile(r'"(?:[^"\\\n]|\\.)*"' r"|'(?:[^'\\\n]|\\.)*'" r'|`(?:[^`\\]|\\.)*`')
HOST = 'https://greencube.app'

# code: (menu label, html lang, og:locale, Stripe checkout locale, Intl locale)
LANGS = {
    'en': ('EN', 'en', 'en_US', 'auto', 'en-IE'),
    'es': ('ES', 'es', 'es_ES', 'es', 'es-ES'),
    'pt': ('PT', 'pt-BR', 'pt_BR', 'pt-BR', 'pt-BR'),
    'fr': ('FR', 'fr', 'fr_FR', 'fr', 'fr-FR'),
    'de': ('DE', 'de', 'de_DE', 'de', 'de-DE'),
    'it': ('IT', 'it', 'it_IT', 'it', 'it-IT'),
    'nl': ('NL', 'nl', 'nl_NL', 'nl', 'nl-NL'),
    'pl': ('PL', 'pl', 'pl_PL', 'pl', 'pl-PL'),
    'tr': ('TR', 'tr', 'tr_TR', 'tr', 'tr-TR'),
    'ja': ('日本語', 'ja', 'ja_JP', 'ja', 'ja-JP'),
    'ko': ('한국어', 'ko', 'ko_KR', 'ko', 'ko-KR'),
}
NAMES = {'en': 'English', 'es': 'Español', 'pt': 'Português', 'fr': 'Français', 'de': 'Deutsch', 'it': 'Italiano',
         'nl': 'Nederlands', 'pl': 'Polski', 'tr': 'Türkçe', 'ja': '日本語', 'ko': '한국어'}


def read(p):
    return open(os.path.join(ROOT, p), encoding='utf-8').read()


def unq(v):
    return v[1:-1] if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'`' else v


def units(page):
    """Every spot where Spanish differs from English: list of dicts {tok, kind, en, es, attr|n, mech}."""
    a, b = TOK.findall(read(page)), TOK.findall(read('es/' + page))
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        ys = b[j1:j2] if i2 - i1 == j2 - j1 else [None] * (i2 - i1)
        for i, x, y in zip(range(i1, i2), a[i1:i2], ys):
            if x.startswith('<style') or x.startswith('<!--'):
                continue
            if x.startswith('<script'):
                sx, sy = STR.findall(x), (STR.findall(y) if y else [])
                for n, s in enumerate(sx):
                    t = sy[n] if len(sx) == len(sy) else None
                    if t != s:
                        out.append({'tok': i, 'kind': 'js', 'n': n, 'en': s, 'es': t})
            elif x.startswith('<'):
                ax = {m[0]: m[2] for m in ATTR.findall(x)}
                ay = {m[0]: m[2] for m in ATTR.findall(y)} if y else {}
                for k, v in ax.items():
                    if ay.get(k) != v:
                        out.append({'tok': i, 'kind': 'attr', 'attr': k, 'en': v, 'es': ay.get(k)})
            elif x.strip():
                out.append({'tok': i, 'kind': 'text', 'en': x, 'es': y})
    for u in out:
        u['mech'] = u['es'] is not None and (swap(u['en'], 'es') == u['es'] or swap(u['en'], 'es', True) == u['es'])
        u['key'] = unq(u['en']).strip() if u['kind'] != 'text' else u['en'].strip()
    return out


def swap(s, lang, loose=False):
    """Point an English value at `lang`: site paths gain /<lang>/, language codes change."""
    o = re.sub(r'(^|["\'(])/(?!/|' + lang + r'/)(?=[a-z#?]|["\']|$)', lambda m: m.group(1) + '/' + lang + '/', s)
    o = re.sub(r'https://greencube\.app/(?!' + lang + r'/)', HOST + '/' + lang + '/', o)
    o = re.sub(r'https://greencube\.app(?=["\']|$)', HOST + '/' + lang + '/', o)
    o = o.replace('/' + lang + '//', '/' + lang + '/')
    if loose:
        o = re.sub(r'(["\'])en\1', r'\1' + lang + r'\1', o)
        o = re.sub(r'\ben[-_]US\b', LANGS[lang][2], o)
    return o


def dictionary(lang):
    p = os.path.join(ROOT, 'i18n', lang + '.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def cmd_todo(lang, pages):
    d, todo = dictionary(lang), {}
    for page in pages:
        for u in units(page):
            if not u['mech'] and u['key'] not in d and u['key'] not in todo:
                es = u['es']
                todo[u['key']] = (unq(es).strip() if es and u['kind'] != 'text' else (es or '').strip())
    json.dump(todo, open(os.path.join(ROOT, 'i18n', f'todo-{lang}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{lang}: {len(todo)} strings to translate, {sum(len(k) for k in todo)} characters')


def put_attr(tok, name, value):
    value = value.replace('"', '&quot;')
    return re.sub(r'(\s' + re.escape(name) + r'\s*=\s*)("[^"]*"|\'[^\']*\')', lambda m: m.group(1) + '"' + value + '"', tok, count=1)


def put_js(tok, n, orig, value, raw=False):
    if not raw:
        q = orig[0]
        value = q + value.replace('\\', '\\\\').replace(q, '\\' + q) + q
    for k, m in enumerate(STR.finditer(tok)):
        if k == n:
            return tok[:m.start()] + value + tok[m.end():]
    return tok


def cmd_build(lang, pages):
    d = dictionary(lang)
    for page in pages:
        toks = TOK.findall(read(page))
        missing = []
        # within a token, apply from the last string to the first so earlier positions stay valid
        for u in sorted(units(page), key=lambda u: (u['tok'], -u.get('n', 0))):
            i = u['tok']
            if u['mech']:
                new = swap(u['en'], lang) if swap(u['en'], 'es') == u['es'] else swap(u['en'], lang, True)
                if u['kind'] == 'text':
                    toks[i] = new
                elif u['kind'] == 'attr':
                    toks[i] = put_attr(toks[i], u['attr'], unq(new))
                else:
                    toks[i] = put_js(toks[i], u['n'], u['en'], new, raw=True)
                continue
            if u['key'] not in d:
                missing.append(u['key'])
                continue
            new = d[u['key']]
            if u['kind'] == 'text':
                lead, trail = re.match(r'\s*', u['en']).group(), re.search(r'\s*$', u['en']).group()
                toks[i] = lead + new + trail
            elif u['kind'] == 'attr':
                toks[i] = put_attr(toks[i], u['attr'], new)
            else:
                toks[i] = put_js(toks[i], u['n'], u['en'], new)
        out = ''.join(toks)
        label, htmllang, oglocale, stripe, intl = LANGS[lang]
        out = re.sub(r'<html lang="[^"]*"', f'<html lang="{htmllang}"', out, count=1)
        out = re.sub(r'(og:locale" content=")[^"]*"', r'\g<1>' + oglocale + '"', out)
        out = re.sub(r'"inLanguage":\s*"[^"]*"', f'"inLanguage": "{htmllang}"', out)
        # pages not translated yet into this language: link to the English one instead of a 404
        def local(m):
            slug = m.group(2)
            ok = os.path.exists(os.path.join(ROOT, lang, (slug or 'index') + '.html')) or (slug + '.html') in pages
            return m.group(0) if ok or not slug else m.group(1) + '/' + slug + m.group(3)
        out = re.sub(r'(href="|"url": "|' + re.escape(HOST) + r')/' + lang + r'/([a-z-]*)(["#?])', local, out)
        dest = os.path.join(ROOT, lang, page)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, 'w', encoding='utf-8', newline='\n').write(out)
        print(f'{lang}/{page}: {len(missing)} missing' + (f': {missing[:6]}' if missing else ''))


def built(lang, page):
    return os.path.exists(os.path.join(ROOT, page if lang == 'en' else f'{lang}/{page}'))


def url(lang, page):
    slug = '' if page == 'index.html' else page[:-5]
    return HOST + ('/' if lang == 'en' else f'/{lang}/') + slug


def path(lang, page):
    slug = '' if page == 'index.html' else page[:-5]
    return ('/' if lang == 'en' else f'/{lang}/') + slug


SWITCH_CSS = """<style id="lang-pick-css">
    .lang-pick { position: relative; }
    .lang-pick > summary { list-style: none; cursor: pointer; }
    .lang-pick > summary::-webkit-details-marker { display: none; }
    .lang-pick .lang-list { position: absolute; right: 0; top: calc(100% + 8px); z-index: 60; display: grid;
      grid-template-columns: repeat(2, minmax(110px, 1fr)); gap: 2px; padding: 8px; border-radius: 14px;
      background: var(--paper, #F5F1E8); border: 1px solid var(--line, rgba(0,0,0,.12)); box-shadow: 0 12px 32px rgba(0,0,0,.12); }
    .lang-pick .lang-list a { padding: 7px 10px; border-radius: 9px; font-size: 13.5px; color: var(--ink, #222); text-decoration: none; white-space: nowrap; }
    .lang-pick .lang-list a:hover, .lang-pick .lang-list a[aria-current="true"] { background: rgba(0,0,0,.06); }
    footer .f-lang { flex-wrap: wrap; }
  </style>"""


def cmd_switcher():
    """Header menu, footer list and hreflang links on every main page in every language (English and Spanish too)."""
    pages = [os.path.basename(p) for p in glob.glob(os.path.join(ROOT, '*.html'))]
    for page in pages:
        langs = [l for l in LANGS if built(l, page)]
        if len(langs) < 2:
            continue
        for lang in langs:
            f = os.path.join(ROOT, page if lang == 'en' else f'{lang}/{page}')
            s = open(f, encoding='utf-8').read()
            alts = ''.join(f'  <link rel="alternate" hreflang="{LANGS[l][1]}" href="{url(l, page)}" />\n' for l in langs)
            alts += f'  <link rel="alternate" hreflang="x-default" href="{url("en", page)}" />\n'
            s = re.sub(r'(?:[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?>\n)+', alts, s, count=1)
            items = ''.join(f'<a href="{path(l, page)}" hreflang="{l}" lang="{LANGS[l][1]}"'
                            + (' aria-current="true"' if l == lang else '') + f'>{NAMES[l]}</a>' for l in langs)
            head = (f'<details class="lang-pick"><summary class="lang" aria-label="Language">{LANGS[lang][0]}</summary>'
                    f'<div class="lang-list">{items}</div></details>')
            s = re.sub(r'<details class="lang-pick">.*?</details>|<a href="[^"]*" class="lang" hreflang="[^"]*">[^<]*</a>',
                       lambda m: head, s, count=1, flags=re.S)
            foot = ''.join(f'<a href="{path(l, page)}" hreflang="{l}"' + (' aria-current="true"' if l == lang else '')
                           + f'>{LANGS[l][0] if len(LANGS[l][0]) <= 2 else l.upper()}</a>' for l in langs)
            s = re.sub(r'(<div class="f-lang">).*?(</div>)', lambda m: m.group(1) + foot + m.group(2), s, count=1, flags=re.S)
            if 'id="lang-pick-css"' not in s:
                s = s.replace('</head>', SWITCH_CSS + '\n</head>', 1)
            open(f, 'w', encoding='utf-8', newline='\n').write(s)
        print(page, ' '.join(langs))


def cmd_redirects():
    """Browsers set to a language we have go to that language's page, like the Spanish rules (first visit only)."""
    v = json.load(open(os.path.join(ROOT, 'vercel.json'), encoding='utf-8'))
    ours = tuple(f'/{l}/' for l in LANGS if l not in ('en', 'es'))
    keep = [r for r in v['redirects'] if not (r.get('destination', '').startswith(ours)
            and any(h.get('key') == 'accept-language' for h in r.get('has', [])))]
    es_rules = [r for r in keep if any(h.get('key') == 'accept-language' for h in r.get('has', []))]
    at = keep.index(es_rules[-1]) + 1 if es_rules else len(keep)
    missing = es_rules[0]['missing'] if es_rules else []
    new = []
    for lang in LANGS:
        if lang in ('en', 'es'):
            continue
        pages = [p[:-5] for p in map(os.path.basename, glob.glob(os.path.join(ROOT, lang, '*.html'))) if p != 'index.html']
        if not os.path.exists(os.path.join(ROOT, lang, 'index.html')):
            continue
        has = [{'type': 'header', 'key': 'accept-language', 'value': lang + r'(-[A-Za-z]+)?([;,].*)?'}]
        new.append({'source': '/', 'has': has, 'missing': missing, 'destination': f'/{lang}/', 'permanent': False})
        if pages:
            new.append({'source': '/:page(' + '|'.join(sorted(pages)) + ')', 'has': has, 'missing': missing,
                        'destination': f'/{lang}/:page', 'permanent': False})
    v['redirects'] = keep[:at] + new + keep[at:]
    open(os.path.join(ROOT, 'vercel.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
    print(len(new), 'language redirects')


def cmd_sitemap():
    """List every translated main page in sitemap.xml (English and Spanish entries are kept as they are)."""
    import datetime
    p = os.path.join(ROOT, 'sitemap.xml')
    s = open(p, encoding='utf-8').read()
    ours = '|'.join(l for l in LANGS if l not in ('en', 'es'))
    s = re.sub(r'  <url><loc>' + re.escape(HOST) + r'/(?:' + ours + r')/[^<]*</loc>.*?</url>\n', '', s)
    today = datetime.date.today().isoformat()
    rows = ''
    for lang in LANGS:
        if lang in ('en', 'es'):
            continue
        for f in sorted(glob.glob(os.path.join(ROOT, lang, '*.html')), key=lambda f: f.endswith('index.html') is False):
            page = os.path.basename(f)
            rows += (f'  <url><loc>{url(lang, page)}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq>'
                     f'<priority>{"1.0" if page == "index.html" else "0.8"}</priority></url>\n')
    s = s.replace('</urlset>', rows + '</urlset>')
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print(rows.count('<url>'), 'translated pages in sitemap.xml')


if __name__ == '__main__':
    c, args = sys.argv[1], sys.argv[2:]
    if c == 'sitemap':
        cmd_sitemap()
    if c == 'todo':
        cmd_todo(args[0], args[1:])
    elif c == 'build':
        cmd_build(args[0], args[1:])
    elif c == 'switcher':
        cmd_switcher()
    elif c == 'redirects':
        cmd_redirects()
