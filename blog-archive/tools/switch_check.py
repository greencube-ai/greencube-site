"""After the blog switch: does every address answer on the new host?

    python blog-archive/tools/switch_check.py            (from the site repo root)

Checks every URL in our blog sitemap, every old BabyLoveGrowth sitemap URL we saved
(blog-archive/old-sitemap-urls.txt), and the host rules (/ -> /blog, /sitemap.xml,
the IndexNow key file, non-blog paths -> greencube.app). Prints only what is wrong.
"""
import re, sys, urllib.request, urllib.error

HOST = 'https://blog.greencube.app'
UA = {'User-Agent': 'Mozilla/5.0 (GreenCube switch check)'}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
opener = urllib.request.build_opener(NoRedirect)

def status(url):
    try:
        r = opener.open(urllib.request.Request(url, headers=UA), timeout=20)
        return r.status, r.headers.get('Location'), r.read(4000).decode('utf-8', 'ignore')
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get('Location'), ''
    except Exception as e:
        return 0, None, str(e)

ours = re.findall(r'<loc>([^<]+)</loc>', open('blog/sitemap.xml', encoding='utf-8').read())
old = [l.strip() for l in open('blog-archive/old-sitemap-urls.txt', encoding='utf-8') if l.strip()]
bad = 0
for u in sorted(set(ours + old)):
    code, loc, body = status(u)
    if code != 200:
        bad += 1; print('NOT 200', code, u, loc or '')
    elif 'babylovegrowth' in body.lower():
        bad += 1; print('STILL BLG', u)
for path, want_code, want_loc in (('/', 308, '/blog'), ('/sitemap.xml', 307, '/blog/sitemap.xml'),
                                  ('/4e7f8a6e94f6cc248272edab7eeb48f5.txt', 200, None),
                                  ('/buy', 308, 'https://greencube.app/buy')):
    code, loc, _ = status(HOST + path)
    if code not in (want_code, 301, 302, 307, 308) or (want_loc and (loc or '').rstrip('/') != want_loc.rstrip('/')):
        if not (want_code == 200 and code == 200):
            bad += 1; print('RULE', path, code, loc)
print(f'{len(set(ours + old))} addresses checked, {bad} problems')
sys.exit(1 if bad else 0)
