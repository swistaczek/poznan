# dabrowskiego/ — kampania ul. Dąbrowskiego (Jeżyce, Poznań)

Pisma wysłane, odpowiedzi urzędów, rejestr sprawy, korespondencja z mieszkańcami, materiały medialne.

## Struktura

```
<obszar>/pisma/        YYYY-MM-DD_ADRESAT_krotki-temat.md
<obszar>/odpowiedzi/   YYYY-MM-DD_ADRESAT_odpowiedz-na-NN.md (+ .pdf oryginałem)
<obszar>/REJESTR.md    tabela chronologiczna
```

Obszary: na razie `halas/`.

**Nazwa pisma**: data wysłania (nie utworzenia!), skrót adresata (`UMP-WOS`, `WIOS`, `MPK`, `ZDM`, `RPO`, `WSA`), slug sprawy.

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
3. Podpis + dane nadawcy (imię, nazwisko, adres — niezbędne dla KPA).
4. Wpis w `REJESTR.md` z terminem odpowiedzi wyliczonym od daty doręczenia.

## Odpowiedzi urzędów

Oryginał PDF + `.md` z transkryptem i notatkami (do przeszukiwania przez Grep). Update `REJESTR.md` — status, data doręczenia.
