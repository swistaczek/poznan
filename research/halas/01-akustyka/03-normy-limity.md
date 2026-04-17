---
title: "Normy prawne, limity hałasu i osiągalność techniczna"
type: reference
domain: halas
source: wyniki-01-akustyka-torowa.md
updated: 2026-04-17
entities: [WHO, KE, Rada-Miasta-Poznania, Minister-Klimatu]
acts: [POŚ, Dz.U.2024.54, Dz.U.2024.271, Dz.U.2024.255, Dyrektywa-2002/49/WE, WHO-ENG-2018]
signatures: []
---

# Normy prawne vs rzeczywistość zdrowotna

Kontekst prawny: ustawa **Prawo ochrony środowiska** (t.j. Dz. U. z 2024 r. poz. 54) + rozporządzenie Ministra Klimatu i Środowiska ws. dopuszczalnych poziomów hałasu (Dz. U. z 2024 r. poz. 271, poz. 255). Z inżynieryjnego punktu widzenia kluczowe jest rozróżnienie między „zgodnością z przepisami krajowymi" a technicznym „występowaniem uciążliwości zdrowotnej".

## Dyskrepancja Polska vs WHO

Wskaźniki z dyrektywy 2002/49/WE: $L_{DWN}$ (dzienno-wieczorno-nocny, mapy strategiczne), $L_{Aeq,D}$ i $L_{Aeq,N}$ (ocena punktowa, audyty).

Limity krajowe dla „terenów zabudowy mieszkaniowej wielorodzinnej i zamieszkania zbiorowego" od linii tramwajowych/kolejowych (stan prawny do 2026 r.):

| Pora | Tereny zwykłe | Strefa śródmiejska (miasta > 100 tys.) |
|---|---|---|
| Dzień (6:00–22:00) | $L_{Aeq,D}$ = 65 dB | 68 dB |
| Noc (22:00–6:00) | $L_{Aeq,N}$ = 55 dB | 59 dB |

Wytyczne **WHO Environmental Noise Guidelines for the European Region (2018)** — progi trwałej degradacji zdrowia (nadciśnienie, zaburzenia kognitywne, deprywacja snu):

| Wskaźnik | WHO — rail |
|---|---|
| $L_{den}$ całodobowy | **54 dB** |
| $L_{night}$ | **44 dB** |

## Skala rozbieżności

Różnica pory nocnej: 59 dB (PL, strefa śródmiejska) vs 44 dB (WHO) = **15 dB**. Skala decybelowa jest logarytmiczna:
- +10 dB = 10-krotny wzrost energii fali.
- +15 dB = ponad **30-krotny** wzrost energii.

Polskie prawo de facto sankcjonuje strefy, w których fizyczna energia akustyczna uderzająca w elewację jest 31× większa niż ta, która pozwala na fizjologiczny niezakłócony odpoczynek. Zarządca cytujący „58 dB w nocy jest zgodne z normą" używa wybiegu prawniczego — stan jest patologiczny z punktu widzenia fizyki budowli i ochrony zdrowia.

## Klasyfikacja Dąbrowskiego — kluczowa zmienna

Decyduje uchwała Rady Miasta o klasyfikacji terenu (Studium + MPZP). Dla Poznania (~540 tys. mieszkańców) możliwe są dwa scenariusze:

- Tereny „zwykłej" zabudowy wielorodzinnej: noc 55 dB.
- Strefa śródmiejska: noc 59 dB.

**Pierwsza kwerenda UDIP**: konkretna klasyfikacja ul. Dąbrowskiego w obowiązującym MPZP oraz w strategicznej mapie hałasu Poznania (aktualizacja cykliczna 5 lat wg dyrektywy 2002/49/WE — czwarta edycja: **2022**; następna: 2027). <!-- poznan.pl/mim/main/-,p,11105,65515.html, dostęp 2026-04-17 -->

Konsekwencja: jeśli limit nocny 59 dB, a pomiar 64–69 dB (wariant zdegradowany — patrz osiągalność techniczna poniżej), MPK ma 5–10 dB przekroczenia (rażące). Przy limicie 55 dB przekroczenie drastyczniejsze.

## Osiągalność techniczna — symulacja CNOSSOS-EU dla Dąbrowskiego

Założenia: zwarta zabudowa pierzejowa, fasady ~15 m wysokie, dystans fronty–oś skrajnego toru 6 m. Tramwaj, prędkość eksploatacyjna 30–40 km/h.

| Wariant torowiska | $L_{Amax}$ pojedynczy przejazd na fasadzie I piętra | $L_{Aeq,N}$ (ekwiwalentne dla nocy) | Status prawny |
|---|---|---|---|
| Skrajnie zdegradowany (stan Dąbrowskiego: corrugation, luki na stykach, zapadnięta podbudowa) | **85–95 dB** | **64–69 dB** | Drastyczne przekroczenie (64 > 59 dB) — absolutna podstawa pozwu |
| Dostateczny (po szlifowaniu, klasyczna podsypka, spawy doraźne) | — | 56–58 dB | „Spełnia" 59 dB — nadal łamie WHO, silne wibracje i dyskomfort nocny |
| Bardzo dobry / Premium Śródmiejski (bezpodsypkowe + maty USM + otuliny poliuretanowe toku szynowego) | 70–73 dB | **48–52 dB** | Blisko WHO, wibracje zredukowane niemal do zera, rozwiązanie na dekady |

## Wniosek inżynieryjny

Redukcja **15 dB** z poziomu fatalnego do optymalnego jest w zasięgu współczesnej wiedzy technicznej. Wymaga porzucenia paradygmatu „patch and mend" (łatanie doraźne) przez MPK Poznań i przejścia na głęboką przebudowę strukturalną profilu podłużnego — maty USM + ERS/FST (katalog interwencji → chunk `04-interwencje-techniczne.md`).

## Dźwignia sądowa WHO

Niezależnie od limitu krajowego, przed sądem cywilnym (art. 144 K.c.) coraz częściej uznaje się WHO ENG 2018 ($L_{night}$ = 44 dB dla rail) jako „standard ostrożności" — argument uzupełniający przy roszczeniu o zaniechanie immisji.
