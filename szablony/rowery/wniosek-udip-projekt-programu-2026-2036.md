---
title: "Wniosek UDIP — projekt Programu Rowerowego 2026–2036, harmonogram konsultacji i dane liczników"
type: template
domain: rowery
adresat_typ: [ZDM-Poznań]
podstawa_prawna:
  - art. 61 Konstytucji RP
  - art. 2 ust. 1, art. 10 ust. 1, art. 13 Ustawy o dostępie do informacji publicznej z 6.09.2001 (Dz.U. 2022 poz. 902 z późn. zm.)
updated: 2026-05-29
---

# Wniosek o udostępnienie informacji publicznej — Program Rowerowy 2026–2036

**Do:**
Zarząd Dróg Miejskich w Poznaniu
ul. Wilczak 17, 61-623 Poznań
e-mail: zdm@zdm.poznan.pl / ePUAP

**Wnioskodawca:** {{IMIE_NAZWISKO}}, {{ADRES}}, {{EMAIL}}

**Data i miejsce:** {{MIEJSCOWOSC}}, {{DATA}}

---

Szanowni Państwo,

na podstawie art. 61 Konstytucji Rzeczypospolitej Polskiej oraz art. 2 ust. 1 i art. 10 ust. 1 ustawy z dnia 6 września 2001 r. o dostępie do informacji publicznej (t.j. Dz.U. 2022 poz. 902) **wnoszę o udostępnienie następujących informacji publicznych:**

## A. Projekt programu i procedura

1. Aktualny projekt „Programu Rowerowego Miasta Poznania na lata 2026–2036" (lub dokumentu pod inną nazwą, zastępującego Program Rowerowy 2017–2022 z perspektywą do 2025, przyjęty uchwałą Nr XLVIII/843/VII/2017) — w wersji na dzień rozpatrzenia wniosku, wraz z załącznikami; jeżeli powstały dotychczas wyłącznie założenia lub teza projektu, wnoszę o ich udostępnienie.

2. Harmonogram prac nad projektem: etapy, terminy oraz planowana data skierowania projektu pod obrady Rady Miasta Poznania.

3. Harmonogram konsultacji społecznych projektu: planowany termin, forma (spotkania, ankieta, zbieranie uwag), termin składania uwag, jednostka prowadząca oraz kanał publikacji ogłoszenia o konsultacjach.

4. Skład zespołu lub komitetu sterującego opracowującego projekt (jednostki organizacyjne, podmioty zewnętrzne, ekspert do spraw polityki rowerowej).

## B. Cele programu i ich relacja do SUMP

5. Docelowy wskaźnik udziału roweru w podziale zadań przewozowych (modal split) miasta Poznania, przyjęty lub rozważany w projekcie programu — wraz z wartością bazową, wartościami pośrednimi oraz rokiem docelowym.

6. Informacja, w jaki sposób projektowany miejski cel udziału roweru odnosi się do celu określonego w Planie Zrównoważonej Mobilności Metropolii Poznań 2040 (SUMP, uchwała Nr XCV/1825/VIII/2023), w którym udział podróży rowerowych w rdzeniu aglomeracji zaplanowano jako spadek z 12,54% do 11,85% — w szczególności, czy program miejski powiela tę trajektorię, czy zakłada wzrost, a jeżeli wzrost — do jakiej wartości.

7. Wykaz tras zakwalifikowanych w projekcie jako priorytetowe do realizacji w latach 2026–2036, ze wskazaniem odcinków uznanych w sprawozdaniu z realizacji poprzedniego programu za „brakujące" oraz „wymagające dalszych działań".

## C. Dane pomiarowe

8. Zagregowane dane zliczeń ze wszystkich automatycznych liczników rowerowych (Eco-Counter, 38 punktów pomiarowych) za okres od 1 stycznia 2023 r. do 31 grudnia 2025 r., w formacie umożliwiającym przetwarzanie (CSV lub XLSX), wraz z metadanymi: identyfikator i lokalizacja (współrzędne) punktu pomiarowego, kierunek detekcji oraz informacja o kompletności szeregu (okresy awarii).

9. Informacja, czy i w jakim zakresie w pracach nad programem zostaną uwzględnione wyniki badań ruchu planowanych na 2026 r. (aktualizacja modelu transportowego w związku z uchwałą Nr L/894/VIII/2021), oraz sposób ich udostępnienia.

## Sposób i forma udostępnienia

Wnoszę o udostępnienie informacji w formie elektronicznej, na adres e-mail wskazany powyżej. Dane, o których mowa w pkt 8, proszę przekazać w formacie edytowalnym (CSV/XLSX).

Jednocześnie informuję, że żądane dane pomiarowe stanowią informację już posiadaną przez Zarząd w systemie pomiarowym, a nie informację przetworzoną w rozumieniu art. 3 ust. 1 pkt 1 ustawy. Gdyby jednak organ uznał którykolwiek z elementów wniosku za informację przetworzoną, wskazuję jako szczególnie istotny interes publiczny: umożliwienie obywatelskiej kontroli kształtu wieloletniego (2026–2036) programu rowerowego miasta oraz weryfikację zasadności przyjmowanego celu udziału roweru w podziale zadań przewozowych.

Zgodnie z art. 13 ust. 1 ustawy oczekuję udostępnienia informacji bez zbędnej zwłoki, nie później niż w terminie 14 dni od dnia złożenia wniosku.

Z wyrazami szacunku,
{{IMIE_NAZWISKO}}

---

## Notatki operacyjne (NIE część pisma — usunąć z kopii wysyłanej)

### Kontekst merytoryczny
- Program 2017–2025 (XLVIII/843/VII/2017) wygasł; nowy 2026–2036 „w przygotowaniu" (Raport o stanie Miasta 2025: zał. 2 s. 34, 50; zał. 4 s. 139–140).
- Cel 12% niezrealizowany (faktycznie 8% w mieście, zał. 1 Tab. 7 s. 30); trasy 44% gotowe / 36% wymagające działań / 23% brak (zał. 4 s. 140).
- Antycel SUMP (XCV/1825/VIII/2023): cała Metropolia 10,69% → 10,23% (2040), rdzeń 12,54% → 11,85% (zał. 2 Tab. 3 s. 28–29). Pełna analiza: `research/raporty-miasta/raport-o-stanie-2025/antycel-rowerowy-sump-analiza.md`.
- Cel pisma: poznać projekt i harmonogram (nie przegapić wyłożenia) + zdobyć dane liczników (dowód popytu kontra cel malejący) + ustalić, czy miejski cel powiela antycel SUMP.

### Procedura wysyłki (per szablony/CLAUDE.md)
1. `cp` do `rowery/pisma/YYYY-MM-DD_ZDM_udip-program-2026-2036.md` (folder lokalny, ignorowany przez git — NIE commitować).
2. Wypełnić pola `{{...}}`, usunąć sekcję „Notatki operacyjne".
3. Frontmatter kopii: `typ: wniosek-udip` → dodać `wyslano: YYYY-MM-DD`, `adresat: Zarząd Dróg Miejskich w Poznaniu`, `termin_odpowiedzi: YYYY-MM-DD` (+14 dni).
4. Wysyłka e-mail (zdm@zdm.poznan.pl) lub ePUAP; zachować potwierdzenie nadania (UPP).
5. Wpis do `rowery/pisma/REJESTR.md` — zsanityzowany (sygnatura neutralna, bez danych osobowych).

### Eskalacja
- Milczenie >14 dni → skarga na bezczynność do WSA w Poznaniu, bez wezwania (art. 3 § 2 pkt 8 p.p.s.a.), wpis 100 zł, żądanie stwierdzenia rażącej bezczynności + grzywny. Szablon: `szablony/transparentnosc/skarga-na-bezczynnosc-wsa.md`.
- Odmowa (decyzja, art. 16 UDIP) → wniosek o ponowne rozpatrzenie do organu → skarga do WSA. Szablon: `szablony/transparentnosc/odwolanie-od-decyzji-odmownej-sko.md` (dostosować — przy UDIP organ I instancji rozpatruje ponownie, nie SKO).
- Przekazanie wg właściwości (część zakresu może dotyczyć Wydziału UMP / Stowarzyszenia Metropolia Poznań dla SUMP) → odnotować, pilnować terminu u organu przejmującego.

### Powiązane szablony
- `szablony/rowery/wniosek-udip-dane-ecocounter.md` — gdy pkt 8 (dane liczników) składać osobno (szersza specyfikacja, rozdzielczość 15-min).
- `szablony/rowery/interpelacja-priorytet-rowerowy.md` — kanał radny, gdy uwagi do programu nieuwzględnione.
- `szablony/transparentnosc/wniosek-udip-informacja-przetworzona.md` — gdy organ podniesie zarzut z art. 3 ust. 1 pkt 1.
