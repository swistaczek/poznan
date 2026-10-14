# Odczyt jednego oświadczenia (instrukcja dla subagenta)

Dostajesz PNG stron jednego oświadczenia (200 dpi) i ewentualnie tekst OCR. Zwracasz wyłącznie dane wg schematu na końcu. Nie piszesz plików poza `$W/png/crop/`.

## Granice

Jawna jest tylko część A. NIE przepisuj, nawet gdy widać: części B; adresów, miejscowości, ulic, ogrodów działkowych, numerów działek i KW (nic, co lokalizuje nieruchomość); daty i miejsca urodzenia, nazwiska rodowego; adresu pracodawcy lub siedziby firmy; numerów rachunków, rejestracyjnych, VIN; imion, danych i dochodów małżonka i dzieci (krewny: tylko "spadek"/"darowizna"); nazwisk osób fizycznych będących wierzycielami lub dłużnikami ("osoba fizyczna"); nazwisk z pieczęci i adnotacji urzędowych; treści kopii PIT. Nie szacuj, nie przeliczaj walut, nie zgaduj cyfr, nie komentuj.

## Źródła i technika

- Obraz jest źródłem. OCR (`-ocr.pdf`) tylko podpowiada: liczby z wydruku zwykle zgodne, ale OCR gubi skreślenia, pieczęć zamienia w śmieci (urwane daty), "II" czyta jako "11", rozbija "m 2", "z ł". Brak OCR nie blokuje odczytu.
- Wycinki: `pdftoppm -r 400 -f N -l N -x X -y Y -W W -H H -png f.pdf $W/png/crop/<id>-sN`. Współrzędne to piksele przy danym `-r` (A4 w 400 dpi: ok. 3307x4672). Maks. 600 dpi; gdy dalej niejasne: `[niepewne]`.
- Cytuj numer strony PDF (nie nadruk "-8-", nie "1/5").

## Struktura

Segmentuj po frazach wzoru, nie po numerach (autonumeracja przesuwa punkty, treść przechodzi na kolejną stronę: cytuj stronę treści): "Zasoby pieniężne", "Dom o powierzchni", "Mieszkanie o powierzchni", "Gospodarstwo rolne", "Inne nieruchomości", "Posiadam udziały", "Posiadam akcje", "Nabyłem(am)", "Prowadzę działalność", "W spółkach handlowych", "Inne dochody", "Składniki mienia ruchomego", "Zobowiązania pieniężne".

Wzory: gmina zał. 1 (radny: `III.1`/`III.2`, `IV.1`/`IV.2`, jedno `VII`) i zał. 2 (wójt, zastępcy, sekretarz, skarbnik, kierownik jednostki, zarząd gminnej osoby prawnej, decyzje z up.: `VII.1`-`VII.3`); województwo zał. 2 do rozp. z 2009 r. (sekcje jak gmina zał. 2). Stary druk: w V brak "związku metropolitalnego". Bywa druk przepisany w edytorze, wydruk z Dz.U., załącznik za częścią B, punkty dopisane przez składającego (`DOD.n`).

## Skreślenia i pieczęć

Skreślenia czytaj z obrazu: funkcje w tytule, klauzula o wspólności w preambule (skreślona = tylko majątek odrębny), skreślone "nie dotyczy" z dopisaną kwotą. Skreślenie to kreska w kolorze wpisów; pieczęć wpływu na tytule daje linie i zabarwienie w kolorze tuszu pieczęci. Przypis "niewłaściwe skreślić" bywa niewykonany: funkcję bierz z pola "stanowisko lub funkcja". Funkcja w formularzu szersza niż w BIP: formularz wiodący, podaj obie.

## Daty

- Pole "dnia" przy miejscowości to data sporządzenia, nie stan.
- Roczne: stan = `RRRR-12-31` roku poprzedniego `(wywiedziony)`, chyba że wypełniono "według stanu na".
- Pierwsze (P) i końcowe (Z): stan = pole "dnia" `(pole "dnia")`.
- Korekta (K, "KOREKTA" w tytule): stan jak w korygowanym oświadczeniu; rok wg stanu, nie wg podpisu.
- Osobno: data podpisu, data z pieczęci wpływu. Cytaty Dz.U. w preambule to nie daty. Pozycja z własną datą stanu: data przy pozycji. Sprzeczne daty: `[do weryfikacji]`. Format zawsze RRRR-MM-DD.

## Liczby i jednostki

- Kropka lub przecinek bywa separatorem tysięcy ("14.425" = 14 425). Grupowanie niezgodne z tysiącami ("600,752,02", "1 2345,67"): dosłownie + `[zapis niejednoznaczny]`, znormalizowana pusta.
- Szacunek `~`: "tys"/"tyś", "~", "ok.", "(około)". NIE szacunek: ",-", ",--" (pełne złote).
- Myślnik przed kwotą to nie minus. Przypisy i numery stron wyglądają jak liczby. Mylone: 1/7, 3/8, 0/6/8, 9/P; odręczne "zł" wygląda jak "26"/"25"/"2ł". Cyfra nadpisana: `[cyfra poprawiana]`. Dopisek innym tuszem lub ręką: dosłownie `[dopisek innym tuszem]`, poza wartością znormalizowaną.
- Normalizacja: spacja tysięcy, przecinek dziesiętny, kod waluty (EUR, USD, CHF; nie €). Brak wartości: `brak`.
- I.PLN: walutę wyznacza rubryka (zł). Brak jednostki przy II, VIII, IX, X: `[jedn. nie podana]`; jednostka tylko w zapisie słownym: weź ją, zaznacz. Waluta obca w wierszu PLN: `I.WAL` z uwagą.
- m², ha, "m", "m kw.": jak w dokumencie.

## Puste, "nie dotyczy", przekreślone

Cztery stany na poziomie kodu: wpis, "nie dotyczy" (też "nie", literówki), przekreślone bez wpisu, puste. "Nie dotyczy" raz na blok nie rozciąga się na sąsiednie kody. Pod-pola bez wpisu w rubryce ND pomijaj.

## Przynależność i wartości

- Przynależność: globalnie (podkreślenie/skreślenie w zdaniu wstępnym), przy pozycji, dopiskiem z parafą. WM: "wspólność ustawowa", "małżeńska współwłasność", "wspólnota majątkowa". MO: "majątek odrębny/osobisty". Współwłasność ułamkowa to nie WM. "Tytuł prawny: własność" bez reżimu = przynależność nie podano. Reżim lub "akt notarialny" w polu tytułu: dosłownie.
- Wartości deklaratywne, różne podstawy: przepisz. Całość i udział w jednym polu: obie, z oznaczeniem. Udział bez wskazania, czego dotyczy wartość: `[całość czy udział: nie podano]`. Pojazdy bez wartości: nie szacuj.
- Pozycje poza rubryką (fundusze i PPK w gotówce, mieszkanie w II.4, dochód z zarządu w VII, zwrot od banku w X): zapisz tam, gdzie wpisano, z uwagą.

## Dochody i zobowiązania

- Dochody: rodzaj przy każdej pozycji (przychód, dochód, "brutto", ryczałt, nie podano). Okres dosłownie, gdy podany (P: bywa część bieżącego roku). Nie nazywaj kwot "pensją" ani "netto".
- Zobowiązania: udzielono, pozostało, obie albo jedna bez określenia: zapisz, co jest, z typem kwoty. Waluta, data zaciągnięcia, oprocentowanie, solidarność: jeśli są.

## Schemat wyjścia

```
META: rodzaj (R | P | Z | K; źródło: BIP / tytuł) | wzor (zal1-radny | zal2 | usw-zal2; stary druk tak/nie) | funkcja_formularz | stan_na RRRR-MM-DD (wywiedziony | pole "dnia" | "według stanu na" | nieustalony) | podpis | wplyw | stron | skan/tekst | pismo maszynowe/ręczne/mieszane
DEKLARACJA: MO + WM | tylko MO | nie wskazano | s.N
POZYCJA: kod | opis bez lokalizacji | wartość dosłownie | wartość znormalizowana | przynależność (WM | MO | udział x/y | nie podano) | okres/typ kwoty | uwaga | s.N
ND: kody | PRZEKR: kody | PUSTE: kody
ODCZYT: kod, s.N, [nieczytelne] / [niepewne] / [zapis niejednoznaczny] / [cyfra poprawiana] / [dopisek innym tuszem] / [do weryfikacji]: co dokładnie
```

Kody: `I.PLN`, `I.WAL`, `I.PAP`, `II.1` dom, `II.2` mieszkanie, `II.3` gospodarstwo, `II.4.n` inne, `III`, `IV` (radny `.1`/`.2`), `V`, `VI.1`, `VI.2`, `VII.1`-`VII.3` (radny `VII`), `VIII.n`, `IX.n`, `X.n`, `DOD.n`.
