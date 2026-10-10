import sys, re, os, json, html, hashlib, urllib.request
raw, out = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(out, 'posts'), exist_ok=True)
os.makedirs(os.path.join(out, 'images'), exist_ok=True)

def meta(s, attr, name):
    m = re.search(r'<meta[^>]+%s="%s"[^>]+content="([^"]*)"' % (attr, re.escape(name)), s)
    return html.unescape(m.group(1)) if m else None

def fetch_img(url):
    ext = os.path.splitext(url.split('?')[0])[1].lower() or '.jpg'
    name = hashlib.sha1(url.encode()).hexdigest()[:12] + ext
    path = os.path.join(out, 'images', name)
    if not os.path.exists(path):
        for _ in range(5):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36", "Accept": "image/*"})
                with urllib.request.urlopen(req, timeout=40) as r: data = r.read()
                open(path, 'wb').write(data); break
            except Exception as e: err = e
        else:
            print('IMG FAIL', url, err); return url
    return 'images/' + name

index = []
for fn in sorted(os.listdir(raw)):
    if fn == 'blog.html': continue
    slug = fn[:-5]
    s = open(os.path.join(raw, fn), encoding='utf-8').read()
    a = re.search(r'<article[^>]*>([\s\S]*?)</article>', s).group(1)
    # drop BabyLoveGrowth CTA cards (they're nested divs; cut from marker to the matching close)
    while True:
        i = a.find('<div data-cta-card')
        if i < 0: break
        depth, j = 0, i
        for m in re.finditer(r'<(/?)div\b[^>]*>', a[i:]):
            depth += -1 if m.group(1) else 1
            if depth == 0: j = i + m.end(); break
        a = a[:i] + a[j:]
    imgs = {}
    def rep(m):
        u = html.unescape(m.group(1))
        imgs[u] = fetch_img(u)
        return 'src="%s"' % imgs[u]
    a = re.sub(r'src="(https://[^"]+)"', rep, a)
    lds = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', s)]
    graph = []
    for ld in lds: graph += ld.get('@graph', [ld])
    art = next((g for g in graph if g.get('@type') in ('Article', 'BlogPosting')), {})
    faq = next((g for g in graph if g.get('@type') == 'FAQPage'), None)
    cover = meta(s, 'property', 'og:image') or (art.get('image') or {}).get('url')
    rec = {
        'slug': slug,
        'old_url': 'https://blog.greencube.app/blog/' + slug,
        'title': html.unescape(re.search(r'<title>([^<]*)</title>', s).group(1)),
        'description': meta(s, 'name', 'description'),
        'date_published': art.get('datePublished'),
        'date_modified': art.get('dateModified'),
        'language': art.get('inLanguage'),
        'cover_image': fetch_img(cover) if cover else None,
        'cover_alt': (art.get('image') or {}).get('caption'),
        'faq': [{'q': q['name'], 'a': q['acceptedAnswer']['text']} for q in faq['mainEntity']] if faq else [],
        'words': len(re.sub(r'<[^>]+>', ' ', a).split()),
        'image_count': len(imgs),
    }
    open(os.path.join(out, 'posts', slug + '.html'), 'w', encoding='utf-8').write(a.strip() + '\n')
    index.append(rec)
    print(slug, rec['words'], 'words', len(imgs), 'imgs', 'faq', len(rec['faq']))
json.dump(index, open(os.path.join(out, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('posts', len(index), 'images', len(os.listdir(os.path.join(out, 'images'))))
