# Sursele de construcție ale paginii v4

Pagina `landing-torino-nord-v4.html` nu a fost scrisă de mână, ci asamblată
din baza v3 plus modulele de mai jos. Scripturile sunt păstrate ca să se poată
reconstrui pagina identic, dacă se schimbă conținutul.

| Fișier | Ce face |
|---|---|
| `css_extra.css` | modulul de grafică și efecte, plus corecturile de contrast |
| `app_v4.js` | interacțiunile: apariție la derulare, cifre, filtre, galerie, bară de progres |
| `build_v4.py` | antet, CSS, valul din hero, cifrele, navigația |
| `build_v4b.py` | filtrele de cursuri, publicul-țintă și data primei lecții pe fiecare card |
| `build_v4c.py` | orarul complet: 28 de grupe, filtre pe zile, coloana „Prima lecție" |
| `build_v4d.py` | galeria cu lupă, clasele de apariție, panglicile tricolore |
| `build_v4e.py` | datele structurate, inclusiv întrebările frecvente, și coada paginii |
| `make_preview.py` | previzualizarea locală, cu fotografiile încorporate |
| `make_graphics.py` | setul grafic social |
| `shots.py`, `check_css.py` | verificările în Chromium: capturi, filtre, galerie, culori calculate |

Ordinea de rulare: `build_v4.py` → `b` → `c` → `d` → `e`, apoi `make_preview.py`.
Baza `base-v3.html` este fișierul `landing-torino-nord-v3.html` primit prin chat.
