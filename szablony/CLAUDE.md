# szablony/ — pisma wielokrotnego użytku

Wzory pism urzędowych: wnioski, skargi, wezwania, interpelacje, odwołania. Reużywalne między kampaniami.

## Zasada: jedno źródło prawdy

Zmiana szablonu = aktualizacja **tutaj**. Kampania (`<inicjatywa>/`) kopiuje szablon, wypełnia pola `{{...}}` i zapisuje kopię jako pismo wysłane w `<inicjatywa>/<obszar>/pisma/` — nie edytuje szablonu z poziomu kampanii.

## Struktura

```
szablony/
  halas/
  uspokojenie-ruchu/
  rowery/
  transparentnosc/    # UDIP, skargi na bezczynność, odwołania
  instytucje/         # pisma o właściwość, spory kompetencyjne
```

## Format szablonu

Frontmatter YAML obowiązkowy:

```yaml
---
title: "Wniosek UDIP o udostępnienie protokołów odbioru torowiska"
type: template
domain: transparentnosc
adresat_typ: [MPK-Poznań, ZDM, UMP]
podstawa_prawna: [art. 10 UDIP, art. 61 Konstytucji]
updated: 2026-04-17
---
```

Treść:
1. Nagłówek — miejscowość, data, dane nadawcy, adresat (pełna nazwa + adres).
2. Tytuł pisma (np. „Wniosek o udostępnienie informacji publicznej").
3. Podstawa prawna — konkretne art. aktualnej wersji aktu.
4. Petitum / Wnioskuję — jasno wyodrębnione żądanie.
5. Uzasadnienie (krótkie).
6. Klauzule: forma doręczenia odpowiedzi, termin z ustawy, podpis.

Pola do wypełnienia w kampanii: `{{IMIE_NAZWISKO}}`, `{{ADRES}}`, `{{DATA}}`, `{{ADRESAT}}`, `{{SYGNATURA_SPRAWY}}`, `{{PRZEDMIOT_SPRAWY}}`, itp.

## Styl

**Pełen protokół urzędowy** — wyjątek od „gęsty styl" z root CLAUDE.md. Zachowuj zwroty grzecznościowe i formalne („Szanowni Państwo", „Z wyrazami szacunku") — mają wartość procesową w KPA i są oczekiwane przez urzędy.

## Użycie w kampanii

1. `cp szablony/<obszar>/<nazwa>.md <inicjatywa>/<obszar>/pisma/YYYY-MM-DD_ADRESAT_temat.md`
2. Wypełnij pola `{{...}}`.
3. Zmień frontmatter: `type: template` → `type: sent`, dodaj `wyslano: YYYY-MM-DD`, `adresat: <pełna nazwa>`, `termin_odpowiedzi: YYYY-MM-DD`.
4. Wpis w `<inicjatywa>/<obszar>/REJESTR.md`.

## Nie

- Nie kopiuj całego szablonu do kampanii bez zmian — zawsze wypełnij pola.
- Nie usuwaj frontmatter po wypełnieniu — jest potrzebny do Grep-retrieval.
- Nie zmyślaj podstawy prawnej — jeśli szablon nie pasuje idealnie, zmodyfikuj `podstawa_prawna:` świadomie.
