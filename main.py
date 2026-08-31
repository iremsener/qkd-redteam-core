# Copyright 2026 Irem Sener
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://apache.org
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from qkd_redteam_core.bb84_engine import BB84RedTeamEngine
from qkd_redteam_core.b92_engine import B92RedTeamEngine
from qkd_redteam_core.e91_engine import E91RedTeamEngine
from qkd_redteam_core.attack_models import QuantumAttackModels
from qkd_redteam_core.defense_models import QuantumDefenseModels

if __name__ == "__main__":
    print("================================================================")
    print("===       QUANTUM RED TEAM CORE CENTRAL SECURITY SUITE       ===")
    print("================================================================\n")
    
    test_distances = [10.0, 50.0]

    # =========================================================================
    # PART 1: BB84 PROTOCOL BENCHMARKS
    # =========================================================================
    print("--- PROTOCOL UNDER TEST: BB84 (4-STATE) ---")
    for dist in test_distances:
        print(f"================ MONITORING FIBER LINK: {dist} KM ================")
        bb84_engine = BB84RedTeamEngine(num_bits=1000, distance_km=dist)
        clean = bb84_engine.run_simulation(attack_enabled=False)
        print(f"[No Attack] Natural Channel Noise: {clean['channel_noise_percentage']}% | QBER: {clean['qber_percentage']}%")
        print(f"-> Security Alert: {'🚨 CRITICAL TIME ATTACK DETECTED' if clean['attack_detected'] else '✅ LINE SECURE'}")
        
        attacked = bb84_engine.run_simulation(attack_enabled=True)
        print(f"[RED TEAM ATTACK] Intercepted Link | QBER: {attacked['qber_percentage']}%")
        print(f"-> Security Alert: {'🚨 CRITICAL TIME ATTACK DETECTED' if attacked['attack_detected'] else '✅ LINE SECURE'}\n")

    # =========================================================================
    # PART 2: B92 PROTOCOL BENCHMARKS
    # =========================================================================
    print("\n--- PROTOCOL UNDER TEST: B92 (2-STATE) ---")
    for dist in test_distances:
        print(f"================ MONITORING FIBER LINK: {dist} KM ================")
        b92_engine = B92RedTeamEngine(num_bits=1000, distance_km=dist)
        clean_b92 = b92_engine.run_simulation(attack_enabled=False)
        print(f"[No Attack] Natural Channel Noise: {clean_b92['channel_noise_percentage']}% | QBER: {clean_b92['qber_percentage']}%")
        print(f"-> Security Alert: {'🚨 CRITICAL TIME ATTACK DETECTED' if clean_b92['attack_detected'] else '✅ LINE SECURE'}")
        
        attacked_b92 = b92_engine.run_simulation(attack_enabled=True)
        print(f"[RED TEAM ATTACK] Intercepted Link | QBER: {attacked_b92['qber_percentage']}%")
        print(f"-> Security Alert: {'🚨 CRITICAL TIME ATTACK DETECTED' if attacked_b92['attack_detected'] else '✅ LINE SECURE'}\n")

    # =========================================================================
    # PART 3: E91 PROTOCOL BENCHMARKS (ENTANGLEMENT-BASED)
    # =========================================================================
    print("\n--- PROTOCOL UNDER TEST: E91 (ENTANGLEMENT-BASED) ---")
    for dist in test_distances:
        print(f"================ MONITORING FIBER LINK: {dist} KM ================")
        e91_engine = E91RedTeamEngine(num_bits=1000, distance_km=dist)
        clean_e91 = e91_engine.run_simulation(attack_enabled=False)
        print(f"[No Attack] Natural Channel Noise: {clean_e91['channel_noise_percentage']}% | QBER: {clean_e91['qber_percentage']}% | CHSH S-Value: {clean_e91['chsh_s_value']}")
        print(f"-> Security Alert: {'🚨 CRITICAL TIME ATTACK DETECTED' if clean_e91['attack_detected'] else '✅ LINE SECURE'}")
        
        attacked_e91 = e91_engine.run_simulation(attack_enabled=True)
        print(f"[RED TEAM ATTACK] Intercepted Link | QBER: {attacked_e91['qber_percentage']}% | CHSH S-Value: {attacked_e91['chsh_s_value']}")
        print(f"-> Security Alert: {'🚨 CRITICAL TIME ATTACK DETECTED' if attacked_e91['attack_detected'] else '✅ LINE SECURE'}\n")

    # =========================================================================
    # PART 4: ADVANCED STEALTH THREAT & DECOY STATE MITIGATION
    # =========================================================================
    print("\n================ TESTING ADVANCED STEALTH THREAT ================")
    print("=== SCENARIO 3: Photon-Number-Splitting (PNS) Attack (50 KM) ===")
    
    bb84_sim = BB84RedTeamEngine(num_bits=2000, distance_km=50.0)
    attack_suite = QuantumAttackModels(mu_intensity=0.2)
    defense_suite = QuantumDefenseModels(signal_intensity=0.6, decoy_intensity=0.1)
    
    alice_bits = np.random.randint(2, size=bb84_sim.num_bits)
    alice_bases = np.random.randint(2, size=bb84_sim.num_bits)
    bob_bases = np.random.randint(2, size=bb84_sim.num_bits)
    
    bob_bits, leakage_rate = attack_suite.simulate_pns_attack(alice_bits, alice_bases, bob_bases)
    
    matching_bases = (alice_bases == bob_bases)
    alice_sifted = alice_bits[matching_bases]
    bob_sifted = bob_bits[matching_bases]
    
    pns_qber = (np.sum(alice_sifted != bob_sifted) / len(alice_sifted) * 100) if len(alice_sifted) > 0 else 0.0
    
    # Trigger the automated Decoy State statistical audit
    decoy_report = defense_suite.verify_decoy_pulse_statistics(num_pulses=2000, attack_active=True)
    
    print(f"[PNS ATTACK ACTIVE] Measured Channel QBER: {round(pns_qber, 2)}% (Hacker successfully blinded standard filters)")
    print(f"[PNS ATTACK ACTIVE] Data Leaked to Red Team: {leakage_rate}% of the total key")
    print(f"[DECOY GUARD ACTIVE] Expected Decoy/Signal Ratio: {decoy_report['expected_decoy_to_signal_ratio']}")
    print(f"[DECOY GUARD ACTIVE] Measured Decoy/Signal Ratio: {decoy_report['measured_decoy_to_signal_ratio']}")
    print(f"[DECOY GUARD ACTIVE] Statistical Anomaly Detected: {decoy_report['statistical_anomaly_percentage']}%")
    
    # Master decision matrix combining standard QBER and the new Decoy Audit
    final_alert = decoy_report['pns_stealth_detected'] or pns_qber > 14.5
    print(f"-> Security Alert: {'🚨 CRITICAL PNS STEALTH ATTACK DETECTED BY DECOY DEFENSE!' if final_alert else '✅ LINE SECURE'}")
    print("\n================================================================")

