---
title: "Metodologia obywatelskich pomiarów akustycznych o wartości dowodowej"
type: reference
domain: halas
source: wyniki-01-akustyka-torowa.md
updated: 2026-04-17
entities: [WIOŚ, MPK-Poznań, ZDM, ZTP, GUM, PCA]
acts: [PN-ISO 1996-2, IEC 61672-1, KC-144, KC-222]
signatures: []
---

# Metodologia obywatelskich pomiarów akustycznych

Asymetria danych pomiarowych między zarządcą (MPK, ZTP, ZDM — budżet na analizy profesjonalne) a mieszkańcami (subiektywne odczucia, niemiarodajne aplikacje) jest strukturalnym problemem. Aby pomiary strony społecznej były wiarygodnym dowodem lub solidną podstawą do wymuszenia powołania biegłego sądowego z urzędu, muszą emulować rygory norm PN-ISO 1996-2 i metodyk referencyjnych Ministerstwa Klimatu i Środowiska.

## Kontekst fizyczny: kanion uliczny

Ul. Dąbrowskiego: fronty kamienic 6–8 m od osi torowiska, stosunek H/W > 1. Wielokrotne odbicia fal między równoległymi twardymi fasadami → pole akustyczne pół-rozproszone. W polu swobodnym spadek 6 dB przy podwojeniu odległości od źródła liniowego; w kanionie spadek spłyca się (efekt amplifikacji kanionowej). Równolegle zestaw kołowy ~kilkadziesiąt ton przez powierzchnię styku wielkości monety wybudza: (a) szynę → promieniowanie powietrzne, (b) podtorze i grunt → drgania parasejsmiczne re-emitowane wewnątrz budynków jako hałas strukturalny.

## Ograniczenia smartfonów

Mikrofony MEMS w telefonach są fabrycznie kalibrowane pod pasmo mowy (300–3400 Hz). DSP często implementuje filtry górnoprzepustowe (redukcja wiatru). Hałas toczenia na zdegradowanym torowisku + hałas strukturalny kumulują energię w 31,5–250 Hz. Błąd pomiarowy smartfonem w tym paśmie: **10–15 dB** — pomiary dyskwalifikowane w każdym postępowaniu formalnym.

## Wymagania sprzętowe: minimum dowodowe

Zewnętrzny kalibrowany mikrofon pojemnościowy na USB — omija wewnętrzny ADC smartfona, narzuca płaską charakterystykę 18 Hz – 20 kHz. Przykład referencyjny klasy budżetowej: **Dayton Audio UMM-6** (ok. 500 zł). Dostarczany z indywidualnym plikiem kalibracyjnym (numer seryjny). Plik wczytany do REW (Room EQ Wizard) lub równoważnego oprogramowania = krzywa korekcyjna zbliżająca dokładność do klasy 2 (w sprzyjających warunkach klasy 1) wg **IEC 61672-1**.

Status prawno-dowodowy:
- **WIOŚ / postępowanie administracyjne**: wyłącznie miernik ze świadectwem wzorcowania akredytowanego laboratorium PCA.
- **Sąd cywilny — art. 144 K.c. w zw. z art. 222 K.c. (immisje)**: poprawnie udokumentowany pomiar kalibrowanym USB = **dowód z dokumentu prywatnego**, wystarczający do uprawdopodobnienia immisji ponadnormatywnych → sąd zobowiązany powołać biegłego z urzędu. Oddalenie wniosku o biegłego wobec twardych danych prywatnych → podstawa apelacji (nierozpoznanie istoty sprawy).

## Topologia punktu pomiarowego (PN-ISO 1996-2)

| Parametr | Wymaganie klasyczne (pole swobodne) | Adaptacja dla kanionu ulicznego |
|---|---|---|
| Wysokość mikrofonu | 4,0 m ± 0,2 m nad terenem | Pomiary z okien kondygnacji. Krytyczne mapowanie 2–3 piętro (8–12 m). Wyższe piętra często mają wyższy hałas: optyczna widoczność źródła, brak ekranowania przez pojazdy, sumowanie odbić od przeciwległej fasady. |
| Dystans od fasady | Min. 3,5 m od powierzchni odbijających | 0,5–2,0 m od zamkniętego okna na wysięgniku. **Obowiązkowa korekta –3 dB** (PN-ISO 1996-2) — brak korekty to najczęstszy błąd dyskwalifikujący pomiar. |
| Kąt orientacji | Oś akustyczna na źródło | Zgodny z wektorem padania fali. Nawet mikrofony dookólne > 2 kHz mają charakterystykę kierunkową — odchylenie 90° zaniża wysokie częstotliwości (piski) o 2–5 dB. |
| Osłona | — | Obowiązkowa poliuretanowa osłona przeciwwietrzna — eliminuje pseudohałasy od naporu wiatru. |

Mocowanie: sztywny statyw. Dalmierz laserowy do dokumentacji wysokości mikrofonu względem główki szyny (p.g.s.).

## Akwizycja danych i analiza tła

Hałas tramwajowy nie jest ustalony — jest impulsowo-przemienny. Długotrwałe uśrednienia (miernik zostawiony na godziny, jedna wartość całkowita) są bezużyteczne: tło miejskie (HVAC, samochody) rozmywa emisję specyficzną z torowiska. Metodyka referencyjna wymaga izolacji pojedynczych zdarzeń i obliczenia poziomu ekspozycji $L_{AE}$.

Procedura:
1. Rejestruj **min. 20–30 izolowanych przejazdów w każdym kierunku**.
2. Loguj $L_{Aeq,T}$ (czas trwania T liczony od wyłonienia się sygnału z tła do powrotu).
3. Sumowanie energetyczne:

$$L_{Aeq,T_{ref}} = 10 \log_{10}\left(\frac{1}{T_{ref}} \sum_{k=1}^{n} 10^{0{,}1 L_{AE,k}}\right)$$

gdzie $T_{ref}$ = 57 600 s (pora dzienna 16 h) lub 28 800 s (pora nocna 8 h), a $L_{AE} = L_{Aeq,T} + 10 \log_{10}(T/T_0)$, $T_0 = 1$ s.

## Kryterium S/N

- $L_{Amax}$ przejazdu **≥ tło + 10 dB** → pomiar miarodajny.
- S/N w przedziale 3–10 dB → konieczna korekcja logarytmiczna na tło.
- S/N < 3 dB → pomiar niemiarodajny, odrzuć zdarzenie.

## Okno czasowe dla Dąbrowskiego

Ze względu na ciągły ruch kołowy najlepiej mierzyć 23:00–01:00 (zjazdy do zajezdni), okna między pojazdami samochodowymi — maksymalizuje odstęp sygnału od tła w naturalny sposób.

## Materiał audio do archiwum

Zapis surowy **WAV, nie MP3** — biegły może odzyskać analizę 1/3 oktawy nawet po latach. MP3 traci dane widmowe przez kompresję stratną.
