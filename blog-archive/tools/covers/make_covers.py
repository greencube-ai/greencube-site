"""Blog covers prototype (Hector 14 Nov: Medium-style cards with cool thumbnails). 1200x630 = card thumbnail + share
image. Paper background, big headline with one word on the site's yellow marker, one of the home page's own drawings
on a pastel tile, the GreenCube blog mark. Rendered with headless Edge from local HTML."""
import os, re, subprocess, sys, html
SITE = r'C:\dev\greencube\site'
OUT = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(SITE, 'index.html'), encoding='utf-8').read(); i = s.find('id="what"'); j = s.find('</section>', i)
ART = {}
for m in re.finditer(r'<article class="make (t-\w+)">(.*?)</article>', s[i:j], re.S):
    ART[re.search(r'make-kind">([^<]+)', m.group(2)).group(1).strip()] = re.search(r'<svg.*?</svg>', m.group(2), re.S).group(0)
COL = {'sage': ('#8EA674', '#4E5F3A'), 'tangerine': ('#FA9F75', '#A8492A'), 'wisteria': ('#8EABE1', '#3D5E93'), 'jasmine': ('#FAE289', '#8A6B1C')}
HL = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 100' preserveAspectRatio='none'%3E%3Cpath fill='%23F9DD5E' "
      "d='M30 16C110 8 190 15 290 9C380 4 450 13 560 8C660 3 740 12 840 7C900 4 940 10 972 9L990 15L968 21L997 29L974 36L999 44L971 51L996 59L975 66L998 74L970 81L992 88L978 93C900 99 820 91 720 97C620 102 540 92 440 98C340 103 240 93 150 99C100 101 60 96 24 95L6 88L28 81L2 73L24 66L0 58L26 51L3 43L25 36L1 28L22 21L8 15Z'/%3E%3C/svg%3E\")")
TPL = """<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="http://127.0.0.1:8765/fonts/fonts.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1200px;height:630px;overflow:hidden;background:#F5F1E8}
.c{position:relative;width:1200px;height:630px;padding:64px 70px;display:flex;align-items:center;gap:40px;
  background:radial-gradient(circle at 88% 12%, color-mix(in srgb,{c} 28%, #F5F1E8) 0 16%, transparent 16.3%),
  radial-gradient(circle at 6% 104%, color-mix(in srgb,{c} 22%, #F5F1E8) 0 20%, transparent 20.3%), #F5F1E8}
.t{flex:1 1 0;display:flex;flex-direction:column;gap:26px}
.k{font:600 22px 'General Sans',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:{deep}}
h1{font:600 {fs}px/1.04 'General Sans',sans-serif;letter-spacing:-.035em;color:#1A1A1A}
h1 .hl{position:relative;isolation:isolate;white-space:nowrap}
h1 .hl::before{content:'';position:absolute;z-index:-1;left:-.06em;right:-.05em;top:.12em;bottom:.02em;background:{hl} no-repeat center/100% 100%;transform:rotate(-1deg)}
.art{flex:0 0 380px;height:380px;border-radius:44px;display:grid;place-items:center;transform:rotate(3deg);
  background:radial-gradient(circle at 78% 22%, color-mix(in srgb,{c} 40%, #fff) 0 18%, transparent 19%), color-mix(in srgb,{c} 34%, #FDFBF5);
  box-shadow:0 30px 60px -30px color-mix(in srgb,{deep} 60%, transparent);border:2px solid color-mix(in srgb,{c} 60%, #fff)}
.art svg{width:230px;height:230px}
.brand{position:absolute;left:70px;bottom:44px;display:flex;align-items:center;gap:12px;font:600 26px 'General Sans',sans-serif;color:#1A1A1A}
.brand i{width:22px;height:22px;border:4px solid #7E8A5A;border-radius:6px}
</style></head><body><div class="c"><div class="t"><div class="k">{kicker}</div><h1>{head}</h1></div>
<div class="art">{art}</div><div class="brand"><i></i>GreenCube blog</div></div></body></html>"""
import sys as _s
LANG = _s.argv[1] if len(_s.argv) > 1 else 'en'
SPEC = _s.argv[2] if len(_s.argv) > 2 else os.path.join(OUT, 'specs_en.txt')
COVERS = []
for line in open(SPEC, encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    slug, kicker, head, art, col = [x.strip() for x in line.split('|')]
    head = html.escape(head).replace('[', '<span class="hl">').replace(']', '</span>')
    COVERS.append((slug, kicker, head, art, col))
os.makedirs(os.path.join(OUT, LANG), exist_ok=True)
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
for slug, kicker, head, art, col in COVERS:
    c, deep = COL[col]
    words = len(re.sub(r'<[^>]+>', '', head).split())
    page = (TPL.replace('{c}', c).replace('{deep}', deep).replace('{hl}', HL).replace('{fs}', str(76 if words > 5 else 88))
            .replace('{kicker}', html.escape(kicker)).replace('{head}', head).replace('{art}', ART[art]))
    if LANG == 'art':
        page = page.replace('<div class="t"><div class="k">', '<div class="t" style="display:none"><div class="k">').replace(
            '.c{position:relative;width:1200px;height:630px;padding:64px 70px;display:flex;align-items:center;gap:40px;',
            '.c{position:relative;width:1200px;height:630px;padding:64px 70px;display:flex;align-items:center;justify-content:center;gap:40px;').replace(
            '<div class="brand"><i></i>GreenCube blog</div>', '')
    hp = os.path.join(SITE, f'zz-cover-{LANG}-{slug}.html'); open(hp, 'w', encoding='utf-8').write(page)
    png = os.path.join(OUT, LANG, f'{slug}.png')
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={OUT}\\prof', '--window-size=1200,630',
                    '--virtual-time-budget=3000', f'--screenshot={png}', f'http://127.0.0.1:8765/zz-cover-{LANG}-{slug}.html'], timeout=60, capture_output=True)
    os.remove(hp)
    if not os.path.exists(png): print('FAILED', slug)
print('done', len(COVERS))
