# [Rust] Implement safe wrappers for the Qiskit C API

## Goal

Prevent raw C pointers, ownership rules, and error codes from leaking into the
Rust domain and protocol layers.

## Requirements

- Introduce RAII wrappers for supported circuit and transpiler objects.
- Convert Qiskit exit codes and null pointers into typed Rust errors.
- Distinguish owned handles from borrowed handles.
- Keep `unsafe` blocks small and confined to the adapter boundary.
- Do not mark wrappers `Send` or `Sync` without verified guarantees.

## Acceptance criteria

- [ ] Every owned Qiskit object is released exactly once through `Drop`.
- [ ] Borrowed objects cannot outlive their owner through safe Rust APIs.
- [ ] Invalid qubit, clbit, gate, and parameter inputs return typed errors.
- [ ] Public safe APIs contain no raw pointers.
- [ ] Unit tests cover creation, mutation, failure, and destruction paths.
- [ ] Sanitizer or Valgrind checks show no leaks for the smoke-test suite.
- [ ] The wrapper reports incompatible Qiskit versions before circuit work.

## Dependencies

- [#2](002-decide-rust-qiskit-integration-boundary.md)
- [#3](003-bootstrap-cargo-workspace-and-qiskit-discovery.md)

## Labels

`rust`, `ffi`, `safety`, `qiskit`
