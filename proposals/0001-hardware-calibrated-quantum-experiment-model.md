# Proposal 0001: Hardware-Calibrated Quantum Experiment Model

- Status: Draft
- Target: Rust QKD core and Qiskit integration
- Related issue: [`Issue 005`](../issues/005-hardware-calibrated-quantum-experiment-model.md)

## Summary

Introduce a protocol-neutral experiment model that separates:

1. protocol intent;
2. physical apparatus;
3. measured calibration data;
4. numerical solution strategy;
5. execution backend;
6. observations and derived security metrics.

The Rust core owns these contracts. Qiskit, Qiskit Aer, native solvers, and
laboratory systems integrate through adapters rather than leaking their types
into the domain model.

## Motivation

The existing engines use NumPy sampling and a scalar distance-dependent noise
rate. That implementation is useful for demonstrations, but it conflates
physical evolution, measurement, and security analysis.

The new model must support both gate-level quantum channels and optical QKD
effects. These are related but not interchangeable. A Kraus channel can model a
CPTP transformation

\[
\mathcal{E}(\rho) = \sum_k K_k \rho K_k^\dagger,
\]

with

\[
\sum_k K_k^\dagger K_k = I,
\]

while photon emission, loss, detector dead time, and afterpulsing require an
event-based model with history.

## Design principles

- Keep Qiskit types outside `qkd-core`.
- Represent measured values with units, uncertainty, and provenance.
- Separate physical models from numerical solvers.
- Reject unsupported combinations instead of applying silent approximations.
- Make seeded runs reproducible under parallel execution.
- Preserve raw observations alongside derived metrics.
- Use exact small-system solvers as validation oracles.
- Treat laboratory data as versioned input, not hard-coded constants.

## Conceptual architecture

```text
ProtocolSpec ───────┐
ApparatusSpec ──────┼──> ValidatedExperiment ──> ExperimentBackend
CalibrationSnapshot┤                              ├── QiskitBackend
ExecutionSpec ──────┘                              ├── DensityMatrixBackend
                                                   ├── TrajectoryBackend
                                                   ├── PhotonicBackend
                                                   └── LaboratoryBackend
                                                              │
                                                              ▼
                                                      ExperimentResult
```

## Proposed Rust workspace placement

```text
rust/qkd-core/src/
├── experiment.rs
├── protocol/
├── physics/
│   ├── source.rs
│   ├── channel.rs
│   ├── kraus.rs
│   ├── lindblad.rs
│   └── detector.rs
├── calibration.rs
├── solver/
│   ├── density_matrix.rs
│   ├── trajectories.rs
│   └── photonic_events.rs
├── metrics.rs
└── result.rs
```

## Core contracts

```rust
pub struct ExperimentSpec {
    pub schema_version: String,
    pub protocol: ProtocolSpec,
    pub apparatus: ApparatusSpec,
    pub execution: ExecutionSpec,
    pub calibration: CalibrationReference,
}

pub struct ApparatusSpec {
    pub source: SourceModel,
    pub channel: Vec<ChannelComponent>,
    pub detectors: DetectorArray,
}

pub struct ExecutionSpec {
    pub solver: SolverSpec,
    pub root_seed: u64,
    pub parallelism: usize,
}

pub enum SolverSpec {
    CircuitShots {
        shots: u64,
    },
    ExactDensityMatrix {
        absolute_tolerance: f64,
    },
    QuantumTrajectories {
        trajectories: u64,
        time_step_seconds: f64,
    },
    PhotonicEvents {
        pulses: u64,
    },
}

pub trait ExperimentBackend {
    type Error;

    fn validate(
        &self,
        experiment: &ExperimentSpec,
    ) -> Result<ValidationReport, Self::Error>;

    fn run(
        &self,
        experiment: &ExperimentSpec,
    ) -> Result<ExperimentResult, Self::Error>;
}
```

These contracts describe intent. Matrix storage, ODE integration, Qiskit FFI,
and device communication remain private implementation details.

## Source model

`SourceModel` must initially support:

- `IdealSinglePhoton`;
- `WeakCoherentPulse` with mean photon number, repetition rate, and phase policy;
- `EntangledPairSource` with pair and multi-pair generation probabilities;
- `RecordedSource` referencing measured events or histograms.

Weak coherent pulses use a Poisson photon-number distribution. The generated
photon count must remain available in event metadata so PNS and decoy-state
models can operate without reconstructing hidden state.

## Channel model

`ChannelComponent` represents an ordered channel pipeline. Initial components:

- unitary polarization rotation;
- depolarizing, phase-damping, and amplitude-damping channels;
- thermal relaxation derived from `T1`, `T2`, and elapsed time;
- arbitrary Kraus operators;
- Hamiltonian and Lindblad collapse operators;
- fiber attenuation;
- polarization drift and crosstalk;
- erasure and explicit vacuum-state loss;
- background photon events.

The model must retain a distinction between:

- state transformations;
- loss/erasure;
- classical event generation;
- time-dependent, history-dependent behavior.

## Lindblad and MCWF model

Markovian open-system evolution follows

\[
\dot{\rho} = -\frac{i}{\hbar}[H, \rho]
+ \sum_j \left(
    C_j \rho C_j^\dagger
    - \frac{1}{2}\{C_j^\dagger C_j, \rho\}
  \right).
\]

The exact density-matrix solver is the reference for small systems. The MCWF
solver evolves pure states with an effective non-Hermitian Hamiltonian and
samples jumps from the collapse operators. Averaging independent trajectories
must converge to the density-matrix reference within a reported statistical
tolerance.

Trajectory results must report:

- requested and completed trajectory counts;
- jump counts by collapse operator;
- sample mean and standard error;
- confidence interval method and level;
- convergence or early-stop criteria;
- RNG stream identifiers.

## Detector model

`DetectorArray` must support per-detector values for:

- quantum efficiency;
- dark-count rate;
- detection window and timing jitter;
- dead time and recovery behavior;
- afterpulse probability and decay;
- basis-dependent efficiency;
- saturation threshold;
- photon-number resolution.

Dead time and afterpulsing depend on earlier events. Backends that only support
memoryless channels must reject these settings or use an explicitly selected
approximation recorded in the output.

## Calibration and provenance

```rust
pub struct CalibratedValue {
    pub value: f64,
    pub standard_uncertainty: Option<f64>,
    pub unit: String,
    pub measured_at: String,
    pub valid_until: Option<String>,
    pub method: Option<String>,
    pub instrument_id: Option<String>,
}
```

A `CalibrationSnapshot` contains:

- schema and calibration versions;
- laboratory and setup identifiers;
- measurement and validity timestamps;
- unit-checked parameter values;
- standard uncertainties;
- measurement methods;
- instrument identifiers;
- environmental metadata;
- raw-data URI or content checksum;
- operator and acquisition-software metadata.

The schema must use canonical units internally. Input units are converted during
validation, and incompatible dimensions are rejected.

## Reproducible randomness

One root seed deterministically derives independent streams for:

- source emission;
- channel evolution;
- detector events;
- basis selection;
- attack behavior;
- numerical solver sampling.

Stream derivation must use stable domain labels. Results may not depend on task
scheduling or worker count.

## Backend capabilities

Each backend publishes machine-readable capabilities, including:

- supported state and channel representations;
- maximum qubit or Hilbert-space dimensions;
- time-dependent dynamics support;
- history-dependent detector support;
- supported noise models;
- gradient or parameter-sweep support;
- hardware execution support.

Validation produces a report before execution. A backend cannot silently drop
unsupported fields.

## Qiskit mapping

The Qiskit adapter maps supported domain values to Qiskit constructs:

| Domain model | Qiskit representation |
|---|---|
| Unitary channel | Circuit unitary or standard gate |
| Kraus channel | `Kraus` / Aer `kraus_error` |
| Depolarizing channel | Aer `depolarizing_error` |
| Amplitude/phase damping | Corresponding Aer quantum error |
| Thermal relaxation | Aer `thermal_relaxation_error` |
| Readout confusion | Aer `ReadoutError` |
| Circuit shots | Sampler or simulator execution |

Photonic source emission, vacuum loss, dead time, and afterpulsing remain in the
Rust event model unless a selected backend explicitly supports them.

The direct Qiskit C API and the Python/Aer adapter can expose different
capabilities. Both must implement the same backend contract and report their
limitations.

## Result model

`ExperimentResult` preserves both observations and analysis:

- raw counts or event summaries;
- sifted-key length, gain, yield, and QBER;
- CHSH correlators and S value;
- source, loss, and detector statistics;
- decoy-state and leakage estimates;
- solver/backend identity and version;
- seeds and stochastic sample counts;
- confidence intervals and standard errors;
- calibration snapshot identity;
- applied approximations and warnings;
- wall-clock and simulation durations.

Security metrics are derived views over immutable observations so new analyses
can be added without rerunning an experiment.

## Validation strategy

### Analytical tests

- Identity channel preserves every test state.
- Amplitude damping matches its closed-form population decay.
- Kraus composition preserves CPTP constraints.
- Trace and positivity are maintained within declared tolerances.
- Thermal relaxation rejects `T2 > 2*T1`.

### Cross-solver tests

- MCWF averages converge to exact Lindblad results.
- Rust Kraus evolution matches Qiskit for fixed fixtures.
- Circuit-shot distributions match expected probabilities statistically.
- Photonic loss matches binomial/Poisson reference distributions.

### Laboratory validation

- Import an anonymized calibration snapshot.
- Simulate a fixed pulse count with recorded source and detector parameters.
- Compare detection rate, QBER, and timing histogram against measured data.
- Report residuals and uncertainty rather than a binary pass alone.

## Delivery plan

1. Approve schemas, physical boundaries, and backend capabilities.
2. Implement validation and the exact density-matrix reference path.
3. Implement Kraus composition and Qiskit parity tests.
4. Implement Lindblad and MCWF solvers.
5. Implement source/channel/detector event simulation.
6. Add calibration ingestion and laboratory fixtures.
7. Add Qiskit, Aer, and hardware adapters.
8. Establish performance and accuracy baselines.

## Open questions

- Should matrix dimensions initially be restricted to qubits, or support qudits?
- Is explicit vacuum-state evolution required for the first release?
- Which confidence-interval method is required for low-count measurements?
- Which calibration format is authoritative: JSON, YAML, or HDF5 plus metadata?
- Is non-Markovian evolution in the initial scope or a later extension?
- Which laboratory control system will provide the first real fixture?

## References

- [Qiskit Kraus representation](https://eu-de.quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.quantum_info.Kraus)
- [Qiskit Aer noise models](https://qiskit.github.io/qiskit-aer/tutorials/3_building_noise_models.html)
- [Qiskit Aer thermal relaxation constraints](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.noise.thermal_relaxation_error.html)
- [Monte Carlo wave-function method in quantum optics](https://opg.optica.org/josab/abstract.cfm?uri=josab-10-3-524)
- [QuTiP Lindblad solver formulation](https://github.com/qutip/qutip/blob/master/doc/guide/dynamics/dynamics-master.rst)
- [NIST quantum network detector metrology](https://www.nist.gov/pml/productsservices/quantum-networks-nist/quantum-network-metrology)
