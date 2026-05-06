# Changelog — runy skill-a `aktualizuj-stenogramy-rm`

Każdy run dopisuje wpis na końcu. Format: timestamp ISO + lista zmian per kategoria.

---

## Run 2026-05-06T10:20:00+02:00 — pierwsze uruchomienie (bootstrap)

Inicjalizacja bazy. Tworzenie struktury katalogów + pierwsze pobrania.

- **Sesje plenarne (kadencja IX)**: bootstrap z BIP (sub-agent A)
- **Sesje plenarne (kadencja VI, historyczne)**: sesja LXII/2014 (PIM) — manualne dodanie (sub-agent A)
- **Komisje (kadencja IX)**:
  - Rewizyjna: 6 posiedzeń III–IV.2026 (sub-agent B)
  - Budżet/Finanse/Nadzór Właścicielski: ostatnie 5 posiedzeń (sub-agent B)
  - Polityki Przestrzennej: ostatnie 5 posiedzeń (sub-agent C)
- **Łącznie nowych dokumentów**: zob. wpisy detail per sub-agent niżej
- **Czas runu**: ~10 min równoległej pracy 3 sub-agentów Sonnet
- **Scope v1**: bootstrap z 3 priorytetowych komisji + lista sesji kadencji IX + 1 historyczna. Pełna 15-komisyjna kwerenda — iteracja 2 (kolejny run).
- **Błędy/luki**: [do uzupełnienia po pierwszym runie]

[Detail per sub-agent zostanie dopisany przez sub-agenty po zakończeniu pracy.]

### Sub-agent B — komisje twarde (2026-05-06)

- **Rewizyjna**: 6 stubów posiedzeń III–IV.2026 (Czerwiński, kontrola spółek + budżet 2025).
  - 2026-03-05 (id=536444), 2026-03-17 (id=536630), 2026-03-19 (id=537856 — częściowo niejawne), 2026-04-09 (id=540140), 2026-04-16 (id=539592), 2026-04-23 (id=540594).
- **Budżet/Finanse/Przedsiębiorczość/Nadzór Właścicielski** (pełna nazwa BIP): 5 ostatnich stubów.
  - 2026-04-13 (id=540537), 2026-03-16 (id=537811), 2026-03-09 (id=537017 — wyjazdowe Port Lotniczy, posiedzenie łączone z KT i KPMTiR), 2026-02-09 (id=533811), 2026-01-19 (id=531849).
- **Łącznie**: 11 stubów + 2 indeksy komisji.
- **Indeksy**: dodano `rewizyjna/index.md`, `budzet-finanse-nadzor-wlascicielski/index.md`. Zaktualizowano `komisje/index.md` (URL-e BIP, korekty: pełna nazwa Komisji Budżetowej zawiera „Przedsiębiorczości"; przewodnicząca = Małgorzata Dudzic-Biskupska KO).
- **Korekty terminologiczne**: Komisja Budżetowa ma 4-człon w nazwie (Budżetu/Finansów/Przedsiębiorczości/Nadzoru Właścicielskiego), nie 3-człon jak w pierwotnej mapie.
- **Błędy/luki**: brak (wszystkie 11 protokołów opublikowanych w BIP). Crawl-delay 5 s respektowany między WebFetch (~16 requestów + 5 s każdy = ~80 s overhead).
- **Obserwacja parsowania**: strony posiedzeń BIP zawierają porządek obrad w czystym numerowanym formacie + link do DOCX (parametr `parent={id-posiedzenia}` + `id={id-protokolu}`). Format spójny w obu komisjach. Strony komisji (`/komisje/{slug},{id}/`) zawierają listę 39+ protokołów retro z ID DOCX, ale bez powiązania z URL-em strony posiedzenia — trzeba przejść przez `/posiedzenia/archiwum/{strona}/` po URL posiedzenia. Paginacja archiwum: 4 strony × ~45 dni = ~180 dni archiwum w czterech stronach.

---

### Sub-agent C — komisje przestrzenne (2026-05-06)

**Weryfikacja struktury komisji:**
- BIP potwierdza: **dwie odrębne komisje** (nie jedna „Polityki Przestrzennej i Rewitalizacji").
- **Komisja Polityki Przestrzennej** (ID 1521) — przewodniczący Łukasz Mikuła; URL: https://bip.poznan.pl/bip/komisje/komisja-polityki-przestrzennej,1521/
- **Komisja Rewitalizacji i Inicjatyw Lokalnych** (ID 1532) — przewodnicząca Monika Danelska; URL: https://bip.poznan.pl/bip/komisje/komisja-rewitalizacji-i-inicjatyw-lokalnych,1532/

**Komisja Polityki Przestrzennej** (Mikuła, MPZP): 5 stubów
- `komisje/polityki-przestrzennej/protokol-2026-05-06.md` — status: brak_protokolu (posiedzenie w dniu runu)
- `komisje/polityki-przestrzennej/protokol-2026-04-22.md` — status: brak_protokolu; Park Kulturowy Ostrów Tumski
- `komisje/polityki-przestrzennej/protokol-2026-04-08.md` — status: opublikowany; DOCX id=540099; MPZP PU 73+74/2026
- `komisje/polityki-przestrzennej/protokol-2026-03-11.md` — status: opublikowany; DOCX id=537361; Rejon Stadionu Miejskiego + Stare Winogrady; art. 36 u.p.z.p.; uchwała krajobrazowa
- `komisje/polityki-przestrzennej/protokol-2026-02-04.md` — status: opublikowany; DOCX id=533282; Strategia 2040+; MPZP 28 Czerwca 1956/Łozowa

**Komisja Rewitalizacji i Inicjatyw Lokalnych** (Danelska): 5 stubów
- `komisje/rewitalizacji/protokol-2026-05-05.md` — status: brak_protokolu; Komitet Rewitalizacji, Centrum Nauki
- `komisje/rewitalizacji/protokol-2026-04-22.md` — status: brak_protokolu; Park Kulturowy Ostrów Tumski; UWAGA: ID 98657 zbieżne z KPP — do weryfikacji (posiedzenie wspólne?)
- `komisje/rewitalizacji/protokol-2026-04-07.md` — status: opublikowany; DOCX id=539953; Poznańskie Rynki i Place
- `komisje/rewitalizacji/protokol-2026-03-31.md` — status: opublikowany; DOCX id=539290; zabytkowa hala filtrów
- `komisje/rewitalizacji/protokol-2026-03-10.md` — status: opublikowany; DOCX id=537128; PBO 2027

**Łącznie**: 10 stubów (5 KPP + 5 KRiIL).

**Korekta nazw komisji w `komisje/index.md`**:
- „Polityki Przestrzennej i Rewitalizacji" → dwie oddzielne pozycje: „Komisja Polityki Przestrzennej" (Mikuła) + „Komisja Rewitalizacji i Inicjatyw Lokalnych" (Danelska)
- „Budżetu, Finansów i Nadzoru Właścicielskiego" → „…Przedsiębiorczości i Nadzoru Właścicielskiego" (ID 1520)
- „Gospodarki Komunalnej i Ochrony Środowiska" → „Ochrony Środowiska i Gospodarki Komunalnej" (ID 1522)
- „Zdrowia i Polityki Społecznej" → „Rodziny, Polityki Społecznej i Zdrowia" (ID 1526)
- „Promocji i Rozwoju" → „Promocji Miasta, Turystyki i Rekreacji" (ID 1530)
- Dodano URL-e BIP dla wszystkich skorygowanych komisji

**Błędy / uwagi**:
- Dwa posiedzenia (2026-05-06 KPP i 2026-05-05 KRiIL) bez protokołów — posiedzenia świeże.
- ID posiedzenia 98657 pojawia się zarówno dla KPP jak i KRiIL z datą 2026-04-22 — prawdopodobnie posiedzenie wspólne lub błąd parsowania BIP. Do weryfikacji po publikacji protokołu.
- BIP nie eksponuje pełnych porządków obrad na stronach komisji — trzeba wchodzić na strony poszczególnych posiedzeń.
- Godzina posiedzenia KRiIL 2026-03-10 zmieniona z 14:30 na 15:00 (nota na stronie BIP).

---

### Sub-agent A — sesje plenarne (2026-05-06)

- **Kadencja IX**: stworzono **22 stuby** (sesje I, XIV–XXXIV) + **1 stub-luka** dla sesji II–XIII 2024. Pełne metadane z API BIP (porządek 34 punkty + 3 załączniki) tylko dla **1 sesji**: XXXIV/12.05.2026, ID=98779. Pozostałe stuby — z harmonogramów RM 2025/2026 (BIP, dokumenty 133755 i 254683).
- **Kadencja VI (historyczna)**: stworzono **1 stub** LXII/2014-01-28 (PIM). URL BIP sesji: `https://bip.poznan.pl/bip/sesje/kadencja-2010-2014,8/lxii,50179/`. Linki do uchwał LXII/959 (BIP id=50447) i LXII/960 (BIP id=50448). Crosslink z `litka-deep-utworzenie-pim.md`, `prezes-pim-litka-werdykt-zbiorczy.md` (T1, T2), `nowe-teorie-2026-05-06.md` (T11), `pim-siec-powiazan-kominy-placowe.md`.
- **Łącznie**: **24 nowe pliki** (22 stuby IX + 1 stub-luka + 1 historyczna LXII) + **2 zaktualizowane** (`sesje-plenarne/index.md`, `sesje-plenarne/kadencja-IX-2024-2029/index.md` — utworzony nowy).
- **Czas runu**: ~50 min (10:05–10:55 CEST).
- **Błędy/luki/odchylenia od skill-a**:
  1. **Limit WebFetch wyczerpany ~10:35 CEST** (reset 13:10) — przerwało crawl pełnych metadanych dla 5 ostatnich sesji XXIX–XXXIII. Skill wymaga „pełne metadane dla 5 ostatnich + planowanej XXXIV" → faktycznie 1/6 (tylko XXXIV).
  2. **BIP renderuje listę sesji dynamicznie (JavaScript)**: WebFetch widzi tylko najbliższą sesję na `/bip/sesje/`. Pełna lista sesji kadencji IX dostępna tylko w przeglądarce JS lub przez `/api-json/bip/sesje/{slug},{id}/` per sesja (musi znać ID).
  3. **Brak harmonogramu sesji 2024 w BIP** — luka strukturalna źródła. Sesje I–XIII (2024) wymagają oddzielnego crawlu po ID (zakres szac. 87000–95000) lub UDIP do BoR.
  4. **API JSON `/api-json/bip/sesje/`** zwraca pustą tablicę `data: [""]` — endpoint indeksu, nie listy sesji. Listę zwraca tylko HTML renderowany JS.
  5. **Skanowanie ID 98200–98778** (między XXXIII a XXXIV): testowane 98200, 98400, 98490, 98600, 98700, 98740, 98760, 98770, 98775, 98777, 98778 — wszystkie przekierowane na slug `sesja-rady-miasta-poznania-brak-danych`. ID dla XXXIII musi być poza tym zakresem (prawdopodobnie 95000–98000 lub niżej).
- **Plan iteracji 2 (po resecie limitu WebFetch lub w kolejnej sesji skill-a)**:
  - Crawl ID-ków sesji XXIX–XXXIII przez próbę slug=`xxix`...`xxxiii` z ID poniżej 98000.
  - Pobrać pełne API JSON dla 5 ostatnich sesji + uzupełnić sekcje (porządek obrad / uchwały / link do protokołu / wyniki głosowań).
  - Crawl sesji 2024 (I–XIII) — alternatywnie UDIP do BoR (`bor@um.poznan.pl`) z wnioskiem o wykaz sesji kadencji IX z ID-kami i datami.
  - Uzupełnić ID DOC uchwał LXII/959 i LXII/960 (otwarcie stron uchwał 50447 i 50448 + wyciąg ID załącznika DOC).
- **Pliki utworzone (24)**: zob. wyżej tabela master w `sesje-plenarne/index.md`.
