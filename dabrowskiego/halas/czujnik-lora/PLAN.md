---
title: "Własny kolektor pomiaru hałasu (LoRa, solar) - plan budowy"
type: project
domain: halas
updated: 2026-09-18
---

# Własny czujnik hałasu na LoRa, zasilany solarnie - plan

Cel: niezależny od ZDM/BAASA, ciągły pomiar hałasu na zewnątrz (elewacja/balkon Dąbrowskiego 96), zasilany bateryjnie-solarnie, transmisja danych przez LoRaWAN. Ernest kupił już czujnik przemysłowy RS485 Modbus (rodzina Renke/Renkeer, rebadge YY010), 30-130 dB, ±0,5dB, IP67, pobór 0,4W w wersji RS485.

Deep research: 3 równoległe subagenty (dev kit + LoRa, gateway/TTN, zasilanie solarne/RS485/obudowa). Poniżej zsyntetyzowany, spójny plan.

## 1. Węzeł czujnikowy (płytka + LoRa + RS485)

**Rekomendacja: RAK WisBlock** - RAK19007 (base board) + RAK4631 (nRF52840 + SX1262 LoRa, BLE) + RAK5802 (moduł RS485, gotowe przykłady Modbus w bibliotece).

- WisBlock Meshtastic Starter Kit 868MHz (RAK19007+RAK4631+antena) - **159 zł**, Botland (24h): https://botland.com.pl (SOC-19318)
- RAK5802 RS485 - brak w PL, ~7 EUR z https://kiloelectronics.com/en/produkt/rs485-rak5802/ lub 6 USD https://store.rakwireless.com/products/rak5802-rs485-interface (~30-40 zł z wysyłką)

Dlaczego to, nie ESP32 (Heltec/LILYGO): RAK5802 to jedyny moduł RS485 gotowy "z pudełka" z przykładami Modbus, zero lutowania. Minus: brak WiFi na RAK4631 - nieistotne, bo i tak kupujemy własną bramkę LoRaWAN (pkt 2).

**Alternatywa** (jeśli wolisz WiFi jako kanał zapasowy i nie przeszkadza lutowanie): Heltec WiFi LoRa 32 V4 (~139 zł, ma wejście solarne wbudowane, V3 NIE ma) + konwerter RS485 izolowany Waveshare 27479 (29,90 zł, Botland, dostawa ok. 09.10.2026) lub tańszy MAX485 (~12-15 zł, bez izolacji).

### Rejestr Modbus (do zaprogramowania)
Wspólny mianownik rodziny Renke/Firstrate/Sonbest: funkcja `0x03` (read holding registers), rejestr `0x0000`, wartość = dB × 10 (Renke, Firstrate) - u Sonbest niepewne (manual sprzeczny, zweryfikować empirycznie). Domyślny baud: Renke 4800 8N1, Firstrate/Sonbest 9600 8N1 - **czujnik YY010 nieudokumentowany publicznie, zrób autodetekcję 2400/4800/9600 przy pierwszym uruchomieniu.**

Ramka zapytania (adres 1): `01 03 00 00 00 01 84 0A` (CRC zweryfikowany).

Szkic Arduino (ModbusMaster, adaptuj piny pod RAK5802):
```cpp
#include <ModbusMaster.h>
#define RS485_DE_RE 4
ModbusMaster node;
void preTransmission()  { digitalWrite(RS485_DE_RE, HIGH); }
void postTransmission() { digitalWrite(RS485_DE_RE, LOW);  }
void setup() {
  Serial.begin(115200);
  pinMode(RS485_DE_RE, OUTPUT);
  Serial2.begin(4800, SERIAL_8N1, RXD2, TXD2);   // Renke 4800, Firstrate/Sonbest 9600
  node.begin(1, Serial2);
  node.preTransmission(preTransmission);
  node.postTransmission(postTransmission);
}
void loop() {
  if (node.readHoldingRegisters(0x0000, 1) == node.ku8MBSuccess) {
    float dB = node.getResponseBuffer(0) / 10.0;
    Serial.printf("Halas: %.1f dB\n", dB);
  }
  delay(1000);
}
```
RAK5802 ma automatyczne przełączanie TX/RX (nie trzeba pinu DE/RE ręcznie) - uprość wg jego przykładów: https://github.com/RAKWireless/WisBlock/tree/master/examples/RAK4630/IO/RAK5802_RS485

**Uwaga bezpieczeństwa:** ESP32/nRF52840 mają logikę 3,3V, klasyczny czerwony moduł MAX485 pracuje na 5V - podłączenie bez dzielnika napięcia na linii RO może uszkodzić GPIO. RAK5802 jest natywnie 3,3V, bezpieczny.

## 2. Bramka LoRaWAN (gateway)

**Publiczne pokrycie TTN w Poznaniu istnieje, ale za słabe do tej sprawy.** Najbliższe działające bramki: 3,8 km (indoor, bez szans), 4,0 km (PCSS, outdoor) i 5,0 km (`poznan-lora-gateway`, outdoor, maszt 100m npt - najlepszy kandydat). Przy tym dystansie wymagane SF10-SF12, a limit Fair Use TTN (30s czasu antenowego/dobę) daje wtedy **tylko ok. 20-40 pomiarów/dobę**. Za mało do wykazania rozkładu dobowego hałasu.

**Rekomendacja: kup własną bramkę.** SenseCAP M2 Multi-Platform (SX1302, EU868, Ethernet+PoE+WiFi, wspiera TTN/ChirpStack/AWS IoT) - **489 zł**, Botland, wysyłka 24h: https://botland.com.pl/sensecap-moduly-lorawan/22110-sensecap-m2-multi-platform-bramka-wewnetrzna-lorawan-sx1302-eu868-seeedstudio-114992981.html

Z własną bramką w domu (SF7, ~0,1s/pakiet) wychodzi ~250 pomiarów/dobę (co ~6 min) bez limitów FUP, jeśli działa jako pełny network server (ChirpStack) - nie przez TTN Sandbox.

**Test za darmo przed zakupem:** zanim kupisz bramkę, uzbrój węzeł w OTAA na TTN Console i zostaw na dobę - zobaczysz w konsoli (RSSI/SNR) czy w ogóle coś łapie któraś z publicznych bramek. Zero kosztu, może zaoszczędzić 489 zł jeśli zasięg jest lepszy niż szacowano.

**Droższa alternatywa** (wbudowany network server, niezależność od TTN): Milesight UG63-868M, 629 zł, Botland, dostawa ok. 23.09.2026.

## 3. Zasilanie solarne

**Kluczowe ustalenie:** czujnik pobiera 0,4W (wersja RS485, potwierdzone kartą Renkeer - 1,2W dotyczy wersji analogowej 0-10V, nie naszej). Bilans dobowy przy pracy 24/7: czujnik 9,6Wh + węzeł LoRa (dobry deep sleep, wysyłka co 5 min) ~1,2Wh + straty ~1Wh = **~12 Wh/dobę**.

Dane nasłonecznienia Poznania (PVGIS, panel nachylony 60°, realne): grudzień 1,23 PSH/dobę średnio (0,73 w najgorszym roku), czerwiec 4,79 PSH. **Panel pod kątem 60-70° albo pionowo na elewacji** (o 13% lepiej w grudniu niż 40°, nie łapie śniegu).

Dobór panelu wg bilansu (MPPT, sprawność 0,75): grudzień średni → 13W, grudzień najgorszy → 22W, 10-dniowa mgła → 46W. **Rekomendacja: panel 30W** - 20W to absolutne minimum przy idealnej ekspozycji, poniżej tylko praca sezonowa (marzec-październik).

Akumulator na autonomię 7-14 dni bez słońca:
- **LiFePO4 12,8V 20Ah (256Wh)** - Green Cell CUBE, IP54, BMS z low-temp charge cutoff (**krytyczne** - ładowanie LiFePO4 poniżej 0°C bez tego zabezpieczenia trwale niszczy ogniwa) - **339,95 zł**: https://greencell.global (LFPGC12V20AH)
- AGM traci 45-75% pojemności w mrozie (derating), do odrzucenia jako główne rozwiązanie - tylko jako wariant budżetowy z krótszą autonomią (4-5 dni zimą).

Regulator ładowania: **Victron SmartSolar MPPT 75/10** (profil LiFePO4, Bluetooth, -30 do +60°C) - **210 zł**: https://energomag.pl/regulator-ladowania-victron-smart-solar-mppt-75-10.html

Architektura: akumulator 12V → czujnik RS485 BEZPOŚREDNIO (mieści się w oknie 10-30V, bez przetwornicy) + akumulator 12V → step-down → 5V dla węzła LoRa. Step-down: **Traco TSR 1-2450** (prąd spoczynkowy ~2mA, ~30-45 zł) - NIE tanie LM2596 (prąd jałowy 6-10mA zjada tyle co cały węzeł).

## 4. Obudowa i montaż

Materiał: **poliwęglan**, nie ABS (ABS pęka w mrozie i degraduje pod UV). Musi pomieścić akumulator Green Cell 185×80×170mm → potrzebna skrzynka min. klasy 300×200×150mm.

- ETI GT 30-20-15, IP65, 300×200×150mm - 249,68 zł: https://elektrycznie.pl/produkt/gt-30-20-15-obudowa-hermetyczna-ip65-300x200x150.html
- (tańsza, ale ABS, tylko pod daszkiem/osłonięta) Kradex ZP240.190.105SJp, IP67, 119,90 zł, Botland - ZA NISKA (105mm) na ten akumulator

Dławnice: PG7 (kable sygnałowe) + PG9 (solar), poliamidowe, ~15 zł łącznie na Allegro.

Antena 868MHz zewnętrzna IP67 + gniazdo panelowe SMA-F (~150 zł łącznie), kabel krótki (RG58 tłumi 0,6-0,8dB/m przy 868MHz, max 1-2m).

Membrana wyrównująca ciśnienie (GORE Protective Vent) - obudowa hermetyczna bez niej działa jak skraplacz, kondensacja niszczy elektronikę. BH Janecki, zaślepki wentylacyjne M12/M16, ~20-60 zł.

Montaż: pionowo, pod okapem jeśli możliwe (pełne słońce = +60-70°C wewnątrz, dobija akumulator). Dławnice zawsze od spodu, z pętlą kapiącą.

## 5. Otwarte pytania / do zweryfikowania na miejscu

- Dokładna nazwa/producent posiadanego czujnika (YY010 nieudokumentowany publicznie) - zrób autodetekcję baudrate przy pierwszym uruchomieniu.
- Realny zasięg do najbliższej publicznej bramki TTN - przetestuj OTAA przed zakupem własnej bramki (zero kosztu).
- Dokładne ceny obudów Spelsberg/Hensel (lepsza jakość niż ETI, ale sklepy nie pokazują cen online - dopytać w TME/Onninen).
- Terminacja RS485 (120Ω) potrzebna tylko przy dłuższym kablu (>kilka metrów) - do sprawdzenia wg realnej odległości czujnik-elektronika w skrzynce.

Zobacz [`zakupy.md`](zakupy.md) - pełna lista zakupowa z cenami i linkami.
