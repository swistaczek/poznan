---
title: "halas / 01 — akustyka torowa i pomiary"
type: index
domain: halas
source: wyniki-01-akustyka-torowa.md
updated: 2026-04-17
---

# halas / 01 — akustyka torowa

**TL;DR.** Hałas tramwajowy na Dąbrowskiego (kanion uliczny 6–8 m fasada–tor) to złożenie czterech zjawisk: corrugation (250–1000 Hz), wheel flats (impulsowo szerokopasmowe), curve squeal (6,3–15,8 kHz), hałas strukturalny (16–80 Hz). Polskie prawo tej samej nocy zezwala na 59 dB $L_{Aeq,N}$ dla strefy śródmiejskiej (WHO: 44 dB) — rozbieżność 15 dB, ~30× energii. Stan obecny 64–69 dB = rażące przekroczenie. Technicznie do 48–52 dB schodzi się pakietem **maty USM + ERS + smarownice** (Warszawa W-Z, Kraków Karmelicka zrobiły to). Broń obywatelska: pomiar kalibrowanym USB (Dayton UMM-6) jako dokument prywatny → sąd cywilny art. 144 K.c., plus WIOŚ, plus 12 pytań UDIP wymuszających diagnostykę MBM zarządcy.

## Chunki merytoryczne

- [01-metodologia-pomiarow](01-metodologia-pomiarow.md) — sprzęt (Dayton UMM-6, kalibratory), topologia punktu, korekta fasadowa −3 dB, $L_{AE}$, kryterium S/N ≥ 10 dB.
- [02-sygnatury-widmowe](02-sygnatury-widmowe.md) — corrugation, wheel flats, curve squeal, hałas styków, rumble strukturalny — katalog widmowy + winny (zarządca vs eksploatator).
- [03-normy-limity](03-normy-limity.md) — limity PL (55/59/65/68 dB) vs WHO (44/54 dB), symulacja CNOSSOS-EU dla Dąbrowskiego, klasyfikacja MPZP jako zmienna kluczowa.
- [04-interwencje-techniczne](04-interwencje-techniczne.md) — szlifowanie, smarownice, tłumiki, maty USM, FST, ERS, tokarnia — koszty, żywotność, skuteczność, rekomendacja pakietu dla Dąbrowskiego.
- [05-precedensy-polskie](05-precedensy-polskie.md) — Warszawa W-Z, Kraków Karmelicka, Wrocław Grabiszyńska: co wdrożono, jakie redukcje dB, finansowanie POIiŚ+NFOŚiGW.
- [06-audyt-mbm](06-audyt-mbm.md) — MBM, Id-1/Id-115, drezyna, CAT, UT, GPR, Wskaźnik J — co zarządca musi mieć udokumentowane.
- [07-udip-zapytania](07-udip-zapytania.md) — 12 pytań UDIP operacjonalizujących audyt MBM.
- [99-faq](99-faq.md) — 15 pytań mieszkańca-aktywisty z cross-refami do chunków merytorycznych.

## Najczęstsze pytania (z FAQ)

- **Czy smartfon wystarczy jako dowód?** → [99-faq #1](99-faq.md) + [01-metodologia-pomiarow](01-metodologia-pomiarow.md).
- **Jak odróżnić corrugation od wheel flats na słuch?** → [99-faq #2](99-faq.md) + [02-sygnatury-widmowe](02-sygnatury-widmowe.md).
- **Co robić z odpowiedzią „zgodnie z normą"?** → [99-faq #4](99-faq.md) + [03-normy-limity](03-normy-limity.md).
- **Jaką technologię forsować w petycji?** → [99-faq #6](99-faq.md) + [04-interwencje-techniczne](04-interwencje-techniczne.md) + [05-precedensy-polskie](05-precedensy-polskie.md).
- **Czy pozywać — jaką ścieżkę?** → [99-faq #11](99-faq.md) (WIOŚ / cywilna / zdrowotna / polityczna).
- **Co napisać w pierwszym piśmie do MPK?** → [99-faq #14](99-faq.md) + szablony poniżej.
- **Czy czekać na remont z WPF?** → [99-faq #15](99-faq.md) (nie — kryterium akustyczne w SIWZ, patrz [07-udip #12](07-udip-zapytania.md)).

## Szablony pism

- [`../../../szablony/halas/wniosek-udip-audyt-torowiska.md`](../../../szablony/halas/wniosek-udip-audyt-torowiska.md) — wniosek UDIP z 12 pytaniami do MPK / ZTM / PIM. Użyć gdy: potrzebne twarde dane diagnostyczne (CAT, UT, wskaźnik J, historia szlifowania, budżety).
- [`../../../szablony/halas/wezwanie-do-mpk-diagnoza-akustyczna.md`](../../../szablony/halas/wezwanie-do-mpk-diagnoza-akustyczna.md) — pierwsze pismo „niezbywalne" z wynikami pomiaru + żądaniem interwencji. Użyć gdy: macie własne pomiary kalibrowanym sprzętem i chcecie otworzyć formalną ścieżkę ze śladem do WSA.
- [`../../../szablony/halas/skarga-wios-pomiar-kontrolny.md`](../../../szablony/halas/skarga-wios-pomiar-kontrolny.md) — skarga do WIOŚ z wnioskiem o kontrolę i pomiar referencyjny (art. 115a POŚ). Użyć gdy: MPK nie reaguje lub chcecie niezależnej ścieżki administracyjnej równolegle z cywilną.

## Pełne źródło

[`../wyniki-01-akustyka-torowa.md`](../wyniki-01-akustyka-torowa.md) — monolityczny raport researchu z promptu `research/prompty/01-akustyka-torowa.md`, pełna narracja + FAQ. Zachowany dla referencji. Do pracy operacyjnej używaj chunków.
