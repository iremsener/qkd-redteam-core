# [Red/Blue Team] Implement PNS and decoy-state hybrid optical models

## Problem

Photon-number-splitting attacks depend on multi-photon emissions and cannot be
represented faithfully as ordinary qubit gates. Decoy-state detection likewise
depends on source intensity and yield statistics.

## Goal

Implement PNS and decoy-state analysis in the photonic event layer while
combining their observations with circuit-level protocol results.

## Requirements

- Sample weak coherent pulses from a Poisson photon-number distribution.
- Preserve pulse class, photon count, basis, and detection metadata.
- Model Eve's configurable multi-photon selection strategy.
- Keep signal, decoy, and optional vacuum intensities distinct.
- Calculate per-intensity gains, yields, error rates, and anomaly metrics.

## Acceptance criteria

- [ ] Photon-number frequencies converge to the configured Poisson model.
- [ ] Single-photon, multi-photon, empty, lost, and detected events are distinct.
- [ ] PNS can increase leakage without requiring an artificial QBER increase.
- [ ] Signal and decoy observations are analyzed independently.
- [ ] Clean-channel fixtures remain within configured statistical thresholds.
- [ ] Attack fixtures produce a measurable yield anomaly.
- [ ] Results identify every approximation used by the optical model.
- [ ] Documentation states that this is not a gate-only Qiskit simulation.

## Dependencies

- [#5](005-hardware-calibrated-quantum-experiment-model.md)
- [#11](011-channel-and-detector-noise.md)

## Labels

`red-team`, `blue-team`, `pns`, `decoy-state`, `physics`
