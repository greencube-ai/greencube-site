"""Build our own copy of the blog (blog.greencube.app/blog/...) from the saved posts.

    python3 -I blog-archive/tools/build_blog.py            (run from the repo root)

Reads blog-archive/ (index.json, posts/, images/) and writes blog/:
one page per post at the same address BabyLoveGrowth used, the list page,
a sitemap, a shared stylesheet and resized images. Safe to re-run: blog/ is
rebuilt from scratch every time, so new posts saved later go through the
same fixes.
"""
import html, json, os, re, shutil, sys
from datetime import date
from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'i18n'))
import facts
import pc_pages
from i18n import LANGS as SITE_LANGS, NAMES  # the main site's languages: (menu label, html lang, ...), and their own names
WD = pc_pages.WD  # words/<lang>.json: every word the blog shows, one file per language
BLOG_LANGS = [l for l in SITE_LANGS if l in WD]  # a language is on the blog once its words file exists
def html_lang(lang): return SITE_LANGS[lang][1]

SRC, OUT = 'blog-archive', 'blog'
HOST = 'https://blog.greencube.app'
TODAY = '2026-10-10'  # the day the archived posts were corrected; rebuilding must not re-date them
MAX_W = 1200

idx = json.load(open(f'{SRC}/index.json', encoding='utf-8'))
idx.sort(key=lambda p: (p['date_published'] or p['sitemap_lastmod'] or ''), reverse=True)

# old posts link to the test that measured their topic (our own posts, by slug)
TESTED = {
    'hardware-for-local-ai': ['can-my-pc-run-ai', 'how-much-vram-for-ai'],
    'best-local-ai-models': ['gemma-4-requirements', 'how-much-vram-for-ai'],
    'llama-3-vs-gemma': ['gemma-4-requirements', 'gemma-4-e2b-vs-e4b'],
    'llm-models': ['gemma-4-requirements'],
    'best-small-llm': ['gemma-4-e2b-vs-e4b'],
    'local-ai-models-explained': ['gemma-4-e2b-vs-e4b'],
    'best-laptop-ai-assistant': ['run-ai-on-8gb-ram', 'ai-on-laptop-without-gpu'],
    'offline-ai-setup-windows': ['can-my-pc-run-ai'],
    'install-local-ai': ['can-my-pc-run-ai'],
    'local-ai-chatbot-windows': ['can-my-pc-run-ai'],
    'best-offline-ai-chatbot': ['can-my-pc-run-ai'],
    'ai-without-internet': ['can-my-pc-run-ai'],
    'unlimited-ai': ['chatgpt-free-limits'],
    'no-rate-limit-ai': ['chatgpt-free-limits'],
    'ai-without-subscription': ['chatgpt-free-limits'],
    'local-ai-vs-chatgpt': ['chatgpt-free-limits'],
    'chatgpt-alternatives-5': ['chatgpt-free-limits'],
    'best-ai-for-students': ['ai-to-study-from-pdf', 'flashcards-from-pdf', 'chatgpt-free-limits', 'can-my-pc-run-ai'],
    'offline-ai-for-students': ['can-my-pc-run-ai', 'run-ai-on-8gb-ram'],
    'ollama-vs-lm-studio': ['how-much-vram-for-ai'],
    'study-guide-from-pdf': ['ai-to-study-from-pdf', 'flashcards-from-pdf'],
    'flashcards-from-pdf': ['ai-to-study-from-pdf'],
    'best-pdf-summarizer': ['ai-to-study-from-pdf'],
    'notebooklm-alternatives': ['ai-to-study-from-pdf', 'flashcards-from-pdf'],
    'humata-ai-alternatives': ['ai-to-study-from-pdf'],
    'ai-study-planner-offline': ['ai-to-study-from-pdf', 'flashcards-from-pdf'],
    'best-ai-for-computer-science-students': ['ai-to-study-from-pdf'],
}
# old posts link to the page where we checked their topic against the companies' own pages (2026-10-18)
TRAINING, NOTES, SUBSCRIPTION = 'ai-that-doesnt-train-on-your-data', 'ai-to-summarize-notes', 'ai-without-subscription'
CHECKED = {
    'is-chatgpt-private': [TRAINING], 'best-private-ai': [TRAINING], 'private-ai-assistant': [TRAINING],
    'best-private-chat-ai': [TRAINING, SUBSCRIPTION], 'secure-ai-on-pc': [TRAINING], 'is-local-ai-safe': [TRAINING],
    'microsoft-copilot-alternatives': [TRAINING], 'gemini-alternatives': [TRAINING], 'meta-ai-alternatives': [TRAINING],
    'deepseek-alternatives': [TRAINING], 'monica-ai-alternatives': [TRAINING],
    'claude-vs-greencube': [TRAINING, SUBSCRIPTION], 'greencube-vs-claude': [TRAINING, SUBSCRIPTION],
    'chatgpt-vs-greencube': [TRAINING, SUBSCRIPTION], 'chatgpt-vs-greencube-offline-privacy-for-students-and-professionals': [TRAINING],
    'gemini-vs-greencube': [TRAINING, NOTES], 'ollama-vs-greencube': [SUBSCRIPTION],
    'best-pdf-summarizer': [NOTES], 'notebooklm-alternatives': [NOTES, TRAINING], 'humata-ai-alternatives': [NOTES],
    'pdfai-alternatives': [NOTES], 'best-private-pdf-ai': [NOTES, TRAINING], 'study-guide-from-pdf': [NOTES],
    'lifetime-ai-software': [SUBSCRIPTION], 'unlimited-ai': [SUBSCRIPTION], 'no-rate-limit-ai': [SUBSCRIPTION],
    'best-ai-for-students': [NOTES, SUBSCRIPTION], 'notion-ai-alternatives': [SUBSCRIPTION],
}
# Old "GreenCube vs X" pages written before our "test it first" rule: kept online for anyone with the link, but out of
# search (noindex) and out of the sitemap until honest, dated fact tables replace them after 14 Nov (Hector, 2026-10-19)
NOINDEX = {'ollama-vs-greencube', 'claude-vs-greencube', 'greencube-vs-claude', 'chatgpt-vs-greencube',
           'chatgpt-vs-greencube-offline-privacy-for-students-and-professionals', 'gemini-vs-greencube'}
# Old posts merged into a stronger page on the same search (2026-10-23): not built, out of the sitemap and lists;
# vercel.json sends their address to the target with a permanent redirect, so their ranking signals carry over
MERGED = {'offline-ai-setup-windows': 'local-ai-chatbot-windows', 'install-local-ai': 'local-ai-chatbot-windows',
          'ai-without-internet': 'best-offline-ai-chatbot', 'best-private-ai': 'private-ai-assistant',
          'no-rate-limit-ai': 'unlimited-ai', 'local-ai-models-explained': 'best-local-ai-models',
          'best-private-chat-ai': 'private-ai-assistant', 'local-ai-vs-chatgpt': 'chatgpt-offline'}
OWN_TITLES = {}
for fn in os.listdir(f'{SRC}/own') if os.path.isdir(f'{SRC}/own') else []:
    if fn.endswith('.html'):
        m = re.match(r'\s*<!--meta\s*(\{.*?\})\s*-->', open(f'{SRC}/own/{fn}', encoding='utf-8').read(), re.S)
        OWN_TITLES[fn[:-5]] = json.loads(m.group(1))['title'].replace('{{pcs}}', str(pc_pages.count()))

def tested_box(slug):
    def items(slugs): return ''.join(f'<li><a href="/blog/{s}">{html.escape(OWN_TITLES[s])}</a></li>' for s in slugs if s in OWN_TITLES)
    tested, checked = items(TESTED.get(slug, [])), items(CHECKED.get(slug, []))
    out = f'<aside class="tested"><strong>We tested this</strong><ul>{tested}</ul></aside>\n' if tested else ''
    return out + (f'<aside class="tested"><strong>We checked this</strong><ul>{checked}</ul></aside>\n' if checked else '')

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f'{OUT}/images')
shutil.copy(os.path.join(os.path.dirname(__file__), 'blog.css'), f'{OUT}/blog.css')

# ---------- images: max 1200 px wide, real JPEG unless it needs transparency ----------
sizes = {}
def image(rel):
    """rel is 'images/<name>' from the archive; returns (published path, w, h)."""
    if rel in sizes: return sizes[rel]
    name = os.path.basename(rel)
    im = Image.open(f'{SRC}/{rel}')
    alpha = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    base = os.path.splitext(name)[0]
    if alpha:
        out = base + '.png'; im.save(f'{OUT}/images/{out}', optimize=True)
    else:
        out = base + '.jpg'; im.convert('RGB').save(f'{OUT}/images/{out}', 'JPEG', quality=80, optimize=True, progressive=True)
    sizes[rel] = (f'/blog/images/{out}', im.width, im.height)
    return sizes[rel]

def cf_email(hexs):
    k = int(hexs[:2], 16)
    return ''.join(chr(int(hexs[i:i + 2], 16) ^ k) for i in range(2, len(hexs), 2))

# ---------- body clean-up ----------
def clean(body):
    body = body.replace(' node="[object Object]"', '')
    body = body.replace('<div class="my-4 w-full overflow-x-auto">', '<div class="tbl-wrap">')
    body = body.replace(' class="min-w-full border-collapse"', '')
    # Cloudflare's email obfuscation mangled "python@3.11" into a fake email link
    body = re.sub(r'<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="([0-9a-f]+)">[^<]*</a>',
                  lambda m: html.escape(cf_email(m.group(1))), body)
    # BabyLoveGrowth's links to its own tools: keep the words, drop the link
    body = re.sub(r'<p><a [^>]*href="https://(www\.)?babylovegrowth\.ai/?"[^>]*>Article generated by BabyLoveGrowth</a></p>\n?', '', body)
    body = re.sub(r'<a [^>]*href="https://(www\.)?babylovegrowth\.ai[^"]*"[^>]*>([\s\S]*?)</a>', r'\2', body)
    # BabyLoveGrowth placed some followed links to other sites in its network; Google's link-spam policy covers
    # links "to or from" a site, so every outside link in these archived posts passes no credit (nofollow)
    def nofollow(m):
        tag = m.group(0)
        if 'greencube.app' in tag or 'nofollow' in tag: return tag
        if ' rel="' in tag: return tag.replace(' rel="', ' rel="nofollow ', 1)
        return tag[:-1] + ' rel="nofollow noopener">'
    body = re.sub(r'<a [^>]*href="https?://[^"]+"[^>]*>', nofollow, body)
    def img(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag).group(1)
        if not src.startswith('images/'): return tag
        path, w, h = image(src)
        alt = re.search(r'alt="([^"]*)"', tag)
        return f'<img src="{path}" alt="{alt.group(1) if alt else ""}" width="{w}" height="{h}" loading="lazy" decoding="async"/>'
    return re.sub(r'<img\b[^>]*>', img, body)

NOTE_PARTS = {
    'models': 'today GreenCube picks the right AI model for your computer automatically '
              '(Gemma 4 E2B on smaller PCs, Gemma 4 E4B with a graphics card), so you no longer choose between two models',
    'account': 'today you sign in once with Google or Microsoft to activate it, and the first launch downloads the AI model; '
               'after that it works offline, and your chats and files stay on your PC',
}

def note(kinds):
    if not kinds: return ''
    parts = [NOTE_PARTS[k] for k in kinds]
    text = parts[0][0].upper() + parts[0][1:] + ('. Also, ' + parts[1].replace('today you', 'you') if len(parts) > 1 else '')
    return ('<aside class="update" role="note"><strong>Updated October 2026</strong>'
            '<p>Parts of this article describe an earlier version of GreenCube. ' + text + '. '
            'It costs &euro;9.99 (US$9.99), paid once. '
            '<a href="https://greencube.app/what-you-get">Check what runs on your PC</a></p></aside>')

def nice_date(iso):
    d = date.fromisoformat(iso[:10]); return f'{d.day} {d.strftime("%B %Y")}'

def esc(s): return html.escape(s, quote=True)

HEAD = open(os.path.join(os.path.dirname(__file__), 'blog_shell.html'), encoding='utf-8').read()
shell_top, shell_bottom = HEAD.split('<!-- CONTENT -->')

# every other language: the same page, its own menu and footer words (words/<lang>.json "shell"), links to its own pages
def shell_words(lang):
    """Menu and footer words: Spanish has its own list; the others take the main site's own translations (i18n/<lang>.json)."""
    if 'shell' in WD[lang]: return WD[lang]['shell']
    d = json.load(open(os.path.join(os.path.dirname(__file__), '..', '..', 'i18n', f'{lang}.json'), encoding='utf-8'))
    pairs = [(f'>{k}<', f'>{d[k]}<') for k in ('AI &amp; the planet', 'Your data', 'Our mission', 'Get GreenCube',
                                               'Will it run on my computer?', 'ChatGPT &amp; your data', 'Contact', 'Privacy policy', 'Terms of use')]
    pairs += [(f'<h3>{k}</h3>', f'<h3>{d[k]}</h3>') for k in ('Product', 'Learn', 'Company')]
    ai = d["AI that's"]
    pairs.append(("AI that's <em>owned,</em> not rented.", f"{ai} <em>{d['owned,']}</em> {d['not rented.']}"))
    made = next(v for k, v in d.items() if k.endswith('Edunexis SL. Made in Spain.'))
    pairs.append(('Made in Spain.', made.split('Edunexis SL. ', 1)[1]))
    return pairs

def make_shell(lang):
    s = HEAD
    if lang != 'en':
        for p in ('ai-environmental-impact', 'your-data', 'mission', 'buy', 'what-you-get'):
            s = s.replace(f'href="https://greencube.app/{p}"', f'href="https://greencube.app/{lang}/{p}"')
        for a, b in [('<html lang="en">', f'<html lang="{html_lang(lang)}">'),
                     ('href="https://greencube.app/" class="brand"', f'href="https://greencube.app/{lang}/" class="brand"'),
                     ('href="https://greencube.app/" class="brand-lock"', f'href="https://greencube.app/{lang}/" class="brand-lock"'),
                     ('<a href="/blog" class="on">', f'<a href="/blog/{lang}" class="on">'), ('<li><a href="/blog">', f'<li><a href="/blog/{lang}">')] + shell_words(lang):
            assert a in s, (lang, a)
            s = s.replace(a, b)
    return tuple(s.split('<!-- CONTENT -->'))
SHELLS = {lang: make_shell(lang) for lang in BLOG_LANGS}

CODE_OF = {v[1]: k for k, v in SITE_LANGS.items()}  # html lang -> our code

def lang_menu(lang, alts):
    """The header's language menu, listing only the languages this page exists in (from its hreflang links)."""
    have = [(CODE_OF[h], u.replace(HOST, '')) for h, u in alts if h != 'x-default']
    if len(have) < 2: return ''
    items = ''.join(f'<a href="{u}" hreflang="{SITE_LANGS[l][1]}" lang="{SITE_LANGS[l][1]}"' + (' aria-current="true"' if l == lang else '')
                    + f'>{NAMES[l]}</a>' for l, u in have)
    return (f'<details class="lang-pick"><summary class="lang" aria-label="Language">{SITE_LANGS[lang][0]}</summary>'
            f'<div class="lang-list">{items}</div></details>')

def page(title, desc, url, og_image, ld, content, og_type='article', lang='en', alts=()):
    top, bottom = SHELLS[lang]
    top = top.replace('<!-- LANGS -->', lang_menu(lang, alts))
    links = ''.join(f'\n  <link rel="alternate" hreflang="{l}" href="{u}" />' for l, u in alts)
    top = (top.replace('<link rel="canonical" href="{{URL}}" />', '<link rel="canonical" href="{{URL}}" />' + links)
           .replace('{{TITLE}}', esc(title)).replace('{{DESC}}', esc(desc))
           .replace('{{URL}}', url).replace('{{OG_IMAGE}}', og_image).replace('{{OG_TYPE}}', og_type)
           .replace('{{LD}}', '\n'.join(f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)))
    if any(url.endswith('/' + slug) for slug in NOINDEX):
        top = top.replace('<link rel="canonical"', '<meta name="robots" content="noindex, follow" />\n  <link rel="canonical"', 1)
    out = HAN_GAP.sub('', CJK_GAP.sub(r'\1', top + content + bottom))
    for old, new in MERGED.items():  # link straight to the page a merged post now redirects to
        out = re.sub(r'(/blog/)' + re.escape(old) + r'(?=["#?])', r'\g<1>' + new, out)
    return out

CJK_GAP = re.compile(r'([。、！？：；）])[ ]+')  # Chinese and Japanese put no space after their own punctuation (a joined fragment brings one)
HAN_GAP = re.compile(r'(?<=[一-鿿]) (?=[约約] ?\d)')  # nor before 'about' when it lands after a word ('每秒 约 20' -> '每秒约 20')

report = []
listing = []
for p in idx:
    slug = p['slug']
    if slug in OWN_TITLES:  # rewritten as our own tested post at the same address; that version is built below
        continue
    if slug in MERGED:
        continue
    raw = open(f'{SRC}/posts/{slug}.html', encoding='utf-8').read()
    kinds = facts.notes_for(p['title'] + '\n' + raw + '\n' + '\n'.join(f['q'] + ' ' + f['a'] for f in p['faq']))
    body, ch1 = facts.fix_text(clean(raw))
    title, ch2 = facts.fix_text(p['title'])
    desc, ch3 = facts.fix_text(p['description'] or '')
    faq = []
    for f in p['faq']:
        q, _ = facts.fix_text(f['q']); a, _ = facts.fix_text(f['a']); faq.append((q, a))
    changed = bool(ch1 or ch2 or ch3 or kinds)
    published = (p['date_published'] or p['sitemap_lastmod'])[:10]
    # corrected posts count as updated on TODAY, but never before they were published (posts saved after 10-10)
    modified = max(TODAY, published) if changed else (p['date_modified'] or p['sitemap_lastmod'] or published)[:10]
    url = f'{HOST}/blog/{slug}'
    cover = image(p['cover_image']) if p['cover_image'] else None
    og = HOST + cover[0] if cover else 'https://greencube.app/og.jpg'
    ld = [{
        '@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': title, 'description': desc,
        'image': og, 'datePublished': published, 'dateModified': modified, 'inLanguage': 'en',
        'mainEntityOfPage': url,
        'author': {'@type': 'Organization', 'name': 'GreenCube', 'url': 'https://greencube.app'},
        'publisher': {'@type': 'Organization', 'name': 'GreenCube', 'url': 'https://greencube.app',
                      'logo': {'@type': 'ImageObject', 'url': 'https://greencube.app/icon-512.png'}},
    }]
    if faq:
        ld.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]})
    byline = f'GreenCube &middot; {nice_date(published)}' + (f' &middot; updated {nice_date(modified)}' if modified != published and changed else '')
    content = (
        f'<article>\n<p class="kicker"><a href="/blog">GreenCube blog</a></p>\n<h1>{esc(title)}</h1>\n'
        f'<p class="byline">{byline}</p>\n{note(kinds)}\n{tested_box(slug)}'
        + (f'<img class="cover" src="{cover[0]}" alt="{esc(p["cover_alt"] or "")}" width="{cover[1]}" height="{cover[2]}" fetchpriority="high"/>\n' if cover else '')
        + body +
        '\n<div class="cta-box"><h3>Your own AI, on your own PC</h3>'
        '<p>GreenCube runs on your computer: no usage limits, no subscription, works without internet. &euro;9.99, paid once.</p>'
        '<a class="cta" href="https://greencube.app/buy">Get GreenCube <span aria-hidden="true">&rarr;</span></a></div>\n</article>\n')
    open(f'{OUT}/{slug}.html', 'w', encoding='utf-8').write(page(f'{title} | GreenCube blog', desc, url, og, ld, content))
    listing.append((slug, title, desc, published, modified))
    report.append({'slug': slug, 'note': kinds, 'text_fixes': [list(c) for c in ch1 + ch2 + ch3]})

# ---------- our own posts: blog-archive/own/<slug>.html, a <!--meta {json} --> block then the body ----------
#     Spanish ones live in blog-archive/own/es/ and are served at /blog/es/<slug>; "alt" in the meta names the
#     other language's slug, which links the pair with hreflang (x-default = English).
def date_in(lang): return lambda iso: pc_pages.date(iso[:10], lang)
WORDS = {lang: dict(WD[lang]['post'], date=date_in(lang)) for lang in BLOG_LANGS}
def post_url(lang, slug): return HOST + pc_pages.blog_path(lang, slug)
AUTHOR = 'Hector Gras'  # our own tested posts are his; the archived BabyLoveGrowth posts stay signed GreenCube
def author_url(lang): return post_url(lang, 'hector-gras')
AUTHOR_PAGE = {lang: WD[lang]['author'] for lang in BLOG_LANGS}
own = []
for lang in BLOG_LANGS:
    folder = f'{SRC}/own' if lang == 'en' else f'{SRC}/own/{lang}'
    for fn in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
        if fn.endswith('.html'):
            raw = open(f'{folder}/{fn}', encoding='utf-8').read()
            m = re.match(r'\s*<!--meta\s*(\{.*?\})\s*-->\s*', raw, re.S)
            body = (raw[m.end():].replace('<!--pcs:table-->', pc_pages.table(lang)).replace('<!--pcs:checker-->', pc_pages.checker(lang))
                    .replace('{{pcs}}', str(pc_pages.count())))
            meta = json.loads(m.group(1).replace('{{pcs}}', str(pc_pages.count())))
            own.append((lang, fn[:-5], meta, body))
    own += [(lang, s, m, b) for s, m, b in pc_pages.pages(lang)]  # one page per measured PC, written from data/pcs.json
# a post and its translations share one key, the English slug: other languages name it in "alt"
def group_key(lang, slug, meta): return slug if lang == 'en' else meta.get('alt', slug)
groups = {}
for lang, slug, meta, body in own:
    groups.setdefault(group_key(lang, slug, meta), {})[lang] = post_url(lang, slug)
listings = {lang: [] for lang in BLOG_LANGS}
own_meta = {}

def localize_links(body, lang):
    """A translated post is written with the English links; point each one at this language's page when it exists."""
    if lang in ('en', 'es'): return body  # English needs nothing; the Spanish posts carry their own links
    def blog(m):
        g = groups.get(m.group(1), {})
        return f'href="{g[lang].replace(HOST, "")}{m.group(2) or ""}"' if lang in g else m.group(0)
    def site(m):
        p = m.group(1) or ''
        if not p: return f'href="https://greencube.app/{lang}/{m.group(2) or ""}"'
        return f'href="https://greencube.app/{lang}/{p}{m.group(2) or ""}"' if os.path.exists(f'{lang}/{p}.html') else m.group(0)
    body = re.sub(r'href="/blog/([a-z0-9-]+)(#[^"]*)?"', blog, body)
    return re.sub(r'href="https://greencube\.app/?([a-z0-9-]*)(#[^"]*)?"', site, body)

for lang, slug, meta, body in own:
    W = WORDS[lang]
    body = localize_links(body, lang)
    title, desc, published = meta['title'], meta['description'], meta['date']
    url = post_url(lang, slug)
    group = groups[group_key(lang, slug, meta)]
    alts = ()
    if len(group) > 1:
        alts = tuple((html_lang(l), group[l]) for l in BLOG_LANGS if l in group) + ((('x-default', group['en']),) if 'en' in group else ())
    faq = [(f['q'], f['a']) for f in meta.get('faq', [])]
    ld = [{
        '@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': title, 'description': desc,
        'image': 'https://greencube.app/og.jpg', 'datePublished': published, 'dateModified': meta.get('modified', published),
        'inLanguage': html_lang(lang), 'mainEntityOfPage': url,
        'author': {'@type': 'Person', 'name': AUTHOR, 'url': author_url(lang)},
        'publisher': {'@type': 'Organization', 'name': 'GreenCube', 'url': 'https://greencube.app',
                      'logo': {'@type': 'ImageObject', 'url': 'https://greencube.app/icon-512.png'}},
    }]
    faq_html = ''
    if faq:
        ld.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]})
        faq_html = (f'<h2>{W["questions"]}</h2>\n<div class="faq">\n'
                    + '\n'.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq) + '\n</div>\n')
    content = (
        f'<article>\n<p class="kicker"><a href="{W["home"]}">{W["kicker"]}</a></p>\n<h1>{esc(title)}</h1>\n'
        f'<p class="byline">{W["by"]} <a href="{author_url(lang).replace(HOST, "")}">{AUTHOR}</a> &middot; {W["date"](published)}'
        + (f' &middot; {W["updated"]} {W["date"](meta["modified"])}' if meta.get('modified', published) != published else '')
        + '</p>\n'
        + body + faq_html +
        f'\n<div class="cta-box"><h3>{W["cta_h"]}</h3><p>{W["cta_p"]}</p>'
        f'<a class="cta" href="{W["cta_url"]}">{W["cta_a"]} <span aria-hidden="true">&rarr;</span></a></div>\n</article>\n')
    path = f'{OUT}/{slug}.html' if lang == 'en' else f'{OUT}/{lang}/{slug}.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(page(f'{title} | {W["kicker"]}', desc, url, 'https://greencube.app/og.jpg', ld, content, lang=lang, alts=alts))
    (listing if lang == 'en' else listings[lang]).append((slug, title, desc, published, meta.get('modified', published)))
    own_meta[(lang, slug)] = meta
listings['en'] = listing
for ls in listings.values():
    ls.sort(key=lambda l: l[3], reverse=True)
def home_url(lang): return f'{HOST}/blog' if lang == 'en' else f'{HOST}/blog/{lang}'

# ---------- the list pages: short hero, "start here" cards, then one short list of titles per topic ----------
TOPICS = [  # (key, tint class, words in the slug that put a post there); first match wins
    ('study', 'b', ('student', 'study', 'flashcard', 'pdf', 'notebooklm', 'humata', 'exam', 'writers', 'grammarly', 'homeschool', 'teacher', 'researcher')),
    ('limits', 'y', ('limit', 'unlimited', 'subscription', 'lifetime', 'limites', 'chatgpt-free')),
    ('pc', 'g', ('gaming-pc', 'pc-gaming', 'hardware', 'laptop', 'models', 'small-llm', 'llm', 'gguf', 'quantization',
                 'setup', 'install', 'windows', 'mac', 'context-window', 'internet', 'offline', 'local-ai', 'llama', 'air-gapped', 'secure-ai')),
    ('tools', 'p', ('alternatives', '-vs-', 'ollama', 'lm-studio', 'desktop-apps', 'chatbot', 'ui', 'gemini', 'claude', 'chatgpt')),
]
_svg = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{}</svg>'
ICONS = {  # one small line icon per topic
    'pc': _svg.format('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>'),
    'study': _svg.format('<path d="M3 5.5C5.5 4.5 8.5 4.5 12 6.5c3.5-2 6.5-2 9-1V19c-2.5-1-5.5-1-9 1-3.5-2-6.5-2-9-1z"/><path d="M12 6.5V20"/>'),
    'limits': _svg.format('<path d="M7.5 15.5c-2 0-3.5-1.6-3.5-3.5s1.5-3.5 3.5-3.5c3.5 0 5.5 7 9 7 2 0 3.5-1.6 3.5-3.5S18.5 8.5 16.5 8.5c-3.5 0-5.5 7-9 7z"/>'),
    'tools': _svg.format('<rect x="4" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.5"/>'),
    'more': _svg.format('<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>'),
}

def topic_of(slug):
    for key, tint, words in TOPICS:
        if any(w in slug for w in words): return key, tint
    return 'more', 'p'
LIST_WORDS = {lang: WD[lang]['list'] for lang in BLOG_LANGS}
SHOW = 6  # titles shown per topic before "Show all"
# the best posts per topic, shown first under short plain names; every other post sits behind "Show all"
PICKS = {'en': {
    'pc': [('best-local-ai-models', 'Best AI models to run on your PC'), ('hardware-for-local-ai', 'What PC you need for AI'),
           ('best-small-llm', 'Best small AI models'), ('local-ai-chatbot-windows', 'Offline AI on Windows'),
           ('offline-ai-mac', 'Offline AI on Mac'), ('best-laptop-ai-assistant', 'AI on a laptop')],
    'study': [('best-ai-for-students', 'Best AI for students'), ('study-guide-from-pdf', 'Turn a PDF into a study guide'),
              ('flashcards-from-pdf', 'Make flashcards from a PDF'), ('notebooklm-alternatives', 'NotebookLM alternatives'),
              ('offline-ai-for-students', 'Offline AI for students'), ('ai-study-planner-offline', 'Plan your study week with AI')],
    'limits': [('unlimited-ai', 'AI with no usage limits'), ('ai-without-subscription', 'AI without a subscription'),
               ('chatgpt-free-limits', 'ChatGPT free limits'), ('lifetime-ai-software', 'Pay once, keep it')],
    'tools': [('best-offline-ai-chatbot', 'Best offline AI chatbots'), ('best-ai-desktop-apps', 'Best AI desktop apps'),
              ('ollama-vs-lm-studio', 'Ollama vs LM Studio'), ('lm-studio-alternatives', 'LM Studio alternatives'),
              ('chatgpt-offline', 'ChatGPT offline?'), ('private-ai-assistant', 'Most private AI assistant')],
}}
# the blog home asks the questions students ask; each tile opens the post that answers it
QUESTIONS = {'en': [('best-ai-for-students', 'Best AI for students?'), ('study-guide-from-pdf', 'PDF to a study guide?'),
                    ('unlimited-ai', 'AI with no limits?'), ('ollama-vs-lm-studio', 'Ollama or LM Studio?'),
                    ('hardware-for-local-ai', 'What PC do I need?'), ('flashcards-from-pdf', 'Flashcards from a PDF?'),
                    ('ai-without-subscription', 'AI without a subscription?'), ('chatgpt-offline', 'ChatGPT offline?')]}
GUIDE_WORDS = {'en': dict(lib='Library', lib_sub='All {n} guides, A to Z.')}

def topic_sections(lang, rest, L):
    pinned = {s: key for key, picks in PICKS.get(lang, {}).items() for s, _ in picks}
    tint_of = {k: tn for k, tn, _ in TOPICS}
    groups = {}
    for e in rest:
        where = (pinned[e[0]], tint_of[pinned[e[0]]]) if e[0] in pinned else topic_of(e[0])
        groups.setdefault(where, []).append(e)
    sections = []
    for key, tint in [(k, t) for k, t, _ in TOPICS] + [('more', 'p')]:
        posts = groups.get((key, tint), [])
        if not posts: continue
        have = {e[0] for e in posts}
        top = [(s, label) for s, label in PICKS.get(lang, {}).get(key, []) if s in have]
        others = [(e[0], e[1]) for e in posts if e[0] not in dict(top)]
        items = ''.join(f'<li><a href="{L["base"]}{s}">{esc(label)}</a></li>' for s, label in top + others)
        sections.append(f'<section class="hub-topic {tint}"><h2><span class="dot" aria-hidden="true"></span>{L["topics"][key]}</h2>'
                        f'<ul class="hub-list">{items}</ul></section>')
    return sections

def list_page(lang, entries, url, path):
    L = LIST_WORDS[lang]
    hidden = ('pc', 'guide') if lang in GUIDE_WORDS else ('pc',)  # with no library (Spanish), a rewritten old post shows as a card
    feat = [e for e in entries if (lang, e[0]) in own_meta and own_meta[(lang, e[0])].get('kind') not in hidden]
    feat.sort(key=lambda e: own_meta[(lang, e[0])].get('rank', 99))
    # PC pages are reached from their test, not listed here; an old post we rewrote ("guide") stays in the library
    rest = [e for e in entries if (lang, e[0]) not in own_meta or own_meta[(lang, e[0])].get('kind') == 'guide']
    cards = []
    for i, (s, t, d, pub, _) in enumerate(feat):
        m = own_meta[(lang, s)]
        stat = f'<b class="hub-stat">{m["stat"]}</b>' if m.get('stat') else ''
        cards.append(f'<a class="hub-feat {("g", "b", "y", "p")[i % 4]}" href="{L["base"]}{s}"><span class="hub-top">{stat}</span>'
                     f'<span class="hub-body"><h3>{esc(t)}</h3><p>{esc(m.get("teaser", d))}</p>'
                     f'<span class="hub-go">{L["read"]} <span aria-hidden="true">&rarr;</span></span></span></a>')
    # the library: every other guide, A to Z, plain titles (leading numbers and prices ignored when sorting)
    G = GUIDE_WORDS.get(lang)
    guides = ''
    if rest and G:
        sort_key = lambda e: re.sub(r'^[^A-Za-z]+', '', e[1]).lower()
        pinned = {s: key for key, picks in PICKS.get(lang, {}).items() for s, _ in picks}
        tint_of = dict((k, tn) for k, tn, _ in TOPICS)
        def where(s):
            return (pinned[s], tint_of[pinned[s]]) if s in pinned else topic_of(s)
        books = ''.join(f'<li><a href="{L["base"]}{s}"><span class="lib-ico {where(s)[1]}">{ICONS[where(s)[0]]}</span>'
                        f'<span class="lib-txt"><h3>{esc(t)}</h3><p>{esc(d)}</p></span></a></li>'
                        for s, t, d, *_ in sorted(rest, key=sort_key))
        guides = (f'<section class="hub-sec" id="library"><h2>{G["lib"]}</h2><p class="hub-sub">{G["lib_sub"].format(n=len(rest))}</p>'
                  f'<ul class="library">{books}</ul></section>\n')
    content = (
        '<article class="list hub">\n'
        f'<section class="hub-hero"><p class="kicker">{L["kicker"]}</p><h1>{L["h1"]}</h1><p class="lede">{L["lede"]}</p>'
        f'<p class="hub-btns"><a class="cta" href="#tests">{L["go"]} <span aria-hidden="true">&darr;</span></a>'
        f'<a class="hub-ghost" href="{L["nudge_url"]}">{L["nudge"]}</a></p></section>\n'
        + (f'<section class="hub-sec" id="tests"><h2>{L["tests"]}</h2><p class="hub-sub">{L["tests_sub"]}</p>'
           f'<div class="hub-feats">{"".join(cards)}</div></section>\n' if cards else '')
        + guides
        + '</article>\n')
    open(path, 'w', encoding='utf-8').write(page(L['title'], L['desc'], url, 'https://greencube.app/og.jpg',
        [{'@context': 'https://schema.org', '@type': 'Blog', 'name': L['kicker'], 'url': url, 'inLanguage': html_lang(lang)}],
        content, og_type='website', lang=lang, alts=all_langs(home_url, [l for l in BLOG_LANGS if listings[l]])))

def all_langs(url_of, langs):
    """hreflang links for a page that exists in every language listed, English as the default"""
    if len(langs) < 2: return ()
    return tuple((html_lang(l), url_of(l)) for l in langs) + (('x-default', url_of('en')),)

def mine_of(lang):
    return sorted([e for e in listings[lang] if (lang, e[0]) in own_meta and own_meta[(lang, e[0])].get('kind') != 'pc'],
                  key=lambda e: own_meta[(lang, e[0])].get('rank', 99))

# ---------- the author page, one per language ----------
authors = [l for l in BLOG_LANGS if mine_of(l)]
for lang in authors:
    entries = listings[lang]
    A, W = AUTHOR_PAGE[lang], WORDS[lang]
    mine = mine_of(lang)
    url = author_url(lang)
    items = ''.join(f'<li><a href="{post_url(lang, s).replace(HOST, "")}"><h3>{esc(t)}</h3><p>{esc(own_meta[(lang, s)].get("teaser", d))}</p></a></li>'
                    for s, t, d, *_ in mine)
    content = (f'<article class="list hub">\n<section class="hub-sec hub-allpage"><p class="kicker"><a href="{W["home"]}">{A["kicker"]}</a></p>'
               f'<h1>{AUTHOR}</h1><p class="hub-sub">{A["role"]}</p>' + ''.join(f'<p>{x}</p>' for x in A['bio'])
               + f'<p>{A["contact"]} <a href="mailto:support@greencube.app">support@greencube.app</a>.</p>'
               f'<h2 class="hub-h" style="margin-top:36px !important">{A["tests"]}</h2><ul class="library">{items}</ul></section>\n</article>\n')
    ld = [{'@context': 'https://schema.org', '@type': 'ProfilePage', 'url': url, 'inLanguage': html_lang(lang),
           'mainEntity': {'@type': 'Person', 'name': AUTHOR, 'url': url, 'jobTitle': A['role'],
                          'worksFor': {'@type': 'Organization', 'name': 'GreenCube', 'url': 'https://greencube.app'}}}]
    path = f'{OUT}/hector-gras.html' if lang == 'en' else f'{OUT}/{lang}/hector-gras.html'
    open(path, 'w', encoding='utf-8').write(page(A['title'], A['desc'], url, 'https://greencube.app/og.jpg', ld, content,
        og_type='profile', lang=lang, alts=all_langs(author_url, authors)))

for lang in BLOG_LANGS[1:]:
    if listings[lang]:
        list_page(lang, listings[lang], home_url(lang), f'{OUT}/{lang}/index.html')
list_page('en', listing, f'{HOST}/blog', f'{OUT}/index.html')

open(f'{OUT}/{pc_pages.CSV_NAME}', 'w', encoding='utf-8', newline='').write(pc_pages.csv_text())  # every measurement, for anyone to download

# ---------- sitemap ----------
urls = [f'  <url><loc>{HOST}/blog</loc><lastmod>{max(l[4] for l in listing)}</lastmod></url>'] + \
       [f'  <url><loc>{HOST}/blog/{s}</loc><lastmod>{m}</lastmod></url>' for s, _, _, _, m in listing if s not in NOINDEX] + \
       [f'  <url><loc>{author_url(lg)}</loc><lastmod>{max(e[4] for e in listings[lg])}</lastmod></url>' for lg in authors]
for lg in BLOG_LANGS[1:]:
    if listings[lg]:
        urls += [f'  <url><loc>{home_url(lg)}</loc><lastmod>{max(l[4] for l in listings[lg])}</lastmod></url>'] + \
                [f'  <url><loc>{post_url(lg, s)}</loc><lastmod>{m}</lastmod></url>' for s, _, _, _, m in listings[lg]]
open(f'{OUT}/sitemap.xml', 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(urls) + '\n</urlset>\n')

json.dump(report, open(f'{SRC}/build-report.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
mb = sum(os.path.getsize(f'{OUT}/images/{f}') for f in os.listdir(f'{OUT}/images')) / 1e6
print(f'{len(listing)} posts, {len(os.listdir(OUT + "/images"))} images ({mb:.1f} MB), '
      f'{sum(1 for r in report if r["note"])} with an update note, {sum(1 for r in report if r["text_fixes"])} with text fixes')
