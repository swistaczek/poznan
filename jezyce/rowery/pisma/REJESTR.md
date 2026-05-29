# REJESTR pism — pre-audyt przejścia pieszo-rowerowego Jeżyce ↔ Sołacz

Rejestr zsanityzowany (bez danych osobowych). Foldery spraw `YYYY-MM-DD_*/` są lokalne (gitignored).

| data | kierunek | adresat | sprawa | termin | plik | status |
|---|---|---|---|---|---|---|
| 2026-05-29 | wychodzące | WGN UMP | własność działek nasypu (rejon Poleska/św. Wawrzyńca) | UDIP 14 dni | `2026-05-29_WGN_wlasnosc-dzialek/` | szkic gotowy |
| 2026-05-29 | wychodzące | ZDM + PIM | tunel w WPF / planach inwestycyjnych, harmonogram | UDIP 14 dni | `2026-05-29_ZDM-PIM_wpf-plany/` | szkic gotowy |
| 2026-05-29 | wychodzące | PKP PLK Zakład Poznań | prędkość linii, status dokumentacji, zgoda/warunki | bez ustawowego terminu | `2026-05-29_PKP-PLK_warunki-przejscia/` | szkic gotowy |

Status: `szkic gotowy` | `do wysłania` | `wyslano` | `doreczono` | `odpowiedziano` | `przeterminowane` | `zamkniete`.

> Szkice wypełnione w folderach lokalnych (gitignored). **Przed wysłaniem**: uzupełnij dane nadawcy ({{IMIE_NAZWISKO}}, {{ADRES}}, {{EMAIL}}), nr działek z SIP Poznań, adres Zakładu PKP PLK. Zmień status na `wyslano` + datę.

## Szablony do użycia

- WGN (własność) i ZDM/PIM (WPF/plany): [`../../../szablony/pbo/wniosek-udip-plan-inwestycji.md`](../../../szablony/pbo/wniosek-udip-plan-inwestycji.md) — dla WGN dostosuj petitum do zapytania o status własności i władania działkami (nr działek z SIP Poznań).
- PKP PLK: [`../../../szablony/pbo/wniosek-pkp-plk-zgoda-przejscie.md`](../../../szablony/pbo/wniosek-pkp-plk-zgoda-przejscie.md).

## Procedura

1. `cp szablony/... jezyce/rowery/pisma/YYYY-MM-DD_ADRESAT_temat/pismo.md`
2. Wypełnij pola `{{...}}` (dane nadawcy TYLKO w pliku lokalnym).
3. `git check-ignore -v jezyce/rowery/pisma/YYYY-MM-DD_*/pismo.md` — potwierdź ignorowanie.
4. Wpis zsanityzowany w tym rejestrze; zmień status na `wyslano`.

## Cel pre-audytu

Rozstrzygnąć przed zgłoszeniem do PBO28 dwa „killery": (1) własność gruntu (WGN/PKP), (2) kolizja z inwestycją w toku/WPF (ZDM/PIM/PKP). Zob. [`../../../research/planowanie-przestrzenne/jezyce/precedensy-pbo-kladki-tory.md`](../../../research/planowanie-przestrzenne/jezyce/precedensy-pbo-kladki-tory.md).
