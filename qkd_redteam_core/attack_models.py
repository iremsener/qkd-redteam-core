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

class QuantumAttackModels:
    """
    Advanced Adversarial Threat Simulation Models for Quantum Networks.
    Provides implementations for sophisticated quantum attack vectors.
    """
    def __init__(self, mu_intensity=0.1):
        """
        mu_intensity: Mean photon number per pulse (Laser intensity parameter).
                      Usually set very low (e.g., 0.1 to 0.5) to avoid multi-photon pulses.
        """
        self.mu = mu_intensity

    def simulate_pns_attack(self, alice_bits, alice_bases, bob_bases):
        """
        Simulates the highly stealthy Photon-Number-Splitting (PNS) attack.
        Eve exploits multi-photon pulses generated based on Poisson distribution.
        
        Returns:
            bob_bits: The bits Bob measures after Eve's selection.
            eve_leaked_info_rate: Percentage of key leaked to Eve without changing QBER.
        """
        num_bits = len(alice_bits)
        bob_bits = np.zeros(num_bits, dtype=int)
        eve_stolen_bits = {} # Eve stores the bits she safely extracted
        
        # Simulated Poisson photon distribution probabilities for given mu intensity
        # P(n=1) vs P(n>=2)
        prob_single_photon = self.mu * np.exp(-self.mu)
        prob_multi_photon = 1 - np.exp(-self.mu) - prob_single_photon
        
        # Normalize probabilities for simulation
        total_prob = prob_single_photon + prob_multi_photon
        p_single = prob_single_photon / total_prob

        for i in range(num_bits):
            current_bit = alice_bits[i]
            current_basis = alice_bases[i]
            
            # Decide if this pulse contains 1 photon or multi-photons based on laser intensity
            is_multi_photon = np.random.rand() > p_single
            
            if is_multi_photon:
                # PNS STRATEGY: Eve splits one photon for herself, stores it,
                # and passes the remaining undisturbed photon to Bob.
                # Eve creates ZERO disturbance (0% QBER contribution here)
                eve_stolen_bits[i] = (current_bit, current_basis)
                bob_measured_bit = current_bit
            else:
                # Single photon pulse: Eve skips to avoid detection (or Bob just measures it)
                bob_measured_bit = current_bit

            # Bob measures what arrived
            if bob_bases[i] == current_basis:
                bob_bits[i] = bob_measured_bit
            else:
                bob_bits[i] = np.random.randint(2)

        # Calculate how much information Eve successfully stole after basis reconciliation
        stolen_count = 0
        matching_bases_count = 0
        
        for i in range(num_bits):
            if alice_bases[i] == bob_bases[i]:
                matching_bases_count += 1
                if i in eve_stolen_bits:
                    stolen_count += 1
                    
        leakage_rate = (stolen_count / matching_bases_count * 100) if matching_bases_count > 0 else 0.0

        return bob_bits, round(leakage_rate, 2)

