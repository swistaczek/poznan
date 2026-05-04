# golecin/ — kampania ws. MPZP „Park Golęcin" (Zachodni Klin Zieleni, Poznań)

Pisma do organów planistycznych, rejestr sprawy, materiały kampanii dotyczącej procedowanego miejscowego planu zagospodarowania przestrzennego „Park Golęcin" (uchwała inicjująca: Nr XLIX/639/V/2009 RMP z 10 lutego 2009 r.).

## Kontekst

Procedura w fazie II wyłożenia (27.03.2026 – 20.04.2026), termin składania uwag w trybie art. 8g ustawy z 27 marca 2003 r. o planowaniu i zagospodarowaniu przestrzennym (Dz.U. 2023 poz. 977 ze zm.) **upływa 4 maja 2026 r.**

Materiał referencyjny: [`research/planowanie-przestrzenne/mpzp-park-golecin-analiza.md`](../research/planowanie-przestrzenne/mpzp-park-golecin-analiza.md), [`research/planowanie-przestrzenne/petycja-sportowy-golecin.md`](../research/planowanie-przestrzenne/petycja-sportowy-golecin.md).

## Struktura

```
planowanie-przestrzenne/
  pisma/REJESTR.md                 publiczny rejestr (zsanityzowany)
  pisma/YYYY-MM-DD_temat/          katalog sprawy (LOKALNY, w .gitignore)
    pismo.md / pismo.docx / pismo.pdf
    email.txt
  odpowiedzi/                      odpowiedzi MPU/UMP (LOKALNE)
  wniosek-uwagi-mpzp.md            wzór z placeholderami {{...}} (PUBLICZNY)
index.md                           publiczny indeks kampanii
```

Nazwa folderu sprawy: `YYYY-MM-DD_ADRESAT_slug-tematu` w kebab-case. Data wysłania, nie utworzenia.

## Dane osobowe

Katalogi spraw `YYYY-MM-DD_*/` oraz pliki `.docx`, `.pdf`, `email.txt` są ignorowane przez `.gitignore` w root repo. **Wzór `wniosek-uwagi-mpzp.md` poza katalogiem `pisma/` zawiera placeholdery `{{...}}`** — można reużywać bez ryzyka ujawnienia danych. Wypełniony wniosek (z imieniem, adresem, sygnaturami pism własnych) trafia wyłącznie do lokalnego folderu `pisma/2026-05-04_*/` lub równoważnego.

Pełna reguła: root [`CLAUDE.md`](../CLAUDE.md) → sekcja „Ochrona danych osobowych".

## Adresat

**Miejska Pracownia Urbanistyczna w Poznaniu**
ul. Za Bramką 1, 61-842 Poznań
e-mail: mpu@poznan.mpu.pl
ePUAP: [do uzupełnienia w wzorze pisma]

Forma uwagi: na ustawowym formularzu „Pismo dotyczące aktu planowania przestrzennego" (rozporządzenie wykonawcze do art. 8g UPZP) — wzór w [`research/planowanie-przestrzenne/przyklad-wniosku-uwagi-do-mpzp.pdf`](../research/planowanie-przestrzenne/przyklad-wniosku-uwagi-do-mpzp.pdf).

## REJESTR.md (format)

| data | kierunek | adresat | sprawa | termin_KPA | plik | status |

Status: `wyslano` | `doreczono` | `odpowiedziano` | `przeterminowane` | `zamkniete`.

## Styl pism

**Pełny protokół urzędowy** — wyjątek od „gęsty styl" z root CLAUDE.md.
- Adresat z pełną nazwą i właściwością rzeczową.
- Podstawa prawna konkretnie (art. + Dz.U. aktualnej wersji).
- Petitum każdej uwagi wyodrębnione i jednoznaczne.
- Sygnatury orzeczeń i uchwał Rady Miasta — tylko zweryfikowane; niepewne `[do weryfikacji]`.
- Klauzula formy doręczenia (e-mail / ePUAP / poczta).

## Przed wysłaniem

1. Zweryfikuj aktualność sygnatur Dz.U. (ISAP).
2. Wpisz dane nadawcy w pliku lokalnym sprawy (NIE w repo).
3. Wpis w `REJESTR.md` (zsanityzowany).
4. `git check-ignore -v <pliki-sprawy>` — potwierdź ignorowanie plików z danymi osobowymi.
