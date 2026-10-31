# Evidence integrity audit and release claim boundaries — 2026-10-29

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Copyright (c) 2026 The Omni-Compass LLC. Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.

**Status:** targeted source-and-report audit; NOT a whole-repository certification or independent referee review. No finding here establishes intentional deception. Retain raw evidence and historic reports.

## Findings requiring explicit disclosure

| Severity | Evidence | Finding | Required interpretation |
|---|---|---|---|
| HIGH | results/OMNI_INDEX.md, tools/omni_index.py | +5.2% is a geometric-mean index over heterogeneous work, latency, resource and energy ratios | Composite score, not +5.2% actual bill savings or universal useful-work gain |
| HIGH | results/OMNI_INDEX.md | Kubernetes energy includes a declared model; service energy uses CPU seconds; machine proxies include connections, consumers, and memory | Do not call these measured joules or physical machine-hours |
| HIGH | README.md, results/WHOLE_SYSTEM.md | Whole-system totals compose evidence from different engine versions and evidence classes | Not one end-to-end same-version physical run |
| HIGH | README.md | +6.0% work result is three specific omni-v18 runs, not an omni-v21 verified universal result | Label exact run and engine; retain raw per-run values and costs |
| MEDIUM | docs/STATE_OF_PLAY.md, tools/readings.py | EVEN can include nonzero effects within a 0.5% threshold | Report signed raw difference, threshold/equivalence label, and statistical uncertainty separately |
| MEDIUM | tools/readings.py | 'power given' describes increases in spent resources | Show raw signed resource regression and whether work/cost constraints still pass |
| MEDIUM | docs/REFEREE_GRADES.md | Grades are internally assigned | Never describe as external referee certification |
| MEDIUM | README.md, docs/STATE_OF_PLAY.md | 22/25 benefit-sheet and 23/26 standing benchmark counts differ | Identify scope and inclusion rule before combining |
| OPEN | all Actions, source and raw data | Full provenance, exact-head reruns, physical meter calibration and independent replication not completed in this audit | No repo-wide clean bill of health |

## Release gate for every outward-facing benchmark claim

1. Every claim identifies engine SHA, benchmark harness SHA, workload/seed, baseline software and settings, hardware, repetition count and provenance class.
2. Preserve raw signed changes in all metrics, including losses and additional expenditure. The signal verdict must not conceal a cost/SLO regression.
3. Distinguish modeled energy, CPU-time proxy, metered joules and invoiced dollars. Never aggregate them as if they share units.
4. A mixed-version composition cannot be described as a single deployed system's observed performance.
5. Treat the three-run and 0.5% conventions as descriptive, not statistical proof or exact equality.
6. Link to source records and verify reproducibility on the exact commit. External claims require independent replication where claimed.
7. Never delete unfavorable original results. Corrections should be versioned with rationale and retained inputs.

## Remediation scope

The README now carries an upfront warning. Existing generated files must be changed at their generator source, with outputs regenerated and checked together; manual edits to generated sections will drift. Pending further audit: `tools/omni_index.py`, `tools/readings.py`, `tools/headline.py`, `tools/summary.py`, their regression tests, the raw three-run records, workflows and all artifact provenance. Do not claim these items are repaired merely because this audit exists.

This audit is not a finding of fraud and not an assertion that all benchmarks are false. It documents where the current presentation exceeds the available inference.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
