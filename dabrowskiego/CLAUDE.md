# dabrowskiego/ — kampania ul. Dąbrowskiego (Jeżyce, Poznań)

Pisma wysłane, odpowiedzi urzędów, rejestr sprawy, korespondencja z mieszkańcami, materiały medialne.

## Struktura

```
<obszar>/pisma/YYYY-MM-DD_temat/    katalog sprawy (LOKALNY, w .gitignore)
  pismo.md / pismo.docx / pismo.pdf   pełne pismo z danymi osobowymi
  email.txt                            treść wiadomości do wklejenia
<obszar>/pisma/REJESTR.md           publiczny rejestr (zsanityzowany)
<obszar>/odpowiedzi/                 odpowiedzi urzędów (LOKALNE PDF/DOCX)
<obszar>/index.md                    publiczny indeks kampanii
```

Obszary: na razie `halas/`.

**Nazwa folderu sprawy**: data wysłania (nie utworzenia!), krótki slug tematu w kebab-case.

**Dane osobowe**: katalogi spraw (`YYYY-MM-DD_*/`) oraz pliki `.docx`, `.pdf`, `email.txt` są ignorowane przez `.gitignore` w root repo. Do repo trafia tylko `REJESTR.md` (zsanityzowany — bez imion, adresów, e-maili) oraz szablon w `szablony/<obszar>/`. Pełna reguła: root `CLAUDE.md` → „Ochrona danych osobowych".

## REJESTR.md (format)

| data | kierunek | adresat | sprawa | termin_KPA | plik | status |

Status: `wyslano` | `doreczono` | `odpowiedziano` | `przeterminowane` | `zamkniete`.

Reguła: wpis w rejestrze **w tej samej godzinie** co wysłanie pisma. Później — zginie w chaosie.

## Styl pism

**Pełny protokół urzędowy.** Ten katalog jest wyjątkiem od zasady „gęsty styl" z root CLAUDE.md.

- Adresat z pełną nazwą i właściwością rzeczową (mapa: `../research/instytucje/wyniki-07-kompetencze-instytucji.md`).
- Podstawa prawna — konkretny art. aktualnej wersji aktu.
- Petitum — jasno wyodrębnione żądanie.
- Termin odpowiedzi (KPA art. 35/237, UDIP 14 dni).
- Klauzula formy doręczenia (ePUAP, e-mail, adres pocztowy).
- Zachowuj zwroty grzecznościowe — mają wartość procesową.

## Przed wysłaniem

1. Podstawa prawna zweryfikowana (ISAP — aktualna wersja).
2. Adresat właściwy (`research/instytucje/`).
3. Podpis + dane nadawcy (imię, nazwisko, adres — niezbędne dla KPA) **w pliku lokalnym**, nie w repo.
4. Wpis w `REJESTR.md` (zsanityzowany) z terminem odpowiedzi wyliczonym od daty doręczenia.
5. `git check-ignore -v <pliki-sprawy>` — potwierdź że pliki z danymi osobowymi są ignorowane przed `git add`.

## Odpowiedzi urzędów

Oryginał PDF + `.md` z transkryptem i notatkami (do przeszukiwania przez Grep). Update `REJESTR.md` — status, data doręczenia.
