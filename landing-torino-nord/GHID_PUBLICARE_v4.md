# Ghid de publicare — Grupul Vatra · Torino Nord (v4.0)

**Fișierul de publicat:** `landing-torino-nord/landing-torino-nord-v4.html`
**Adresa finală:** `https://grupulvatra.com/grupulvatratorinonord/`
**Data:** 16 septembrie 2026

---

## 1. Ce este versiunea 4.0

Este o singură pagină, care înlocuiește toate variantele anterioare. Conține:

| Sursă | Ce s-a păstrat |
|---|---|
| v3.0 | întregul conținut: 10 cursuri detaliate, 8 ansambluri cu palmares, repertoriul pe zone etnografice, cuvintele maeștrilor, participările, echipa, media, voluntariatul, 10 întrebări frecvente |
| v2.0 | navigația lipicioasă, orarul filtrabil cu data primei lecții, galeria cu lupă, datele structurate |
| v1.0 | structura de secțiuni și tonul textelor |
| nou în v4 | modulul de grafică și efecte, filtrarea cursurilor pe vârste, bara de progres, butonul „sus", datele FAQ pentru Google, corecturile de contrast |

**Nu există informații dublate.** Am verificat automat tot textul: singura frază care se repetă
este numele echipei de instructori ai Ansamblului Vatra, în două carduri diferite, unde repetarea
este corectă.

## 2. Ce lipsea și s-a completat

| Lipsea | S-a adăugat |
|---|---|
| data primei lecții, la 6 din cele 10 cursuri | dată confirmată pentru fiecare curs: 4 septembrie pentru grupele formate, 5 octombrie pentru grupele noi, prima săptămână din octombrie pentru cursurile Sofiei |
| „Prima lecție: scrie-ne pe WhatsApp" la celelalte 4 cursuri | datele reale, în locul trimiterii la WhatsApp |
| coloana „Prima lecție" în orar | adăugată; orarul are acum 28 de grupe, fiecare cu data de început |
| numărul de grupe la Căluș | „o singură grupă în stagiunea 2026–2027", cum ai confirmat |
| navigație în pagină | bară lipicioasă cu 12 secțiuni, care marchează secțiunea curentă |
| filtrare | cursurile se filtrează pe copii / adolescenți / adulți, orarul pe zile |
| date structurate | școala, adresa, sălile, serviciile și cele 10 întrebări frecvente, pentru Google |

## 3. Ce s-a reparat

Trei defecte reale, moștenite din v3, care s-ar fi văzut în pagina publicată:

1. **Butonul „Vezi cursurile" din hero** se colora albastru-închis pe fundal bleumarin — practic invizibil.
2. **Butonul „Cere disponibilitatea"** din secțiunea de închiriere se colora galben pe fundal alb.
3. **Sloganul final** pierdea galbenul și devenea gri-albastru.

Cauza era aceeași la toate trei: în v3, regulile generale pentru legături aveau prioritate
în cascadă față de clasele butoanelor. Corectura este explicată în comentariile din fișier și
nu folosește `!important`.

De asemenea: coloana orelor nu se mai rupe pe două rânduri, titlul final nu mai lasă „e."
singur pe un rând, iar orașul pe care nu-l publicăm a fost scos din toate cele patru locuri
în care apărea, păstrând concursul și data.

## 4. Modulul de grafică și efecte

| Element | Cum arată |
|---|---|
| Valul tricolor | desen SVG în partea de jos a hero-ului, în patru straturi — albastru, galben, roșu, alb |
| Panglica tricoloră | linie de 7 px care separă secțiunile pe fond închis |
| Textura de altiță | motiv de broderie, foarte discret, pe fundalurile porțelan |
| Apariție la derulare | textele și cardurile urcă 18 px și se dezvăluie; conținutul este vizibil și fără JavaScript |
| Cifrele din hero | se numără de la zero când ajung în ecran, cu separatorul de mii românesc |
| Carduri | se ridică 4 px la trecerea cursorului, iar fotografia se apropie cu 4,5% |
| Bara de progres | fir de 3 px sus, de la roșu la galben |
| Galeria | lupă pe fiecare fotografie, navigare cu săgeți și închidere cu Esc |
| Butonul „sus" | apare după 700 px de derulare |
| Mișcare redusă | cine are „reduce motion" activat în sistem primește pagina fără animații |
| Tipărire | navigația, filtrele și butoanele dispar; fondurile închise devin albe |

## 5. Publicarea în Elementor

1. Încarcă în **Media Library** cele **54 de fotografii** din tabelul de la punctul 8.
   Dacă le încarci în altă lună decât septembrie 2026, înlocuiește în tot fișierul
   `/wp-content/uploads/2026/09/` cu luna corectă.
2. Deschide pagina `/grupulvatratorinonord/` în **Elementor**. Nu crea o pagină nouă —
   păstrezi adresa existentă.
3. Șterge conținutul vechi al paginii.
4. Adaugă un **container pe toată lățimea**, cu spațierile exterioare la zero.
5. În container, pune un singur widget **HTML**.
6. Copiază **tot** conținutul fișierului `landing-torino-nord-v4.html` în widget.
7. Din setările paginii, alege șablonul **Elementor Full Width** sau **Canvas**, ca antetul
   temei să nu dubleze titlul.
8. Salvează ca ciornă, verifică, apoi publică.

> Alternativa cu plugin: pachetul `instaleaza-grupul-vatra-torino-nord.zip` instalează o
> variantă mai veche a paginii, cu 21 de fotografii locale. Versiunea 4.0 folosește 54 de
> fotografii și nu a fost împachetată în plugin, ca să nu existe două pagini diferite în
> circulație. Dacă vrei varianta cu plugin, îmi spui și reconstruiesc pachetul.

## 6. Yoast SEO

| Câmp | Valoare |
|---|---|
| Expresie cheie principală | Grupul Vatra Torino Nord |
| Slug | `grupulvatratorinonord` |
| Titlu SEO | Grupul Vatra Torino Nord — dansuri populare, balet și artă |
| Meta-descriere | Sediul principal al Școlii Grupul Vatra, Via Gressoney 29/B, Torino. Dans popular, balet, dans de caracter și Pilates pentru copii, adolescenți și adulți. Prima lecție de probă este gratuită. |
| URL canonic | `https://grupulvatra.com/grupulvatratorinonord/` |
| Titlu social | Grupul Vatra · Torino Nord |
| Descriere socială | Dans. Artă. Comunitate. Cursuri pentru copii, adolescenți și adulți, în Via Gressoney 29/B, Torino. |
| Imagine socială | `og-grupul-vatra-torino-nord-1200x630.png` |

Pagina conține deja date structurate. Dacă Yoast generează propriul bloc `LocalBusiness`,
lasă-le pe amândouă: `@id`-urile sunt diferite și nu intră în conflict.

## 7. Grafica socială

| Fișier | Dimensiune | Unde se folosește |
|---|---|---|
| `og-grupul-vatra-torino-nord-1200x630.png` | 1200 × 630 | previzualizarea linkului pe Facebook și WhatsApp |
| `post-facebook-torino-nord-1080x1350.png` | 1080 × 1350 | postare pe Facebook |
| `post-instagram-torino-nord-1080x1080.png` | 1080 × 1080 | postare pe Instagram |
| `story-torino-nord-1080x1920.png` | 1080 × 1920 | Story pe Instagram și Facebook |

Sigla este așezată din fișierul oficial, pe câmp alb — nu este redesenată. Tipografia este
Aileron Heavy și Aileron Regular, din fișierele pe care mi le-ai trimis.

## 8. Fotografiile de încărcat, cu textul alternativ

| Fișier | Text alternativ |
|---|---|
| `logo-grupul-vatra-alb.png` | Grupul Vatra — Școala de Dansuri Populare Românești |
| `valori-grupul-vatra-intrare-via-gressoney.jpg` | Indicatorul cu valorile Școlii Grupul Vatra, la intrarea din Via Gressoney 29/B, Torino |
| `copii-dans-folclor-8-12-vatra.jpg` | Copii la cursul de dans popular al Școlii Grupul Vatra din Torino |
| `Ansamblul-Folcloric-Hora-Padului.webp` | Adolescenți din Ansamblul Folcloric Hora Padului, Grupul Vatra Torino |
| `curs-dans-popular-adulti-incepatori-torino.jpg` | Șase adulți în costum popular, ținându-se de mână la cursul de dans popular din Torino |
| `balet-adulti-danza-classica-torino-nord.jpg` | Cursantă adultă la balet, pe scena Școlii de Dans și Artă Primo Passo din Torino |
| `lectie-balet-adulti-bara-via-gressoney.jpg` | Grupa de adulți la bara de balet, în sala Școlii Grupul Vatra din Via Gressoney |
| `dans-de-caracter-adolescenti-torino-nord.jpg` | Adolescente în costume de caracter, pe scenă, la Școala Grupul Vatra din Torino |
| `cursuri-traditii-dansuri-populare-copii.jpg` | Cei mai mici copii ai Școlii Grupul Vatra, la curs în Torino |
| `dansuri-internationale-grupul-vatra-torino.jpg` | Dansatoare cu evantaie într-un dans internațional, Școala Grupul Vatra Torino |
| `grupul-elle-dans-irlandez-torino-nord.jpg` | Grupul Feminin Elle în costume de dans irlandez, pe scenă la Torino |
| `grupa-barbati-dans-popular-adulti-torino.jpg` | Grupa de bărbați a Școlii Grupul Vatra, în costum popular, pe scena spectacolului Ritmuri de Acasă |
| `calusar-portret-studio-grupul-vatra.jpg` | Călușar din Ceata de Călușari a Școlii Grupul Vatra, în costum complet, portret de studio |
| `sala-arte-balet-grupul-vatra-torino.jpg` | Sala Arte a Școlii Grupul Vatra, cu parchet, oglinzi și bară de balet |
| `ANSAMBLUL-BUJORII-DE-LA-PRUT.webp` | Ansamblul folcloric de copii Bujorii de la Prut, Grupul Vatra Torino |
| `sala-mare-salone-danza-grupul-vatra-torino-nord.jpg` | Salone Danza, sala mare de 100 mp a Școlii Grupul Vatra din Torino Nord |
| `sala-mare-bare-balet-oglinzi-via-gressoney.jpg` | Bare de balet și oglinzi în sala mare din Via Gressoney, Torino |
| `sala-multimedia-studio-podcast-grupul-vatra.jpg` | Sala Multimedia, studioul de podcast și streaming al Grupului Vatra |
| `secretariat-receptie-grupul-vatra-torino-nord.jpg` | Secretariatul și recepția Școlii Grupul Vatra din Via Gressoney |
| `vestiar-scoala-de-dans-torino-nord.jpg` | Vestiarul Școlii Grupul Vatra din Torino Nord |
| `intrare-scoala-via-gressoney-29b-torino.jpg` | Intrarea în Școala Grupul Vatra din Via Gressoney 29/B, Torino |
| `sala-arte-dulapuri-costume-populare-torino.jpg` | Garderoba de costume populare a Școlii Grupul Vatra, în Sala Arte |
| `secretariat-vitrina-trofee-costume-torino.jpg` | Vitrina cu trofee și păpuși în port popular de la secretariatul școlii |
| `sala-mare-parchet-dans-popular-torino.jpg` | Salone Danza gol, pregătit pentru repetiții sau evenimente, Via Gressoney Torino |
| `ansamblul-artistic-vatra-fotografie-oficiala.jpg` | Fotografia oficială a Ansamblului Artistic Vatra, formație completă pe scenă |
| `ansamblul-vatra-costume-dobrogea-scena.jpg` | Ansamblul Artistic Vatra pe scenă, formație completă în costume populare, la spectacolul de final de an |
| `ansamblul-stramoseasca-pereche-adulti-torino.jpg` | Dansatorii adulți ai Ansamblului Strămoșeasca, Grupul Vatra Torino |
| `ansamblul-veselia-costume-bucovina-torino.jpg` | Ansamblul Veselia al Școlii Grupul Vatra din Torino |
| `Ansamblul-Mugurel-Festival-International-Vatra-Dornei.jpg` | Ansamblul de copii Mugurel la Festivalul Internațional de la Vatra Dornei |
| `ansamblul-hora-padului-diplome-spectacol-2026.jpg` | Ansamblul Hora Padului la spectacolul de final de an 2026, Torino |
| `ansamblul-bujorii-de-la-prut-scena-2026.jpg` | Ansamblul de copii Bujorii de la Prut pe scenă, spectacolul Ritmuri de Acasă 2026 |
| `detaliu-costum-calus-ciucuri-opinci.jpg` | Ceata de Călușari a Grupului Vatra, dans călușăresc la Torino |
| `grupul-elle-dans-egiptean-torino-nord.jpg` | Grupul Feminin Elle al Școlii Grupul Vatra, moment de dans de caracter |
| `spectacol-ritmuri-de-acasa-2026-grupul-vatra.jpg` | Fotografia de grup a Școlii Grupul Vatra la spectacolul Ritmuri de Acasă 2026, Teatro San Giuseppe Torino |
| `parada-festival-calusul-romanesc-slatina.jpg` | Parada Școlii Grupul Vatra pe străzile din Slatina, la Festivalul Călușul Românesc |
| `ansamblul-vatra-suita-din-maramures.jpg` | Ansamblul Artistic Vatra în suita din Maramureș, pe scenă |
| `grupul-elle-pizzica-aer-liber-torino.jpg` | Grupul Feminin Elle dansând Pizzica în aer liber, la un eveniment din Torino |
| `ansamblul-vatra-final-suita-scena-torino.jpg` | Finalul unei suite, Ansamblul Artistic Vatra pe scena spectacolului de final de an |
| `ansamblul-veselia-suita-din-galati-grup.jpg` | Ansamblul Veselia, fotografie de grup pe scenă, suita din Galați |
| `barbati-dans-popular-torino-parteneri-de-joc.jpg` | Bărbați din Școala Grupul Vatra, în costum popular, cântând pe scenă |
| `dansatoare-adulte-grupul-vatra-bucurie.jpg` | Dansatoare adulte ale Școlii Grupul Vatra, râzând pe scenă |
| `iurie-raileanu-coregraf-grupul-vatra__varianta-A.jpg` | Iurie Răileanu, fondatorul și coregraful general al Grupului Vatra |
| `gessica-ecaterina-sfabu-instructoare-torino-nord__varianta-A.jpg` | Gessica Ecaterina Sfabu, instructoare de dans popular la Grupul Vatra Torino Nord |
| `sofia-zaynetdinova-coregrafa-balet-grupul-vatra__varianta-A.jpg` | Sofia Zaynetdinova, profesoară de balet și coregrafă de dansuri internaționale |
| `carmen-rotariu-instructoare-dansuri-populare__varianta-A.jpg` | Carmen Georgiana Rotariu, instructoare de dansuri populare la Grupul Vatra |
| `cristian-costin-asistent-instructor-milano__varianta-A.jpg` | Cristian Costin, instructor și dansator în Ansamblul Vatra și Ceata de Călușari |
| `costel-muntianu-instructor-dans-adulti-torino-sud__varianta-A.jpg` | Costel Muntianu, asistent instructor la Ansamblul Strămoșeasca |
| `andreea-mititiuc-secretariat-grupul-vatra.jpg` | Andreea Mititiuc, secretariatul și înscrierile Școlii Grupul Vatra |
| `ioan-ungurianu-departament-media-grupul-vatra.jpg` | Ioan Ungurianu, responsabilul Departamentului Media al Școlii Grupul Vatra |
| `seminar-stanimir-minev-grupul-vatra-torino.jpg` | Seminar de dans cu maestrul Stanimir Minev, la sediul Școlii Grupul Vatra din Torino |
| `departament-media-regie-streaming-torino.jpg` | Regia video și masa de podcast din Sala Multimedia a Grupului Vatra |
| `vatra-solidale-open-graph-1200x630-1.png` | Vatra Solidale — programul de voluntariat al Grupului Vatra în Italia |
| `ansamblul-vatra-joc-barbatesc-saritura-torino.jpg` | (fundal de secțiune — fără text alternativ) |
| `dans-popular-grup-bucurie-scena-torino.jpg` | (fundal de secțiune — fără text alternativ) |


## 9. Verificare înainte de publicare

- [ ] toate cele 54 de fotografii sunt încărcate și se văd
- [ ] filtrele de la cursuri și de la orar funcționează
- [ ] galeria se deschide și se închide cu Esc
- [ ] pagina nu se derulează lateral pe telefon
- [ ] numerele de telefon și linkurile WhatsApp deschid conversația corectă
- [ ] datele structurate trec prin Rich Results Test
- [ ] imaginea socială se vede în Facebook Sharing Debugger

## 10. Ce a rămas de decis

| Punct | Stare |
|---|---|
| Numele persoanelor din portretele trimise recent | **așteaptă confirmarea ta** — nu am atribuit niciun nume |
| Cifra „15" de pe totemul cu valori | presupun aniversarea a 15 ani; nu am publicat-o ca atare |
| Curățarea fostului angajat din celelalte pagini ale site-ului | rămâne de făcut separat, pe cele ~8 pagini de curs |
| Pagina generală a filialelor | amânată de tine, pe parcurs |

Restul este închis. Pagina poate fi publicată.
