# Formelsammlung: Projekt Asymmetrische Gravitation

**Stand: 05. August 2025**

---

## 1. Fundamentale Gleichungen (Die Regeln)

Dies sind die etablierten Gesetze und Beobachtungen, die den Rahmen unseres Universums definieren und die wir lokal zu beeinflussen versuchen.

**Einsteinsche Feldgleichungen (Allgemeine Relativitätstheorie):** Dies ist die Master-Gleichung. Sie besagt, dass die **Geometrie der Raumzeit** ($G_{\mu\nu}$) durch die **Verteilung von Masse und Energie** ($T_{\mu\nu}$) bestimmt wird. Unser Ziel ist es, den Energie-Impuls-Tensor $T_{\mu\nu}$ auf der rechten Seite so zu modifizieren, dass auf der linken Seite eine abstoßende Geometrie entsteht.

```math
G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
```

**Das Hubble-Tension-Dilemma (Experimentelle Realität 2025):** Die gemessene Expansionsrate des Universums ist widersprüchlich. Dies ist keine Messungenauigkeit, sondern eine fundamentale Herausforderung für die Kosmologie. Die Diskrepanz zwischen der lokalen Messung ($H_0^{\text{lokal}}$) und der Vorhersage aus dem frühen Universum ($H_0^{\text{CMB}}$) deutet auf "neue Physik" hin. Unsere Hypothese ist, dass die lokale Struktur des Vakuums die Expansion beeinflusst. Das QHS könnte somit ein Werkzeug sein, um diese "neue Physik" im Labor zu untersuchen.

```math
\Delta H_0 = H_0^{\text{lokal}} - H_0^{\text{CMB}} > 0
```

**Hawking-Temperatur eines Ereignishorizonts:** Diese Formel beschreibt die fundamentale **Instabilität** von Horizonten. Jeder "Gravitationshügel", den wir erzeugen, würde durch Quantenfluktuationen "verdampfen". Dies ist die quantitative Beschreibung des **Stabilitätsdilemmas**, das unser QHS überwinden muss.

```math
T_H = \frac{\hbar c^3}{8\pi G M k_B}
```

---

## 2. Gleichungen der relevanten Effekte (Die Hebel)

Dies sind die Formeln für bekannte physikalische Effekte, die als Anknüpfungspunkte für unsere Hypothese dienen.

**Casimir-Kraft (zwischen zwei Platten):** Dies ist der experimentelle Beweis, dass das **Quantenvakuum eine physikalische Realität** ist und dass durch geometrische Anordnungen eine **negative Energiedichte** (resultierend in einer anziehenden Kraft) erzeugt werden kann. Wir wollen diesen Effekt verallgemeinern und umkehren.

```math
\frac{F_c}{A} = - \frac{\hbar c \pi^2}{240 d^4}
```

---

## 3. Hypothetische Gleichungen (Unser Kernkonzept)

Dies sind die neuen, spekulativen Formeln, die das Herz unseres Projekts bilden und als testbare Hypothesen formuliert sind.

**Modifizierter Energie-Impuls-Tensor:** Wir postulieren, dass der Gesamt-Energie-Impuls-Tensor eine zusätzliche, künstlich erzeugte Komponente durch das Quanten-Helfersystem (QHS) enthält:

```math
T_{\mu\nu}^{\text{Total}} = T_{\mu\nu}^{\text{Materie}} + T_{\mu\nu}^{\text{QHS}}
```

**Der QHS-Term (Triple-Alpha-Analogie):** Die Energiedichte des QHS-Terms ($\rho_{QHS}$) ist negativ und hängt von der **Resonanz** ab. Dabei ist $\chi(\psi, \omega, g)$ eine dimensionslose **Kopplungseffizienz**, die vom Quantenzustand des Materials ($\psi$), der Frequenz des Impulses ($\omega$) und der Geometrie ($g$) abhängt.

```math
\rho_{QHS} = - \chi(\psi, \omega, g) \cdot E_{\text{impuls}}
```

**Die Resonanzbedingung:** Die Kopplungseffizienz $\chi$ ist nur in einem sehr schmalen Frequenzband signifikant. Wir modellieren sie mit einer Lorentz-Funktion. **Bedeutung:** Nur wenn die Frequenz $\omega$ exakt die **Resonanzfrequenz** $\omega_{res}$ des Materials trifft, kommt es zu einer signifikanten Kopplung und zur Erzeugung einer negativen Energiedichte.

```math
\chi(\omega) \propto \frac{\Gamma^2}{(\omega - \omega_{res})^2 + (\Gamma/2)^2}
```

---

## 4. Falsifizierbare Vorhersagen (Der Weg zum Experiment)

Aus den Hypothesen leiten wir konkrete, messbare Vorhersagen ab, die unser Modell beweisen oder widerlegen können.

1.  **Anomale Kraftmessung:** Wenn das QHS bei der Frequenz $\omega_{res}$ wirkt, sollte eine Torsionswaage eine **abstoßende Kraft** $F_{\text{anomal}}$ messen, deren Stärke proportional zu $\rho_{QHS}$ ist. **Falsifikation:** Wird bei keiner Frequenz eine anomale Kraft gemessen, ist die Hypothese falsch.

2.  **Interferometrische Phasenverschiebung:** Die durch $\rho_{QHS}$ erzeugte negative Raumzeitkrümmung muss zu einer messbaren **Verkürzung der Lichtlaufzeit** führen. Ein Laser-Interferometer sollte eine charakteristische, negative Phasenverschiebung $\Delta\phi$ zeigen. **Falsifikation:** Bleibt die Phasenverschiebung aus, ist die Hypothese falsch.

3.  **Lokale Hubble-Modulation:** Wenn unsere Hypothese zur Hubble-Tension stimmt, muss das QHS in der Lage sein, den **effektiven lokalen Expansionsparameter** messbar zu verändern. Dies wäre der ultimative Test. **Falsifikation:** Kann keine Korrelation zwischen QHS-Aktivität und einer lokalen Raumzeit-Expansion/-Kontraktion nachgewiesen werden, ist die Verbindung zur Hubble-Tension widerlegt.

## 5. Simulations-Framework: Projekt Asymmetrische Gravitation 

**Stand: 05. August 2025**

## Zusammenfassung

Dieses Dokument enthält das Python-Skript, das als Simulationsumgebung für die Hypothese der asymmetrischen Gravitation dient. Es übersetzt die theoretische Formelsammlung in ein funktionierendes, testbares Modell und führt folgende Schritte aus:

1.  **Definition** der fundamentalen und hypothetischen Gleichungen als Python-Funktionen.
2.  **Festlegung** von physikalischen Konstanten und Materialparametern für ein konkretes Experiment (hier: Supraleiter YBa₂Cu₃O₇).
3.  **Durchführung** einer Simulation, die einen Frequenzscan um die erwartete Resonanzfrequenz des Materials durchführt.
4.  **Berechnung und Visualisierung** einer falsifizierbaren Vorhersage: Die Stärke der anomalen, abstoßenden Kraft in Abhängigkeit von der Frequenz.

Das Ergebnis ist eine Resonanzkurve, die als direkte Blaupause für ein reales Laborexperiment dient. Wenn die Hypothese korrekt ist, muss ein reales Experiment ein qualitativ gleiches Ergebnis liefern.

---

## Python-Simulationscode

Hier ist der vollständige Code zur Simulation. Er kann direkt kopiert und ausgeführt werden, sofern die Bibliotheken `numpy` und `matplotlib` installiert sind.

```python
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Theoretisches Fundament ---

# Einsteinsche Feldgleichungen (Platzhalter für das konzeptionelle Verständnis)
def einstein_field_equations():
    return "G_μν + Λg_μν = (8πG/c⁴) T_μν"

# Experimentelle Daten: Hubble-Tension-Dilemma
H0_lokal = 73.0  # km/s/Mpc
H0_CMB = 67.4    # km/s/Mpc
ΔH0 = H0_lokal - H0_CMB

# Hawking-Temperatur
def hawking_temperature(M, G, c, ħ, k_B):
    return (ħ * c**3) / (8 * np.pi * G * M * k_B)

# --- 2. Physikalische Effekte als Hebel ---

# Casimir-Kraft
def casimir_force(d, ħ, c):
    return - (ħ * c * np.pi**2) / (240 * d**4)

# --- 3. Kernhypothesen des Modells ---

# Energiedichte des QHS-Terms
def qhs_energy_density(χ, E_impuls):
    return -χ * E_impuls

# Resonanzbedingung (Lorentz-Profil für die Kopplungseffizienz)
def coupling_efficiency(ω, ω_res, Γ):
    return Γ**2 / ((ω - ω_res)**2 + (Γ/2)**2)

# --- 4. Experimentelle Vorhersagen ---

class ExperimentalPredictions:
    def __init__(self, material_params, constants):
        self.material = material_params
        self.constants = constants
        self.ω_res = material_params['resonance_frequency']
        self.Γ = material_params['resonance_width']
        
    def anomalous_force_prediction(self, E_impuls, ω):
        """Vorhersage der abstoßenden Kraft F_anomal."""
        χ = coupling_efficiency(ω, self.ω_res, self.Γ)
        ρ_qhs = qhs_energy_density(χ, E_impuls)
        # Vereinfachte Annahme: Kraft ist proportional zur Energiedichte
        return ρ_qhs * self.material['sensitivity_factor']
    
# --- 5. Konstanten und Materialparameter ---

# Physikalische Konstanten
constants = {
    'ħ': 1.0545718e-34,    # J·s
    'c': 299792458,         # m/s
    'G': 6.67430e-11,       # m³/kg/s²
    'k_B': 1.380649e-23,    # J/K
}

# Beispielmaterial: Supraleiter YBa₂Cu₃O₇
supraleiter = {
    'name': "YBa₂Cu₃O₇",
    'resonance_frequency': 2e12,  # 2 THz, ausgedrückt in rad/s
    'resonance_width': 1e10,      # 10 GHz, ausgedrückt in rad/s
    'sensitivity_factor': 5e-9    # Umrechnungsfaktor [N/(J/m³)]
}

# --- 6. Simulation und Visualisierung ---

if __name__ == "__main__":
    # Initialisiere Vorhersagen für das gewählte Material
    predictions = ExperimentalPredictions(supraleiter, constants)
    
    # Frequenzscan um die Resonanzfrequenz herum
    frequencies = np.linspace(1.9e12, 2.1e12, 500)  # rad/s
    anomalous_forces = []
    
    # Simuliere das Experiment für jede Frequenz
    for ω in frequencies:
        F_anomal = predictions.anomalous_force_prediction(
            E_impuls=1e3,  # Annahme: 1 kJ/m³ Pulsenergie
            ω=ω
        )
        anomalous_forces.append(F_anomal)
    
    # Plot der Ergebnisse
    plt.figure(figsize=(12, 7))
    # Umrechnung der Frequenz von rad/s zu THz für die x-Achse
    plt.plot(frequencies / (2 * np.pi * 1e12), anomalous_forces)
    # Markiere die Resonanzfrequenz
    plt.axvline(x=supraleiter['resonance_frequency'] / (2 * np.pi * 1e12), 
                color='r', linestyle='--', label=f"Resonanz bei {supraleiter['resonance_frequency']/ (2 * np.pi * 1e12):.2f} THz")
    
    plt.xlabel('Frequenz [THz]')
    plt.ylabel('Anomale abstoßende Kraft [N] (simuliert)')
    plt.title('Simulierte Resonanzkurve der QHS-Kopplung für YBa₂Cu₃O₇')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
