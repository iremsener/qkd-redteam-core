# [Rust] Bootstrap Cargo workspace and Qiskit build discovery

## Goal

Create the Rust workspace and a reproducible build path for the selected Qiskit
integration without changing the public Python API.

## Proposed layout

```text
rust/
├── Cargo.toml
├── qkd-core/
├── qiskit-sys/
├── qiskit-adapter/
└── qkd-python/
```

## Requirements

- Keep raw FFI declarations inside `qiskit-sys`.
- Keep domain logic in `qkd-core` free of Python and Qiskit dependencies.
- Discover Qiskit headers and libraries from documented configuration.
- Support `QISKIT_INCLUDE` and `QISKIT_LIB` overrides.
- Pin supported toolchain and dependency versions.

## Acceptance criteria

- [ ] `cargo build --workspace` succeeds on a supported Linux environment.
- [ ] `cargo test --workspace` executes an initial smoke test.
- [ ] Missing Qiskit artifacts produce an actionable build error.
- [ ] Runtime Qiskit ABI/version compatibility is checked.
- [ ] Build artifacts and Cargo output are ignored by Git.
- [ ] The workspace layout is documented in the root README.

## Dependencies

- [#2](002-decide-rust-qiskit-integration-boundary.md)

## Labels

`rust`, `build`, `qiskit`
