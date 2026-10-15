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


HARDWARE_BLANKS = [
    ('<td>Entry-level</td><td>—</td>', '<td>Entry-level</td><td>8 GB</td>'),
    ('<td>Mid-range</td><td>—</td><td>PDF analysis', '<td>Mid-range</td><td>16 GB</td><td>PDF analysis'),
    ('<td>High-end (with GPU)</td><td>—</td>', '<td>High-end (with GPU)</td><td>16 GB + a 6 GB or larger graphics card</td>'),
    ('<td>— RAM handles basic chat;', '<td>8 GB of RAM handles basic chat;'),
    ('<td>Modern CPU + discrete GPU</td><td>—</td><td>—</td>', '<td>Modern CPU + discrete GPU</td><td>16 GB or more</td><td>10 GB+ free (more for pictures)</td>'),
    ('<td>Minimum</td><td>—</td><td>10 GB free</td><td>Integrated / — VRAM</td>', '<td>Minimum</td><td>8 GB</td><td>10 GB free</td><td>Integrated graphics, no card</td>'),
    ('<td>Mid-range</td><td>16 GB</td><td>—</td><td>4 GB VRAM</td>', '<td>Mid-range</td><td>16 GB</td><td>10 GB free</td><td>4 GB VRAM</td>'),
    ('<td>Recommended</td><td>—</td><td>—</td><td>—</td>', '<td>Recommended</td><td>16 GB or more</td><td>10 GB+ free</td><td>8 GB VRAM or more</td>'),
    ('<td>10 GB free</td><td>—</td>', '<td>10 GB free</td><td>10 GB+ free (more for pictures)</td>'),
]

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
    # the refund window is 15 days since 2026-10-11 (terms §5); only inside sentences about a refund
    def refund15(m):
        a = max(s.rfind('.', 0, m.start()), s.rfind('>', 0, m.start()), s.rfind('"', 0, m.start()))
        b = min([x for x in (s.find('.', m.end()), s.find('<', m.end()), s.find('"', m.end())) if x != -1] or [len(s)])
        if 'refund' not in s[a + 1:b].lower(): return m.group(0)
        changes.append((m.group(0), '15' + m.group(1)))
        return '15' + m.group(1)
    s = re.sub(r'\b14([- ]days?)\b', refund15, s)
    # the Why GreenCube page moved into the home page (2026-10-15); a link fix, not a content change
    s = re.sub(r'https://(?:www\.)?greencube\.app/(es/)?how-it-works', lambda m: f'https://greencube.app/{m.group(1) or ""}#can', s)
    for old, new in (('Refund window</td><td>14 days', 'Refund window</td><td>15 days'),
                     ('GreenCube offers 14 days', 'GreenCube offers 15 days'),
                     ('A 14-day window covers', 'A 15-day window covers')):
        if old in s:
            changes.append((old, new)); s = s.replace(old, new)
    # hardware tables BabyLoveGrowth left blank ("—"), filled with what we measured (8 GB chats, 16 GB for PDFs, a card for speed)
    for old, new in HARDWARE_BLANKS:
        if old in s:
            changes.append((old[:40], new[:40])); s = s.replace(old, new)
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
