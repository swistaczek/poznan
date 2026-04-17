---
title: "FAQ mieszkańca-aktywisty: akustyka torowa i walka z hałasem tramwajowym"
type: faq
domain: halas
source: wyniki-01-akustyka-torowa.md
updated: 2026-04-17
entities: [WIOŚ, MPK-Poznań, ZDM, ZTP, RPO, PCA, WHO, KE, AGH]
acts: [KC-144, KC-222, KC-23, KC-24, POŚ, UDIP, PN-ISO-1996-2, IEC-61672-1, PN-B-02171, Dyrektywa-2002/49/WE, WHO-ENG-2018, PN-EN-ISO-3095]
signatures: []
---

# FAQ — najczęstsze pytania mieszkańca-aktywisty

## 1. Czy pomiar aplikacją w smartfonie wystarczy, żeby WIOŚ albo sąd zajął się skargą?

Nie jako dowód twardy, ale nie jest bezużyteczny. Mikrofony MEMS smartfonów są optymalizowane pod pasmo mowy (300–3400 Hz), mają filtry górnoprzepustowe ucinające to, co najbardziej dokucza przy tramwaju na zdegradowanym torowisku: energię poniżej 250 Hz. Błąd pomiarowy 10–15 dB dyskwalifikuje go formalnie. **WIOŚ** wymaga miernika klasy 1 lub 2 (**IEC 61672-1**) ze świadectwem wzorcowania PCA. Smartfon daje dokumentację wzorca czasowego, lokalizacji, oraz screening — uprawdopodobnienie, że warto wezwać profesjonalistów. Do sądu cywilnego (art. 144 K.c.) znacznie lepszy jest **kalibrowany mikrofon USB** (np. Dayton UMM-6, ok. 500 zł) z plikiem kalibracyjnym — wynik dostaje status dokumentu prywatnego wystarczającego do wymuszenia biegłego. Minimalny koszt wejścia w metrologię obywatelską: 700–1500 zł [do weryfikacji 2026].

Szczegóły → `01-metodologia-pomiarow.md`.

## 2. Jak odróżnić na słuch zużycie faliste od płaskich miejsc na kołach?

**Corrugation**: ciągły jednostajny „wycie" / „świst" o stałej wysokości przez cały przejazd — „śpiewne", pasmo 250–1000 Hz (~500–800 Hz). Przy hamowaniu wysokość tonu opada synchronicznie z prędkością.

**Wheel flats**: regularne rytmiczne „łup-łup-łup" / „stukot" o metronomicznej cykliczności. Odstęp = obwód koła (ok. 2,2 m przy Ø 700 mm) / prędkość — przy 30 km/h uderzenie co ~0,26 s. Wheel flats **czuje się nogami** (parasejsmicznie grunt i stropy), corrugation — uszami.

Konsekwencja dla kierowania skargi:
- Corrugation → wina **zarządcy infrastruktury** (ZTM/MPK jako właściciel toru).
- Wheel flats → wina **eksploatatora taboru** (brak tokarni podtorowej, konkretny numer boczny).

Szczegóły → `02-sygnatury-widmowe.md`, sygnatury interwencji → `04-interwencje-techniczne.md`.

## 3. Ile kosztuje zlecenie profesjonalnego audytu akustycznego torowiska?

Dwa różne produkty:

**Pomiar immisji akustycznej** — protokół PN-ISO 1996-2 z kilku punktów przy fasadach: $L_{Aeq}$ D/N, $L_{Amax}$, analiza 1/3 oktawy. Wykonują laboratoria akredytowane PCA (40–60 w PL [do weryfikacji BIP PCA]): Instytut Ochrony Środowiska, politechniki (Poznańska, AGH, Śląska), firmy EKKOM, Sweco, LEMITOR, Ekolab. Koszt 4–8 punktów, doba + raport: **8–15 tys. zł netto** [do weryfikacji].

**Audyt diagnostyczny torowiska (MBM)** — CAT, UT, GPR, wskaźnik J. Zlecają zarządcy. Cena: **50–150 tys. zł**. Wykonawcy: Track Tec, ZRK, Skanska Kolej, zagraniczne Vossloh, Plasser & Theurer.

Ścieżka obywatelska: zrzutka na produkt pierwszy (dowód twardy), drugi wymuszać z UDIP (patrz `07-udip-zapytania.md`). Niektóre katedry akustyki wykonują „społeczne" pomiary za zwrot kosztów dojazdu.

## 4. Co robić, gdy MPK/ZTM odpowie „pomiary wykazują zgodność z normą"?

Odpowiedź rozebrać na czynniki pierwsze (90% to wytrych formalny):
1. **Którą normę / który limit?** — 55 dB (zwykła wielorodzinna w nocy) czy 59 dB (strefa śródmiejska, +15 dB nad WHO)?
2. **Jaki wskaźnik?** — $L_{Aeq,N}$ długookresowy czy chwilowy? W którym punkcie (parter/II piętro), jaka odległość od fasady, wysokość nad p.g.s.?
3. **UDIP** — surowe dane 1/3 oktawy, plik audio, spektrogram, świadectwo wzorcowania, protokół kalibratora polowego (94/114 dB przed i po), warunki meteo.
4. **Korekty PN-ISO 1996-2**: $K_T$ +3 do +6 dB za tonalność (curve squeal 6,3–15,8 kHz), $K_I$ +3 do +5 dB za impulsowość (wheel flats). Zarządcy ich zwykle nie stosują — dodanie zrzuca z „normy".
5. Równolegle: skarga do WIOŚ (obowiązek pomiaru kontrolnego) + wystąpienie do RPO w trybie art. 68 Konstytucji.

Szczegóły → `03-normy-limity.md`, `07-udip-zapytania.md`.

## 5. Czy szlifowanie szyn to placebo, czy realna interwencja?

Realna, ale na niewłaściwym poziomie hierarchii. Redukcja 3–7 dB $L_{Aeq}$, pasmo 250–1000 Hz (uderza w corrugation). Koszt 150–280 zł/mb. Problemy:
- **Żywotność 1–3 lata**. Bez smarownic, mat USM, tokarni — corrugation wraca w 18 miesięcy (rezonans zestaw kołowy–szyna jest systemowy). Pułapka „patch and mend".
- **Na łukach R < 50 m** szlifowanie wewnętrznej szyny może paradoksalnie podnieść curve squeal o ~10% (gładsza powierzchnia ułatwia stick-slip).

Zabieg ma sens **tylko w pakiecie**: szlifowanie + smarownica + audyt corrugation co 6 miesięcy. Komunikat: „zgoda na szlifowanie jako etap 0, nie jako rozwiązanie docelowe. Etap 1 = maty USM, etap 2 = FST lub ERS."

Szczegóły → `04-interwencje-techniczne.md`.

## 6. Który wariant technologiczny forsować w petycji dla ul. Dąbrowskiego?

Dla fasad 6–8 m od osi toru, wysokości kamienic ~15 m realistyczny cel $L_{Aeq,N}$ = 48–52 dB (WHO 44 dB nadal poza zasięgiem) wymaga kombinacji: **maty USM (Getzner Sylomer, ~2000 zł/mb) + ERS (Edilon Sedra, 8–12 tys. zł/mb)**. Czysty FST (15–30 tys. zł/mb) to rozwiązanie filharmoniczne — uzasadnione przy fundamentach ceglanych na piasku lub sąsiedztwie obiektów chronionych.

Strategia petycji:
- Wariant bazowy minimum: ERS + USM + smarownice na łukach.
- Wariant preferowany: FST na 300 m newralgicznych.
- Nieakceptowalne: torowisko bezpodsypkowe bez mat.

Dźwignia: precedensy Warszawa W-Z, Kraków Karmelicka → `05-precedensy-polskie.md`.

## 7. Czy zielone torowisko faktycznie wycisza, czy to tylko PR?

Obie rzeczy naraz. Trawnik z Sedum redukuje **pogłos kanionowy** 3–5 dB $L_{Aeq}$ (porowata powierzchnia pochłania wysokie/średnie częstotliwości pod wagonem). Ale:
- NIE redukuje wibracji gruntu (hałasu strukturalnego).
- NIE wpływa na corrugation.
- NIE rozwiązuje curve squeal.
- NIE ogranicza uderzeń wheel flats.

Warstwa kosmetyczno-absorpcyjna, nie izolacyjna. Ma sens tylko zintegrowana z matami USM pod spodem (tak zrobił Wrocław) i żywiczną otuliną szyny. Samo „trawa i zamkniemy temat" od MPK = PR. Dodatkowo torowisko ekologiczne wymaga większej szerokości (drenaż, warstwa wegetacyjna) — przy 6 m od fasady Dąbrowskiego może być geometrycznie problematyczne.

## 8. Jakie dopuszczalne limity obowiązują dokładnie dla ul. Dąbrowskiego i kto decyduje?

Uchwała Rady Miasta o klasyfikacji terenu (Studium + MPZP) + rozporządzenie MKiŚ. Dla „terenów zabudowy mieszkaniowej wielorodzinnej" od linii tramwajowych: **65 dB D / 55 dB N**. W strefie śródmiejskiej miast > 100 tys.: **68 dB D / 59 dB N**. Poznań ~540 tys. → obie kwalifikacje możliwe.

**Kwerenda UDIP #1**: konkretna klasyfikacja Dąbrowskiego w MPZP + w strategicznej mapie hałasu Poznania (aktualizacja co 5 lat, dyrektywa 2002/49/WE; czwarta edycja: **2022**; następna: 2027 <!-- poznan.pl/mim/main/-,p,11105,65515.html, dostęp 2026-04-17 -->).

Dla Dąbrowskiego (wariant zdegradowany 64–69 dB w nocy):
- Limit 59 dB → przekroczenie 5–10 dB (rażące).
- Limit 55 dB → przekroczenie drastyczniejsze.

Dźwignia: przed sądem cywilnym argumentować WHO ENG 2018 ($L_{night}$ 44 dB dla rail) jako standard ostrożności.

## 9. Który z sąsiadów na którym piętrze słyszy najwięcej i dlaczego ma to znaczenie?

Intuicja „najwyżej, najciszej" w kanionie jest fałszywa. H/W > 1 + odbicia od równoległych fasad spłaszczają spadek 6 dB/2×.

- **Parter**: często ekranowany przez zaparkowane samochody i niską zieleń.
- **II–III piętro (8–12 m)**: pełna „widoczność optyczna" na torowisko, fala bezpośrednia + odbita od fasady naprzeciwko.
- **IV–V piętro**: czasem paradoksalnie najsilniejszy odbity sygnał z dachu przeciwległej kamienicy.

Konsekwencja strategiczna:
- **Pomiar referencyjny** → II–III piętro od strony torowiska, okno zamknięte, mikrofon na wysięgniku 0,5–2,0 m (korekta –3 dB wg PN-ISO 1996-2).
- **Petycja** → podpisy z pełnego pionu (parter do strychu). Wyższe piętra wzmacniają dowód zjawiska kanionowego — dla biegłego różnica poziomów II vs V = kluczowy wskaźnik, że to akustyka kanionu, nie „fantazja parteru".

Szczegóły → `01-metodologia-pomiarow.md`.

## 10. Jak długo i w jakich godzinach mierzyć, żeby dane miały wartość dowodową?

Minimum: **24 h** z podziałem na dzień (6–22, 57 600 s) i noc (22–6, 28 800 s) — czasy referencyjne z rozporządzenia. Ale doba pojedyncza jest podważalna („anegdotyczna").

Standard PN-ISO 1996-2: **7 dni powszednich w 2 sezonach** (jesień–wiosna).

Obywatelskie dossier — realistyczne minimum: **3 doby powszednie + 1 weekendowa** z adnotacjami meteo (wiatr < 5 m/s, brak opadów — patrz osłona przeciwwietrzna w `01-metodologia-pomiarow.md`).

Kluczowe okna czasowe: **22:00–1:00 i 4:30–6:00** — najniższe tło drogowe (S/N > 10 dB), wieczorne kursy + poranne zjazdy z zajezdni.

Dla zdarzeń izolowanych ($L_{AE}$): **20–30 przejazdów w każdym kierunku** z logbookiem (godzina, numer boczny z aplikacji tramwajowej, kierunek, warunki, subiektywne wrażenie). Materiał audio w **WAV** (nie MP3) do archiwum — biegły odzyska 1/3 oktawy po latach.

## 11. Czy mogę pozwać MPK/Miasto i jaką ścieżkę wybrać?

**Cztery ścieżki równolegle** (różne tempa, różne ciężary dowodu):

1. **Administracyjna**: skarga do **WIOŚ** w trybie POŚ. Obowiązek pomiaru kontrolnego, decyzja o ograniczeniu emisji. Tańsza, wolna, ustawia oficjalny ślad urzędowy.

2. **Cywilna**: pozew indywidualny lub grupowy (min. 10 osób zgodnie z ustawą o postępowaniu grupowym) o zaniechanie immisji — **art. 144 K.c. w zw. z art. 222 § 2 K.c.** Prywatne pomiary skalibrowanym mikrofonem → dokument prywatny wystarczający do biegłego z urzędu. Horyzont: **2–4 lata**. Można uzyskać nakaz konkretnego środka (np. mat USM).

3. **Zdrowotna**: pozew o zadośćuczynienie za naruszenie dóbr osobistych (**art. 23–24 K.c.**) — prawo do odpoczynku, snu, zdrowego środowiska. Wymaga dokumentacji medycznej (bezsenność, nadciśnienie; epidemiologia WHO ENG 2018).

4. **Polityczna**: interpelacja radnego, obywatelska inicjatywa uchwałodawcza, skarga do RPO, skarga do Komisji Europejskiej (Petycje PE) za niewdrożenie dyrektywy 2002/49/WE w zakresie planów działania.

W realiach polskich najszybszy efekt: **WIOŚ + presja medialna + interpelacja**. Sąd cywilny to horyzont długi, ale wyrok działa długo.

## 12. Ile kosztuje mieszkańca udział i jak podzielić koszty?

Trzy kubełki:

**Diagnostyczny** (pomiary obywatelskie): UMM-6 ~500 zł, kalibrator polowy 94 dB ~1500–2500 zł [do weryfikacji], interfejs USB + laptop (zwykle już macie), osłona przeciwwietrzna 100 zł, statyw 200 zł, REW bezpłatne. **Razem 2–4 tys. zł** → przy 10 rodzinach 200–400 zł/rodzinę jednorazowo.

**Ekspercki** (protokół akredytowany): 8–15 tys. zł za dobę pomiarową — warto raz jako „kotwicę" dowodową → **800–1500 zł/rodzinę**.

**Prawny**: radca ~300–500 zł/h, pozew grupowy 5–15 tys. zł, opłata sądowa ~600 zł + 5% wartości przedmiotu sporu dla roszczeń majątkowych [do weryfikacji stawek aktualnych].

Dobra praktyka: **stowarzyszenie zwykłe** (koszt 0, wpis do rejestru starosty) → darowizny + granty (Batorego, ClientEarth Poland, Polska Zielona Sieć). Poznań ma Budżet Obywatelski (PBO) — można zgłosić „monitoring akustyczny dzielnicy".

Budżet 20-osobowej grupy sąsiedzkiej: **1,5–3 tys. zł/rodzinę na cykl 18–24 miesięcy**. ROI = miliony zł inwestycji miejskich w rozwiązanie.

## 13. Czy sens mierzyć wibracje oddzielnie od hałasu?

Tak — argumentacyjny game-changer. Hałas powietrzny → miernik dźwięku. Wibracje budowli → **akcelerometr**. Dwie różne jednostki (dB vs mm/s lub m/s²), dwie różne normy — w PL obowiązuje **PN-B-02171 „Ocena wpływu drgań na ludzi w budynkach"** z wartościami dopuszczalnymi zależnymi od pory i przeznaczenia pomieszczenia.

Hałas strukturalny: 16–80 Hz, „głęboki rumble" budzący o 5 rano, drżenie żyrandola. Akcelerometr klasy Piezo IEPE z rejestratorem (wariant hobbystyczny PCB 352C33 + NI-DAQ, ok. 3–5 tys. zł, lub wypożyczenie z katedry akustyki) pokazuje drugi niezależny problem: naruszenie normy wibracyjnej.

Wzmocnienie pozwu o immisje: sąd dostaje dwa niezależne naruszenia. Kieruje też dyskusję na rozwiązania adresujące oba zjawiska (maty USM, FST) — szlifowanie i tłumiki szynowe wibracji nie redukują.

## 14. Co napisać w pierwszym piśmie do MPK, żeby nie dostać „odnotowano"?

Szablon zbywalny: „Jest głośno, prosimy o remont." **Szablon niezbywalny**:
- (a) Precyzyjna lokalizacja (adres, nr działki, kierunek) + czas (konkretne doby).
- (b) Wynik pomiarowy z kalibrowanego sprzętu: $L_{Aeq,N}$ = X dB, $L_{Amax}$ = Y dB, pasmo dominujące Z Hz. Metoda: mikrofon USB + plik kalibracyjny, korekta fasadowa –3 dB, wysokość, odległość.
- (c) Diagnoza typu defektu: „spektrogram wykazuje dominantę 630 Hz o charakterze ciągłym — sygnatura zużycia falistego wg PN-EN ISO 3095."
- (d) Wniosek UDIP o KONKRETNE dokumenty — 12 punktów z `07-udip-zapytania.md`.
- (e) Termin ustawowy 14 dni z adnotacją „brak odpowiedzi w terminie skutkować będzie skargą do WSA i pozwem o udostępnienie informacji publicznej".

Dodatkowo: numer ewidencyjny pracownika odpowiedzialnego merytorycznie + potwierdzenie rejestracji w SMS. Po takim piśmie „odnotowano" jest prawnie niewystarczające — otwiera drogę do WSA.

## 15. Czy warto czekać na remont z Wieloletniej Prognozy Finansowej?

Nie — z trzech powodów:

1. **Plan bez specyfikacji materiałowej to pusty plan.** „Remont 2028" może być ERS + USM + FST (40 lat) albo wymianą tłucznia bez mat (powrót problemu za 8 lat). Należy wymusić wpis do **SIWZ** minimalnych kryteriów wibroakustycznych — udział w ocenie (patrz UDIP #12 → `07-udip-zapytania.md`). Przy wadze ceny 80–100% wygra najtańszy z najgorszą technologią.

2. **WPF to dokument budżetowy, nie kontraktowy** — przesuwany o 2–4 lata pod wpływem cięć (częste w dużych miastach).

3. **Narażenie zdrowotne**: 64–69 dB $L_{Aeq,N}$ przez 5 lat → trwałe skutki kardiologiczne i neurokognitywne. W okresie „oczekiwania" dzieci rosną w środowisku bezsennym, dorośli akumulują ryzyko udaru.

Aktywna presja (UDIP, WIOŚ, media, interpelacja) nie tylko przyspiesza remont — przede wszystkim **kształtuje jego jakość**. Różnica między biernym a aktywnym sąsiedztwem: „patch and mend" (3 dB redukcji, 3 lata) vs „premium śródmiejski" (15 dB redukcji, 40 lat). Najbardziej opłacalna dźwignia inwestycyjna, jaką sąsiedztwo może poruszyć.
