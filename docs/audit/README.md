# The referee's audit pack

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's solid-A directive of 26 October 2026 asks for an A that survives an independent review, earned by evidence: no gain
made up, no loss hidden, no proof invented, no controller action forced, no measurement changed to raise a grade. This folder
holds what has been executed for it, each file written by a tool from the repository's own records, and says plainly what has
not yet been executed. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

| File | What it is | Written by | Status |
|---|---|---|---|
| [`BENCHMARK_DISCREPANCIES.csv`](BENCHMARK_DISCREPANCIES.csv) | every gauge of every three-run table: benchmark, engine, native and Omni-Compass in each run, the raw change 100 × (omni − native) / native with its true sign, the gauge's aim, its effect, the word, its class, the confidence, the practical significance, the run-to-run stability, the evidence class, the source, and an independent reclassification | `tools/audit_export.py` | executed: 10,281 rows |
| [`STATISTICAL_VALIDATION.md`](STATISTICAL_VALIDATION.md) | the rule, the counts by engine and class, the confidence and stability, and the independent check's result | `tools/audit_export.py` | executed: 9,424 agree, 0 differ, 857 not recomputable from the committed tables (101 of them standing) |
| [`LIVE_ENGINE_ACCEPTANCE.md`](LIVE_ENGINE_ACCEPTANCE.md) | the live benchmark engine in a real browser: load, errors, links, the three shapes, the four live words, the reflex on the engine's numbers, the kill switch, a phone | `tools/live_engine_acceptance.py` | executed: 13 pass, 0 fail |
| [`RELEASE_GATE_REPORT.md`](RELEASE_GATE_REPORT.md) | the ten release gates, each marked by what was executed | written by hand from the runs it names | gates open, below |
| [`../../results/verdict_audit/VERDICT_AUDIT.md`](../../results/verdict_audit/VERDICT_AUDIT.md), [`DISCREPANCIES.md`](../../results/verdict_audit/DISCREPANCIES.md) | the one count of every reading, and every printed value that changed against main with its reason | `tools/verdict_audit.py` | executed |

Not yet executed (each named here so that nobody reads its absence as a pass): the repository inventory with its call graph,
the mathematical referee report, the control-safety audit with failure-injection tests, the workflow and security audit, and the
claim-evidence matrix. Their reviews were started on 26 October on commit `7678d817d8` and stopped before writing anything, at
the review service's weekly limit; they run again when it resets (29 October, 20:00 UTC). No grade is given while they are open.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
