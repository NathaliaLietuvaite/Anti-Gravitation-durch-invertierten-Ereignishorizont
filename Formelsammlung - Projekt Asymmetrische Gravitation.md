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
from matplotlib.ticker import ScalarFormatter

# --- 1. Physikalische Grundlagen ---

def hawking_temperature(M, G, c, ħ, k_B):
    """Berechnet die Hawking-Temperatur eines Schwarzen Lochs mit Masse M"""
    return (ħ * c**3) / (8 * np.pi * G * M * k_B)

def casimir_force(d, ħ, c):
    """Berechnet die Casimir-Kraft pro Flächeneinheit zwischen zwei Platten"""
    return - (ħ * c * np.pi**2) / (240 * d**4)

def coupling_efficiency(ω, ω_res, Γ):
    """Berechnet die Resonanzkopplungseffizienz (Lorentz-Profil)"""
    return (Γ/2)**2 / ((ω - ω_res)**2 + (Γ/2)**2)

def qhs_energy_density(χ, E_impuls_density):
    """Berechnet die QHS-Energiedichte aus der Kopplungseffizienz"""
    return -χ * E_impuls_density  # [J/m³]

# --- 2. Experimentelle Vorhersagen ---

class GravitationsModulator:
    """Simuliert den Gravitationsmodulationseffekt für ein bestimmtes Material"""
    
    def __init__(self, material_params):
        self.ω_res = material_params['resonance_frequency']  # [rad/s]
        self.Γ = material_params['resonance_width']          # [rad/s]
        self.sensitivity = material_params['sensitivity_factor']  # [N / (J/m³)]
        self.name = material_params.get('name', 'Unbenanntes Material')
    
    def χ(self, ω):
        """Gibt die Kopplungseffizienz bei Frequenz ω zurück"""
        return coupling_efficiency(ω, self.ω_res, self.Γ)
    
    def F_anomal(self, E_impuls_density, ω):
        """Berechnet die anomale Kraft bei gegebener Pulsenergiedichte und Frequenz"""
        χ_val = self.χ(ω)
        ρ_qhs = qhs_energy_density(χ_val, E_impuls_density)
        return ρ_qhs * self.sensitivity
    
    def analyze_resonance(self, E_impuls_density, f_min, f_max, num_points=500):
        """Führt eine Resonanzanalyse durch und gibt Frequenzen und Kräfte zurück"""
        ω_min = 2 * np.pi * f_min * 1e12
        ω_max = 2 * np.pi * f_max * 1e12
        ω_range = np.linspace(ω_min, ω_max, num_points)
        
        forces = []
        efficiencies = []
        
        for ω in ω_range:
            forces.append(self.F_anomal(E_impuls_density, ω))
            efficiencies.append(self.χ(ω))
        
        f_range = ω_range / (2 * np.pi * 1e12)  # Konvertiere rad/s -> THz
        
        return f_range, np.array(forces), np.array(efficiencies)

# --- 3. Materialdatenbank ---

MATERIAL_DATABASE = {
    "YBa₂Cu₃O₇": {
        'resonance_frequency': 2e12,     # rad/s (≈0.318 THz)
        'resonance_width': 1e10,         # rad/s (≈1.6 GHz)
        'sensitivity_factor': 5e-9,      # N/(J/m³)
        'color': 'blue'
    },
    "Bi₂Sr₂CaCu₂O₈": {
        'resonance_frequency': 3.5e12,   # rad/s (≈0.557 THz)
        'resonance_width': 8e9,          # rad/s (≈1.27 GHz)
        'sensitivity_factor': 7e-9,       # N/(J/m³)
        'color': 'green'
    },
    "MgB₂": {
        'resonance_frequency': 1.2e12,   # rad/s (≈0.191 THz)
        'resonance_width': 2e10,          # rad/s (≈3.18 GHz)
        'sensitivity_factor': 3e-9,       # N/(J/m³)
        'color': 'red'
    }
}

# --- 4. Hauptsimulation und Visualisierung ---

def plot_resonance_analysis(material_name, E_impuls_density, f_range):
    """Führt eine vollständige Resonanzanalyse durch und visualisiert die Ergebnisse"""
    material = MATERIAL_DATABASE[material_name]
    modulator = GravitationsModulator(material)
    
    # Resonanzanalyse durchführen
    f_points, forces, efficiencies = modulator.analyze_resonance(
        E_impuls_density, 
        f_range[0], 
        f_range[1]
    )
    
    # Resonanzfrequenz in THz
    f_res = material['resonance_frequency'] / (2 * np.pi * 1e12)
    
    # Plot erstellen
    plt.figure(figsize=(12, 8))
    plt.title(f"QHS-Resonanzanalyse: {material_name}", fontsize=16, pad=20)
    
    # Hauptplot für die anomale Kraft
    plt.plot(f_points, forces * 1e6, 
             color=material['color'], 
             linewidth=2.5,
             label="Anomale Kraft")
    
    # Resonanzfrequenz markieren
    plt.axvline(x=f_res, color='black', linestyle='--', alpha=0.7)
    plt.annotate(f'Resonanz: {f_res:.3f} THz', 
                 xy=(f_res, max(forces * 1e6) * 0.9), 
                 xytext=(f_res + 0.02, max(forces * 1e6) * 0.9),
                 arrowprops=dict(arrowstyle="->", color='black'))
    
    # Zweite Y-Achse für Kopplungseffizienz
    ax2 = plt.gca().twinx()
    ax2.plot(f_points, efficiencies, 
             color='purple', 
             linestyle=':', 
             linewidth=2.5,
             label="Kopplungseffizienz")
    
    # Achsenbeschriftungen und Styling
    plt.xlabel("Frequenz [THz]", fontsize=12, labelpad=15)
    plt.ylabel("Anomale Kraft [µN]", fontsize=12, labelpad=15)
    ax2.set_ylabel("Kopplungseffizienz χ(ω)", fontsize=12, labelpad=15)
    
    # Formattierung
    plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    plt.gca().ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Legende kombinieren
    lines, labels = plt.gca().get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(lines + lines2, labels + labels2, loc='upper right', fontsize=10)
    
    # Zusätzliche Informationen
    plt.figtext(0.5, 0.01, 
                f"Energiedichte: {E_impuls_density/1000:.1f} kJ/m³ | "
                f"Resonanzbreite: {material['resonance_width']/(2*np.pi*1e9):.2f} GHz | "
                f"Max. Kraft: {max(forces)*1e6:.2f} µN",
                ha="center", fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.5))
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)
    return plt

# --- 5. Simulationsaufruf ---

if __name__ == "__main__":
    # Simulationsparameter
    MATERIAL = "YBa₂Cu₃O₇"
    ENERGY_DENSITY = 1e3  # J/m³ = 1 kJ/m³
    FREQ_RANGE = (0.29, 0.34)  # THz
    
    # Analyse durchführen und plotten
    plot = plot_resonance_analysis(MATERIAL, ENERGY_DENSITY, FREQ_RANGE)
    
    # Zusätzliche Hawking-Temperaturanalyse
    M = 1e-10  # 0.1 mg Testmasse
    T_H = hawking_temperature(
        M, 
        G=6.67430e-11, 
        c=299792458,
        ħ=1.0545718e-34,
        k_B=1.380649e-23
    )
    
    print("\n" + "="*70)
    print(f"Zusätzliche Stabilitätsanalyse für {MATERIAL}:")
    print(f"• Hawking-Temperatur für {M*1e6:.1f} mg Masse: {T_H:.3e} K")
    print(f"• Vergleich: Raumtemperatur ≈ 300 K, flüssiges Helium ≈ 4 K")
    print("="*70 + "\n")
    
    plot.show()
