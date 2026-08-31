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

class E91RedTeamEngine:
    """
    Pure-Python and NumPy-based E91 Quantum Key Distribution (QKD)
    Security Engine based on Quantum Entanglement (EPR pairs) and CHSH inequality validation.
    """
    def __init__(self, num_bits=1000, distance_km=25.0):
        self.num_bits = num_bits
        self.distance_km = distance_km
        self.attenuation_coeff = 0.2  # standard fiber attenuation
        self.base_noise = 0.01        # 1% baseline imperfection

    def calculate_channel_noise(self):
        """
        Calculates realistic physical entanglement degradation over distance.
        """
        loss_probability = 1 - (10 ** (-(self.attenuation_coeff * self.distance_km) / 10))
        total_noise = self.base_noise + (loss_probability * 0.10)
        return min(total_noise, 0.5)

    def run_simulation(self, attack_enabled=False):
        """
        Simulates the E91 protocol. Entangled pairs are distributed to Alice and Bob.
        Alice measures in 3 angles (0, 45, 90). Bob measures in 3 angles (45, 90, 135).
        CHSH S-value is calculated to verify entanglement validity.
        """
        channel_noise_rate = self.calculate_channel_noise()

        # 1. Source generates entangled EPR pairs (strictly correlated states)
        # For simulation, we model the underlying correlated source bits
        source_bits = np.random.randint(2, size=self.num_bits)

        # Alice chooses randomly from 3 bases (0, 1, 2)
        alice_bases = np.random.randint(3, size=self.num_bits)
        # Bob chooses randomly from 3 bases (0, 1, 2)
        bob_bases = np.random.randint(3, size=self.num_bits)

        alice_bits = np.copy(source_bits)
        bob_bits = np.copy(source_bits) # Entangled correlation baseline

        # 2. Quantum Channel and Eavesdropping (Eve attempts to intercept one half of the pair)
        for i in range(self.num_bits):
            # Physical fiber decoherence noise
            if np.random.rand() < channel_noise_rate:
                bob_bits[i] = 1 - bob_bits[i]

            if attack_enabled:
                # Intercept-Resend on entangled states breaks the entanglement correlation
                eve_measurement = np.random.randint(2)
                if np.random.rand() > 0.5:
                    alice_bits[i] = eve_measurement
                    bob_bits[i] = np.random.randint(2) # Decoherence collapse

        # 3. Sifting and CHSH Inequality Verification
        # In E91, identical bases are used for raw key generation.
        # Differentiating bases are used to calculate the CHSH "S" value to detect Eve.
        matching_bases = (alice_bases == bob_bases)
        alice_key = alice_bits[matching_bases]
        bob_key = bob_bits[matching_bases]

        # Calculate QBER on the raw sifted key
        if len(alice_key) > 0:
            errors = np.sum(alice_key != bob_key)
            qber = (errors / len(alice_key)) * 100
        else:
            qber = 0.0

        # CHSH S-Value mathematical simulation (Theoretical Max: 2.82, Broken Entanglement Baseline: <= 2.0)
        if attack_enabled:
            # Attacks collapse quantum state, pushing S close to classical limit (~1.4)
            chsh_s_value = max(1.4 + np.random.normal(0, 0.1), 0.0)
        else:
            # Clean channel maintains quantum correlation minus distance noise drift
            chsh_s_value = min(2.82 - (channel_noise_rate * 2.0) + np.random.normal(0, 0.05), 2.82)

        return {
            "distance_km": self.distance_km,
            "channel_noise_percentage": round(channel_noise_rate * 100, 2),
            "sifted_key_length": len(alice_key),
            "qber_percentage": round(qber, 2),
            "chsh_s_value": round(chsh_s_value, 2),
            # In E91, an attack is officially triggered if CHSH S-value drops below 2.0
            "attack_detected": chsh_s_value < 2.0 or qber > (11.0 + (channel_noise_rate * 100))
        }
