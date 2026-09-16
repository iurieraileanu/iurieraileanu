# -*- coding: utf-8 -*-
import re, pathlib, html as H
B = pathlib.Path('/home/user/iurieraileanu/build')
h = (B / 'stage3.html').read_text(encoding='utf-8')

# ---------------------------------------------- 1. galeria devine lightbox ---
def gal(m):
    fig = m.group(0)
    src = re.search(r'src="([^"]+)"', fig).group(1)
    alt = re.search(r'alt="([^"]*)"', fig).group(1)
    cap = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.search(r'<figcaption>(.*?)</figcaption>', fig, flags=re.S).group(1))).strip()
    btn = ('<button type="button" class="vtn-lbbtn" data-vtn-src="%s" data-vtn-alt="%s" data-vtn-cap="%s">'
           '<span class="vtn-sr">Mărește fotografia: %s</span></button>') % (src, H.escape(alt, quote=True), H.escape(cap, quote=True), H.escape(alt))
    return fig.replace('<figure>', '<figure class="vtn-rv">', 1).replace('</figure>', btn + '</figure>', 1)

h, n = re.subn(r'<figure><img[^>]*>\s*<figcaption>.*?</figcaption></figure>', gal, h, flags=re.S)
print('galerie:', n, 'figuri')

# ---------------------------------------- 2. apariție la derulare pe blocuri --
pairs = [('<article class="vtn-ens">', '<article class="vtn-ens vtn-rv">'),
         ('<article class="vtn-person">', '<article class="vtn-person vtn-rv">'),
         ('<div class="vtn-repcard">', '<div class="vtn-repcard vtn-rv">'),
         ('<div class="vtn-quote">', '<div class="vtn-quote vtn-rv">'),
         ('<div class="vtn-time-row">', '<div class="vtn-time-row vtn-rv">'),
         ('<div class="vtn-room">', '<div class="vtn-room vtn-rv">'),
         ('<a class="vtn-ytcard"', '<a class="vtn-ytcard vtn-rv"'),
         ('<div class="vtn-box">', '<div class="vtn-box vtn-rv">'),
         ('<div class="vtn-callout">', '<div class="vtn-callout vtn-rv">')]
for a, b in pairs:
    c = h.count(a); h = h.replace(a, b); print('  %-34s %d' % (a[:34], c))
h = re.sub(r'<h2>', '<h2 class="vtn-rv">', h)
h = h.replace('<h2 class="vtn-rv" class="vtn-rv">', '<h2 class="vtn-rv">')

# ------------------------------------- 3. panglica tricoloră între secțiuni --
for anchor in ['<section class="vtn-sec vtn-sec--deep" id="vtn-inchiriere">',
               '<section class="vtn-sec vtn-sec--deep" id="vtn-media">',
               '<section class="vtn-sec vtn-sec--deep vtn-final" id="vtn-inscrieri">']:
    assert h.count(anchor) == 1, anchor
    h = h.replace(anchor, '<hr class="vtn-ribbon" aria-hidden="true">\n' + anchor, 1)

(B / 'stage4.html').write_text(h, encoding='utf-8')
print('etapa 4 OK')
