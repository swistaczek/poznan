---
title: "Lista zakupów - kolektor hałasu LoRa"
type: project
domain: halas
updated: 2026-09-18
---

# Lista zakupów

Zobacz [`PLAN.md`](PLAN.md) dla uzasadnienia każdego wyboru. Czujnik hałasu RS485 już kupiony (nie w tej liście).

## Wariant rekomendowany (praca całoroczna 24/7, mniej kompromisów)

| # | Element | Produkt | Cena | Link |
|---|---|---|---|---|
| 1 | Węzeł LoRa | WisBlock Meshtastic Starter Kit 868MHz (RAK19007+RAK4631+antena) | 159,00 zł | Botland SOC-19318 |
| 2 | Moduł RS485 | RAK5802 RS485 Interface | ~30-40 zł | kiloelectronics.com lub store.rakwireless.com |
| 3 | Bramka LoRaWAN | SenseCAP M2 Multi-Platform SX1302 EU868 | 489,00 zł | Botland 22110 |
| 4 | Panel solarny | Panel mono 30W 12V Maxx, 470×390×25mm | 149,00 zł | centrumzasilania.pl |
| 5 | Regulator ładowania | Victron SmartSolar MPPT 75/10 (profil LiFePO4) | 210,00 zł | energomag.pl |
| 6 | Akumulator | Green Cell CUBE LiFePO4 12,8V 20Ah (256Wh), LFPGC12V20AH | 339,95 zł | greencell.global |
| 7 | Przetwornica 12V→5V | Traco TSR 1-2450 | ~40,00 zł | Kamami/TME |
| 8 | Obudowa | ETI GT 30-20-15, IP65, 300×200×150mm | 249,68 zł | elektrycznie.pl |
| 9 | Antena LoRa | Antena 868MHz zewnętrzna IP67, złącze SMA | ~130,00 zł | Botland (Qoltec 57025 z pigtailem N-SMA, lub prostsza antena łamana SMA) |
| 10 | Gniazdo panelowe | Gniazdo SMA-F panelowe, PTFE | 22,00 zł | konektor5000.pl |
| 11 | Membrana wentylacyjna | Zaślepka wentylacyjna GORE-style M12/M16 | ~40,00 zł | bhjanecki.pl |
| 12 | Dławnice | Zestaw PG7 + PG9 IP68 (poliamidowe) | ~15,00 zł | Allegro |
| 13 | Uchwyt panelu | Uchwyt regulowany 30-60°, aluminium, 1 panel | 103,32 zł | pekabet.pl |
| 14 | Drobnica | Bezpiecznik 1-2A, dioda przeciw odwrotnej polaryzacji, kondensator 470-1000µF, silikażel, taśma samowulkanizująca | ~50,00 zł | Allegro/Botland |

**Razem: ok. 2020 zł** (bez czujnika hałasu, już posiadanego)

## Wariant budżetowy (krótsza autonomia zimą, akceptujesz wymianę akumulatora co 2-3 lata, test TTN przed zakupem gateway)

| # | Element | Produkt | Cena |
|---|---|---|---|
| 1 | Węzeł | Heltec WiFi LoRa 32 V4 (ma wejście solarne wbudowane) | ~139 zł |
| 2 | Konwerter RS485 | Waveshare 27479 TTL-RS485 izolowany (dostawa ~09.10.2026) | 29,90 zł |
| 3 | Bramka | (pomiń na start - test OTAA na publicznym TTN przez dobę, zero kosztu) | 0 zł |
| 4 | Panel | Panel poli 20W 12V | 118,47 zł |
| 5 | Regulator | AZO Digital SOL-10S PWM 10A (UWAGA: brak profilu litowego, tylko AGM/żel) | 74,99 zł |
| 6 | Akumulator | Green Cell AGM 12V 17Ah | ~130 zł |
| 7 | Obudowa | Kradex ZP240.190.105SJp, ABS, IP67 (tylko pod daszkiem) | 119,90 zł |
| 8 | Antena + drobnica | j.w., tańsze warianty | ~150 zł |

**Razem: ok. 760 zł** + ewentualnie SenseCAP M2 489 zł później, jeśli test TTN wypadnie źle.

## Kolejność zakupu (żeby nie utknąć)

1. **Najpierw** RAK WisBlock Starter Kit + RAK5802 - zaprogramuj i przetestuj odczyt Modbus z czujnika na biurku (zasilanie z USB, bez solara).
2. **Test TTN**: zarejestruj węzeł na TTN Console (OTAA), zostaw na dobę, sprawdź czy któraś z publicznych bramek (poznan-lora-gateway, PCSS) coś złapie.
3. **Jeśli zasięg słaby** (bardzo prawdopodobne wg researchu) → kup SenseCAP M2, postaw w domu, przełącz węzeł na własną bramkę (ChirpStack albo TTN self-hosted).
4. **Dopiero teraz** zasilanie solarne i obudowa - masz już działający, przetestowany węzeł, wiesz dokładnie ile prądu realnie ciągnie.
