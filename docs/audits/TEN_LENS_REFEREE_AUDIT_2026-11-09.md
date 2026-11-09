# Ten-lens referee consensus-style audit: Omni-Compass

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Review date:** 9 November 2026. **Source:** `main` through commit `95c46b6fb753c09ad3e70cb0aab66a97297b3db8` before this report's own commit. **Standing engine:** omni-v26 (`OMNI_V26.json`, digest prefix `75d3c22eed4473b9`, 65 files). **Audit type:** one reviewer applying ten distinct disciplinary criteria. These are **not** ten independently appointed human reviewers; no independent certification, execution of the current test suite or third-party replication is implied. A scoped review of governing files, index receipts, formal-status documents, run logs summarized in the repository, historical CI receipts, loss ledger and documentation. Not a line-by-line audit of the whole approximately 52,529,777 KiB GitHub repository.

## Scoring standard

Equal weighting across ten lenses for transparency; the score is a subjective evidence-readiness estimate, **not** a statistical probability, measured engine performance, or external accredited grade. Scale: A++ ≥98, A+ 95–97, A 90–94, A− 85–89, B+ 82–84, B 78–81, B− 70–77, C+ 67–69, C 63–66, C− 60–62, D+ 55–59, D 50–54; below 50 F. An A+ needs reproducible, independently examinable, version-current evidence throughout each material domain; it does not require pretending every benchmark is positive, but adverse effects must be bounded, explained and honestly presented.

| Lens | Discipline and burden of proof | Score | Letter | Verified strength | Gap blocking A+ |
|---:|---|---:|---|---|---|
| 1 | Mathematical formalization | 80 | B | Explicit controlled U-channel Lyapunov proof, bounded drift assumptions, computer-assisted/discrete proof record | Reconcile formal-status page with later `ENGINE_PROOFS`; full forced six-state/global plant theorem and realization maps remain unestablished |
| 2 | Physics and scientific scope | 64 | C | Clear separation between modeled energy, device-meter GPU energy, and nonphysical computational abstractions | No general physics unification or universal physical law established; no whole-machine physical energy proof; external plant realizations limited |
| 3 | Control theory and fail-safe engineering | 72 | B− | Versioned guardrails, watch/kill design, V26 hold fix for waiting pods | V26 behavioral branch not exercised by the 104 model-gate readings; remaining failures, recovery and controller interaction require live tests |
| 4 | Python / C++ implementation architecture | 85 | A− | Fingerprinted 65-file engine; sealed parity framework, modular orchestrator and benchmark harness | One Python-only store-brain path, changing integration layers, environment-specific correctness and no independent deployment audit |
| 5 | Verification, CI and software assurance | 81 | B | Broad unit/property/parity inventory (self-reported 863 unit cases, 14 parity files; coverage measured 71% on V23); source receipts | Stored quick-verification receipt at `c18896e...` (7 Nov) predates current head; current CI green not confirmed; V26 coverage not remeasured |
| 6 | Experimental design and reproducibility | 74 | B− | Native/Omni pairing, preregistration records, raw artifact digests, invalid run retention, GPU no-write control | Incomplete independent reproduction, heterogeneous machines, few independent GPU runs, and multiple changed harnesses |
| 7 | Statistics, benefit index and adversarial accounting | 65 | C | Per-run gauge directions, uncertainty columns, precise index formula; observed 26-test V25 index recomputes; loss ledger explicit | Composite equates unlike ratios, extreme Kafka influence (+218.6% category), unequal physical meaning of resources, multiple comparisons, 287 adverse native-relative rows and no general total net estimator |
| 8 | Physical GPU, CPU and real-cloud efficacy | 58 | D+ | A10 V23 physical energy/request cut +0.78%–1.79% across three runs; Azure V18 97 paired valid cloud repeats | A10 run C worsened service; bare-metal CPU power not run; AWS/GCP no completed benchmark verified; Azure bill +1.2% with interval spanning zero; V26 end-to-end physical efficacy unmeasured |
| 9 | Repository architecture, manifests and provenance | 77 | B− | Source manifests, provenance ledgers, legal governance, 71 reported workflows, restored START_HERE navigation | Enormous repository and generated artifacts, outdated narrative snapshots, inter-file contradictions, current-run status not guaranteed by old receipts |
| 10 | Technical writing, editorial clarity and legal defensibility | 77 | B− | Explicit P/L/S/T/V/O distinctions, limitations and licensing, manuals, claim registry, risk notices | Over-strong phrases (“proven”, “do no harm” unconditional), inconsistent grading/claim labels, ambiguous “GAIN/power given”, outdated source versions and verbosity obscure conditional claims |
| | **Equal-weight collective** | **73.3** | **B−** | Strong engineered research program with substantive test infrastructure | **Not yet an independently verified, current-engine end-to-end performance claim** |

### 1. Mathematical referee

`docs/TRACKING_THEOREM.md` proves conditional continuous-time tracking for the internal U channel: with unsaturated input and fixed target, `e'=-K_P e`; the Lyapunov function `V=e²/2` satisfies `V'=-K_P e²`. Its saturated case requires a bound `|f_U|<u_max`. The sampled-data bound `|e_{k+1}| ≤ ρ|e_k|+ε_h` is contingent upon an error bound. The paper correctly distinguishes computed fixture bounds from true domain-wide proof; it also reports later computer-assisted enclosures in `docs/ENGINE_PROOFS.md`. However `docs/FORMAL_STATUS.md` still says domain-wide discrete invariance is open. Referee action: check the solver certificates and precision model, separate proven E/S/U/I sub-properties from full-plant claims, and regenerate a single canonical theorem-status registry with lemma IDs, assumptions and tool versions. External plant realization is not established merely by the controller tracking its own target.

### 2. Physics referee

An energy meter on a rented A10 is physical class P for that device and workload; energy numbers on a kind cluster are often a declared model. A physically measured GPU energy reduction is not a general law of thermodynamics, a total data-center wall-plug saving, or a cross-domain unification. Require calibration and uncertainty, exact driver/firmware and power-limit logging, complete power/energy boundaries and external actuator model for every intended transfer. No Navier–Stokes, quantum field, gravity or Millennium Problem proof is established by the receipts inspected.

### 3. Control and safety referee

`docs/OMNI_V26.md` identifies a real Kubernetes failure mode: target bouncing between 30% and 50% as unrelated pending pods intermittently appear. The new hold rule is a relevant safety improvement, yet `results/model_gate/V26_VS_V25.md` explicitly says the new branch never fired in twelve models with 104 unchanged readings. Therefore 104 identical model readings are a non-regression result **on that modeled support**, not confirmation of the repaired branch on a real cluster. Demand current-engine controller-fault-injection, failed-request, pending-pod, kill/restore and rollback measurements.

### 4–5. Software and verification referees

The 65-file `OMNI_V26.json` fingerprint, C++ seal and parity tests support traceable implementation. The repository's report card quotes 863 unit tests, 14 C++ parity files and 157 PASS at an older verification commit. `docs/ENGINE_COVERAGE.md` says **71%** (8,148 of 11,424 statements) measured on V23, not V26. A test suite existing does not establish it passed at this review's HEAD. The visible `results/VERIFY_RECEIPT.txt` begins “verify.py --quick at commit c18896e0a8ea..., 2026-11-07...” while main had later commits. The GitHub connector’s combined commit statuses do not provide a green current-workflow confirmation. Require current SHA-bound successful CI, fresh coverage on the current fingerprint and a signed/verifiable release-manifest receipt.

### 6–7. Benchmark and statistical referees

`results/OMNI_INDEX.json` records a **20.3543% equal-category composite index** and **93.9746% separate service-only composite** across **26 V25 entries**. They are reproducible from the per-test scored ratios but do not equal a single work-per-dollar improvement. The six category scores are Kubernetes **+20.4633%**, PostgreSQL **−1.3744%**, Kafka **+218.5565%**, Redis **−6.8491%**, MongoDB **−4.7904%**, MySQL **−9.4536%**, under their declared project-specific index definitions. The category scores are not necessarily signed physical throughput changes; for example a resource-cost penalty can drive a negative category score while some service measures improve. Show native/Omni raw work and cost at identical service guardrails rather than declaring all six “gain”. For global inference, predeclare the aggregation and correct or bound multiple comparisons; give interval estimates and negative-case sensitivity analysis.

`docs/LOSS_LEDGER.md` records **534 total LOSS rows** across its selected latest tables, **287** relative to Omni against its own native. The November 7 `docs/REPORT_CARD.md` separately describes V25's **281**, V12's **6**, and **74** V25 causes still unwritten. These are overlapping snapshots/categorizations, not an automatic new failure count on V26. Respect the direction of the metric: decreasing p95 is favorable; increasing failed-request rate is adverse. Neither a resource labeled “power given” nor the 0.5% reporting floor cancels an operator's hard guardrail.

### 8. Hardware and cloud referee

**GPU:** `results/gpu/V23_A10_CAP_FULL_ABC.md` reports physical A10 power-cap full-load runs (A/B/C; 5 paired repetitions each). Energy per served request fell **1.79%, 1.35%, 0.78%**, and work per energy rose **1.82%, 1.37%, 0.79%**. Run C nevertheless had **requests served −0.70%**, **p95 latency worse by 2.25%**, **mean latency worse by 2.18%**. This is **mixed** under nonnegotiable service guardrails, regardless of the positive energy readings. V23 is historical even where relevant code is unchanged.

**CPU:** `docs/RUN_LEDGER.md` reports no real bare-metal Linux governor/power-meter run, unlike GitHub's virtual CPU execution of software tests.

**Azure:** `results/live/AKS_STEADY_100_OMNI_V18.md` records 97 valid pairs out of 100 planned, three failed, on V18. Estimated bill **+1.2%** (uncertainty includes zero); p99 improved **11.0%**, but failed requests **+3.9%** with interval crossing zero. No cloud saving demonstrated.

**AWS/GCP:** Workflows and queues exist; current `switch=on` values do not prove service-account permissions, quotas or runs. The last stored ledger reports failures and no successful physical/managed-cloud benchmark there. Do not claim newer credential status from October entries or simulate AWS/GCP via Azure.

### 9. Repository systems referee

The repo metadata reports a public, very large tree; its size and extensive manuals are neither defects nor proof of engineering quality. The `START_HERE.md` entry point is now present and linked from `docs/README.md`, while `docs/RUN_LEDGER.md` says AWS/GCP “switched off” and their current queue files say “on”. The `docs/REPORT_CARD.md` carries internally conflicting freshness phrases (e.g. V24-era table language alongside V26 metadata). Maintain canonical current-state generated dashboards separate from append-only historical receipts. Avoid moving or renaming versioned raw data without a validated reference migration.

### 10. CTO, legal/referee and technical editor

The author-produced evidence is material and can form a professional due-diligence package, with clear licensing, disclosures and native baselines. But unqualified “proved,” “safe,” “no loss,” “best” or “global optimum” must be restricted to exact theorem hypotheses, certified test domains or empirically verified envelopes. Internal grades are not expert endorsements; revised numbers should preserve their generators and version/receipt identity. Give the executive claim first, then table of native/Omni/paired interval, and only then the engineering discussion.

## The binding A+ program, by impact

1. **Reproduce current V26 verification** at an exact commit: signed/captured CI run, build, unit/properties, C++ parity, release SHA, model gate, legal/layout and site feed consistency; measure V26 coverage. A PASS cannot be inferred from an older receipt.
2. **Close unaccounted service harm:** prioritize the 287 native-relative historical LOSS rows and 74 causes unassigned in the last report card; identify affected V26 behaviors, reproduce, repair and exercise live control safety and restore. Never reclassify a loss to erase it.
3. **Run V26 paired Kubernetes evidence**, especially combined/fairness/robustness/kill paths hit by the hold fix; the report card explicitly had **zero V26 three-run tables** as of 7 November.
4. **Complete one physically defensible CPU and one new GPU study**, with all hardware/driver versions, meters, energy and work metrics, p95, error guardrails and failure logs. Pair enough replicates for a prespecified precision target; no cherry-picking a favorable GPU run.
5. **Finish cloud gates:** fresh zero-cost AWS and GCP checks and one bounded real run after approval; Azure same-version work-meter and bill pairing; record invalid and aborted work.
6. **Resolve theorem status formally:** reconcile the discrete proof language and verify all interval arithmetic or solver assumptions. Explicitly separate internal tracking from real-plant realization and any conjectural physics.
7. **Audit aggregate statistics:** make scoring policy and its sensitivity transparent, compare absolute useful work at equal cost and service, report uncertainty and multiplicity; do not equate Kafka's 218% category index to an economic return.
8. **Clean the information architecture** with generated current-state summary, source/version matrix and reproducibility links; move files only with reference mapping and complete passing tests.
9. **Obtain outside reproduction** by a separate tester with immutable files, independent results and known hardware, or label all evidence internally reproduced.
10. **Publish audited conditional claims** with exact hypothesis, engine version, workload and instrumentation on each claim; preserve the full legal notice and historical failures.

**Collective disposition:** **B− (73.3/100)** as a ten-lens evidence-readiness assessment; the largest deficits are external physical validation and inferential/statistical defensibility, not merely editing or file organization. Distance to A+ threshold under this declared scoring rubric: **21.7 points**. These numbers do not imply an exact A+ probability.

**Key files:** `OMNI_V26.json`; `docs/OMNI_V26.md`; `docs/TRACKING_THEOREM.md`; `docs/ENGINE_PROOFS.md`; `docs/FORMAL_STATUS.md`; `docs/EVIDENCE_LEDGER.md`; `docs/REPORT_CARD.md`; `docs/LOSS_LEDGER.md`; `docs/ENGINE_COVERAGE.md`; `results/VERIFY_RECEIPT.txt`; `results/OMNI_INDEX.json`; `results/model_gate/V26_VS_V25.md`; `results/gpu/V23_A10_CAP_FULL_ABC.md`; `results/live/AKS_STEADY_100_OMNI_V18.md`; `docs/RUN_LEDGER.md`; `scripts/amazon_queue.txt`; `scripts/google_queue.txt`; `START_HERE.md`.

---

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
