# [Protocol] Implement E91 and CHSH evaluation in Rust

## Goal

Implement entangled-pair preparation, basis selection, key extraction, and CHSH
correlation analysis without substituting a synthetic random S value.

## Requirements

- Prepare a documented Bell state.
- Represent Alice and Bob measurement settings as physical angles/operators.
- Separate key-generation samples from Bell-test samples.
- Compute correlators from observed joint outcomes.
- Derive the CHSH S value from those correlators.

## Acceptance criteria

- [ ] Bell-state preparation is verified by a reference state test.
- [ ] Measurement-angle conventions are documented and unit tested.
- [ ] CHSH correlators are calculated from raw counts.
- [ ] Ideal simulation approaches the expected quantum bound statistically.
- [ ] Separable or attacked fixtures remain at or below the classical bound.
- [ ] QBER and CHSH decisions include sample counts and uncertainty.
- [ ] No random value is injected directly as the CHSH result.
- [ ] The protocol runs through the common backend interface.

## Dependencies

- [#4](004-safe-qiskit-c-api-wrappers.md)
- [#5](005-hardware-calibrated-quantum-experiment-model.md)
- [#6](006-pluggable-quantum-execution-backend.md)

## Labels

`protocol:e91`, `rust`, `qiskit`, `chsh`
