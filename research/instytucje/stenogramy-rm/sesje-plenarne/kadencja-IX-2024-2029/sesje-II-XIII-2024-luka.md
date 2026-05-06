---
typ: stub-luka-informacyjna
zakres: sesje II–XIII kadencji IX RM Poznania
rok: 2024
od_daty: 2024-04-25 (po sesji inauguracyjnej I)
do_daty: 2024-12-31
liczba_sesji_szacunkowa: 12
status: luka_do_uzupelnienia_iteracja_2
data_pobrania: 2026-05-06
---

# Sesje II–XIII RM Poznania (2024) — luka informacyjna

## Stan rzeczy

Bootstrap skill-a `aktualizuj-stenogramy-rm` w runie 2026-05-06 (sub-agent A) napotkał ograniczenie:

1. **BIP Poznania nie publikuje harmonogramu sesji 2024** w lokalizacji `/bip/ramowy-harmonogram-sesji,doc,1616/` (gdzie znajdują się harmonogramy 2025 i 2026).
2. **Strona listingu sesji `/bip/sesje/`** renderuje listę dynamicznie (przez JavaScript) — WebFetch widzi tylko najbliższą sesję XXXIV (12.05.2026), nie historyczne.
3. **Limit WebFetch wyczerpany** w trakcie crawlu (godz. ~10:35 CEST 2026-05-06, reset 13:10) — nie udało się wyszukać ID sesji binarnym przeszukaniem zakresu ID 87000–98000.

## Wyliczenie liczby sesji 2024

XXXIV = 5. sesja 2026 (12.05.2026)
- Sesje 2026 do XXXIV: 5 (XXX, XXXI, XXXII, XXXIII, XXXIV)
- Sesje 2025 z harmonogramu: 16 (XIV–XXIX)
- Sesje 2024: **34 − 16 − 5 = 13** (I–XIII)

Sesja I = 24.04.2024 (inauguracyjna). Sesje II–XIII odbyły się od 25.04.2024 do 17.12.2024 (typowo grudniowa = budżetowa).

## Plan iteracji 2

1. Po resecie limitu WebFetch (2026-05-06 ~13:10):
   - Crawl `/bip/sesje/sesja-rady-miasta-poznania,{ID}/` przez ID 87000, 87500, 88000, 88500, 89000, … aż znajdziemy sesję z prawdziwym slugiem (np. "ii", "iii", "iv"…).
   - Z otrzymanego slug+ID skonstruuj URL API JSON i pobierz pełne metadane.
   - Powtórz dla wszystkich 13 sesji.
2. **Alternatywa**: UDIP (art. 13 ust. 1 ustawy o dostępie do informacji publicznej) do Biura Rady Miasta — wniosek o "wykaz sesji RM Poznania kadencji IX (24.04.2024 – do dziś) z numerami, datami, ID BIP, linkami do protokołów". Zwykle BoR odpowiada w 14 dni listą Excel/PDF.
3. **Alternatywa 2**: Pobranie przez różne klucze SEO — Google search "site:bip.poznan.pl sesja II 2024" zwykle zwraca konkretne URL-e BIP z ID-ami.

## Sesje typowo zdarzające się w 2024 (kalendarzowo prawdopodobne)

| Numer (szacunkowy) | Data (szacunkowa) | Charakter |
|---|---|---|
| I | 2024-04-24 | inauguracyjna ✓ (potwierdzona) |
| II | 2024-05-07 lub 14 | zwyczajna |
| III | 2024-05-28 lub 06-04 | zwyczajna |
| IV | 2024-06-18 | absolutoryjna (za 2023) |
| V | 2024-06-29 | uroczysta? (rocznica 1956) |
| VI | 2024-07 | wakacyjna lub pominięta |
| VII | 2024-09 | zwyczajna pierwsza po wakacjach |
| VIII | 2024-09-24 lub 10-01 | zwyczajna |
| IX | 2024-10-15 | zwyczajna |
| X | 2024-11-05 | zwyczajna |
| XI | 2024-11-19 | budżet 2025 — pierwsze czytanie |
| XII | 2024-12-03 | zwyczajna |
| XIII | 2024-12-17 lub 19 | budżetowa (uchwalenie budżetu 2025) |

> **Uwaga**: powyższa tabela jest **rekonstrukcją kalendarzową** typowego rytmu RM Poznania (3-tygodniowe odstępy, rytm 17/18.06 absolutorium + 17/19.12 budżet). Faktyczne daty potwierdzane w iteracji 2 z BIP.

## Powiązania

- [`./sesja-I-2024-04-24.md`](./sesja-I-2024-04-24.md) — jedyna sesja 2024 z konkretnym stubem
- [`./sesja-XIV-2025-01-17.md`](./sesja-XIV-2025-01-17.md) — pierwsza sesja 2025 (od niej harmonogram dostępny)
- [`./index.md`](./index.md) — indeks kadencji IX z listą sesji

## Status

Pliki indywidualne `sesja-II-2024-XX-XX.md` ... `sesja-XIII-2024-XX-XX.md` **nie zostały utworzone** w runie 1, ponieważ:
- nie znamy dokładnych dat,
- tworzenie 12 stubów z niepoprawnymi datami w nazwie pliku byłoby niezgodne z konwencją skill-a (`sesja-{numer}-{YYYY-MM-DD}.md` wymaga prawdziwej daty).

W iteracji 2: po pobraniu prawdziwych dat z BIP — dopisać stuby z poprawnymi nazwami plików, usunąć niniejszy stub-lukę.
