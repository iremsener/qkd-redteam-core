# [CI] Add Rust, Python, and Qiskit compatibility workflows

## Goal

Continuously verify source quality, FFI safety, package compatibility, and
reproducible builds across the supported platform matrix.

## Required jobs

- Rust format, Clippy, and unit tests
- Python lint and test suite
- Rust/Python integration tests
- Qiskit compatibility matrix
- FFI sanitizer or Valgrind checks
- Source distribution and wheel smoke tests
- Documentation link and Markdown checks

## Acceptance criteria

- [ ] `cargo fmt --check`, Clippy, and Rust tests pass in CI.
- [ ] Python tests run on every supported Python version.
- [ ] Minimum and current supported Qiskit versions are tested.
- [ ] Linux and macOS builds are verified.
- [ ] FFI leak and undefined-behavior checks run on Linux.
- [ ] Built wheels install into clean environments and execute a smoke test.
- [ ] Dependency and compiler caches are keyed safely.
- [ ] Workflows contain no credentials or laboratory secrets.
- [ ] Required checks and release-blocking failures are documented.

## Dependencies

- [#3](003-bootstrap-cargo-workspace-and-qiskit-discovery.md)
- [#13](013-python-bindings-with-pyo3.md)
- [#14](014-statistical-parity-and-regression-tests.md)

## Labels

`ci`, `rust`, `python`, `qiskit`, `packaging`
