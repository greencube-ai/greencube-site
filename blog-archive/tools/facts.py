"""Fact fixes applied to the saved BabyLoveGrowth posts before we publish them.

Only things a reader could act on are changed in the text (price, brand spelling).
Outdated product descriptions (the old Quick / All-rounder models, "no account")
are not rewritten; the post gets a dated note at the top instead (see notes_for).
"""
import re

GC = re.compile(r'green\s?cube', re.I)

PRICE_FIXES = [
    # GreenCube was €8.99 / €9 at different times; it's €9.99 / US$9.99 now.
    (r'€\s?8[.,]9[89]', '€9.99'),
    (r'€\s?9(?![.,]?\d)', '€9.99'),
    (r'\b9 euros\b', '9.99 euros'),
]
# "about $10" style wording only when the same sentence is about GreenCube
ABOUT_10 = re.compile(r'\b(about|approximately|around|roughly) \$10\b( USD)?', re.I)

OLD_MODELS = re.compile(r'All-rounder|\bQuick\b[^.<]{0,40}\bmodel|\btwo (local )?models\b|Llama 3\.2 3B|Gemma 4 E4B', re.I)
NO_ACCOUNT = re.compile(r'no (cloud )?accounts?\b|without (an )?account|no (account|sign[- ]?in|signup|sign[- ]up|login)\b|no account creation|no activation key', re.I)


def fix_text(s):
    """Fix prices and brand spelling in a piece of HTML or text. Returns (new, changes)."""
    changes = []
    def sub(rx, rep, s, only_gc=False):
        def r(m):
            if only_gc:
                # look at the surrounding sentence
                a = max(s.rfind('.', 0, m.start()), s.rfind('>', 0, m.start()))
                b = min([x for x in (s.find('.', m.end()), s.find('<', m.end())) if x != -1] or [len(s)])
                if not GC.search(s[a + 1:b]): return m.group(0)
            new = m.expand(rep) if '\\' in rep else rep
            changes.append((m.group(0), new))
            return new
        return re.sub(rx, r, s)
    for rx, rep in PRICE_FIXES:
        s = sub(rx, rep, s)
    s = sub(ABOUT_10, 'US$9.99', s, only_gc=True)
    s = s.replace('$9.99 USD', 'US$9.99')
    n = len(re.findall(r'\bGreencube\b', s))
    if n: changes.append(('Greencube', 'GreenCube x%d' % n))
    s = re.sub(r'\bGreencube\b', 'GreenCube', s)
    return s, changes


def gc_sentences(text):
    return [x for x in re.split(r'(?<=[.!?])\s+|\n', text) if GC.search(x)]


def notes_for(text):
    """Which outdated product details this post contains (only in sentences about GreenCube
    for the account check, anywhere for the old model names, which only GreenCube had)."""
    plain = re.sub(r'<[^>]+>', ' ', text)
    out = []
    if OLD_MODELS.search(plain): out.append('models')
    if any(NO_ACCOUNT.search(x) for x in gc_sentences(plain)): out.append('account')
    return out
