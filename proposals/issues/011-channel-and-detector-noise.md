# [Physics] Implement configurable channel and detector noise

## Goal

Replace the scalar distance-based bit-flip approximation with composable,
calibrated channel and detector models supported by the experiment schema.

## Initial models

- Fiber attenuation in dB/km
- Unitary polarization drift
- Depolarizing, amplitude-damping, and phase-damping channels
- Thermal relaxation from `T1`, `T2`, and elapsed time
- Detection efficiency and readout confusion
- Dark counts and background photons
- Timing jitter, dead time, and afterpulsing

## Acceptance criteria

- [ ] Channel components compose in declared physical order.
- [ ] Loss/erasure remains distinct from bit flips and readout errors.
- [ ] Kraus channels pass CPTP validation.
- [ ] Invalid thermal parameters such as `T2 > 2*T1` are rejected.
- [ ] Detector history is preserved when dead time or afterpulsing is enabled.
- [ ] Laboratory calibration values retain units and uncertainties.
- [ ] Unsupported backend features return explicit capability errors.
- [ ] The legacy `0.2 dB/km` behavior is available as a documented preset.
- [ ] Analytical fixtures validate each initial channel independently.

## Dependencies

- [#5](005-hardware-calibrated-quantum-experiment-model.md)
- [#6](006-pluggable-quantum-execution-backend.md)
- [#7](007-bb84-circuit-generation-in-rust.md)
- [#8](008-b92-circuit-generation-in-rust.md)
- [#9](009-e91-and-chsh-in-rust.md)

## Labels

`physics`, `noise`, `detector`, `simulation`
