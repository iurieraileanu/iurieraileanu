# -*- coding: utf-8 -*-
"""Previzualizare locală: înlocuiește fotografiile de pe site cu fișiere locale
sau cu substitute generate, ca să se poată verifica aspectul fără internet."""
import re, base64, io, pathlib, unicodedata
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path('/home/user/iurieraileanu')
SRC = ROOT / 'landing-torino-nord/landing-torino-nord-v4.html'
FOTO = ROOT / 'landing-torino-nord/foto-torino-nord'
ASSETS = pathlib.Path('/tmp/claude-0/-home-user-iurieraileanu')
cand = list(ASSETS.glob('*/scratchpad/zipnou/grupul-vatra-torino-nord/assets'))
WEBP = cand[0] if cand else None

h = SRC.read_text(encoding='utf-8')
srcs = sorted(set(re.findall(r'https://grupulvatra\.com/wp-content/uploads/[^"]+', h)))

def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return re.sub(r'[^a-z0-9]+', ' ', ''.join(c for c in s if not unicodedata.combining(c)))

local = {}
for f in FOTO.glob('*.jpg'):
    local[f.stem] = f
webps = {f.stem: f for f in (WEBP.glob('*.webp') if WEBP else [])}

KEY = [('sala-mare', 'sala-mare'), ('sala-arte', 'sala-mica'), ('studio', 'studio'),
       ('media', 'media'), ('balet', 'balet'), ('calus', 'calus'), ('copii', 'copii'),
       ('adult', 'adulti'), ('elle', 'elle'), ('hora', 'hora'), ('mugurel', 'mugurel'),
       ('veselia', 'veselia'), ('stramoseasca', 'stramoseasca'), ('bujorii', 'bujorii'),
       ('vatra', 'vatra'), ('pilates', 'pilates'), ('baby', 'baby')]

try:
    FONT = ImageFont.truetype(str(FOTO.parent / '..' / 'x'), 20)
except Exception:
    FONT = None
def font(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
              '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        if pathlib.Path(p).exists():
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

def placeholder(label, w=900, hh=600):
    im = Image.new('RGB', (w, hh), (0, 16, 66))
    d = ImageDraw.Draw(im)
    for i, col in enumerate([(9, 28, 122), (249, 213, 35), (247, 44, 37)]):
        d.rectangle([0, hh - 24 + i * 8, w, hh - 16 + i * 8], fill=col)
    f = font(22); fs = font(15)
    d.text((28, 26), 'FOTOGRAFIE DE ÎNCĂRCAT', font=fs, fill=(249, 213, 35))
    words, line, lines = label.split(), '', []
    for wd in words:
        t = (line + ' ' + wd).strip()
        if d.textlength(t, font=f) > w - 56: lines.append(line); line = wd
        else: line = t
    lines.append(line)
    for i, ln in enumerate(lines[:6]):
        d.text((28, 70 + i * 32), ln, font=f, fill=(255, 255, 255))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=70)
    return b.getvalue()

def encode(p, maxw=1100):
    im = Image.open(p).convert('RGB')
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=62, optimize=True)
    return b.getvalue()

used_local = used_webp = made = 0
for s in srcs:
    stem = pathlib.Path(s).stem
    alt = ''
    m = re.search(r'src="%s"[^>]*alt="([^"]*)"' % re.escape(s), h)
    if m: alt = m.group(1)
    data = None
    if stem in local:
        data = encode(local[stem]); used_local += 1
    else:
        ns = norm(stem)
        for k, v in KEY:
            if k in ns and v in webps:
                data = encode(webps[v]); used_webp += 1; break
    if data is None:
        data = placeholder(alt or stem.replace('-', ' ')); made += 1
    h = h.replace('"%s"' % s, '"data:image/jpeg;base64,%s"' % base64.b64encode(data).decode())

BANNER = '''<div style="position:sticky;top:0;z-index:99;background:#F9D523;color:#181717;
 font:700 14px/1.4 system-ui,sans-serif;padding:11px 18px;text-align:center;">
 PREVIZUALIZARE LOCALĂ — nu se publică. Fotografiile marcate „FOTOGRAFIE DE ÎNCĂRCAT" sunt
 substitute generate; în pagina reală se încarcă fișierele din Media Library.</div>'''
doc = ('<!doctype html><html lang="ro"><head><meta charset="utf-8">'
       '<meta name="viewport" content="width=device-width,initial-scale=1">'
       '<meta name="robots" content="noindex,nofollow">'
       '<title>Previzualizare · Grupul Vatra Torino Nord v4</title>'
       '<style>body{margin:0;background:#fff;}</style></head><body>' + BANNER + h + '</body></html>')
out = ROOT / 'landing-torino-nord/PREVIZUALIZARE-TORINO-NORD-v4.html'
out.write_text(doc, encoding='utf-8')
print('surse: %d | locale: %d | din plugin: %d | substitute: %d' % (len(srcs), used_local, used_webp, made))
print('previzualizare: %.1f MB' % (out.stat().st_size / 1e6))
