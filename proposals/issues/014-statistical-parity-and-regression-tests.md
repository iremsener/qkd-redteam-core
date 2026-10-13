# [Test] Add statistical parity and deterministic regression tests

## Goal

Verify the Rust implementation against analytical results, the current Python
engine, Qiskit reference behavior, and selected laboratory fixtures.

## Test categories

- Deterministic domain and validation tests
- Analytical channel fixtures
- Seeded structural circuit tests
- Statistical protocol and attack tests
- Rust/Python compatibility tests
- Rust/Qiskit parity tests
- Calibration and laboratory-data tests

## Acceptance criteria

- [ ] Fixed-seed tests reproduce identical logical inputs and RNG streams.
- [ ] Identity and amplitude-damping channels match analytical references.
- [ ] MCWF averages converge to exact Lindblad fixtures within tolerance.
- [ ] QBER, yield, CHSH, leakage, and detector statistics are covered.
- [ ] Statistical assertions use declared confidence levels and sample sizes.
- [ ] Python/Rust differences have documented tolerances and rationale.
- [ ] Qiskit parity fixtures record the Qiskit version used.
- [ ] Failed statistical tests report seed, sample count, and observed interval.
- [ ] A policy limits flaky retries and prohibits hiding unstable tests.

## Dependencies

- [#7](007-bb84-circuit-generation-in-rust.md) through
  [#13](013-python-bindings-with-pyo3.md)

## Labels

`testing`, `regression`, `statistics`, `qiskit`
