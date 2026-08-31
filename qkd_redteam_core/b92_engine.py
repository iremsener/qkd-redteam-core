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

class B92RedTeamEngine:
    """
    Pure-Python and NumPy-based B92 Quantum Key Distribution (QKD)
    Security and Threat Simulation Engine. Pure quantum optical logic implemented.
    """
    def __init__(self, num_bits=1000, distance_km=25.0):
        self.num_bits = num_bits
        self.distance_km = distance_km
        self.attenuation_coeff = 0.2  # 0.2 dB/km standard fiber loss
        self.base_noise = 0.01        # 1% intrinsic error baseline

    def calculate_channel_noise(self):
        """
        Models physical layer drift over fiber optic links for B92.
        """
        loss_probability = 1 - (10 ** (-(self.attenuation_coeff * self.distance_km) / 10))
        total_noise = self.base_noise + (loss_probability * 0.15)
        return min(total_noise, 0.5)

    def run_simulation(self, attack_enabled=False):
        """
        Simulates the B92 protocol under active Intercept-Resend threats.
        Alice: Bit 0 -> Rectilinear Rectangular, Bit 1 -> Diagonal State.
        Bob: Measures randomly in Rectilinear or Diagonal.
        """
        channel_noise_rate = self.calculate_channel_noise()

        # 1. Alice prepares random bits (0 or 1)
        alice_bits = np.random.randint(2, size=self.num_bits)

        # 2. Bob prepares random measurement bases (0: Rectilinear, 1: Diagonal)
        bob_bases = np.random.randint(2, size=self.num_bits)
        
        # Arrays to record Bob's final filtered outcomes
        bob_bits = np.zeros(self.num_bits, dtype=int)
        bob_detected = np.zeros(self.num_bits, dtype=bool)

        # 3. Quantum Channel & Attack Simulation
        for i in range(self.num_bits):
            current_bit = alice_bits[i]
            
            # Environmental physical noise impact on the flying photon
            if np.random.rand() < channel_noise_rate:
                current_bit = 1 - current_bit

            if attack_enabled:
                # Intercept-Resend: Eve intercepts and projects onto a random basis
                eve_basis = np.random.randint(2)
                if eve_basis != current_bit:  # Mismatched projection causes 50% collapse
                    current_bit = np.random.randint(2)

            # 4. Bob's Quantum Detection Logic
            # In B92, Bob obtains a deterministic detection ONLY when his basis 
            # is DIFFERENT from Alice's bit value (basis), and he measures the dark port.
            if bob_bases[i] != current_bit:
                # With a clean photon, Bob definitely registers a projection
                if np.random.rand() > 0.5: # 50% intrinsic projection probability in B92
                    bob_detected[i] = True
                    bob_bits[i] = bob_bases[i] # Bob's bit is his own basis choice

        # 5. Sifting Process: Keep bits only where Bob successfully registered a click
        alice_sifted = alice_bits[bob_detected]
        bob_sifted = bob_bits[bob_detected]

        # 6. QBER Evaluation
        # In B92 quantum mechanics, if Alice sent 0, Bob detected on 1 basis -> bob_bits[i]=1.
        # Therefore, clean sifted keys are strictly anti-correlated (alice_bits == 1 - bob_bits).
        if len(alice_sifted) > 0:
            # An error occurs if Alice's bit is EQUAL to Bob's detected basis choice
            errors = np.sum(alice_sifted == bob_sifted)
            qber = (errors / len(alice_sifted)) * 100
        else:
            qber = 0.0

        return {
            "distance_km": self.distance_km,
            "channel_noise_percentage": round(channel_noise_rate * 100, 2),
            "sifted_key_length": len(alice_sifted),
            "qber_percentage": round(qber, 2),
            "attack_detected": qber > (11.0 + (channel_noise_rate * 100)) # Dynamic protection line
        }


