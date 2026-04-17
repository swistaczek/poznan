---
title: "Projekt do Poznańskiego Budżetu Obywatelskiego — infrastruktura rowerowa"
type: template
domain: rowery
adresat_typ: [UMP, ZDM-Poznań]
podstawa_prawna:
  - Uchwała-Rady-Miasta-Poznania-w-sprawie-PBO
  - Zasady-PBO-Poznań-aktualna-edycja
updated: 2026-04-17
---

# Formularz projektu do Poznańskiego Budżetu Obywatelskiego

> Szablon wniosku (część merytoryczna — nagłówek i uzasadnienie) dla projektów rowerowych: modernizacja nawierzchni, separatory, stojaki, wiaty, pasy rowerowe, obniżenie krawężników. Kompletny formularz PBO zawiera dodatkowo pola administracyjne (wnioskodawca, poparcia, kosztorys szczegółowy, mapa), które należy uzupełnić w systemie PBO Poznania.

## Dane projektu

- **Tytuł projektu:** {{TYTUL_PROJEKTU}}
- **Typ projektu:** ogólnomiejski / rejonowy (rejon nr {{NR_REJONU}})
- **Wnioskodawca (lider):** {{IMIE_NAZWISKO}}, {{ADRES}}
- **Współwnioskodawcy (koalicja min. 3 podmioty — rekomendowane):**
  - {{RADA_OSIEDLA}}
  - {{NGO}}
  - {{INICJATYWA_MIESZKANCOW}}
- **Szacowany koszt całkowity:** {{KWOTA}} zł
- **Lokalizacja (ulica/odcinek/skrzyżowanie):** {{LOKALIZACJA}}
- **Działka / działki (nr ewidencyjny):** {{DZIALKA}}
- **Zarządca terenu:** {{ZARZADCA}} (np. ZDM Poznań; w przypadku PKP PLK, GDDKiA, Skarbu Państwa, prywatnych — załączyć list intencyjny)

## Opis projektu

### 1. Przedmiot projektu

{{OPIS_PRZEDMIOTU}}

Zakres rzeczowy:
- {{ZAKRES_1}} (np. wymiana nawierzchni kostki na bitumiczną, długość … m)
- {{ZAKRES_2}} (np. montaż 20 stojaków U-kształtnych w betonowym cokole)
- {{ZAKRES_3}} (np. obniżenie 15 krawężników na skrzyżowaniach)

### 2. Kosztorys orientacyjny

| Pozycja | Jednostka | Ilość | Stawka | Wartość |
|---|---|---|---|---|
| {{POZYCJA_1}} | {{JEDNOSTKA_1}} | {{ILOSC_1}} | {{STAWKA_1}} | {{WARTOSC_1}} |
| {{POZYCJA_2}} | {{JEDNOSTKA_2}} | {{ILOSC_2}} | {{STAWKA_2}} | {{WARTOSC_2}} |
| **Suma** | | | | **{{KWOTA}} zł** |

Stawki kontrolne dla Poznania 2026 (orientacja przy weryfikacji — szczegóły w `research/rowery/05-polityka/04-priorytety-inwestycyjne.md`):
- 1 km kontrapasu (znaki + malowanie): 80–120 tys. zł
- 1 km pasa buforowego z separatorami: 300–600 tys. zł
- Obniżenie 1 krawężnika: 2–4 tys. zł
- Stojak U-kształtny w cokole: 400–800 zł
- Wiata zadaszona na 10 stanowisk: 15–30 tys. zł
- Przeprogramowanie sygnalizacji 1 węzła: 20–80 tys. zł

### 3. Uzasadnienie

#### (a) Zgodność z polityką miasta

Projekt realizuje cele:
- **Planu ogólnego miasta Poznania** (Uchwała Nr XXIX/529/IX/2025) — priorytet dla ruchu rowerowego i dostępności.
- **Planu Zrównoważonej Mobilności Miejskiej (SUMP) Metropolii Poznań** — zwiększenie udziału roweru w dojazdach na dystansach do 10 km.
- **Standardów projektowych i wykonawczych dla systemu rowerowego** (ministerialne, 2016).

#### (b) Odpowiedź na zdiagnozowaną lukę CROW

{{OPIS_LUKI_CROW}}

Kryterium CROW, które projekt podnosi:
- [ ] Spójność (cohesion) — likwidacja "teleportacji" rowerzysty, domknięcie missing link.
- [ ] Bezpośredniość (directness) — skrócenie czasu przejazdu, eliminacja oczekiwania na cykle świateł.
- [ ] Bezpieczeństwo (safety) — eliminacja "dooring zone" / separatorów fizycznych / Protected Intersection.
- [ ] Komfort (comfort) — wymiana nawierzchni, obniżenie krawężników.
- [ ] Atrakcyjność (attractiveness) — integracja z korytarzem błękitno-zielonym.

#### (c) Liczba beneficjentów

Szacowana dzienna liczba użytkowników: {{BENEFICJENCI}} osób.
Dane źródłowe: {{ZRODLO_DANYCH}} (np. liczniki Eco-Counter — punkt {{ID_PUNKTU}}, średnia z 2024 r.).

#### (d) Efekt systemowy

{{EFEKT_SYSTEMOWY}} (np. "Projekt domyka dystrybucyjny ring śródmiejski, zwiększając wskaźnik spójności CROW o 1,5–2 pkt — patrz rozdział 02-gap-analysis-crow.md").

#### (e) Koalicja poparcia

- Radni: {{RADNI}}
- Organizacje: {{ORGANIZACJE}} (rekomendowane: Rowerowy Poznań — Sekcja Rowerzystów Miejskich)
- Rada Osiedla: {{RADA_OSIEDLA}}
- Liczba zebranych poparć (weryfikacja formalna): {{LICZBA_POPARC}}

### 4. Harmonogram

| Etap | Termin |
|---|---|
| Ogłoszenie przetargu | {{Q1_YYYY}} |
| Wybór wykonawcy | {{Q2_YYYY}} |
| Realizacja | {{Q3_YYYY}} – {{Q4_YYYY}} |
| Odbiór | {{Q4_YYYY}} |

### 5. Załączniki

- [ ] Mapa z zaznaczonym zakresem (skala 1:500 lub 1:1000).
- [ ] Dokumentacja fotograficzna stanu istniejącego.
- [ ] Pisemne potwierdzenie z Wydziału ds. Rowerowych ZDM o braku kolizji ze Studium, Planem ogólnym i trwającymi przetargami.
- [ ] List intencyjny od zarządcy terenu (jeśli nie ZDM).
- [ ] Opinia inżynieryjna / audyt BRD (dla interwencji w organizację ruchu).

---

**Data sporządzenia:** {{DATA}}
**Podpis wnioskodawcy:** {{PODPIS}}
