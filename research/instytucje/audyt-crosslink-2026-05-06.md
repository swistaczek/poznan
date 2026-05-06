---
typ: audyt crosslinkowania po dodaniu 4 plików referencyjnych
data: 2026-05-06
autor: panel info-arch Opus (sub-agent)
nowe_pliki:
  - ustawa-kominowa-prawo.md
  - ustawa-kominowa-omijanie.md
  - ustawa-kominowa-reformy.md
  - inwestycja-mosty-berdychowskie.md
wykonano:
  - wiceprezydent-golek.md L50 -> inwestycja-mosty-berdychowskie.md
  - wiceprezydent-golek.md L74 -> ustawa-kominowa-prawo.md + ustawa-kominowa-omijanie.md
  - wiceprezydent-golek.md L93 -> ustawa-kominowa-prawo.md
  - prezes-pim-litka.md L141 -> ustawa-kominowa-prawo.md
  - prezes-pim-litka-aneks-pim.md L65 -> ustawa-kominowa-prawo.md + ustawa-kominowa-omijanie.md
  - prezes-pim-litka-teoria-01-werdykt.md L9 -> ustawa-kominowa-prawo.md
  - prezes-pim-litka-teoria-07-werdykt.md L104 -> inwestycja-mosty-berdychowskie.md
pozostawiono: 11 (7 B + 4 C)
---

# Audyt crosslinkowania — 2026-05-06

Cel: po dodaniu 4 plików referencyjnych (`ustawa-kominowa-{prawo,omijanie,reformy}.md` + `inwestycja-mosty-berdychowskie.md`) zweryfikować nawigację między starym a nowym materiałem. `index.md` zaktualizowany w osobnym kroku; w `prezes-pim-litka-aneks-pim.md` L21 i `pim-siec-powiazan-kominy-placowe.md` L165 crosslinki dodano osobno — pomijam.

Metoda: dla każdego z 26 plików `research/instytucje/*.md` (poza nowymi 4) — dwustronny grep po słowach kluczowych (`kominow`, `premia`, `9.06.2016`, `3.03.2000`, `art. 10c`, `antykorup`, `polski ład`, `berdychow`, `budimex`, `95 mln`, `156 mln`, `spółk[ai] komunal`). Identyfikacja kierunku OUT (stary → nowy) oraz IN (nowy → stary).

## Tabela propozycji

| # | Plik źródłowy | Linia | Akcja (link do) | Priorytet | Wykonane |
|---|---|---|---|---|---|
| 1 | wiceprezydent-golek.md | 50 (Mosty Berdychowskie w katalogu inwestycji) | `inwestycja-mosty-berdychowskie.md` | A | TAK |
| 2 | wiceprezydent-golek.md | 74 ("omijania rygorystycznych ograniczeń kominowych") | `ustawa-kominowa-prawo.md` + `ustawa-kominowa-omijanie.md` | A | TAK |
| 3 | wiceprezydent-golek.md | 93 ("nieograniczonego ustawą kominową zarządu PIM") | `ustawa-kominowa-prawo.md` | A | TAK |
| 4 | prezes-pim-litka.md | 141 ("rygor tzw. ustawy kominowej") | `ustawa-kominowa-prawo.md` | A | TAK |
| 5 | prezes-pim-litka-aneks-pim.md | 65 ("zgodność z ustawą z 9.06.2016 r.") | `ustawa-kominowa-prawo.md` + `ustawa-kominowa-omijanie.md` | A | TAK |
| 6 | prezes-pim-litka-teoria-01-werdykt.md | 9 ("nowa ustawa kominowa 9.06.2016") | `ustawa-kominowa-prawo.md` | A | TAK |
| 7 | prezes-pim-litka-teoria-07-werdykt.md | 104 (cytat "Mosty do poprawki") | `inwestycja-mosty-berdychowskie.md` | A | TAK |
| 8 | prezes-pim-litka-werdykt-zbiorczy.md | 9 (T1 "PIM jako obejście polityki płacowej") | `ustawa-kominowa-prawo.md` | B | nie |
| 9 | prezes-pim-litka-werdykt-zbiorczy.md | 16 (T7 "kara 5 tys.") | `inwestycja-mosty-berdychowskie.md` (kontrast Budimex spoza grupy) | B | nie |
| 10 | prezes-pim-litka-aneks-recepcja.md | 35 ("Mosty Berdychowskie — eskalacja kosztów" 28→68,8→156) | `inwestycja-mosty-berdychowskie.md` | B | nie |
| 11 | prezes-pim-litka-aneks-recepcja.md | 37 ("Mosty Berdychowskie — wada dylatacji") | `inwestycja-mosty-berdychowskie.md` | B | nie |
| 12 | prezes-pim-litka-teorie-sledcze.md | 11 ("Teoria 1: Architektura PIM jako obejście ustawy kominowej") | `ustawa-kominowa-prawo.md` + `ustawa-kominowa-reformy.md` | B | nie |
| 13 | prezes-pim-litka-teorie-sledcze.md | 25 ("ustawa kominowa z 9.06.2016 r.") | `ustawa-kominowa-prawo.md` | B | nie |
| 14 | wiceprezes-pim-zaradny.md | 154 ("wynagrodzenia regulowane ustawą kominową") | `ustawa-kominowa-prawo.md` | B | nie |
| 15 | wiceprezes-pim-zaradny-aneks-posum-mtp-pim.md | 75 ("Zmienna część (premie) ≈ 50% bazy") | `ustawa-kominowa-prawo.md` (sec 3.2) | C | nie |
| 16 | wiceprezes-pim-zaradny-aneks-posum-mtp-pim.md | 103 ("nadzorował m.in. mosty Berdychowskie") | `inwestycja-mosty-berdychowskie.md` | C | nie |
| 17 | litka-deep-utworzenie-pim.md | 179 ("Mosty Berdychowskie — most pieszo-rowerowy") | `inwestycja-mosty-berdychowskie.md` | C | nie |
| 18 | litka-deep-utworzenie-pim.md | 238 ("wyższe wynagrodzenia zarządu vs. siatka płac") | `ustawa-kominowa-prawo.md` | C | nie |
| 19 | litka-deep-avrio-eteron.md | 114 ("ustawa antykorupcyjna z 21.08.1997, art. 4") | `ustawa-kominowa-omijanie.md` (sec 4.2 — kaskadowanie + art. 6 antykorupcyjnej) | B | nie |
| 20 | prezes-pim-litka-teoria-04-werdykt.md | 29 ("hipoteza naruszenia ustawy antykorupcyjnej") | `ustawa-kominowa-omijanie.md` | C | nie |

## Kierunek IN (nowe → stare)

Wszystkie 4 nowe pliki w sekcji `## Crosslink z bazą Poznań` linkują już do trzech kotwic: `pim-siec-powiazan-kominy-placowe.md`, `prezes-pim-litka-aneks-pim.md`, `prezes-pim-litka-werdykt-zbiorczy.md`. Brak krytycznych braków IN. Drobna luka:

- `inwestycja-mosty-berdychowskie.md` linkuje do `prezes-pim-litka-aneks-pim.md`, `prezes-pim-litka-teoria-07-werdykt.md`, `pim-siec-powiazan-kominy-placowe.md`, `prezes-pim-litka-werdykt-zbiorczy.md` — kompletne. Mógłby (B) dolinkować do `wiceprezydent-golek.md` (Gołek nadzorował Mosty z ramienia PIM, sekcja "Katalog Inwestycji Strategicznych"), ale to dublowanie.
- `ustawa-kominowa-omijanie.md` mógłby (C) odsyłać do `wiceprezydent-golek.md` jako empirycznego kazusu Nowego Zarządzania Publicznego (sec 6.2 "ugruntowana korupcja polityczna"). Niekrytyczne.

## Uwagi dotyczące spójności bazy

1. **Portrety osób (Litka, Zaradny, Jaśkowiak) — luka strukturalna ograniczona.** Portret Litki (`prezes-pim-litka.md`, 40 KB, 2026-05-05) wzmiankuje ustawę kominową raz (L141) — link dodany. Brak wzmianki o Mostach Berdychowskich w portrecie głównym Litki jest **akceptowalny** — biografia portretowa, nie listing inwestycji; pełna lista w `prezes-pim-litka-aneks-pim.md` (L21 — link już dodano). Portret Zaradnego analogicznie — brak Mostów w głównym pliku jest OK (Zaradny dołączył 1.04.2026, po otwarciu Mostów). Portret Jaśkowiaka (`prezydent-jaskowiak.md`, 51 KB) **nie wzmiankuje** ani ustawy kominowej (mimo że odpowiada za politykę kadrową spółek), ani Mostów — to faktyczna luka treściowa, ale nie crosslinkowa (nie ma czego linkować). Sygnał do uzupełnienia portretu o sekcję "Wskaźniki polityki płacowej w spółkach" — osobny task, poza zakresem audytu.

2. **5 plików deep-dive Litki (`litka-deep-*.md`)** — okres 2002–2014, sprzed PIM/ustawy 2016. Kontakt z nowymi plikami minimalny (kilka wzmianek L114 avrio-eteron, L179 i 238 utworzenie-pim). Pozostawiono jako C — niska wartość retrieval-owa.

3. **9 werdyktów teorii** — najsilniejsze powiązania T1 (kominy) i T7 (Mosty/Tormel). T1 i T7 dostały link A (gotowe). Werdykt zbiorczy L9 i L16 to drugorzędne odniesienia — proponowane B, ale werdykt zbiorczy linkuje już bezpośrednio do plików teorii indywidualnych, więc czytelnik dotrze tam dwoma skokami.

4. **`wyniki-07-kompetencje-instytucji.md`** — plik 67 KB, monolityczny, opis ogólnopolskiego porządku kompetencyjnego (Wojewoda, Marszałek, Prezydent, RM). **Nie zawiera** wzmianek o ustawie kominowej, premiach, Polskim Ładzie ani Mostach Berdychowskich w istotnym kontekście. Brak crosslinku jest **akceptowalny** — to plik referencyjny innej domeny (kompetencje instytucji, nie wynagrodzenia spółek miejskich).

5. **Konwencja crosslinku przyjęta:** śródliniowo `[`nazwa-pliku.md`](./nazwa-pliku.md)` z krótką adnotacją w nawiasie wskazującą sekcję/zakres pliku celu. Format identyczny z istniejącym wzorem w `pim-siec-powiazan-kominy-placowe.md` L165 i `prezes-pim-litka-aneks-pim.md` L21.

6. **Symetria OUT/IN.** Po wykonaniu A: każdy z 4 nowych plików ma minimum 2 wejścia z bazy + linkuje do 3 kotwic w bazie. `inwestycja-mosty-berdychowskie.md` i `ustawa-kominowa-prawo.md` są dobrze odnalazane przez retrieval (odpowiednio 2 i 5 linków przychodzących z 4 różnych plików). `ustawa-kominowa-omijanie.md` ma 1 link przychodzący poza linią 165 `pim-siec-powiazan` — rekomenduję wykonać B-19 (avrio-eteron L114) by dorównać. `ustawa-kominowa-reformy.md` ma 1 link przychodzący (L165 pim-siec-powiazan) — rekomenduję B-12 (teorie-sledcze L11) by zwiększyć retrievability.

## Rekomendacja kolejnych iteracji

- Wykonać B-12 (`prezes-pim-litka-teorie-sledcze.md` L11) i B-19 (`litka-deep-avrio-eteron.md` L114) w pierwszej kolejności — uzupełnią retrievability dla `ustawa-kominowa-reformy.md` i `ustawa-kominowa-omijanie.md`.
- Pozostałe B i C odłożyć do iteracji 2; nie dają nowych ścieżek nawigacyjnych, jedynie redundancję.
