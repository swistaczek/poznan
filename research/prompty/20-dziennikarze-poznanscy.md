---
prompt_nr: 20
tytul: Baza dziennikarzy zaangażowanych w sprawy poznańskie
data: 2026-05-06
przeznaczenie: deep research (Perplexity Pro / ChatGPT Deep Research / Gemini Deep Research / Claude Research)
target_obszar: research/instytucje/dziennikarze/ (do utworzenia po otrzymaniu wyniku)
target_rozmiar: pełna baza 30–60 dziennikarzy + indeks per-medium + indeks per-temat
---

# Brief deep research — baza dziennikarzy zaangażowanych w sprawy poznańskie

## Twoja rola

Jesteś media-OSINT analystem **top 1%** ze specjalizacją w polskich mediach regionalnych i ogólnopolskich. Pracujesz dla obywatelskiej bazy wiedzy w Poznaniu (`https://swistaczek.github.io/poznan/`). Twoje narzędzia: katalog redakcji, archiwa internetowe (Wayback Machine), wyszukiwarka mediów (Press Service, IMM, Mediabank), profile autorów na X/LinkedIn/Mastodon, RSS-y branżowe, podcasty regionalne. Nie polegasz wyłącznie na Wikipedii — szukasz autorskich sygnatur w tekstach z 2022–2026.

## Cel końcowy

Zbuduj **bazę dziennikarzy** (osób fizycznych — nie redakcji jako instytucji), którzy w ostatnich 4 latach (2022–2026) **regularnie pisali, mówili lub kręcili materiały** o sprawach Poznania, w tematach pokrywanych przez nasze repo:

- transport miejski (tramwaje, autobusy, mosty, drogi, MPK, ZDM)
- spółki miejskie (PIM, Aquanet, MPK Poznań sp. z o.o., MTP Poznań, ZKZL, POSUM, Termy Maltańskie, Modertrans, PTBS, MPGM, WCWI)
- inwestycje kubaturowe i drogowe (Stary Rynek, Mosty Berdychowskie, Trasa Tramwajowa Naramowice, Program Centrum, Wiadukt Lutycka/Golęcińska, Palmiarnia)
- polityka miejska (Rada Miasta Poznania, prezydent Jacek Jaśkowiak, kluby radnych KO/PiS/Trzecia Droga/Lewica)
- rady osiedli (42 jednostki pomocnicze)
- transparentność i kontrola (UDIP, BIP, NIK, CBA, prokuratura, oświadczenia majątkowe)
- ład korporacyjny i kominy płacowe spółek miejskich (skandal IV.2026, Komisja Rewizyjna RM)
- urbanistyka i planowanie przestrzenne (MPZP, WZ, Studium, MPU)
- środowisko i zdrowie (hałas tramwajowy, smog, drzewa, woda, immisje cywilne KC art. 144/222)
- mobilność rowerowa (audyt CROW, ścieżki, polityka rowerowa)
- aktywizm obywatelski i ruchy społeczne (Sieć Wspólnoty Lokalne, Stowarzyszenie My-Poznaniacy, lokalne komitety mieszkańców)

Baza ma służyć trzem celom operacyjnym:

1. **Komu wysyłać sygnały o nowych sprawach obywatelskich** (kto reaguje, kto ignoruje).
2. **Komu proponować materiały ekskluzywne / zwroty UDIP / dokumenty** (zachęta, nie spam).
3. **Komu udzielać wywiadów / komentarzy** (kto zachowuje rzetelność źródeł, kto nie miesza cytatów).

## Schemat per dziennikarz (obowiązkowy)

Każda pozycja w bazie ma zawierać **wszystkie poniższe pola**. Jeśli pole nieznane — wpisz `[brak danych]`, **nie zmyślaj**.

```yaml
imie_nazwisko: <pełne>
pseudonim_handle: <jeśli używa>
aktualna_redakcja: <2026, instytucja + dział>
poprzednie_redakcje:
  - <YYYY–YYYY: redakcja, rola>
  - <chronologia od najnowszych>
specjalizacja_glowna: <1-3 słowa kluczowe, np. „transport miejski", „samorząd", „korupcja JST">
specjalizacje_drugoplanowe: [<lista>]
kontakt:
  email_sluzbowy: <imie.nazwisko@redakcja.pl> | [brak danych]
  twitter_x: <@handle> | [brak danych]
  linkedin: <URL> | [brak danych]
  mastodon_bluesky: <jeśli aktywny> | [brak danych]
  telefon_redakcyjny: <jeśli publiczny> | [brak danych]
reprezentatywne_artykuly_o_poznaniu_2024_2026:
  - data: YYYY-MM-DD
    tytul: "<dokładny>"
    medium: <redakcja>
    url: <pełny>
    temat: <z listy „cele" wyżej>
    waga: kluczowy / istotny / przyczynkowy
  # 3–5 pozycji per dziennikarz, w odwrotnej chronologii
ulubione_tematy:
  - <ranking >50% pokrycia, np. „spółki miejskie", „transport publiczny">
stosunek_do_ump_jaskowiaka:
  ocena: krytyczny / niuansowany / neutralny / przychylny / klakier
  dowod: <konkretny artykuł/cytat z URL>
stosunek_do_aktywistow_obywatelskich:
  ocena: bywa sojusznikiem / neutralny / sceptyczny / niechętny
  dowod: <konkretny artykuł>
reagowal_na_sygnal_obywatelski:
  status: tak / nie / brak danych
  zrodlo: <jeśli udokumentowane: wpis na X, wzmianka w cytacie>
preferowany_kanal_zaczepienia:
  - <kanał: e-mail / DM Twitter / spotkanie / formularz redakcyjny>
  - <komentarz operacyjny: np. „odpowiada w 24h na DM, e-mail ignoruje">
ryzyko_redakcyjne:
  - <czy znany za nadinterpretację, klakierstwo, zmienianie cytatów, niekompletne sourcing'i>
  - <jeśli brak — wpisz „brak udokumentowanych zarzutów">
```

## Zakres mediów do przeszukania

Kompletność jest istotna. Idź po listach poniżej, plus eksploracja po linkach autorskich.

**Lokalne (Poznań):**
- Głos Wielkopolski (Polska Press)
- Gazeta Wyborcza Poznań (Agora)
- epoznan.pl
- codziennypoznan.pl
- wpoznaniu.pl
- naszemiasto.pl/poznan (Polska Press)
- Radio Poznań (Polskie Radio Regionalne)
- Radio Eska Poznań
- Radio ZET Poznań / RMF Poznań
- TVP3 Poznań
- TVN24 (oddział Poznań / korespondencja)
- onet.pl/poznan
- wirtualnemedia.pl (gdy piszą o poznańskich mediach)

**Ogólnopolskie z relewancją poznańską:**
- TVN24 (transport, korupcja JST)
- Onet (śledztwa)
- Wirtualna Polska — wiadomosci.wp.pl
- Polsat News
- Newsweek Polska
- Polityka
- Tygodnik Powszechny (rzadko, ale wraca)
- Rzeczpospolita / Parkiet
- Gazeta Prawna / DGP
- Forsal.pl
- OKO.press (kontrola JST, korupcja)
- Wprost
- Press Service / wirtualnemedia.pl

**Branżowe (transport / urbanistyka / samorząd):**
- transport-publiczny.pl
- rynek-kolejowy.pl
- muratorplus.pl
- propertydesign.pl
- inzynieria.com
- bryla.pl
- Architektura-Murator
- Serwis Samorządowy PAP (samorzad.pap.pl)
- Wspólnota (tygodnik)
- portalsamorzadowy.pl
- A&B (Architektura & Biznes)
- Magazyn Miasta

**Niezależne / autorskie:**
- Substack PL (transport, urbanistyka — szukaj „Poznań")
- YouTube: kanały lokalne („Poznań w pigułce", autorów technologicznych)
- Twitter/X — handle z Poznaniem w bio
- Podcasty: „Raport o stanie świata" (Dariusz Rosiak, gdy dotyka samorządu), regionalne audycje Polskiego Radia
- Mastodon / Bluesky polskich dziennikarzy

## Anchor names — już znane z naszego repo (zaczepki, NIE zamknięta lista)

Te nazwiska są pewne. Użyj ich jako punktu wyjścia: rozszerz na ich krąg redakcyjny, śledź autorską linię.

- **Filip Czekała** (TVN24) — kominy płacowe spółek miejskich Poznania, artykuły 18.03.2026 i 18.04.2026; jakość: rzetelna, dwa źródła, kontekst
- **Szymon Majchrzak** (Radio Poznań) — 16.04.2026 17:59 / 17.04 10:44 — pełne kwoty wynagrodzeń zarządów spółek
- **Filip Wenc** (epoznan.pl, wpoznaniu.pl?) — bieżące tematy Poznania [do weryfikacji]
- **Dziennikarze Codzienny Poznań** — protokół KR 5–6 marca 2026, kontrola wynagrodzeń
- **Dziennikarze Głosu Wielkopolskiego** — komentarz „nieśmieszny żart" o karze 5 tys. zł na Tormela za Stary Rynek (148 mln zł)
- **wPoznaniu.pl** — relacje z budowy Mostów Berdychowskich, wywiady z Mają Chłopocką (PIM)
- **muratorplus.pl** — branżowe materiały o Mostach Berdychowskich, ECF Award

Dla każdego z powyższych: znajdź **autora konkretnego artykułu**, nie tylko medium. Często teksty mają stopki/podpisy autorskie.

## Czego NIE chcemy

- **Nie listy wszystkich dziennikarzy w Polsce.** Tylko ci, którzy mają **udokumentowany ślad autorski** w poznańskich tematach 2022–2026 (min. 2 artykuły).
- **Nie biografii prywatnych** (rodzina, szkoła, hobby — bez znaczenia, chyba że ujawniają konflikt interesów, np. małżonka/małżonek pracuje w UMP).
- **Nie ocen ad hominem** — „dziennikarz X jest sympatykiem PiS / KO" tylko z konkretnym dowodem (wpis na X, kandydowanie z listy partii, członkostwo w klubie parlamentarnym X).
- **Nie zmyślaj e-maili służbowych ani telefonów.** Jeśli redakcja nie publikuje — wpisz `[brak danych]`. Halucynacja kontaktu = utrata reputacji.
- **Nie pomijaj dziennikarzy krytycznych wobec ruchów obywatelskich.** Oni też są ważni — często ich felietony wymuszają reakcję urzędu.
- **Nie podawaj URL-i, których nie zweryfikowałeś.** Każdy URL w bazie ma być dostępny w momencie zapisu (lub mieć notatkę „archive.org snapshot YYYY-MM-DD").
- **Nie pakuj wszystkiego do tabeli.** Profile pełne (per dziennikarz blok 15–25 wierszy) + tabela master jako indeks na końcu.

## Format wyjścia (struktura raportu)

Plik markdown, ~80–150 KB (do podziału na chunki w naszym repo, zob. konwencje `research/CLAUDE.md`).

```markdown
# Baza dziennikarzy zaangażowanych w sprawy poznańskie 2022–2026

## Metoda i źródła

[2-3 akapity: jak szukałeś, jakie filtry, jakie ograniczenia]

## Tabela master (indeks)

| # | Imię i nazwisko | Aktualne medium | Specjalizacja | Top temat 2024–2026 | Stosunek do UMP | Najlepszy kanał kontaktu |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

## Profile pełne (alfabetycznie po nazwisku)

### Nazwisko, Imię

[blok schemy YAML/markdown z pełnym profilem per schemat wyżej]

[3–5 reprezentatywnych artykułów]

[komentarz operacyjny — 2–3 zdania: jak go zaczepić, czego unikać]

---

[następny dziennikarz...]

## Indeksy nawigacyjne

### Per medium
[lista per redakcja — kto pisze tam o Poznaniu]

### Per temat
- Spółki miejskie / kominy płacowe: [...]
- Transport publiczny / tramwaje: [...]
- Mosty i wiadukty: [...]
- Hałas i środowisko: [...]
- Rowery / mobilność: [...]
- Korupcja / oświadczenia majątkowe / NIK: [...]
- Aktywizm obywatelski: [...]
- Urbanistyka / MPZP: [...]
- Rady osiedli / partycypacja: [...]

### Top 10 „gotowi do współpracy"
[ranking z uzasadnieniem — kto reaguje, dla kogo materiał jest priorytetem, kto buduje serię]

### Top 5 „do unikania" lub „ostrożna współpraca"
[z dowodem: kto przekręcał cytaty, kto oddawał materiał urzędowi przed publikacją, kto miesza komentarz z faktem]

## Luki i kierunki dalszego researchu

[czego nie udało się ustalić; kogo podejrzewasz że jest aktywny ale nie znalazłeś autorskich tekstów; co warto zbadać w iteracji 2]
```

## Pytania kontrolne (zrób self-check przed oddaniem)

1. Czy każdy dziennikarz ma **co najmniej 2 reprezentatywne artykuły o Poznaniu** w okresie 2022–2026 z URL-em?
2. Czy żaden e-mail nie jest zmyślony (sprawdź formaty redakcyjne, zwłaszcza Polska Press, Agora, Onet)?
3. Czy odróżniłeś **autorów stałych** od **freelancerów/korespondentów** (różnica operacyjna: stały autor = ścieżka stała, freelancer = projekt do projektu)?
4. Czy w bazie są dziennikarze **z różnych nurtów politycznych** (krytyczni wobec KO, krytyczni wobec PiS, technokraci, eseiści)? Sygnał o pluralizmie.
5. Czy jest minimum 2 dziennikarzy per główny temat z listy (transport, kominy, środowisko, urbanistyka, rowery, aktywizm)?
6. Czy oznaczyłeś **konflikty interesów** (znany związek z UMP / spółką miejską / partią)?
7. Czy w „Top 10 gotowi" i „Top 5 do unikania" decyzje są oparte na **konkretnych dowodach**, a nie odczuciu?
8. Czy każdy URL jest **zweryfikowany** (otwarty raz, sprawdzony że istnieje)?

## Konwencje formalne

- **Po polsku** w 100%.
- **Bez emoji.**
- **Daty w formacie ISO YYYY-MM-DD.**
- Nazwy mediów oryginalne (np. „Gazeta Wyborcza Poznań", nie „Wyborcza").
- URL pełne, nie skrócone (`bit.ly` zakazane).
- Sygnatury / numery uchwał / KRS — dokładnie, jeśli się pojawiają.
- Niepewne dane → `[do weryfikacji]` zamiast pomijania.

---

## Po otrzymaniu wyniku (instrukcja dla następnej sesji Claude)

1. Wklej wynik do `research/instytucje/dziennikarze/wyniki-20-dziennikarze-poznanscy.md` (utworzyć katalog).
2. Rozbij na chunki ≤ 12 KB:
   - `index.md` — tabela master + nawigacja per medium / per temat
   - `01-transport-publiczny.md`
   - `02-spolki-miejskie-kominy.md`
   - `03-srodowisko-halas.md`
   - `04-rowery-mobilnosc.md`
   - `05-urbanistyka-mpzp.md`
   - `06-aktywizm-rady-osiedli.md`
   - `07-korupcja-nik-cba.md`
   - `08-medialny-mainstream-poznanski.md`
   - `99-faq.md` — 12–15 pytań aktywisty (jak zaczepić X, kto pisze o Y, komu wysłać UDIP-zwrot)
3. Zaktualizuj `research/instytucje/index.md` o pozycję bazy.
