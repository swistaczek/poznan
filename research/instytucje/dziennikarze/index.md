# Baza dziennikarzy zaangażowanych w sprawy poznańskie 2022–2026

Wynik briefu deep research [`research/prompty/20-dziennikarze-poznanscy.md`](../../prompty/20-dziennikarze-poznanscy.md), uruchomionego 2026-05-06. Zawiera 26 sprofilowanych dziennikarzy z udokumentowanym śladem autorskim w sprawach Poznania (transport, spółki miejskie, kominy, urbanistyka, środowisko, rowery, korupcja JST, aktywizm).

> **AI-disclaimer.** Niniejsza baza jest wynikiem deep research generowanego przez model językowy (Gemini Deep Research / równoważny). Z dużą szansą zawiera **błędy faktograficzne, nieaktualne dane personalne, halucynowane URL i e-maile, mylne atrybucje artykułów**. Każdy fakt cytowany dalej (e-mail służbowy, profil X, lista artykułów) **wymaga niezależnej weryfikacji** w stopkach redakcyjnych, archiwach mediów (`web.archive.org`) oraz przez bezpośredni kontakt redakcji. Ranking „Top 10 / Top 5" — opinie LLM, nie fakty. Korekty zgłaszaj przez Issues.

## Punkty wejścia

| Sekcja | Zawartość | Wejście |
|---|---|---|
| Surowy raport (110 KB) | wszystkie 26 profili + tabela master + indeksy + Top 10/5 + luki | [`wyniki-20-dziennikarze-poznanscy.md`](./wyniki-20-dziennikarze-poznanscy.md) |
| Brief źródłowy | prompt deep research uruchomiony 2026-05-06 | [`../../prompty/20-dziennikarze-poznanscy.md`](../../prompty/20-dziennikarze-poznanscy.md) |

## Sekcje surowego raportu (linki bezpośrednie)

- [Metoda i źródła](./wyniki-20-dziennikarze-poznanscy.md#metoda-i-źródła)
- [Tabela master (indeks)](./wyniki-20-dziennikarze-poznanscy.md#tabela-master-indeks)
- [Profile pełne (alfabetycznie po nazwisku)](./wyniki-20-dziennikarze-poznanscy.md#profile-pełne-alfabetycznie-po-nazwisku)
- [Luki operacyjne rynku i kierunki przyszłego researchu](./wyniki-20-dziennikarze-poznanscy.md#luki-operacyjne-rynku-i-konieczne-kierunki-przyszłego-dalszego-researchu-miejskiego)

## Pierwsze 4 dziennikarze z tabeli master (sample)

| # | Imię i nazwisko | Aktualne medium | Specjalizacja | Top temat 2024–2026 | Stosunek do UMP | Kanał kontaktu |
|---|---|---|---|---|---|---|
| 1 | Blanka Aleksowska | Głos Wielkopolski | Śledztwa, sprawy społeczne | Nieprawidłowości instytucjonalne | Krytyczny | E-mail służbowy |
| 2 | Maria Bielicka | Gazeta Wyborcza Poznań | Inwestycje drogowe, infrastruktura | Mosty Berdychowskie, PIM | Niuansowany | E-mail służbowy |
| 3 | Piotr Bojarski | Wydawnictwo Miejskie Posnania | Dziedzictwo, urbanistyka | Historia i rewitalizacja centrum | Neutralny | LinkedIn |
| 4 | Mateusz Chłystun | Radio Eska / ZPR Media | Zdrowie, incydenty, służby | Paraliż SOR, wypadki | Neutralny | DM X (Twitter) |

Pełna lista 26 — w surowym raporcie: [`wyniki-20-dziennikarze-poznanscy.md`](./wyniki-20-dziennikarze-poznanscy.md).

## Jak korzystać z bazy operacyjnie

Trzy cele praktyczne (z prompta źródłowego):

1. **Komu wysyłać sygnały** o nowych sprawach obywatelskich — sekcja „Top 10 gotowi" w surowym raporcie + per-temat wyciąg z profili pełnych.
2. **Komu proponować materiały ekskluzywne** (zwroty UDIP, dokumenty) — dziennikarze z notą „reagował_na_sygnal_obywatelski: tak" oraz „preferowany_kanal_zaczepienia".
3. **Komu udzielać wywiadów** — pole „ryzyko_redakcyjne" filtruje klakierów / nadinterpretatorów.

Zanim zaczepisz dziennikarza:
- Otwórz **2–3 reprezentatywne artykuły** z jego profilu (są URL-e w surowym raporcie). Zweryfikuj że nadal istnieją.
- Sprawdź jego ostatni miesiąc na X (sygnał aktywności).
- Jeśli e-mail służbowy z bazy nie odpowiada — sprawdź formatkę redakcji (Polska Press: `imie.nazwisko@polskapress.pl`; Agora: `imie.nazwisko@agora.pl`; itd.).

## Iteracja 2 — chunking per-osoba i per-temat

Surowy raport jest monolitem 110 KB. Plan rozbicia na chunki ≤ 12 KB (zgodnie z `research/CLAUDE.md`):

- `01-transport-publiczny.md` — dziennikarze MPK/PIM/inwestycji drogowych (Bielicka, Czekała, Majchrzak częściowo)
- `02-spolki-miejskie-kominy.md` — afera kominów IV.2026 (Czekała TVN24, Majchrzak Radio Poznań, Codzienny Poznań)
- `03-srodowisko-halas.md` — hałas, smog, immisje
- `04-rowery-mobilnosc.md` — polityka rowerowa
- `05-urbanistyka-mpzp.md` — MPZP, Studium, dziedzictwo (Bojarski Posnania)
- `06-aktywizm-rady-osiedli.md` — ruchy społeczne, partycypacja
- `07-korupcja-nik-cba.md` — śledcza krytyka JST (Aleksowska)
- `08-medialny-mainstream-poznanski.md` — pozostali
- `99-faq.md` — 12-15 pytań aktywisty

**Status**: do wykonania w kolejnym runie. Wymaga przepracowania sekcji „Profile pełne" (narracyjna, bez czystych H3 per osoba) na 26 dyskretnych bloków + klasyfikacji tematycznej.

## Powiązania

- [`../../prompty/20-dziennikarze-poznanscy.md`](../../prompty/20-dziennikarze-poznanscy.md) — brief deep research
- [`../pim-siec-powiazan-kominy-placowe.md`](../pim-siec-powiazan-kominy-placowe.md) — kontekst sprawy kominów
- [`../prezes-pim-litka-werdykt-zbiorczy.md`](../prezes-pim-litka-werdykt-zbiorczy.md) — teorie T1–T9
- [`../nowe-teorie-2026-05-06.md`](../nowe-teorie-2026-05-06.md) — teorie T10–T14 (w tym T13 niesymetryczne KPI Mostów — temat dla dziennikarzy infrastrukturalnych)
- [`../inwestycja-mosty-berdychowskie.md`](../inwestycja-mosty-berdychowskie.md) — studium 28→156 mln (temat dla Bielickiej)
