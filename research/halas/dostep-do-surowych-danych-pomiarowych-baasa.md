---
title: "Dostęp do surowych danych pomiarowych BAASA — status researchu"
type: research
domain: halas
updated: 2026-09-17
---

# Czy można żądać surowych nagrań/danych źródłowych z pomiarów hałasu BAASA

Pytanie wyjściowe: po otrzymaniu 5 sprawozdań BAASA (16.09.2026, zob. `pomiary-baasa-2026-05-wyniki.md`) — czy warto i można skutecznie zażądać od ZDM i/lub BAASA Acoustics surowych danych pomiarowych (plik z miernika SVAN 971/971A, ewentualnie nagranie audio), na podstawie których powstały uśrednione wyniki LAeq, żeby wyodrębnić z nich pojedyncze zdarzenia impulsywne (LAmax/SEL dla trzasków/uderzeń).

**Status researchu: w większości NIEROZSTRZYGNIĘTY.** Z sześciu postawionych pytań badawczych tylko jedno (nr 3, retencja danych wg akredytacji PCA) doczekało się ustaleń, które przetrwały weryfikację adwersaryjną — z wynikiem częściowo negatywnym. Pozostałe pięć pytań (status prawny danych źródłowych wg UDIP, zakres podmiotowy UDIP wobec prywatnego wykonawcy, czy SVAN w ogóle nagrywa audio, RODO, praktyczna wartość danych) pozostaje otwarte — nie z powodu ustalenia "nie da się", tylko z powodu braku zweryfikowanego materiału źródłowego w tej turze (budżet WebSearch wyczerpany w trakcie sesji). **Nie budować na tym pliku żadnego twierdzenia poza tym, co niżej oznaczone jako potwierdzone.**

## Ustalone (weryfikacja adwersaryjna 3-0)

1. **Dokumenty programu akredytacji PCA "DAB-07"** (regulujące akredytację laboratoriów badawczych wg PN-EN ISO/IEC 17025, edycje sprawdzone: nr 4 z 17.01.2024 i nr 14 z 29.12.2023) **nie zawierają żadnego określonego okresu przechowywania zapisów źródłowych/danych surowych/nagrań pomiarowych**. Sama akredytacja ISO 17025 przez PCA NIE daje więc samodzielnej podstawy do twierdzenia, że BAASA ma ustawowy/regulaminowy obowiązek przechowywania danych surowych przez konkretny czas. Źródła: [DAB-07 ed.14](https://www.pca.gov.pl/storage/file/core_files/2024/7/9/55bf3a80b3c968e278ed9ad020cd65f1/dab-07_14.pdf), [DAB-07 Lista wymagań ed.4](https://www.pca.gov.pl/storage/file/core_files/2024/7/9/ce10c98399c793815f9d7efebab473bb/dab-07_4_lista_wymagan.pdf), [dokumenty PCA dla laboratoriów badawczych](https://www.pca.gov.pl/o-pca/dokumenty/pca/dokumenty-lb).

2. **Pomiary hałasu drogowego/tramwajowego/kolejowego w Polsce muszą być wykonywane przez laboratorium akredytowane wg PN-EN ISO/IEC 17025 na podstawie rozporządzenia Ministra Środowiska z 16.06.2011 r.** — to dokładnie reżim, w którym BAASA Acoustics (akredytacja PCA AB 1820) wykonała zlecenie ZDM-RO.401.544.2026. Potwierdza to formalną poprawność wyboru wykonawcy, ale nie rozstrzyga kwestii dostępu do danych. Źródło: [DAB-07 Lista wymagań ed.4, str. 6/10](https://www.pca.gov.pl/storage/file/core_files/2024/7/9/ce10c98399c793815f9d7efebab473bb/dab-07_4_lista_wymagan.pdf).

## Nierozstrzygnięte — wymaga odrębnego researchu przed napisaniem wniosku

1. **Czy surowe dane pomiarowe (log poziomu dB w czasie, ewentualne nagranie audio) stanowią "informację publiczną" w rozumieniu UDIP** oraz czy istnieje orzecznictwo NSA/WSA o dostępie do "danych źródłowych" leżących u podstaw opracowań zlecanych przez organy administracji (analogie: dane meteo, monitoring środowiska). Nie znaleziono zweryfikowanego materiału.
2. **Czy BAASA jako prywatny wykonawca podlega UDIP** na podstawie art. 4 ust. 1 pkt 5 UDIP (podmioty wykonujące zadania publiczne), czy wniosek powinien iść tylko do ZDM (które powinno mieć dostęp do danych na mocy umowy z wykonawcą) — nierozstrzygnięte.
3. **Czy miernik SVAN 971/971A w ogóle rejestruje audio (nagranie dźwięku), czy wyłącznie poziom SPL w czasie (bez możliwości odtworzenia treści dźwiękowej)** — to kluczowe rozróżnienie dla ewentualnego zarzutu RODO/nagrywania osób w tle. Nie potwierdzone w tej turze; do sprawdzenia bezpośrednio w specyfikacji technicznej producenta (Svantek) i w umowie/SIWZ zlecenia ZDM.
4. **Czy z surowego logu poziomu dB (bez dostępu do audio) da się w ogóle wyodrębnić LAmax i SEL dla pojedynczych zdarzeń impulsywnych** przy rozdzielczości czasowej rzędu 1s (parametr "Stała czasu próbkowania [s]: 1" widoczny w protokołach BAASA) — to determinuje praktyczną wartość takiego wniosku. Nierozstrzygnięte.
5. **Rekomendacja końcowa (do kogo, na jakiej podstawie, jakie ryzyko odmowy)** — nie sformułowana, bo zależy od punktów 1-4 wyżej.

## Wniosek operacyjny

Na obecnym etapie NIE ma wystarczającego materiału, żeby napisać skuteczny, dobrze uzasadniony wniosek o surowe dane — ryzyko, że trafi bez podstawy prawnej i zostanie łatwo odrzucony. Przed sformułowaniem wniosku potrzebne jest osobne sprawdzenie (poza tym researchem, ręcznie lub w kolejnej turze z odnowionym budżetem WebSearch):
- specyfikacji technicznej SVAN 971/971A (czy zapisuje audio),
- orzecznictwa NSA/WSA w bazie CBOSA pod kątem "dane źródłowe" + UDIP,
- czy umowa ZDM-BAASA (zlecenie ZDM-RO.401.544.2026) przewiduje przekazanie danych surowych zamawiającemu — to najprostsza droga: żądać od ZDM danych, które ZDM powinien mieć od wykonawcy na mocy umowy, zamiast kierować wniosek bezpośrednio do BAASA.

Do czasu tego uzupełnienia nie wysyłać wniosku o surowe dane — priorytet ma pytanie już zadane ZDM (17.09.2026) o powód niewypełnienia klasyfikacji terenu dla punktu PPH3.58 oraz o działania naprawcze wobec stwierdzonych przekroczeń (PPH3.05, PPH4.16).
