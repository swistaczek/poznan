---
name: aktualizuj-stenogramy-rm
description: Use when the user asks to update or refresh the local base of Rada Miasta Poznania session/committee minutes. Fetches new protokoły (PDF/DOCX) from BIP Poznania, updates per-session/per-committee markdown stubs in research/instytucje/stenogramy-rm/, regenerates indexes, appends a changelog entry. Idempotent — safe to re-run.
---

# Aktualizuj stenogramy RM Poznania

> **Doprecyzowanie terminologiczne:** BIP Poznania nie publikuje **stenogramów verbatim**. Publikuje **protokoły** (skróty merytoryczne, zatwierdzane przez radnych) + **PDF głosowań** + **DOCX uchwał**. Pełen zapis dyskusji = własny Whisper na archiwum audio (`bip.poznan.pl/bip/archiwum-audio/`) lub UDIP do BoR (`bor@um.poznan.pl`). Skill v1 zbiera tylko protokoły. Audio/wideo/transkrypcje Whisper to iteracja 2.

## Cel

Utrzymywać aktualną, lokalną bazę dokumentów Rady Miasta Poznania — sesji plenarnych i komisji stałych — w `research/instytucje/stenogramy-rm/`, w formie markdownowych metadanych z linkami do oryginalnych plików w BIP. Plików binarnych (PDF/DOCX) nie commitujemy do repo (rozmiar, stabilność URL); commitujemy tylko stuby markdown.

## Źródła i wzorce URL

**Sesje plenarne:**
- Strona główna RM: `https://bip.poznan.pl/bip/rada-miasta-poznania/`
- Listing aktualnej kadencji IX (2024–2029): `https://bip.poznan.pl/bip/sesje/`
- Archiwum kadencji: `https://bip.poznan.pl/bip/sesje/archiwum/`
- Per kadencja (przykład VI): `https://bip.poznan.pl/bip/sesje/kadencja-2010-2014,8/`
- Per sesja: `https://bip.poznan.pl/bip/sesje/{slug},{id}/` (np. `lxii,50179` = sesja LXII z 28.01.2014)
- API JSON per sesja: `https://bip.poznan.pl/api-json/bip/sesje/{slug},{id}/` (pola: `sesje, zalaczniki, sesja_program, sesja_protokol, changelogs`)
- Harmonogram bieżący: `https://bip.poznan.pl/bip/ramowy-harmonogram-sesji,doc,1616/`

**Komisje stałe (15, kadencja IX):**
- Listing per komisja: `https://bip.poznan.pl/bip/komisje/{slug},{id-1500-1534}/`
- Protokoły komisji: zwykle DOCX, wzorzec attachments: `https://bip.poznan.pl/public/bip/attachments.att?co=show&instance=1167&id={num_id}&lang=pl`
- Listing posiedzeń wszystkich komisji: `https://bip.poznan.pl/bip/posiedzenia/`

**Audio (od 2014):**
- BIP archiwum audio: `https://bip.poznan.pl/bip/archiwum-audio/`
- Otwarte Dane: `https://dane.gov.pl/pl/dataset/259,archiwum-audio-sesji-rady-miasta-poznania/resource/1217`

**Wideo (kadencja IX):**
- Transmisja na żywo: `https://bip.poznan.pl/bip/transmisja-na-zywo/`
- video.poznan.pl: `https://video.poznan.pl/video-tag/sesja-rady-miasta-poznania/` (niestabilny)
- esesja.tv kanał 230: `https://esesja.tv/transmisje_z_obrad/230/rada-miasta-poznania.htm` (do ~01.2022)

**Etyka technicznego dostępu:**
- `robots.txt` BIP wymaga Crawl-delay 5 s. **Każdy WebFetch musi mieć ≥5 s odstępu**. Bash z `sleep 5` między requestami.
- Nie używaj user-agentów udających przeglądarkę. `User-Agent: Claude Code (skill: aktualizuj-stenogramy-rm; baza obywatelska Poznania)` to standard.
- Boty AhrefsBot/SemrushBot/Yandex są zbanowane — nie symulujemy.

## Struktura repo (target)

```
research/instytucje/stenogramy-rm/
  index.md                              # nawigacja po bazie
  changelog.md                          # historia runów skill-a
  CLAUDE.md                             # konwencje lokalne
  sesje-plenarne/
    index.md                            # tabela master wszystkich kadencji
    kadencja-IX-2024-2029/
      sesja-XXXIV-2026-05-12.md         # metadane + linki + lista uchwał + status
      sesja-XXXIII-2026-04-22.md
      ...
    kadencja-VIII-2018-2024/
      ...
    kadencja-VI-2010-2014/
      sesja-LXII-2014-01-28.md          # historyczna (PIM)
  komisje/
    index.md                            # lista 15 komisji + statystyka
    rewizyjna/
      index.md
      protokol-2026-03-05.md
      protokol-2026-04-16.md
      ...
    budzet-finanse-nadzor-wlascicielski/
      ...
```

## Format pliku per-sesja (`sesja-{numer-rzymski}-{YYYY-MM-DD}.md`)

```yaml
---
typ: sesja-plenarna
numer_rzymski: XXXIV
numer_arabski: 34
kadencja: IX
data: 2026-05-12
godzina_rozpoczecia: "09:00"
url_bip: https://bip.poznan.pl/bip/sesje/xxxiv,98779/
url_api: https://bip.poznan.pl/api-json/bip/sesje/xxxiv,98779/
status_protokolu: opublikowany | brak | oczekiwany
data_pobrania: 2026-05-06
liczba_punktow_porzadku: 34
liczba_uchwal: 28
---

# Sesja XXXIV Rady Miasta Poznania — 12 maja 2026

## Metadane

- **Numer**: XXXIV (rzymski) / 34 (arabski)
- **Kadencja**: IX (2024–2029)
- **Data**: wtorek, 12 maja 2026, 09:00
- **Miejsce**: [z BIP — typowo sala sesyjna UMP, pl. Kolegiacki 17]
- **Przewodniczący sesji**: [z protokołu]

## Pliki źródłowe (linki do BIP, nie kopie)

- **Protokół**: [PDF — id={num}](https://bip.poznan.pl/public/bip/attachments.att?co=show&instance=1167&id={num}&lang=pl) ({rozmiar}, pobrano {data})
- **Porządek obrad**: [link]
- **Lista uchwał (28)**: zob. sekcja niżej
- **PDF głosowań** (per uchwała): [linki]
- **Audio**: [link do archiwum audio jeśli dostępne] / brak
- **Wideo**: [link transmisji jeśli zarchiwizowana] / brak

## Porządek obrad (skrót)

1. ...
2. ...

## Uchwały

| Numer | Tytuł | Wynik głosowania | URL |
|---|---|---|---|
| XXXIV/{nr}/{rok} | ... | przyjęta / odrzucona / wycofana | ... |

## Notatki

[Najważniejsze decyzje, kontrowersje, sprzeczne głosowania, sygnaturowe wystąpienia. Krótka synteza, nie verbatim.]

## Powiązania

- [Inne sesje dot. tego samego tematu]
- [Werdykty teorii śledczych jeśli powiązane, np. T1, T7]
- [Pisma w repo które odnoszą się do tej sesji]
```

## Format pliku per-protokół-komisji (`protokol-{YYYY-MM-DD}.md`)

```yaml
---
typ: protokol-komisji
komisja: rewizyjna
przewodniczacy: Zbigniew Czerwiński
data: 2026-04-16
godzina_rozpoczecia: "10:00"
miejsce: sala 1, UMP pl. Kolegiacki 17
url_bip: https://bip.poznan.pl/bip/komisje/{slug},{id}/{posiedzenie}/
url_protokolu_docx: https://bip.poznan.pl/public/bip/attachments.att?co=show&instance=1167&id={num}&lang=pl
status: opublikowany
data_pobrania: 2026-05-06
liczba_punktow_porzadku: 8
---

# Protokół Komisji Rewizyjnej RM Poznania — 16 kwietnia 2026

## Metadane

- **Komisja**: Rewizyjna
- **Przewodniczący**: Zbigniew Czerwiński (PiS)
- **Skład**: 6 członków [imiona z BIP]
- **Data**: czwartek, 16 kwietnia 2026, 10:00
- **Miejsce**: sala 1, UMP pl. Kolegiacki 17
- **Liczba punktów porządku**: 8

## Plik źródłowy

[DOCX — id={num}](URL) ({rozmiar}, pobrano {data})

## Porządek obrad

1. ...

## Najważniejsze ustalenia

[Synteza 5–15 zdań — kluczowe decyzje, opinie, wnioski, głosowania komisyjne. Cytaty tylko z protokołu (nie verbatim z dyskusji — protokół jest skrótem).]

## Powiązania

- [Sesja plenarna na której temat trafił]
- [Wcześniejsze posiedzenia tej samej komisji w tej sprawie]
- [Werdykty teorii śledczych]
```

## Procedura skill-a (algorytm)

### Faza 1: stan obecny

1. Przeczytaj `research/instytucje/stenogramy-rm/changelog.md` — znajdź timestamp ostatniego runu.
2. Przeczytaj `research/instytucje/stenogramy-rm/sesje-plenarne/index.md` — najwyższy numer sesji w kadencji IX.
3. Przeczytaj `research/instytucje/stenogramy-rm/komisje/index.md` — ostatnie daty per komisja.

### Faza 2: detekcja nowych

1. WebFetch `https://bip.poznan.pl/bip/sesje/` — wyparsuj listę sesji kadencji IX (numer, data, slug, id).
2. Porównaj z lokalnym indeksem — odfiltruj te które już są.
3. Dla nowych: pobierz `/api-json/bip/sesje/{slug},{id}/` (z `sleep 5` między).
4. Analogicznie dla każdej z 15 komisji: WebFetch strony komisji, wyparsuj listę posiedzeń, odfiltruj nowe.

### Faza 3: zapis stubów

1. Dla każdej nowej sesji/posiedzenia stwórz plik markdown w odpowiednim katalogu.
2. **Nigdy nie nadpisuj** istniejącego pliku bez sprawdzenia changelog (w razie aktualizacji protokołu — dopisz adnotację, nie nadpisuj treści notatek).
3. Aktualizuj indexy (`sesje-plenarne/index.md`, `komisje/index.md`).

### Faza 4: changelog

Dopisz wpis na końcu `changelog.md`:

```markdown
## Run YYYY-MM-DDTHH:MM:SS+02:00

- **Sesje plenarne (kadencja IX)**: dodano {N} — {lista numerów}
- **Komisje**:
  - Rewizyjna: dodano {N} protokołów ({daty})
  - Budżet/Finanse/Nadzór Właścicielski: ...
  - ...
- **Łącznie nowych dokumentów**: {N}
- **Czas runu**: {duration}
- **Błędy/luki**: {opis ew. brakujących PDF / 404}

```

### Faza 5: raport końcowy

Zwróć użytkownikowi (max 250 słów):
- Liczba dodanych dokumentów per typ.
- Najnowsza sesja w bazie.
- Wykryte ostrzeżenia (404, brak protokołu mimo daty po sesji, zmiany w protokole — bo `changelogs` w API może wskazywać redaktę).
- Sugestie dalszych kwerend (UDIP w razie luk).

## Tryb pracy z sub-agentami

Pełny run w pojedynczej sesji może być długi (15 komisji × ~5 ostatnich posiedzeń + sesje plenarne) — łatwo eksplodować kontekst. **Standard**: skill **deleguje** poszczególne komisje do paralel sub-agentów Sonnet (tańsze, wystarczają do scrape + zapisu stubów). Główna sesja syntetyzuje raport.

Schemat delegacji:
- Sub-agent A: sesje plenarne kadencji IX (pełna lista + nowe stuby)
- Sub-agent B: 5 komisji „twardych" (Rewizyjna, Budżet+Finanse+Nadzór, Polityki Przestrzennej, GKiOŚ, Skarg/Wniosków/Petycji)
- Sub-agent C: 5 komisji „miękkich" (Oświaty, Kultury+Nauki, Kultury Fizycznej, Zdrowia/Polityki Społecznej, Bezpieczeństwa)
- Sub-agent D: 5 komisji „pozostałych" (Polityki Mieszkaniowej, Transportu, Rewitalizacji, Promocji+Rozwoju, Samorządowa)

Każdy sub-agent dostaje target ścieżki katalogu, listę URL-i, instrukcję respektowania Crawl-delay 5s.

## Szczególne uwagi

1. **Słownik osób** w protokołach (radni, urzędnicy) — gdy nazwisko pojawia się w tekście, oznacz `[osoba: Nazwisko, Imię, klub/funkcja]` w sekcji notatek dla późniejszego retrieval. Zlinkuj z `research/instytucje/radni/{slug}.md` jeśli istnieje.

2. **Wzmianki o inwestycjach** — gdy protokół dotyczy PIM/Aquanet/MTP/ZKZL/MPK lub konkretnych inwestycji (Mosty Berdychowskie, Stary Rynek, tramwaj Naramowice), zlinkuj z odpowiednim plikiem w `research/instytucje/`.

3. **Wzmianki o teoriach śledczych** — gdy protokół dotyczy spraw poznawczo śledczo-relewantnych (kominy płacowe, B2B, Hipodrom Wola, art. 10c u.g.k.), zlinkuj z teoriami T1–T14 w `research/instytucje/`.

4. **Sygnatura uchwał** — format `XXXIV/123/2026` (sesja XXXIV / numer uchwały / rok). Stabilna konwencja BIP.

5. **Brak protokołu po sesji** — typowo 2–4 tygodnie. Tworzymy stub z `status_protokolu: oczekiwany` i odznacz w changelog. Skill na każdym kolejnym runie sprawdza czy się pojawił.

6. **Aktualizacje protokołów** (kiedy radni nanoszą poprawki w trybie autoryzacji) — `changelogs` w API JSON pokaże modyfikacje. Wtedy: dopisz adnotację „protokół zmodyfikowany {data}, sprawdzić diff" w stubie + changelog wpis.

## Definition of Done dla pojedynczego runu

- [ ] Przeczytany lokalny stan (changelog + indexy).
- [ ] Pobrana świeża lista sesji plenarnych kadencji IX z BIP.
- [ ] Pobrane listy posiedzeń wszystkich 15 komisji.
- [ ] Stworzone stuby dla nowych dokumentów (z respektem Crawl-delay 5s).
- [ ] Zaktualizowane indeksy (`sesje-plenarne/index.md`, `komisje/index.md`).
- [ ] Dopisany wpis w `changelog.md` z timestamp i szczegółami zmian.
- [ ] Raport końcowy do użytkownika (max 250 słów) z liczbami i ostrzeżeniami.
- [ ] **NIE** zapisywać binarek (PDF/DOCX) do repo — tylko markdownowe stuby z linkami.
- [ ] **NIE** nadpisywać istniejących plików bez świadomej decyzji (sprawdź changelogs).

## Czego NIE robić

- Nie pobieraj samych PDF-ów / DOCX-ów do repo (rozmiar, prawa autorskie, niestabilność URL).
- Nie symuluj user-agenta przeglądarki ani znanego bota.
- Nie ignoruj Crawl-delay 5s (BIP może odpowiedzieć 429 i zablokować IP).
- Nie nadpisuj stuba protokołu, gdy istnieje — dopisuj sekcje aktualizacji.
- Nie przesypuj treści protokołu (verbatim) do markdownu — bo to chronione prawem autorskim. Tylko **synteza własna 5–15 zdań** + linki do oryginału.
- Nie cituj radnych z dyskusji bez własnej weryfikacji w wideo/audio (protokoły są skrótami i czasem mylą wypowiedzi).
- Nie omijaj kroku changelog — to jedyny audytowalny ślad runu.

## Powiązania w repo

- `research/instytucje/12-rada-miasta-radni/` — struktura RM, frakcje
- `research/instytucje/13-radni-dialog/` — metodologia dialogu z radnymi
- `research/instytucje/radni/` — karty per osoba
- `research/instytucje/pim-siec-powiazan-kominy-placowe.md` — chronologia kontroli KR 2024–2026
- `research/instytucje/prezes-pim-litka-werdykt-zbiorczy.md` — teorie T1–T9 (kominy, PIM)
- `research/instytucje/nowe-teorie-2026-05-06.md` — teorie T10–T14 (B2B, Hipodrom Wola, art. 10c, KPI premii)
- `research/instytucje/audyt-crosslink-2026-05-06.md` — wzorzec crosslinkowania nowych dokumentów
