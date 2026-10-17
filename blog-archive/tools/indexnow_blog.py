"""Tell Bing (IndexNow; Bing feeds ChatGPT and Copilot) about every blog page at once.

    python blog-archive/tools/indexnow_blog.py           (from the site repo root, after the switch)

The key file must answer at https://blog.greencube.app/<key>.txt (vercel.json lets it through).
A 200 or 202 reply means accepted.
"""
import json, re, urllib.request

KEY = '4e7f8a6e94f6cc248272edab7eeb48f5'
HOST = 'blog.greencube.app'
urls = re.findall(r'<loc>([^<]+)</loc>', open('blog/sitemap.xml', encoding='utf-8').read())
body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'https://{HOST}/{KEY}.txt', 'urlList': urls}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body,
                             headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    r = urllib.request.urlopen(req, timeout=30)
    print('IndexNow', r.status, 'for', len(urls), 'URLs')
except urllib.error.HTTPError as e:
    print('IndexNow refused', e.code, e.read()[:300])
