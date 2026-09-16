# -*- coding: utf-8 -*-
"""Asamblează landing-torino-nord-v4.html din baza v3 + modulele v4."""
import re, io, json, pathlib

B = pathlib.Path('/home/user/iurieraileanu/build')
h = (B / 'base-v3.html').read_text(encoding='utf-8')
css_extra = (B / 'css_extra.css').read_text(encoding='utf-8')
js = (B / 'app_v4.js').read_text(encoding='utf-8')
UP = 'https://grupulvatra.com/wp-content/uploads/2026/09/'

def once(old, new, label):
    global h
    if h.count(old) != 1:
        raise SystemExit('PATCH %s: %d potriviri' % (label, h.count(old)))
    h = h.replace(old, new, 1)

# ---------------------------------------------------------------- 1. antet ---
h = h.replace('LANDING PAGE v3.0', 'LANDING PAGE v4.0 — versiune finală, consolidată')
once('  15 septembrie 2026\n',
     '  16 septembrie 2026\n'
     '  Consolidează v1, v2 și v3 într-un singur fișier: conținutul complet al v3,\n'
     '  interacțiunile v2 (navigație lipicioasă, filtre, galerie cu lupă, date\n'
     '  structurate) și un modul nou de grafică și efecte. Fără informații dublate.\n',
     'data')

# -------------------------------------------------------- 2. CSS suplimentar -
once('</style>', css_extra + '</style>', 'css')

# ------------------------------------------------------------------ 3. hero --
once('<p class="vtn-credit">Fotografie: Grupul Vatra Torino</p>\n  </div>\n</header>',
     '<p class="vtn-credit">Fotografie: Grupul Vatra Torino</p>\n'
     '  </div>\n'
     '  <div class="vtn-hero-wave" aria-hidden="true">\n'
     '    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" preserveAspectRatio="none">\n'
     '      <path d="M0 74 C 190 18, 370 112, 560 66 C 750 20, 930 104, 1120 60 C 1260 28, 1350 52, 1440 40 L1440 120 L0 120 Z" fill="%23091C7A" opacity=".55"/>\n'
     '      <path d="M0 92 C 200 44, 380 126, 580 84 C 780 42, 950 118, 1140 80 C 1280 52, 1360 70, 1440 62 L1440 120 L0 120 Z" fill="%23F9D523" opacity=".5"/>\n'
     '      <path d="M0 104 C 210 66, 400 134, 600 100 C 800 66, 980 130, 1180 98 C 1300 78, 1370 88, 1440 84 L1440 120 L0 120 Z" fill="%23F72C25" opacity=".55"/>\n'
     '      <path d="M0 116 C 240 88, 430 140, 640 114 C 860 88, 1020 142, 1220 114 C 1330 98, 1380 104, 1440 100 L1440 120 L0 120 Z" fill="%23FFFFFF"/>\n'
     '    </svg>\n'
     '  </div>\n'
     '</header>', 'hero-wave')
h = h.replace('fill="%23', 'fill="#')

for old, num, suf in [('<b>1.700+</b>', '1700', '+'),
                      ('<b>560+</b>', '560', '+'),
                      ('<b>8</b>', '8', '')]:
    once(old, old.replace('<b>', '<b data-vtn-count="%s" data-vtn-suffix="%s">' % (num, suf)), 'count' + num)

# ------------------------------------------------------------- 4. navigație --
NAV = '''
<!-- ========== NAVIGAȚIA PAGINII (lipicioasă) ========== -->
<nav class="vtn-nav" aria-label="Secțiunile paginii">
  <div class="vtn-nav__in">
    <a href="#vtn-acces">Cum ajungi</a>
    <a href="#vtn-valori">Valori</a>
    <a href="#vtn-cursuri">Cursuri</a>
    <a href="#vtn-orar">Orar</a>
    <a href="#vtn-spatii">Săli</a>
    <a href="#vtn-inchiriere">Închiriere</a>
    <a href="#vtn-ansambluri">Ansambluri</a>
    <a href="#vtn-repertoriu">Repertoriu</a>
    <a href="#vtn-echipa">Echipa</a>
    <a href="#vtn-media">Media</a>
    <a href="#vtn-intrebari">Întrebări</a>
    <a href="#vtn-inscrieri">Înscriere</a>
  </div>
</nav>
'''
once('\n\n<!-- ========== 2 · ACCES ========== -->', NAV + '\n<!-- ========== 2 · ACCES ========== -->', 'nav')

(B / 'stage1.html').write_text(h, encoding='utf-8')
print('etapa 1 OK — %d octeți' % len(h.encode('utf-8')))
