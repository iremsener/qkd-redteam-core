# [Python] Expose the Rust engine through PyO3 and maturin

## Goal

Make the Rust engine available to Python users while preserving the current
package's public behavior during migration.

## Compatibility targets

- `BB84RedTeamEngine`
- `B92RedTeamEngine`
- `E91RedTeamEngine`
- `QuantumAttackModels`
- `QuantumDefenseModels`

## Acceptance criteria

- [ ] The Rust extension builds through maturin on supported Python versions.
- [ ] Existing public classes remain importable or have documented shims.
- [ ] Existing constructor defaults remain compatible unless explicitly deprecated.
- [ ] Existing result keys are preserved during the transition.
- [ ] New typed configuration APIs are exposed without breaking simple usage.
- [ ] Rust errors map to meaningful Python exceptions.
- [ ] Rust panics cannot cross the Python FFI boundary.
- [ ] NumPy conversion avoids copies where ownership and layout permit it.
- [ ] Editable installation and wheel installation both pass smoke tests.

## Dependencies

- [#7](007-bb84-circuit-generation-in-rust.md)
- [#8](008-b92-circuit-generation-in-rust.md)
- [#9](009-e91-and-chsh-in-rust.md)
- [#10](010-intercept-resend-attack.md)
- [#11](011-channel-and-detector-noise.md)
- [#12](012-pns-and-decoy-state-hybrid-model.md)

## Labels

`python`, `pyo3`, `maturin`, `compatibility`
