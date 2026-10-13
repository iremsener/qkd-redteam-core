# [Docs] Document Rust/Qiskit setup, architecture, and migration

## Goal

Provide enough documentation for contributors, Python users, and laboratory
operators to install, validate, and safely extend the Rust-backed engine.

## Required documentation

- Rust toolchain and Qiskit installation
- Qiskit C API/library discovery
- Workspace and adapter architecture
- Experiment and calibration schemas
- BB84, B92, and E91 examples
- Noise, MCWF, and photonic simulation modes
- Laboratory calibration ingestion
- Python API migration guide
- Backend capability and limitation matrix
- Troubleshooting and supported-version policy

## Acceptance criteria

- [ ] A new contributor can build and run the project from a clean environment.
- [ ] Examples cover clean and attacked scenarios for every protocol.
- [ ] Solver selection guidance explains accuracy/performance trade-offs.
- [ ] Circuit-shot, MCWF, and photonic Monte Carlo are clearly distinguished.
- [ ] Experimental Qiskit C API risks are documented.
- [ ] Calibration examples use no sensitive laboratory identifiers.
- [ ] Python migration examples show old and new APIs side by side.
- [ ] Documentation links and code snippets are checked in CI.
- [ ] Known unsupported combinations are listed explicitly.

## Dependencies

- [#13](013-python-bindings-with-pyo3.md)
- [#14](014-statistical-parity-and-regression-tests.md)
- [#15](015-rust-python-qiskit-ci.md)

## Labels

`documentation`, `rust`, `qiskit`
