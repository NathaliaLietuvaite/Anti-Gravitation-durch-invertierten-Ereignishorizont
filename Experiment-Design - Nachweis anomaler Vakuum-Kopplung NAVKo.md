# Experiment-Design: Nachweis anomaler Vakuum-Kopplung (NAVKo)

**Stand: 02. August 2025**
**Version: 1.0 (basierend auf YIG-Resonanz und SQUID-Detektion)**

---

## 1. Zielsetzung

Dieses Experiment dient nicht dem Bau eines Antriebs, sondern der Beantwortung einer fundamentalen Frage, die aus unserem Projekt "Asymmetrische Gravitation" folgt:

> **Gibt es eine messbare, anomale Kraft oder eine lokale Vakuum-Signatur, die entsteht, wenn ein hochkohärenter Materiezustand bei seiner spezifischen Resonanzfrequenz angeregt wird?**

Wir wollen den von der NASA-Perspektive geforderten "Hebel" nachweisen: eine kontrollierbare Kopplung zwischen einem herstellbaren Materiezustand und dem Quantenvakuum.

---

## 2. Theoretischer Hintergrund & Wahl der Komponenten

Unsere Hypothese postuliert eine **Resonanz-Katalyse**, bei der ein instabiler Vakuumzustand durch einen präzisen Impuls in einen neuen, stabilen Zustand überführt wird. Um dies zu testen, benötigen wir:
1.  Eine "Antenne" mit einer extrem scharfen, wohldefinierten Resonanz.
2.  Einen "Empfänger", der die subtilsten lokalen Feldänderungen wahrnehmen kann.

* **Warum YIG-Sphären (Yttrium-Eisen-Granat)?**
    YIG ist ein Ferrimagnet mit den **schärfsten bekannten ferromagnetischen Resonanzlinien** (höchster Q-Faktor). Das macht eine polierte YIG-Einkristall-Sphäre zur perfekten "Antenne". Ihre kollektiven Spin-Anregungen (Magnonen) sind extrem kohärent und reagieren nur in einem winzigen Frequenzband.

* **Warum SQUIDs (Supraleitende Quanteninterferometer)?**
    SQUIDs sind die **empfindlichsten Magnetfeldsensoren**, die existieren. Sie können die Fluktuationen einzelner magnetischer Flussquanten detektieren. Wenn unsere postulierte Vakuum-Kopplung eine anomale Signatur erzeugt, werden die SQUIDs sie als unerklärliches "magnetisches Rauschen" genau am Ort des Geschehens hören.

---

## 3. Experimenteller Aufbau

Das Experiment wird in einem Ultrahochvakuum-Kryostaten durchgeführt, um thermische und atmosphärische Störungen zu eliminieren.

**********mermaid
graph TD
    subgraph UHV-Kryostat (77K, 10^-9 mbar, µ-Metall-Schirmung)
        A["Mikrowellenquelle (HF-Generator)"] --> B["Mikrowellen-Resonator"];
        subgraph Torsionspendel (zur Kraftmessung)
            C(YIG-Sphäre)
        end
        B -- Anregung der Spinresonanz --> C;
        C -- Anomales Magnetfeld? --> D[SQUID-Array];
        C -- Anomale Kraft? --> E[Laser-Interferometer];
    end
    D --> F((Datenanalyse));
    E --> F;
    A -- Referenzsignal --> F;
**********

* **Kernkomponenten:**
    * Eine hochreine **YIG-Sphäre** (ca. 1 mm Durchmesser) ist das Herzstück. Sie ist an einem ultradünnen Quarzfaden als **Torsionspendel** aufgehängt.
    * Die Sphäre befindet sich im Zentrum eines **Mikrowellen-Resonators**, der sie mit einem präzise steuerbaren HF-Signal anregt.
    * Ein Array von **SQUID-Sensoren** ist so nah wie möglich an der YIG-Sphäre platziert, um lokale Magnetfeld-Anomalien zu detektieren.
    * Ein **Laser-Interferometer** misst die Auslenkung des Torsionspendels mit Nanometer-Präzision.
    * Das gesamte System ist in einer **Kryokammer** unter Ultrahochvakuum und mehrschichtiger **magnetischer Abschirmung (µ-Metall)** untergebracht.

---

## 4. Versuchsprotokoll

1.  **System-Cooldown & Kalibrierung:** Das System wird auf 77 K (oder 4 K für höhere Empfindlichkeit) heruntergekühlt. Die Basis-Rauschlevel von SQUIDs und Interferometer werden über 24h aufgezeichnet.
2.  **Resonanz-Sweep:** Die Mikrowellenquelle bestrahlt die YIG-Sphäre und fährt langsam ein Frequenzband ab, das die bekannte ferromagnetische Resonanz (FMR) der Sphäre beinhaltet.
3.  **Korrelierte Datenerfassung:** Während des Sweeps werden die Daten der SQUIDs und des Laser-Interferometers mit dem Frequenzsignal des HF-Generators synchronisiert aufgezeichnet.
4.  **Signatur-Analyse:** Mittels Fourier-Analyse wird nach einem statistisch signifikanten Signal gesucht, das **gleichzeitig** in beiden Detektoren (SQUID & Interferometer) auftritt und **exakt** mit der FMR-Frequenz der YIG-Sphäre korreliert.

---

## 5. Falsifizierbare Vorhersage

> **WENN** unsere Hypothese der Resonanz-Katalyse korrekt ist, **DANN** muss eine anomale, nicht-klassische Kraftauslenkung des Pendels (> 5 Sigma über dem Rauschpegel) UND ein korrelierter Peak im SQUID-Signal exakt bei der ferromagnetischen Resonanzfrequenz der YIG-Sphäre auftreten. Bleibt dieses korrelierte Doppel-Signal aus, ist die Hypothese in dieser experimentellen Form widerlegt.

---

## 6. Materialliste & Kostenschätzung (Labor-Prototyp)

| Komponente | Spezifikation / Zweck | Preis (ca.) |
| :--- | :--- | :--- |
| **Kern-System** | | |
| UHV-Kryostat (LN2 / LHe) | 77K / 4K, vibrationsentkoppelt | 40.000 € |
| YIG-Einkristall-Sphäre | 1mm, hochrein, poliert | 1.500 € |
| SQUID-System (3-Kanal) | inkl. Ausleseelektronik | 35.000 € |
| Torsionspendel-Aufbau | Quarzfaden, µN-Sensitivität | 5.000 € |
| **Anregung & Messung** | | |
| Mikrowellen-Generator (1-20 GHz) | Frequenz- und Phasenstabil | 8.000 € |
| Mikrowellen-Resonator (Kupfer) | Maßanfertigung für Kryostat | 2.500 € |
| Laser-Interferometer-System | nm-Auflösung, fasergekoppelt | 12.000 € |
| Lock-In-Verstärker (2x) | Zur Rauschunterdrückung | 10.000 € |
| **Infrastruktur** | | |
| µ-Metall-Abschirmkammer | Mehrschichtig | 15.000 € |
| Hochpräzises DAQ-System | 24 Bit, synchronisiert | 6.000 € |
| **GESAMTSUMME (Grobschätzung)** | **ca. 135.000 €** |
