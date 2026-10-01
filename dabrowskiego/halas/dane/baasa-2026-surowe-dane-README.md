---
title: "Surowe dane pomiarów hałasu BAASA 2026 (ul. Dąbrowskiego) - opis"
type: dane
domain: dabrowskiego
area: halas
updated: 2026-10-01
---

# Surowe dane pomiarów hałasu BAASA 2026, ul. Dąbrowskiego

Źródło: załącznik nr 5 ("zapisy z mierników (kopia plików źródłowych)") do pisma ZDM Poznań **ZDM-PK.01520.249.2026.8**, doręczonego e-mailem 01.10.2026 (odpowiedź na wniosek z 18.09.2026, sprawa pomiarów ZDM-RO.401.544.2026). Oryginał: plik `Kopia Zapisy z mierników.xlsx` (7,4 MB, 5 arkuszy), lokalnie poza repo. Wykonawca pomiarów: Laboratorium Badawcze BAASA Acoustics sp. j. (PCA AB 1820), sprawozdania S-2026.03-10/... z 31.07.2026. Dane pomiarowe nie są danymi osobowymi; arkusz nie zawiera nazwisk.

Analiza i wnioski: [`../odpowiedzi/2026-10-01_zdm-dane-zrodlowe-baasa.md`](../odpowiedzi/2026-10-01_zdm-dane-zrodlowe-baasa.md). Wyniki sprawozdań: `pomiary-baasa-2026-05-wyniki.md` (lokalnie).

## Co jest w arkuszu (i czego nie ma)

Każdy arkusz: wiersz 1 `P1 (A, Lin)` (profil 1 miernika Svantek, korekcja A, uśrednianie liniowe), wiersz 2 nagłówki `No.`, `Date & time`, `LAeq (TH) [dB]` (TH = time history, logger). Wartości zapisane jako tekst, czas lokalny, polskie skróty miesięcy (`19 maj 2026 11:29:47`). Jedna wielkość: **LAeq w kroku loggera**. Brak przerw w zapisie (krok stały w każdym arkuszu).

**Brak**: LAFmax, LAmin, LApeak, Summary Results (LAE, LN), widm, znaczników zdarzeń, audio, parametrów kalibracji. To eksport (prawdopodobnie SvanPC++), nie natywny plik .SVL/.SVT.

| arkusz | punkt | adres | źródło | początek | koniec | krok | wierszy | miernik (z protokołu) |
|---|---|---|---|---|---|---|---|---|
| 2.43 | PPH2.43 | Dąbrowskiego 82 | drogowe + torowisko | 19.05.2026 11:29:47 | 20.05.2026 12:14:18 | 1 s | 89 072 | SVAN 971 nr 44533 |
| 3.05 | PPH3.05 | Dąbrowskiego 118 | drogowe | 19.05.2026 11:09:55 | 20.05.2026 12:01:31 | 1 s | 89 497 | SVAN 971 nr 107463 |
| 3.58 | PPH3.58 | Dąbrowskiego 52 | drogowe | 19.05.2026 15:58:47 | 20.05.2026 17:20:24 | 1 s | 91 298 | SVAN 971 nr 72531 |
| 4.05 | PPH4.05 | opisany jako Dąbrowskiego 82 / Polna; współrzędne (52°24'41,4" 16°54'35,2") ok. 840 m na wschód, odcinek Most Teatralny - Rynek Jeżycki | tramwajowe | 23.04.2026 15:18:07.357 | 19:07:45.857 | 0,5 s | 27 558 | SVAN 971A, "nr fabryczny" wpisany jako 2026.03-10/Z4/05 |
| 4.16 | PPH4.16 | Dąbrowskiego 73 | tramwajowe | 23.04.2026 11:42:50.713 | 14:42:28.213 | 0,5 s | 21 556 | SVAN 971A, "nr fabryczny" wpisany jako 2026.03-10/Z4/16 |

Punkty tramwajowe: tylko ok. 3 h i 3 h 50 min w dzień, linie 2, 8, 18 (PPH4.16) i tylko 8, 18 (PPH4.05). **Brak jakiejkolwiek próbki z pory nocnej** - LAeqN w sprawozdaniach PPH4.05/PPH4.16 jest wyliczony z natężenia ruchu ZTM, nie zmierzony. Punkty drogowe: pomiar ciągły ok. 24-25 h, noc zmierzona.

## Pliki w tym katalogu

| plik | zawartość |
|---|---|
| `baasa-2026-pph2-43-surowe.csv.gz` ... `baasa-2026-pph4-16-surowe.csv.gz` | wierny eksport każdego arkusza: `nr`, `czas_lokalny` (ISO 8601, ms dla kroku 0,5 s), `LAeq_dB` (0,1 dB). gzip, łącznie ok. 2,1 MB (CSV ok. 8 MB) |
| `baasa-2026-tramwaj-przejazdy-porownanie.csv` | 177 przejazdów z tabel protokołów P-2026.03-10/Z4/05 i /Z4/16 (godzina, kierunek, linia, nr boczny, typ, prędkość, LAEk z protokołu, uwagi) + wartości policzone z surowego zapisu (szczyt 0,5 s w minucie, czas szczytu, czas zdarzenia 10 dB, LAE, L90 lokalne, różnica, flaga podzbioru czystego) |
| `baasa-2026-drogowe-godzinowe-porownanie.csv` | 72 przedziały 1 h (3 punkty drogowe): LAeq i L95 z surowych vs tabela protokołu, różnica, najgłośniejsze sekundy, minimalna liczba sekund do usunięcia, by uzyskać wartość protokołu |
| `baasa-2026-tramwaj-lae-protokol-vs-surowe.png` | LAEk z protokołu vs LAE z surowego zapisu, oba punkty tramwajowe |
| `baasa-2026-tramwaj-przebieg-czasowy.png` | przebieg LAeq 0,5 s PPH4.16 i PPH4.05 z zaznaczonymi przejazdami |
| `baasa-2026-tramwaj-szczyty-przejazdow.png` | rozkład najwyższego LAeq 0,5 s w minucie przejazdu |
| `baasa-2026-drogowe-godzinowe-surowe-vs-protokol.png` | godzinowe LAeq z surowych vs protokół, 3 punkty drogowe |

Odczyt: `pandas.read_csv('baasa-2026-pph4-16-surowe.csv.gz', parse_dates=['czas_lokalny'])`.

## Jak liczono

- LAeq przedziału: średnia energetyczna, 10·log10(mean(10^(L/10))).
- Okna godzinowe dróg: 24 h od godziny startu z protokołu (PPH2.43, PPH3.05: 19.05 12:00; PPH3.58: 19.05 17:00). Dzień 6-22, noc 22-6.
- LAE przejazdu tramwaju: w minucie podanej w protokole szukany najwyższy LAeq 0,5 s; zdarzenie = ciągły odcinek próbek nie niższych niż szczyt minus 10 dB (max ±30 s); LAE = 10·log10(Σ 10^(L/10)·0,5 s / 1 s). Ta sama metoda dla obu punktów.
- Podzbiór czysty: tylko przejazdy z wartością LAEk, czas zdarzenia 2-30 s, szczyt < 90 dB (bez mijanek, zakłóceń, zatrzymań i okien z obcym głośnym zdarzeniem). PPH4.16: 60, PPH4.05: 65.
- LAeqD/N tramwaju: wzór z protokołu, LAeqT = 10·log10(Σ Nk·10^(LAEk/10) / T), T = 57 600 s (dzień) lub 28 800 s (noc), Nk z tabeli "Parametry ruchu" (dane ZTM). Klasa bez pomiaru: najwyższa średnia innej klasy (reguła laboratorium).

## Ograniczenia

- Krok 0,5 s / 1 s: najwyższy LAeq kroku jest dolnym oszacowaniem LAFmax (przy krótkich uderzeniach zaniżenie kilka do kilkunastu dB, por. `research/halas/dostep-do-surowych-danych-pomiarowych-baasa.md` pkt 13). LAmax/LApeak nie da się z tych danych odtworzyć.
- Brak audio: źródła pików (tramwaj / samochód / motocykl / sygnał uprzywilejowany / służby utrzymania) nie da się potwierdzić. Przypisanie szczytu w minucie do tramwaju opiera się na godzinie z protokołu.
- Punkty tramwajowe rejestrują sumę hałasu tramwajowego i drogowego (torowisko wspólne z jezdnią).
- Pomiar tramwajowy z jednego dnia (czwartek 23.04.2026, 11:40-19:05), pomiar drogowy z jednej doby (19-20.05.2026).
