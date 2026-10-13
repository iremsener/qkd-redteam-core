# [EPIC] Rust-native Qiskit integration

## Goal

Move the performance-sensitive QKD simulation core to Rust while preserving the
current Python API and integrating circuit construction, transpilation, and
execution with Qiskit-compatible backends.

## Scope

- Rust workspace and core domain model
- Safe Qiskit integration boundary
- BB84, B92, and E91 implementations
- Physical channel, source, detector, attack, and defense models
- Python bindings and backward compatibility
- Verification, CI, packaging, and documentation

## Success criteria

- Rust can construct and execute BB84, B92, and E91 experiments.
- Qiskit-specific types remain outside the protocol domain core.
- Existing Python entry points continue to work or have documented shims.
- Simulation runs are reproducible from a root seed.
- Noise and detector models can consume laboratory calibration snapshots.
- Rust, Python, and Qiskit compatibility tests pass in CI.

## Child issues

- [#2 — Integration boundary](002-decide-rust-qiskit-integration-boundary.md)
- [#3 — Cargo workspace](003-bootstrap-cargo-workspace-and-qiskit-discovery.md)
- [#4 — Safe C API wrappers](004-safe-qiskit-c-api-wrappers.md)
- [#5 — Experiment and physics model](005-hardware-calibrated-quantum-experiment-model.md)
- [#6 — Execution backend](006-pluggable-quantum-execution-backend.md)
- [#7 — BB84](007-bb84-circuit-generation-in-rust.md)
- [#8 — B92](008-b92-circuit-generation-in-rust.md)
- [#9 — E91](009-e91-and-chsh-in-rust.md)
- [#10 — Intercept-resend](010-intercept-resend-attack.md)
- [#11 — Noise](011-channel-and-detector-noise.md)
- [#12 — PNS and decoy state](012-pns-and-decoy-state-hybrid-model.md)
- [#13 — Python bindings](013-python-bindings-with-pyo3.md)
- [#14 — Parity tests](014-statistical-parity-and-regression-tests.md)
- [#15 — CI](015-rust-python-qiskit-ci.md)
- [#16 — Documentation](016-rust-qiskit-documentation.md)

## Labels

`epic`, `rust`, `qiskit`, `qkd`
