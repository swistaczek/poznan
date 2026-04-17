---
title: "halas / 04 — monitoring torowisk MPK i okna interwencyjne"
type: index
domain: halas
source: wyniki-17-monitoring-torowisk-mpk.md
updated: 2026-04-17
---

# halas / 04 — monitoring remontów torowisk MPK Poznań

> Źródło: [`../wyniki-17-monitoring-torowisk-mpk.md`](../wyniki-17-monitoring-torowisk-mpk.md) | Prompt: [`../../prompty/17-monitoring-torowisk-mpk.md`](../../prompty/17-monitoring-torowisk-mpk.md)

## TL;DR

Skuteczność interwencji społecznej w procesie modernizacji torowiska maleje wykładniczo od fazy programowania budżetu do odbioru robót. Okna krytyczne: **WPF wrzesień–listopad** (kosztorys inwestorski PIM/ZDM), **wyłożenie MPZP 21 dni**, **postępowanie DUŚ w RDOŚ Poznań** (art. 31 KPA), **termin pytań do SWZ** (ostatnia realna szansa na BAT). Po podpisaniu umowy z wykonawcą — tylko art. 115a POŚ (WIOŚ, pomiar kontrolny → decyzja nakazująca, kary art. 362 POŚ). Architektura: PIM/ZDM = przebudowy, MPK Sp. z o.o. = utrzymanie i remonty odtworzeniowe (kancelaria@mpk.poznan.pl), ZTM = koordynacja. PHNUA Wielkopolska: uchwała Sejmiku **nr IV/92/24 z lipca 2024** (Marszałek Województwa, art. 119–120 POŚ). SMH Poznania 2022. Dla ul. Dąbrowskiego: pomiar ZDM 2016 L_AeqN = 62,2 dB (Dąbrowskiego/Roosevelta) → twardy dowód przekroczeń.

## Tabela okien decyzyjnych (skrócona)

| Faza | Kiedy | Co robić | Szablon / instrument |
|---|---|---|---|
| PHNUA — konsultacje | cykl 5-letni, UMWW BIP | uwagi do harmonogramu, priorytetyzacja ulicy | uwagi do projektu uchwały Sejmiku |
| WPF — budżet Miasta | wrz–lis (uchwała grudniowa) | analiza Zał. nr 2 (wykaz przedsięwzięć), lobbing u radnych Komisji Transportu RM | pismo interwencyjne / projekt interpelacji |
| Plan remontów MPK | sty–lut (publikacja zarysu IV) | UDIP do MPK o harmonogram + technologie | [wniosek-udip-audyt-torowiska](../../../szablony/halas/wniosek-udip-audyt-torowiska.md) [do stworzenia] |
| MPZP — wyłożenie | 21 dni od ogłoszenia | uwagi strukturalne (obowiązkowa wibroizolacja BAT w §) | uwagi do wyłożonego MPZP |
| LICP | obwieszczenia w BIP | przez właścicieli kamienic (strona z interesem prawnym) | wniosek dowodowy stron |
| DUŚ — RDOŚ Poznań | od wszczęcia, obwieszczenia | stowarzyszenie na prawach strony (art. 31 KPA), wymuszenie OOŚ + monitoring porealizacyjny | wniosek o OOŚ |
| OPZ / projekt techniczny | przed ogłoszeniem przetargu | UDIP o wstępną dokumentację projektową | wniosek UDIP |
| SWZ — termin pytań | kilkanaście dni od publikacji BZP/TED | transfer analiz akustycznych do firm branżowych → oficjalne pytania | formalne zapytanie do SWZ |
| Eksploatacja — odbiór | wznowienie ruchu po remoncie | pomiar kontrolny, skarga WIOŚ art. 115a POŚ | [skarga-wios-pomiar-kontrolny](../../../szablony/halas/skarga-wios-pomiar-kontrolny.md) |

## Architektura kompetencji

| Podmiot | Co robi | Kontakt / podstawa |
|---|---|---|
| PIM (Poznańskie Inwestycje Miejskie) | generalne przebudowy, nowe trasy tramwajowe | [do weryfikacji] |
| ZDM (Zarząd Dróg Miejskich) | zarząd pasa drogowego, odbiory, pomiary (2016 L_AeqN 62,2 dB Dąbrowskiego/Roosevelta) | [do weryfikacji] |
| MPK Poznań Sp. z o.o. | utrzymanie, remonty odtworzeniowe, szlifowanie, wymiana wkładek | kancelaria@mpk.poznan.pl |
| ZTM Poznań | koordynacja przewozów, harmonogramy z MPK | [do weryfikacji] |
| WIOŚ Poznań | pomiary kontrolne art. 115a POŚ, wnioskowanie kar | [do weryfikacji] |
| RDOŚ Poznań | DUŚ, OOŚ, KIP dla inwestycji tramwajowych | [do weryfikacji] |
| UMWW — Marszałek Województwa | PHNUA (uchwała IV/92/24), mapy dla województwa | BIP UMWW |
| Prezydent Miasta Poznania | SMH aglomeracji (art. 118 POŚ, cykl 5-letni, ostatnia 2022), funkcje starosty | BIP UMP |
| Sejmik Woj. Wielkopolskiego | uchwala PHNUA (IV/92/24 z VII.2024) | BIP UMWW |
| Rada Miasta Poznania | WPF, Komisja Transportu i Polityki Mieszkaniowej | [research/instytucje/12-rada-miasta-radni/](../../instytucje/12-rada-miasta-radni/) |

## Nawigacja chunków

- [01-cykl-remontowy](01-cykl-remontowy.md) — WPF, plan MPK, PZP, BZP/TED, CPV, tryb z wolnej ręki, regulamin wewnętrzny MPK
- [02-phnua-mapa-halasu](02-phnua-mapa-halasu.md) — SMH 2022 (L_DWN/L_N), PHNUA IV/92/24, wskaźnik M, NHA/NHSD, ścieżka UDIP do UMWW
- [03-mpzp-licp](03-mpzp-licp.md) — MPZP (wyłożenie 21 dni), LICP (ograniczona partycypacja), DUŚ (art. 31 KPA, KIP, OOŚ)
- [04-wymagania-techniczne](04-wymagania-techniczne.md) — corrugation, f=v/λ 400–1000 Hz, szlifowanie, UBM/USP, wkładki, C_dyn, smarownice, art. 115a POŚ, art. 362 POŚ
- [05-udip-przetargi](05-udip-przetargi.md) — TED/BZP (CPV 45234121-0 i in.), Logintrade, eB2B, UDIP do MPK i UMWW, SKO → WSA
- [99-faq](99-faq.md) — 7 pytań aktywisty (cezury, pretekst WPF, zejście pod normę, wymiana szyn)

## Kluczowe akty prawne

- **POŚ** (Prawo ochrony środowiska): art. 113 (poziomy dopuszczalne), art. 115a (pomiar kontrolny → decyzja nakazująca), art. 118 (SMH co 5 lat), art. 119–120 (PHNUA), art. 362 (decyzja o ograniczeniu emisji), art. 315a nn. (kary pieniężne)
- **KPA**: art. 31 (stowarzyszenie na prawach strony), art. 35/237 (terminy)
- **PZP**: art. 214 ust. 1 pkt 5 (tryb z wolnej ręki — wyjątkowa sytuacja), art. 454–455 (modyfikacja umów)
- **UDIP**: art. 13 (termin 14 dni), art. 16 (decyzja odmowna), art. 23 (sankcje karne)
- **Konstytucja RP**: art. 61 (prawo do informacji publicznej)
- **Ustawa o planowaniu i zagospodarowaniu przestrzennym**: wyłożenie MPZP, procedura LICP
- **Dyrektywa 2002/49/WE** — tzw. dyrektywa hałasowa
- **Rozporządzenie ws. przedsięwzięć mogących znacząco oddziaływać na środowisko** — kwalifikacja torowisk do DUŚ
- **PHNUA Wielkopolska** — uchwała Sejmiku **nr IV/92/24 z lipca 2024** (akt prawa miejscowego)
- **SMH Poznania 2022** — ostatnia wielka aktualizacja map (Prezydent jako zarządca aglomeracji >100 tys.)
- **WPF Poznania** — uchwały nowelizacyjne 2024: III/38/IX/2024 (11.06), VIII/115/IX/2024 (24.09), XII/207/IX/2024 (3.12)
- **Regulamin udzielania zamówień MPK Poznań nieobjętych PZP** (ujednolicony 2022) — §1 ust. 2 klauzula odstąpienia

## Szablony pism

- [`../../../szablony/halas/wniosek-udip-audyt-torowiska.md`](../../../szablony/halas/wniosek-udip-audyt-torowiska.md) — żądanie Paszportu Toru, dzienników oględzin, rejestru umów, protokołów odbiorów (do MPK, kancelaria@mpk.poznan.pl, 14 dni)
- [`../../../szablony/halas/skarga-wios-pomiar-kontrolny.md`](../../../szablony/halas/skarga-wios-pomiar-kontrolny.md) — art. 115a POŚ, pomiar kontrolny, wniosek o decyzję nakazującą
- UDIP do UMWW o załączniki tabelaryczne PHNUA z wykazem ulic dla Poznania [do stworzenia]
- uwagi do wyłożonego MPZP z obligatoryjną izolacją wibroakustyczną [do stworzenia]
- wniosek o status strony (stowarzyszenie) w postępowaniu DUŚ [do stworzenia]

## Powiązania

- Pomiary: [`../wyniki-zdm-pomiary-halas-2016.md`](../wyniki-zdm-pomiary-halas-2016.md) — 37 punktów tramwajowych
- Akustyka: [`../01-akustyka/04-interwencje-techniczne.md`](../01-akustyka/04-interwencje-techniczne.md), [`../01-akustyka/06-audyt-mbm.md`](../01-akustyka/06-audyt-mbm.md)
- Immisje cywilne: [`../02-immisje/index.md`](../02-immisje/index.md)
- Kompetencje: [`../../instytucje/07-kompetencje/`](../../instytucje/07-kompetencje/)
- Radni: [`../../instytucje/12-rada-miasta-radni/`](../../instytucje/12-rada-miasta-radni/)
