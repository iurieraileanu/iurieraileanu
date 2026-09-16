# -*- coding: utf-8 -*-
"""Set grafic Torino Nord: Open Graph, Facebook, Instagram, Story.
Sigla este așezată din fișierul oficial, pe câmp alb — nu este redesenată."""
import math, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

U = pathlib.Path('/root/.claude/uploads/39032637-2755-53a5-b505-cd2829f9247f')
ASSET = sorted(pathlib.Path('/tmp/claude-0/-home-user-iurieraileanu').glob('*/scratchpad/zipnou/grupul-vatra-torino-nord/assets'))[0]
OUT = pathlib.Path('/home/user/iurieraileanu/landing-torino-nord/grafica-sociala')
OUT.mkdir(parents=True, exist_ok=True)
DEEP, CATALINA, RUBY, LEMON, WHITE = (0,16,66), (9,28,122), (247,44,37), (249,213,35), (255,255,255)
FF = {'heavy': U/'da7d00db-Aileron-Heavy.otf', 'bold': U/'83da97ff-Aileron-Bold.otf', 'reg': U/'00241023-Aileron-Regular.otf'}
font = lambda k, s: ImageFont.truetype(str(FF[k]), s)
LOGO = Image.open(ASSET / 'logo-vatra.png').convert('RGBA')

def band(W, H, y0, amp, span, color, alpha, phase, th):
    pts_t, pts_b = [], []
    for x in range(0, W + 8, 8):
        y = y0 + math.sin(x / W * math.pi * 2 * span + phase) * amp
        pts_t.append((x, y)); pts_b.append((x, y + th))
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(lay).polygon(pts_t + pts_b[::-1], fill=color + (alpha,))
    return lay

def wrap(d, text, f, maxw):
    out, line = [], ''
    for w in text.split():
        t = (line + ' ' + w).strip()
        if d.textlength(t, font=f) > maxw and line: out.append(line); line = w
        else: line = t
    out.append(line); return out

def compose(W, H, name, title_pt, sub_pt, tag_pt, addr_pt):
    im = Image.new('RGBA', (W, H), DEEP + (255,))
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([-W*0.3, -H*0.5, W*0.8, H*0.6], fill=CATALINA + (90,))
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(W*0.06)))

    th = int(min(W, H) * 0.048)
    for y0, phase, cols in [(H*0.03, 0.0, [CATALINA, LEMON, RUBY]),
                            (H*0.865, 2.1, [RUBY, LEMON, CATALINA])]:
        for i, c in enumerate(cols):
            im = Image.alpha_composite(im, band(W, H, y0 + i*th*1.5, H*0.042, 1.05, c, 240, phase + i*0.55, th))

    # voal vertical, ca textul să rămână lizibil peste panglici
    scrim = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for i in range(H):
        t = abs(i - H/2) / (H/2)
        a = int(232 * max(0.0, 1 - t**2.3))
        sd.line([(0, i), (W, i)], fill=DEEP + (a,))
    im = Image.alpha_composite(im, scrim)

    d = ImageDraw.Draw(im)
    # sigla oficială, pe câmp alb
    lw = int(W * 0.34); lh = int(lw * LOGO.height / LOGO.width)
    padx, pady = int(lw * 0.09), int(lh * 0.16)
    plate = Image.new('RGBA', (lw + padx*2, lh + pady*2), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle([0, 0, plate.width-1, plate.height-1],
                                            radius=int(plate.height*0.28), fill=WHITE + (255,))
    plate.alpha_composite(LOGO.resize((lw, lh), Image.LANCZOS), (padx, pady))

    ft, fs, fg, fa = font('heavy', title_pt), font('heavy', sub_pt), font('bold', tag_pt), font('reg', addr_pt)
    maxw = W * 0.86
    l1 = wrap(d, 'Grupul Vatra', ft, maxw); l2 = wrap(d, 'Torino Nord', fs, maxw)
    lines = [(t, ft) for t in l1] + [(t, fs) for t in l2]
    hs = [f.getbbox('Ag')[3] - f.getbbox('Ag')[1] for _, f in lines]
    block = plate.height + H*0.045 + sum(h*1.26 for h in hs) + tag_pt*3.0 + addr_pt*1.6
    y = (H - block) / 2
    im.alpha_composite(plate, (int((W - plate.width)/2), int(y)))
    y += plate.height + H*0.045
    for (t, f), hh in zip(lines, hs):
        d.text((W/2, y), t, font=f, fill=WHITE, anchor='ma'); y += hh*1.26
    y += tag_pt*0.85
    d.text((W/2, y), 'DANS · ARTĂ · COMUNITATE', font=fg, fill=LEMON, anchor='ma')
    y += tag_pt*1.95
    d.text((W/2, y), 'Via Gressoney 29/B · 10155 Torino', font=fa, fill=(196, 209, 240), anchor='ma')

    bar = max(4, int(H*0.011))
    for i, c in enumerate([CATALINA, LEMON, RUBY]):
        d.rectangle([W*i/3, H-bar, W*(i+1)/3, H], fill=c)
    im.convert('RGB').save(OUT / name, quality=94)
    print('  ', name, im.size)

compose(1200, 630,  'og-grupul-vatra-torino-nord-1200x630.png',   96, 70, 25, 24)
compose(1080, 1080, 'post-instagram-torino-nord-1080x1080.png',  104, 76, 27, 25)
compose(1080, 1350, 'post-facebook-torino-nord-1080x1350.png',   108, 78, 28, 26)
compose(1080, 1920, 'story-torino-nord-1080x1920.png',           112, 82, 29, 27)
