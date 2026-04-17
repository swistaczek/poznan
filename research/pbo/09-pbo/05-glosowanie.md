---
title: "Głosowanie w PBO — mechanika, progi, antyfraud"
type: reference
domain: pbo
source: wyniki-09-pbo.md
updated: 2026-04-17
entities: [UMP, PCSS, Centrum-Inicjatyw-Rodzinnych, Centrum-Inicjatyw-Senioralnych]
acts: [uchwala-RMP-XVII-318-IX-2025]
edycje: [2024, 2025, 2026]
---

# Głosowanie — mechanika i obrona antyfraud

## Uprawnieni do głosowania

- **Każdy mieszkaniec Poznania**, bez wymogu formalnego zameldowania.
- **Dzieci** — dopuszczone; wymagane oświadczenie woli opiekuna prawnego.
- Model inkluzywny — brak dolnej granicy wieku.

## Autoryzacja głosu

Procedura elektroniczna (dominująca):

1. Serwer PBO (responsywny serwis, utrzymanie: **PCSS**).
2. Weryfikacja: **ostatnie 4 cyfry PESEL** + konfrontacja z systemem ewidencyjnym/bankowym.
3. Autoryzacja finalna: **kod OTP** (SMS na zweryfikowany numer telefonu).

Kanał stacjonarny (dla wykluczonych cyfrowo):

- **UMP, Plac Kolegiacki 17**.
- **Centrum Inicjatyw Rodzinnych**.
- **Centrum Inicjatyw Senioralnych**.
- Wsparcie techniczne na miejscu.

## Koszyk głosów (5 głosów / mieszkańca)

Architektura asymetryczna:

**Koszyk ogólnomiejski (max 3 głosy):**
- maks. 1 głos na projekt **ogólnomiejski duży**,
- maks. 1 głos na projekt **ogólnomiejski mały**,
- maks. 1 głos na projekt **ogólnomiejski duży — Zielony Budżet**.

**Koszyk rejonowy (max 2 głosy):**
- maks. 1 głos na projekt **rejonowy mały**,
- maks. 1 głos na projekt **rejonowy duży**,
- **wyłącznie w jednym wybranym rejonie** terytorialnym.

## Algorytm rozstrzygania

Rygorystyczna malejąca użyteczność finansowa:

1. System generuje ranking poparcia w każdej kategorii.
2. Sumuje koszty kolejnych pozycji aż do wyczerpania puli.
3. **Funkcja omijania**: jeśli kolejny projekt w rankingu przekracza pozostałe saldo, algorytm go pomija i schodzi niżej w rankingu do projektu, który „wyzeruje" pulę bez przekroczenia.

   Przykład: pozostało 150 tys. zł w rejonie, kolejny projekt kosztuje 800 tys. zł → pomijany, szukanie tańszego.

4. **Kolizja fizyczna projektów** (§10 Zasad PBO26): przy niemożności jednoczesnej realizacji realizowany ten z większą liczbą głosów.
5. **Remisy** — rozstrzygnięcie wg protokołów w uchwale [do weryfikacji konkretnego paragrafu].

## Frekwencje referencyjne

| Edycja | Ważne głosy |
|---|---|
| PBO24 | 60 817 |
| PBO25 | 52 995 |
| PBO26 | **76 472** (rekord mobilizacji) |

## Antyfraud — znane wektory manipulacji

### Pomyłki rutynowe (wyłapywane automatycznie)

- Niepełne imiona.
- Zmyślone/nieistniejące nazwy ulic (poza siatką topograficzną Poznania).
- Błędne cyfry kontrolne w nr PESEL.

### Zmasowane ataki IP (farmy kliknięć)

Skrypty analityczne UMP/PCSS wychwytywały:

- **Setki głosów z pojedynczego IP** w wąskich oknach czasowych.
- Głosy skoncentrowane na jednym konkretnym projekcie osiedlowym.
- IP nienależące do autoryzowanych stacjonarnych punktów (tam zbieżność IP byłaby legalna).

### Klonowanie tożsamości

- Ten sam numer telefonu dla autoryzacji wielu odrębnych PESELI.
- Fikcyjne adresy + fikcyjne końcówki PESEL.
- Kradzież danych uwierzytelniających.

### Deduplikacja

Wszystkie zidentyfikowane „widmowe głosy" są kasowane przed wygenerowaniem protokołu końcowego. PBO26: usunięto kilkanaście tysięcy fałszywych głosów IP.

## Afera ZSZ nr 1 (PBO25) — manipulacja ocenami

Patrz szczegółowo `09-kontrowersje.md`. W skrócie: Zespół Szkół Zawodowych nr 1 (ul. św. Floriana, Stare Jeżyce) — uczniowie zwalniani z zajęć, zbierali głosy na projekt „Jeżycka Strefa Edukacji i Relaksu", obiecywano im „piątki" z przedmiotów merytorycznych. Śledztwo Kuratorium Oświaty z inicjatywy Karoliny Adamskiej (Dyrektor Wydziału Wspierania Edukacji UMP). Luka regulacyjna: brak etycznego embarga w regulaminie PBO dla szkół angażujących nieletnich.

## Promocja i mikro-kampania (legal)

- Plakaty i ulotki w pasie zieleni komunalnej — wymagają zezwolenia ZDM (płatne za m²/dzień).
- Praktyka dominująca: „karteczki na klamki" bez zajęcia pasa drogowego — tydzień przed głosowaniem + w trakcie.
- Stoiska ze smartfonem po uzyskaniu zgody proboszcza (po mszach niedzielnych) — historycznie wysoka konwersja.

Szczegóły taktyki wyborczej: `10-taktyka-wygrania.md`.
