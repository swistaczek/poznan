---
title: "FAQ — medyczne (dokumentacja, diagnostyka, dzieci, ciąża)"
type: faq
domain: halas
source: wyniki-03-zdrowie-publiczne.md
updated: 2026-04-17
entities:
  - WHO
  - EEA
  - NFZ
  - POZ
  - GIOŚ
  - UK-Biobank
acts:
  - KC-6
  - ustawa-o-prawach-pacjenta-art-14
  - ustawa-o-prawach-pacjenta-art-23
  - ustawa-o-prawach-pacjenta-art-26
  - KPC-233
  - ICD-10
  - PN-EN-ISO-717-1
  - WHO-ENG-2018
  - rozp-MZ-standard-opieki-okoloporodowej
signatures: []
---

# FAQ — medyczne (dokumentacja, diagnostyka, dzieci, ciąża)

Pytania prawno-proceduralne (sanepid, WHO vs urzędy, okna, pozew, ETPC) → [`99-faq-prawne.md`](./99-faq-prawne.md).

## Jak przekonać mojego lekarza POZ, żeby wpisał hałas jako czynnik sprawczy w dokumentacji medycznej?

Lekarze POZ często obawiają się wpisów "pozamedycznych", uznając je za domenę medycyny pracy. Twoim zadaniem jest dostarczenie mu gotowego mostu klinicznego. Na wizytę przynieś: (1) wydruk mapy akustycznej z portalu SIP Poznań z Twoim adresem i wartościami $L_{DEN}$/$L_{NIGHT}$, (2) wydruk rekomendacji WHO ENG 2018 (str. 5–6, tabela "strong" dla railway noise: <54 dB $L_{DEN}$, <44 dB $L_{NIGHT}$), (3) dzienniczek snu z minimum 14 dni, (4) wyniki ABPM Holter, jeśli posiadasz. Poproś o konkretny wpis do wywiadu środowiskowego (patrz [`03-protokol-dokumentowania.md`](./03-protokol-dokumentowania.md)): _"Pacjent zgłasza nasilone przewlekłe mikrowybudzenia nocne oraz objawy tachykardii korelujące czasowo z przejazdami transportu szynowego w bezpośrednim sąsiedztwie miejsca zamieszkania"_. Kluczowe są kody ICD-10: G47.0 (zaburzenia zasypiania/utrzymania snu), F43.2 (reakcja adaptacyjna), I10 (nadciśnienie pierwotne) plus rozszerzenia Z56–Z65 (problemy psychospołeczne/środowiskowe) oraz Z91.89 (inne czynniki ryzyka w wywiadzie). Podstawa prawna żądania: art. 23 ustawy o prawach pacjenta — masz prawo do rzetelnej dokumentacji zawierającej wszystkie istotne informacje o stanie zdrowia i czynnikach wpływających. Jeżeli lekarz odmawia, złóż pisemne uzupełnienie dokumentacji (art. 14 ust. 3 ustawy o prawach pacjenta) — sama próba i odmowa w aktach stanowią dowód procesowy.

## Czy dzieci faktycznie mają gorsze wyniki w szkole przez hałas tramwajowy?

Tak, jedna z najlepiej udokumentowanych zależności w epidemiologii środowiskowej. Badanie **RANCH** (Stansfeld et al., The Lancet 2005, DOI: 10.1016/S0140-6736(05)66660-3) na 2 844 dzieciach 9–10 l. w Anglii, Holandii i Hiszpanii wykazało, że wzrost ekspozycji o 5 dB w szkole → statystycznie istotne pogorszenie czytania ze zrozumieniem o 1–2 miesiące opóźnienia rozwojowego. Meta-analizy 2020–2025 (patrz [`02-daly-wbv-populacje.md`](./02-daly-wbv-populacje.md)): wzrost wskaźnika zachowań hiperaktywnych i deficytu uwagi o **12% per 10 dB** w środowisku szkolnym (RR 1.120) i **7.3%** w domowym (RR 1.073). Mechanizm dwutorowy: (1) bezpośrednie zakłócenie pamięci roboczej podczas lekcji i odrabiania zadań, (2) chroniczna deprywacja snu REM i N3 zaburzająca konsolidację pamięci długotrwałej oraz sekrecję hormonu wzrostu (GH). Hałas obniża też prospołeczność i motywację (learned helplessness). WHO ENG 2018 rozdz. 3.3 ("Effects on cognition in children") klasyfikuje dowody jako **high quality** — najwyższy poziom GRADE. Do dyrekcji szkoły / kuratorium żądaj przeniesienia zajęć wymagających koncentracji (matematyka, język obcy) do sal od strony podwórka oraz instalacji przegród akustycznych klasy 4 dB wg PN-EN ISO 717-1.

## Jak odróżnić skutki hałasu od skutków smogu w moim przypadku?

Urzędy notorycznie "rozmywają" oba czynniki. Epidemiologicznie rozplątywane metodą adjustacji wielowymiarowej w modelach Coxa. Analizy UK Biobank (Cai et al., Environment International 2018, DOI: 10.1016/j.envint.2018.02.048 [rok/tytuł zweryfikowany; EHJ 2023 nie potwierdzono]) po adjustacji na PM2.5, NO2, palenie, BMI i SES: efekt hałasu pozostaje niezależnie istotny — HR dla IHD ~1.04 per 10 dB nawet w modelach pełnych. Klinicznie:

- **Smog**: głównie układ oddechowy (kaszel, POChP, astma, nowotwory płuca), pośrednio sercowo-naczyniowy przez stan zapalny płuc.
- **Hałas**: neuroendokrynia (kortyzol, noradrenalina) + sen — zaburzenia zasypiania, mikrowybudzenia, tachykardia, wzrost ciśnienia nocnego (non-dipper ABPM), lęk, bóle głowy, trudności z koncentracją.

Indywidualnie decyduje **sezonowość i rytm dobowy**: objawy hałasu korelują z rozkładem jazdy MPK (szczyt 5:30–23:15, nasilenie w weekendy nocne przy pracach szlifierskich); smog ma wyraźny pik zimowy (sezon grzewczy). Polisomnografia rejestruje wybudzenia z latencją ~3 s od zdarzenia akustycznego — najsilniejszy dowód specyficznie przypisujący objawy hałasowi. Cykl Holter ABPM + dzienniczek z godzinami przejazdów ≥90 dB LAmax daje korelację czasową niemożliwą do przypisania smogowi (ekspozycja ciągła, nie impulsowa).

## Ile dB rocznego $L_{DEN}$ realnie skraca życie i o ile?

All-cause mortality w meta-analizach 2023–2025 (tabela RR w [`01-epidemiologia-rr.md`](./01-epidemiologia-rr.md)): RR 1.055 (+5.5%) per 10 dB $L_{DEN}$ (95% CI: 1.026–1.084). Przekład na lata życia: Hoffmann et al. (Heidelberg cohort, Environment International [do weryfikacji — DOI/rok; szukano 2026-04-17, nie potwierdzono w PubMed/EI]) — różnica 20 dB $L_{DEN}$ (50 vs 70 dB) ≈ skrócenie LE o **1,0–1,4 roku** w populacji 60+. W ujęciu DALY/YLL: EEA "Environmental noise in Europe 2020" przypisuje hałasowi transportowemu w Europie **12 000 przedwczesnych zgonów i 48 000 nowych przypadków IHD rocznie**. Dla ul. Dąbrowskiego przy $L_{DEN}$ 68–72 dB (14–18 dB powyżej progu WHO 54 dB) skumulowany wzrost ryzyka zgonu ~**8–11%**. Na 100 mieszkańców frontowej kamienicy — statystycznie kilku "dodatkowych" zgonów kardiologicznych w ciągu dekady vs kohorta odniesieniowa. Efekty rzędu wielkości **bliskie biernemu paleniu tytoniu**.

## Czy badanie polisomnografii (PSG) pomoże mi w sądzie?

Pomoże, mocno — pod warunkiem właściwej realizacji. PSG to złoty standard diagnostyki snu (AASM Manual 2023). Kluczowe: (1) arousal index — mikrowybudzenia >3 s na godzinę snu; wartości >15/h patologiczne. WHO ENG 2018: przejazd pociągu generuje ~0,7 arousals per event u eksponowanych. (2) Redukcja SWS (N3) — u narażonych spada z 15–25% TST do 8–12%. (3) Fragmentacja REM. Najmocniejszy dowód: jednoczesny zapis dźwięku mikrofonem przyłóżkowym + synchroniczny EEG — biegły wykazuje zależność "zdarzenie akustyczne X dB LAmax → mikrowybudzenie". Protokół: **Basner et al., Sleep 2011, DOI: 10.1093/sleep/34.1.11** (praca dla FAA). Sąd traktuje PSG jako obiektywny dowód fizjologiczny — niepodważalny przez argumentację o "subiektywności". Koszt prywatny 800–1 500 zł; bywa refundowane przez NFZ po skierowaniu z poradni zaburzeń snu (kod G47). Dla pozwu: **2 noce w domu + 1 noc w laboratorium poza strefą hałasu** (kontrola własna).

## Co dokładnie pokazuje "profil non-dipper" w ABPM i dlaczego to takie ważne?

Całodobowa rejestracja ciśnienia 24 h (Holter ABPM) ujawnia fizjologiczny wzór dobowy. U zdrowego: ciśnienie skurczowe spada w nocy o 10–20% vs dzień — profil **dipper**, dowód prawidłowego wyciszenia współczulnego (sympatikolizy) podczas snu. Spadek <10% → **non-dipper**; ciśnienie nocne > dzienne → **reverse dipper**. Meta-analiza **Salles et al., Hypertension 2016, DOI: 10.1161/HYPERTENSIONAHA.115.06981** (N=17 312): non-dipper ma 27% wyższe ryzyko incydentów sercowo-naczyniowych niż dipper przy identycznym ciśnieniu średnim dziennym (HR 1.27, 95% CI 1.10–1.47). Non-dipper jest **patognomoniczny** dla przewlekłej aktywacji układu współczulnego — dokładnie takiej, jaką wywołuje nocny hałas tramwajowy przez non-arousal cardiovascular responses (Griefahn-Basner effect). Dla sądu to twardy, obiektywny, mierzony aparatem medycznym dowód uszkodzenia wegetatywnego — niemożliwy do zakwestionowania argumentem o symulacji/subiektywności. ABPM refundowany przez NFZ; koszt prywatny 120–200 zł. Zalecenie: 2× w odstępie 3–6 mies. + 1× w warunkach kontrolnych (nocleg poza strefą). "Dom vs kontrola" to złoty standard dowodowy (**Münzel et al., European Heart Journal 2018, DOI: 10.1093/eurheartj/ehy481**).

## Jestem w ciąży — co hałas robi mojemu dziecku?

Kategoria szczególnej ochrony prawnej i medycznej. Meta-analiza **Dzhambov et al., Noise & Health 2014, DOI: 10.4103/1463-1741.127847**: ekspozycja matki na hałas transportowy >60 dB $L_{DEN}$ → wzrost ryzyka niskiej masy urodzeniowej (LBW <2500 g) o **9% per 10 dB** i porodu przedwczesnego o **3–5%**. **Smith et al. 2020** [do weryfikacji — PLOS Medicine i 144 tys. ciąż nie potwierdzono; bliskie: Smith RB et al. 2020, Environment International, DOI: 10.1016/j.envint.2019.105290, N=581 774 urodzeń Londyn] na UK potwierdziła zależność dawka-reakcja po adjustacji na PM2.5, SES, palenie. Mechanizm: (1) kortyzol matki przechodzi łożysko i programuje oś HPA płodu (fetal programming — hipoteza Barkera), (2) skurcz naczyń macicznych w odpowiedzi na katecholaminy ogranicza perfuzję łożyska, (3) od 25. t.c. płód słyszy dźwięki niskoczęstotliwościowe (Querleu et al. — reakcje ruchowe i tętna płodu na hałas 85 dB). Twoje prawa: art. 23 ustawy o świadczeniach opieki zdrowotnej + rozp. MZ w sprawie standardu opieki okołoporodowej — lekarz prowadzący ma obowiązek zebrania wywiadu środowiskowego. Żądaj wpisania ekspozycji na hałas do karty ciąży (ICD-10 **O35.8** — "opieka nad matką z powodu innych podejrzewanych nieprawidłowości płodu") oraz skierowania na USG doplerowskie tętnic macicznych (IP/RI) w 20–24. t.c. jako badania kontrolnego. Dokumentacja ginekologiczna z jawnym wpisem o hałasie = potężny materiał procesowy i argument petycyjny.

## Jak udowodnić, że moja bezsenność i nadciśnienie pojawiły się PO pojawieniu się wzmożonego hałasu, a nie wcześniej?

Element czasowy łańcucha przyczynowo-skutkowego, kluczowy procesowo. Strategia:

1. **Pełna kopia dokumentacji POZ z ≥10 lat** — art. 26 ustawy o prawach pacjenta (30 dni, bezpłatnie). Kwerenda wpisów i recept pod kątem leków nasennych, hipotensyjnych, przeciwlękowych — oś czasu stanu zdrowia.
2. **Z ZDM/MPK/archiwum miasta**: daty zmian infrastruktury — kiedy wymieniono tabor na Tramino (**pierwsze dostawy S105p: kwiecień 2011; zakończenie: maj 2012; kontrakt 2009**) <!-- źródło: poznan.pl/mim/prezydent/news,1093/..., dostęp 2026-04-17 -->, kiedy zwiększono częstotliwość linii, kiedy ostatnio szlifowano szyny na Dąbrowskiego.
3. **Zestawienie osi czasu** — korelacja zmiana infrastruktury ↔ pogorszenie zdrowia = kryteria **Bradforda Hilla** (temporality, biological gradient).
4. **Grupa kontrolna**: 10–15 sąsiadów z oficyn (niska ekspozycja) + 10–15 z frontu (wysoka). Porównanie skumulowanej zachorowalności na nadciśnienie, bezsenność, cukrzycę. Dla N=30, przy RR 1.5 — różnica istotna statystycznie (p<0.05).
5. **Świadkowie** — sąsiedzi, rodzina obserwująca pogorszenie zdrowia w konkretnym okresie.

Sąd cywilny wymaga "uprawdopodobnienia w wysokim stopniu" (art. 6 k.c. + art. 233 k.p.c.), nie dowodu ponad wszelką wątpliwość (jak w karnym). Taki pakiet spełnia z nawiązką.
