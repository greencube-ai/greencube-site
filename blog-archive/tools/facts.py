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


# The old product made you PICK "Quick" (Llama 3.2 3B, text-only) or "All-rounder" (Gemma 4 E4B).
# Today GreenCube picks for you: Gemma 4 E2B on smaller PCs, Gemma 4 E4B with a graphics card.
# Only phrases that mean the model are touched ("Quick fixes", "Quick how-to" stay).
Q = r'(?:&quot;|"|“|”|</?strong>|</?b>|</?em>)*'
MODEL_FIXES = [
    (r'At setup,? you (?:pick|choose)(?: between)?(?: one of)? two (?:local )?models(?: to download)?:', 'GreenCube picks one of two local models for your PC:'),
    (r'(?i:choose) ' + Q + 'Quick' + Q + ' or ' + Q + 'All-rounder' + Q + r' and download it', 'GreenCube picks the model that fits your PC and downloads it'),
    (r'choose ' + Q + 'Quick' + Q + ' or ' + Q + 'All-rounder' + Q + r' depending on whether you need image reading', 'GreenCube picks the model that fits your PC'),
    (r'with a ' + Q + 'Quick' + Q + ' or ' + Q + 'All-rounder' + Q + r' model download', 'with an AI model picked for your PC'),
    (Q + 'Quick' + Q + r'(?: model)?\s*\(Llama 3\.2 3B,\s*(?:about |roughly |around |~)?2\s?GB(?: download)?(?:,\s*(?:fast, )?text-only(?:, fast)?)?', 'the smaller model (Gemma 4 E2B, about 2.6 GB'),
    (Q + 'All-rounder' + Q + r'(?: model)?\s*\(Gemma 4 E4B,\s*(?:about |roughly |around |~)?4', 'the bigger model (Gemma 4 E4B, about 4'),
    (r'\bQuick pulls about 2\s?GB', 'The smaller model pulls about 2.6 GB'),
    (r'\bAll-rounder pulls about 4', 'the bigger one pulls about 4'),
    (r'the quick model is around 2\s?GB', 'the smaller model is around 2.6 GB'),
    (r'the all-rounder is about 4', 'the bigger model is about 4'),
    (Q + 'Quick' + Q + ' or ' + Q + 'All-rounder' + Q, 'the smaller or bigger model'),
    (r"(?:\bthe )?" + Q + 'All-rounder' + Q + r' model', 'the bigger model'),
    (r"(?:\bthe )?" + Q + 'Quick' + Q + r' model', 'the smaller model'),
    (r'\bpick ' + Q + 'Quick' + Q, 'get the smaller model'),
    (r'\bor ' + Q + 'All-rounder' + Q, 'or the bigger model'),
    (r'(smaller model|Quick option|Quick) \(Llama 3\.2 3B', 'smaller model (Gemma 4 E2B'),
    (r'\bQuick uses Llama 3\.2 3B, weighs in around 2\s?GB', 'The smaller model is Gemma 4 E2B, about 2.6 GB'),
    (r"GreenCube(&#x27;|')s Quick option", r"GreenCube\1s smaller model"),
    (r'\b(stick with|picked|pick|choose|chose|with|use|using|handle) ' + Q + 'Quick' + Q + r'\b(?! (?:fixes|how-to|diagnostics|start|tip|check|look|reference|summary|guide))', r'\1 the smaller model'),
    (r'\b' + Q + 'Quick' + Q + r' (can|can&#x27;t|cannot|is|handles|runs|works|for|and)\b', r'the smaller model \1'),
    (r'(smaller model[^.<]{0,60}?)(?:,\s*)?(?:and )?(?:can&#x27;t|cannot|can\'t) (?:see|read) images(?: at all)?', r'\1'),
    (r'((?:smaller model|Quick|built on|GreenCube)[^.]{0,50}?)Llama 3\.2 3B', r'\1Gemma 4 E2B'),
    (r'\bCurated local models \(Llama 3\.2 3B or Gemma 4 E4B\)', 'Curated local models (Gemma 4 E2B or E4B)'),
    (Q + 'Quick' + Q + r'\s*\((about|approximately|roughly|around) 2\s?GB', r'the smaller model (\1 2.6 GB'),
    (r'\b(as|since|because|but|while|unless) ' + Q + 'Quick' + Q + r' ', r'\1 the smaller model '),
    (r'\bQuick uses Gemma 4 E2B', 'The smaller model uses Gemma 4 E2B'),
    (Q + 'Quick' + Q + r'\s*\(~\s?2\s?GB', 'the smaller model (~2.6 GB'),
    (r'\bQuick or All-Rounder\b', 'the smaller or bigger model'),
    (r'\b(Pick|Choose) ' + Q + 'Quick' + Q + r'\b', r'\1 the smaller model'),
    (r'\bQuick needs about 2\s?GB', 'The smaller model needs about 2.6 GB'),
    (r'Bundled \(Llama 3\.2 3B or Gemma 4 E4B\)', 'Bundled (Gemma 4 E2B or E4B)'),
    (r'the (?:fast )?text-only the smaller model', 'the smaller, faster model'),
    (r'the image(?:[- ]and PDF)?-capable the bigger model', 'the bigger model'),
    (r'(Gemma 4 E2B, about 2\.6 GB),?\s*(?:fast, )?(?:text-only|plain text only)(?:, fast)?', r'\1, fast'),
    (r'(smaller model[^.<]{0,40}?)\b(?:fast, )?text-only\b ?', r'\1'),
    (Q + 'All-rounder' + Q, 'the bigger model'),
    (r"'s the (smaller|bigger) model", r"'s \1 model"),
    (r'&#x27;s the (smaller|bigger) model', r'&#x27;s \1 model'),
    (r'\bthe the (smaller|bigger)', r'the \1'),
    (r'\bThe the (smaller|bigger)', r'The \1'),
]

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

# Claims about GreenCube that are not true (it goes online to sign in once, download the AI and updates, and search when
# Online is on) or not measured (better than LM Studio, Ollama and the rest), fixed by exact phrase (2026-10-18)
ONLINE = 'it goes online only to sign in once, download the AI and its updates, and search the web when you turn Online on (it starts off every time)'
EXACT_FIXES = [
    ('The best offline AI chatbot for most users is <strong>Greencube</strong>: a one-time purchase desktop app',
     'One offline AI chatbot to look at is <strong>Greencube</strong>: a one-time purchase desktop app'),
    ('reads PDFs and images, and never phones home', 'reads PDFs and images, and keeps your chats and files on your PC'),
    ('deserve a tool that never phones home', 'deserve a tool that keeps them on your own PC'),
    ('reads their documents, and never phones home', 'reads their documents, and keeps their chats and files on their own machine'),
    ('understands your images, and never phones home', 'understands your images, and keeps your chats and files on your PC'),
    ('<td>Zero telemetry, fully local</td>', '<td>Chats and files stay on your PC</td>'),
    ('Greencube and Atomic Chat are explicit about zero external communication after setup.',
     'Greencube keeps your chats and files on your PC: ' + ONLINE + '.'),
    ('If zero data leakage is non-negotiable, choose Greencube or Atomic Chat. Both are explicit about no external communication.',
     'If keeping your chats on your own PC matters most, check what each app still sends. Greencube keeps chats and files on your PC; only Online search, which starts off every time, sends your question to a search engine.'),
    ('Greencube is the offline AI that actually works for most people', 'Where Greencube fits'),
    ('Greencube is the strongest choice for non-technical users. It installs', 'Greencube is built for non-technical users. It installs'),
    ('Apps like Greencube operate with zero telemetry and no external server communication after setup, meaning your conversations never leave your device.',
     'Check what each app still sends. Greencube keeps your chats and files on your PC; ' + ONLINE + '.'),
    ('Greencube supports PDF reading and image analysis fully offline. Most other apps on this list focus on text chat only, so document analysis is a meaningful differentiator for Greencube.',
     'Greencube reads PDFs and images offline. Several other apps on this list can chat with documents too, so check how each one handles long files.'),
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
    for old, new in EXACT_FIXES:
        if old in s:
            changes.append((old[:40], new[:40])); s = s.replace(old, new)
    for rx, rep in MODEL_FIXES:
        s, k = re.subn(rx, rep, s)
        if k: changes.append(('old model names', '%s x%d' % (rep[:30], k)))
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
