# Release gates

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each gate of the solid-A directive, marked only by what was executed on this branch's commit (the merge of main's omni-v21,
`7678d817d8`, and the commit that carries this page). PASS means the check ran and passed; PARTLY names what ran and what did
not; NOT RUN means it has not been executed. No gate is marked PASS because it was skipped, blocked or not executed. Run and scored
by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

| Gate | Status | What was executed | What is open |
|---|---|---|---|
| A. Source integrity | PARTLY | `tools/omni_version.py` reads omni-v21 (digest `b658f05d43c1e602`, 63 files) on the commit; the page's build stamps it | the release manifest's check on the pushed commit and GitHub's verify run on it |
| B. Mathematical correctness | PARTLY | the page's engine against the Python (`docs/engine/check_live_engine.py` through the build's `--check`: every record the repository's own run) and the C++ twins (12 parity checks, 156,480 organism readings, every number identical) | an independent reference for each law, the adversarial numerical tests and the proof status of each claim (the mathematical referee report): not yet executed |
| C. Mechanism correctness | PARTLY | omni-v21's immune rule and its C++ twin proven alike on 200 seeded scripts (`tests/test_cpp_immune_parity.py`, main's own record); the page's reflex on the same numbers, read in a browser | the control-safety audit of every write path with failure injection: not yet executed |
| D. Benchmark integrity | PARTLY | every reading recomputed from its stored native and Omni-Compass values by an independent classifier: 9,424 agree, 0 differ | 857 rows not recomputable from the committed tables, 101 of them in standing tables (CityLearn and pandapower printed their changes to two decimals; the runner's raw files hold the values); 73 of the 85 standing tables still on an engine before omni-v21 until their three runs land |
| E. Statistical integrity | PASS | the key's rule applied to every row (`tests/test_verdict_audit.py`, `tests/test_audit_export.py`): STEADY of three kinds kept apart, the raw change with its true sign, the confidence and the stability printed apart from the word | — |
| F. Security | NOT RUN | — | the workflow, dependency and secret audit |
| G. Live benchmark engine | PASS | built on omni-v21; `build_live_engine.py --check` passes; the browser acceptance, 13 of 13 | — |
| H. Documentation | PARTLY | the engine that stands named as omni-v23 on the page, its manual and its appraisal; the documents indexed by reader | the claim-evidence matrix over every published claim |
| I. Release verification | PARTLY | the tests named above, run on the commit | `verify.py` in full and GitHub's verify run on the pushed commit |
| J. Independent reproducibility | NOT RUN | — | the checks repeated in a separate clean environment from the documented commands |

**The two workflow fixes of 26 October** (commit `0cc26d8cfd`): the injection grid's planner installs its dependencies before
it imports them, and its first run on the fixed commit finished green (run 40395118932, success, its results on main as
`results/injection_grid/INJECTION_GRID_1635237724.*`); kwok-scale's node selector and early failure check are committed, and its
first run on main after the fix (run 40400903184) was still queued when this page was written: that fix is not yet shown to pass.

**No grade is declared.** The directive's rule stands: the repository is not called a solid A while any release-blocking gate
is unverified. The open items are listed above and in [`README.md`](README.md).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
