---
title: "Spory kompetencyjne, formy kontaktu, anti-patterns"
type: reference
domain: instytucje
source: wyniki-07-kompetencje-instytucji.md
updated: 2026-04-17
entities:
  - SKO-Poznan
  - NSA
  - WSA-Poznan
  - RPO
  - Biuro-Nadzoru-Wlascicielskiego-UMP
  - PIM-Poznan
  - MPK-Poznan
  - ZDM-Poznan
  - UTK
  - GDDKiA-Oddzial-Poznan
  - UODO
acts:
  - KPA-art-22
  - KPA-art-65
  - KPA-art-37
  - KPA-art-35
  - KPA-art-237
  - PPSA-art-3
  - PPSA-art-4
  - PPSA-art-53
  - PPSA-art-149
  - UDIP-art-13
  - ustawa-o-doreczeniach-elektronicznych
signatures: []
---

# Spory kompetencyjne, formy kontaktu, anti-patterns

## Spór o właściwość — art. 22 i 65 KPA

### Tryb standardowy — art. 65 § 1 KPA

„Jeżeli organ administracji publicznej, do którego podanie wniesiono, jest niewłaściwy w sprawie, niezwłocznie przekazuje je do organu właściwego, zawiadamiając jednocześnie o tym wnoszącego podanie".

Wada: przesuwa bieg terminów ustawowych o 30–60 dni („ping-pong urzędniczy").

### Negatywny spór kompetencyjny — art. 22 KPA

Gdy jeden organ stwierdza niewłaściwość, a drugi robi to samo — konflikt negatywny.

| Typ sporu | Organ rozstrzygający | Podstawa |
|---|---|---|
| Między organami tej samej jst (np. Prezydent vs wydziały) | **SKO Poznań** | art. 22 § 1 pkt 1 KPA |
| Między organem gminy/powiatu a administracją rządową (Marszałek/Wojewoda) | **Naczelny Sąd Administracyjny** | art. 4 PPSA |

### Scenariusz obywatela w sporze

1. **Żądać postanowień** (pisemnie) o niewłaściwości od każdego z organów. Art. 65 § 1 KPA nakazuje wskazać organ właściwy — ustna/e-mailowa odmowa nie wystarczy.
2. Gdy dwa sprzeczne postanowienia → spór kompetencyjny.
3. Wniosek do SKO (al. Niepodległości 16/18) lub NSA (Warszawa) — **sporządza sam obywatel**, nie czeka się na organy.
4. **Strategia awaryjna**: ponaglenie art. 37 KPA + skarga na bezczynność do WSA Poznań (ul. Ratajczaka 10/12). W międzyczasie **DW do RPO i SKO** na każdym piśmie.

**Zasada**: nigdy nie akceptować „proszę zwrócić się do innego urzędu" — żądać formalnego postanowienia na piśmie.

## Strategie wymuszania procedury

### 1. Nadzór właścicielski (dla spółek komunalnych)

Gdy spółka (MPK, Aquanet, PIM, ZKZL) argumentuje „brak merytorycznej kontroli" — pismo interwencyjne do **Biura Nadzoru Właścicielskiego UMP**.

Powołanie na nadzór właścicielski w 90% wymusza uzyskanie stanowiska prezesa spółki na polecenie służbowe Prezydenta.

### 2. Adnotacja DW (do wiadomości)

Skarga z adnotacją:
- `DW: Biuro Rzecznika Praw Obywatelskich w Warszawie`
- `DW: Samorządowe Kolegium Odwoławcze w Poznaniu`

Uruchamia mechanizm transparentności — podmioty priorytetyzują pisma z perspektywą postępowania skargowego i NIK.

### 3. Ponaglenie art. 37 KPA

Podstawowe terminy:

| Postępowanie | Termin | Podstawa |
|---|---|---|
| Wniosek UDIP | 14 dni (przedłużenie do 2 m-cy z uzasadnieniem) | art. 13 ust. 1 UDIP |
| Postępowanie administracyjne standardowe | 1 miesiąc | art. 35 § 3 KPA |
| Postępowanie administracyjne skomplikowane | 2 miesiące | art. 35 § 3 KPA |
| Skarga Dział VIII KPA | 1 miesiąc | art. 237 § 1 KPA |

### Narzędzia egzekwowania:

- **Krok A — ponaglenie (art. 37 KPA)**: do organu wyższego stopnia (SKO dla Prezydenta, WINB dla PINB, GIOŚ dla WIOŚ) **za pośrednictwem** organu prowadzącego. Organ wyższy — 7 dni na rozpatrzenie; może stwierdzić przewlekłość i wyznaczyć nowy termin.
- **Krok B — skarga na bezczynność/przewlekłość do WSA** (art. 3 § 2 pkt 8 PPSA; art. 53 § 2b PPSA — po uprzednim ponagleniu). Termin nieograniczony (dopóki bezczynność trwa). WSA może nałożyć grzywnę (art. 149 § 2 PPSA) oraz zasądzić 500–10 000 zł na rzecz skarżącego.
- **Krok C — dochodzenie szkody** z art. 417¹ § 3 KC za szkody wyrządzone niewydaniem decyzji w terminie.
- **Krok D — DW RPO i SKO** na każdym piśmie procesowym.

**Pułapka**: ponaglenie musi być wniesione **w trakcie bezczynności** — nie po wydaniu decyzji.

## Formy kontaktu — aspekty doręczeniowe

Prawidłowe doręczenie generuje skutki prawne, od których biegną terminy ustawowe.

### 1. ePUAP (Elektroniczna Skrzynka Podawcza — ESP) / e-Doręczenia

**Rekomendacja: używać bezwzględnie.**

- Generuje automatycznie Urzędowe Poświadczenie Przedłożenia (UPP) i Urzędowe Poświadczenie Odbioru (UPO) — moc dowodowa listu poleconego za zwrotnym potwierdzeniem.
- Obowiązek posiadania skrytek: urzędy administracji rządowej i samorządowej, ZDM, ZTM (skrytka `AE:PL-88237-25958-BSCDW-19`), ZZM.
- Format znosi fizyczne limity objętości skrzynki mailowej dla dowodów elektronicznych (PDF, DOCX, ZIP dla dźwięków/filmów na skargi hałasowe).
- Podpis: Profil Zaufany, mObywatel, Certyfikat Kwalifikowany.
- Typ dokumentu: „Pismo ogólne do podmiotu publicznego".

### 2. Poczta polecona

Skuteczna, ale proces skanowania u adresata opóźnia nadanie numeru sprawy w EZD (Elektroniczne Zarządzanie Dokumentacją).

### 3. Zwykły e-mail (np. `urzad@um.poznan.pl`)

Dopuszczalny dla:
- skarg i wniosków Działu VIII KPA,
- wniosków UDIP.

**Niewystarczający** dla trybów odwoławczych / wszczęcia postępowania o decyzję ostateczną (np. art. 115a POŚ) — organ może powołać się na niepodpisanie dokumentu i wezwać do usunięcia braków formalnych w terminie 7 dni. Zignorowanie = pozostawienie bez rozpoznania.

### 4. Formularze BIP / e-urząd

Niektóre organy (WZDW, WIOŚ, UMWW) preferują strukturalne formularze w systemie e-urząd — sprawdź BIP przed złożeniem.

## Anti-patterns — najdroższe błędy adresacyjne

Uniknięcie przekazania wg właściwości oszczędza średnio 30–60 dni.

### 1. Traktowanie spółek (PIM, MPK, Aquanet, ZKZL) jak komórek Urzędu Miasta

Wniosek UDIP do Prezydenta z żądaniem ekspertyz technicznych będących w zasobach MPK sp. z o.o. → Urząd przekaże lub odpowie „brak posiadania wnioskowanej informacji" po 14 dniach.

**Zasada**: adresować **do Prezesa Zarządu właściwej spółki**.

### 2. Traktowanie miast na prawach powiatu jako podmiotów „obcych" na tle GDDKiA

Skargi na dziury w ul. Krzywoustego (DK11) do GDDKiA Oddział Poznań → odrzucenie; podanie trafi do ZDM (art. 19 ust. 5 UoDP). Dotyczy wszystkich dróg krajowych / wojewódzkich w granicach miasta (z wyjątkiem A2, S11).

### 3. Błąd adresacji szynowej na tle UTK

Ignorowanie wyłączenia tramwajów z ustawy o transporcie kolejowym (art. 3 ust. 1 pkt 1). Skargi na torowisko w jezdni do UTK → wniosek jest umarzany.

**Zamiast UTK**: PINB (stan techniczny), WIOŚ (hałas/wibracje), MPK/ZTM (eksploatacja).

### 4. Skarga RODO anonimowa do UODO

UODO odrzuca bezlitośnie skargi bez własnoręcznego adresu i imienia. **Pełna identyfikacja wnioskodawcy obligatoryjna.**

### 5. Odwołanie od pozwolenia na budowę do SKO

Prezydent jako Starosta w sprawach budowlanych → II instancja to **Wojewoda** (art. 82 ust. 2 Prawa budowlanego), **nie SKO**.

### 6. Odwołanie od decyzji MKZ (porozumienie) do Wojewody lub Prezydenta

Porozumienie Wojewoda–Prezydent m. Poznania 2016 r. przekazuje sprawy konserwatorskie miastu, ale organem wyższego stopnia KPA pozostaje **Generalny Konserwator Zabytków / Minister Kultury** — nie Wojewoda, nie Prezydent.

### 7. Skarga na Prezydenta do Wojewody jako „skarga na decyzję"

Wojewoda bada **legalność uchwał** (art. 85 USG) — nie indywidualnych decyzji. Decyzja indywidualna → SKO → WSA. Skarga na Prezydenta jako kierownika urzędu (Dział VIII KPA) → **Rada Miasta Poznania** (art. 229 pkt 3 KPA).

## Powiązania

- Szablony realizujące scenariusze tego chunku:
  - `szablony/instytucje/pismo-o-wlasciwosc.md` — żądanie postanowienia art. 65 § 1 KPA.
  - `szablony/instytucje/ponaglenie-kpa-art-37.md` — uniwersalne ponaglenie.
  - `szablony/instytucje/wniosek-spor-kompetencyjny.md` — art. 22 KPA → SKO / NSA.
- Drzewo decyzji (wybór organu) → `05-drzewo-decyzji.md`.
- Mapa instytucji UMP i spółek → `02-jednostki-miasta-i-spolki.md`.
