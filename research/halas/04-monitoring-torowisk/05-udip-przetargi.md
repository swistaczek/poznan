---
title: "UDIP, platformy przetargowe, strategia przez rynek"
type: chunk
domain: halas
source: wyniki-17-monitoring-torowisk-mpk.md
updated: 2026-04-17
---

# 05 — UDIP i monitoring przetargów

> Źródło: [`../wyniki-17-monitoring-torowisk-mpk.md`](../wyniki-17-monitoring-torowisk-mpk.md)

Wywiad jawnoźródłowy (OSINT) — fundament operacyjny kampanii torowej. Władze samorządowe **nie promują** informacji o planowanych remontach z wyprzedzeniem; aktywista musi przejąć inicjatywę w ich pozyskaniu.

## 1. Platformy monitoringu zamówień

### 1.1 Publikatory urzędowe

**BZP — Biuletyn Zamówień Publicznych.**
- URL: bzp.uzp.gov.pl / ezamowienia.gov.pl
- Zamówienia krajowe poniżej progów unijnych.
- Alerty: konto + subskrypcja po kodach CPV i po zamawiającym.

**TED — Tenders Electronic Daily (Dz.U. UE).**
- URL: ted.europa.eu
- Powyżej progów unijnych (np. roboty budowlane ~5,5 mln EUR).
- Alerty: RSS / e-mail per CPV + lokalizacja.

### 1.2 Platformy komercyjne (zamówienia podprogowe MPK)

**Logintrade.** Platforma komercyjna — wielu zamawiających publicznych.

**eB2B.** Portal zakupowy MPK Poznań / PIM — natywny.

**Co publikują.** Postępowania poniżej progów PZP (regulamin wewnętrzny MPK) + zamówienia z **§1 ust. 2 regulaminu** (odstąpienie Kierownika Zamawiającego). Sekcje:
- „Przetargi > Ogłoszone"
- „Regulamin udzielania zamówień"

### 1.3 Kody CPV — słownik

**Wspólny Słownik Zamówień (CPV):**

| CPV | Zakres |
|---|---|
| **45234121-0** | Roboty w zakresie kładzenia torów tramwajowych |
| **45234116-2** | Roboty budowlane w zakresie torowisk |
| **45233140-2** | Roboty drogowe |
| 45234126-5 | Roboty budowlane w zakresie budowy linii tramwajowych |
| 71320000-7 | Usługi inżynieryjne w zakresie projektowania |
| 71631480-8 | Usługi kontroli dróg |
| 45234115-5 | Roboty w zakresie sygnalizacji kolejowej |

Filtr dodatkowy: **zamawiający = „MPK Poznań", „Poznańskie Inwestycje Miejskie", „ZDM Poznań"**.

### 1.4 Konfiguracja alertów

1. **BZP** — ezamowienia.gov.pl, konto wykonawcy → alerty po CPV.
2. **TED** — ted.europa.eu → „My searches" z filtrem CPV + NUTS-PL415 (Poznań).
3. **Logintrade** — konto → subskrypcje po zamawiającym.
4. **eB2B** — rejestracja + newsletter.
5. **Dodatkowo**: RSS/API BIP bip.poznan.pl (sekcje uchwał RM, ogłoszeń MPU).

**Cel operacyjny:** powiadomienie **w ciągu 24 h** od publikacji SWZ — kluczowe dla wykorzystania kilkudniowego okna pytań.

## 2. UDIP do MPK — dokumentacja techniczna torowiska

**Podstawa prawna.** Art. 61 Konstytucji RP + **Ustawa o dostępie do informacji publicznej** (UDIP, Dz.U. 2001 nr 112 poz. 1198 z późn. zm.).

**Odrzucenie obron urzędniczych.**
- „Tajemnica przedsiębiorstwa" → **nie ma zastosowania** do infrastruktury tramwajowej finansowanej z pieniędzy publicznych i realizującej usługę publiczną. Mocna linia orzecznicza NSA.
- „Dokumenty wewnętrzne / robocze" → jeżeli dokument dotyczy sprawy publicznej (majątek komunalny, zdrowie mieszkańców) — **jest informacją publiczną**.

### 2.1 Zakres żądania

Wniosek UDIP do MPK powinien domagać się:

1. **Paszporty techniczne / Książka Toru** dla zdigitalizowanych odcinków z ostatnich 24 miesięcy.
2. **Dzienniki oględzin torowisk** — adnotacje o falowaniu szyn, luźnych łączeniach, uszkodzeniach wkładek.
3. **Wyciąg ze zintegrowanego rejestru umów** z zewnętrznymi kooperantami (podbijanie, szlifowanie, diagnostyka defektoskopowa). Format: **arkusz XLS** (umożliwia analizę wolumenów wydatków na mitygację wibracji).
4. **Protokoły odbiorów gwarancyjnych** i pomiarów technicznych po wcześniejszych remontach — weryfikacja trwałości powłok mas zalewowych, uszczelnień.
5. **Harmonogram szlifowania** na rok bieżący.
6. **Raport MGT** (obciążenie skumulowane) dla konkretnego odcinka.
7. **Założenia techniczne do planu remontów** na rok bieżący.

### 2.2 Procedura

**Adres.** `kancelaria@mpk.poznan.pl` (zwykły e-mail wystarczy — art. 10 ust. 1 UDIP, bez ePUAP).

**Termin.** **14 dni** (art. 13 ust. 1 UDIP). Przedłużenie — maks. 2 miesiące z uzasadnieniem.

**Odmowa.** Tylko w formie **decyzji administracyjnej** (art. 16 UDIP) — zaskarżalnej.

**Ścieżka odwoławcza.**

1. **Samorządowe Kolegium Odwoławcze (SKO)** w Poznaniu — 14 dni od doręczenia decyzji.
2. **Wojewódzki Sąd Administracyjny (WSA)** w Poznaniu — skarga po wyczerpaniu trybu instytucjonalnego, 30 dni od doręczenia decyzji SKO.
3. **NSA** — skarga kasacyjna.

**Sankcje za odmowę.** **Art. 23 UDIP** — grzywna, ograniczenie wolności lub pozbawienie wolności do roku dla funkcjonariusza odmawiającego bezpodstawnie. Przywołanie w ponagleniu działa dyscyplinująco.

**Szablon.** [`../../../szablony/halas/wniosek-udip-audyt-torowiska.md`](../../../szablony/halas/wniosek-udip-audyt-torowiska.md) [do stworzenia]

## 3. UDIP do UMWW — PHNUA i mapy hałasu

**Adresat.** Urząd Marszałkowski Województwa Wielkopolskiego, Departament Środowiska (Poznań).

**Podstawa.** Ustawa o udostępnianiu informacji o środowisku (UUIŚ) + UDIP — stosować równolegle.

**Żądanie.**

1. **Załączniki tabelaryczne PHNUA** (uchwała Sejmiku **IV/92/24 z lipca 2024**) — szczegółowy wykaz ulic dla Poznania z wartościami wskaźników L_DWN/L_N.
2. **Rozbicie na kategorie** — 1.3.1 (hałas drogowy) oraz 1.3.3 (hałas szynowy tramwajowy).
3. **Algorytm wyliczania wskaźnika „M"** — parametry: gęstość zaludnienia, procent poszkodowanych, L_DWN, L_N.
4. **Uzasadnienie przeszeregowania** — jeżeli odcinek z przekroczeniem SMH 2022 nie trafił do priorytetów 2024–2029.
5. **Harmonogram działań naprawczych** 2024–2029 dla Poznania.

**Terminy.**
- UUIŚ art. 14 — **1 miesiąc** dla informacji o środowisku (wyjątek: do 2 miesięcy przy złożoności).
- UDIP art. 13 — **14 dni** dla pozostałych dokumentów (raporty, wskaźniki).

**Cel.** Wymuszenie wpisu ul. Dąbrowskiego na listę priorytetów krótkoterminowych (2024–2029) → aktywacja obowiązku PHNUA wobec MPK i ZDM.

## 4. Strategia „przez rynek" — transfer wiedzy

Stowarzyszenia **nie mają legitymacji** do wnoszenia odwołań KIO / żądań wyjaśnień do zamawiającego. Ustawa PZP przyznaje je tylko wykonawcom z „interesem w uzyskaniu danego zamówienia". Ale:

**Mechanizm.**

1. **Przygotowanie analizy akustycznej** — własne pomiary (protokół z [`../01-akustyka/01-metodologia-pomiarow.md`](../01-akustyka/01-metodologia-pomiarow.md)), ekspertyzy, odwołanie do pomiarów ZDM 2016 (L_AeqN 62,2 dB Dąbrowskiego/Roosevelta).
2. **Przekazanie** do biur projektowych / firm drogowych / producentów mat wibroizolacyjnych (ERS, edilon)(sedra, Pandrol, Phoenix) działających na rynku wielkopolskim.
3. **Firmy branżowe** oficjalnie zadają pytania do SWZ — w ich interesie ekonomicznym jest rozszerzenie OPZ o technologie, które dostarczają.
4. **Zamawiający** musi odpowiedzieć na każde pytanie (art. 135 PZP); odpowiedzi publikowane publicznie.
5. **Odrzucenie uzasadnionego żądania** → odwołanie wykonawcy do **KIO**.

**Efekt.** Firma branżowa robi to, czego stowarzyszenie nie może zrobić formalnie — dźwignia proceduralna.

**Uwaga.** Transfer jawny (pisma, e-mail) — nie angażowanie w „zmowę" z konkretnym oferentem (ryzyko wykluczenia z postępowania).

## 5. Strategia retrospektywna — analiza §1 ust. 2

Regulamin wewnętrzny MPK (ujednolicony 2022) zawiera **§1 ust. 2**: Kierownik Zamawiającego może w uzasadnionych przypadkach odstąpić od stosowania regulaminu.

**Ewidencja.** Co kwartał — UDIP do MPK z żądaniem:

1. Liczba postępowań udzielonych z wyłączeniem §1 ust. 2 w ostatnich 12 miesiącach.
2. Łączna wartość zamówień z wyłączenia.
3. Uzasadnienia wyłączeń (lista).
4. Nazwy wykonawców.

**Cel.** Wskaźnik inercji proceduralnej MPK + podstawa do interpelacji radnych / skargi do Rady Nadzorczej spółki / petycji do Prezydenta jako właściciela (100% udziałów Miasta).

## Cross-ref

- Okna przetargowe i cykl: [`01-cykl-remontowy.md`](01-cykl-remontowy.md)
- PHNUA — co żądać: [`02-phnua-mapa-halasu.md`](02-phnua-mapa-halasu.md)
- UDIP ogólna praktyka: [`../01-akustyka/07-udip-zapytania.md`](../01-akustyka/07-udip-zapytania.md)
- Transparentność (obszar): [`../../transparentnosc/`](../../transparentnosc/)
