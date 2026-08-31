# QKD-Redteam-Core 🔐⚛️

An open-source, modern Python library (`pyproject.toml` structured) designed for **Quantum Key Distribution (QKD)** simulation, **Quantum Network Penetration Testing (Red Teaming)**, and **Statistical Countermeasure Verification (Blue Teaming)**—fully licensed under Apache 2.0.

This framework acts as a lightweight, pure-Python core engine that simulates cryptographic protocols under realistic physical layer constraints and evaluates them against sophisticated adversarial threat vectors **without requiring heavy external simulation suites**.

---

## 🚀 Key Features

- **Multi-Protocol Simulation Suite:** Hosts standard **BB84 (4-State)**, **B92 (2-State with Anti-Correlation)**, and entanglement-based **E91 (EPR Pairs & CHSH Validation)** architectures under a unified framework.
- **Pure Python Architecture:** Leverages standard scientific computing tools (`NumPy`), making it portable and easy to integrate into corporate SOC panels or academic testing tools.
- **Realistic Physical Noise Modeling:** Implements distance-based photon attenuation (0.2 dB/km standard baseline) and Dark Count Rates, mapping environmental impacts directly onto the Quantum Bit Error Rate (QBER).
- **Adversarial Attack Suite:** Simulates active brute-force eavesdropping (*Intercept-Resend*) and highly stealthy multi-photon pulse splitting (*Photon-Number-Splitting*).
- **Adaptive Blue Team Countermeasures:** Implements the **Decoy State Protocol** to audit channel transmission yields, dynamically exposing zero-footprint PNS attacks using statistical anomaly filters.

---

## 🖥️ Simulation Output Preview

When you execute the core validation suite (`python main.py`), the framework benchmarks the core quantum infrastructure and displays real-time cryptographic audit telemetry:



```text
================================================================
===       QUANTUM RED TEAM CORE CENTRAL SECURITY SUITE       ===
================================================================

--- PROTOCOL UNDER TEST: BB84 (4-STATE) ---
================ MONITORING FIBER LINK: 10.0 KM ================
[No Attack] Natural Channel Noise: 6.54% | QBER: 6.95%
-> Security Alert: ✅ LINE SECURE
[RED TEAM ATTACK] Intercepted Link | QBER: 28.28%
-> Security Alert: 🚨 CRITICAL TIME ATTACK DETECTED

================ MONITORING FIBER LINK: 50.0 KM ================
[No Attack] Natural Channel Noise: 14.5% | QBER: 15.11%
-> Security Alert: ✅ LINE SECURE
[RED TEAM ATTACK] Intercepted Link | QBER: 33.05%
-> Security Alert: 🚨 CRITICAL TIME ATTACK DETECTED


--- PROTOCOL UNDER TEST: B92 (2-STATE) ---
================ MONITORING FIBER LINK: 10.0 KM ================
[No Attack] Natural Channel Noise: 6.54% | QBER: 4.71%
-> Security Alert: ✅ LINE SECURE
[RED TEAM ATTACK] Intercepted Link | QBER: 32.79%
-> Security Alert: 🚨 CRITICAL TIME ATTACK DETECTED

================ MONITORING FIBER LINK: 50.0 KM ================
[No Attack] Natural Channel Noise: 14.5% | QBER: 17.89%
-> Security Alert: ✅ LINE SECURE
[RED TEAM ATTACK] Intercepted Link | QBER: 32.49%
-> Security Alert: 🚨 CRITICAL TIME ATTACK DETECTED


--- PROTOCOL UNDER TEST: E91 (ENTANGLEMENT-BASED) ---
================ MONITORING FIBER LINK: 10.0 KM ================
[No Attack] Natural Channel Noise: 4.69% | QBER: 5.7% | CHSH S-Value: 2.61
-> Security Alert: ✅ LINE SECURE
[RED TEAM ATTACK] Intercepted Link | QBER: 25.43% | CHSH S-Value: 1.21
-> Security Alert: 🚨 CRITICAL TIME ATTACK DETECTED

================ MONITORING FIBER LINK: 50.0 KM ================
[No Attack] Natural Channel Noise: 10.0% | QBER: 11.92% | CHSH S-Value: 2.57
-> Security Alert: ✅ LINE SECURE
[RED TEAM ATTACK] Intercepted Link | QBER: 30.88% | CHSH S-Value: 1.4
-> Security Alert: 🚨 CRITICAL TIME ATTACK DETECTED


================ TESTING ADVANCED STEALTH THREAT ================
=== SCENARIO 3: Photon-Number-Splitting (PNS) Attack (50 KM) ===
[PNS ATTACK ACTIVE] Measured Channel QBER: 0.0% (Hacker successfully blinded standard filters)
[PNS ATTACK ACTIVE] Data Leaked to Red Team: 10.78% of the total key
[DECOY GUARD ACTIVE] Expected Decoy/Signal Ratio: 0.2109
[DECOY GUARD ACTIVE] Measured Decoy/Signal Ratio: 0.0888
[DECOY GUARD ACTIVE] Statistical Anomaly Detected: 57.89%
-> Security Alert: 🚨 CRITICAL PNS STEALTH ATTACK DETECTED BY DECOY DEFENSE!

================================================================
```

---

## 💻 Local Installation (Development Mode)

To set up the framework as a local, fully editable Python package on your system, navigate to the root directory and execute:

```bash
pip install -e .
```

---

## 🛠️ API Reference & Custom Usage

Software engineers and quantum researchers can import specific sub-modules into their custom projects to benchmark networks with custom parameters.

### 1. Simulating Custom Quantum Channels (BB84, B92, E91)
You can instantiate custom simulation benchmarks by defining the transmission length and the quantum bit volume.

```python
import qkd_redteam_core as qkd

# --- BB84 Example ---
bb84_engine = qkd.BB84RedTeamEngine(num_bits=5000, distance_km=45.5)
bb84_report = bb84_engine.run_simulation(attack_enabled=True)
print(f"BB84 Attack Detected: {bb84_report['attack_detected']}")

# --- B92 Example (Anti-Correlation Logic) ---
b92_engine = qkd.B92RedTeamEngine(num_bits=3000, distance_km=25.0)
b92_report = b92_engine.run_simulation(attack_enabled=False)
print(f"B92 Clean Channel QBER: {b92_report['qber_percentage']}%")

# --- E91 Example (Entanglement Based) ---
e91_engine = qkd.E91RedTeamEngine(num_bits=2000, distance_km=50.0)
e91_report = e91_engine.run_simulation(attack_enabled=True)
print(f"E91 CHSH S-Value: {e91_report['chsh_s_value']} (Broken if < 2.0)")
```

#### Engine Configurable Parameters:
- `num_bits` *(int, default=1000)*: Number of quantum pulses/EPR pairs simulated.
- `distance_km` *(float, default=25.0)*: Evaluates environmental signal loss and decoherence based on physical distance.

---

### 2. Threat & Defense Custom Intersections
You can dynamically modify the laser source intensity and integrate decoy audit structures to verify hardware vulnerability tolerances.

```python
from qkd_redteam_core.attack_models import QuantumAttackModels
from qkd_redteam_core.defense_models import QuantumDefenseModels

# Initialize threat suite with a custom laser source intensity
attack_suite = QuantumAttackModels(mu_intensity=0.20)

# Initialize defense suite with custom Signal and Decoy mean photon values
defense_suite = QuantumDefenseModels(signal_intensity=0.6, decoy_intensity=0.1)

# Audit channel statistics against active PNS threats
decoy_report = defense_suite.verify_decoy_pulse_statistics(num_pulses=2000, attack_active=True)
print(f"Decoy Guard Alarm Status: {decoy_report['pns_stealth_detected']}")
```

#### Advanced Parameters:
- `mu_intensity` *(float, default=0.1)*: Laser mean photon pulse parameter. Higher intensity increases multi-photon availability for the Red Team.
- `decoy_intensity` *(float, default=0.1)*: Auditing pulse intensity used by the Blue Team to catch zero-footprint anomalies.

---

## ⚖️ License & Copyright

This project is officially licensed under the **Apache License 2.0**—providing embedded patent protection and corporate utility. 

Developed and Maintained by **Irem Sener**.
