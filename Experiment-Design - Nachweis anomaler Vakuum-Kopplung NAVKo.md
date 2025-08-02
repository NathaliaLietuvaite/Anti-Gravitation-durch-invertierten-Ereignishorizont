# Experiment-Design: Nachweis anomaler Vakuum-Kopplung (NAVKo)

**Stand: 02. August 2025**
**Version: 1.1 (basierend auf YIG-Resonanz und SQUID-Detektion)**

---

## 1. Zielsetzung

Dieses Experiment dient nicht dem Bau eines Antriebs, sondern der Beantwortung einer fundamentalen Frage, die aus unserem Projekt "Asymmetrische Gravitation" folgt:

> **Gibt es eine messbare, anomale Kraft oder eine lokale Vakuum-Signatur, die entsteht, wenn ein hochkohärenter Materiezustand bei seiner spezifischen Resonanzfrequenz angeregt wird?**

Wir wollen den von der NASA-Perspektive geforderten **"Hebel"** nachweisen: eine kontrollierbare Kopplung zwischen einem herstellbaren Materiezustand und dem Quantenvakuum.

---

## 2. Theoretischer Hintergrund & Wahl der Komponenten

Unsere Hypothese postuliert eine **Resonanz-Katalyse**, bei der ein instabiler Vakuumzustand durch einen präzisen Impuls in einen neuen, stabilen Zustand überführt wird. Um dies zu testen, benötigen wir:

* Eine **"Antenne"** mit einer extrem scharfen, wohldefinierten Resonanz.
* Einen **"Empfänger"**, der die subtilsten lokalen Feldänderungen wahrnehmen kann.

### Warum YIG-Sphären (Yttrium-Eisen-Granat)?
YIG ist ein Ferrimagnet mit den **schärfsten bekannten ferromagnetischen Resonanzlinien** (Q-Faktor > 10⁵ bei 10 GHz). Das macht eine polierte YIG-Einkristall-Sphäre zur perfekten "Antenne". Ihre kollektiven Spin-Anregungen (Magnonen) sind extrem kohärent und reagieren nur in einem winzigen Frequenzband.

### Warum SQUIDs (Supraleitende Quanteninterferometer)?
SQUIDs sind die **empfindlichsten Magnetfeldsensoren** (Rauschen < 1 fT/√Hz). Sie können Fluktuationen einzelner magnetischer Flussquanten detektieren. Wenn unsere postulierte Vakuum-Kopplung eine anomale Signatur erzeugt, werden SQUIDs sie als unerklärliches "magnetisches Rauschen" am Ort des Geschehens registrieren.

### Warum Torsionspendel?
Es misst Kräfte bis **≈ 100 aN (10⁻¹⁸ N)**. Jede vom Vakuum ausgeübte anomale Kraft würde eine messbare Auslenkung verursachen.

---

## 3. Experimenteller Aufbau

Das Experiment wird in einem Ultrahochvakuum-Kryostaten durchgeführt, um thermische und atmosphärische Störungen zu eliminieren.

**********mermaid
graph TD
    subgraph UHV-Kryostat["UHV-Kryostat (4K, 10⁻⁹ mbar, µ-Metall-Schirmung)"]
        A["Mikrowellenquelle (HF-Generator)"] --> B["Mikrowellen-Resonator"];
        subgraph Torsionspendel["Torsionspendel (Kraftmessung)"]
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

### Kernkomponenten:
* Eine hochreine **YIG-Sphäre** (Ø 1 mm) als Herzstück, aufgehängt an einem ultradünnen Quarzfaden (Torsionspendel).
* Die Sphäre befindet sich im Zentrum eines **Mikrowellen-Resonators** (präzise HF-Anregung).
* Ein **SQUID-Array** (3-Achsen) ist radial um die YIG-Sphäre angeordnet (Abstand ≤ 5 mm).
* Ein **homodynes Laser-Interferometer** misst Pendelauslenkungen mit **< 1 nm** Präzision.
* Der Kryostat ist **vibrationsisoliert** und **magnetisch abgeschirmt** (µ-Metall).

---

## 4. Versuchsprotokoll

1.  **System-Cooldown & Kalibrierung:**
    * Abkühlung auf **4 K** (für höhere SQUID-Empfindlichkeit).
    * 24h Basisrauschmessung (SQUIDs, Interferometer).
    * Kalibrierung der Torsionskonstante des Pendels.
2.  **Resonanz-Sweep:**
    * HF-Generator fährt Frequenzband **ω_res ± 1 GHz** in 1 MHz-Schritten ab.
    * Pro Frequenzpunkt: Messdauer ≥ 60 s (für Statistik).
3.  **Korrelierte Datenerfassung:**
    * Synchronisierte Aufzeichnung von: HF-Frequenz und -Amplitude, SQUID-Ausgang (3 Kanäle), Interferometer-Signal, Umgebungsparameter (Temperatur, Vibrationen).
4.  **Signatur-Analyse:**
    * Fourier-Transformation der Zeitreihen.
    * Kreuzkorrelation zwischen HF-Signal und Detektorantwort.
    * Suche nach einem **korrelierten Doppelpeak** bei ω_res in SQUID **und** Interferometer.

---

## 5. Falsifizierbare Vorhersage

> **WENN** unsere Hypothese der Resonanz-Katalyse korrekt ist, **DANN** tritt bei exakt ω_res auf:
> * Eine **anomale Kraft** (gemessen am Torsionspendel) von **> 0.5 fN** (5σ über Rauschen),
> * Ein **korrelierter Magnetfeld-Peak** im SQUID (Änderung > 5 fT),
> * Beide Signale sind **phasenkohärent** mit dem HF-Anregungssignal.
>
> Bleibt dieses korrelierte Doppelsignal aus, ist die Hypothese in dieser Form widerlegt.

---

## 6. Materialliste & Kostenschätzung (Labor-Prototyp)

| Komponente | Spezifikation / Zweck | Preis (ca.) |
| :--- | :--- | :--- |
| **Kern-System** | | |
| UHV-Kryostat (4K) | Vibrationsentkoppelt, optische Fenster | 55.000 € |
| YIG-Einkristall-Sphäre | Ø 1 mm, Oberflächenrauheit < 5 nm | 1.500 € |
| SQUID-System (3-Achsen) | inkl. Flux-Locked-Loop-Elektronik | 38.000 € |
| Torsionspendel-Aufbau | Quarzfaden, Auflösung < 100 aN | 7.000 € |
| **Anregung & Messung** | | |
| Mikrowellen-Generator | 1–20 GHz, Frequenzstabil < 1 ppb | 12.000 € |
| Mikrowellen-Resonator | Hohlraumresonator, vergoldet | 3.500 € |
| Homodynes Interferometer | 633 nm, nm-Auflösung, fasergekoppelt | 15.000 € |
| Lock-In-Verstärker (2x) | Dual-Phase, für Rauschfilterung | 12.000 € |
| **Infrastruktur** | | |
| µ-Metall-Abschirmung | Zylindrisch, Restfeld < 1 nT | 18.000 € |
| DAQ-System | 24 Bit, 16 Kanäle, synchronisiert | 8.000 € |
| Vibrationsisolierung | Aktive/passive Hybridlösung | 22.000 € |
| **GESAMTSUMME** | | **≈ 192.000 €** |

**Hinweis:** Kosten können durch Kooperationen mit Universitäten (Nutzung von Kryostaten, SQUIDs) deutlich reduziert werden.

---

## 7. Risikoanalyse & Alternativen

* **Hauptrisiko:** Elektromagnetisches Übersprechen zwischen HF-Anregung und SQUIDs.
    * **Gegenmaßnahme:** Abschirmung des Resonators, getrennte Erdung, Filterung.
* **Alternative Detektion:** Statt Interferometer – **Mikro-Elektromechanisches System (MEMS)** mit integrierter Kraftrückkopplung.
* **Alternative "Antenne":** **Bose-Einstein-Kondensat** (noch schärfere Resonanzen, aber aufwendiger).

---

## 8. Ethische Aspekte

* Alle Daten werden **open source** (MIT-Lizenz) veröffentlicht.
* Negative Ergebnisse sind ebenso wertvoll wie positive – sie verengen den Suchraum für zukünftige Forschung.
