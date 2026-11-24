# Enterprise review handoff and acceptance gates

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This document coordinates parallel human and AI engineering reviews without modifying measured results or the running governor. It is a review plan, not a certification.

## Source-of-truth and change ownership

| Area | Source of truth | Safe edit practice |
|---|---|---|
| Root executive claims | `tools/headline.py`, `tools/summary.py`, and raw results | Edit generators, rebuild outputs, compare with receipts |
| Mathematical engine | `omnicompass/`, `omni_orchestrator/`, `omni_controller/` | Freeze version and run reference, parity, and boundary tests |
| Benchmarks and verdicts | `tools/readings.py`, raw run files, preregistrations | Preserve originals; show raw Native/Omni and independent recomputation |
| Live Engine | `docs/engine/build_live_engine.py`, `docs/engine/check_live_engine.py` | Rebuild rather than hand-edit generated HTML |
| Board and diligence | `docs/DUE_DILIGENCE.md`, `docs/CLAIMS_REGISTER.md`, `docs/EVIDENCE_LEDGER.md` | Every assertion must link to a dated, versioned source |
| Security and licensing | `SECURITY.md`, `LICENSE`, `NOTICE`, `DISCLOSURES.md` | Do not alter legal terms as part of cosmetic cleanup |

## Open referee issues for the next pass

1. **Version drift.** The root README describes v18 benchmark results and elsewhere references a v19 factory profile while the state-of-play record identifies v21. Preserve historical results but identify their versions conspicuously; use generators for generated sections.
2. **Current-engine coverage.** The state-of-play record says 4 of 26 real benchmark cases have current-v21 results. Require all cases or mark the unrun ones unverified for v21.
3. **Verdict precision.** `EVEN` presently includes nonzero changes under a 0.5% threshold. Distinguish exact equality, small changes, and inconclusive statistical results without rewriting historical receipts.
4. **Resource tradeoffs.** Work-per-energy deterioration and extra resources must be visible alongside gains. Enforce declared hard limits and operator authority.
5. **Live Engine availability.** Verify an actual browser-accessible page and distinguish replay/simulation from live physical actuation.
6. **Workflow repairs.** Verify fresh successful runs for KWOK-scale and injection-grid after the October 26 fixes, not only the verification receipt.
7. **Mathematical status.** Distinguish a proved property of the control model from a claim about realizing an external scientific theory. Require explicit maps and proofs for any claimed universal realization.
8. **Security.** Audit workflow permissions, pinned dependencies, secret handling, and deployment approval before production claims.

## Parallel work rules

- One branch per bounded change; no concurrent writes to the same file.
- Rebase on the latest `main` before merge; resolve generator conflicts at their source.
- Every pull request must list changed files, exact tests executed, evidence, limitations, and rollback.
- No automatic grade upgrades. A reviewer must inspect actual output and failures.
- Do not enable cloud hardware control merely to eliminate a disabled badge. Verify credentials, billing authorization, limits, actuator authority, and restore behavior first.
- Do not remove a loss or suppress an adverse result to improve the front page.

## Merge acceptance checklist

- [ ] Links in executive navigation resolve.
- [ ] Generated files reproduce from their generators.
- [ ] `python verify.py` passes on the exact proposed commit.
- [ ] Required GitHub Actions checks complete successfully.
- [ ] No material claim is detached from its engine version and evidence class.
- [ ] No raw benchmark receipt or legal notice was modified.
- [ ] Independent reviewer records outstanding issues before approval.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
