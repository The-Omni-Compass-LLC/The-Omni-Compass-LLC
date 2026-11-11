# Current evidence addendum for all Omni-Compass manuals

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**As of 2026-11-09; current repository evidence boundary.** This is an editorial correction and source-reference sheet, not a new benchmark, a replacement raw receipt, an updated binary manual PDF, or an external certification. Where an earlier manual headline or unqualified statement conflicts with the version-tagged underlying receipts, the original receipt, generator and this **dated** clarification control interpretation. Regenerate this addendum whenever the engine or index changes. A stale addendum cannot establish later run status.

## 1. Establish what stands

- **Software engine standing on main:** `omni-v26`, 65 files, `OMNI_V26.json` and `docs/OMNI_V26.md`. The V26 repair affects Kubernetes waiting-pod behavior. Its model-gate's unchanged 104 readings did **not** exercise the new branch, so a new live Kubernetes run is required before claiming V26 measured improvement from that fix.
- **Last software index:** `results/OMNI_INDEX.json` on **omni-v25**, 26 scored workload entries. The **resource-inclusive** geometric composite `headline_pct` is **20.354306904733164%**; the **service-only** geometric composite `service_headline_pct` is **93.97457452769498%**; Kubernetes resource-inclusive category is **20.463324423521236%**. These are distinct computed index quantities, **not whole-system work-per-dollar or universal throughput gains**. See `tools/omni_index.py` and per-entry `results/live/V25_*.json`.
- **Historical V21 software index:** **5.0%** (resource-inclusive) and **12.9%** (service-only) are previous-version outputs, not current whole-system bare-metal / through-cloud benefits. Earlier **28%** Kubernetes fallback text is not the V25 published category index. Do not relabel old versions as V25 or overwrite results to fit a website guard.
- **Measured GPU (P):** the `omni-v23` A10 cap-full three runs, five pairs/run, show energy per served request decreasing **1.79%, 1.35%, 0.78%**. The last run also worsened requests served **0.70%** and P95 latency **2.25%**. Therefore a service-safe work-per-dollar gain across all three is **not** established by this receipt. Primary file `results/gpu/V23_A10_CAP_FULL_ABC.md` and paired bill `results/TWO_BILLS.json`.
- **Azure AKS (L):** `omni-v18`, **97 valid of 100 planned pairs**, bill mean approximately **1.2% higher** with uncertainty spanning zero, P99 latency approximately **11% lower**; completed work was **not measured for work-per-dollar**. Primary file `results/live/AKS_STEADY_100_OMNI_V18.md`.
- **Bare-metal Linux CPU energy:** the reviewed dated `docs/RUN_LEDGER.md` says **not run with physical power metering**. Virtual GitHub CPU harnesses are software evidence, not wall-plug CPU power data. AWS/GCP workflows and enabled queue files do not demonstrate completed paid-cloud run receipts.
- **Modeled Monte Carlo and simulation (S):** record as models, not independent physical metering; Python/C++ twins are code-parity evidence, not physical hardware performance. No physical/modeled result may be silently promoted to an independent theorem or current-version measurement.

## 2. Mathematics and physical scope

`docs/TRACKING_THEOREM.md` gives conditional continuous-time U-channel tracking, with `e=U−σ`, `V=e²/2` and `dV/dt=−K_Pe²` inside the unsaturated region. `docs/ENGINE_PROOFS.md` states computer-assisted SMT/interval proofs E1–E2, S1, I1, U1–U5 and B1 for its declared initial-state/parameter sets; the sampled U-error ball is bounded by 0.0677 under those assumptions. This **does not** establish an unconditional universal law for external plants, full forced six-state global convergence or CERT-10 for every admissible initial state. Read `docs/FORMAL_STATUS.md` and `docs/EVIDENCE_LEDGER.md` for the named open obligations.

## 3. Mandatory editorial rules for every inherited chapter

1. Every quantified benefit names **metric, baseline, version, hardware/software setup, class P/L/S/T/V, workload, denominator, replication count, uncertainty and receipt**. A +number need not be beneficial; p95 and spend aim down, work aims up; failed requests are a hard safety guardrail.
2. Distinguish software-end index, physical GPU energy/work, cloud spending, CPU metering, simulated organism and conditional composition. **Never add or multiply** cross-version percentage headlines as if they were a jointly measured chip-to-cloud improvement. `results/WHOLE_SYSTEM.md` is a class-S conditional cross-layer composition, not a single end-to-end physical run.
3. `results/ABC_TABLE.json` is intentionally retired; its archived `docs/history/model_tables/ABC_TABLE_MODEL.json` is class S. An outdated site fallback or old AI synopsis is not a sealed physical benchmark.
4. The `docs/LOSS_LEDGER.md` records adverse readings including **287** historical native-relative LOSS rows in its selected latest tables at review time. Do not erase, reinterpret, or silently omit them. “Do no harm” is a design goal enforced through shields/rollback, **not proof that adverse run outcomes never occurred**.
5. Historical test PASS, old manuals, old verification receipt and current manifests must not be conflated. `results/VERIFY_RECEIPT.txt` is pinned to an earlier commit than the main branch at this review. Current green CI, build/parity and current-version complete physical measurements require fresh execution and matching commit identifiers.
6. Preserve all licensing and proprietary notices from `LICENSE`, `NOTICE` and `DISCLOSURES.md`; avoid unsupported independent underwriter endorsement, certification, global-optimum claims or patents-granted language.

## 4. Controlled manual-rebuild procedure

The three primary Markdown manuals are `docs/OMNI_COMPASS_MANUAL.md`, `docs/OMNI_COMPASS_OWNERS_MANUAL.md` and `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`. Update substantive chapters **through their documented source-of-truth generators where applicable**, verify all backlinks, run reproducibility/legal/layout tests and rebuild their PDFs. Until the corresponding PDF artifacts are actually regenerated and verified, **do not claim that the PDFs incorporate this addendum**. A markdown-only correction is explicitly distinguished from a rebuilt printed manual.

Source navigation: `START_HERE.md`; `docs/README.md`; `docs/audits/TEN_LENS_REFEREE_AUDIT_2026-11-09.md`; `docs/REFEREE_VERSION_AND_BENCHMARK_STANDARD.md`; `docs/ENGINE_PROOFS.md`; `results/OMNI_INDEX.json`; `results/TWO_BILLS.json`; `docs/RUN_LEDGER.md`.

---

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
