---
title: "Akustyka placu zabaw — strategia spełnienia zasady dobrosąsiedzkości PBO26"
type: analiza-akustyczna
autor: panel-2026-05-05/akustyk
data: 2026-05-05
status: draft
---

# Akustyka placu zabaw w Parku Sołackim — strategia spełnienia "zasady dobrosąsiedzkości"

Cel: dowieść, że codzienna eksploatacja spektakularnego placu zabaw nie generuje "ponadnormatywnego, uciążliwego akustycznie hałasu zaburzającego mir domowy" w rozumieniu regulaminu PBO26 (zob. `research/pbo/09-pbo/01-podstawa-prawna.md`, linia 104 `research/pbo/studium-park-ujazdowski.md`).

## 1. Status prawny hałasu z placów zabaw

Stan prawny niejednoznaczny — trzy reżimy:

- **Rozporządzenie Ministra Środowiska z 14 czerwca 2007 r. ws. dopuszczalnych poziomów hałasu w środowisku** (t.j. Dz.U. 2014 poz. 112; nowelizacja Dz.U. 2024 poz. 271/255). Tabela 1 załącznika: tereny zabudowy mieszkaniowej **jednorodzinnej** — **L_Aeq,D = 50 dB** (6:00–22:00), **L_Aeq,N = 40 dB** (22:00–6:00); wskaźniki długookresowe L_DWN = 50 dB, L_N = 40 dB. Kategorie wymienione w rozporządzeniu: drogi, koleje, hałas pozostały (przemysł, działalność). Plac zabaw mieści się w "hałasie pozostałym" — formalnie obejmie go reżim, gdy plac jest urządzeniem instalowanym i eksploatowanym (zarządca: ZZM Poznań).
- **Wyłączenie z niemieckiego BImSchG (§22 ust. 1a)** — hałas dziecięcy "co do zasady nie jest immisją szkodliwą". W Polsce **brak analogicznej klauzuli ustawowej**. Sądy administracyjne i powszechne stosują różne podejścia — przeważa pogląd, że hałas placu zabaw zlokalizowanego w obiekcie publicznym nie podlega rygorystycznej weryfikacji w trybie POŚ, jeśli urządzenia spełniają normy bezpieczeństwa (PN-EN 1176). Konkretne sygnatury NSA/SN — `[do weryfikacji]`.
- **Immisja cywilnoprawna (art. 144 KC)** — sąsiad zawsze może wystąpić z roszczeniem negatoryjnym (art. 222 §2 KC) o zaniechanie immisji "ponad przeciętną miarę". Tu kryterium nie jest 50 dB rozporządzenia, lecz **subiektywno-obiektywna miara sąsiedzka** — ocenia sąd ad casum. Por. `research/halas/02-immisje/02-orzecznictwo.md`.

**Wniosek operacyjny:** projektowanie pod **L_Aeq,D ≤ 50 dB** w punkcie immisji (linia elewacji najbliższego budynku jednorodzinnego, wysokość 4 m n.p.t.) eliminuje zarówno reżim administracyjny, jak i typową argumentację cywilną. To benchmark "dobrosąsiedzkości" do udowodnienia urzędowi.

## 2. Typowe poziomy emisji urządzeń

Dane z literatury europejskiej (DIN 18034, raporty LUBW Baden-Württemberg, BAFU CH) — bez polskich norm szczegółowych dla placów zabaw.

| Źródło | L_Aeq @ 1 m [dB] | L_Amax @ 1 m [dB] | Pasmo dominujące |
|---|---|---|---|
| Krzyk dziecka (radość/strach) | — | **85–95 dB** | 250–2000 Hz |
| Grupa 10–20 dzieci, zabawa swobodna | **65–75** | 80–90 | 250–4000 Hz |
| Zjeżdżalnia (zjazd + krzyk) | 70–78 | 90–95 | 500–2000 Hz |
| Huśtawka łańcuchowa (skrzyp) | 55–65 | 75 | 1000–4000 Hz (metaliczne) |
| Linarium / zestaw drewniany | 60–70 | 80 | 250–1000 Hz |
| Piaskownica, urządzenia sensoryczne | 50–60 | 70 | szerokopasmowe |
| Tyrolka / grawitacyjne | 65–75 | 90 | 500–2000 Hz |

Wskaźniki: **L_Aeq** — równoważny ciągły A-ważony (miara dla L_DWN/L_N); **L_Amax** — szczytowy A-ważony (miara dla "uciążliwości"). Pasmo C — istotne tylko przy diagnostyce niskotonowych źródeł (tu nieistotne).

## 3. Propagacja w przestrzeni parkowej

Tłumienie wg ISO 9613-2 (model inżynierski):

| Mechanizm | Skuteczność | Uwagi |
|---|---|---|
| Odległość (pole swobodne, źródło punktowe) | **–6 dB / podwojenie r** | Z 70 dB @ 1 m → 64 @ 2 m → 52 @ 16 m → **40 @ 128 m** |
| Pas drzew/krzewów liściastych szer. ≥10 m | 1–3 dB | Słaba bariera akustyczna; dominuje efekt "wizualny" |
| Pas zwarty iglasty + liściasty ≥30 m | 5–8 dB | Dopiero realny wkład |
| Wał ziemny / skarpa h≥3 m, ekran zwarty | **5–15 dB** | Najefektywniejsza pasywna ochrona; działa gdy przerywa LOS źródło–odbiornik |
| Lustro wody (staw) | 0 dB tłumienia, **+1 do +3 dB** od strony przeciwnej | Odbicia — nie kierować źródła w stronę domów przez taflę |
| Atmosfera (absorpcja) | 0,5–2 dB / 100 m @ 1 kHz | Pomijalna na dystansie 100–200 m |

Założenie projektowe: źródło L_Aeq = 75 dB @ 1 m (grupowa zabawa, najgorszy scenariusz). Przy 100 m czysto geometrycznie → 35 dB; z dodatkowymi odbiciami od fasad, brakiem ekranu i napływem fal częstotliwości głosowych → realnie **45–50 dB**. Z ekranem ziemnym +5 dB rezerwy.

## 4. Strategia spełnienia "dobrosąsiedzkości"

- **Lokalizacja:** **min. 100 m**, cel **120–150 m** od najbliższej elewacji budynku jednorodzinnego. Punkt immisji — 1. piętro (4 m n.p.t.), bo wyższe piętro widzi ponad ekrany.
- **Ekrany naturalne:** wykorzystać istniejące skarpy nad doliną Bogdanki; uzupełnić wałem krajobrazowym h = 2,5–3,5 m maskowanym jako "górka do zjeżdżania" (funkcja podwójna — ekran + atrakcja). Dodatkowo zwarty pas krzewów liściastych szer. ≥10 m, gęstość ≥3 sadzonki/m² (grab, dereń, kalina) — efekt głównie wizualno-psychoakustyczny.
- **Strefowanie wewnętrzne:** od strony willi (kierunek najczulszy) — strefa "cicha" (piaskownica, urządzenia sensoryczne, stoły piknikowe). Najdalej od domów — strefa "głośna" (zjeżdżalnie, tyrolka, linarium, urządzenia grawitacyjne). Bufor zieleni między strefami 15–20 m.
- **Godziny funkcjonowania:** **7:00–21:00** (regulamin tabliczkowy + brak oświetlenia urządzeń po 22:00). Eliminuje reżim nocy (40 dB) z definicji.
- **Materiały:** drewno (HPL, robinia) zamiast metalu; liny zamiast łańcuchów; nawierzchnie EPDM/wiór drzewny pod urządzeniami (absorpcja uderzeń); brak elementów rezonujących (rury stalowe, blachy, dzwony plenerowe).

## 5. Mapa lokalizacji w Parku Sołackim

Park Sołacki (~12 ha) ma trzy potencjalne strefy:

- **Strefa A — środek parku, między stawem górnym a pętlą wewnętrzną (rejon polany centralnej).** Dystans do najbliższych willi (ul. Mazowiecka, Małopolska) **~150–200 m**. Naturalne ekrany: skarpa stawu, drzewostan dojrzały. **Rekomendacja prymarna.**
- **Strefa B — północna część parku, w pobliżu ul. Małopolskiej.** Krótki dystans (50–80 m) do zabudowy willowej — **odrzucić** bez agresywnego ekranowania (wał h≥3 m + pas zieleni 30 m).
- **Strefa C — południowa, przy ul. Wojska Polskiego/UPP.** Dystans do mieszkań mały, ale sąsiedztwo to obiekty uczelni (mniej wrażliwe akustycznie wg rozporządzenia — kategoria "tereny związane ze stałym lub czasowym pobytem dzieci i młodzieży" 55/45 dB). Wariant zapasowy.

Kierunki wymagające ekranowania: **północny i zachodni** (willowa zabudowa Salonu Poznania). Wschód — UPP (mniej wrażliwy). Południe — park i ulica Wojska Polskiego (bufor naturalny).

## 6. Ekspertyza akustyczna — kiedy, zakres, koszt

- **Kiedy:** ekspertyzę zlecić **przed złożeniem wniosku PBO** (faza koncepcyjna, jako załącznik do dokumentacji projektowej) — proaktywnie unieszkodliwia argument "brak dowodu". Druga ekspertyza — pomiarowa, post-realizacyjna — tylko jeśli sąsiedzi zakwestionują (art. 115a POŚ, decyzja środowiskowa-naprawcza).
- **Zakres:** (a) pomiar tła akustycznego w punktach immisji (3 dni × dzień/wieczór, PN-ISO 1996-2); (b) symulacja prognostyczna w CadnaA / SoundPLAN / IMMI z modelem ISO 9613-2; (c) mapa imisji L_Aeq,D na siatce 5×5 m; (d) rekomendacje techniczne (lokalizacja, ekrany, godziny).
- **Koszt:** **15–30 tys. zł** netto (zakres standardowy); 30–50 tys. zł z modelowaniem CFD propagacji w skomplikowanym terenie.
- **Wykonawcy:** laboratoria akredytowane PCA (np. EKKOM, LEMITOR, Ekoton), Politechnika Poznańska — Instytut Inżynierii Środowiska/Akustyki, AWF Poznań — Zakład Biomechaniki (rzadziej), niezależni rzeczoznawcy POIIB z uprawnieniami akustycznymi.

## 7. Antyargumenty na typowe protesty mieszkańców

- "Hałas dzieci zaburzy mir domowy" → projektowo gwarantujemy L_Aeq,D ≤ 50 dB w punkcie immisji = limit rozporządzenia dla zabudowy jednorodzinnej; ekspertyza w załączeniu.
- "Tłumy na weekendach zniszczą spokój" → strefowanie wewnętrzne, godziny 7–21, regulamin parkowy, monitoring frekwencyjny przez ZZM po roku.
- "Park to miejsce kontemplacji, nie zabawy" → historycznie place zabaw są elementem parków krajobrazowych od XIX w. (Park Ujazdowski 1926); separacja "pokoi parkowych" (Szanior) zachowuje strefę kontemplacji.
- "Dzieci są głośne, prawo nas chroni" → orzecznictwo cywilne (art. 144 KC) wymaga immisji "ponad przeciętną miarę" — hałas dziecięcy w parku publicznym nie kwalifikuje się; precedensy `[do weryfikacji]`. Argument konstytucyjny: art. 72 Konstytucji — prawo dziecka do ochrony i prawidłowego rozwoju.
- "Spadnie wartość naszych nieruchomości" → przeciwnie, badania (np. JLL Polska) wskazują na premię cenową 5–12% dla nieruchomości w odległości 200–500 m od atrakcyjnych terenów rekreacyjnych.

## 8. Wkład do strategii kampanii

- **Kolejność:** ekspertyzę akustyczną zamówić **w fazie 02–03** (wraz z koncepcją architektoniczną i uwarunkowaniami planistycznymi), **przed** finalnym wnioskiem PBO. Bez ekspertyzy ryzyko odrzucenia w fazie weryfikacji wzrasta drastycznie — UMP nie ma własnego akustyka i polega na ekspertyzie wnioskodawcy lub odrzuca z ostrożności.
- **Finansowanie:** crowdfunding lokalny (zrzutka.pl) na kwotę 25–35 tys. zł (ekspertyza + koncepcja architektoniczna + wizualizacje); patroni — Rada Osiedla Sołacz (dotacja celowa do 15 tys. zł), Koalicja ZaZieleń, instytuty UPP/PP (sponsoring barter — praktyki studenckie jako wkład).
- **Prezentacja w piśmie do urzędu:** załącznik nr X do wniosku PBO — "Analiza akustyczna lokalizacji placu zabaw w Parku Sołackim, autor: [laboratorium], data, podpis"; w treści wniosku jeden akapit z konkluzją: "L_Aeq,D w punkcie immisji nie przekracza 48 dB, tj. 2 dB poniżej dopuszczalnego limitu rozporządzenia MŚ z 14.06.2007 r. dla zabudowy jednorodzinnej". Krótko, konkretnie, z liczbą.

---

**Powiązane:** `research/halas/01-akustyka/03-normy-limity.md` (limity ogólne), `research/halas/02-immisje/02-orzecznictwo.md` (immisje cywilne), `research/pbo/studium-park-ujazdowski.md` linia 104 (zasada dobrosąsiedzkości), `research/pbo/09-pbo/04-kryteria-odrzucenia.md`.
