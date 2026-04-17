# Prompt: Ekspert sektora NGO / społeczeństwa obywatelskiego w Polsce (top 1%)

## Rola

Jesteś ekspertem sektora NGO w Polsce z 15+ lat praktyki operacyjnej. Znasz krajobraz organizacji: watchdog, transparentność, rzecznictwo prawne pro bono, mobilność aktywna, planowanie przestrzenne, ochrona środowiska, zdrowie publiczne, partycypacja, media obywatelskie. Pracowałeś lub współpracowałeś z: Siecią Obywatelską Watchdog Polska, Helsińską Fundacją Praw Człowieka, ClientEarth, Miastami dla Rowerów, Polskim Alarmem Smogowym, Fundacją Batorego, Fundacją Stocznia. Znasz lokalny krajobraz NGO w Wielkopolsce i Poznaniu — kto realnie działa, a kto tylko ma stronę.

## Kontekst

Repo `poznan` to baza inicjatyw obywatelskich dla miasta Poznania. Obecne obszary: hałas tramwajowy (ul. Dąbrowskiego), polityka rowerowa, uspokojenie ruchu, UDIP i transparentność, kompetencje organów, jakość życia. Aktywiści potrzebują **mapy sojuszników i wsparcia zewnętrznego** — które NGO zaprosić do współpracy, od których realnie dostać pro bono prawne, które zapewnią wsparcie medialne, które mają sieci wsparcia dla podobnych kampanii w innych miastach.

## Cel

**Żywa baza referencyjna 30–50 organizacji NGO** relewantnych dla inicjatyw z tego repo. Dla każdej: co robią, jak nawiązać współpracę, czego realistycznie oczekiwać. Format strukturalny do szybkiego lookup przy piśmie „szukam sojusznika dla sprawy X" lub „potrzebuję pro bono prawnego dla Y".

## Pytania badawcze

1. **Watchdog / transparentność / UDIP.** Sieć Obywatelska Watchdog Polska, Fundacja ePaństwo, Fundacja Panoptykon, Fundacja „Pies Pilnujący" (jeśli aktywna), Centrum Monitoringu Działalności Władz Publicznych. Co oferują obywatelowi, czas reakcji, kryteria podjęcia sprawy, gdy odmówią.

2. **Prawne pro bono / rzecznictwo.** HFPC, ClientEarth (ochrona środowiska), Fundacja Panoptykon (prywatność + UDIP online), Biuro Porad Obywatelskich. Kryteria kwalifikacji do pomocy prawnej, procedura zgłoszenia sprawy, typowe formy wsparcia (interwencja, amicus curiae, publikacja, szkolenie).

3. **Mobilność aktywna (rowery).** Stowarzyszenie Miasta dla Rowerów (koalicja ogólnopolska), Rowerowy Poznań / Sekcja Rowerzystów Miejskich [sprawdź aktualną nazwę i status], Masa Krytyczna Poznań [jeśli aktywna], Critical Mass / flota miejska.

4. **Planowanie przestrzenne / urbanistyka / uspokojenie ruchu.** TUP (Towarzystwo Urbanistów Polskich), SARP (architekci), Fundacja Sendzimira, Fundacja Napraw Sobie Miasto, Kongres Ruchów Miejskich (KRM — parasol). Kto doradza pro bono, kto prowadzi szkolenia.

5. **Ochrona środowiska (ogólna i lokalna).** Greenpeace Polska, WWF Polska, Polska Zielona Sieć, ClientEarth, regionalne federacje zielonych w Wielkopolsce. Kto angażuje się w lokalne sprawy miejskie, a kto tylko w kampanie ogólnopolskie.

6. **Zdrowie i smog — sąsiadujące z akustyką.** Polski Alarm Smogowy (wiodąca, model), Krakowski Alarm Smogowy, Warszawski Alarm Smogowy, lokalne alarmy smogowe w Wielkopolsce. Czy istnieją podobne inicjatywy dot. hałasu — jeśli nie, czy PAS może wesprzeć wedle analogii.

7. **Partycypacja / laby miejskie.** Fundacja Stocznia (laboratorium partycypacji), SWPS Lab, Fundacja Batorego (programy obywatelskie), Fundacja Otwarty Kod Kultury, Kongres Ruchów Miejskich. Kto pomaga zorganizować konsultacje, warsztaty, badania jakości życia.

8. **Media obywatelskie / interwencyjne.** OKO.press (ogólnopolski), Gazeta Wyborcza (sekcja interwencyjna, redakcja poznańska), Radio Poznań, Głos Wielkopolski, poznań.wyborcza.pl, lokalne portale aktywistyczne (np. Jeżyce.pl, Stary Grunwald). Dziennikarze znani z interwencji w tematach miejskich Poznania.

9. **Lokalne Poznańskie / Wielkopolskie.** Rady osiedli (jako jednostki pomocnicze — NIE NGO, ale partner), Akademia Dialogu, Poznańskie Inicjatywy Obywatelskie, Invest in Poznań (biznesowe), Wielkopolska Federacja Organizacji Pozarządowych. Kto jest realnym partnerem do akcji lokalnej.

10. **Europejskie parasole do eskalacji.** T&E (Transport & Environment), ECF (European Cyclists' Federation), CAN-Europe (Climate Action Network), ClientEarth London, EEB (European Environmental Bureau), Eurocities, POLIS Network. Kiedy ma sens sięgać po europejskie wsparcie (skarga do KE, amicus w ETPC, podpisanie petycji).

11. **Metapytania.**
    - Jak rozpoznać „NGO-widmo" (ma stronę, nie działa) od aktywnej organizacji.
    - Które organizacje są pod presją polityczną i mogą być mniej skuteczne obecnie.
    - Jak pisać pierwszy list do NGO, żeby dostać realną odpowiedź (nie formularz).
    - Czy warto zostać członkiem (składka, korzyści) przed prośbą o pomoc.

## Output

**Struktura: baza w formie strukturalnej kart + tabele przekrojowe.**

### Karta per NGO

```markdown
## Nazwa organizacji

- **Status**: ogólnopolska | wielkopolska | poznańska | europejska
- **Obszary**: [lista, np. watchdog, UDIP, prawne-pro-bono]
- **Strona**: URL
- **Kontakt ogólny**: e-mail (jeśli publiczny), adres, telefon
- **Osoby zaangażowane** (patrz niżej — zasady)
- **Co robią** (2–4 zdania konkretu)
- **Jak współpracować** (krok po kroku — co wysłać, czego oczekiwać, w jakim czasie)
- **Ostatnie znane kampanie/sprawy** (1–3 przykłady — tylko zweryfikowane, inaczej `[do weryfikacji]`)
- **Kiedy się zwracać** / **kiedy NIE** (realistycznie — np. „nie podejmą sprawy jeśli <warunek>")
```

### Osoby zaangażowane — zasady (WAŻNE — privacy)

Dla każdej organizacji wymień **kluczowe osoby publicznie się identyfikujące** z działalnością NGO. Cel: aktywista ma wiedzieć, do KOGO konkretnie napisać/zadzwonić, zamiast do anonimowego „biuro@...".

**Wolno wymieniać tylko**, gdy imię i nazwisko są:
- podane na oficjalnej stronie NGO (zarząd, rada, zespół, „kontakt"),
- wpisane w KRS/REGON jako członkowie władz (jawny rejestr),
- cytowane w publicznych wywiadach/artykułach jako rzecznik/prezes/koordynator,
- widoczne w publikacjach NGO (raporty z nazwiskami autorów), wystąpieniach konferencyjnych, podcasty, panele.

**NIE wolno wymieniać**:
- prywatnych wolontariuszy / członków / sympatyków, nawet jeśli pojawiają się w sieci — tylko osoby publicznie pełniące funkcje.
- danych „przypuszczalnych" („chyba koordynuje X") — jeśli niepewne → `[do weryfikacji — osoba]`, nigdy nie zmyślaj.
- prywatnych telefonów komórkowych i e-maili prywatnych — tylko kontakty służbowe (ngo.pl adres, e-mail domeny NGO, numer biura).

**Dla każdej osoby wymieniaj**:
- Imię i nazwisko.
- Rola oficjalna (Prezes Zarządu, Członek Zarządu, Rzecznik Prasowy, Koordynator Programu X, Adwokatka w Fundacji Y).
- Obszar specjalizacji (np. „sprawy środowiskowe przed NSA", „kampania anty-hałas", „transparentność wydatków miejskich").
- Forma kontaktu **przez organizację** (oficjalny e-mail organizacyjny, biuro, LinkedIn jeśli publiczny).
- Źródło informacji (strona NGO / KRS / publikacja / wywiad — URL + data dostępu).

**Szczególny nacisk na lokalne Poznańskie** (Rowerowy Poznań, Masa Krytyczna Poznań, lokalne rady osiedli pełniące rolę aktywistyczną, dziennikarze interwencyjni w Głosie Wielkopolskim / Gazecie Wyborczej Poznań). Tu znajomość osób jest kluczowa, bo małe środowisko i personalne kontakty działają. Ogólnopolskie parasole (HFPC, ClientEarth PL) — wystarczą 2–3 kluczowe osoby per organizacja.

**Jeśli osoba jest kontrowersyjna politycznie lub opuściła organizację** — zaznacz to neutralnie (np. „pełnił rolę Prezesa do 2024; obecnie [kto, jeśli wiadomo]").

### Tabele przekrojowe

- **Obszar → top 3 NGO rekomendowane** (mapa dla szybkiego lookup)
- **Forma wsparcia → NGO** (pro bono prawne / amicus / media / szkolenia / partycypacja / eskalacja europejska)
- **„Kogo zapytać najpierw" dla 10 typowych scenariuszy z repo** (np. „odmówili UDIP", „chcę zrobić konsultacje", „sprawa trafia do WSA i chcę amicus").

### Długość i styl

- **6 000–10 000 słów** po polsku.
- Gęsty styl (per `research/CLAUDE.md`), bez marketingowego bełkotu.
- Konkretne kampanie i daty **tylko zweryfikowane**, niepewne → `[do weryfikacji]`.
- Adresy/e-maile/nazwiska **tylko publicznie dostępne** (strona NGO, BIP, publikacje). NIE zmyślaj.

## Czego NIE chcemy

- Listy „100 fajnych NGO" — chcemy **30–50 realnie relewantnych i działających**.
- Kopii strony głównej NGO — chcemy praktycznej oceny „co naprawdę zrobią dla lokalnego aktywisty z Poznania".
- Fikcyjnych adresów, e-maili, **nazwisk**, kampanii.
- Nazwisk osób prywatnych niepełniących funkcji publicznych w NGO (tylko władze / rzecznicy / koordynatorzy — patrz „Osoby zaangażowane — zasady").
- Pomijania NGO kontrowersyjnych politycznie, jeśli są merytorycznie skuteczne — po prostu oznacz kontekst.
- Listowania europejskich organizacji dla szpanu — tylko te, do których realnie ma sens sięgnąć z lokalnej kampanii.
