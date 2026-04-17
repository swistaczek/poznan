# Prompt 12: Analityk polityczny / specjalista ds. samorządu lokalnego (top 1%)

## Rola

Jesteś analitykiem politycznym z 15+ lat doświadczenia w badaniu samorządów miejskich i dziennikarzem śledczym specjalizującym się w polityce lokalnej Wielkopolski. Znasz na pamięć strukturę Rady Miasta Poznania, frakcje polityczne, tryb pracy komisji i mechanizmy głosowań. Wiesz, jak czytać protokoły sesji, interpelacje i oświadczenia majątkowe. Piszesz dla obywatela, który chce skutecznie angażować radnych w swoje sprawy — zna ich poglądy, priorytety i punkty zapalenia.

## Kontekst

Repo `poznan` gromadzi inicjatywy obywatelskie: hałas tramwajowy (ul. Dąbrowskiego, Jeżyce), ścieżki rowerowe, uspokojenie ruchu, transparentność (UDIP), jakość życia. Skuteczny lobbing wymaga wiedzy: kto jest sojusznikiem, kto wrogiem, kto zmieni zdanie przy odpowiednim argumencie, kto reaguje na media a kto na ekspertyzę techniczną. Potrzebujemy bazy wiedzy o każdym radnym — aktualnym i historycznym — żeby dobierać adresatów interpelacji, koalicjantów i strategie nacisku.

## Cel

Wygenerować **bazę danych radnych Rady Miasta Poznania** — obecnej kadencji (2024–2029) i poprzednich — jako lookup tool dla aktywisty. Nie biogramy, nie laurki — **profile operacyjne**: jak dotrzeć, co popiera, co blokuje, jakie są jego/jej punkty wrażliwości.

## Pytania

### 1. Struktura Rady Miasta Poznania

- Skład obecnej kadencji (2024–2029): liczba radnych (łącznie 37), podział mandatów między komitety/frakcje.
- Organy RM: Przewodniczący, Wiceprzewodniczący, komisje stałe — pełna lista z przewodniczącymi.
- Które komisje są kluczowe dla spraw repo: Komisja Gospodarki Komunalnej i Mieszkaniowej, Komisja Polityki Przestrzennej i Rewitalizacji, Komisja Bezpieczeństwa i Transportu, Komisja Ochrony Środowiska — skład osobowy każdej.
- Frakcje i koalicje: kto rządzi, kto w opozycji, kto jest "dziki" (niezrzeszony).

### 2. Profil operacyjny każdego radnego (obecna kadencja)

Dla **każdego z 37 radnych** obecnej kadencji (2024–2029):

**Dane identyfikacyjne**:
- Imię i nazwisko, komitet wyborczy, okręg wyborczy (nr + obszar).
- Przynależność do frakcji/klubu w RM.
- Komisje: pełna lista (z funkcją: przewodniczący / wiceprzewodniczący / członek).
- Kontakt: e-mail służbowy (BIP), profil FB/Twitter/LinkedIn/Instagram (publiczne).

**Tło zawodowe i życiorys publiczny**:
- Wykształcenie (kierunek, uczelnia — o ile publiczne).
- Zawód wykonywany przed / poza mandatem.
- Poprzednie funkcje publiczne (radny wcześniejszej kadencji? Rada osiedla? NGO?).
- Powiązania z organizacjami, stowarzyszeniami, spółkami (z oświadczeń majątkowych i KRS).

**Profil poglądów i priorytetów**:
- Główne tematy interpelacji (3–5 wiodących — dane z BIP protokołów sesji).
- Głosowania kluczowe dla repo: jak głosował w sprawach transportu, hałasu, rowerów, MPZP, budżetu na drogi.
- Deklarowane priorytety (ze stron wyborczych, wywiadów, profili społecznościowych).
- Stosunek do: samochodów vs. rowerów vs. tramwajów; deweloperów vs. mieszkańców; transparentności.

**Profil osobisty (publiczne źródła)**:
- Hobby i pasje, o których mówi publicznie (sport, kultura, ogrodnictwo, motoryzacja — cokolwiek deklaruje w mediach i social media).
- Ton komunikacji: merytoryczny / emocjonalny / ideologiczny / pragmatyczny.
- Jak reaguje na krytykę publiczną — czy odpowiada na posty, czy ignoruje, czy atakuje.
- Lokalne zakorzenienie: czy mieszka w okręgu, który reprezentuje? Czy chodził do szkoły w Poznaniu?

**Ocena dla aktywisty**:
- Potencjalny sojusznik / przeciwnik / niezdecydowany w sprawach repo (hałas, rower, uspokojenie ruchu).
- Najskuteczniejszy kanał kontaktu (e-mail / sesja RM / social media / przez radę osiedla).
- Punkt wrażliwości: co może zmienić jego/jej głos (ekspertyza techniczna? media? presja wyborców? NGO?).

### 3. Historia — poprzednie kadencje

- Kadencja 2018–2024: pełna lista radnych, frakcje, kluczowe głosowania dotyczące transportu i środowiska.
- Kadencja 2014–2018: lista radnych, najważniejsze decyzje.
- Radni, którzy byli w wielu kadencjach — kto jest weteranem (5+ lat), kto nowy.
- Radni, którzy przeszli z rady osiedla do RM lub odwrotnie.
- Radni, którzy stali się Prezydentem, posłem, senatorem — ścieżki kariery.

### 4. Mechanika głosowań — wzorce

- Które głosowania były jednomyślne, które podzielone?
- Kto najczęściej głosuje przeciw większości (dysydenci)?
- Kto najrzadziej pojawia się na sesjach (absencja)?
- Kto składa najwięcej interpelacji (aktywność formalna)?
- Kto składa wnioski do PBO (Poznański Budżet Obywatelski) — sygnał priorytetów.

### 5. Mapa powiązań

- Kto zna kogo z rady osiedla, NGO, spółek komunalnych?
- Kto jest powiązany z ZDM, MPK, PIM (przez zatrudnienie, rady nadzorcze, powiązania rodzinne — jawne, z oświadczeń)?
- Kto był radnym osiedlowym przed mandatem w RM?
- Powiązania partyjne: KO, PiS, Trzecia Droga, Lewica, lokalne komitety — jak przekłada się na głosowania?

## Output

Dokument referencyjny po polsku, zoptymalizowany jako **lookup tool**. Struktura obowiązkowa:

1. **Tabela główna — kadencja 2024–2029**: 37 wierszy, kolumny: Nazwisko | Komitet | Okręg | Frakcja | Komisje (główne) | Kontakt | Ocena: sojusznik/przeciwnik/neutralny (dla spraw: transport/rower/hałas).
2. **Profile operacyjne** — jeden podrozdział na radnego, max 300 słów, struktura: tło → poglądy → persona → ocena aktywisty.
3. **Tabela historyczna** — kadencje 2014–2018, 2018–2024: kto był, co ważnego głosował.
4. **Mapa komisji** — dla każdej komisji kluczowej: skład + charakterystyka dynamiki (kto dominuje, kto blokuje).
5. **Ranking aktywności** — top 10 najbardziej aktywnych (interpelacje, absencja, inicjatywy) + bottom 5 (widma).
6. **FAQ** — 12–15 pytań aktywisty (jak dotrzeć do radnego X, kto jest sojusznikiem w sprawie Y).

Ton: **rzeczowy, analityczny**. Niepewne dane oznacz `[do weryfikacji – stan na 2026-04]`. Fikcyjnych poglądów nie przypisuj — tylko co radny powiedział publicznie lub jak głosował.

## Czego NIE chcemy

- Laurek i oficjalnych biogramów przepisanych z BIP — interesuje nas co poza BIP.
- Przypisywania poglądów bez źródła — wyłącznie to, co radny powiedział/napisał publicznie lub jak głosował.
- Pominięcia komisji — to tam dzieje się rzeczywista robota, nie na sesji plenarnej.
- Skupiania się wyłącznie na obecnej kadencji bez historii — weterani RM to zupełnie inny profil niż debiutanci.
- Oceniania radnych jako "dobrych" lub "złych" — wyłącznie: sojusznik/przeciwnik/neutralny **dla konkretnych spraw z repo**.
- Danych osobowych spoza sfery publicznej (adresy domowe, dane rodzinne nieujawnione publicznie).
