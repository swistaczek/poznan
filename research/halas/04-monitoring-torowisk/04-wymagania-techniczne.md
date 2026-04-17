---
title: "Wymagania techniczne BAT: szlifowanie, wibroizolacja, art. 115a POŚ"
type: chunk
domain: halas
source: wyniki-17-monitoring-torowisk-mpk.md
updated: 2026-04-17
---

# 04 — Wymagania techniczne (BAT) i egzekucja art. 115a POŚ

> Źródło: [`../wyniki-17-monitoring-torowisk-mpk.md`](../wyniki-17-monitoring-torowisk-mpk.md)

Strona społeczna nie może opierać roszczeń na ogólnikach („mniej hałasu"). Skuteczne pisma wymagają profesjonalnej nomenklatury inżynieryjnej — konkretne parametry, konkretne technologie, konkretne normy. Europejskie prawo środowiskowe wdraża koncepcję **BAT (Best Available Techniques)** jako minimum dla infrastruktury miejskiej w zabudowie.

## 1. Zużycie faliste szyn (rail corrugation)

**Zjawisko.** Torowisko dyskretnie podparte (podkłady sprężyste) tworzy układ rezonujący. Przejazd zestawu kołowego generuje siły zależne od różnicy prędkości ślizgu i lepkości materiału → cykliczne odkształcenia plastyczne powierzchni tocznej główki szyny → **regularne grzbiety i doliny fal** o określonej długości λ.

**Wzbudzenie.** Pojazd o prędkości v w interakcji z falą λ generuje wibracje o częstotliwości:

$$f = v / \lambda$$

**Pasmo dominujące.** **400–1000 Hz** — manifestuje się jako przenikliwy, dudniący warkot w mieszkaniach pierzei.

**Oznaki degradacji.** Silne impulsy uderzeniowe przy przejeździe składów przez węzły (rondo Kaponiera, most Teatralny, węzeł Roosevelta/Dąbrowskiego). = zaawansowana degradacja + zaniedbania serwisowe.

**Cross-ref.** Diagnostyka widmowa: [`../01-akustyka/02-sygnatury-widmowe.md`](../01-akustyka/02-sygnatury-widmowe.md).

## 2. Programy szlifowania szyn

### 2.1 Szlifowanie profilaktyczne (zapobiegawcze)

**Kiedy.** Krótko po oddaniu torowiska do użytku.

**Cel.** Usunięcie **warstwy odwęglonej** i wad hutniczych ze strefy tocznej — nowa szyna ma powierzchnię zdegradowaną termicznie przez walcowanie, która przyspiesza powstawanie fali.

**Zaniechanie** = kardynalne uchybienie, skutkujące degeneracją toru w ciągu 1–2 lat eksploatacji.

### 2.2 Szlifowanie korekcyjne (cykliczne)

**Podstawa.** Obciążenie przewozowe mierzone w **MGT** (Million Gross Tons — miliony ton brutto obciążenia toru).

**Praktyka BAT.** Ścisły cykl (np. co X MGT) oparty na pomiarach defektoskopowych i monitoringu profilu główki szyny. Brak cyklu = zarządca toleruje fale do poziomu awarii.

**Narzędzia egzekucji (UDIP do MPK).**

1. **Książka Toru / Paszport Toru** — dokumentacja odcinka (parametry, historia remontów, defektoskopia).
2. **Harmonogram szlifowania** na rok bieżący.
3. **Rejestr przeglądów defektoskopowych** — daty, wyniki, decyzje o podjęciu szlifowania.
4. **Raport MGT** dla konkretnego odcinka (obciążenie skumulowane).

Kontakt: **kancelaria@mpk.poznan.pl** — termin 14 dni. Szablon: [`../../../szablony/halas/wniosek-udip-audyt-torowiska.md`](../../../szablony/halas/wniosek-udip-audyt-torowiska.md) [do stworzenia].

## 3. Wibroizolacja masywno-sprężysta — technologie BAT

**Problem fizyczny.** Drgania strukturalne w paśmie **20–80 Hz** propagują energię przez grunt do fundamentów okolicznych budynków → nieznośne drżenie szyb i podłóg wewnątrz mieszkań. Pasmo niesłyszalne / na granicy słyszalności, ale odczuwalne sensorycznie.

**Wymaganie BAT.** Systemowe **przerwanie ciągłości akustycznej konstrukcji** torowiska.

### 3.1 Maty podtłuczniowe (UBM — Under-Ballast Mats)

**Stosowanie.** Torowiska klasyczne z podsypką tłuczniową.

**Funkcja.** Separacja całego masywu torowego od podłoża — dolne odbicie fali sprężystej.

**Parametr krytyczny: sztywność dynamiczna C_dyn** [N/mm³].

**Weryfikacja w OPZ.**
- **Brak parametru C_dyn** w OPZ = dowód, że projektant **nie przeprowadził strojenia wibroakustycznego**. Maty dobrane losowo lub pod cenę.
- Wymaganie: jawny wpis wartości granicznej C_dyn ≤ [wartość] dla konkretnego pasma częstotliwości i obciążenia.
- Certyfikat producenta: ISO 10846 (pomiar sztywności dynamicznej elementów izolacyjnych).

### 3.2 Podkładki podpodkładowe (USP — Under-Sleeper Pads)

**Stosowanie.** Pomiędzy podkładem a podsypką / płytą.

**Funkcja.** Homogenizacja sprężystości punktów podparcia toru. Zapobiega uderzeniom o sztywny styk, tłumi energię przed wniknięciem do podłoża.

**Uzupełnia UBM** — razem tworzą układ **dwustopniowej izolacji**.

### 3.3 Wkładki przyszynowe i powłoki zalewowe (PU)

**Stosowanie.** Torowiska bezpodsypkowe (w tym „zielone torowisko" z trawą).

**Funkcja.** Chronią przed hałasem emitowanym bezpośrednio przez **drgania szyjki i stopki szyny** (wysokie częstotliwości). Ciągła otulina zamiast punktowego mocowania.

**Przykład rozwiązań.** ERS (Embedded Rail System), edilon)(sedra, Pandrol, Phoenix — wkładki PU + masy zalewowe.

### 3.4 Stacjonarne systemy smarowania na łukach

**Stosowanie.** Łuki o małym promieniu (np. ul. Kraszewskiego).

**Funkcja.** Redukcja zjawiska **stick-slip** (przyleganie–ślizg) = źródło piszczenia o wysokiej ostrości tonalnej (pasmo 2–4 kHz, maksymalnie dokuczliwe).

**Rodzaje.** Wayside lubricators (stacjonarne), smarowanie obrzeża koła (onboard), smary biodegradowalne — wymóg dla torowisk w zabudowie.

## 4. Wzorzec zapisu w OPZ / MPZP / DUŚ

Żądanie strony społecznej w dowolnym oknie (MPZP, DUŚ, pytania do SWZ):

> „Dla torowiska na odcinku X zastosować:
> a) ciągłą sprężystą otulinę szyn typu ERS lub równoważnik, C_dyn ≤ [wartość],
> b) maty podtłuczniowe UBM o sztywności dynamicznej C_dyn mierzonej wg ISO 10846,
> c) podkładki podpodkładowe USP na każdym podkładzie,
> d) stacjonarne smarownice w łukach o promieniu < R [m],
> e) program szlifowania profilaktycznego co X MGT z dokumentacją w Paszporcie Toru."

## 5. Interwencja WIOŚ — art. 115a POŚ

**Podstawa prawna.** Ustawa Prawo ochrony środowiska, **art. 115a** — tryb pomiaru kontrolnego.

**Kto składa skargę.**

- Mieszkańcy (indywidualnie, sąsiedzko).
- Organizacje społeczne (stowarzyszenie, fundacja).
- Rada Osiedla (stanowisko/interpelacja).

**Procedura.**

1. **Skarga do WIOŚ Poznań** z żądaniem przeprowadzenia pomiarów kontrolnych ze względu na domniemane przekroczenie dopuszczalnych poziomów hałasu. Dowody wstępne: pomiary własne (niecertyfikowane, ale wskazujące skalę), pomiary ZDM 2016 (L_AeqN 62,2 dB Dąbrowskiego/Roosevelta), skargi mieszkańców.
2. **WIOŚ przeprowadza akredytowane pomiary** — protokół.
3. Po uprawomocnieniu wyników wykazujących przekroczenia — **organ właściwy** (Starosta / Prezydent Miasta wykonujący funkcje starosty) **z urzędu wydaje decyzję** narzucającą operatorowi źródła:
   - maksymalny dopuszczalny poziom hałasu,
   - terminy naprawcze,
   - obowiązek monitoringu porealizacyjnego.

**Konsekwencje niewykonania.**

- **Art. 362 POŚ** — decyzja o ograniczeniu oddziaływania na środowisko.
- **Kary pieniężne cykliczne** (art. 298 nn. POŚ) — stawki za każdy dzień przekroczenia.
- **Administracyjne wstrzymanie użytkowania** — zawieszenie ruchu tramwajowego na odcinku do czasu usunięcia przyczyn (**art. 367 POŚ**). Generuje presję finansową przewyższającą koszt szlifowania.

**Szablon.** [`../../../szablony/halas/skarga-wios-pomiar-kontrolny.md`](../../../szablony/halas/skarga-wios-pomiar-kontrolny.md)

**Uwaga proceduralna.** WIOŚ **nie decyduje o technologii** — organ narzuca limit, operator (MPK/ZDM) dobiera środki. W praktyce jedyny sposób zejścia pod normę dla torowiska w pierzei to BAT → wymuszenie ekonomiczne.

## Cross-ref

- Akustyka i pomiary: [`../01-akustyka/01-metodologia-pomiarow.md`](../01-akustyka/01-metodologia-pomiarow.md)
- Normy i limity (rozp. Ministra Środowiska): [`../01-akustyka/03-normy-limity.md`](../01-akustyka/03-normy-limity.md)
- Precedensy polskie: [`../01-akustyka/05-precedensy-polskie.md`](../01-akustyka/05-precedensy-polskie.md)
- UDIP i przetargi: [`05-udip-przetargi.md`](05-udip-przetargi.md)
