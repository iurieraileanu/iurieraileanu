# Ghid de publicare — landing page Torino Nord v2.0

**APS ASD Primo Passo · Școala de Dansuri Populare Românești „Grupul Vatra"**
15 septembrie 2026 · Statut: **DE APLICAT** · Durată estimată: 45–60 de minute, o singură persoană.

## Ce se livrează

| Fișier | Ce este |
| --- | --- |
| `landing-torino-nord-v2.html` | Pagina completă, de lipit în widgetul HTML din Elementor. Include CSS, JS și schema JSON-LD. |
| `schema-torino-nord-v2.json` | Aceeași schemă, separat, dacă preferi să o pui prin Yoast. |
| `foto-torino-nord/` | **17 fotografii** cu nume optimizate SEO, gata de încărcat. |
| `grafica-sociala/` | Patru grafice: Open Graph, postare Facebook, postare Instagram, Story. |
| `PREVIZUALIZARE-local.html` | Versiunea v1, pentru comparație. |

## Ce s-a schimbat față de v1.0

Galeria celor 250 mp de spații, cu lightbox · modulul de închiriere a sălilor · secțiunea YouTube cu
ambele canale ale școlii și șase playlisturi · trimiteri video în fișele Balet, Dans de caracter și
Dansuri internaționale · palmaresul Ansamblului Vatra și al Grupului Elle · portretele reale ale celor
șase instructori, în locul monogramelor · Pilates cu instructor numit · schema extinsă cu dotarea
sălilor și cele două oferte de serviciu.

---

## Pasul 1 · încarcă fotografiile

Media → Adaugă fișier nou → trage **toate cele 17 fotografii** din `foto-torino-nord`.
**Nu le redenumi** — pagina le caută exact așa.

Completează alt-textul pentru fiecare:

| Fișier | Alt text |
| --- | --- |
| sala-mare-salone-danza-grupul-vatra-torino-nord.jpg | Salone Danza, sala mare de dans a Școlii Grupul Vatra din Torino Nord, cu oglinzi și bare de balet |
| sala-mare-bare-balet-oglinzi-via-gressoney.jpg | Bare de balet și oglinzi în sala mare din Via Gressoney, Torino |
| sala-arte-balet-costume-populare-torino.jpg | Sala Arte a Școlii Grupul Vatra, cu bare de balet și dulapurile cu costume populare |
| sala-multimedia-studio-podcast-grupul-vatra.jpg | Sala Multimedia, studioul de podcast și streaming al Grupului Vatra din Torino |
| departament-media-regie-streaming-torino.jpg | Regia video cu patru camere și transmisiune live din Sala Multimedia a Grupului Vatra |
| secretariat-receptie-grupul-vatra-torino-nord.jpg | Secretariatul și recepția Școlii Grupul Vatra din Via Gressoney, Torino |
| secretariat-vitrina-trofee-costume-torino.jpg | Vitrina cu trofee și păpuși în port popular de la secretariatul Școlii Grupul Vatra |
| intrare-scoala-via-gressoney-29b-torino.jpg | Intrarea în Școala Grupul Vatra din Via Gressoney 29/B, Torino |
| indicator-valori-grupul-vatra-torino-nord.jpg | Indicator de lemn la intrarea în Școala Grupul Vatra, cu valorile școlii scrise pe verticală |
| vestiar-scoala-de-dans-torino-nord.jpg | Vestiarul Școlii Grupul Vatra din Torino Nord, cu bănci și cuiere |
| birou-aps-asd-primo-passo-torino.jpg | Biroul APS ASD Primo Passo din Via Gressoney, Torino |
| dans-de-caracter-grupul-vatra-torino.jpg | Dansatoare în costume de caracter, cu evantaie, pe scena Școlii de Dans și Artă Primo Passo din Torino |
| dansuri-internationale-grupul-elle-torino.jpg | Dansatoarele Grupului Feminin Elle într-un dans internațional, pe scenă, la Torino |
| instructor-iurie-raileanu-grupul-vatra.jpg | Iurie Răileanu, fondatorul și coregraful general al Școlii Grupul Vatra |
| instructor-carmen-georgiana-rotariu-grupul-vatra.jpg | Carmen Georgiana Rotariu, instructoare și dansatoare la Grupul Vatra Torino Nord |
| instructor-cristian-costin-grupul-vatra.jpg | Cristian Costin, dansator și asistent instructor la Grupul Vatra Torino Nord |
| instructor-costel-muntianu-grupul-vatra.jpg | Costel Muntianu, asistent instructor la Ansamblul Strămoșeasca |

**Verificare obligatorie.** Deschide una dintre fotografiile încărcate și uită-te la adresa ei. Dacă
scrie `/wp-content/uploads/2026/09/`, e în regulă. Dacă scrie altă lună, deschide fișierul HTML într-un
editor de text, caută `2026/09` și înlocuiește peste tot cu luna reală.

Fotografiile lui **Gessica Ecaterina Sfabu** și ale **Sofiei Zaynetdinova** sunt deja pe site, în
`2026/08`, și nu trebuie reîncărcate. Restul imaginilor din pagină (hero, cardurile de curs, Vatra
Solidale) sunt tot în biblioteca media, din 2024/11, 2025/08 și 2026/08.

## Pasul 2 · pune pagina în Elementor

1. Pagini → **GrupulvatraTorinoNord** → Editează cu Elementor.
2. Șterge secțiunea goală rămasă din titlul vechi.
3. Adaugă o secțiune nouă, cu o singură coloană.
4. Fila **Layout**: Content Width = **Full Width**, Columns Gap = **No Gap**.
5. Fila **Advanced**: Padding = 0 pe toate laturile, Margin = 0.
6. Trage în coloană widgetul **HTML**.
7. Deschide `landing-torino-nord-v2.html`, selectează tot, copiază și lipește în casetă.
8. **Actualizează**.

Dacă tema adaugă un titlu deasupra: rotița din stânga jos → Page Layout → **Elementor Full Width**,
Hide Title = Da.

Tot CSS-ul este limitat la `#vtn-torino-nord`, deci nu atinge antetul, subsolul sau alte pagini.
Singura resursă din afara site-ului sunt miniaturile de pe `i.ytimg.com`.

## Pasul 3 · verifică pe cele trei ecrane

**Desktop, 1440 px.** Cardurile de curs stau câte trei pe rând, galeria spațiilor la fel. Tabelul
orarului se vede integral.

**Tabletă, 1024 și 768 px.** Cardurile trec la două pe rând, apoi la unu. Caseta de contact coboară
sub text.

**Mobil, 390 px.** Totul pe o coloană. Tabelul orarului se derulează lateral — este intenționat și
scrie asta sub el.

Verificat automat în Chromium la 1440 px și 390 px: fără derulare orizontală, filtrele de orar
funcționale, lightbox-ul se deschide și se închide cu Escape, fără erori JavaScript.

## Pasul 4 · Yoast SEO

| Câmp | Valoare |
| --- | --- |
| Focus keyphrase | dans popular Torino |
| Slug | `grupulvatratorinonord` — **nu îl schimba**, are vechime SEO |
| SEO title | Grupul Vatra Torino Nord – dans popular din 2011 |
| Meta description | Școala Grupul Vatra, sediul principal din Via Gressoney 29/B, Torino: dans popular, balet și modern pentru copii, adolescenți și adulți. Lecție de probă gratuită. |
| Cornerstone content | Activat |
| Facebook image | `grafica-sociala/og-grupul-vatra-torino-nord-1200x630.png` |
| Facebook title | Aici s-a născut Vatra. Din 2011, în Via Gressoney. |
| Facebook description | Sediul principal al Școlii Grupul Vatra, în Via Gressoney 29/B. Cursuri pentru copii, adolescenți și adulți, opt ansambluri și prima lecție de probă gratuită. |
| Advanced | Allow search engines: **Yes** · Follow links: **Yes** |

**Setare globală, o singură dată:** Yoast → Setări → Social → Facebook = `https://www.facebook.com/grupulvatra`.
Acum, pe toate paginile românești, Open Graph indică pagina italiană.

## Pasul 5 · schema JSON-LD

Este deja în pagină, la final. Declară `DanceSchool` + `LocalBusiness`, data de înființare
25 septembrie 2011, fondatorul, asociația-mamă cu codul fiscal, orarul secretariatului, cele opt
localități deservite, catalogul de opt cursuri, dotarea sălilor, cele două canale de YouTube la
`sameAs` și `subjectOf` și cele două oferte de serviciu — închirierea sălilor și producția media.
**Nu conține niciun preț.**

## Pasul 6 · grafica socială

Cele patru fișiere sunt în `grafica-sociala/`. Fiecare are, în colțul din dreapta sus, un
dreptunghi punctat care marchează locul logoului: **logoul se așază din fișier, în varianta albă**,
înainte de publicare — regula de brand cere să nu fie redesenat. Responsabil: Ioan Ungurianu.

Textul este randat cu Helvetica, nu cu Aileron, pentru că fontul nu este instalat în mediul de
generare. Pentru varianta finală de brand, textul se reia cu Aileron.

Programarea postărilor se face prin Postiz.

## Pasul 7 · după publicare

1. Deschide pagina pe telefon și apasă două-trei butoane de WhatsApp: mesajul pre-completat trebuie să apară cu diacritice.
2. **Facebook Sharing Debugger** → lipește adresa → Scrape Again.
3. Trimite-ți linkul pe WhatsApp, ție însuți.
4. **Google Rich Results Test** → trebuie să detecteze DanceSchool și LocalBusiness.
5. **Search Console** → Inspectare URL → Solicită indexarea.
6. Verifică cele 23 de linkuri interne și cele 22 de linkuri către YouTube.
7. Înscrie intrarea în `CALENDAR_MASTER`, cu dată și responsabil.

---

## Ce se corectează în jurul paginii

**P0 — tarife publice.** Pagina `/intrebari-frecvente/` afișează taxa anuală și intervalul lunar, iar
butonul „Scopri i nostri prezzi" de pe primopasso.org duce la un magazin SumUp. Ambele contrazic regula
„tarifele nu se publică online".

**P0 — Cristian Munteanu.** Numele apare pe circa opt pagini de curs și pe pagina *Danze folcloristiche*
de pe primopasso.org. Persoana nu mai face parte din echipă; numele se elimină din toate sursele.
Instructorii reali pentru 2026–2027 sunt cei din orarul acestei pagini.

**P1 — Nichelino** apare încă pe pagina principală, pe „Despre noi" și pe „Contact". Structura este
închisă din 27 august 2026.

**P1 — cifrele.** Pagina principală afișează 1.600 / 530 / 5 milioane. Setul unic este 1.700+ / 560+ / 6 milioane.

**P1 — `/filiale-grupul-vatra/`** este goală și indexată, iar meta-descrierea ei numește o filială închisă.

**P1 — două pagini de curs dau 404** și sunt încă în sitemap: `/cursuri/torino-curs-copii-4-7-ani/` și
`/cursuri/calus-copii-4-7-torino/`. Pagina nu le linkează.

**P2 — pe YouTube**, descrierea videoclipului cu suita din Căluș conține cuvântul „UNESCO", iar clipul de
recrutare din 2024 afișează cifre vechi.

**P2 — dansul modern nu are niciun videoclip** pe niciunul dintre canale, deși este curs nou. Hora
Padului și Bujorii de la Prut nu au playlist propriu. Responsabil: Ioan Ungurianu.

## Ce rămâne de decis

1. **Datele primei lecții** pentru fiecare grupă. Pagina trimite corect pe WhatsApp, dar o dată fermă crește conversia.
2. **Acordurile de imagine** pentru fotografiile cu minori de pe cardurile de copii și adolescenți. Registrul cerut prin DEC-017 nu există. Responsabil: Andreea Mititiuc.
3. **Grupele de căluș pe vârste** — tabelul de abonamente are o singură linie, miercuri 19:30–20:30.
4. **Grafiile Diculescu și Doboș**, folosite în blocul consiliului director.
5. **Ziua și ora pentru grupa de dansuri internaționale** — încă nu sunt în tabelul de abonamente.
6. **Eticheta de pe grafica lui Cristian Costin** spune „asistent instructor · Milano", dar tabelul de abonamente 2026–2027 îl pune la Torino Nord. Pagina folosește rolul din tabel; grafica socială ar trebui refăcută.
7. **Fotografia lui Ioan Ungurianu** apare în Drive și sub numele „Ionut Ungurianu". Grafia corectă este Ioan.

## Decizii aplicate în această versiune

- **Sanremo 2024** — Premiul I este atribuit **Ansamblului Artistic Vatra**, conform fișei ansamblului. La Grupul Elle apare doar participarea la festival, fără revendicarea premiului.
- **Pilates** — instructoare Sofia Zaynetdinova.
- **Miniatura „Ritmuri de Acasă 2026"** conține prețul biletului, deci nu este folosită. Nu se semnalează public.
- **Închirierea sălilor** — condițiile provin de pe primopasso.org, fără niciun cost afișat. Disponibilitatea se discută în privat.
- **Nichelino** a fost scos și din palmaresul Grupului Elle, unde apărea ca oraș-gazdă al unui concurs. Faptul rămâne — concursul și data — fără localitate.
- **Regulamentele** asociației, ale școlii și ale ansamblurilor au fost consultate, dar nu sunt publicate și nu sunt linkate.

---

## Surse

Folderul Drive al filialei (`Torino Nord`): arhitectura și textele aprobate · ghidul de publicare v2.1 ·
auditul site-ului · pachetul SEO Yoast · fișele celor opt ansambluri · catalogul de servicii media ·
documentul de echipă · tabelul de abonamente 2026–2027 (orarul, fără tarife) · certificatul Agenzia
delle Entrate (codul fiscal) · folderele `11. Spații`, `10.Echipă` și `03 Ansambluri și Grupuri`
(fotografiile). Canalele YouTube `@grupulvatra` și `@scuoladidanzaprimopasso` (playlisturile și
palmaresul Grupului Elle). primopasso.org (condițiile de închiriere).

Nu au fost inventate date, cifre, persoane sau evenimente. Orarul provine integral din tabelul de
abonamente. Punctele neconfirmate sunt comentarii HTML în fișier și apar în listele de mai sus, nu în
textul publicat.
