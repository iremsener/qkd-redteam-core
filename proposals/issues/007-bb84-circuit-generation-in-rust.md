# [Protocol] Implement BB84 circuit generation in Rust

## Goal

Implement BB84 state preparation, measurement, sifting, and result analysis in
Rust using the protocol-neutral experiment and backend contracts.

## Requirements

- Generate Alice bits and Z/X bases from deterministic RNG streams.
- Prepare the corresponding quantum states.
- Generate Bob bases and apply the required basis rotations.
- Measure, reconcile bases, and sift the raw key.
- Calculate raw errors, QBER, yield, and detection decision.
- Preserve observations needed for later finite-key analysis.

## Acceptance criteria

- [ ] Ideal matching-basis fixtures return the expected bits.
- [ ] Mismatched bases show the expected statistical distribution.
- [ ] Identical root seeds reproduce inputs and outputs.
- [ ] Sifting excludes all non-matching bases.
- [ ] QBER is calculated from raw error counts without premature rounding.
- [ ] The implementation runs with both fake and selected Qiskit backends.
- [ ] Small circuits have stable snapshot or structural tests.
- [ ] Results remain compatible with the existing Python result contract.

## Dependencies

- [#4](004-safe-qiskit-c-api-wrappers.md)
- [#5](005-hardware-calibrated-quantum-experiment-model.md)
- [#6](006-pluggable-quantum-execution-backend.md)

## Labels

`protocol:bb84`, `rust`, `qiskit`
