# REJESTR pism — pre-audyt przejścia pieszo-rowerowego Jeżyce ↔ Sołacz

Rejestr zsanityzowany (bez danych osobowych). Foldery spraw `YYYY-MM-DD_*/` są lokalne (gitignored).

| data | kierunek | adresat | sprawa | termin | plik | status |
|---|---|---|---|---|---|---|
| 2026-05-29 | wychodzące | WGN UMP | własność działek nasypu (rejon Poleska/św. Wawrzyńca) | UDIP 14 dni | `2026-05-29_WGN_wlasnosc-dzialek/` | szkic gotowy |
| 2026-05-29 | wychodzące | ZDM + PIM | tunel w WPF / planach inwestycyjnych, harmonogram | UDIP 14 dni | `2026-05-29_ZDM-PIM_wpf-plany/` | szkic gotowy |
| 2026-05-29 | wychodzące | PKP PLK Zakład Poznań | prędkość linii, status dokumentacji, zgoda/warunki | bez ustawowego terminu | `2026-05-29_PKP-PLK_warunki-przejscia/` | szkic gotowy |

## Korespondencja z UMP (BKPiRM), znak KPRM-XIII.7226.5.16.2026

Szczegóły i cytaty: [`../../../research/planowanie-przestrzenne/jezyce/bariera-kolejowa-351-przejscia.md`](../../../research/planowanie-przestrzenne/jezyce/bariera-kolejowa-351-przejscia.md), sekcja „Stan uzgodnień z UMP, wrzesień 2026".

| data | kierunek | adresat / nadawca | sprawa | status |
|---|---|---|---|---|
| 2026-08-27 | przychodzące | UMP BKPiRM, nr rej. 27082603575 | odpowiedź na pisma z 27.07 i 10.08.2026: przejście Poleska w umowie PKP PLK z BBF od 29.05.2026; ZDM: wniosek zasadny | odpowiedziano |
| 2026-08-27 | wychodzące | UMP BKPiRM | 2 pytania uzupełniające (termin i jednostka uzgodnienia; układ wiaduktu Kościelna) | wyslano |
| 2026-08-28 | przychodzące | UMP BKPiRM, nr rej. 28082600810 | uzgodnienia koncepcji PWK od 06.2025; koordynacja BKPiRM; konsultacje z mieszkańcami po stronie PKP PLK | odpowiedziano |
| 2026-09-04 | wychodzące | UMP BKPiRM | prośba o kwartał/rok przekazania rozwiązań Poleskiej; informacja o układzie wiaduktu Kościelna | wyslano |
| 2026-09-22 | przychodzące | UMP BKPiRM, nr rej. 22092602884 | terminy Poleskiej Miastu nieznane, pytania do PKP PLK; Kościelna: ruch pieszy i rowerowy odseparowany od jezdni | odpowiedziano |
| 2026-09-23 | wychodzące | UMP BKPiRM | podziękowanie, utrwalenie deklaracji ws. Kościelnej, zapowiedź zapytania do PKP PLK | szkic gotowy (niewysłany) |
| do ustalenia | wychodzące | PKP PLK S.A., al. Niepodległości 8, Poznań | harmonogram projektów dla przejścia Poleska; najpierw odczytać pismo PKP PLK z 04.08.2026 (IRRK5/13/2.2233.205.2026.IRE-03590-I.1) | do przygotowania |

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
