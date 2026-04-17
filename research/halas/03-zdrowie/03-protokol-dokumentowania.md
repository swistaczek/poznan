---
title: "Protokół dokumentowania szkody zdrowotnej — POZ, ICD-10, ABPM, PSG"
type: reference
domain: halas
source: wyniki-03-zdrowie-publiczne.md
updated: 2026-04-17
entities:
  - NFZ
  - PZH
  - GIOŚ
  - POZ
  - PSSE
  - WIOŚ
acts:
  - KC-23
  - KC-24
  - KC-444
  - KC-448
  - ustawa-o-prawach-pacjenta-art-14
  - ustawa-o-prawach-pacjenta-art-23
  - ustawa-o-prawach-pacjenta-art-26
  - ICD-10
signatures:
  - V-CSK-314/14
  - V-CSK-112/12
---

# Protokół dokumentowania szkód zdrowotnych u indywidualnych mieszkańców

Aby skutecznie odeprzeć narrację organów deprecjonujących problem jako "subiektywny" i przygotować solidny fundament dowodowy pod postępowania w oparciu o prawo cywilne (ochrona dóbr osobistych, zadośćuczynienie za uszczerbek na zdrowiu — **art. 23, 24, 444, 448 k.c.**), aktywiści oraz mieszkańcy muszą wdrożyć precyzyjny protokół medyczno-prawny.

**Cel**: udowodnienie pełnego łańcucha przyczynowo-skutkowego:

> Emisja dźwięku/wibracji → Narażenie ekspozycyjne → Mierzalny skutek patofizjologiczny

## Krok 1. Obiektywizacja ekspozycji

- Pobrać dane z państwowego systemu mapowania akustycznego (operaty GIOŚ, mapa miasta) wykazujące ponadnormatywny poziom $L_{DEN}$ i $L_{NIGHT}$ pod konkretnym adresem.
- Inżynieryjny raport o poziomie **wibracji WBV** od niezależnego rzeczoznawcy budowlanego/akustyka (patrz PN-88/B-02171).
- Warto: pomiary własne mikrofonem przyłóżkowym z synchronizacją czasową do rozkładu jazdy MPK.

## Krok 2. Wywiad POZ — krytyczny element łańcucha

Obywatel zgłaszający się do lekarza rodzinnego **nie może poprzestać na opisie "złego samopoczucia"**. W dokumentacji z wizyty pacjent musi wymusić na lekarzu wpis w wywiadzie środowiskowym o brzmieniu:

> _"Pacjent zgłasza nasilone, przewlekłe mikrowybudzenia nocne oraz objawy tachykardii korelujące bezpośrednio w czasie z przejazdami ciężkiego transportu szynowego w bezpośrednim sąsiedztwie miejsca zamieszkania."_

Na wizytę przynieść:

1. Wydruk mapy akustycznej z SIP Poznań z Twoim adresem i wartościami $L_{DEN}$/$L_{NIGHT}$.
2. Wydruk rekomendacji WHO ENG 2018 (str. 5–6, tabela "strong" dla railway noise: <54/<44 dB).
3. Dzienniczek snu z minimum 14 dni.
4. Wyniki ABPM Holter (jeśli posiadasz).

**Podstawa prawna żądania wpisu**: art. 23 ustawy o prawach pacjenta — prawo do rzetelnej dokumentacji zawierającej wszystkie istotne informacje o stanie zdrowia i czynnikach wpływających.

**Gdy lekarz odmawia**: złóż pisemne uzupełnienie dokumentacji (art. 14 ust. 3 ustawy o prawach pacjenta) — sama próba i odmowa w aktach stanowią dowód procesowy.

_Uwaga: w/w formuła wpisu + lista załączników nadają się do wyodrębnienia jako szablon pisma "Wniosek o uzupełnienie dokumentacji medycznej o wywiad środowiskowy" — kandydat na `szablony/halas/wniosek-uzupelnienie-dokumentacji-poz.md`. Nie wyodrębniono w tym przebiegu, bo oryginał zawiera opis protokołu, nie gotową formułę pisma z polami `{{...}}`._

## Krok 3. Klasyfikacja ICD-10

Prawnicy środowiskowi wymagają jednoznacznego przyporządkowania objawów do jednostek nozologicznych. Lekarz POZ poza kodami podstawowymi:

- **I10** — nadciśnienie tętnicze pierwotne.
- **G47** / **G47.0** — zaburzenia snu / zaburzenia zasypiania i utrzymania snu.
- **F43** / **F43.2** — reakcja na ciężki stres / reakcja adaptacyjna.

— musi użyć **rozszerzających** kodów z grupy "Czynniki wpływające na stan zdrowia i kontakt ze służbą zdrowia":

- **Z55–Z65** — problemy związane z warunkami socjoekonomicznymi i psychospołecznymi.
- **Z91.89** — inne określone czynniki ryzyka w wywiadzie (personal risk factors not elsewhere classified).

Legalizuje to klinicznie powiązanie choroby z otoczeniem zamieszkania.

## Krok 4. Specjalistyczna weryfikacja patofizjologiczna

### Kardiologia — ABPM Holter 24 h

Ambulatory Blood Pressure Monitoring. Najważniejszy dowód dla biegłego kardiologa: **brak fizjologicznego spadku ciśnienia w nocy**.

- Profil **dipper** (zdrowy) — spadek ciśnienia o 10–20% w nocy vs dzień.
- Profil **non-dipper** — spadek <10%.
- Profil **reverse dipper** — ciśnienie nocne > dzienne.

Non-dipper ma 27% wyższe ryzyko incydentów sercowo-naczyniowych przy identycznym ciśnieniu średnim dziennym (Salles et al., Hypertension 2016, DOI: **10.1161/HYPERTENSIONAHA.115.06981**, N=17 312, HR 1.27, 95% CI 1.10–1.47).

Non-dipper jest **patognomoniczny** dla przewlekłej aktywacji układu współczulnego — dokładnie takiej, jaką wywołuje nocny hałas tramwajowy (Griefahn-Basner effect, non-arousal cardiovascular responses). Z punktu widzenia sądu — **twardy, obiektywny, mierzony aparatem medycznym dowód uszkodzenia wegetatywnego**, niemożliwy do zakwestionowania argumentem o symulacji czy subiektywności.

Badanie refundowane przez NFZ; koszt prywatny 120–200 zł. Zalecenie: wykonać 2× w odstępie 3–6 mies. + 1× w warunkach kontrolnych (nocleg poza strefą hałasu). Porównanie "dom vs kontrola" to złoty standard opisywany w pracach **Münzel et al., European Heart Journal 2018, DOI: 10.1093/eurheartj/ehy481**.

### Polisomnografia (PSG)

Złoty standard diagnostyki snu (AASM Manual 2023). Kluczowe parametry:

- **Arousal index** — liczba mikrowybudzeń >3 s na godzinę snu; wartości >15/h są patologiczne. WHO ENG 2018: przejazd pociągu generuje ~0.7 arousals per event u osób eksponowanych.
- **Redukcja SWS (faza N3)** — u narażonych spada z normy 15–25% TST do 8–12%.
- **Fragmentacja REM**.

Najmocniejszy dowód: jednoczesny zapis dźwięku mikrofonem przyłóżkowym + synchroniczny EEG → biegły wykazuje zależność przyczynowo-skutkową "zdarzenie akustyczne X dB LAmax → mikrowybudzenie". Protokół stosowany przez **Basner et al., Sleep 2011, DOI: 10.1093/sleep/34.1.11** (praca dla FAA).

Koszt prywatny 800–1 500 zł; bywa refundowane przez NFZ po skierowaniu z poradni zaburzeń snu (kod G47). Dla pozwu idealnie: **2 noce w domu + 1 noc w laboratorium poza strefą hałasu** (kontrola własna).

### Neurologia / psychiatria

Dokumentacja narastającego upośledzenia funkcji kognitywnych i somatyzacji lękowej. Kody ICD-10 dot. ośrodkowego układu nerwowego:

- **G09–G13** — choroby układu ruchu i ośrodkowego układu nerwowego.
- **G54** — uszkodzenia korzeni nerwowych (w przypadku objawów somatycznych WBV).

Dowodzi to, że chroniczny deficyt snu doprowadził do trwałych następstw.

## Krok 5. Dzienniczek samoobserwacji + korelacja z rozkładem MPK

- Dokładny wykaz godzinowy nocnych wybudzeń, napadów lęku i bólu.
- Korelacja z oficjalnym, publicznie dostępnym rozkładem jazdy oraz godzinami prac technicznych (przejazdy szlifierek torowych).
- Zgromadzenie teczek medycznych przez **10–20 mieszkańców tej samej kamienicy** buduje potężny, powtarzalny materiał dowodowy dla biegłych medycyny sądowej.

## Łańcuch czasowy — odparcie zarzutu "zawsze tu było głośno"

Dla odparcia obrony urzędu (volenti non fit iniuria / "wiedzieliście kupując"):

1. Pełna kopia dokumentacji POZ z ≥10 lat (art. 26 ustawy o prawach pacjenta, 30 dni, bezpłatnie) — oś czasu leków nasennych, hipotensyjnych, przeciwlękowych.
2. Z ZDM/MPK/archiwum miasta — daty zmian infrastruktury: wymiana taboru na Tramino (ok. 2012–2015 [do weryfikacji — rok dokładny]), zwiększenie częstotliwości linii, daty szlifowań na Dąbrowskiego.
3. Korelacja obu osi — spełnia kryteria przyczynowości **Bradforda Hilla** (temporality + biological gradient).
4. Grupa kontrolna — 10–15 sąsiadów z oficyn (niska ekspozycja) + 10–15 z frontu (wysoka). Dla N=30, przy oczekiwanym RR 1.5, różnica istotna statystycznie (p<0.05).
5. Świadkowie — sąsiedzi, rodzina obserwująca pogorszenie.

Standard dowodu w sądzie cywilnym: "uprawdopodobnienie w wysokim stopniu" (art. 6 k.c. + art. 233 k.p.c.) — nie ponad wszelką wątpliwość jak w karnym.

Orzecznictwo wspierające:

- **SN V CSK 314/14** (26.03.2015) — poszkodowany immisjami nie ma obowiązku ponoszenia kosztów ochrony przed nimi; zasada "zanieczyszczający płaci".
- **SN V CSK 112/12** — zgoda na zamieszkanie w mieście nie jest zgodą na immisje ponadnormatywne.

## Cisza jako dobro publiczne — soundscape

Argumentacja urzędnicza "w mieście musi być głośno" jest **archaiczna**. Doktryna WHO **"Quiet Areas in Europe"**: prawo do środowiska o nienaruszonej strukturze akustycznej (szczególnie w porze spoczynku) to **fundamentalne prawo obywatelskie** i element zdrowia publicznego, nie luksus dla posiadaczy podmiejskich willi.

## Rachunek Koszt-Korzyść (CBA) — argument ekonomiczny

Odpowiedź miasta/MPK na żądania natychmiastowych napraw: "brak środków w budżetach rocznych (25–30 mln zł na naprawy w Poznaniu)". Retoryka ignoruje **koszty zewnętrzne** ponoszone już przez społeczeństwo.

Metodyka monetaryzacji wskaźnika DALY ("Handbook on the external costs of transport", wytyczne UE): **1 DALY ≈ 70 000 EUR (>300 000 PLN)** — czysty koszt z tytułu utraconej produktywności, skrócenia życia, wydatków medycznych.

### Symulacja dla kwartału miejskiego

- EEA: ponadnormatywny hałas transportowy → ~300 DALY / rok / 100 000 mieszkańców.
- Populacja 20 000 osób w strefie najwyższego oddziaływania → **60 DALY / rok**.
- Koszt roczny: 60 × 70 000 EUR = **4 200 000 EUR ≈ 18 mln PLN / rok** dla małego fragmentu miasta.

Koszty NFZ — przykład T2DM:

- Średni roczny koszt pacjenta z zaawansowaną cukrzycą w POZ: **243 PLN**.
- Hospitalizacje (ślepota cukrzycowa, stopa cukrzycowa, amputacje, niewydolność nerek) → **miliardy PLN / rok w skali makro**.
- Koszty pacjenta z kieszeni: farmakoterapia uspokajająca, hipotensyjna, leczenie zaburzeń psychicznych.

**Konkluzja**: 2 lata zwłoki z remontem torowiska na ul. Dąbrowskiego generują przez NFZ, ZUS i pracodawców straty **przekraczające roczny budżet naprawczy MPK Poznań**. Zaniechanie inwestycji jest drastycznie droższe niż jej realizacja.
