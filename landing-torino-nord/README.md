# Landing page Filiala Torino Nord — grupulvatra.com/grupulvatratorinonord/

**APS ASD Primo Passo · Școala de Dansuri Populare Românești „Grupul Vatra"**
Versiunea 1.0 · 15 septembrie 2026 · Status: **DE APROBAT** — se publică după aprobarea lui Iurie Răileanu.

## Fișiere

| Fișier | Ce conține |
| --- | --- |
| `02_LANDING_TORINO_NORD_ELEMENTOR_v1.0.html` | Pagina completă, gata de lipit în widgetul HTML din Elementor. Include CSS-ul, JS-ul și schema JSON-LD. |
| `schema-torino-nord.json` | Aceeași schemă JSON-LD, separat, pentru cazul în care se pune prin Yoast și nu prin pagină. |

## Ce conține pagina

Opt secțiuni, în ordinea din arhitectura aprobată, plus bara de cifre, navigarea pe ancore și subsolul:

1. **Hero** — sediul principal, din 2011, pe fotografie cu scrim Deep Cove.
2. **Acces și localități limitrofe** — Porcelain. Autobuz, gara Rebaudengo, A4, aeroport, cele 7 localități, caseta de contact.
3. **Cursuri pe segmente** — alb. Opt carduri, fiecare cu ziua, ora, vârsta, instructorul și buton WhatsApp pre-completat.
4. **Orarul complet 2026–2027** — Porcelain. 20 de intervale, cu filtre pe zile.
5. **Ansambluri** — alb. Opt ansambluri cu anul, publicul, o frază și link către pagina de ansamblu.
6. **Echipa** — Porcelain. Șase instructori, secretariatul, consiliul director.
7. **Departamentul Media** — Deep Cove. Serviciile și butonul de colaborare.
8. **Vatra Solidale** — Porcelain. Profiluri căutate, cele șase domenii, formularul de voluntariat.
9. **Apel final la acțiune** — Deep Cove, cu sloganul de închidere și nota legală.

Raportul de culoare respectă regula 70/20/10: patru secțiuni deschise, trei pe Deep Cove plus hero pe
fotografie, roșu numai pe butoanele de acțiune și pe eyebrow, galben pe eticheta „Nou din 2026–2027" și
pe slogan. Namu apare **o singură dată**, pe sloganul de închidere.

## Ce NU conține, intenționat

Tarife · simbolul euro · date de start (peste tot scrie „Scrie-ne pe WhatsApp", conform DEC-012) ·
date din stagiunea 2025–2026 · emoji · hashtaguri · „UNESCO" · „imigranți" · „călătorie" · „Nichelino" ·
al doilea număr de telefon · adresa `vatratorino@gmail.com` · formularele Google de curs ·
blocul aniversar de 15 ani · niciun marcaj `[DE CONFIRMAT]` la vedere.

## Cum se pune în Elementor

1. Editează pagina Torino Nord (`/grupulvatratorinonord/`) în Elementor.
2. Adaugă o secțiune nouă, pe toată lățimea: **Layout → Content Width: Full Width**, **Columns Gap: No Gap**, padding lateral 0.
3. Trage în ea widgetul **HTML** și lipește tot conținutul fișierului `02_LANDING_TORINO_NORD_ELEMENTOR_v1.0.html`, de la primul comentariu până la ultima linie.
4. Publică și verifică pe telefon: pagina se rearanjează singură sub 980 px și sub 700 px.

**Note tehnice.** Tot CSS-ul este limitat la `#vtn-torino-nord`, deci nu atinge restul temei. Nu se încarcă
niciun script și nicio resursă externă, în afara imaginilor care sunt deja în biblioteca media. Fonturile
Aileron și Namu se preiau din `/wp-content/uploads/fonturi/`; dacă lipsesc, pagina cade elegant pe
Helvetica/Arial. JS-ul rulează într-un IIFE și este pur *progressive enhancement*: dacă este blocat,
pagina rămâne complet lizibilă.

## Imaginile folosite

Toate sunt deja în biblioteca media a site-ului; nu trebuie încărcat nimic ca pagina să funcționeze.

| Loc | Fișier |
| --- | --- |
| Hero | `2025/08/Ansamblul-Vatra-pe-scena-la-Pala-Alpitour-Torino.jpg` |
| Logo alb | `2026/08/logo-grupul-vatra-alb.png` |
| Card copii | `2024/11/copii-dans-folclor-8-12-vatra.jpg` |
| Card adolescenți | `2025/08/Ansamblul-Folcloric-Hora-Padului.webp` |
| Card adulți | `2024/11/hora-mare-cursuri-dans-adulti-torino-scaled-e1755805708939.jpg` |
| Card balet | `2026/08/sofia-zaynetdinova-coregrafa-balet-grupul-vatra__varianta-A.jpg` |
| Card baby dance | `2024/11/cursuri-traditii-dansuri-populare-copii.jpg` |
| Card internaționale | `2025/08/tarantella-festival-vatra-dornei-ansamblul-vatra.jpg` |
| Card Călușari | `2025/08/Ceata-de-Calusari-din-Torino.jpg` |
| Portret Gessica | `2026/08/gessica-ecaterina-sfabu-instructoare-torino-nord__varianta-A.jpg` |
| Portret Sofia | `2026/08/sofia-zaynetdinova-coregrafa-balet-grupul-vatra__varianta-A.jpg` |
| Vatra Solidale | `2026/08/vatra-solidale-open-graph-1200x630-1.png` |

**Portretele care lipsesc.** Arhiva are portrete de studio doar pentru Gessica și Sofia. Iurie Răileanu,
Carmen Georgiana Rotariu, Cristian Costin și Costel Muntianu apar cu monograma de brand, nu cu o
fotografie de grup — regula DEC-009. Se înlocuiesc cu portretul real imediat ce există (responsabil: Ioan Ungurianu).

**Grupul Elle** nu are încă o fotografie proprie în biblioteca media; cardul lui folosește un panou de brand.

## SEO — de completat în Yoast

| Câmp | Valoare |
| --- | --- |
| Slug | `grupulvatratorinonord` (rămâne neschimbat, pentru vechimea SEO) |
| Focus Keyphrase | dans popular Torino |
| Meta Title | Grupul Vatra Torino Nord – dans popular din 2011 |
| Meta Description | Școala Grupul Vatra, sediul principal din Via Gressoney 29/B, Torino: dans popular, balet și modern pentru copii, adolescenți și adulți. Lecție de probă gratuită. |
| Open Graph title | Aici s-a născut Vatra. Din 2011, în Via Gressoney. |
| Open Graph description | Sediul principal al Școlii Grupul Vatra, în Via Gressoney 29/B. Cursuri pentru copii, adolescenți și adulți, opt ansambluri și prima lecție de probă gratuită. |
| Open Graph image | de generat, 1200×630, pe modelul `og-dansuri-populare-torino-sud-1200x630-1.jpg` |
| Robots | `index, follow` — se scoate setarea `noindex` propusă prin DEC-018, pentru că pagina nu mai este goală |
| Cornerstone content | da |

Cuvinte-cheie secundare de folosit în text și în alt-uri: *cursuri de dans popular pentru copii Torino* ·
*școala de dansuri populare românești Torino* · *Grupul Vatra Torino Nord* · *balet Torino nord*.

Schema JSON-LD este deja în pagină. Declară `DanceSchool` + `LocalBusiness`, data de înființare
25 septembrie 2011, fondatorul, asociația-mamă cu codul fiscal `97814410011`, cele opt localități deservite
și catalogul de opt cursuri. Nu conține niciun preț și niciun câmp `offers`.

## Legături interne incluse

23 de linkuri interne verificate față de audit și de pachetul SEO: nouă pagini de curs, opt pagini de
ansamblu, cele șase articole ale instructorilor, harta, formularul de voluntariat și `primopasso.org`.
Plus 16 butoane WhatsApp cu text pre-completat care numește cursul (DEC-010).

**Nu au fost linkate**, pentru că răspund cu eroare 404: `/cursuri/torino-curs-copii-4-7-ani/` și
`/cursuri/calus-copii-4-7-torino/`. Ambele figurează încă în sitemap și pe pagina Cursuri noi —
de reparat sau de scos din sitemap.

## Verificări făcute înainte de livrare

Rulate automat pe fișier și în Chromium, la 1440 px și la 390 px:

- Fără tarife, fără simbolul euro, fără cuvintele interzise, fără emoji, fără marcaje la vedere.
- Diacritice complete. Un singur număr de telefon și o singură adresă de e-mail.
- Un singur set de cifre: 1.700+ elevi, 560+ spectacole, 6 milioane de vizualizări.
- Toate cele 12 imagini au `alt`. Etichetele HTML sunt echilibrate. JSON-LD validat, fără `offers` și fără preț.
- Fără scroll orizontal la 1440 px și la 390 px. Filtrele de orar testate: „Miercuri" → 6 rânduri, „Toate" → 20.
- Contrastul titlurilor și al butoanelor pe fundal închis verificat în browser.

## Ce rămâne de decis înainte de publicare

1. **Data primei lecții** pentru fiecare grupă. Până atunci pagina trimite corect pe WhatsApp, dar conversia crește semnificativ cu o dată fermă pe fiecare card.
2. **Instructorul de la Pilates** — tabelul de abonamente nu îl numește; în orar apare „Scrie-ne pe WhatsApp".
3. **Ziua și ora pentru grupa de dansuri populare internaționale** — nu sunt încă în tabelul de abonamente.
4. **Anul înființării Ansamblului Mugurel** (2021) — până la confirmare, coloana afișează „Nivel avansat", nu anul.
5. **Orarul secretariatului** din schema JSON-LD: luni–vineri 14:00–21:00 și sâmbătă 10:00–18:00. Dacă se schimbă, se schimbă în două locuri: schema și Google Business Profile.
6. **Acordurile de imagine** pentru fotografiile cu minori din cardurile copii și adolescenți (registrul cerut prin DEC-017 nu există încă — responsabil: Andreea Mititiuc).
7. **Grafiile Diculescu și Doboș**, folosite în blocul consiliului director.
8. **Adresa articolului Vatra Solidale** — linkul „Citește despre program" se adaugă după confirmare; deocamdată secțiunea trimite direct la formular.
9. **Imaginea Open Graph** de 1200×630 pentru pagină.

## După publicare

Se scoate setarea `noindex` de pe pagină, se cere indexarea în Google Search Console, se verifică schema
în testul de rezultate îmbogățite și se actualizează pagina `/filiale-grupul-vatra/`, care este tot goală
și trimite către această pagină. Intrarea se înscrie în `CALENDAR_MASTER`, cu dată, canal și responsabil.

## Surse

Toate datele provin din folderul Drive al filialei (`Torino Nord`) și din documentele aprobate:
`06_LANDING_PAGE_TORINO_NORD_ARHITECTURA_SI_TEXTE_v1.0` (arhitectura și textele) ·
`02_LANDING_TORINO_NORD_IMPLEMENTARE_v1.0` (imagini, SEO, verificări) ·
`06_AUDIT_SITE_TORINO_NORD_v1.0` (slug-urile verificate live) ·
`06_SEO_YOAST_TORINO_NORD_v1.0` (meta și schema) ·
`06_ECHIPA_OAMENII_DIN_SPATELE_VATREI_v1.0` (consiliul și articolele instructorilor) ·
`Abbonamenti Scuola di Danza e Arte Primo Passo staggione 2026 - 2027.xlsx` (orarul, fără tarife) ·
`Codice fiscale Primo Passo ASD APS.PDF` (codul fiscal din schema JSON-LD).

Nu au fost inventate date, cifre, persoane sau evenimente. Orarul provine integral din tabelul de
abonamente din Drive. Punctele care nu au putut fi verificate sunt comentarii HTML în fișier și apar
în lista de mai sus, nu în textul publicat.
