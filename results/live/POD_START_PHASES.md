# Where the pod start wait goes: every serving pod's start, phase by phase

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Read by `tools/pod_phases.py` from the runs' own files (Kubernetes' pod watch and the host's processor record; evidence class L, the real thing on one GitHub runner). Each serving pod started inside a measured window is split into scheduling, the node side (the kubelet, the container runtime and the image) and the app with its readiness probe, and placed by the host's busy share over its start and by whether its node already carried a serving pod. Every number here is shown, not judged: the judged row is the three-run table's "pod start wait, mean". The mechanism and its physics: `docs/POD_START_WAIT.md`.

## The runs read

- `results/live/raw/addons-run-39108180989/`: 141 starts (omni-v10)
- `results/live/raw/addons-run-39115242861/`: 143 starts (omni-v10)
- `results/live/raw/addons-run-39123583570/`: 151 starts (omni-v10)
- `results/live/raw/addons-run-39148024948/`: 153 starts (omni-v11)
- `results/live/raw/addons-run-39157778756/`: 153 starts (omni-v11)

### omni-v10, test http: every serving pod started in a measured window

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 75 | 8.49 | 0.00 | 7.93 | 0.56 |
| native | 0.0 to 0.5 | already serving | 1 | 1.00 | 0.00 | 0.00 | 1.00 |
| native | 0.5 to 0.7 | empty | 11 | 9.36 | 0.00 | 8.82 | 0.55 |
| omni | 0.0 to 0.5 | empty | 20 | 8.45 | 0.00 | 7.90 | 0.55 |
| omni | 0.5 to 0.7 | empty | 27 | 9.04 | 0.00 | 8.41 | 0.63 |
| omni | 0.7 to 1.0 | empty | 21 | 12.52 | 0.10 | 11.86 | 0.57 |

Mean wait: native 8.52 s, omni 9.94 s, ΔW̄ = +1.42 s (+16.7%). Of it, the shift of starts into other strata (a busier host, an empty node): +1.57 s; the wait in the same stratum: -0.14 s.

### omni-v10, test both: every serving pod started in a measured window

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 22 | 8.00 | 0.00 | 7.41 | 0.59 |
| native | 0.0 to 0.5 | already serving | 113 | 1.27 | 0.02 | 0.72 | 0.53 |
| native | 0.5 to 0.7 | empty | 5 | 10.20 | 0.20 | 9.40 | 0.60 |
| native | 0.5 to 0.7 | already serving | 1 | 2.00 | 0.00 | 1.00 | 1.00 |
| omni | 0.0 to 0.5 | empty | 19 | 8.42 | 0.00 | 7.95 | 0.47 |
| omni | 0.0 to 0.5 | already serving | 111 | 1.44 | 0.00 | 0.94 | 0.50 |
| omni | 0.5 to 0.7 | empty | 1 | 7.00 | 0.00 | 7.00 | 0.00 |
| omni | 0.5 to 0.7 | already serving | 8 | 1.38 | 0.00 | 0.88 | 0.50 |

Mean wait: native 2.64 s, omni 2.43 s, ΔW̄ = -0.21 s (-7.8%). Of it, the shift of starts into other strata (a busier host, an empty node): -0.35 s; the wait in the same stratum: +0.14 s.

### omni-v11, test http: every serving pod started in a measured window

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 49 | 8.33 | 0.02 | 7.76 | 0.55 |
| native | 0.5 to 0.7 | empty | 6 | 11.00 | 0.00 | 10.33 | 0.67 |
| omni | 0.0 to 0.5 | empty | 10 | 8.30 | 0.00 | 7.90 | 0.40 |
| omni | 0.0 to 0.5 | already serving | 1 | 1.00 | 0.00 | 1.00 | 0.00 |
| omni | 0.5 to 0.7 | empty | 22 | 9.05 | 0.00 | 8.32 | 0.73 |
| omni | 0.7 to 1.0 | empty | 11 | 11.36 | 0.09 | 10.36 | 0.91 |

Mean wait: native 8.62 s, omni 9.27 s, ΔW̄ = +0.65 s (+7.6%). Of it, the shift of starts into other strata (a busier host, an empty node): +1.64 s; the wait in the same stratum: -0.98 s.

### omni-v11, test both: every serving pod started in a measured window

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 25 | 7.92 | 0.00 | 7.40 | 0.52 |
| native | 0.0 to 0.5 | already serving | 80 | 1.41 | 0.00 | 0.93 | 0.49 |
| native | 0.5 to 0.7 | empty | 1 | 6.00 | 0.00 | 6.00 | 0.00 |
| omni | 0.0 to 0.5 | empty | 17 | 7.47 | 0.00 | 6.94 | 0.53 |
| omni | 0.0 to 0.5 | already serving | 66 | 1.38 | 0.00 | 0.76 | 0.62 |
| omni | 0.5 to 0.7 | empty | 4 | 10.25 | 0.00 | 9.75 | 0.50 |
| omni | 0.5 to 0.7 | already serving | 14 | 1.71 | 0.00 | 0.86 | 0.86 |

Mean wait: native 2.99 s, omni 2.80 s, ΔW̄ = -0.19 s (-6.3%). Of it, the shift of starts into other strata (a busier host, an empty node): -0.26 s; the wait in the same stratum: +0.07 s.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
