# [RFC] Decide the Rust–Qiskit integration boundary

## Problem

Qiskit offers several possible integration paths: its experimental C API,
embedded Python through PyO3, OpenQASM interchange, and remote execution APIs.
Their feature coverage, deployment requirements, and stability differ.

## Goal

Select and document the primary Rust–Qiskit boundary before implementation
couples protocol code to an incomplete or unstable interface.

## Required investigation

- Build a Rust proof of concept that creates a circuit containing `H`, `CX`,
  and measurement operations through the Qiskit C API.
- Compare C API, PyO3, worker-process, and OpenQASM approaches.
- Record circuit, transpiler, simulator, noise, and hardware execution coverage.
- Compare Python runtime, dynamic linking, packaging, and cross-platform costs.
- Define a fallback for capabilities missing from the direct C API.

## Decision constraints

- Protocol and physics domain types cannot depend on Qiskit types.
- Experimental ABI changes must be isolated behind an adapter.
- The selected design must support both local simulation and laboratory use.
- Unsupported behavior must be discoverable through backend capabilities.

## Acceptance criteria

- [ ] A working C API proof of concept is committed.
- [ ] The alternatives and trade-offs are documented in an ADR.
- [ ] The primary integration path and fallback path are selected.
- [ ] Python runtime requirements are explicit.
- [ ] Supported Qiskit versions and upgrade policy are defined.
- [ ] Packaging and dynamic-library risks are documented.
- [ ] The decision is reviewed before Issues #3 and #4 are finalized.

## Dependencies

None.

## Labels

`architecture`, `research`, `rust`, `qiskit`
