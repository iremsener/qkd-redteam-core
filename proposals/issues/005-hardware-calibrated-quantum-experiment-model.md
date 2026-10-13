# [RFC/Core Physics] Define a hardware-calibrated stochastic quantum experiment model

## Problem

The current Python engines reduce distance-dependent channel noise to a single
bit-flip probability. This abstraction cannot accurately represent:

- Kraus/CPTP quantum channels;
- Lindblad open-system dynamics;
- Monte Carlo wave-function (MCWF) trajectories;
- photon loss and photon-number statistics;
- detector efficiency, dark counts, timing jitter, afterpulsing, and dead time;
- measured laboratory calibration data.

Three distinct stochastic processes must not be combined under one generic
`MonteCarloConfig`:

1. circuit-shot sampling of measurement outcomes;
2. MCWF quantum trajectories for Lindblad dynamics;
3. photonic event Monte Carlo for sources, channels, and detectors.

## Goal

Define a versioned experiment contract that separates protocol intent,
physical apparatus, calibration data, numerical solver, and execution backend.
The contract must be implementable in Rust and portable across Qiskit,
local simulators, and physical laboratory backends.

## Scope

- BB84, B92, and E91 experiment definitions
- Kraus/CPTP channels
- Lindblad/GKSL dynamics
- MCWF/quantum trajectory execution
- shot-based circuit execution
- photonic event Monte Carlo
- source, fiber, and detector models
- laboratory calibration snapshots
- reproducibility and uncertainty reporting
- Qiskit and Qiskit Aer adapters

## Non-goals

- Implement every production solver in this issue
- Reimplement Qiskit or QuTiP
- Provide formal QKD security proofs
- Complete finite-key security analysis
- Implement vendor-specific laboratory drivers

## Deliverables

- `ExperimentSpec` and `ExperimentResult` domain contracts
- A versioned JSON Schema for configuration and results
- A calibration snapshot format with units, uncertainty, and provenance
- Capability contracts for execution backends
- Validation rules for supported physical models
- Reference fixtures for simulated and laboratory-derived configurations
- The design described in
  [`docs/proposals/0001-hardware-calibrated-quantum-experiment-model.md`](../proposals/0001-hardware-calibrated-quantum-experiment-model.md)

## Required physical models

### Sources

- Ideal single-photon source
- Weak coherent pulse source with Poisson photon-number sampling
- Entangled-pair source
- Recorded laboratory source data

### Channels

- Unitary polarization rotation
- Depolarizing channel
- Phase and amplitude damping
- Thermal relaxation
- User-defined Kraus operators
- Lindblad Hamiltonian and collapse operators
- Fiber attenuation and erasure
- Polarization drift and crosstalk
- Background photons

Photon loss must not be represented as a bit flip. It must be modeled either as
an explicit vacuum state or as a photonic loss/erasure event.

### Detectors

- Detection efficiency
- Dark-count rate
- Timing jitter and detection window
- Dead time and recovery
- Afterpulse probability
- Basis-dependent efficiency
- Saturation
- Number-resolving and non-resolving modes

## Validation requirements

- Kraus matrix dimensions are consistent.
- CPTP models satisfy `sum(K_i^dagger K_i) ~= I` within configured tolerances.
- Density matrices are Hermitian, positive semidefinite, and trace one.
- Lindblad Hamiltonian and collapse operators have compatible dimensions.
- Thermal relaxation parameters satisfy `T2 <= 2*T1`.
- Probabilities remain in `[0, 1]`.
- Durations and rates are non-negative.
- History-dependent detector effects cannot use a memoryless solver silently.
- Unsupported model/backend combinations return explicit capability errors.
- Every approximation is included in result metadata.

## Result requirements

Results must include, where applicable:

- raw counts or event summary;
- sifted-key length, gain, yield, and QBER;
- CHSH correlators and S value;
- photon-loss and dark-count contributions;
- detection probability and leakage estimate;
- decoy-state statistics;
- solver name and version;
- RNG algorithm, root seed, and derived stream identifiers;
- trajectory, shot, or pulse count;
- confidence intervals and standard errors;
- calibration snapshot identifier;
- approximation and warning lists;
- execution duration.

## Reproducibility requirements

Independent deterministic RNG streams must be derived from one root seed for:

- source generation;
- channel evolution;
- detector events;
- basis selection;
- attack behavior;
- solver sampling.

Parallel execution must not change results because of thread scheduling.

## Acceptance criteria

- [ ] The proposal is reviewed and accepted before production solver work starts.
- [ ] Rust domain types compile without Python or Qiskit dependencies.
- [ ] `ExperimentSpec` and `ExperimentResult` have versioned JSON Schemas.
- [ ] Solver, physics model, calibration, and backend modules are independent.
- [ ] Kraus completeness and CPTP validation are implemented.
- [ ] Lindblad operator and dimension validation are implemented.
- [ ] Exact density-matrix and MCWF solvers share one result contract.
- [ ] Photonic event simulation is distinct from circuit-shot sampling.
- [ ] Fiber and detector loss are not reduced to bit flips.
- [ ] Fixed seeds produce repeatable results under parallel execution.
- [ ] Amplitude-damping output matches an analytical reference case.
- [ ] MCWF averages converge to the exact Lindblad reference within a declared tolerance.
- [ ] Supported models can be mapped to a Qiskit Aer `NoiseModel`.
- [ ] An anonymized laboratory calibration fixture is included.
- [ ] Unsupported models fail with explicit, test-covered errors.

## Follow-up issues

1. Implement versioned experiment and calibration schemas.
2. Implement Kraus channel validation and composition.
3. Implement the exact density-matrix reference solver.
4. Implement Lindblad dynamics and the MCWF trajectory solver.
5. Implement weak-coherent-source and fiber-loss event models.
6. Implement a history-dependent single-photon detector model.
7. Map supported models to Qiskit Aer noise models.
8. Build laboratory calibration ingestion and validation.
9. Add analytical, Qiskit parity, and laboratory validation tests.

## References

- [Qiskit Kraus representation](https://eu-de.quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.quantum_info.Kraus)
- [Qiskit Aer noise models](https://qiskit.github.io/qiskit-aer/tutorials/3_building_noise_models.html)
- [Qiskit Aer thermal relaxation constraints](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.noise.thermal_relaxation_error.html)
- [Monte Carlo wave-function method in quantum optics](https://opg.optica.org/josab/abstract.cfm?uri=josab-10-3-524)
- [QuTiP Lindblad solver formulation](https://github.com/qutip/qutip/blob/master/doc/guide/dynamics/dynamics-master.rst)
- [NIST quantum network detector metrology](https://www.nist.gov/pml/productsservices/quantum-networks-nist/quantum-network-metrology)
