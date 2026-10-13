# [Architecture] Introduce a pluggable quantum execution backend

## Problem

Circuit construction, numerical simulation, and hardware execution have
different capabilities. Tying protocols directly to Qiskit Aer or one local
solver would prevent laboratory and future backend integration.

## Goal

Define a capability-aware execution boundary that accepts validated experiment
specifications and returns backend-neutral observations.

## Required backends

- Deterministic test backend
- Exact density-matrix reference backend
- Qiskit-compatible circuit backend
- Extension points for MCWF, photonic events, and laboratory hardware

## Acceptance criteria

- [ ] An `ExperimentBackend` interface accepts a validated experiment.
- [ ] Backends publish machine-readable capabilities and limits.
- [ ] Inputs include solver settings, sample counts, seed, and physical model.
- [ ] Outputs preserve raw counts/events and execution metadata.
- [ ] Unsupported model/backend combinations fail before execution.
- [ ] Protocol code does not branch on concrete backend names.
- [ ] A deterministic fake backend verifies orchestration and error handling.
- [ ] Cancellation, timeout, and partial-result behavior are documented.

## Dependencies

- [#2](002-decide-rust-qiskit-integration-boundary.md)
- [#5](005-hardware-calibrated-quantum-experiment-model.md)

## Labels

`architecture`, `backend`, `simulation`, `rust`
