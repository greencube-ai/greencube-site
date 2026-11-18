"""Blog covers, round 2 (Hector 18 Nov: "a lot more different styles, simple but different for everything").
One style per kind of post, picked from the slug and title: X vs Y, hardware, numbered lists, checklists/guides,
pictures, privacy, limits/price, studying, questions, and the old drawing card for the rest. Same 1200x630 size,
same paper + pastels + General Sans as the site. Rendered with headless Edge from http://127.0.0.1:8765.
Usage: python make_covers2.py [out_dir]   (writes <out>/<slug>.png for every line of specs_en.txt)"""
import os, re, sys, html, hashlib, subprocess
SITE = r'C:\dev\greencube\site'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SITE, 'zz-covers-v2')
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
s = open(os.path.join(SITE, 'index.html'), encoding='utf-8').read(); i = s.find('id="what"'); j = s.find('</section>', i)
ART = {re.search(r'make-kind">([^<]+)', m.group(2)).group(1).strip(): re.search(r'<svg.*?</svg>', m.group(2), re.S).group(0)
       for m in re.finditer(r'<article class="make (t-\w+)">(.*?)</article>', s[i:j], re.S)}
PAL = [('#8EA674', '#4E5F3A', '#E4EBD9'), ('#FA9F75', '#A8492A', '#FCE3D6'), ('#8EABE1', '#3D5E93', '#DFE7F6'),
       ('#FAE289', '#8A6B1C', '#FCF3CF'), ('#E9A6B5', '#93415A', '#F8E1E7'), ('#9FD6C2', '#2F6E5A', '#DDF1E9'),
       ('#B9A6E0', '#5B4691', '#ECE6F7'), ('#8FD0E8', '#22657E', '#DCF0F7'), ('#E3C9A0', '#7A5A2A', '#F4EADB')]
def pick(slug, n): return int(hashlib.md5(slug.encode()).hexdigest(), 16) % n
def esc(t): return html.escape(t, quote=False)
def mark(head): return esc(head).replace('[', '<span class="hl">').replace(']', '</span>')
def plain(head): return head.replace('[', '').replace(']', '')

HL = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 100' preserveAspectRatio='none'%3E%3Cpath fill='%23F9DD5E' "
      "d='M30 16C110 8 190 15 290 9C380 4 450 13 560 8C660 3 740 12 840 7C900 4 940 10 972 9L990 15L968 21L997 29L974 36L999 44L971 51L996 59L975 66L998 74L970 81L992 88L978 93C900 99 820 91 720 97C620 102 540 92 440 98C340 103 240 93 150 99C100 101 60 96 24 95L6 88L28 81L2 73L24 66L0 58L26 51L3 43L25 36L1 28L22 21L8 15Z'/%3E%3C/svg%3E\")")
BASE = """<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="http://127.0.0.1:8765/fonts/fonts.css"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1200px;height:630px;overflow:hidden}
body{font-family:'General Sans',sans-serif;color:#1A1A1A;background:#F5F1E8}
.c{position:relative;width:1200px;height:630px;overflow:hidden}
.k{font-weight:600;font-size:22px;letter-spacing:.14em;text-transform:uppercase}
h1{font-weight:600;letter-spacing:-.035em;line-height:1.04}
.hl{position:relative;isolation:isolate;white-space:nowrap}
.hl::before{content:'';position:absolute;z-index:-1;left:-.06em;right:-.05em;top:.12em;bottom:.02em;background:HLURL no-repeat center/100% 100%;transform:rotate(-1deg)}
.brand{position:absolute;left:70px;bottom:44px;display:flex;align-items:center;gap:12px;font-weight:600;font-size:24px}
.brand i{width:20px;height:20px;border:4px solid currentColor;border-radius:6px}
.line{height:14px;border-radius:7px;background:currentColor;opacity:.16}
STYLE</style></head><body><div class="c">BODY<div class="brand"><i></i>GreenCube blog</div></div></body></html>""".replace('HLURL', HL)

def fs(text, big, small, cut=18):  # headline size by length
    n = len(plain(text)); return big if n <= cut else (small if n <= cut * 2 else int(small * .86))

def s_vs(sp, t, P):
    a, b = t['names']; c, deep, light = P
    st = f""".c{{background:{light};display:flex;flex-direction:column;padding:56px 70px}}
.k{{color:{deep}}} .row{{flex:1;display:flex;align-items:center;justify-content:center;gap:0;margin-top:-10px}}
.tile{{width:400px;height:290px;border-radius:40px;display:grid;place-items:center;text-align:center;padding:24px;font-weight:600;letter-spacing:-.03em;line-height:1}}
.a{{background:#FFFDF7;transform:rotate(-4deg);box-shadow:0 30px 60px -30px {deep}80;border:2px solid #fff}}
.b{{background:{c};color:#1A1A1A;transform:rotate(3deg);box-shadow:0 30px 60px -30px {deep}}}
.vs{{width:96px;height:96px;margin:0 -18px;z-index:2;border-radius:50%;background:#1A1A1A;color:#F5F1E8;display:grid;place-items:center;font-weight:600;font-size:40px}}"""
    size = lambda n: 70 if len(n) <= 7 else (56 if len(n) <= 10 else 44)
    body = (f'<div class="k">{esc(sp["kicker"])}</div><div class="row"><div class="tile a" style="font-size:{size(a)}px">{esc(a)}</div>'
            f'<div class="vs">vs</div><div class="tile b" style="font-size:{size(b)}px">{esc(b)}</div></div>')
    return st, body

def s_number(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:{c};display:flex;align-items:center;padding:0 70px;gap:50px}}
.n{{font-weight:600;font-size:360px;line-height:.8;letter-spacing:-.06em;color:#FFFDF7;text-shadow:0 18px 0 {deep}40;flex:none}}
.t{{display:flex;flex-direction:column;gap:22px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 74, 62)}px}}
.brand{{color:#1A1A1A}}"""
    return st, f'<div class="n">{t["num"]}</div><div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div>'

def s_chip(sp, t, P):
    c, deep, light = P
    gpu = t['gpu']
    draw = ("""<div class="gpu"><div class="fan"></div><div class="fan"></div><div class="pins"></div></div>""" if gpu else
            """<div class="lap"><div class="scr"><div class="line" style="width:70%"></div><div class="line" style="width:50%"></div><div class="line" style="width:60%"></div></div><div class="kb"></div></div>""")
    st = f""".c{{background:#1F211A;color:#F5F1E8;display:flex;align-items:center;padding:0 70px;gap:56px}}
.t{{flex:1;display:flex;flex-direction:column;gap:20px}} .k{{color:{c}}}
.name{{font-weight:600;font-size:{96 if len(t['hw']) <= 9 else 72}px;letter-spacing:-.04em;line-height:1}}
.sub{{font-size:30px;color:#CFCBBE;font-weight:500;max-width:520px;line-height:1.25}}
.tag{{align-self:flex-start;background:#F9DD5E;color:#1A1A1A;font-weight:600;font-size:22px;padding:8px 16px;border-radius:10px;letter-spacing:.04em}}
.gpu{{width:430px;height:250px;border-radius:26px;background:{c};position:relative;display:flex;align-items:center;justify-content:space-evenly;transform:rotate(-5deg);box-shadow:0 40px 80px -30px #000}}
.fan{{width:150px;height:150px;border-radius:50%;background:repeating-conic-gradient({deep} 0 18deg,transparent 18deg 45deg),#1F211A;border:10px solid {deep}}}
.pins{{position:absolute;bottom:-22px;left:60px;width:260px;height:22px;background:repeating-linear-gradient(90deg,#F9DD5E 0 10px,transparent 10px 16px)}}
.lap{{transform:rotate(-4deg)}} .scr{{width:420px;height:260px;border-radius:20px 20px 6px 6px;background:#FFFDF7;border:14px solid {c};padding:40px 34px;display:flex;flex-direction:column;gap:18px;color:#1A1A1A}}
.kb{{width:500px;height:26px;margin-left:-40px;border-radius:0 0 20px 20px;background:{c}}} .brand{{color:#F5F1E8}}"""
    body = (f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><div class="name">{esc(t["hw"])}</div>'
            f'<div class="sub">{esc(plain(sp["head"]))}</div><div class="tag">MEASURED</div></div>{draw}')
    return st, body

def s_check(sp, t, P):
    c, deep, light = P
    rows = ''.join(f'<div class="r"><span class="bx{" on" if k < 2 else ""}"></span><div class="line" style="width:{w}%"></div></div>' for k, w in enumerate((78, 62, 70, 54)))
    st = f""".c{{background:{light};display:flex;align-items:center;padding:0 70px;gap:50px}}
.t{{flex:1;display:flex;flex-direction:column;gap:24px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 80, 66)}px}}
.list{{width:400px;background:#FFFDF7;border-radius:30px;padding:40px 34px;display:flex;flex-direction:column;gap:30px;transform:rotate(2.5deg);box-shadow:0 30px 60px -30px {deep}}}
.r{{display:flex;align-items:center;gap:20px;color:#1A1A1A}} .r .line{{flex:none}}
.bx{{width:36px;height:36px;border-radius:10px;border:4px solid {deep};flex:none;position:relative}}
.bx.on{{background:{c};border-color:{c}}} .bx.on::after{{content:'';position:absolute;left:9px;top:3px;width:9px;height:17px;border:solid #1A1A1A;border-width:0 5px 5px 0;transform:rotate(45deg)}}"""
    return st, f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="list">{rows}</div>'

def s_photo(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:url(http://127.0.0.1:8765/demo/{t['img']}) center/cover}}
.c::after{{content:'';position:absolute;inset:0;background:linear-gradient(90deg,#1A1A1Acc 0,#1A1A1A55 55%,transparent)}}
.t{{position:absolute;z-index:2;left:70px;top:0;bottom:0;width:640px;display:flex;flex-direction:column;justify-content:center;gap:22px;color:#FFFDF7}}
.k{{color:#F9DD5E}} h1{{font-size:{fs(sp['head'], 82, 68)}px}} .hl::before{{opacity:.9}} .hl{{color:#1A1A1A}}
.brand{{z-index:2;color:#FFFDF7}} .made{{position:absolute;z-index:2;right:40px;bottom:40px;background:#FFFDF7;color:#1A1A1A;font-weight:600;font-size:20px;padding:10px 16px;border-radius:12px}}"""
    return st, f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="made">Made with GreenCube, offline</div>'

def s_lock(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:{deep};color:#FFFDF7;display:flex;align-items:center;padding:0 70px;gap:60px}}
.t{{flex:1;display:flex;flex-direction:column;gap:24px}} .k{{color:{c}}} h1{{font-size:{fs(sp['head'], 80, 66)}px}} .hl{{color:#1A1A1A}}
.lock{{position:relative;width:300px;height:330px;flex:none;transform:rotate(4deg)}}
.sh{{position:absolute;left:55px;top:0;width:190px;height:200px;border:34px solid {c};border-bottom:0;border-radius:110px 110px 0 0}}
.bd{{position:absolute;left:0;bottom:0;width:300px;height:210px;border-radius:40px;background:#FFFDF7;display:grid;place-items:center;box-shadow:0 40px 80px -30px #0008}}
.kh{{width:44px;height:80px;border-radius:22px;background:{deep}}} .brand{{color:#FFFDF7}}"""
    return st, f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="lock"><div class="sh"></div><div class="bd"><div class="kh"></div></div></div>'

def s_bubble(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:{light};display:flex;align-items:center;padding:0 70px;gap:44px}}
.t{{flex:1;display:flex;flex-direction:column;gap:24px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 80, 64)}px}}
.chat{{width:430px;display:flex;flex-direction:column;gap:18px}}
.b{{border-radius:26px;padding:24px 26px;display:flex;flex-direction:column;gap:12px}}
.me{{align-self:flex-end;width:280px;background:#1A1A1A;color:#FFFDF7;border-bottom-right-radius:8px}}
.ai{{width:360px;background:#FFFDF7;color:#1A1A1A;border-bottom-left-radius:8px;box-shadow:0 20px 40px -24px {deep}}}
.cap{{align-self:flex-start;display:flex;align-items:center;gap:12px;background:{c};color:#1A1A1A;font-weight:600;font-size:26px;padding:14px 22px;border-radius:999px;transform:rotate(-3deg)}}
.ring{{width:30px;height:30px;border-radius:50%;background:conic-gradient(#1A1A1A 0 300deg,transparent 300deg);border:3px solid #1A1A1A}}"""
    body = (f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="chat">'
            '<div class="b me"><div class="line" style="width:90%"></div><div class="line" style="width:60%"></div></div>'
            '<div class="b ai"><div class="line" style="width:95%"></div><div class="line" style="width:80%"></div><div class="line" style="width:55%"></div></div>'
            f'<div class="cap"><span class="ring"></span>{esc(t["cap"])}</div></div>')
    return st, body

def s_card(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:{c};display:flex;align-items:center;padding:0 70px;gap:40px}}
.t{{flex:1;display:flex;flex-direction:column;gap:24px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 80, 66)}px}}
.stack{{position:relative;width:400px;height:320px;flex:none}}
.cd{{position:absolute;inset:0;border-radius:30px;background:#FFFDF7;padding:44px 40px;display:flex;flex-direction:column;gap:20px;color:#1A1A1A;box-shadow:0 30px 60px -30px {deep}}}
.cd.b1{{transform:rotate(9deg) translate(28px,10px);background:{light}}} .cd.b2{{transform:rotate(4deg) translate(14px,4px);background:#FBF8F0}}
.cd.f{{transform:rotate(-3deg)}} .q{{width:56px;height:56px;border-radius:16px;background:{deep};color:#FFFDF7;display:grid;place-items:center;font-weight:600;font-size:30px}}
.cnt{{position:absolute;right:34px;top:44px;font-weight:600;font-size:20px;color:{deep}}}"""
    body = (f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="stack">'
            '<div class="cd b1"></div><div class="cd b2"></div><div class="cd f"><div class="q">Q</div><span class="cnt">1 / 18</span>'
            '<div class="line" style="width:92%"></div><div class="line" style="width:74%"></div><div class="line" style="width:40%;margin-top:18px;opacity:.3"></div></div></div>')
    return st, body

def s_question(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:{c};display:flex;align-items:center;padding:0 70px}}
.qm{{position:absolute;right:-30px;top:-120px;font-weight:600;font-size:880px;line-height:1;color:#FFFDF7;opacity:.55;letter-spacing:-.05em}}
.t{{position:relative;z-index:2;width:820px;display:flex;flex-direction:column;gap:24px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 92, 78)}px}}"""
    return st, f'<div class="qm">?</div><div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div>'

def s_term(sp, t, P):
    c, deep, light = P
    rows = ''.join(f'<div class="r"><b>$</b><span class="line" style="width:{w}%"></span></div>' if k % 2 == 0 else
                   f'<div class="r o"><span class="line" style="width:{w}%"></span></div>' for k, w in enumerate((62, 80, 48, 70, 36)))
    st = f""".c{{background:{light};display:flex;align-items:center;padding:0 70px;gap:50px}}
.t{{flex:1;display:flex;flex-direction:column;gap:24px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 80, 64)}px}}
.term{{width:460px;border-radius:22px;background:#1F211A;box-shadow:0 30px 60px -30px #000;overflow:hidden;transform:rotate(-2.5deg);flex:none}}
.bar{{height:44px;background:#2C2F25;display:flex;align-items:center;gap:10px;padding:0 18px}} .bar i{{width:14px;height:14px;border-radius:50%;background:#FA9F75}}
.bar i:nth-child(2){{background:#FAE289}} .bar i:nth-child(3){{background:#8EA674}}
.body{{padding:30px 28px;display:flex;flex-direction:column;gap:20px;color:#F5F1E8}} .r{{display:flex;align-items:center;gap:14px}}
.r b{{color:{c};font-size:26px;font-family:monospace}} .r .line{{opacity:.5}} .r.o .line{{color:{c};opacity:.55;margin-left:30px}}
.cur{{width:14px;height:26px;background:{c};margin-left:30px}}"""
    return st, (f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div>'
                f'<div class="term"><div class="bar"><i></i><i></i><i></i></div><div class="body">{rows}<div class="cur"></div></div></div>')

def s_bag(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:{c};display:flex;align-items:center;padding:0 70px;gap:60px}}
.t{{flex:1;display:flex;flex-direction:column;gap:24px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 80, 64)}px}}
.bag{{position:relative;width:340px;height:300px;flex:none;transform:rotate(-4deg)}}
.hd{{position:absolute;left:105px;top:0;width:130px;height:80px;border:22px solid #1F211A;border-bottom:0;border-radius:30px 30px 0 0}}
.bx{{position:absolute;left:0;bottom:0;width:340px;height:236px;border-radius:34px;background:#FFFDF7;box-shadow:0 30px 60px -30px {deep}}}
.bx::before{{content:'';position:absolute;left:0;right:0;top:78px;height:14px;background:{light}}}
.bx::after{{content:'';position:absolute;left:146px;top:62px;width:48px;height:46px;border-radius:10px;background:{deep}}}"""
    return st, f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="bag"><div class="hd"></div><div class="bx"></div></div>'

def s_window(sp, t, P):
    c, deep, light = P
    mac = t.get('mac')
    st = f""".c{{background:{light};display:flex;flex-direction:column;justify-content:center;padding:0 70px 40px;gap:26px}}
.k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 72, 60)}px;max-width:560px}}
.win{{position:absolute;right:-40px;top:70px;width:560px;height:420px;border-radius:22px;background:#FFFDF7;box-shadow:0 30px 70px -30px {deep};overflow:hidden;transform:rotate(-3deg)}}
.tb{{height:52px;background:{c};display:flex;align-items:center;gap:10px;padding:0 20px;justify-content:{'flex-start' if mac else 'flex-end'}}}
.tb i{{width:16px;height:16px;border-radius:{'50%' if mac else '3px'};background:#FFFDF7;opacity:.85}}
.gridw{{padding:30px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}} .gridw span{{height:100px;border-radius:16px;background:{light}}}
.gridw span:nth-child(2){{background:{c};opacity:.6}}"""
    return st, (f'<div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1>'
                f'<div class="win"><div class="tb"><i></i><i></i><i></i></div><div class="gridw">{"<span></span>" * 6}</div></div>')

def s_board(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:#7A5A2A;padding:34px}}
.bd{{position:relative;width:100%;height:100%;border-radius:18px;background:#2F4A3A;box-shadow:inset 0 0 80px #0006;display:flex;flex-direction:column;justify-content:center;padding:0 60px 40px;gap:24px;color:#F5F1E8}}
.k{{color:{c}}} h1{{font-size:{fs(sp['head'], 84, 70)}px;font-weight:500;letter-spacing:-.02em}} .hl{{color:#1A1A1A}}
.chalk{{position:absolute;right:70px;bottom:46px;width:120px;height:22px;border-radius:6px;background:#F5F1E8;transform:rotate(-8deg)}}
.sc{{position:absolute;right:80px;top:70px;width:220px;height:6px;border-radius:3px;background:#F5F1E8;opacity:.35;transform:rotate(-4deg);box-shadow:0 40px 0 #F5F1E8,0 80px 0 #F5F1E880}}
.brand{{color:#F5F1E8;left:104px;bottom:78px}}"""
    return st, f'<div class="bd"><div class="sc"></div><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1><div class="chalk"></div></div>'

def s_timer(sp, t, P):
    c, deep, light = P
    st = f""".c{{background:{deep};color:#FFFDF7;display:flex;align-items:center;padding:0 70px;gap:60px}}
.t{{flex:1;display:flex;flex-direction:column;gap:24px}} .k{{color:{c}}} h1{{font-size:{fs(sp['head'], 80, 64)}px}} .hl{{color:#1A1A1A}}
.w{{position:relative;width:330px;height:330px;flex:none}}
.dial{{position:absolute;inset:0;border-radius:50%;background:conic-gradient({c} 0 250deg,#FFFDF722 250deg);display:grid;place-items:center}}
.dial::after{{content:'';position:absolute;inset:34px;border-radius:50%;background:{deep}}}
.time{{position:relative;z-index:2;font-weight:600;font-size:{64 if len(t['time']) <= 6 else 48}px;letter-spacing:-.03em}}
.knob{{position:absolute;left:145px;top:-34px;width:40px;height:30px;border-radius:8px;background:{c}}}"""
    return st, f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="w"><div class="knob"></div><div class="dial"><span class="time">{esc(t["time"])}</span></div></div>'


def s_classic(sp, t, P):
    c, deep, light = P
    st = f""".c{{display:flex;align-items:center;gap:40px;padding:64px 70px;background:radial-gradient(circle at 88% 12%, {light} 0 16%, transparent 16.3%),radial-gradient(circle at 6% 104%, {light} 0 20%, transparent 20.3%),#F5F1E8}}
.t{{flex:1;display:flex;flex-direction:column;gap:26px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 88, 76)}px}}
.art{{flex:0 0 380px;height:380px;border-radius:44px;display:grid;place-items:center;transform:rotate(3deg);background:{light};border:2px solid #fff;box-shadow:0 30px 60px -30px {deep}}}
.art svg{{width:230px;height:230px}}"""
    return st, f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="art">{ART.get(sp["art"], "")}</div>'

NAMES = {'chatgpt': 'ChatGPT', 'greencube': 'GreenCube', 'claude': 'Claude', 'gemini': 'Gemini', 'ollama': 'Ollama', 'lm-studio': 'LM Studio',
         'gguf': 'GGUF', 'ggml': 'GGML', 'llama-3': 'Llama 3', 'gemma': 'Gemma', 'gemma-4-e2b': 'Gemma E2B', 'e4b': 'Gemma E4B',
         'offline-ai': 'Offline AI', 'cloud-ai': 'Cloud AI', 'rag': 'RAG', 'fine-tuning': 'Fine-tuning',
         'anythingllm': 'AnythingLLM', 'bard': 'Bard', 'bing-chat': 'Bing Chat', 'deepseek': 'DeepSeek', 'elicit': 'Elicit',
         'gpt4all': 'GPT4All', 'grammarly': 'Grammarly', 'humata-ai': 'Humata', 'meta-ai': 'Meta AI', 'microsoft-copilot': 'Copilot',
         'monica-ai': 'Monica', 'notebooklm': 'NotebookLM', 'notion-ai': 'Notion AI', 'novelai': 'NovelAI', 'openwebui': 'Open WebUI',
         'pdfai': 'PDF.ai', 'perplexity': 'Perplexity', 'poe': 'Poe', 'typingmind': 'TypingMind', 'consensus': 'Consensus'}

def s_alts(sp, t, P):
    c, deep, light = P
    n = t['alt']
    st = f""".c{{background:{light};display:flex;align-items:center;padding:0 70px;gap:30px}}
.t{{width:470px;display:flex;flex-direction:column;gap:22px}} .k{{color:{deep}}} h1{{font-size:{fs(sp['head'], 72, 60)}px}}
.flow{{flex:1;display:flex;align-items:center;gap:26px}}
.old{{padding:28px 30px;border-radius:28px;background:#FFFDF7;font-weight:600;font-size:{54 if len(n) <= 9 else 40}px;letter-spacing:-.03em;color:#8A836F;text-decoration:line-through;text-decoration-thickness:5px;text-decoration-color:{deep};transform:rotate(-4deg);box-shadow:0 24px 50px -28px {deep}}}
.arr{{font-size:64px;font-weight:600;color:{deep}}}
.opts{{display:flex;flex-direction:column;gap:14px}} .o{{width:170px;height:58px;border-radius:16px;background:{c};display:flex;align-items:center;padding:0 18px;gap:12px}}
.o .line{{flex:1;opacity:.35;color:#1A1A1A}} .o i{{width:22px;height:22px;border-radius:7px;background:#FFFDF7}}
.o:nth-child(2){{transform:translateX(26px)}}"""
    o = '<div class="o"><i></i><span class="line"></span></div>'
    return st, (f'<div class="t"><div class="k">{esc(sp["kicker"])}</div><h1>{mark(sp["head"])}</h1></div><div class="flow"><div class="old">{esc(n)}</div>'
                f'<div class="arr">&rarr;</div><div class="opts">{o * 3}</div></div>')
def name_of(part):
    best = max((k for k in NAMES if part.startswith(k)), key=len, default=None)
    return NAMES[best] if best else part.replace('-', ' ').title()
HW = [(r'rtx[- ]?(\d{4})( ti)?', 'RTX {}'), (r'gtx[- ]?(\d{4})( super)?', 'GTX {}'), (r'rx[- ](\d{3,4})( xt)?', 'RX {}')]
def classify(slug, title, sp):
    t = {}; low = title.lower()
    if '-vs-' in slug:
        a, b = slug.split('-vs-', 1); t['names'] = (name_of(a), name_of(b)); return 'vs', t
    m = re.search(r'\b(rtx|gtx|rx)[- ]?(\d{3,4})([- ]?(ti|super|xt))?', slug + ' ' + low)
    if m or re.search(r'vram|8gb|without-gpu|hardware|requirements|can-my-pc|run-ai-on|local-ai-models|^ai-on-|laptop-ai|small-llm|llm-models', slug):
        t['hw'] = (m.group(0).upper().replace('-', ' ').replace('TI', 'Ti').replace('SUPER', 'Super') if m else
                   '8 GB RAM' if '8gb' in slug else 'VRAM' if 'vram' in slug else 'No GPU' if 'without-gpu' in slug else
                   'Gemma 4' if 'gemma' in slug else 'Laptop' if 'laptop' in slug else 'Your PC')
        t['gpu'] = bool(m) or 'vram' in slug or 'hardware' in slug
        return 'chip', t
    m = re.search(r'(?:top |^)(\d{1,2})\b|(?<![.,$€\d])\b(\d{1,2}) (?:apps|tools|options|ways|ais|local|offline|real|alternatives|questions)', low)
    if m and ('alternatives' in slug or re.search(r'apps|tools|options|ways|checked|top|ais', low)):
        t['num'] = m.group(1) or m.group(2); return 'number', t
    if re.search(r'image|picture|novelai', slug):
        t['img'] = ['img-01.webp', 'img-05.webp', 'img-09.webp', 'img-12.webp'][pick(slug, 4)]; return 'photo', t
    if re.search(r'privat|secure|safe|train|gdpr|ferpa|air-gapped|security', slug):
        return 'lock', t
    if re.search(r'ollama$|^ollama-in|quantization|gguf|rag-vs|context-window|self-hosted|developers', slug + ' ' + low):
        return 'term', t
    if 'alternatives' in slug:
        t['alt'] = name_of(slug.split('-alternatives')[0]); return 'alts', t
    if re.search(r'teacher|school|homeschool', slug):
        return 'board', t
    if re.search(r'business|freelancer|lawyer|travel|professional', slug):
        return 'bag', t
    if re.search(r'windows|offline-ai-mac|desktop-apps|local-ai-ui|no-setup', slug):
        t['mac'] = 'mac' in slug; return 'window', t
    m2 = re.search(r'(\d+)\s?(minutes|min|seconds)\b', low)
    if m2 or re.search(r'how long|speed|afternoon|measure', low):
        t['time'] = (m2.group(1) + (' min' if m2.group(2).startswith('m') else ' s')) if m2 else ('1 day' if 'afternoon' in low else 'tok/s'); return 'timer', t
    if re.search(r'student|study|flashcard|pdf|notes|teacher|homeschool|writer|research|summar', slug):
        return 'card', t
    if re.search(r'step|checklist|guide|policy|compliant|compliance|roadmap|workflow|hardening|prompts|deployment|pilot', low + ' ' + slug):
        return 'check', t
    if re.search(r'limit|unlimited|subscription|lifetime|login|9\.99|€|\$', slug + ' ' + low):
        t['cap'] = 'Limit reached' if 'limit' in slug else 'No account' if 'login' in slug else 'Paid once'; return 'bubble', t
    if title.rstrip().endswith('?') or '?' in plain(sp['head']):
        return 'question', t
    return 'classic', t
STYLES = dict(term=s_term, bag=s_bag, window=s_window, board=s_board, timer=s_timer, alts=s_alts, vs=s_vs, number=s_number, chip=s_chip, check=s_check, photo=s_photo, lock=s_lock, bubble=s_bubble, card=s_card, question=s_question, classic=s_classic)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for line in open(os.path.join(HERE, 'specs_en.txt'), encoding='utf-8'):
        if not line.strip() or line.startswith('#'): continue
        slug, kicker, head, art, col = [x.strip() for x in line.split('|')]
        try: title = html.unescape(re.search(r'<h1>(.*?)</h1>', open(os.path.join(SITE, 'blog', slug + '.html'), encoding='utf-8').read()).group(1))
        except Exception: title = plain(head)
        sp = dict(kicker=kicker, head=head, art=art)
        style, t = classify(slug, title, sp)
        st, body = STYLES[style](sp, t, PAL[pick(slug, len(PAL))])
        if style in ('number', 'chip', 'check', 'lock', 'bubble', 'card', 'classic', 'term', 'bag', 'timer') and pick(slug + 'm', 2):
            st += '.c{flex-direction:row-reverse}.brand{left:auto;right:70px}'  # mirrored: the picture on the left
        pat = '' if style in ('photo', 'question', 'board', 'window') else ['', 'dots', 'grid', 'diag', 'ring'][pick(slug + 'p', 5)]
        if pat:
            st += ('.c>*:not(.brand){position:relative;z-index:1}.c::before{content:"";position:absolute;pointer-events:none;' + {
                'dots': 'inset:0;background:radial-gradient(currentColor 2px,transparent 2.6px) 0 0/30px 30px;opacity:.09}',
                'grid': 'inset:0;background:linear-gradient(currentColor 1px,transparent 1px) 0 0/44px 44px,linear-gradient(90deg,currentColor 1px,transparent 1px) 0 0/44px 44px;opacity:.07}',
                'diag': 'inset:0;background:repeating-linear-gradient(-45deg,currentColor 0 2px,transparent 2px 24px);opacity:.06}',
                'ring': 'width:760px;height:760px;right:-240px;top:-300px;border-radius:50%;border:70px solid currentColor;opacity:.06}'}[pat])
        page = BASE.replace('STYLE', st).replace('BODY', body)
        hp = os.path.join(SITE, f'zz-c2-{slug}.html'); open(hp, 'w', encoding='utf-8').write(page)
        png = os.path.join(OUT, f'{slug}.png')
        subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={os.environ["TEMP"]}\\c2prof', '--window-size=1200,630',
                        '--virtual-time-budget=3000', f'--screenshot={png}', f'http://127.0.0.1:8765/zz-c2-{slug}.html'], timeout=60, capture_output=True)
        os.remove(hp)
        rows.append((slug, style, title))
        print(style.ljust(8), slug, '' if os.path.exists(png) else 'FAILED', flush=True)
    open(os.path.join(OUT, 'styles.tsv'), 'w', encoding='utf-8').write('\n'.join('\t'.join(r) for r in rows))
