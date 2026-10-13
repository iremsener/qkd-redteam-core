# [Red Team] Implement circuit-level intercept-resend attack

## Goal

Model Eve as an explicit participant who measures and prepares states between
Alice and Bob rather than directly modifying final classical bits.

## Requirements

- Support random, fixed, and externally supplied Eve basis strategies.
- Record Eve's basis, outcome, and forwarded state when audit output is enabled.
- Keep attack randomness isolated in its own deterministic RNG stream.
- Support BB84 and the selected B92 attack convention.
- Expose attack metadata without leaking hidden simulation state by default.

## Acceptance criteria

- [ ] Attack-disabled execution is identical to the clean protocol path.
- [ ] Matching Eve bases preserve the expected state in ideal fixtures.
- [ ] Mismatched Eve bases introduce the expected disturbance statistically.
- [ ] BB84 QBER increases into the expected range under full interception.
- [ ] B92 behavior is validated against its documented attack model.
- [ ] Results report interception rate and Eve information estimates.
- [ ] Fixed seeds reproduce Eve's choices and outcomes.
- [ ] Tests use confidence intervals rather than exact random percentages.

## Dependencies

- [#7](007-bb84-circuit-generation-in-rust.md)
- [#8](008-b92-circuit-generation-in-rust.md)

## Labels

`red-team`, `attack`, `rust`, `qiskit`
