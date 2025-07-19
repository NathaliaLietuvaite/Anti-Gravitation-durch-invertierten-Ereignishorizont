# Materialliste: Quanten-Helfersystem (QHS) – Mini-Version
## Version 1.0 – Desktop-Prototyp zur Vakuum-Modulation und Signaldetektion

Ziel: Realisierung eines testbaren Tischgeräts mit Kernfunktionen:
- Erzeugung strukturierter EM-Felder
- Lokalisierte negative Energiedichte (Casimir-artig)
- Stabilisierung & kohärente Modulation
- Messung kleinster Abweichungen in Raumzeit-kopplungsrelevanten Größen

---

## Gehäuse & Infrastruktur

| Komponente                        | Spezifikation / Zweck                              | Preis (ca.)     |
|----------------------------------|-----------------------------------------------------|-----------------|
| Aluminiumgehäuse (EMV-geschirmt) | 20×20×20 cm – modular, abschirmend                  | 150 €           |
| Vibrationstisch (Mini-Version)   | Gedämpft, Gummi-/Stahlhybrid                        | 300 €           |
| Trenntransformator / UPS         | Netzfilterung / Stromstabilität                     | 150 €           |

---

## Kryo- & Thermomanagement (optional für Supraleitung)

| Komponente                        | Spezifikation                                       | Preis (ca.)     |
|----------------------------------|-----------------------------------------------------|-----------------|
| Kryokammer mit Stickstoffanschluss | max. 77 K, isoliert                                 | 500 €           |
| Temperaturcontroller + Sensoren  | PT1000, ±0.1 K, mehrkanalig                         | 250 €           |

---

## Casimir-Platten & Nanoantrieb

| Komponente                        | Spezifikation                                       | Preis (ca.)     |
|----------------------------------|-----------------------------------------------------|-----------------|
| Goldbeschichtete Siliziumplatten | 2× 20×20 mm, hochplan, λ/10                         | 500 €           |
| Piezoaktuator (x, y, z)          | nm-Auflösung, 3-Achs-Nanopositionierung             | 900 €           |
| Abstandssensor (kapazitiv/opto)  | Genauigkeit < 10 nm                                 | 300 €           |

---

## EM-Feldgenerator & Spintronic-Module

| Komponente                        | Spezifikation                                       | Preis (ca.)     |
|----------------------------------|-----------------------------------------------------|-----------------|
| HF-Signalquelle (1 MHz–3 GHz)    | Frequenzstabil, programmierbar                      | 500 €           |
| TMR/GMR-Sensoren (Spintronik)    | Magnetische Rauschmodulation, Vakuumkopplung       | 300 €           |
| Helmholtzspule (Mini)            | zur Feldlinearität & Symmetrieprüfung              | 150 €           |
| EMV-Schutzmatrix                 | Ferritkerne, HF-Dämpfer, Faraday-Mesh               | 100 €           |

---

## Detektion & Auswertung

| Komponente                        | Spezifikation                                       | Preis (ca.)     |
|----------------------------------|-----------------------------------------------------|-----------------|
| Torsionswaage (Mini)             | Auflösung < 1 µN                                    | 1.200 €         |
| Mini-Interferometer              | z. B. laserbasierter 2-Kanal-Aufbau                 | 800 €           |
| ADC / DAQ                        | 24 Bit, Multikanal, Sampling ≥ 10 kHz               | 350 €           |
| FFT-Analyse-Software (open src)  | z. B. GNU Octave, SciPy                             | –               |
| Digitale Rauschreduktion         | Python-basierter Noise-Cancellation-Algorithmus     | –               |

---

## Isolation, Sicherheit & Störschutz

| Komponente                        | Spezifikation                                       | Preis (ca.)     |
|----------------------------------|-----------------------------------------------------|-----------------|
| μ-Metall-Schirmung               | Innenauskleidung zur Magnetfeldabschirmung          | 300 €           |
| EMV-Isoliermatten                | Boden / Rückwand                                    | 100 €           |
| Optische Abschirmung             | Schwarze PTFE-Wände (Streulichtunterdrückung)       | 80 €            |

---

## Steuerung & Logging

| Komponente                        | Spezifikation                                       | Preis (ca.)     |
|----------------------------------|-----------------------------------------------------|-----------------|
| Raspberry Pi / BeagleBone        | GPIO-Steuerung, Datenspeicherung                    | 100 €           |
| I²C / SPI Breakout Boards        | Für Sensorverbindung & Echtzeitsteuerung            | 50 €            |
| Python-basierte Steuerplattform  | (z. B. PyDAQ, PyVisa, PySerial)                     | –               |

---

## Gesamtkalkulation

| Kategorie                        | Preisbereich (ca.)       |
|----------------------------------|---------------------------|
| Mechanik + Gehäuse               | 600 €                     |
| Casimir + Positionierung         | 1.700 €                   |
| Spintronik + HF-Systeme          | 1.000 €                   |
| Detektion + Auswertung           | 2.700 €                   |
| Steuerung + Sicherheit           | 400 €                     |
| **Gesamtkosten (QHS Mini)**      | **ca. 6.400 € – 8.000 €** |

---

## Kommentar zur Realisierbarkeit

> Viele Komponenten können aus *Open Hardware*-Kreisen oder gebrauchten Laborbeständen bezogen werden (z. B. Piezo-Scanner, Laserdioden, Interferometerbauteile).  
> Fokus sollte anfangs auf der **passiven Messung von Feldmodulationen** durch strukturierte Casimir-Kammern + HF-Feld liegen – der stabilisierte Zustand kann zunächst als Fluktuationsanomalie verstanden werden.

