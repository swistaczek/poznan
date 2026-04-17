# poznan — inicjatywy obywatelskie

Baza wiedzy, szablonów pism i kampanii dla mieszkańców Poznania: hałas tramwajowy, rowery, uspokojenie ruchu, transparentność (UDIP), kompetencje organów, jakość życia.

> [!TIP]
> **Nie musisz umieć programować.** Całość jest dostępna jako zwykła strona z wyszukiwarką: **https://swistaczek.github.io/poznan/**

Repo obsługuje dwie grupy:

- **Mieszkańcy i aktywiści** — czytają stronę w przeglądarce, kopiują szablony pism, sprawdzają terminy i adresatów.
- **Kontrybutorzy** — klonują repo, używają [Claude Code](https://claude.ai/code) do generowania pism, prowadzenia researchu i obsługi kampanii.

Wybierz swoją ścieżkę poniżej.

---

## 🏛️ Jestem mieszkańcem / aktywistą

### 1. Znajdź swój temat

[**INDEKS.md**](./INDEKS.md) to mapa całego repo. Wybierasz obszar (hałas, rowery, uspokojenie ruchu, transparentność, instytucje) i wchodzisz w `_index.md` — dostajesz uporządkowany zestaw źródeł i szablonów.

Obszary aktualnie pokryte:

| Obszar | Po co |
|---|---|
| `research/halas/` | hałas tramwajowy i drogowy — normy, pomiary, immisje cywilne, zdrowie |
| `research/uspokojenie-ruchu/` | Tempo 30, woonerfy, fizyczne interwencje |
| `research/rowery/` | polityka rowerowa Poznania, audyt CROW |
| `research/transparentnosc/` | UDIP, skargi na bezczynność, dostęp do danych |
| `research/instytucje/` | kto za co odpowiada (mapa kompetencji) |

### 2. 📝 Napisz pismo z gotowego szablonu

Szablony są w [`szablony/`](./szablony/) podzielone na obszary. Przykład — chcesz złożyć wniosek o informację publiczną (UDIP):

1. Wejdź do [`szablony/transparentnosc/`](./szablony/transparentnosc/).
2. Wybierz wzór (np. `wniosek-udip-podstawowy.md`).
3. Skopiuj treść, wypełnij pola `{{IMIE_NAZWISKO}}`, `{{ADRES}}`, `{{DATA}}`, `{{ADRESAT}}`, `{{PRZEDMIOT_SPRAWY}}`.
4. Wyślij e-mailem lub przez ePUAP (adresy niżej).

Lista szablonów rośnie — jeśli brakuje ci wzoru pod konkretną sprawę, załóż [issue](https://github.com/swistaczek/poznan/issues) albo zobacz ścieżkę kontrybutora niżej.

### 3. Dowiedz się, do kogo pisać

- [**ADRESY.md**](./ADRESY.md) — szybka tabela: UMP, ZDM, MPK, WIOŚ, RDOŚ, Wojewoda, sądy, RPO.
- [**research/instytucje/\_index.md**](./research/instytucje/_index.md) — pełna mapa kompetencji (kto jest właściwy rzeczowo i miejscowo — kluczowe, bo niewłaściwy adresat = miesiące zwłoki).

> [!WARNING]
> Pozycje z markerem `[do weryfikacji]` w ADRESY.md wymagają sprawdzenia w BIP przed wysyłką — sprawdź adres, skrytkę ePUAP i datę aktualności.

### 4. Sprawdź terminy

[**TERMINY.md**](./TERMINY.md) — tabela procesowa: UDIP (14 dni), KPA (1–2 miesiące), skarga do WSA (30 dni), wniosek o uzasadnienie wyroku (**7 dni** — krytyczny termin), apelacja cywilna, petycje.

### 5. Sprawdź aktywne kampanie

| Kampania | Obszar |
|---|---|
| [`dabrowskiego/`](./dabrowskiego/) | ul. Dąbrowskiego (Jeżyce) — hałas tramwajowy |

Każda kampania ma własny `REJESTR.md` z listą pism wysłanych i odpowiedzi — możesz zobaczyć, co już poszło, i podpiąć się ze swoim adresem w treści.

### 6. Jak pomóc bez technicznych kompetencji

- **Linkuj** konkretne strony ([publiczna wersja](https://swistaczek.github.io/poznan/)) w mediach społecznościowych, prasie, rozmowach z radnymi — każda strona ma stabilny URL.
- **Edytuj przez przeglądarkę** — na stronie publicznej, u góry każdego artykułu jest ikona ołówka, która otwiera plik w edytorze GitHuba (wymaga darmowego konta).
- **Zgłoś** brakujący temat, błąd lub nowe źródło przez [GitHub Issues](https://github.com/swistaczek/poznan/issues).
- **Wyślij** pismo wzorowane na szablonie i **wróć z odpowiedzią organu** — zasilamy bazę precedensami i orzecznictwem.

**Kontakt:** `[do uzupełnienia]` (Discord/Signal/e-mail koordynatora).

---

## 💻 Jestem kontrybutorem / deweloperem

### 1. Zainstaluj Claude Code

[Claude Code](https://claude.ai/code) to CLI asystent AI od Anthropic, który czyta pliki w repo, rozumie lokalne konwencje (ten repo ma `CLAUDE.md` z regułami pisania pism) i generuje treść zgodną z nimi. W praktyce: mówisz „wygeneruj wniosek UDIP do MPK o protokoły odbioru torowiska" — Claude Code znajduje odpowiedni szablon, wypełnia pola, dodaje podstawę prawną, zaznacza pola do weryfikacji.

> [!NOTE]
> **Komendy instalacyjne zmieniają się** — zamiast kopiować z tego README, sprawdź oficjalne źródła:
>
> - **Strona produktu:** https://claude.ai/code
> - **Dokumentacja:** https://docs.claude.com/
>
> Zazwyczaj wymaga konta Anthropic i Node.js. Sprawdź aktualny install-flow w docs.

### 2. Sklonuj repo i otwórz w Claude Code

```bash
git clone https://github.com/swistaczek/poznan.git
cd poznan
claude          # uruchom Claude Code w tym katalogu
```

Claude Code automatycznie wczyta [`CLAUDE.md`](./CLAUDE.md) (konwencje) oraz nested `CLAUDE.md` w podkatalogach (lokalne reguły dla `szablony/`, `research/`, `dabrowskiego/`).

### 3. Co Claude Code potrafi w tym repo

- **Generuje pisma** — bierze szablon z `szablony/<obszar>/`, wypełnia, zapisuje w `<kampania>/<obszar>/pisma/YYYY-MM-DD_ADRESAT_temat.md`, dopisuje do `REJESTR.md`.
- **Wyciąga fakty z researchu** — `research/<obszar>/wyniki-*.md` to 40–80 KB gęstego tekstu; Claude Code Grepuje po sygnaturach orzeczeń, art. ustaw, datach.
- **Weryfikuje spójność** — sprawdza czy adresat jest właściwy rzeczowo (mapa w `research/instytucje/`), czy termin zgadza się z KPA/UDIP, czy podstawa prawna cytowana precyzyjnie.
- **Prowadzi panel ekspertów** (patrz sekcja niżej) przed decyzjami strategicznymi.

### 4. Dodaj nową kampanię

```
<miejsce>/
  CLAUDE.md              # lokalne reguły (krótkie — tylko specyfika miejsca)
  <obszar>/
    REJESTR.md           # dziennik pism wysłanych i odpowiedzi
    pisma/               # kopie szablonów z wypełnionymi polami
    odpowiedzi/          # skany/PDFy/transkrypty odpowiedzi organów
```

Wypełnianie szablonów: zobacz [`szablony/CLAUDE.md`](./szablony/CLAUDE.md) — zasada „jedno źródło prawdy", kopia do kampanii z frontmatterem `type: sent`.

### 5. Dodaj nowy research

1. Napisz brief eksperta w [`research/prompty/NN-<obszar>.md`](./research/prompty/) — persona top 1%, zakres, „czego NIE chcemy".
2. Uruchom eksperta (Claude Code z Agent tool albo zewnętrzny LLM).
3. Zapisz wynik w `research/<obszar>/wyniki-NN-<temat>.md`. Pamiętaj o limicie pliku (cel ≤ 12 KB, twardy limit ~40 KB — patrz [`CLAUDE.md`](./CLAUDE.md)).
4. Dodaj wpis do `research/<obszar>/_index.md`.

### 6. Lokalny podgląd strony (opcjonalne)

Strona publikowana automatycznie z `main` przez GitHub Actions ([`.github/workflows/gh-pages.yml`](./.github/workflows/gh-pages.yml)). Do lokalnego podglądu:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve    # http://127.0.0.1:8000/poznan/
```

Szczegóły (build strict, troubleshooting, rozszerzenia): [`docs-local.md`](./docs-local.md).

Stos: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) + pluginy `search` (PL stemmer) i `awesome-pages`. Konfiguracja w [`mkdocs.yml`](./mkdocs.yml).

---

## Struktura repo (high-level)

```
research/<obszar>/          wiedza referencyjna, reużywalna między kampaniami
research/prompty/           briefy 01–NN dla ekspertów (persona + zakres)
szablony/<obszar>/          wzory pism (jedno źródło prawdy)
<kampania>/<obszar>/        konkretna sprawa (np. dabrowskiego/halas/)
ADRESY.md                   adresaci organów
TERMINY.md                  terminy KPA / UDIP / p.p.s.a. / KPC
INDEKS.md                   mapa nawigacyjna
CLAUDE.md                   konwencje dla Claude Code
mkdocs.yml, .pages, *.md    konfiguracja strony publicznej
```

Pełne drzewo z linkami: [`INDEKS.md`](./INDEKS.md).

---

## Konwencje (skrót)

Pełna wersja: [`CLAUDE.md`](./CLAUDE.md). W dwóch zdaniach:

- **Wszystko po polsku** (treść, commity, nazwy plików); **nazwy plików w kebab-case bez polskich znaków i spacji**.
- **Dokumenty źródłowe** (`research/`, notatki) — gęsty styl, fakty, liczby, sygnatury; **pisma urzędowe** (`<kampania>/pisma/`) — pełny protokół urzędowy (zwroty grzecznościowe mają wartość procesową).
- Każdy podkatalog może mieć własny `CLAUDE.md` z lokalnymi regułami.
- Cytuj akty prawne dokładnie: akt, Dz.U., art./§/ust., data wersji.

---

## Panel ekspertów

Przy strategicznych decyzjach (np. wybór strategii procesowej, treść pisma wysokostawkowego) Claude Code uruchamia równolegle 4–6 sub-agentów w rolach top 1% ekspertów — prawo administracyjne, akustyka, zdrowie publiczne, urbanistyka, UDIP — i syntetyzuje wnioski. Persony w [`research/prompty/`](./research/prompty/). Kryterium użycia: „gdyby rekomendacja okazała się błędna, koszt > kilka minut korekty". Szczegóły: sekcja „Panel ekspertów" w [`CLAUDE.md`](./CLAUDE.md).

---

## Licencja

> [!NOTE]
> **Propozycja — do potwierdzenia przez maintainera:**
>
> - **Treść** (research, szablony, analizy): [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pl) — wolno kopiować i adaptować pod warunkiem przypisania autorstwa i zachowania licencji.
> - **Kod konfiguracyjny** (MkDocs, GitHub Actions, skrypty): [MIT](https://opensource.org/licenses/MIT).
>
> Do czasu dodania pliku `LICENSE` w repo — traktuj materiały jako **referencyjne, nie stanowią porady prawnej**. W sprawach wysokostawkowych skonsultuj radcę prawnego lub rzeczoznawcę.

---

## Kontakt i kredyty

- **Maintainer:** [@swistaczek](https://github.com/swistaczek) (GitHub).
- **Kanały komunikacji:** `[do uzupełnienia]` — Discord / Signal / e-mail koordynatora.
- **Zgłoszenia:** [GitHub Issues](https://github.com/swistaczek/poznan/issues).

Kontrybucje (każda forma — tekst, korekta, weryfikacja adresów, opowiedzenie o sprawie) mile widziane.
