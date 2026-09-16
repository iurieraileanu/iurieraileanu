# -*- coding: utf-8 -*-
import re, json, pathlib
B = pathlib.Path('/home/user/iurieraileanu/build')
R = pathlib.Path('/home/user/iurieraileanu/landing-torino-nord')
h = (B / 'stage4.html').read_text(encoding='utf-8')
js = (B / 'app_v4.js').read_text(encoding='utf-8')

# ------------------------------------------------- 1. întrebările → FAQPage --
faq = re.search(r'id="vtn-intrebari".*?</section>', h, flags=re.S).group(0)
qa = re.findall(r'<h3 class="vtn-rv">(.*?)</h3>\s*<p>(.*?)</p>', faq, flags=re.S)
if not qa:
    qa = re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', faq, flags=re.S)
clean = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()
qa = [(clean(q), clean(a)) for q, a in qa]
print('întrebări găsite:', len(qa))

schema = json.loads((R / 'schema-torino-nord-v2.json').read_text(encoding='utf-8'))
schema['@graph'].append({
    '@type': 'FAQPage',
    '@id': 'https://grupulvatra.com/grupulvatratorinonord/#intrebari',
    'mainEntity': [{'@type': 'Question', 'name': q,
                    'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa]
})
raw = json.dumps(schema, ensure_ascii=False, indent=2)
assert '"price' not in raw and '€' not in raw and '"offers"' not in raw, 'preț în schema!'
(R / 'schema-torino-nord-v4.json').write_text(raw + '\n', encoding='utf-8')

# ------------------------------------------------------------- 2. coada ------
TAIL = '''
<!-- ========== ELEMENTE DE INTERFAȚĂ ========== -->
<div class="vtn-progress" aria-hidden="true"><i></i></div>
<button type="button" class="vtn-top" aria-label="Înapoi sus">&#8593;</button>

<figure class="vtn-lb" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Fotografie mărită">
  <button type="button" class="vtn-lb__close" aria-label="Închide fotografia">&times;</button>
  <button type="button" class="vtn-lb__nav vtn-lb__prev" aria-label="Fotografia anterioară">&#8249;</button>
  <button type="button" class="vtn-lb__nav vtn-lb__next" aria-label="Fotografia următoare">&#8250;</button>
  <div style="text-align:center;">
    <img src="" alt="">
    <figcaption></figcaption>
  </div>
</figure>

</div><!-- /.vtn-page -->

<script>
%s
</script>

<!-- Date structurate: școala, sălile, serviciile și întrebările frecvente.
     Nu conțin tarife: prețurile se comunică în privat. -->
<script type="application/ld+json">
%s
</script>
''' % (js, raw)

end = '</div><!-- /.vtn-page -->'
assert h.count(end) == 1
h = h[:h.index(end)] + TAIL
(R / 'landing-torino-nord-v4.html').write_text(h, encoding='utf-8')
print('v4 scris: %.1f KB' % (len(h.encode('utf-8')) / 1024))
