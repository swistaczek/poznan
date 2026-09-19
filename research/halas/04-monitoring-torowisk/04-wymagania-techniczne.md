---
title: "Wymagania techniczne BAT: szlifowanie, wibroizolacja, przegląd ekologiczny art. 237/241 POŚ"
type: chunk
domain: halas
source: wyniki-17-monitoring-torowisk-mpk.md
updated: 2026-09-19
---

> **KOREKTA 19.09.2026**: sekcja 5 poniżej pierwotnie opierała egzekucję na art. 115a POŚ + WIOŚ. To błędne dla hałasu drogowego/tramwajowego - **art. 115a ust. 2 POŚ wyłącza drogi i linie tramwajowe** z tego trybu, a WIOŚ nie ma tu sprawczości. Poprawiono na właściwą ścieżkę: art. 237/241 POŚ (przegląd ekologiczny) + art. 362 POŚ, z właściwością **Marszałka Województwa** (art. 378 ust. 2a pkt 4 POŚ), nie Starosty/Prezydenta. Zobacz też `../../dabrowskiego/halas/PLAN-KOMPLEKSOWY-REMONT-TOROWISKA.md` pkt 2.

# 04 — Wymagania techniczne (BAT) i przegląd ekologiczny (art. 237/241 POŚ)

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

## 5. Przegląd ekologiczny — art. 237/241 POŚ (WŁAŚCIWA ścieżka dla hałasu drogowego/tramwajowego)

**Podstawa prawna.** Ustawa Prawo ochrony środowiska: art. 237 (organ może zobowiązać do sporządzenia i przedłożenia przeglądu ekologicznego), art. 241 (treść przeglądu), art. 362 (decyzja o ograniczeniu oddziaływania/dostosowaniu do wymagań). **Nie art. 115a** - ten wprost wyłącza drogi i linie tramwajowe (art. 115a ust. 2 POŚ). Organ właściwy: **Marszałek Województwa Wielkopolskiego** (art. 378 ust. 2a pkt 4 POŚ - dla przedsięwzięć mogących znacząco oddziaływać na środowisko, w tym dróg i linii tramwajowych), nie Starosta/Prezydent i nie WIOŚ.

**Kto może wnioskować/skarżyć się.**

- Mieszkańcy (indywidualnie, sąsiedzko) - wniosek o wszczęcie postępowania z urzędu.
- Organizacje społeczne (stowarzyszenie, fundacja) - status strony na zasadach art. 44 ustawy OOŚ.
- Rada Osiedla (stanowisko/interpelacja).

**Procedura.**

1. Wniosek do Marszałka Województwa Wielkopolskiego o zobowiązanie zarządcy torowiska (Miasto/ZTM) do sporządzenia i przedłożenia **przeglądu ekologicznego** (art. 237 POŚ), z dowodami wstępnymi: pomiary BAASA 2026 (PPH3.05 +2,1/+3,9 dB, PPH4.16 +3,9 dB dzień), pomiary ZDM 2016, skargi mieszkańców.
2. Przegląd ekologiczny (art. 241 POŚ) musi zawierać m.in. ocenę oddziaływania na środowisko, w tym hałas, oraz wskazanie ewentualnych działań naprawczych.
3. Na podstawie przeglądu Marszałek może wydać **decyzję na podstawie art. 362 POŚ**, nakładającą na zarządcę obowiązek ograniczenia oddziaływania w określonym terminie, w tym m.in. wymóg zastosowania dostępnych technik ograniczających hałas.

**Konsekwencje niewykonania decyzji z art. 362 POŚ.**

- Kary pieniężne cykliczne (art. 298 nn. POŚ) - stawki za każdy dzień niewykonania.
- Wstrzymanie użytkowania instalacji/urządzenia w skrajnych przypadkach (art. 367-368 POŚ) - w praktyce trudne do zastosowania wobec czynnej linii tramwajowej obsługującej komunikację miejską, traktować jako środek teoretyczny, nie realny straszak.

**Szablon.** Brak gotowego wzoru wniosku o przegląd ekologiczny w repo - [do stworzenia], NIE używać `skarga-wios-pomiar-kontrolny.md` (ten dotyczy instalacji/urządzeń w rozumieniu art. 115a, nie dróg/torowisk).

**Uwaga proceduralna.** Marszałek **nie decyduje o konkretnej technologii** w decyzji - narzuca obowiązek ograniczenia oddziaływania w terminie, zarządca (ZTM/MPK) dobiera środki (BAT z sekcji 1-4 wyżej). Ta ścieżka jest wolniejsza i mniej przetestowana niż nacisk budżetowy przez WPF (zob. `../../dabrowskiego/halas/PLAN-KOMPLEKSOWY-REMONT-TOROWISKA.md`) - traktować jako uzupełniającą, nie główną.

## Cross-ref

- Akustyka i pomiary: [`../01-akustyka/01-metodologia-pomiarow.md`](../01-akustyka/01-metodologia-pomiarow.md)
- Normy i limity (rozp. Ministra Środowiska): [`../01-akustyka/03-normy-limity.md`](../01-akustyka/03-normy-limity.md)
- Precedensy polskie: [`../01-akustyka/05-precedensy-polskie.md`](../01-akustyka/05-precedensy-polskie.md)
- UDIP i przetargi: [`05-udip-przetargi.md`](05-udip-przetargi.md)
