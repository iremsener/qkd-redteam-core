# [Protocol] Implement B92 circuit generation in Rust

## Goal

Implement B92 with explicit non-orthogonal state preparation, conclusive
measurement handling, sifting, and QBER analysis.

## Requirements

- Represent the two non-orthogonal signal states explicitly.
- Separate conclusive, inconclusive, lost, and invalid detector outcomes.
- Preserve anti-correlation semantics during sifting.
- Avoid treating inconclusive outcomes as ordinary bit errors.

## Acceptance criteria

- [ ] State-preparation circuits match the selected B92 convention.
- [ ] Ideal fixtures reproduce expected conclusive probabilities.
- [ ] Only conclusive outcomes enter the sifted key.
- [ ] Anti-correlated Alice/Bob values are interpreted correctly.
- [ ] Loss and detector effects remain distinct from logical errors.
- [ ] Seeded runs are reproducible.
- [ ] Rust and Python outputs agree within declared statistical tolerances.
- [ ] The implementation works with every backend advertising B92 support.

## Dependencies

- [#4](004-safe-qiskit-c-api-wrappers.md)
- [#5](005-hardware-calibrated-quantum-experiment-model.md)
- [#6](006-pluggable-quantum-execution-backend.md)

## Labels

`protocol:b92`, `rust`, `qiskit`
