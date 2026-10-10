import sys, os, re, html, json, collections
d = sys.argv[1]
idx = json.load(open(os.path.join(d, 'index.json')))
rules = [
 ('Wrong price', r'€\s?8[.,]9\d|€\s?8[.,]98|€\s?9(?![.,]\d)\b|\b9 ?euros?\b|about \$10|approximately \$10|\$10 USD|€9,'),
 ('Old product (Quick / All-rounder models)', r'\bQuick model|All-rounder|\btwo (local )?models\b|Quick \(~'),
 ('Promises a 14-day refund', r'14[- ]day refund|refund window|refund period|two full weeks'),
 ('Says no account / no sign-in', r'no account (is )?required|without (an )?account|no sign[- ]?(in|up) (required|needed)'),
 ('Legal compliance claim about GreenCube', r'GreenCube[^.]{0,80}\b(HIPAA|FERPA|GDPR|SOC ?2)[- ]?(compliant|certified|ready)|\b(HIPAA|FERPA|GDPR)[- ](compliant|certified)[^.]{0,60}GreenCube'),
 ('Says it runs on Mac/Linux today', r'GreenCube[^.]{0,60}\b(runs|works|available) on (mac|macos|linux)\b'),
 ('"Lifetime" / "forever"', r'GreenCube[^.]{0,80}\b(lifetime|forever)\b|\b(lifetime|forever)\b[^.]{0,60}GreenCube'),
]
res = {}
for p in idx:
    t = open(os.path.join(d, 'posts', p['slug'] + '.html'), encoding='utf-8').read()
    t = p['title'] + '. ' + p['description'] + '. ' + html.unescape(re.sub(r'<[^>]+>', ' ', t)) + ' ' + ' '.join(f['q'] + ' ' + f['a'] for f in p['faq'])
    t = re.sub(r'\s+', ' ', t)
    hits = {}
    for name, rx in rules:
        m = re.findall(rx, t, re.I)
        if m: hits[name] = len(m)
    res[p['slug']] = {'hits': hits, 'brand_lowercase': len(re.findall(r'\bGreencube\b', t)), 'title': p['title'], 'words': p['words'], 'date': (p['date_published'] or '')[:10]}
c = collections.Counter(k for r in res.values() for k in r['hits'])
for k, v in c.most_common(): print(f'{v:3d} posts: {k}')
print(f"{sum(1 for r in res.values() if r['brand_lowercase'])} posts: brand written 'Greencube' instead of 'GreenCube'")
print(f"{sum(1 for r in res.values() if r['hits'])} of {len(res)} posts have at least one wrong fact")
json.dump(res, open(os.path.join(d, 'audit.json'), 'w'), indent=1)
