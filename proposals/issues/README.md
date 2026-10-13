# Rust–Qiskit Integration Backlog

This directory contains the proposed implementation backlog for moving the QKD
simulation core to Rust and integrating it with Qiskit and laboratory systems.

| Issue | Title | Milestone |
|---|---|---|
| [#1](001-rust-native-qiskit-integration-epic.md) | Rust-native Qiskit integration | Epic |
| [#2](002-decide-rust-qiskit-integration-boundary.md) | Decide the Rust–Qiskit integration boundary | Architecture |
| [#3](003-bootstrap-cargo-workspace-and-qiskit-discovery.md) | Bootstrap Cargo workspace and Qiskit discovery | Foundation |
| [#4](004-safe-qiskit-c-api-wrappers.md) | Implement safe Qiskit C API wrappers | Foundation |
| [#5](005-hardware-calibrated-quantum-experiment-model.md) | Define a hardware-calibrated experiment model | Core physics |
| [#6](006-pluggable-quantum-execution-backend.md) | Introduce a pluggable execution backend | Architecture |
| [#7](007-bb84-circuit-generation-in-rust.md) | Implement BB84 circuit generation in Rust | Protocols |
| [#8](008-b92-circuit-generation-in-rust.md) | Implement B92 circuit generation in Rust | Protocols |
| [#9](009-e91-and-chsh-in-rust.md) | Implement E91 and CHSH evaluation in Rust | Protocols |
| [#10](010-intercept-resend-attack.md) | Implement circuit-level intercept-resend | Red team |
| [#11](011-channel-and-detector-noise.md) | Implement channel and detector noise | Physics |
| [#12](012-pns-and-decoy-state-hybrid-model.md) | Implement PNS and decoy-state hybrid models | Red/blue team |
| [#13](013-python-bindings-with-pyo3.md) | Expose the Rust engine through PyO3 | Python API |
| [#14](014-statistical-parity-and-regression-tests.md) | Add statistical parity and regression tests | Quality |
| [#15](015-rust-python-qiskit-ci.md) | Add Rust, Python, and Qiskit CI | Delivery |
| [#16](016-rust-qiskit-documentation.md) | Document setup, architecture, and migration | Documentation |

## Recommended order

`#2 → #3 → #4 → #5 → #6 → #7 → #10 → #11 → #8 → #9 → #12 → #13 → #14 → #15 → #16`
