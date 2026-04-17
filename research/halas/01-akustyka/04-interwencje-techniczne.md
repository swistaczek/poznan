---
title: "Inżynieryjna hierarchia interwencji technicznych — koszty, skuteczność, żywotność"
type: reference
domain: halas
source: wyniki-01-akustyka-torowa.md
updated: 2026-04-17
entities: [MPK-Poznań, ZTP, Poznanskie-Inwestycje-Miejskie, Getzner, Pandrol, Edilon-Sedra, Tata-Steel, Speno, Schweerbau]
acts: []
signatures: []
---

# Hierarchia interwencji technicznych (stan 2025/2026, PL)

Rozmyte obietnice „nadchodzących remontów" można zneutralizować egzekwowaniem konkretnych rozwiązań technologicznych. Odpowiedzi ZTM / Poznańskich Inwestycji Miejskich często celowo nie precyzują technologii — poniższa gradacja od doraźnych do strukturalnych.

## Tabela interwencji

### 1. Profilowanie szyn (szlifowanie reprofilujące)

- **Mechanika**: skrawanie wierzchniej warstwy tocznej tarczami ściernymi. Usuwa mikronierówności i corrugation. Likwiduje 250–1000 Hz.
- **Redukcja**: $L_{Aeq}$ –3 do –7 dB.
- **Efekt uboczny**: na łukach R < 50 m szlifowanie tylko szyny wewnętrznej może paradoksalnie **podnieść curve squeal o ok. 10%** (gładsza powierzchnia ułatwia stick-slip).
- **Koszt**: 150–280 zł/mb toru pojedynczego.
- **Żywotność**: 1–3 lata. Wdrożenie szybkie (okna nocne).
- **Dostępność**: Speno, Schweerbau (operują w PL).
- **Status**: bazowe minimum higieny infrastruktury, odpowiednik odśnieżania. Nie traktować jako „inwestycji".

### 2. Zautomatyzowane smarownice torowe (stacjonarne / pokładowe)

- **Mechanika**: szafy z dyszami aplikującymi friction modifier na boczną powierzchnię główki szyny zewnętrznej w łuku lub obrzeżach kół. Likwiduje lateral creepage.
- **Redukcja**: **–8 do –15 dB** w pasmach 4–15 kHz (curve squeal).
- **Koszt**: 60–120 tys. zł za punkt aplikacyjny (para smarująca).
- **Żywotność urządzenia**: ~10 lat. Pojemnik smaru: uzupełnianie **co 2–4 tygodnie**.
- **Pułapka operacyjna**: skuteczność zeruje się w 48 h od opróżnienia zbiornika.
- **Status**: jedyna skuteczna metoda przeciw potężnemu curve squeal na rozjazdach i ciasnych łukach.

### 3. Tłumiki szynowe (rail dampers / absorbers)

- **Mechanika**: klocki ze stopów stali w stratnej otulinie elastomerowej (Tata Steel, Schrey & Veit). Zaciskane bezinwazyjnie z boków szyjki szyny. Zwiększają Track Decay Rate (TDR) — tłumią pasożytnicze fale giętne w stali, ograniczają „dzwonienie" Vignoles'a.
- **Redukcja**: –2 do –5 dB (umiarkowana).
- **Koszt**: 1 200–2 500 zł/mb (klocek + montaż).
- **Żywotność**: > 15–20 lat. Bezobsługowe.
- **Ograniczenie**: skuteczność **tylko na odcinkach prostych**. Nie redukują hałasu koła ani wibracji gruntu.

### 4. Maty podtorowe USM (Under Sleeper Mats) — wibroizolacja dywanowa

- **Mechanika**: arkusze elastomerowe / poliuretanowe o skalibrowanej sztywności dynamicznej (**Getzner Sylomer**, MELT). Układane na podbudowie gruntowej, separują tłuczeń od podłoża.
- **Redukcja**: **–10 do –20 dB** dla pasm poniżej 125 Hz (wibracje gruntu, hałas strukturalny w mieszkaniach).
- **Koszt**: 1 500–3 500 zł/mb (bez kolosalnych prac ziemnych).
- **Żywotność**: 25–35 lat (cykl życia warstwy nośnej).
- **Status**: **obligatoryjne** w kanionach z XIX-wiecznymi kamienicami na fundamentach ceglanych / palach dębowych / piasku (Dąbrowskiego). Pochłania energię wibroakustyczną zanim wniknie w mury.

### 5. Płyta pływająca FST (Floating Slab Track) — system masa-sprężyna

- **Mechanika**: najwyższy standard światowy. Żelbetowa płyta (kilkanaście m) z zakotwionymi szynami, zawieszona na rzędach sprężynowych izolatorów polimerowych (Pandrol, CDM). Częstotliwość rezonansowa układu **< 8 Hz**.
- **Redukcja wibracji**: **–15 do –25 dB**.
- **Koszt**: **15–30 tys. zł/mb** (skrajnie kosztowny, elitarny).
- **Żywotność płyty**: 40–60 lat; izolatory wymienne przez otwory inspekcyjne.
- **Wdrożenie**: wstrzymanie ruchu na miesiące, głębokie wykopy, przekładki teletechniczne.
- **Status**: filharmoniczny. Uzasadniony ekonomicznie przy bezpośrednim sąsiedztwie obiektów chronionych (szpital, sala koncertowa) lub fundamentów ceglanych na piasku.

### 6. System żywiczny ERS (szyna pływająca z otuliną poliuretanową, Edilon Sedra)

- **Mechanika**: rezygnacja z mechanicznych złączy (brak śrub, łubków, SKL). Profil szyny w szczelinie płyty betonowej, zalany elastyczną masą elastomerową. Powierzchnia zlicowana z jezdnią asfaltową.
- **Redukcja**: –5 do –9 dB (hałas powietrzny).
- **Koszt**: 8–12 tys. zł/mb (torowisko kompletne).
- **Żywotność masy**: 15–20 lat przed wulkanizacją zwrotną.
- **Ograniczenie**: trudniejsza interwencja przy pęknięciu szyny.
- **Status**: stosowane globalnie na skrzyżowaniach i estakadach. Rekomendowane w ścisłym śródmieściu — eliminuje najgłośniejsze uderzenia pionowe.

### 7. Tokarnia podtorowa (przetaczanie obręczy)

- **Mechanika**: obróbkowe przywracanie geometrii profilu koła w warsztacie podtorowym zajezdni. Usuwa wheel flats i zużycie wielokątne (polygonal wear).
- **Redukcja**: **–10 do –15 dB** $L_{Amax}$ (peak) dominujących o poranku.
- **Koszt**: operacyjny budżet utrzymania taboru (brak nakładu inwestycyjnego na drogi).
- **Żywotność**: krótkoterminowa, zależna od techniki motorniczych (prewencyjne hamowanie).
- **Dźwignia obywatelska**: identyfikacja po uchu „klekoczącego" składu → żądanie wycofania konkretnego numeru bocznego za emisję ~100 dB i łamanie homologacji.

## Rekomendacja dla Dąbrowskiego (zgodnie z symulacją CNOSSOS-EU — patrz `03-normy-limity.md`)

Dla osiągnięcia $L_{Aeq,N}$ = 48–52 dB przy fasadach 6–8 m od toru:
- **Wariant bazowy minimum**: ERS + USM + smarownice na łukach.
- **Wariant preferowany**: FST na odcinku największej koncentracji zabudowy (np. 300 m newralgicznych).
- **Nieakceptowalne**: torowisko bezpodsypkowe bez mat wibroizolacyjnych = ruletka prawna na 10 lat.

Czysty zabieg pojedynczy (samo szlifowanie, same tłumiki) nie rozwiązuje problemu kanionu ulicznego. Strategia pakietowa jest obligatoryjna.
