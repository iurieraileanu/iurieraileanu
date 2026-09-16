# -*- coding: utf-8 -*-
import pathlib
B = pathlib.Path('/home/user/iurieraileanu/build')
h = (B / 'stage2.html').read_text(encoding='utf-8')

OCT = 'Prima săptămână din octombrie'
ROWS = [
 ('luni','Luni','17:00–18:00','Propedeutică · balet și dans modern','7–10 ani','Sofia Zaynetdinova',OCT),
 ('luni','Luni','17:30–19:00','Dans popular · copii','4–11 ani','Gessica Ecaterina Sfabu','5 octombrie'),
 ('luni','Luni','18:00–20:30','Balet, dans de caracter și modern','15 ani +','Sofia Zaynetdinova',OCT),
 ('luni','Luni','19:00–20:30','Dans popular · adolescenți și Hora Padului','14–25 ani','Gessica Ecaterina Sfabu','4 septembrie'),
 ('luni','Luni','20:30–22:00','Dansuri internaționale · Grupul Elle, începători','Tineri și adulți','Sofia Zaynetdinova',OCT),
 ('luni','Luni','20:30–22:30','Dans popular · adulți','Adulți','Cristian Costin','5 octombrie'),
 ('marti','Marți','17:00–18:00','Baby dance','4–6 ani','Sofia Zaynetdinova',OCT),
 ('marti','Marți','18:00–19:00','Balet și dans modern','11–14 ani','Sofia Zaynetdinova',OCT),
 ('marti','Marți','19:00–20:00','Pilates','Adolescenți și adulți','Sofia Zaynetdinova',OCT),
 ('marti','Marți','20:00–21:00','Balet · adulți','Adulți','Sofia Zaynetdinova',OCT),
 ('miercuri','Miercuri','17:00–18:00','Teatru-dans pentru copii','4–11 ani','Sofia Zaynetdinova',OCT),
 ('miercuri','Miercuri','18:00–19:30','Ansamblul Mugurel · caracter și dansuri internaționale','Copii și adolescenți','Sofia Zaynetdinova','4 septembrie'),
 ('miercuri','Miercuri','19:30–20:30','Joc bărbătesc · Mugurel și Ceata de Călușari','Copii și adolescenți','Cristian Costin','4 septembrie'),
 ('miercuri','Miercuri','19:30–20:30','Joc femeiesc · Mugurel, Vatra și Grupul Elle','Copii și adolescenți','Sofia Zaynetdinova','4 septembrie'),
 ('miercuri','Miercuri','20:30–22:30','Ansamblul Artistic Vatra','Adolescenți și adulți','Iurie Răileanu, cu Cristian Costin și Carmen Georgiana Rotariu','4 septembrie'),
 ('miercuri','Miercuri','20:45–22:45','Ansamblul Strămoșeasca','Adulți','Iurie Răileanu, asistent Costel Muntianu','4 septembrie'),
 ('joi','Joi','17:00–18:00','Baby dance','4–6 ani','Sofia Zaynetdinova',OCT),
 ('joi','Joi','17:30–19:00','Ansamblul Bujorii de la Prut','7–13 ani','Gessica Ecaterina Sfabu','4 septembrie'),
 ('joi','Joi','18:00–19:00','Balet și dans modern','11–14 ani','Sofia Zaynetdinova',OCT),
 ('joi','Joi','19:00–20:00','Pilates','Adolescenți și adulți','Sofia Zaynetdinova',OCT),
 ('joi','Joi','19:00–20:30','Dans popular · adolescenți și Hora Padului','14–25 ani','Gessica Ecaterina Sfabu','4 septembrie'),
 ('joi','Joi','20:00–21:00','Balet · adulți','Adulți','Sofia Zaynetdinova',OCT),
 ('joi','Joi','20:30–22:30','Ansamblul Veselia','Tineri și adulți','Gessica Ecaterina Sfabu','4 septembrie'),
 ('vineri','Vineri','17:00–18:00','Propedeutică · balet și dans modern','7–10 ani','Sofia Zaynetdinova',OCT),
 ('vineri','Vineri','18:00–20:30','Balet, dans de caracter și modern','15 ani +','Sofia Zaynetdinova',OCT),
 ('vineri','Vineri','18:00–20:30','Ansamblul Mugurel · dansuri românești și moldovenești','Copii și adolescenți','Carmen Georgiana Rotariu','4 septembrie'),
 ('vineri','Vineri','20:30–22:30','Ansamblul Artistic Vatra','Adolescenți și adulți','Iurie Răileanu, cu Cristian Costin și Carmen Georgiana Rotariu','4 septembrie'),
 ('sambata','Sâmbătă','17:00–19:00','Dans popular · adulți','Adulți','Gessica Ecaterina Sfabu','5 septembrie'),
]
DAYS = [('luni','Luni'),('marti','Marți'),('miercuri','Miercuri'),('joi','Joi'),('vineri','Vineri'),('sambata','Sâmbătă')]

body, last = [], None
for key, day, hh, grp, age, instr, start in ROWS:
    if key != last:
        body.append('          <tr class="vtn-row-head" data-vtn-head="%s"><td colspan="6">%s</td></tr>' % (key, day))
        last = key
    cls = ' vtn-start--soon' if start == OCT else ''
    body.append('          <tr data-vtn-day="%s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>'
                '<td class="vtn-start%s">%s</td></tr>' % (key, day, hh, grp, age, instr, cls, start))

filters = '\n'.join(
    '        <button type="button" class="vtn-filter" data-vtn-for="%s" aria-pressed="false">%s</button>' % (k, d)
    for k, d in DAYS)

ORAR = '''<!-- ========== ORAR COMPLET ========== -->
    <div id="vtn-orar" class="vtn-orar-block" style="margin-top:56px;padding-top:44px;border-top:1px solid var(--line);">
      <span class="vtn-eyebrow">Orarul sălii din Via Gressoney</span>
      <h2 class="vtn-rv">Toate grupele, zi cu zi</h2>
      <p class="vtn-lead vtn-rv">Grila completă a stagiunii 2026–2027, cu data primei lecții pentru fiecare grupă.
        Ansamblurile și grupele deja formate au început pe 4 septembrie; grupele noi pornesc în octombrie.
        <b>Înscrierile sunt deschise tot anul</b>, iar cine vine mai târziu este preluat și adus din urmă.</p>

      <div class="vtn-filters vtn-rv" data-vtn-dayfilters role="group" aria-label="Filtrează orarul după zi">
        <button type="button" class="vtn-filter vtn-on" data-vtn-for="all" aria-pressed="true">Toate zilele</button>
%s
      </div>
      <p class="vtn-count" data-vtn-daycount aria-live="polite">28 de grupe afișate.</p>

      <div class="vtn-tablewrap vtn-rv">
        <table class="vtn-table">
          <caption>Orarul stagiunii 2026–2027 · Via Gressoney 29/B, Torino</caption>
          <thead><tr>
            <th scope="col">Zi</th><th scope="col">Ora</th><th scope="col">Grupă</th>
            <th scope="col">Vârstă</th><th scope="col">Instructor</th><th scope="col">Prima lecție</th>
          </tr></thead>
          <tbody>
%s
          </tbody>
        </table>
      </div>
    </div>''' % (filters, '\n'.join(body))

i = h.index('<!-- ORAR -->')
j = h.index('</table>', i)
j = h.index('</div>', j) + len('</div>')
h = h[:i] + ORAR + h[j:]
(B / 'stage3.html').write_text(h, encoding='utf-8')
print('etapa 3 OK — %d rânduri de orar' % len(ROWS))
