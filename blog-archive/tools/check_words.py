"""Check every words/<lang>.json against words/en.json: same keys, same {placeholders}, same HTML tags.

    python blog-archive/tools/check_words.py        (prints only what is wrong)

A placeholder English uses only for its own grammar ({an}, "a"/"an" before a number) may be left out.
"""
import json, os, re, sys

DIR = os.path.join(os.path.dirname(__file__), 'words')
EN = json.load(open(os.path.join(DIR, 'en.json'), encoding='utf-8'))
OPTIONAL = {'an', 'The', 'm'}  # grammar helpers a language may not need
NOT_TEXT = {'pcs', 'shell', 'units'}  # per-language extras, not translations of English
bad = 0

def walk(e, o, where, lang):
    global bad
    if isinstance(e, dict):
        if not isinstance(o, dict): bad += 1; print(lang, where, 'is not a group'); return
        for k in e:
            if k in NOT_TEXT and where == '': continue
            if k not in o: bad += 1; print(lang, where + '/' + k, 'missing'); continue
            walk(e[k], o[k], where + '/' + k, lang)
        for k in o:
            if k not in e and not (k in NOT_TEXT and where == ''): bad += 1; print(lang, where + '/' + k, 'not in English')
    elif isinstance(e, list):
        if not isinstance(o, list) or len(o) != len(e): bad += 1; print(lang, where, 'list length differs'); return
        for i, (a, b) in enumerate(zip(e, o)): walk(a, b, f'{where}[{i}]', lang)
    elif isinstance(e, str):
        if not isinstance(o, str): bad += 1; print(lang, where, 'is not text'); return
        pe, po = set(re.findall(r'\{(\w+)\}', e)), set(re.findall(r'\{(\w+)\}', o))
        if po - pe or (pe - po) - OPTIONAL:
            bad += 1; print(lang, where, 'placeholders differ:', sorted(pe), sorted(po))
        te, to = sorted(re.findall(r'</?(\w+)', e)), sorted(re.findall(r'</?(\w+)', o))
        if te != to: bad += 1; print(lang, where, 'tags differ:', te, to)
        glue = lambda x: bool(re.match(r'[\s,;:.]', x))  # a fragment that attaches to the text before it
        if e.endswith('\n') != o.endswith('\n') or glue(e) != glue(o):
            bad += 1; print(lang, where, 'leading space or trailing newline differs')

for f in sorted(os.listdir(DIR)):
    if f.endswith('.json') and f != 'en.json':
        walk(EN, json.load(open(os.path.join(DIR, f), encoding='utf-8')), '', f[:-5])
print(f'{bad} problems')
sys.exit(1 if bad else 0)
