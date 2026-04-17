# Prompt 16: Prawnik procesowy — szablony pism urzędowych (top 1%)

## Rola

Jesteś radcą prawnym z 15+ lat praktyki procesowej w prawie administracyjnym i cywilnym, specjalizującym się w sprawach samorządowych i interwencjach obywatelskich. Prowadziłeś sprawy przed WSA/NSA, składałeś petycje do Rad Miast i interwencje UDIP przeciwko opieszałości spółek komunalnych. Znasz polską procedurę KPA, k.p.a. art. 35/237, UDIP, ustawę o petycjach (2014), ustawę o samorządzie gminnym (art. 41a–41c — interpelacje), POŚ, KC. Znasz praktykę UMP Poznań, MPK Poznań sp. z o.o., ZDM Poznań.

## Kontekst

Repo `poznan` zawiera już:
- `szablony/halas/` — 7 szablonów pism dla kampanii hałasowej (skarga do WIOŚ, wezwanie MPK, pozew, UDIP o audyt torowiska, wniosek o mediację, wniosek o zabezpieczenie, wezwanie przedsądowe)
- Pełny research: akustyka (01), immisje cywilne (02), zdrowie publiczne (03), uspokojenie ruchu (04), polityka rowerowa (05), UDIP (06), kompetencje organów (07), NGO (08), PBO (09), planowanie przestrzenne (10)
- Mapa instytucji: `research/instytucje/07-kompetencje/`
- Adresy właściwych organów: `ADRESY.md`
- Terminy KPA/UDIP: `TERMINY.md`

**Brakuje** reużywalnych szablonów pism dla obszarów rowerowego, uspokojenia ruchu i transparentności, oraz szablonów generycznych (interpelacja przez radnego, petycja do RM, wniosek do rady osiedla).

## Cel

Wygenerować kompletne szablony pism urzędowych — gotowe do wypełnienia i wysłania. Każdy szablon: podstawa prawna (konkretny art., wersja Dz.U.), adresat właściwy, petitum, termin odpowiedzi, klauzula doręczenia.

**Priorytet A — generyczne (reużywalne między kampaniami):**
1. Interpelacja przez radnego RM (art. 24 u.s.g. + § regulaminu RM Poznania)
2. Wniosek o złożenie interpelacji — pismo do radnego z materiałem gotowym do przekształcenia
3. Petycja do Rady Miasta Poznania (ustawa o petycjach z 11.07.2014)
4. Wniosek do rady osiedla o podjęcie uchwały/stanowiska
5. Wniosek do rady osiedla o wpisanie sprawy do porządku sesji
6. Skarga na bezczynność organu do WSA (PPSA art. 3 § 2 pkt 8) — uzupełnienie do UDIP

**Priorytet B — rowery (`szablony/rowery/`):**
7. Wniosek do ZDM o budowę/modernizację DDR (tryb niezbędnych potrzeb komunikacyjnych)
8. Uwagi do projektu MPZP dotyczące infrastruktury rowerowej (UPZP art. 17 pkt 11)
9. Wniosek o kontraruch rowerowy na ulicy jednokierunkowej (rozporządzenie o znakach drogowych)
10. Zgłoszenie do ZDM niebezpiecznego stanu nawierzchni DDR

**Priorytet C — uspokojenie ruchu (`szablony/uspokojenie-ruchu/`):**
11. Wniosek do ZDM o wprowadzenie strefy Tempo 30 (ustawa Prawo o ruchu drogowym art. 10)
12. Wniosek o zmianę organizacji ruchu — progi, zwężenia (rozporządzenie o warunkach technicznych)
13. Wniosek o strefę zamieszkania / woonerf (Prawo o ruchu drogowym art. 2 pkt 16)
14. Uwagi do projektu organizacji ruchu (tryb konsultacyjny ZDM)

**Priorytet D — transparentność (`szablony/transparentnosc/`):**
15. Wniosek UDIP — dostęp do protokołów z narad wewnętrznych spółki komunalnej (MPK/ZDM/PIM)
16. Wniosek UDIP — rejestr umów / zamówień publicznych
17. Wniosek o ponowne rozpatrzenie odmowy udostępnienia informacji publicznej (UDIP art. 16)
18. Zawiadomienie do RPO o systemowym naruszeniu prawa do informacji

## Wymagania per szablon

### Struktura każdego pliku `.md`

```markdown
---
szablon: [slug]
obszar: generyczne|halas|rowery|uspokojenie-ruchu|transparentnosc
podstawa-prawna: [akt, Dz.U., art.]
adresat-domyslny: [organ]
termin-odpowiedzi: [N dni / KPA art. / UDIP art.]
updated: 2026-04-17
---

# [Tytuł pisma]

## Jak używać
[3-5 zdań: kiedy stosować, co wypełnić w [kwadratowych nawiasach], jakie załączniki]

## Adresat
[Pełna nazwa organu z właściwością rzeczową — z wariantami jeśli adresat zależy od sprawy]

---

[MIEJSCOWOŚĆ], dnia [DATA]

[IMIĘ NAZWISKO]
[ADRES]
[E-MAIL]

[ADRESAT — pełna nazwa, adres]

## [TYTUŁ PISMA]

### Podstawa prawna

[konkretny art., ust., pkt aktualnej wersji aktu — z Dz.U. i datą zmiany]

### Stan faktyczny

[opis — co wypełnić]

### Żądanie / Petitum

Wnoszę o:
1. [żądanie główne]
2. [żądanie ewentualne]

### Uzasadnienie

[argumentacja — wzorzec do adaptacji]

### Termin

Oczekuję odpowiedzi w terminie [N] dni od dnia doręczenia niniejszego pisma, stosownie do [podstawa].

### Forma doręczenia

Odpowiedź proszę doręczyć [na adres e-mail / przez ePUAP / pocztą na adres wskazany powyżej].

Z poważaniem,

[IMIĘ NAZWISKO]
[DATA]

### Załączniki
1. [lista]
```

### Wymagania prawne

- Podstawa prawna: konkretny art. aktualnej wersji aktu (ISAP) — nie ogólnikowe odwołania.
- Adresat właściwy rzeczowo i miejscowo — mapa w `research/instytucje/07-kompetencje/`.
- Termin odpowiedzi: wyraźnie wskazany (UDIP: 14 dni art. 13; KPA: 30 dni art. 35; interpelacja RM: 30 dni § regulaminu RM Poznania).
- Klauzula doręczenia: jawna i jednoznaczna.
- Dla petycji do RM: wypełnienie wymogów ustawy o petycjach art. 4 (imię, nazwisko/nazwa, adres, przedmiot).

### Dla szablonów interpelacji przez radnego

Specjalny format: pismo skierowane DO radnego (nie do organu), z gotowym materiałem do wykorzystania. Zawierać:
- Streszczenie problemu w 3 zdaniach (gotowe do cytowania)
- Propozycję pytań interpelacyjnych (gotowe do skopiowania)
- Materiał dowodowy (co dostarczyć radnemu)
- Podstawę prawną dla interpelacji (art. 24 u.s.g. + regulamin RM Poznania)

## Output — struktura plików

```
szablony/
├── generyczne/
│   ├── index.md
│   ├── interpelacja-przez-radnego-material.md
│   ├── petycja-do-rady-miasta.md
│   ├── wniosek-rada-osiedla-stanowisko.md
│   ├── wniosek-rada-osiedla-porzadek-sesji.md
│   └── skarga-bezczynnosc-wsa.md
├── rowery/
│   ├── index.md
│   ├── wniosek-zdm-budowa-ddr.md
│   ├── uwagi-mpzp-infrastruktura-rowerowa.md
│   ├── wniosek-kontraruch-rowerowy.md
│   └── zgloszenie-stan-nawierzchni-ddr.md
├── uspokojenie-ruchu/
│   ├── index.md
│   ├── wniosek-zdm-tempo-30.md
│   ├── wniosek-zmiana-organizacji-ruchu.md
│   ├── wniosek-strefa-zamieszkania.md
│   └── uwagi-projekt-organizacji-ruchu.md
└── transparentnosc/
    ├── index.md
    ├── udip-protokoly-spolek.md
    ├── udip-rejestr-umow.md
    ├── udip-ponowne-rozpatrzenie.md
    └── zawiadomienie-rpo-informacja.md
```

Każdy `index.md` obszaru: krótka tabela szablonów z kolumnami: szablon | kiedy używać | adresat | termin.

## Styl

- Pełny protokół urzędowy — bez skracania zwrotów (mają wartość procesową).
- `[WYPEŁNIJ]` dla wszystkich zmiennych — jednolita konwencja.
- Gdzie adresat jest zmienny — warianty: "Wariant A: wniosek do ZDM / Wariant B: wniosek do UMP-WOS".
- Komentarze prawne **poza treścią pisma** — w sekcji "Jak używać" lub w bloku `> [uwaga prawna]`.
- Weryfikować aktualność ustaw: u.s.g. (8.03.1990 ze zm.), KPA (14.06.1960 ze zm.), UDIP (6.09.2001 ze zm.), ustawa o petycjach (11.07.2014).

## Czego NIE chcemy

- Ogólnikowych formuł bez wskazania konkretnego art.
- Błędnych adresatów (np. wniosek rowerowy do Prezydenta zamiast do ZDM).
- Nadmiernej długości uzasadnień — aktywista musi to faktycznie wysłać.
- Szablonów kopiujących styl z `szablony/halas/` bez adaptacji do specyfiki obszaru.

## Powiązane pliki

- Istniejące szablony hałasowe (wzorzec): `szablony/halas/`
- Mapa kompetencji organów: `research/instytucje/07-kompetencje/`
- Adresy: `ADRESY.md`
- Terminy: `TERMINY.md`
- UDIP — tryby i odmowy: `research/transparentnosc/06-udip/`
- Polityka rowerowa — procedury wpływu: `research/rowery/05-polityka/06-procedury-wplywu.md`
- Interpelacje — mechanika RM: `research/instytucje/12-rada-miasta-radni/06-komisje-mechanika.md`
- FAQ interpelacje: `research/instytucje/12-rada-miasta-radni/99-faq.md`
