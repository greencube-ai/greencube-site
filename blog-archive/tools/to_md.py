"""Our own HTML (blog posts, PC pages) -> plain markdown, for the .md copy next to each page.

Only the tags our pages use. Links become absolute, scripts and form controls are dropped,
a div of short stat boxes becomes a list, a table stays a table. Standard library only.
"""
import re
from html.parser import HTMLParser
from urllib.parse import urljoin

VOID = {'br', 'img', 'input', 'hr', 'meta', 'link', 'source', 'wbr'}
SKIP = {'script', 'style', 'button', 'input', 'select', 'label', 'svg', 'form', 'noscript', 'nav', 'footer', 'img'}
BLOCK = {'p', 'div', 'section', 'article', 'main', 'header', 'aside', 'ul', 'ol', 'li', 'table', 'blockquote', 'pre',
         'details', 'summary', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'figure', 'figcaption', 'dl', 'dt', 'dd'}


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.kids = tag, dict(attrs), parent, []


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.cur = Node('root', {}, None)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.cur)
        self.cur.kids.append(node)
        if tag not in VOID: self.cur = node

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag: n = n.parent  # tolerate an unclosed <p> or <li>
        if n is not self.root: self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)


def has_block(n):
    return any(isinstance(k, Node) and (k.tag in BLOCK or has_block(k)) for k in n.kids)


def inline(n, base):
    out = ''
    for k in n.kids:
        if isinstance(k, str):
            out += re.sub(r'\s+', ' ', k).replace('*', r'\*')
            continue
        if k.tag in SKIP: continue
        t = inline(k, base)
        if k.tag == 'br': t = ' '
        elif k.tag in ('strong', 'b') and t.strip(): t = f'**{t.strip()}**'
        elif k.tag in ('em', 'i') and t.strip(): t = f'*{t.strip()}*'
        elif k.tag == 'code': t = f'`{t}`'
        elif k.tag == 'sup' and t.strip(): t = f'[{t.strip()}]'  # a footnote number
        elif k.tag == 'a' and k.attrs.get('href') and t.strip():
            t = f'[{t.strip()}]({urljoin(base, k.attrs["href"])})'
        if out and t and not out[-1].isspace() and not t[0].isspace() and k.tag in ('span', 'div', 'b', 'strong') \
                and out[-1] not in '([' and t[0] not in '.,;:)':
            t = ' ' + t  # <b>14x</b><span>faster</span> reads as two words
        out += t
    return out


def table(n, base):
    rows = []
    def walk(x):
        for k in x.kids:
            if isinstance(k, Node):
                if k.tag == 'tr':
                    rows.append([inline(c, base).strip().replace('|', r'\|') for c in k.kids
                                 if isinstance(c, Node) and c.tag in ('td', 'th')])
                elif k.tag not in SKIP: walk(k)
    walk(n)
    rows = [r for r in rows if r]
    if not rows: return []
    w = max(len(r) for r in rows)
    rows = [r + [''] * (w - len(r)) for r in rows]
    return ['\n'.join(['| ' + ' | '.join(rows[0]) + ' |', '|' + ' --- |' * w] + ['| ' + ' | '.join(r) + ' |' for r in rows[1:]])]


def blocks(n, base, depth=0):
    out, run = [], ''
    def flush():
        nonlocal run
        if run.strip(): out.append(run.strip())
        run = ''
    for k in n.kids:
        if isinstance(k, str) or (k.tag not in BLOCK and not has_block(k)):
            if not (isinstance(k, Node) and k.tag in SKIP):
                run += inline(_wrap(k), base)
            continue
        flush()
        if k.tag in SKIP: continue
        if k.tag == 'section' and has_tag(k, ('input', 'select', 'button')):  # an interactive tool: its heading, its first line and a link to use it on the page
            h = find(k, ('h1', 'h2', 'h3', 'h4')); p = find(k, ('p',))
            if h: out.append('#' * int(h.tag[1]) + ' ' + inline(h, base).strip())
            out.append(((inline(p, base).strip() + ' ') if p else '')
                       + f'Interactive, on the page: {base}#{(h and h.attrs.get("id")) or k.attrs.get("id", "")}')
            continue
        if k.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            t = inline(k, base).strip()
            if t: out.append('#' * int(k.tag[1]) + ' ' + t)
        elif k.tag == 'table':
            out += table(k, base)
        elif k.tag in ('ul', 'ol'):
            items = [c for c in k.kids if isinstance(c, Node) and c.tag == 'li']
            out.append('\n'.join(('  ' * depth) + (f'{i}. ' if k.tag == 'ol' else '- ') + li(c, base, depth)
                                 for i, c in enumerate(items, 1)))
        elif 'stats' in k.attrs.get('class', '').split():
            out.append('\n'.join('- ' + inline(c, base).strip() for c in k.kids if isinstance(c, Node)))
        elif k.tag == 'blockquote':
            out += ['> ' + b.replace('\n', '\n> ') for b in blocks(k, base, depth)]
        elif not has_block(k):
            t = inline(k, base).strip()
            if t: out.append(t)
        else:
            out += blocks(k, base, depth)
    flush()
    return out


def has_tag(n, tags):
    return any(isinstance(k, Node) and (k.tag in tags or has_tag(k, tags)) for k in n.kids)


def find(n, tags):
    for k in n.kids:
        if isinstance(k, Node):
            if k.tag in tags: return k
            f = find(k, tags)
            if f: return f


def _wrap(k):
    w = Node('x', {}, None); w.kids = [k]; return w


def li(n, base, depth):
    head = Node('x', {}, None); head.kids = [k for k in n.kids if not (isinstance(k, Node) and k.tag in ('ul', 'ol'))]
    sub = Node('x', {}, None); sub.kids = [k for k in n.kids if isinstance(k, Node) and k.tag in ('ul', 'ol')]
    text = ' '.join(blocks(head, base, depth)) if has_block(head) else inline(head, base).strip()
    return text + ''.join('\n' + b for b in blocks(sub, base, depth + 1))


def convert(html, base):
    t = Tree(); t.feed(html); t.close()
    return '\n\n'.join(blocks(t.root, base)).strip() + '\n'


def page(title, desc, url, body_html, published=None, modified=None, author=None, faq=()):
    """One .md file: title, summary, canonical address and dates, the body, then the questions."""
    head = [f'# {title}', f'> {desc}', f'Canonical: {url}']
    if published: head.append(f'Published: {published}' + (f' · Updated: {modified}' if modified and modified != published else ''))
    if author: head.append(f'Author: {author}')
    md = head[0] + '\n\n' + head[1] + '\n\n' + '  \n'.join(head[2:]) + '\n\n' + convert(body_html, url)
    if faq:
        md += '\n## FAQ\n\n' + '\n\n'.join(f'### {q}\n\n{a}' for q, a in faq) + '\n'
    return md
