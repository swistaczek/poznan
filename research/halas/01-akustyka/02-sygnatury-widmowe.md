---
title: "Sygnatura częstotliwościowa i diagnostyka defektów infrastruktury"
type: reference
domain: halas
source: wyniki-01-akustyka-torowa.md
updated: 2026-04-17
entities: [MPK-Poznań, ZTP, ZDM]
acts: [PN-EN ISO 3095, PN-ISO 1996-2]
signatures: []
---

# Sygnatura widmowa defektów — spektrogram jako odcisk palca

Zarządca zdegradowanej infrastruktury najczęściej tłumaczy emisje „standardową eksploatacją" lub „niedoskonałościami taboru". Analiza częstotliwościowa w pasmach 1/3 oktawy lub wysokorozdzielcza FFT pozwala jednoznacznie przypisać hałas do konkretnych zaniedbań utrzymaniowych. **PN-EN ISO 3095** wymaga badania rozkładu widmowego; jednoczynnikowe wskaźniki szerokopasmowe A-ważone (jak $L_{Aeq}$) maskują fizyczną naturę i dokuczliwość tonalną.

Analiza 1/3 oktawy: logarytmiczny podział słyszalnego widma, odwzorowuje percepcję psychoakustyczną. Centralna częstotliwość × 0,89/1,12 = granice pasma 1/3.

## Katalog defektów i ich sygnatur

### Zużycie faliste główki szyny (corrugation)

- **Fizyka**: plastyczne odkształcenia powierzchni szyny w postaci fal o długości λ = 30–80 mm („tarka"). Koło doświadcza cyklicznych przyspieszeń pionowych → rezonans przekroju szyny/koła.
- **Sygnatura**: ekstremalna dominacja 250–1000 Hz, pik 500–800 Hz (częstotliwość zależna od prędkości).
- **Spektrogram**: ciągłe jasne poziome pasma o stałej częstotliwości. Przy hamowaniu pasma „schodzą" w dół osi Y (efekt Dopplera + spadek prędkości wzbudzenia).
- **Winny**: zarządca infrastruktury (torowisko).

### Płaskie miejsca na obręczach kół (wheel flats)

- **Fizyka**: awaryjne zablokowanie koła → poślizg topi stal → płaskie ścięcie długości kilku cm. Każdy obrót = uderzenie płaszczyzny w szynę.
- **Sygnatura**: szerokopasmowe impulsy 63 Hz – 4000 Hz, brak pasma rezonansowego.
- **Spektrogram**: pionowe „szpilki" amplitudy z matematyczną cyklicznością. Czas między uderzeniami = obwód koła / prędkość liniowa. Przy Ø 700 mm (obwód ~2,2 m) i 30 km/h — uderzenie co ~0,26 s. Potężne wzbudzenie parasejsmiczne gruntu.
- **Winny**: eksploatator taboru (brak tokarni podtorowej).

### Pisk na łukach (curve squeal)

- **Fizyka**: mechanizm stick-slip. Boczne pełzanie zestawów kołowych na ciasnych łukach (R < 50 m), naprężenia zrywane przy przekroczeniu tarcia statycznego.
- **Sygnatura**: najnowsze badania — dominacja 6,3–15,8 kHz (starsze analizy wskazywały 400–2000 Hz, błędne).
- **Spektrogram**: wąskopasmowe ostre tonalne linie poziome w górnych partiach (sustained tonal squeal). $L_{Amax}$ może przewyższać normalny hałas toczenia o 10–15 dB.
- **Winny**: zarządca (brak smarownic torowych) / eksploatator (geometria obręczy).

### Degradacja styków szynowych (hałas styków)

- **Fizyka**: przerwy dylatacyjne, wyrwy, wykruszenia przy spawach termitowych lub stykach łubkowych. Koło wpada w szczelinę, uderza w krawędź natarcia.
- **Sygnatura**: nagły wzrost 31,5–125 Hz + rezonans układu podkład-tłuczeń.
- **Spektrogram**: pojedyncze szersze pionowe ślady (szersze niż wheel flats) w stałych interwałach — długość przęsła szynowego (np. co 15 lub 18 m). Przedłużone niskoczęstotliwościowe „wybrzmienie" obrazuje tłumienie podtorza.
- **Winny**: zarządca infrastruktury.

### Hałas strukturalny / wibracje gruntu (ground-borne noise)

- **Fizyka**: drgania skrętne i pionowe szyny → niesprężyste zapadnięte podtorze → zlewiska wód gruntowych i struktury piaskowe → fundamenty kamienic XIX-wiecznych. Ściany re-emitują dźwięk wewnątrz pomieszczeń.
- **Sygnatura**: 16–80 Hz (infradźwięki + dolny skraj widma). W mieszkaniu odczuwalne jako drżenie podłóg, wibrowanie szyb, głębokie dudnienie (rumble).
- **Spektrogram**: na zewnątrz — ucięte wysokie częstotliwości (rozproszone na fasadach), potężna „chmura" energii widmowej na samym dnie osi Y.
- **Winny**: zarządca (zapadnięte podtorze, brak mat USM).

## Konsekwencja taktyczna

Żądania w pismach do organów nadzoru muszą być precyzyjne technicznie, nie rozmyte. Zamiast „prosimy o remont torowiska":

> Żądamy natychmiastowego wycofania z eksploatacji składu o numerze bocznym X i skierowania na tokarnię podtorową ze względu na występowanie rozległych płaskich miejsc na obręczach, generujących immisje uderzeniowe rzędu 100 dB $L_{Amax}$, co stanowi rażące naruszenie standardów utrzymania wózków tocznych.

Albo przy corrugation z zapisem spektrogramu:

> Spektrogram z kalibrowanego mikrofonu wykazuje ciągłą dominantę 630 Hz o charakterze tonalnym — sygnatura zużycia falistego wg PN-EN ISO 3095. Wnosimy o niezwłoczne wezwanie zespołu szlifierki torowej.
