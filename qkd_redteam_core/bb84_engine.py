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

class BB84RedTeamEngine:
    """
    Pure-Python and NumPy-based BB84 Quantum Key Distribution (QKD) 
    Security and Threat Simulation Engine .
    """
    def __init__(self, num_bits=1000, distance_km=25.0):
        self.num_bits = num_bits
        self.distance_km = distance_km
        
        # Standard fiber-optic attenuation coefficient (approx. 0.2 dB/km for 1550nm wavelength)
        self.attenuation_coeff = 0.2 
        
        # Detector intrinsic error rate (Dark Count Rate effect)
        self.base_noise = 0.01 

    def calculate_channel_noise(self):
        """
        Calculates realistic physical noise based on fiber-optic channel distance.
        Formula models photon loss and polarization drift over distance.
        """
        # Loss formula derived from fiber attenuation (dB to probability mapping)
        loss_probability = 1 - (10 ** (-(self.attenuation_coeff * self.distance_km) / 10))
        
        # Total environmental noise combining baseline imperfections and distance loss
        total_noise = self.base_noise + (loss_probability * 0.15)
        
        # Bound noise between 0% and 50% (maximum quantum entropy limit)
        return min(total_noise, 0.5)

    def run_simulation(self, attack_enabled=False):
        """
        Simulates the BB84 protocol under distance-based noise and active attacks.
        """
        # Calculate environmental channel noise for this distance
        channel_noise_rate = self.calculate_channel_noise()

        # 1. Alice prepares random bits and random bases (0: Z basis, 1: X basis)
        alice_bits = np.random.randint(2, size=self.num_bits)
        alice_bases = np.random.randint(2, size=self.num_bits)

        # 2. Allocate space for Bob and Eve
        bob_bits = np.zeros(self.num_bits, dtype=int)
        bob_bases = np.random.randint(2, size=self.num_bits)

        # 3. Quantum Channel & Attack Simulation
        for i in range(self.num_bits):
            current_bit = alice_bits[i]
            current_basis = alice_bases[i]

            # Simulate natural physical noise flipping the qubit state in transit
            if np.random.rand() < channel_noise_rate:
                current_bit = 1 - current_bit

            if attack_enabled:
                # RED TEAM PENETRATION TEST: Eve intercepts the qubit and measures
                eve_basis = np.random.randint(2)
                if eve_basis == current_basis:
                    eve_bit = current_bit
                else:
                    eve_bit = np.random.randint(2)
                current_bit = eve_bit

            # 4. Bob measures the qubit
            if bob_bases[i] == current_basis:
                if attack_enabled and eve_basis != current_basis:
                    bob_bits[i] = np.random.randint(2)
                else:
                    bob_bits[i] = current_bit
            else:
                bob_bits[i] = np.random.randint(2)

        # 5. Sifted Key Process
        matching_bases = (alice_bases == bob_bases)
        alice_sifted = alice_bits[matching_bases]
        bob_sifted = bob_bits[matching_bases]

        # 6. QBER Analysis
        if len(alice_sifted) > 0:
            errors = np.sum(alice_sifted != bob_sifted)
            qber = (errors / len(alice_sifted)) * 100
        else:
            qber = 0.0

        return {
            "distance_km": self.distance_km,
            "channel_noise_percentage": round(channel_noise_rate * 100, 2),
            "sifted_key_length": len(alice_sifted),
            "qber_percentage": round(qber, 2),
            "attack_detected": qber > (11.0 + (channel_noise_rate * 100)) # Dynamic adaptive threshold
        }
   