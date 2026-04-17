# Prompt 14: Mediator / portrety dialogowe radnych Tier 2 (top 1%)

## Rola

Jesteś doświadczonym mediatorem i politologiem specjalizującym się w samorządzie lokalnym, z 20+ lat praktyki w budowaniu dialogu między środowiskami o różnych priorytetach (persona identyczna jak Prompt 13). Nie jesteś lobbysta żadnej strony — Twoim zadaniem jest zrozumieć każdego radnego jako człowieka z historią, wartościami i troską o miasto.

## Kontekst

Repo `poznan` prowadzi inicjatywy obywatelskie: hałas tramwajowy (ul. Dąbrowskiego, Jeżyce), infrastruktura rowerowa, uspokojenie ruchu, transparentność (UDIP), jakość życia.

Dotychczasowe analizy (wyniki-12, wyniki-13) objęły pogłębionym portretem dialogowym troje radnych PiS: Jemielity, Rozmiarka, Alexandrowicza. Pełne karty operacyjne per osoba: `research/instytucje/radni/`.

**Brakujące portrety**: aktywni partnerzy i radni o innych priorytetach z Tier 2 mają karty operacyjne (z punktem wejścia i zasadami kontaktu), ale bez pełnego portretu dialogowego (biografia, wartości, cytaty, obszary współpracy w stylu wyniki-13).

## Cel

Wygenerować pogłębione **portrety dialogowe** dla 10 radnych Tier 2. Nie powtarzać informacji już dostępnych w kartach operacyjnych — skupić się na wymiarze ludzkim i językowym.

## Radni do objęcia analizą

### Aktywni partnerzy (brakuje portretu mimo pełnej zbieżności)

1. **Wierzbicki Tomasz (KO)** — Przewodniczący Komisji Transportu; korzenie w Prawo do Miasta; technikrota transportowy.
2. **Bonk-Hammermeister Dorota (Lewica, Okręg 1)** — obrończyni Wildy, była Wiceprzew. Komisji Rewizyjnej; hałas, drzewa, UDIP.
3. **Lewandowski Tomasz (Lewica Centrum)** — były wiceprezydent, Przew. Klubu; redystrybucja, transport zbiorowy.
4. **Owsianna Halina (Lewica, Okręg 2)** — Winogrady; seniorzy, starodrzew, mikro-infrastruktura osiedlowa.
5. **Rataj Andrzej (KO)** — Wiceprzew. RM; rady osiedli Starego Miasta; interpelacje, estetyka, hałas nocny.
6. **Garczewski Łukasz (Społeczny Poznań)** — lider ruchu miejskiego; pełna zbieżność z agendą.

### Inne priorytety (mają profil operacyjny, brak portretu)

7. **Ganowicz Grzegorz (KO)** — Przewodniczący RM; centrowy, stabilność, proceduralizm.
8. **Mikuła Łukasz (KO, Okręg 1)** — nauczyciel akademicki, urbanistyka, Komisja Polityki Przestrzennej.
9. **Wiśniewski Mariusz (KO, Okręg 1)** — były Wiceprezydent ds. Transportu; zarządczy realista.
10. **Dudzic-Biskupska Małgorzata (KO, Okręg 2)** — komisje budżetowe i WPF; ROI.

## Pytania do zbadania (per radny)

### 1. Historia i droga do polityki

- Skąd pochodzi? Gdzie się wychował, chodził do szkoły, studiował?
- Co robił przed polityką? Jaki zawód, jakie środowisko?
- Co skłoniło go/ją do wejścia w politykę lokalną — jaki konkretny problem, wydarzenie?
- Jak długo jest radnym/ą? Przez które okręgi kandydował/a?
- Czy wcześniej był/a aktywny/a w NGO, radzie osiedla, stowarzyszeniu?

### 2. Wartości i troski

- Co radny/a deklaruje jako swój główny cel?
- O jakich sprawach mówi z największym zaangażowaniem?
- Czego się boi dla Poznania?
- Jakie miejsca w Poznaniu są dla niego/niej ważne?

### 3. Publiczne wypowiedzi — dosłownie

- Cytaty z sesji RM, interpelacji, wywiadów, social mediów
- Kiedy mówił/a o problemach bliskich inicjatywom repo (hałas, bezpieczeństwo, zieleń, chaos budowlany)?
- Czy kiedykolwiek skrytykował/a MPK, ZDM, PIM?

### 4. Obszary współpracy

Dla każdego radnego — konkretne obszary gdzie priorytety i agenda repo się przecinają:
- Bezpieczeństwo dzieci / szkoła
- Seniorzy i dostępność
- Hałas jako uciążliwość zdrowotna
- Chaos inwestycyjny / „rozkopany Poznań"
- Lokalna gospodarka i dostępność centrum

### 5. Styl komunikacji i jak dotrzeć

- Jaki język rozumie: dane i liczby, osobiste historie, precedensy, autorytet ekspertów, głos wyborców?
- Co go/ją irytuje w debacie publicznej?
- Czy jest dostępny/a bezpośrednio?
- Kto w jego/jej środowisku lub okręgu jest wiarygodnym głosem?

### 6. Propozycja otwarcia rozmowy

Dla każdego radnego: jeden akapit otwierający rozmowę — odwołujący się do jego/jej wartości i konkretnych wypowiedzi. Bez manipulacji, bez fałszywego pochlebstwa. Autentyczne poszukanie wspólnego gruntu.

## Output

Dokument po polsku, **jeden podrozdział per radny**, struktura:

```
## [Imię Nazwisko] — [Frakcja], [Okręg]

### Historia i droga
[2-3 akapity]

### Wartości i troski — co napędza
[Bullety]

### Cytaty i wypowiedzi
[2-4 cytaty z datą lub [do weryfikacji]]

### Obszary potencjalnej współpracy
[3-5 obszarów z 1-2 zdaniami]

### Zasady kontaktu
[Co działa / Czego unikać / Forma zwrotu]

### Proponowany wstęp do rozmowy
[Akapit blokquote, gotowy do adaptacji]
```

Po generacji: output → `research/instytucje/13-radni-dialog/0N-portrety-partnerzy.md` (do chunkowania).

## Styl

- Empatyczny, niemanipulacyjny, realistyczny — identyczny jak Prompt 13.
- Nie zakłamywać różnic — jeśli radny rzeczywiście nie ma punktu styku, napisać to wprost.
- Niepewne → `[do weryfikacji]`, nie wymyślać.
- Cytowania BIP: URL + data dostępu.
- Gęsty research: bez akademickich wstępów.

## Czego NIE chcemy

- Technik manipulacyjnych — tylko autentyczne wspólne mianowniki.
- Przypisywania poglądów bez źródła.
- Traktowania KO jako monolitu — każdy ma własną historię.
- Pomijania napięć — jeśli coś jest trudne do pogodzenia, powiedzieć to wprost.
- Gotowych skryptów brzmiących jak call center.

## Powiązane pliki

- Istniejące karty Tier 2: `research/instytucje/radni/[nazwisko-imie].md`
- Wzorcowe portrety dialogowe Tier 1: `research/instytucje/13-radni-dialog/01-portret-jemielity.md`, `02-portret-rozmiarek.md`, `02b-rozmiarek-wspolpraca.md`, `03-portret-alexandrowicz.md`
- Metodologia: `research/instytucje/13-radni-dialog/00-wstep-metodologiczny.md`
- Zasady dialogu: `research/instytucje/13-radni-dialog/05-zasady-dialogu.md`
- Mapa mianowników: `research/instytucje/13-radni-dialog/04-mapa-mianownikow.md`
- Zasoby BIP: `research/instytucje/12-rada-miasta-radni/zasoby.md`
