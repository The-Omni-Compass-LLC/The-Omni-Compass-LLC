# Referee standard: current engine, inherited evidence, physical measurements, and website claims

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Record examined:** repository `main`, 9 November 2026. **This is a review protocol and source reconciliation, not a claim of independent reproduction.** The project’s current engine and the engines on historical experiment receipts must never be conflated.

## 1. Three independent questions

1. **Current implementation.** `OMNI_V26.json` identifies **omni-v26** as a 65-file fingerprinted engine (digest prefix `75d3c22eed4473b9`); `docs/OMNI_V26.md` records a fix in the Kubernetes governor involving waiting pods and the hand-back hold. The core law may remain unchanged while a controller decision changes. “Same mathematics” is not proof of identical deployed performance.
2. **Published software evidence.** `results/OMNI_INDEX.json` currently indexes **26 V25 test entries**. It records an index of **20.354306904733164%**, a separate work-and-speed score of **93.97457452769498%**, and the real Kubernetes category score of **20.463324423521236%**. These are index scores defined by their generator, not proof of 20.4% more throughput, a 94% reduction in bills, or a universal improvement. The Kubernetes fairness V25 row reads **LOSS, −2.3%** by that index’s criterion and remains disclosed. No V26 physical or real-software retest is represented by those values.
3. **Historical physical and cloud evidence.** The A10 card’s measured performance belongs to **omni-v23** (class P); its work-per-dollar paired run deltas are **+1.46%, +0.73%, −0.69%**. Azure AKS’s 97 paired repetitions belong to **omni-v18** (class L); its estimated cloud bill rose approximately **1.2%**, inside the reported noise, and completed work for a work-per-dollar comparison was not counted. Each remains valid evidence of what its own experiment observed, not a newly measured V26 performance claim.

## 2. Equivalence and inheritance theorem: what it does and does not prove

Let `M_v` denote the governing mathematical model for version `v`; `G_v` the complete executable decision mapping, including adaptation, safety guards, integration steps and controller schedule; `H_v` the hardware/software environment; `D_v` a fixed workload distribution; `Y_v` the measured outcome.

**Structural equivalence** requires an explicit state map `T` and matching parameters such that, for the declared admissible domain and time discretization,

```text
T(F_old(x, u; θ)) = F_new(T(x), u; θ'),  with T preserving the constraints.
```

Here `F` is the complete closed-loop transition relation, not merely the isolated six-state governing formula. In stochastic settings, the corresponding transition kernels must be intertwined. The identity of a formula is insufficient to show closed-loop equivalence if the workload adapters, sampling schedule, fail-up, hand-back logic, or safety thresholds change.

**Conditional inheritance proposition.** If the same observed inputs and initial conditions are furnished, the old and new full transition relations are equivalent on a stated domain, and the relevant inputs/outputs and safety actions are preserved by `T`, then their deterministic controller traces agree under this experiment’s stated assumptions. This proposition supports inherited *functional parity*, not automatically inherited *physical effect sizes*.

**Physical transfer is a separate empirical proposition.** In general,

```text
Y_v = Measure( G_v, H_v, D_v, metering_v, randomness_v ).
```

Even if `G_old = G_new`, changes in `H`, `D`, metering, scheduling or drivers can change `Y`. An old physical result must retain the label “measured on version old”; “validated as code-compatible with current” may be appended only after the relevant parity evidence is recorded. “Newly measured on current” requires a current experiment.

## 3. Minimum evidence for a cross-version compatibility certificate

For each proposed inheritance edge, record in a machine-readable manifest:

- source and destination version, exact Git commit, all relevant engine and adapter SHA-256 digests;
- the complete changed-file list and a *semantic* impact classification (law, shield, governor decisions, actuator/write path, workload, harness, logger, scheduler, documentation-only);
- exact input fixtures and guardrail cases, deterministic traces, comparison tolerance, and counterexamples found;
- state-constraint and restore-to-native checks, including forced crashes and cancellation;
- environment compatibility envelope: hardware model, firmware/driver, OS/kernel, orchestrator version, application version, workloads, time window, energy/meter units;
- historical receipt identifiers, paired arms, random seeds, sufficient statistics, uncertainty intervals, missing data, multiplicity treatment and all adverse results;
- an explicit status: **historical only**, **functional parity shown on tested domain**, **applicable with stated restrictions**, **fresh physical verification required**, or **new current-version result measured**.

No “universal V18 = V23 = V25 = V26” statement may be issued without proving each transition over the relevant behavior. In particular, `docs/OMNI_V26.md` describes a behavioral controller repair, so V25-to-V26 Kubernetes performance must be treated as **not yet remeasured** until a V26 receipt exists; its earlier V25 measurements remain historical.

## 4. When fresh hardware/cloud experiments are warranted

A new run is required to claim a current-version *measured* improvement. For merely retaining historical measurements, new hardware rentals are not intrinsically required. Prioritize targeted physical reruns when a change affects: actuator mapping or power-cap writes; adaptive timing/decision rules; Kubernetes autoscaler/hold behavior; GPU integration, safety, driver or scheduler; energy or cost metering; experimental comparator; sample collection; or reported uncertainty.

The smallest reasonable new study is not necessarily a full multi-cloud campaign: first run deterministic regression and replay, then watch/kill/restore drills, then preregister and execute the **affected** physical configurations with paired native/Omni arms and a no-write watch control where possible. Choose replications from a power/precision analysis, not a universal “three is enough” rule. Preserve every attempt and cancellation.

## 5. Site publication and language contract

The website must consume `results/SITE_NUMBERS.json` (generated by `tools/site_numbers.py`), rendering `show[].sentence` and `four_arms` with the evidence class and experiment version. If unavailable, explicitly say “the record could not be read just now.” No silent older cached figure masquerading as real-time evidence, no manually adjusted percentages and no inferred positive cloud-work number.

The legacy `results/ABC_TABLE.json` should **not** be recreated: it was deliberately retired because it was a class-S model table, now at `docs/history/model_tables/ABC_TABLE_MODEL.json`; `tests/test_site_numbers.py` enforces this restriction. A website endpoint that demands it should be repaired to use the proper source. An HTTP 503 from the website proxy does not alone establish a GitHub outage.

**Careful terminology:** “up 20.4% by the project’s composite index” is not interchangeable with “20.4% more useful work for the same bill.” “+94.0% work-and-speed index” is not a standalone throughput measurement. “P95 down 4%” is directionally favorable for latency; a negative sign alone is not a loss. A 0.5% deadband is a policy threshold, not automatically a statistical confidence statement. A physically measured reduction in joules/request does not prove a cost saving if rental expenses or completed-work counts do not support it.

The current site and the evidence record must distinguish **standing engine V26** from **software-index evidence V25**, **GPU evidence V23**, and **Azure evidence V18**. Do not overwrite any of the source numbers simply to satisfy an outdated website “sanity guard.”

## 6. Claims that remain unestablished by these sources

- An independently certified A++ grade, global optimum over all possible controllers, or dominance on every metric.
- A single aggregate improvement percentage combining the Kubernetes index, GPU efficiency and cloud bill changes.
- V26 physical GPU and Azure effects; V26 remeasurements of affected Kubernetes controllers.
- A mathematical proof of globally attracting dynamics for the whole forced controller in all admissible plants.
- Production-safe zero-harm guarantees for arbitrary third-party actuators, without environment-specific bounded-error validation.

References: `OMNI_V26.json`, `docs/OMNI_V26.md`, `docs/OMNI_V25.md`, `docs/FORMAL_STATUS.md`, `results/OMNI_INDEX.json`, `results/SITE_NUMBERS.json`, `results/TWO_BILLS.json`, `results/gpu/V23_A10_CAP_FULL_ABC.md`, `results/live/AKS_STEADY_100_OMNI_V18.md`, `docs/WEBSITE_CLAIMS.md`, `docs/CLAIMS_REGISTER.md`, `docs/REFEREE_CHECKLIST.md`, and `tests/test_public_benchmark_contract.py`.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
