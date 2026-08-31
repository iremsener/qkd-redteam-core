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

class QuantumDefenseModels:
    """
    Advanced Countermeasure and Defense Protocols for QKD Networks.
    Provides implementations for anomaly detection and stealth attack mitigations.
    """
    def __init__(self, signal_intensity=0.6, decoy_intensity=0.1):
        """
        signal_intensity (mu): Mean photon number for raw key generation pulses.
        decoy_intensity (nu): Lower mean photon number for decoy validation pulses.
        """
        self.mu = signal_intensity
        self.nu = decoy_intensity

    def verify_decoy_pulse_statistics(self, num_pulses, attack_active=False):
        """
        Simulates the Decoy State protocol countermeasure against PNS attacks.
        Alice intersperses weaker decoy states to audit the channel transmission statistics.
        """
        # Determine total types of pulses allocated (e.g., 80% signal, 20% decoy)
        is_decoy = np.random.rand(num_pulses) < 0.20
        
        # Calculate theoretical expected transmission rates based on photon distributions
        expected_signal_yield = 1.0 - np.exp(-self.mu)
        expected_decoy_yield = 1.0 - np.exp(-self.nu)
        
        # Simulated actual detection yields received by Bob
        if attack_active:
            # Under a PNS attack, Eve selectively suppresses/filters weaker pulses 
            # to hide her multi-photon splitting on the stronger signal pulses.
            # This skews the decoy yield ratio catastrophically.
            actual_signal_yield = expected_signal_yield * 0.95 # slight loss
            actual_decoy_yield = expected_decoy_yield * 0.40   # massive drop due to Eve's filtering
        else:
            # Clean channel baseline with standard physical layer entropy
            actual_signal_yield = expected_signal_yield * (1.0 - np.random.normal(0.02, 0.005))
            actual_decoy_yield = expected_decoy_yield * (1.0 - np.random.normal(0.02, 0.005))

        # Calculate the dynamic yield ratio metric
        measured_ratio = actual_decoy_yield / actual_signal_yield
        expected_ratio = expected_decoy_yield / expected_signal_yield
        
        # Statistical anomaly deviation percentage
        statistical_deviation = abs(expected_ratio - measured_ratio) / expected_ratio * 100
        
        # If the statistical transmission yield of decoys drops by more than 15%, 
        # a high-fidelity stealth attack anomaly is validated.
        pns_stealth_detected = statistical_deviation > 15.0

        return {
            "expected_decoy_to_signal_ratio": round(expected_ratio, 4),
            "measured_decoy_to_signal_ratio": round(measured_ratio, 4),
            "statistical_anomaly_percentage": round(statistical_deviation, 2),
            "pns_stealth_detected": pns_stealth_detected
        }
