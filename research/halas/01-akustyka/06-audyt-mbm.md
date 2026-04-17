---
title: "Egzekucja audytu diagnostycznego torowiska (MBM) — parametry i żądania"
type: reference
domain: halas
source: wyniki-01-akustyka-torowa.md
updated: 2026-04-17
entities: [MPK-Poznań, ZDM, ZTP, UTK, PKP-PLK, Plasser-Theurer]
acts: [Id-1, Id-115, SMS]
signatures: []
---

# Audyt MBM — Measurement Based Maintenance

Zarządcy odpowiadają najczęściej mantrą: „torowisko jest w stanie zadowalającym, spełnia dopuszczalne normy, jest systematycznie badane, nakłady inwestycyjne są nieuzasadnione". Taka odpowiedź minimalizuje ryzyko natychmiastowego nakazu UTK, ale strona społeczna nie musi się jej poddawać.

Przepisy nadzorcze Urzędu Transportu Kolejowego (instrukcje **Id-1**, **Id-115**) formalnie dotyczą PKP PLK S.A., ale orzecznictwo i zalecenia wewnętrzne miejskich sieci tramwajowych kopiują ten reżim przez analogię. Metodyka **MBM** (Measurement Based Maintenance — utrzymanie predykcyjne oparte o pomiary geometryczne) zakłada cykliczne automatyczne mierzenie wad torowych oprzyrządowanymi wagonami diagnostycznymi.

## Parametry krytyczne — pełne raporty do żądania

### 1. Profil geometryczny toru w ciągłości

Wymagane dane:
- Profile wichrowatości (skręcenie przestrzenne toru).
- Odchyłki szerokości toru w milimetrach.
- Przechyłki.

Narzędzia: drezyny Plasser & Theurer adaptowane do torowisk tramwajowych, moduły EM-120 z akcelerometrami i laserami.

Klasyfikacja odchyłek:
- Klasa 1: tolerowane.
- **Klasa 2**: wymaga interwencji planowej.
- **Klasa 3**: bezpośrednie ryzyko bezpieczeństwa dynamicznego + wzrost gęstości rezonansowej hałasu impulsowego.

Obecność odchyłek klasy 2 lub (zwłaszcza) 3 **dyskwalifikuje** ocenę „stan bardzo dobry".

**Wskaźnik Syntetyczny Stanu Toru (J)** — matematyczna ocena gładkości i stabilności mechanicznej. Wysokie J koreluje z kolosalną energią immisji akustycznych.

### 2. Defektoskopia profilometryczna corrugation

Narzędzia: **CAT** (Corrugation Analysis Trolley), mierniki **m-p-a** (m-prof). Rozdzielczość mikrometryczna dla przedziałów długości fali:
- 10–30 mm (falistość krótka).
- 30–100 mm (akustycznie krytyczna).
- 100–300 mm.

Próg alarmowy: **pofalowanie > 0,05 mm** w paśmie akustycznym → proceduralnie bezzwłoczne wezwanie szlifierki.

Brak wydruku CAT / m-p-a w odpowiedzi zarządcy = kompromitacja przed sądem powszechnym (techniczne zaniechanie obowiązków kontrolnych, dowód zawinienia).

### 3. Defektoskopia ultradźwiękowa (UT)

Wózki z głowicami wysyłającymi fale ultradźwiękowe wysokiej częstotliwości. Identyfikacja:
- Wzdłużne i poprzeczne wady produkcyjne.
- Pęknięcia zmęczeniowe.
- Wyszczerbienia podpowierzchniowe (prekursor „dziury z wybuchem").

Te ukryte defekty indukują ekstremalny hałas o bardzo niskich częstotliwościach (rumble, ekwiwalent wheel-flats impact).

### 4. Georadar podtorza (GPR — Ground Penetrating Radar)

Kanion ulic historycznych + grunty piaszczyste + fundamenty ceglane = drgania wnikają wprost w struktury budynków. GPR skanuje pustki i wymycia pod torem bezinwazyjnie (bez rozkopu).

Jeśli zarządca przyzna, że GPR nie był robiony od 30 lat → podstawa do **zawiadomienia prokuratury** o zaniedbanie zagrażające katastrofą struktury fundamentowej budynków narażonych na rezonans.

## Formuła żądania — zamiast „wszystko OK"

Gdy MPK oświadcza pisemnie „torowisko oceniamy jako OK", odpowiedź strony społecznej:

> Jako strona postępowania stanowczo żądamy wykazania tego twierdzenia:
> (a) matematycznymi odpisami metrykalnymi z zapisów drezyny pomiarowej — laserowe wydruki osi X, Y, Z toru w dziesiątych częściach milimetra na każdym przęśle;
> (b) raportem diagnostyki defektoskopii szynowej, przeprowadzonej zgodnie ze standardami pomiarowymi (Id-1 / Id-115 przez analogię);
> (c) protokołem CAT / m-p-a z rozbiciem amplitud i długości fal dla pasm 30–100 mm;
> (d) wskaźnikiem J z ostatniego pełnego przejazdu drezyny diagnostyczno-geometralnej.

Brak takich dokumentów demaskuje stanowisko MPK jako oparte na wizualnych obserwacjach „na przysłowiowe oko" montera obchodowego — bez rzetelnych podstaw technicznych. Sąd administracyjny uznaje taki brak na korzyść mieszkańców.

## Cross-reference

- Katalog konkretnych 12 pytań UDIP operacjonalizujących ten rozdział → `07-udip-zapytania.md`.
- Sygnatury widmowe, które te pomiary mają wyjaśnić → `02-sygnatury-widmowe.md`.
