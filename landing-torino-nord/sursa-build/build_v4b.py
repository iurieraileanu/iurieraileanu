# -*- coding: utf-8 -*-
import re, pathlib
B = pathlib.Path('/home/user/iurieraileanu/build')
h = (B / 'stage1.html').read_text(encoding='utf-8')

AUD = ['copii', 'adolescenti', 'adulti', 'copii adolescenti adulti', 'copii adolescenti',
       'copii', 'adolescenti adulti', 'adolescenti adulti', 'adolescenti adulti', 'copii']
FIRST = ['5 octombrie · grupă nouă',
         '4 septembrie',
         'Luni: 5 octombrie · Sâmbătă: 5 septembrie',
         'Prima săptămână din octombrie',
         'Prima săptămână din octombrie',
         'Prima săptămână din octombrie',
         'Începători: prima săptămână din octombrie · Avansați: 4 septembrie',
         '4 septembrie',
         'Prima săptămână din octombrie',
         '4 septembrie']

arts = re.findall(r'<article class="vtn-course">.*?</article>', h, flags=re.S)
assert len(arts) == 10, len(arts)

for i, a in enumerate(arts):
    n = a
    # public-țintă pentru filtre + clasa de apariție
    n = n.replace('<article class="vtn-course">',
                  '<article class="vtn-course vtn-rv" data-vtn-audience="%s">' % AUD[i], 1)
    row = '<li><b>Prima lecție</b><span>%s</span></li>' % FIRST[i]
    if '<b>Prima lecție</b>' in n:
        n = re.sub(r'<li><b>Prima lecție</b><span>.*?</span></li>', row, n, count=1, flags=re.S)
    else:
        n = n.replace('</ul>\n          <div class="vtn-detail">',
                      '  ' + row + '\n          </ul>\n          <div class="vtn-detail">', 1)
        if row not in n:  # carduri fără bloc .vtn-detail
            n = re.sub(r'(</ul>)', '  ' + row + '\n          </ul>', n, count=1)
    h = h.replace(a, n, 1)

# corectură: călușul are o singură grupă
h = h.replace('<li><b>Alte grupe</b><span>Scrie-ne pe WhatsApp</span></li>',
              '<li><b>Grupe</b><span>O singură grupă în stagiunea 2026–2027</span></li>')

# ---- bara de filtre pentru cursuri ------------------------------------------
FILTERS = '''
    <div class="vtn-filters vtn-rv" data-vtn-coursefilters role="group" aria-label="Filtrează cursurile după vârstă">
      <button type="button" class="vtn-filter vtn-on" data-vtn-for="toate" aria-pressed="true">Toate cursurile</button>
      <button type="button" class="vtn-filter" data-vtn-for="copii" aria-pressed="false">Copii</button>
      <button type="button" class="vtn-filter" data-vtn-for="adolescenti" aria-pressed="false">Adolescenți</button>
      <button type="button" class="vtn-filter" data-vtn-for="adulti" aria-pressed="false">Adulți</button>
    </div>
    <p class="vtn-count" data-vtn-coursecount aria-live="polite">10 cursuri afișate.</p>
'''
old = '\n    <div class="vtn-grid vtn-grid--3" style="margin-top:34px;">\n\n      <!-- copii -->'
assert h.count(old) == 1
h = h.replace(old, FILTERS + '\n    <div class="vtn-grid vtn-grid--3" style="margin-top:28px;">\n\n      <!-- copii -->', 1)

(B / 'stage2.html').write_text(h, encoding='utf-8')
print('etapa 2 OK — carduri patch-uite:', len(arts))
