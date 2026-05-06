# research/instytucje/stenogramy-rm/ — konwencje lokalne

Baza dokumentów Rady Miasta Poznania: sesje plenarne + komisje stałe. Aktualizowana skill-em `.claude/skills/aktualizuj-stenogramy-rm.md`.

## Doprecyzowanie terminologiczne

Nazwa katalogu zawiera „stenogramy" (potoczna), ale BIP Poznania **nie publikuje stenogramów verbatim**. Publikuje **protokoły** (zatwierdzane skróty merytoryczne). Pełen zapis dyskusji = własna transkrypcja Whisper z archiwum audio (`bip.poznan.pl/bip/archiwum-audio/`) lub UDIP do Biura Rady Miasta (`bor@um.poznan.pl`). Skill v1 zbiera tylko protokoły.

## Co tu jest

- `sesje-plenarne/` — sesje plenarne RM, podzielone per kadencja (IX, VIII, VI). Per sesja: stub markdown z metadanymi i linkami.
- `komisje/` — protokoły 15 komisji stałych kadencji IX. Per komisja: katalog z indeksem i protokołami.
- `changelog.md` — historia runów skill-a (timestamp + lista zmian).
- `index.md` — punkt wejścia do bazy.

## Czego TU NIE MA i NIE BĘDZIE

- **Plików binarnych (PDF, DOCX, MP3, MP4)** — rozmiar, prawa autorskie, niestabilność URL. Linki tylko do oryginału w BIP.
- **Verbatim protokołów** — chronione prawem autorskim BIP. W stubach: synteza własna 5–15 zdań + linki.

## Wzorce nazewnictwa

- Sesja plenarna: `sesja-{numer-rzymski}-{YYYY-MM-DD}.md` (np. `sesja-XXXIV-2026-05-12.md`).
- Komisja — slug katalogu: krótka, zwięzła nazwa kebab-case (np. `rewizyjna`, `budzet-finanse-nadzor-wlascicielski`, `polityki-przestrzennej`, `gkios` dla Gospodarki Komunalnej i Ochrony Środowiska).
- Protokół komisji: `protokol-{YYYY-MM-DD}.md`.
- Sygnatury uchwał (w treści): `XXXIV/123/2026` (sesja / numer / rok).

## Krytyczne reguły

1. **Nie nadpisuj istniejącego pliku** bez sprawdzenia `changelogs` w API JSON. Aktualizacja protokołu (radni nanoszą poprawki) = dopisz sekcję adnotacji, nie zastępuj treści.
2. **Crawl-delay 5 s** między requestami do `bip.poznan.pl` (`robots.txt`).
3. **User-Agent**: `Claude Code (skill: aktualizuj-stenogramy-rm; baza obywatelska Poznania)`.
4. **Każdy URL z BIP** musi mieć w stubie notę „pobrano YYYY-MM-DD" — bo treść BIP znika po kadencjach.
5. **Crosslinkuj** z resztą bazy: portretami radnych, werdyktami teorii, plikami inwestycyjnymi (Mosty, Stary Rynek, tramwaj Naramowice).

## Aktualizacja bazy

Użyj skill-a (jeśli środowisko wspiera Claude Code Skills): `/aktualizuj-stenogramy-rm`. Skill respektuje konwencje, deleguje do paralel sub-agentów Sonnet, generuje changelog.

W razie ręcznego dodania dokumentu: utrzymaj format, dopisz wpis do `changelog.md` z notą „ręcznie dodane".

## Powiązania

- `../12-rada-miasta-radni/` — struktura RM, frakcje
- `../radni/` — karty per radny
- `../pim-siec-powiazan-kominy-placowe.md` — chronologia KR 2024–2026
- `../prezes-pim-litka-werdykt-zbiorczy.md` — teorie T1–T9
- `../nowe-teorie-2026-05-06.md` — teorie T10–T14
- `../../../INDEKS.md` — punkt wejścia do całego repo
