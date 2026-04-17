# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Czym jest to repo

Repozytorium gromadzi materiały i inicjatywy obywatelskie dotyczące **miasta Poznania** — w szczególności:

- jakości życia mieszkańców,
- ścieżek rowerowych i mobilności aktywnej,
- norm hałasu (drogowego, tramwajowego, kolejowego),
- uspokojenia ruchu (traffic calming, strefy Tempo 30, woonerfy),
- transparentności działania władz miasta, spółek miejskich i ZTM/MPK.

To **nie jest projekt programistyczny** — nie ma kodu źródłowego, buildów, testów ani zależności. Treścią są dokumenty (`.md`, `.pdf`), studia prawno-techniczne, pisma, notatki, dane i linki do źródeł.

## Język

**Wszystkie odpowiedzi, commit messages, nazwy plików i treść dokumentów — po polsku.** Dotyczy to też komentarzy, opisów PR-ów i podsumowań. Terminologia prawna i techniczna powinna być zgodna z polskim porządkiem prawnym (nie tłumaczymy np. "rozporządzenia" jako "regulation" w tekście).

## Struktura katalogów

Konwencja jest dwupoziomowa:

```
<inicjatywa-lub-lokalizacja>/<obszar-problemowy>/
research/<obszar-problemowy>/
```

- **`<inicjatywa>/`** (np. `dabrowskiego/`) — konkretna kampania, ulica, osiedle lub projekt obywatelski. Trzyma pisma, wnioski, interwencje, korespondencję z urzędami.
- **`research/`** — materiały źródłowe przekrojowe: studia prawne, regulacje, analizy, dane pomiarowe, opracowania eksperckie. Nie są związane z jedną kampanią — stanowią bazę wiedzy reużywalną między inicjatywami.
- **`<obszar-problemowy>/`** (np. `halas/`, `rowery/`, `uspokojenie-ruchu/`, `transparentnosc/`) — kategoria tematyczna wspólna dla `research/` i katalogów inicjatyw.

Tworząc nowy materiał: najpierw rozstrzygnij, czy to ogólna wiedza (→ `research/`), czy działanie w konkretnej sprawie (→ `<inicjatywa>/`).

## Styl pracy z dokumentami

- **Cytuj źródła prawne dokładnie** — numer aktu, dziennik ustaw, artykuł/paragraf/ustęp. Dla aktów zmienianych — wersja aktualna na dzień pisania (podaj datę).
- **Rozróżniaj fakty od postulatów.** W piśmie do urzędu: stan prawny i stan faktyczny osobno od żądania/wniosku.
- **Nie zmyślaj danych pomiarowych, numerów interwencji, dat posiedzeń rady.** Jeśli brak źródła — zaznacz `[do weryfikacji]` zamiast wstawiać prawdopodobną wartość.
- **Zachowuj oryginalne nazwy instytucji** (ZDM, MPK Poznań sp. z o.o., GIOŚ, WIOŚ, RDOŚ, Rada Miasta Poznania, jednostki pomocnicze — rady osiedli).

## Pisanie pism urzędowych

Gdy generujesz pismo, wniosek, skargę lub interpelację:

1. Ustal **podstawę prawną** (konkretny artykuł) — nie ogólnikowe "zgodnie z przepisami".
2. Określ **adresata właściwego rzeczowo i miejscowo** — nie pisz do Prezydenta, gdy sprawa leży w kompetencji zarządcy drogi lub spółki komunalnej.
3. Wskaż **termin** wynikający z KPA (art. 35, 237) lub ustawy o dostępie do informacji publicznej (14 dni).
4. Dodaj **klauzulę o sposobie doręczenia odpowiedzi** (ePUAP, e-mail, adres pocztowy).

## Transparentność i dane publiczne

Preferowane źródła danych o Poznaniu (gdy potrzebujesz faktu, a nie masz go w repo):

- BIP Miasta Poznania (bip.poznan.pl) — uchwały, zarządzenia, budżet, oświadczenia majątkowe.
- System Informacji Przestrzennej Poznania (sip.poznan.pl) — MPZP, warunki zabudowy.
- Rejestr umów, rejestr petycji, rejestr interpelacji.
- Wnioski o informację publiczną (14 dni, forma pisemna lub elektroniczna).

Jeśli cytujesz dane z tych źródeł — zapisuj URL **i** datę dostępu; treść BIP-u potrafi zniknąć po kadencji.

## Czego NIE robić

- Nie zakładaj struktury projektu kodowego (nie twórz `package.json`, `.gitignore` dla `node_modules`, CI, itp.) — to repo dokumentowe.
- Nie tłumacz dokumentów na angielski, jeśli użytkownik nie poprosi wprost.
- Nie usuwaj dokumentów źródłowych — nawet jeśli wyglądają na duplikaty, mogą różnić się datą lub wersją.
- Nie agreguj wielu spraw w jeden dokument — jedna sprawa = jeden katalog `<inicjatywa>/` = osobna ścieżka urzędowa.
