---
name: oswiadczenia-majatkowe
description: Use when the user asks to analyze, summarize or compare asset declarations (oświadczenia majątkowe) of a Polish local-government official, councillor or municipal company board member, given a name or BIP PDF links. Finds PDFs in the repo index, reads scans page by page in subagents, and writes one concise, fact-only markdown file per person with a year-to-year table and page citations.
---

# Oświadczenia majątkowe: podsumowanie per osoba

Wynik: jeden plik md na osobę wg [`szablon.md`](./szablon.md). Tylko fakty z oświadczeń, liczby z jednostkami, `[s.N]` przy każdej pozycji. Bez przymiotników, ocen, hipotez, wniosków. Reguły odczytu i granice danych: [`odczyt.md`](./odczyt.md).

## Wymagane narzędzia

- `Bash`: `curl`, `pdftotext`, `pdftoppm` (poppler). Brak poppler: poproś o `brew install poppler`, nie zastępuj tesseractem.
- `Read` (PNG) i `Agent` (odczyt, `model: opus`).
- Indeks linków: `research/transparentnosc/oswiadczenia-majatkowe/dane/oswiadczenia.csv` + `oswiadczenia-zewnetrzne.csv`, wyszukiwarka `scripts/oswiadczenia_szukaj.py`.

## Granice

Obowiązują granice z `odczyt.md` (tylko część A; bez lokalizacji nieruchomości, danych rodziny, urodzenia, numerów, nazwisk z pieczęci). Nie łącz z innymi źródłami (media, KRS, KW). Pliku md nie commituj bez wyraźnej decyzji użytkownika; PDF-ów i PNG nigdy.

## Procedura

1. **Lista.** `W=$TMPDIR/oswiadczenia/<slug-osoby>; mkdir -p $W/pdf $W/png/crop`. `python3 scripts/oswiadczenia_szukaj.py <nazwisko> [imię] --csv > $W/lista.csv`. Sprawdź, czy to jedna osoba (jednostka, funkcja, ciągłość lat); przy popularnym nazwisku i wątpliwości zapytaj. URL-e PDF od użytkownika: użyj wprost.
2. **Pobranie** do `$W/pdf/<rok|brak>-<roczne|rozp|zakoncz|korekta>-<lz_id>.pdf`, poza repo. bip.poznan.pl: min. 5 s między zapytaniami (robots.txt `Crawl-delay: 5`); serwer potrafi przestać odpowiadać na kilka minut.
   ```
   curl -sS --connect-timeout 20 -m 90 --retry 3 --retry-delay 60 -o "$W/pdf/$F" "$URL"; sleep 5
   ```
   Jest `url_pdf_dostepny`: pobierz też jako `*-ocr.pdf` (warstwa OCR, tylko podpowiedź).
3. **Tekst czy skan.** `pdftotext -layout f.pdf - | tr -d '\f[:space:]' | wc -c`; 0 = skan bez tekstu.
4. **Render.** `pdftoppm -r 200 -png f.pdf $W/png/<id>` (obrót strony uwzględnia sam). Wycinki tylko do `$W/png/crop/` (szczegóły w `odczyt.md`).
5. **Odczyt.** Jeden `Agent` (opus) na oświadczenie, równolegle do 6. Prompt: "Przeczytaj i stosuj `<ścieżka>/odczyt.md`" + `W` + ścieżki PNG + ścieżka OCR (jeśli jest) + rodzaj i rok z indeksu. Subagent zwraca dane wg schematu z `odczyt.md`.
6. **Złożenie** wg `szablon.md`, od najnowszego oświadczenia. Wyjście: ścieżka od użytkownika, domyślnie `research/osoby/oswiadczenia/<slug>.md`.
7. **Kontrola.**
   ```
   grep -nE '\b[0-9]{11}\b|[A-Z]{2}[0-9][A-Z]/[0-9]{8}/[0-9]|\b[0-9]{2}-[0-9]{3}\b|\b(ul|al|os|pl)\. |Pozna[nń]|gm\.|gmina|powiat|woj\.|obręb|dz\. ?nr|PL[0-9]{2}|[0-9]{26}' plik.md
   grep -oE '[A-ZŁŚŻ][a-ząćęłńóśźż]+ [A-ZŁŚŻ][a-ząćęłńóśźż]+' plik.md | sort -u      # przejrzyj ręcznie: tylko składający i nazwy instytucji
   grep -nE '[0-9]{1,3}( [0-9]{3})+' plik.md | grep -vE 'zł|EUR|USD|CHF|GBP|jedn\.|m²|ha'  # kwoty bez jednostki
   ```
   Trafienia z nazw jednostek i sekcji BIP (np. "Urząd Miasta Poznania") są w porządku. Każda pozycja ma `[s.N]`. Brak słów oceniających ("duży", "znaczny", "podejrzany", "aż").

## Składanie pliku

- **Etykiety kolumn:** `RRRR R` (roczne, rok stanu), `P RRRR-MM-DD`, `Z RRRR-MM-DD`, `RRRR K` (korekta zastępuje R z tym samym stanem).
- **Nagłówek:** funkcja z pola "stanowisko lub funkcja"; nawias to zakres dat oświadczeń w BIP, nie okres pełnienia funkcji (nie wywodź).
- **Zestawienie:**
  - wiersze jak w szablonie; sumy tylko z kwot wpisanych i odczytanych pewnie (`~` szacunek, `?` niepewne);
  - pozycje `[zapis niejednoznaczny]` poza sumą: `+ pozycja [zapis niejednoznaczny]`;
  - waluty osobno, bez przeliczania;
  - nieruchomości: składnik wspólny w całości, nie na pół; przy całości i udziale bierz udział;
  - dochody: suma tylko kwot tego samego rodzaju, mieszane osobno;
  - zobowiązania: suma "pozostało" per waluta, kwoty bez określenia osobno; nie odejmuj od nieruchomości.
- **Zmiany:**
  - tylko fakty: pozycja pojawiła się, zniknęła, zmieniła wartość z X na Y;
  - dopasowanie po kodzie + opisie + powierzchni (kolejność w formularzach się zmienia), bez powierzchni zaznacz dopasowanie ręczne;
  - dochodów P i Z nie porównuj z R; korekta: zmiany względem pierwotnego, jeśli jest w BIP, inaczej "zakres zmian nieoznaczony".
- **Bloki per oświadczenie:**
  - nie powtarzaj pozycji identycznych z zestawieniem;
  - podaj tylko to, czego tabela nie mówi: rozbicie II, VIII, X, pozycje DOD, ND/przekreślone/puste, Odczyt, różnice formularza;
  - brak jednostki odnotuj raz na blok;
  - stan równy podpisowi: `stan na = podpis RRRR-MM-DD`.
- **Cel:** ok. 15 linii na oświadczenie, cały plik do ok. 60 linii przy 3-4 oświadczeniach.

## Podstawa prawna

Art. 24h usg (obowiązek; terminy ust. 4 radny/wójt, ust. 5 pozostali; analiza ust. 6-9), art. 24i usg (jawność części A, BIP); usw art. 27c, 27d. Wzory: rozp. PRM z 26.02.2003, t.j. Dz.U. 2017 poz. 2020 (gmina, zał. 1 radny, zał. 2 pozostali); rozp. PRM z 9.04.2009, t.j. Dz.U. 2017 poz. 2015 (województwo). Stopka pliku: jak w szablonie.
