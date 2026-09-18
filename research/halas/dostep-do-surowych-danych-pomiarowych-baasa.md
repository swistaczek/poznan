---
title: "Dostęp do surowych danych pomiarowych BAASA"
type: research
domain: halas
updated: 2026-09-18
---

# Czy można żądać surowych danych/nagrań z pomiarów hałasu BAASA

Pytanie wyjściowe: po otrzymaniu 5 sprawozdań BAASA (16.09.2026, zob. `pomiary-baasa-2026-05-wyniki.md`) czy warto i można skutecznie zażądać od ZDM i/lub BAASA Acoustics surowych danych pomiarowych (plik z miernika SVAN 971/971A, ewentualnie nagranie audio), na podstawie których powstały uśrednione wyniki LAeq, żeby wyodrębnić z nich pojedyncze zdarzenia impulsywne (LAmax/SEL dla trzasków i uderzeń).

**Status researchu: ROZSTRZYGNIĘTY (tura 2, 18.09.2026).** Pierwsza tura (17.09.2026) zamknęła tylko pytanie o retencję wg akredytacji PCA, z wynikiem negatywnym. Druga tura zamknęła pozostałe pięć pytań. Odpowiedź: TAK, wniosek ma sens, ale nie na podstawie UDIP tylko **ustawy OOŚ**, i nie do BAASA tylko **do ZDM**. Szczegóły i podstawy poniżej.

Wszystkie cytaty przepisów pochodzą z tekstów ujednoliconych pobranych z ELI/API Sejmu (`api.sejm.gov.pl/eli/...`), nie ze źródeł wtórnych.

## Ustalone

### A. Retencja i obowiązek posiadania danych leży po stronie ZDM, nie laboratorium

1. **Dokumenty programu akredytacji PCA "DAB-07"** (PN-EN ISO/IEC 17025, edycje: nr 4 z 17.01.2024 i nr 14 z 29.12.2023) **nie zawierają żadnego okresu przechowywania zapisów źródłowych**. Sama akredytacja nie daje podstawy do twierdzenia, że BAASA musi przechowywać dane surowe przez konkretny czas. Źródła: [DAB-07 ed.14](https://www.pca.gov.pl/storage/file/core_files/2024/7/9/55bf3a80b3c968e278ed9ad020cd65f1/dab-07_14.pdf), [DAB-07 Lista wymagań ed.4](https://www.pca.gov.pl/storage/file/core_files/2024/7/9/ce10c98399c793815f9d7efebab473bb/dab-07_4_lista_wymagan.pdf). (tura 1, weryfikacja 3-0)

2. **Lukę z pkt 1 zamyka ustawa, po stronie zarządzającego.** Art. 175 ust. 1 POŚ: "Zarządzający drogą, linią kolejową, **linią tramwajową**, lotniskiem lub portem (...) jest obowiązany do okresowych pomiarów poziomów w środowisku substancji lub energii wprowadzanych w związku z eksploatacją tych obiektów." Art. 175 ust. 5 POŚ: "Do wyników pomiarów, o których mowa w ust. 1-3, stosuje się odpowiednio przepis art. 147 ust. 6." Art. 147 ust. 6 POŚ nakłada obowiązek "**ewidencjonowania wyników przeprowadzonych pomiarów oraz ich przechowywania przez 5 lat** od zakończenia roku kalendarzowego, którego dotyczą". Art. 175 ust. 5a odsyła do art. 147a, czyli obowiązku zlecenia akredytowanemu laboratorium (to wyjaśnia obecność BAASA). Art. 177 ust. 1: wyniki przedkłada się organowi ochrony środowiska oraz GIOŚ, o ile mają szczególne znaczenie dla obserwacji zmian stanu środowiska. Źródło: [POŚ, tekst ujednolicony ISAP, stan 2026-09-11](https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20010620627/U/D20010627Lj.pdf); potwierdzone niezależnie na t.j. [Dz.U. 2025 poz. 647](https://api.sejm.gov.pl/eli/acts/DU/2025/647/text.pdf).
   **Skutek:** ZDM nie może twierdzić "nie posiadamy", bo ma ustawowy obowiązek ewidencjonowania i 5-letniego przechowywania wyników.

3. **Pomiar musi być wykonany przez laboratorium akredytowane wg PN-EN ISO/IEC 17025** (art. 147a ust. 1 pkt 1 POŚ w zw. z art. 175 ust. 5a POŚ oraz rozporządzenie MŚ z 16.06.2011). BAASA (PCA AB 1820) spełnia ten wymóg. (tura 1, weryfikacja 3-0)

### B. Rozporządzenie pomiarowe SAMO wymaga istnienia danych źródłowych

Rozporządzenie Ministra Środowiska z 16.06.2011 w sprawie wymagań w zakresie prowadzenia pomiarów poziomów substancji lub energii w środowisku przez zarządzającego drogą, linią kolejową, linią tramwajową, lotniskiem lub portem, [Dz.U. 2011 nr 140 poz. 824](https://api.sejm.gov.pl/eli/acts/DU/2011/824/text.pdf). Status zweryfikowany w ELI: **obowiązujące**, wejście 22.07.2011, jedyna zmiana [Dz.U. 2011 nr 288 poz. 1697](https://api.sejm.gov.pl/eli/acts/DU/2011/1697/text.pdf) poprawia wyłącznie literówkę w definicji LAeq N (pora nocy 22:00-06:00). Załącznik nr 3 (drogi publiczne, linie kolejowe, linie tramwajowe) bez zmian od 2011 r.

4. **Rozporządzenie nakazuje zapisanie danych "w postaci źródłowej".** Zał. nr 3 cz. C pkt 3: przy ciągłej rejestracji przyrządy powinny umożliwiać "1) rejestrowanie w pamięci miernika przebiegu zmian poziomu dźwięku w czasie, co najmniej w czasie odniesienia, **z krokiem próbkowania nie większym niż 1 s**; 2) **przeniesienie z miernika do komputera zarejestrowanych w pamięci przyrządu pomiarowego wyników pomiarów i zapamiętanie ich w postaci źródłowej**; 3) rejestrowanie i drukowanie niezbędnych parametrów pracy miernika wraz ze współczynnikiem kalibracyjnym toru pomiarowego (...); 4) dokonanie analizy statystycznej sygnału akustycznego, w szczególności wyznaczenie poziomów statystycznych, określonych w normie PN-ISO 1996-1".
   To jest bezpośrednia podstawa do twierdzenia, że plik źródłowy z miernika nie jest prywatnym plikiem roboczym laboratorium, tylko elementem wymaganym metodyką referencyjną.

5. **Metodyka zakłada możliwość ODSŁUCHANIA zapisu.** Zał. nr 3 cz. C pkt 4: "Należy zapewnić warunki techniczne do możliwości **odsłuchania fragmentów zarejestrowanego zdarzenia akustycznego, którego interpretacja może budzić zastrzeżenia**." Czyli sam prawodawca przewiduje istnienie zapisu dźwiękowego jako narzędzia weryfikacji spornego wyniku. To argument, że żądanie odsłuchu spornego fragmentu nie jest ekstrawagancją, tylko korzystaniem z mechanizmu wpisanego w metodykę.

6. **Dla linii tramwajowej metodyką referencyjną jest procedura SEL na pojedynczych zdarzeniach, a nie sam LAeq ciągły.** Zał. nr 3 cz. A pkt 3: wartość LAeq wyznacza się procedurą "1) ciągłej rejestracji hałasu powodowanego przez **ruch drogowy** (...); 2) pomiarów poziomu ekspozycyjnego dźwięku w odniesieniu do **pojedynczych zdarzeń akustycznych**, stosowaną w celu określenia poziomów hałasu (...) b) linii kolejowych, c) **linii tramwajowych, w odniesieniu do odcinków torowisk**; 3) (...) próbkowania". Zał. nr 3 cz. F pkt 11: "Na potrzeby pomiarów hałasu (...) w związku z eksploatacją linii tramwajowej, w odniesieniu do odcinków torowisk, określa się tyle klas pojedynczych zdarzeń akustycznych, ile typów tramwajów przejeżdża przed punktem pomiarowym w czasie dokonywania pomiarów."
   **Skutek strategiczny:** odmowa ZDM z 4.05.2026 (pismo ZDM-RO.401.544.2026.3) na prośbę o LAmax/SEL z 24.04.2026 stoi w napięciu z metodyką referencyjną, która dla torowiska tramwajowego przewiduje wprost pomiar poziomów ekspozycyjnych per zdarzenie i ewidencję w tabeli 5 załącznika nr 3.

7. **LAE (SEL) wolno wyznaczyć post factum z zarejestrowanego przebiegu, bez powtarzania pomiaru.** Zał. nr 3 cz. F pkt 2: "Poziomy ekspozycyjne dźwięku, oznaczane jako LAE, są mierzone w przypadku występowania pojedynczych zdarzeń akustycznych. **Poziomy ekspozycyjne mogą być również wyznaczane z przeprowadzonej w laboratorium analizy zarejestrowanych w terenie przebiegów zmienności hałasu w czasie.**" Zał. nr 3 cz. F pkt 12: czas pomiaru poziomu ekspozycji nie może być mniejszy niż czas trwania zdarzenia, pod warunkiem że LAmax zdarzenia przewyższa tło o co najmniej 10 dB. Definicja z zał. nr 1 pkt 3 (wzór 1): "LAmax - maksymalna wartość poziomu dźwięku dla danego, mierzonego zdarzenia akustycznego **według stałej czasowej FAST**".
   **Skutek:** ZDM nie może odpowiedzieć "żeby podać LAmax/SEL trzeba by zrobić nowe pomiary". Jeśli przebieg czasowy istnieje, LAE liczy się z niego w laboratorium.

8. **Sprawozdanie to nie to samo co protokół, a protokół jest dużo bogatszy.** Zał. nr 3 cz. I pkt 2: "Sprawozdanie z pomiarów zawiera: 1) informacje zamieszczone w protokołach pomiarów **lub załączone protokoły pomiarów**; 2) wyniki pomiarów równoważnych poziomów dźwięku A (...) zgodnie z tabelą 7". Protokół (cz. I pkt 1) zawiera m.in.:
   - pkt 8 lit. c: "**klasyfikację terenu określoną w miejscowym planie zagospodarowania przestrzennego**"; lit. d: "dopuszczalny poziom hałasu; **jeżeli nie został on określony, należy podać, której pozycji w tabeli zawierającej dopuszczalne poziomy hałasu w środowisku odpowiada faktyczne zagospodarowanie terenu**" (to bezpośrednia podstawa dla pytania już zadanego ZDM 17.09.2026 o niewypełnioną klasyfikację terenu w PPH3.58: pusta rubryka jest naruszeniem zał. nr 3 cz. I pkt 1 ppkt 8 lit. c i d, a nie dopuszczalnym uproszczeniem);
   - pkt 9: wysokość punktu, współrzędne geograficzne, odległość od źródła i od elewacji;
   - pkt 10 lit. a: "charakterystyka korekcyjna A, zastosowana stała czasowa, zakres pomiarowy, charakterystyka mikrofonu, **stała czasu próbkowania**"; lit. b: odchyłka wzorcowania przed i po pomiarze;
   - pkt 11: warunki meteorologiczne (średnie oraz maksymalne i minimalne);
   - pkt 12: wyniki ewidencjonowane wg **tabeli 3** ("Wyniki pomiarów hałasu, uzyskane przy zastosowaniu ciągłej rejestracji hałasu **z podziałem na krótsze czasy obserwacji**": kolumny Lp. / długość przedziału ti [s] / LAeq i zmierzony w czasie ti [dB] / poziom tła LATla lub L95) oraz wg **tabeli 5** ("Wyniki pomiarów poziomów ekspozycji dla pojedynczych zdarzeń akustycznych", osobna tabela dla każdej klasy zdarzeń);
   - pkt 13: szkic pomiarowy lub mapa obszaru badań.
   **Skutek taktyczny:** zanim w ogóle sięgnie się po plik binarny z miernika, warto zażądać **protokołów pomiarowych** w pełnym zakresie zał. nr 3 cz. I pkt 1. To dokument przewidziany wprost przepisem, więc trudno go zakwalifikować jako "materiał wewnętrzny", a zawiera już rozbicie czasowe (tabela 3) i, jeśli procedurę zastosowano prawidłowo dla torowiska, wartości per zdarzenie (tabela 5).

### C. SVAN 971 / 971A: co miernik faktycznie zapisuje

Źródła: karty katalogowe i instrukcje producenta (Svantek), zweryfikowane parami dokument-dokument: [SV 971A datasheet](https://svantek.com/wp-content/uploads/2021/06/SV971A_datasheet_HS_application_2021.pdf), [SV 971A specyfikacja PL](https://svantek.com/wp-content/uploads/2021/06/SV971A-specyfikacja-pl.pdf), [SV 971A User Manual v.1.03](https://svantek.com/wp-content/uploads/2023/01/SV971A-Man.EN_v.1.03_2024-05-28.pdf), [SVAN 971 datasheet](https://svantek.com/wp-content/uploads/2023/01/SVAN971_datasheet.pdf), [SVAN 971 User Manual v.3.1](https://svantek.com/wp-content/uploads/2020/08/svan_971_man_en_v.3.1_2020-09-03.pdf).

9. **Audio: oba modele POTRAFIĄ nagrywać realny dźwięk (WAV, odtwarzalny), ale jest to OPCJA PŁATNA, aktywowana kodem.** SV 971A: "Audio Recording (option) | Audio recording on trigger or continuous mode, 12 / 24 / 48 kHz sampling rate, wav format"; instrukcja: "The Wave Recording function is optional and should be unlocked by entering the activation code". Kod opcji: SF 971A_15. SVAN 971: "Audio Recording1 (optional) | Audio events recording, trigger and continuous mode, 12 kHz sampling rate, wav format", opcja SF 971_15; w 971 audio zdarzeń zapisuje się **wewnątrz** pliku loggera .SVL, w 971A jako osobne pliki .WAV.
   **Skutek dla zarzutu RODO:** zarzut "nagrywaliście rozmowy przechodniów" jest warunkowy, nie automatyczny. Bez wykupionej opcji miernik nagrania dźwiękowego w ogóle nie tworzy. Pierwsze pytanie do ZDM/BAASA brzmi więc: czy opcja SF 971_15 / SF 971A_15 była aktywna i czy podczas tych pomiarów włączono Wave/Event Recording. **Dodatkowo art. 18 pkt 4 ustawy OOŚ (niżej, pkt 14) i tak wyłącza ochronę danych osobowych jako podstawę odmowy dla informacji o poziomie emitowanego hałasu**, więc RODO nie jest tu skuteczną tarczą organu.

10. **Minimalny krok logowania to 100 ms, nie 10 ms.** Instrukcje obu modeli, identyczne brzmienie: "Logger Step can be selected from the set: **100 ms, 200 ms, 500 ms** or from 1 second to 59 seconds with 1-second step (...)". Domyślna wartość: 1 s. Krok 2 ms istnieje tylko w 971A i tylko w trybie RT60 (czas pogłosu), nie w normalnym loggerze poziomu.
    Widoczny w protokołach BAASA parametr "Stała czasu próbkowania [s]: 1" odpowiada więc ustawieniu domyślnemu i zarazem minimum wymaganemu przez zał. nr 3 cz. C pkt 3 ppkt 1, ale miernik mógł logować 10x gęściej.

11. **LAmax JEST logowany jako osobny wynik w każdym kroku loggera.** Instrukcja SV 971A rozdz. 4.5.2: "For the Level Meter function, the following results can be logged: **Lpeak (Lpk), Lmax, Lmin, Leq**, LR1 and LR2." Instrukcja SVAN 971 rozdz. 4.5.2: "it is possible to log next results: Lpeak (Lpk), **Lmax**, Lmin and Leq."
    **To jest kluczowe rozróżnienie.** Jeżeli BAASA logowała profil z włączonym Lmax, to w pliku .SVL leży **LAFmax dla każdej sekundy pomiaru**, a nie tylko LAeq,1s. Wtedy wyodrębnienie maksimów pojedynczych przejazdów jest natychmiastowe i nie wymaga żadnego audio.

12. **SEL (LAE) i percentyle LN są zapisywane, ale jako Summary Results co Integration Period (minimum 1 s), nie w strumieniu loggera.** Datasheet: "Sound Level Meter Results | (...) Lxye (SEL), LN (LEQ STATISTICS), Lden, LEPd (...)"; "Statistics | Ln (L1-L99), complete histogram in meter mode". Widma 1/1 i 1/3 oktawy to osobne opcje płatne (SF 971_03, SF 971A_1, SF 971A_3).
    Oba modele: klasa 1 wg IEC 61672-1:2013, zatwierdzenie typu GUM. Pliki: .SVL (dane), .SVT (konfiguracja), .WAV (audio, tylko 971A). Odczyt i eksport do CSV: darmowe SvanPC++ oraz Supervisor.

13. **Czy z samego logu LAeq,1s da się odtworzyć zdarzenie impulsywne:** częściowo.
    - **SEL: tak.** Sumowanie energetyczne po sekundach, SEL = 10*log10(suma 10^(Li/10) * ti / t0), t0 = 1 s. Przy przejeździe tramwaju trwającym 5-15 s krok 1 s daje kilkanaście próbek na zdarzenie, co jest wystarczające, a zał. nr 3 cz. F pkt 2 wprost dopuszcza takie wyznaczanie w laboratorium (pkt 7 wyżej).
    - **LAFmax pojedynczego trzasku: nie, będzie zaniżony.** LAeq uśredniony po 1 s rozmywa pik trwający 35-200 ms. Zaniżenie to wprost 10*log10(t_zdarzenia / 1 s): dla 125 ms (stała FAST) około 9 dB, dla 35 ms (stała IMPULSE) około 14,6 dB. To arytmetyka uśredniania energetycznego, nie wartość z literatury, ale pokazuje rząd wielkości problemu. **Dlatego nie wystarczy żądać "logu", trzeba żądać logu z wartościami Lmax per krok** (pkt 11), a najlepiej dodatkowo z krokiem 100 ms.
    - Wniosek praktyczny do petitum: żądać (a) pliku .SVL w formacie natywnym, (b) eksportu CSV z kolumnami Leq, Lmax, Lmin, Lpeak per krok loggera, (c) Summary Results z LAE i percentylami, (d) informacji o faktycznie ustawionym Logger Step i o tym, które wyniki były logowane.

### D. Podstawa prawna: ustawa OOŚ bije UDIP

Ustawa z 3.10.2008 o udostępnianiu informacji o środowisku i jego ochronie, udziale społeczeństwa w ochronie środowiska oraz o ocenach oddziaływania na środowisko, tekst jednolity [Dz.U. 2026 poz. 670](https://api.sejm.gov.pl/eli/acts/DU/2026/670/text.pdf). Cytaty dosłowne z tego tekstu.

14. **Art. 18 pkt 4 OOŚ wyłącza najgroźniejsze podstawy odmowy.** "Przepisów art. 16 ust. 1 **pkt 4-7 i 10** nie stosuje się, jeżeli informacja dotyczy: (...) 4) **poziomu emitowanego hałasu**". Wyłączone zostają zatem: ochrona danych osobowych osób trzecich (pkt 4), dane dostarczone dobrowolnie przez osoby trzecie (pkt 5), ochrona stanu środowiska (pkt 6), **ochrona informacji o wartości handlowej i danych technologicznych objętych tajemnicą przedsiębiorstwa (pkt 7)** oraz tajemnica statystyczna (pkt 10). **UDIP nie ma odpowiednika tego przepisu.** To jednocześnie usuwa zarzut RODO i najbardziej prawdopodobną linię obrony "know-how laboratorium BAASA".

15. **Art. 8 ust. 1 w zw. z art. 3 ust. 1 pkt 2 OOŚ zamyka wybieg "dane zostały u wykonawcy".** Art. 8 ust. 1: "Władze publiczne są obowiązane do udostępniania każdemu informacji o środowisku i jego ochronie, które są informacjami znajdującymi się w posiadaniu władz publicznych **lub informacjami przeznaczonymi dla władz publicznych** (...)". Art. 3 ust. 1 pkt 2: "informacji przeznaczonej dla władz publicznych rozumie się przez to informację, którą **w imieniu władz publicznych dysponują osoby trzecie**, w tym też informację, **której władze publiczne mają prawo żądać od osób trzecich**". Art. 19 ust. 2: jeżeli wniosek dotyczy informacji nieznajdującej się w posiadaniu, władze publiczne w 14 dni przekazują wniosek podmiotowi, który ją posiada, i powiadamiają wnioskodawcę.
    Na gruncie UDIP organ broni się skutecznie twierdzeniem "nie posiadamy" (art. 4 ust. 3 UDIP). Na gruncie OOŚ nie.

16. **Pozostałe przepisy OOŚ przydatne w petitum.** Art. 4: "Każdy ma prawo do informacji o środowisku i jego ochronie." Art. 9 ust. 1 pkt 2: udostępnieniu podlegają informacje dotyczące **emisji** (hałas jest emisją energii: art. 3 pkt 4 lit. b POŚ wymienia "energie, takie jak ciepło, hałas, wibracje lub pola elektromagnetyczne"). Art. 9 ust. 2: udostępnienie "w formie ustnej, pisemnej, wizualnej, **dźwiękowej, elektronicznej** lub innej formie" (podstawa do żądania pliku, nie skanu PDF). **Art. 9 ust. 3**: "Udostępniając informacje, o których mowa w ust. 1 pkt 2, władze publiczne informują także, na wniosek podmiotu żądającego informacji, o **miejscu, w którym znajdują się dane na temat metod przeprowadzania pomiarów, w tym sposobów poboru i przetwarzania próbek oraz sposobów interpretacji uzyskanych danych, które posłużyły do wytworzenia udostępnianej informacji**, lub odsyłają do stosownych metodyk referencyjnych w tym zakresie" (jedyny w polskim prawie przepis wprost adresujący warstwę danych źródłowych pod opracowaniem). Art. 11: udostępniając informacje przekazane przez osoby trzecie, wskazuje się źródło ich pochodzenia. Art. 13: nie wymaga się wykazania interesu prawnego ani faktycznego. Art. 14 ust. 1-2: bez zbędnej zwłoki, nie później niż **miesiąc**, przedłużenie do 2 miesięcy. Art. 15 ust. 1: udostępnienie "w sposób i w formie określonych we wniosku". Art. 20 ust. 1: **odmowa zawsze w drodze decyzji**; ust. 2: przyspieszona ścieżka sądowa (akta i odpowiedź w 15 dni, rozpoznanie skargi w 30 dni).
    **W ustawie OOŚ nie ma instytucji informacji przetworzonej**, więc znika cała oś sporu o "szczególnie istotny interes publiczny".

17. **ZDM jest bezspornie podmiotem zobowiązanym.** Komunalna jednostka budżetowa Miasta Poznania (ul. Wilczak 17, 61-623 Poznań, zdm@zdm.poznan.pl). Na gruncie UDIP: art. 4 ust. 1 pkt 4. Na gruncie OOŚ: art. 3 ust. 1 pkt 15a ("władze publiczne (...) organy administracji") w zw. z art. 3 ust. 1 pkt 9 lit. a i b, przy czym lit. b w obecnym brzmieniu obejmuje "**inne podmioty wykonujące zadania publiczne dotyczące środowiska i jego ochrony**" (pierwotny tekst z 2008 r. wymagał powołania "z mocy prawa lub na podstawie porozumień", ten warunek zniknął).

18. **BAASA jako adresat: możliwe, ale ryzykowne i bez precedensu wprost.** Art. 4 ust. 1 pkt 5 UDIP obejmuje podmioty wykonujące zadania publiczne. Linia korzystna: NSA 4.12.2015 **I OSK 8/15** ("Kryterium przesądzającym jest zatem nie charakter prawny organu (...) a kryterium przedmiotowe, wykonywanie zadań publicznych"; ale też zastrzeżenie: przekształcenie zadania tradycyjnie prywatnego w publiczne wymaga "wyraźnej normy prawnej"), WSA Łódź 15.09.2022 **II SAB/Łd 90/22** (prywatna spółka realizująca umowę z gminą na transport zbiorowy jest zobowiązana), WSA Olsztyn 23.01.2020 **II SAB/Ol 95/19**, NSA 6.09.2022 **III OSK 1571/21**. Linia niekorzystna: NSA 4.04.2019 **I OSK 1605/17** ("o udostępnieniu informacji nie przesądza i nie wystarcza określony status podmiotu (...) Żądana informacja musi bowiem wynikać z wykonywania zadania publicznego (...) To jest kryterium pierwotne").
    **Nie znaleziono orzeczenia rozstrzygającego wprost status akredytowanego laboratorium pomiarowego.** To luka. Argument za istnieniem "wyraźnej normy prawnej" z I OSK 8/15: art. 175 ust. 1 POŚ czyni pomiary obowiązkiem publicznoprawnym, a BAASA realizuje cudzy obowiązek ustawowy. Argument przeciw: ZDM kupił usługę techniczną, nie przekazał zadania. Spór realny, procesowo długi.

19. **Orzecznictwo wspierające żądanie skierowane do ZDM** (sygnatury zebrane z lustra CBOSA orzeczenia-nsa.pl i bazy Sieci Obywatelskiej Watchdog; przed użyciem w piśmie potwierdzić w CBOSA, patrz "Do weryfikacji"):
    - NSA 9.02.2007 **I OSK 517/06**: "Informacją publiczną są nie tylko dokumenty bezpośrednio zredagowane (...) ale także te dokumenty, których organ używa do zrealizowania powierzonych mu zadań", nawet wykonane przez podmioty zewnętrzne.
    - WSA Poznań 14.04.2023 **IV SAB/Po 31/23** (analogia bliska 1:1, dokumentacja powykonawcza wykonawcy żądana od organu): "dokumenty związane z procesem inwestycyjnym realizowanym przez podmiot publiczny stanowią informację publiczną (...) informację o sposobie gospodarowania majątkiem publicznym (art. 6 ust. 1 pkt 5 u.d.i.p.)"; "Żądana dokumentacja powykonawcza bez wątpienia należy do szeroko rozumianej sfery faktów". Sąd stwierdził bezczynność.
    - NSA 22.02.2019 **I OSK 473/17** i WSA Warszawa 20.04.2021 **II SAB/Wa 104/21**: "nie jest wystarczające zawarcie w piśmie informacyjnym lakonicznego stwierdzenia, iż podmiot obowiązany wnioskowanej informacji nie posiada (...) powinien twierdzenie to uwiarygodnić".
    - NSA 12.12.2012 **I OSK 2149/12**: "opracowania, mapy i ekspertyzy załączone do dokumentów i sporządzone na zlecenie organu administracji nie są chronione prawem autorskim w sposób uniemożliwiający ich udostępnienie jako informacji publicznej".
    - NSA 27.01.2012 **I OSK 2130/11** (a contrario, na korzyść): "Informację publiczną stanowią wyłącznie dane obiektywne lub fakty, a nie kwestie ocenne czy postulatywne". Log przyrządu to czysty zapis faktów fizycznych.
    - NSA 19.04.2023 **III OSK 3749/21**: "Pojęcie 'dokumentu wewnętrznego' należy interpretować wąsko, stanowi bowiem wyjątek od zasady dostępu do informacji publicznej".
    - NSA 14.10.2022 **III OSK 5418/21**: anonimizacja to zabieg techniczny i nie czyni informacji przetworzoną.
    - WSA Gliwice 7.04.2022 **III SAB/Gl 80/22**: przy kolizji reżimów organ ma obowiązek zbadać, czy żądana informacja nie jest informacją o środowisku, i pisemnie powiadomić o zmianie trybu; milczenie to bezczynność.
    - Linia ryzyka po stronie ZDM: NSA 24.09.2015 **I OSK 1681/14** (ekspertyzy zewnętrzne jako etap kształtowania stanowiska) i NSA 10.09.2024 **III OSK 2399/22** (studium korytarzowe GDDKiA jako materiał pomocniczy nieprzesądzający kierunków działania organu, więc nie informacja publiczna). To najbliższa dostępna ZDM obrona.

20. **Umowy ZDM-BAASA są jawne i już zidentyfikowane w rejestrze umów BIP Poznania** ([filtr kontrahenta](https://bip.poznan.pl/bip/rejestr-umow/?ru_kontrahent_in=BAASA)). Postępowanie "Pomiary poziomów hałasu w otoczeniu dróg krajowych, wojewódzkich, powiatowych i gminnych oraz hałasu tramwajowego", 4 zadania, łącznie około 928 tys. zł, wszystkie umowy z 13.04.2026:

    | Nr umowy | Wykonawca | Zadanie | Wartość |
    |---|---|---|---|
    | DZ.RO.344.66.2026 | LGL Akustyka Sp. z o.o. | Zadanie 1 | 194 832,00 zł |
    | DZ.RO.344.67.2026 | BAASA Acoustics Sp.j. | Zadanie 2 | 247 230,00 zł |
    | DZ.RO.344.68.2026 | BAASA Acoustics Sp.j. | Zadanie 3 | 269 370,00 zł |
    | DZ.RO.344.69.2026 | BAASA Acoustics Sp.j. | Zadanie 4 | 216 480,00 zł |

    Znak ZDM-RO.401.544.2026 to numer sprawy korespondencyjnej, nie numer umowy. Rejestr publikuje wyłącznie metrykę, nie treść, więc treść umowy, SWZ i OPZ trzeba pozyskać wnioskiem. Centralny Rejestr Umów (art. 34a ustawy o finansach publicznych, rejestrumow.gov.pl) tych umów **nie pokaże**: rejestr obejmuje umowy zawarte od 1.07.2026, a te są z 13.04.2026.
    Jawność umów i dokumentów postępowania: NSA 17.06.2026 **III OSK 2278/25**, WSA Bydgoszcz 23.02.2021 **II SA/Bd 878/20**. Sama deklaracja tajemnicy przedsiębiorcy nie wystarcza: WSA Opole **II SA/Op 289/21**.

## Wniosek operacyjny (rekomendacja)

**Wniosek warto napisać. Adresat: ZDM Poznań. Podstawa główna: ustawa OOŚ, posiłkowo UDIP. Do BAASA dopiero w drugim kroku, jeśli ZDM odpowie, że danych nie posiada i nie ma prawa ich żądać.**

Dlaczego OOŚ, a nie UDIP:
1. art. 18 pkt 4 OOŚ zakazuje odmowy z powołaniem na tajemnicę przedsiębiorstwa i na dane osobowe, gdy informacja dotyczy poziomu emitowanego hałasu (UDIP nie ma odpowiednika);
2. art. 8 ust. 1 w zw. z art. 3 ust. 1 pkt 2 OOŚ obejmuje dane, którymi dysponuje wykonawca i których ZDM ma prawo żądać (UDIP nie ma odpowiednika);
3. w OOŚ nie ma informacji przetworzonej, więc nie trzeba wykazywać szczególnie istotnego interesu publicznego;
4. każda odmowa musi być decyzją (art. 20 ust. 1 OOŚ), a ścieżka sądowa jest przyspieszona (art. 20 ust. 2).
Koszty tego wyboru: termin miesiąc zamiast 14 dni, forma pisemna wniosku (art. 12 ust. 1 OOŚ), możliwe drobne opłaty za wyszukanie i kopie.

Proponowane petitum (rozbić na punkty, żeby każdy dało się osobno zaskarżyć):
- a) **protokoły pomiarów** w pełnym zakresie zał. nr 3 cz. I pkt 1 rozp. MŚ z 16.06.2011 dla wszystkich 5 punktów, w tym tabele 2-6 (nie same sprawozdania, które już są w posiadaniu mieszkańca);
- b) **pliki źródłowe z miernika** SVAN 971/971A (.SVL, ewentualnie .WAV) w formacie natywnym oraz eksport CSV zawierający dla każdego kroku loggera wartości **Leq, Lmax, Lmin, Lpeak** wraz ze znacznikami czasu, a także Summary Results z LAE i percentylami LN; podstawa faktyczna: zał. nr 3 cz. C pkt 3 ppkt 2 nakazuje zapamiętanie wyników "w postaci źródłowej";
- c) informacja o **faktycznie ustawionym Logger Step** i o tym, które wyniki były logowane, oraz czy podczas pomiarów była aktywna opcja rejestracji audio (SF 971_15 / SF 971A_15) i czy z niej skorzystano;
- d) na podstawie **art. 9 ust. 3 OOŚ**: wskazanie miejsca, w którym znajdują się dane o metodach przeprowadzania pomiarów i sposobach interpretacji uzyskanych danych;
- e) wyjaśnienie, którą procedurę z zał. nr 3 cz. A pkt 3 zastosowano dla **hałasu tramwajowego** i, jeśli nie zastosowano procedury z cz. F (pojedyncze zdarzenia akustyczne wg klas typów tramwajów, cz. F pkt 11), na jakiej podstawie odstąpiono od metodyki referencyjnej;
- f) na podstawie UDIP: **umowy DZ.RO.344.66-69.2026** wraz z załącznikami, SWZ i OPZ postępowania;
- g) informacja, czy i kiedy ZDM przedłożył wyniki organowi ochrony środowiska i GIOŚ w trybie art. 177 ust. 1 POŚ.

Konstrukcje ratunkowe do wpisania wprost w pismo:
- "Jeżeli ZDM nie dysponuje fizycznie danymi z ppkt b), wnoszę o ich udostępnienie jako informacji przeznaczonej dla władz publicznych w rozumieniu art. 3 ust. 1 pkt 2 ustawy OOŚ, tj. informacji, którą w imieniu ZDM dysponuje wykonawca i której ZDM ma prawo żądać."
- "W zakresie, w jakim organ uzna, że żądana informacja nie jest informacją o środowisku, wnoszę o rozpoznanie wniosku na podstawie art. 2 ust. 1 i art. 10 ust. 1 UDIP." (zamyka odsyłanie między reżimami, por. III SAB/Gl 80/22)
- Uprzedzić zarzut dokumentu wewnętrznego: "Żądane dane mają charakter wyłącznie faktograficzny, są automatycznym zapisem przyrządu pomiarowego, nie zawierają ocen ani postulatów (por. I OSK 2130/11, III OSK 3749/21, IV SAB/Po 31/23)."
- **Nigdy nie pisać "proszę wyliczyć LAmax/SEL"** (to zamówienie na przetworzenie i gotowa podstawa do wezwania o szczególnie istotny interes publiczny na gruncie UDIP). Zawsze: "proszę o kopię danych".
- Poprosić o odpowiedź w postaci elektronicznej (art. 15 ust. 1 OOŚ).

Ryzyko odmowy, realistycznie:
- **art. 16 ust. 2 pkt 2 OOŚ** (dokumenty przeznaczone do wewnętrznego komunikowania się) nie jest wyłączony przez art. 18. Kontra: sprawozdanie i protokół akredytowanego laboratorium to produkt odpłatnej umowy z podmiotem zewnętrznym, nie komunikacja wewnętrzna ZDM.
- **art. 16 ust. 1 pkt 3 OOŚ** (prawa własności intelektualnej) nie jest wyłączony przez art. 18. To jedyna realnie żywa przesłanka. Kontra: I OSK 2149/12 oraz argument, że automatyczny zapis przyrządu nie jest utworem (brak indywidualnego charakteru).
- **art. 16 ust. 2 pkt 4 OOŚ** (wniosek zbyt ogólny) neutralizuje się precyzją petitum, stąd rozbicie na ppkt a-g.
- "Nie posiadamy plików źródłowych, mamy tylko PDF" to najbardziej prawdopodobna odpowiedź faktyczna. Kontrargumenty: art. 175 ust. 5 w zw. z art. 147 ust. 6 POŚ (ewidencja i 5 lat przechowywania), art. 8 ust. 1 w zw. z art. 3 ust. 1 pkt 2 OOŚ, art. 19 ust. 2 OOŚ, I OSK 473/17.

Kolejność działań: **priorytet nadal ma pytanie już zadane ZDM 17.09.2026** (klasyfikacja terenu dla PPH3.58, działania naprawcze wobec przekroczeń PPH3.05 i PPH4.16). Wniosek o dane źródłowe wysłać jako osobne pismo, po otrzymaniu tamtej odpowiedzi albo po upływie terminu, żeby nie mieszać dwóch ścieżek proceduralnych w jednej sprawie. Adresaci równolegli, którzy mogą mieć te same dane: Prezydent Miasta Poznania jako organ ochrony środowiska (ksr@um.poznan.pl) oraz GIOŚ, obaj jako ustawowi adresaci wyników z art. 177 ust. 1 POŚ.

## Do weryfikacji przed użyciem w piśmie urzędowym

- Sygnatury z pkt 18-20 pochodzą z lustra CBOSA (orzeczenia-nsa.pl) i z bazy Sieci Obywatelskiej Watchdog; sama CBOSA (orzeczenia.nsa.gov.pl) była w obu turach niedostępna dla narzędzi automatycznych. Przed cytowaniem w piśmie potwierdzić w CBOSA co najmniej: I OSK 517/06, I OSK 2149/12, I OSK 2130/11, IV SAB/Po 31/23, I OSK 473/17, III OSK 3749/21, III OSK 5418/21, III SAB/Gl 80/22, I OSK 8/15, I OSK 1605/17, II SAB/Łd 90/22.
- Nie odnaleziono orzeczenia dotyczącego wprost udostępnienia surowych danych z miernika hałasu ani danych stanowiących podstawę mapy akustycznej. To luka, nie ustalenie negatywne. Zalecane frazy do przeszukania CBOSA z przeglądarki: "poziom emitowanego hałasu" + "art. 18", "wyniki pomiarów hałasu" + "udostępnienie", ustawa OOŚ art. 9 ust. 3.
- Który z odcinków (Zadanie 2, 3 czy 4) obejmuje ul. Dąbrowskiego: nie wynika z rejestru umów, trzeba z OPZ.
- Rozbieżność w dokumentacji Svantek: częstotliwość próbkowania audio SV 971A (48 kHz w karcie katalogowej vs 12/24 kHz w instrukcji v.1.03). Bez znaczenia dla wniosku, ale nie cytować konkretnej wartości.
- Zaniżenie LAFmax przy odczycie z LAeq,1s (pkt 13) to obliczenie własne z definicji uśredniania energetycznego, nie wartość zaczerpnięta z normy ani z literatury. Nie przypisywać jej źródła.
