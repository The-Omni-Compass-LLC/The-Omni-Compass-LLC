# Referee decision record: V25 versus V26 and champion selection

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Date:** 2026-11-09. **Decision class:** engineering review and prospective test specification, not a new performance certificate, new engine release, completed multi-cloud trial, or verified universal optimum.

## Findings established by source comparisons

1. **Exactly one of 65 frozen fingerprinted engine files differs.** `OMNI_V25.json` identifies `omni_controller/controller.py` as SHA-256 `124823c23bdb7f413bf67622067954b73f324a3d5832c3348a95465efbf71dbb`; `OMNI_V26.json` gives `427f7d1d3cc23591cd186da69cead547a1eed96d28b4f30a21b0745463b55458`. The other 64 engine files match. Thus V26 is a Kubernetes-controller change, not a new GPU law, chip governor, or whole-stack tuning pass.
2. **The controlled fault:** under a competing batch queue with intermittent Pending pods, V25's HPA target repeatedly alternated between a 30% fail-up target and the native 50% target. A ten-minute adaptive immune/native hold was not reliably started on the return to native. V26 starts that hold when **another nongoverned workload** has Pending pods, excludes DaemonSets and the service's own pods, and preserves the older rule in other cases. See `docs/OMNI_V26.md`, `tests/test_neighbour_hold.py`, `docs/LOSS_CAUSES_2026-11-06.md`.
3. **The relevant limited evidence:** `results/model_gate/V26_BATCH_FLIP.md` is an **open-loop model/replay** of 30 repetitions. It reports target writes **16.13 → 2.67** (−83.5%); target changes after first **15.20 → 1.73** (−88.6%); and time below native target while another workload waits **22.17 → 4.83 seconds** (−78.2%). It does **not** remeasure closed-loop service goodput, latency, job completion, power, or total spend under V26.
4. **The other model gate is not a benefit trial:** `results/model_gate/V26_VS_V25.md` reports 104 identical modeled readings because the corrected branch never fires on its model support. A successful non-exercising gate cannot prove the new logic's service-level impact.
5. **The 20.463324% Kubernetes index is V25**, calculated from nine `results/live/V25_*.json` workloads in `results/OMNI_INDEX.json`. It is an equal-test geometric composite of unlike declared scores, not a raw percentage increase in successful Kubernetes throughput. A previously quoted **28.0351%** belongs to a website-audit request in `docs/audits/WEBSITE_LIVE_SOURCE_RECONCILIATION_2026-11-09.md`; its original index selection/weighting and run provenance are **not reconstructed here**. A numerical difference between 28.0351 and 20.463324 is not evidence of a V26 regression.
6. **Current V26 coverage:** a repository `results/live` directory inspection shows a V26 Kafka table (`V26_KAFKA.json`) but no `V26_...` Kubernetes three-run table. `results/CARRY.md` identifies 23 older outcomes as unchanged-code compatible and 93 as requiring new measurements; its snapshot counts are not a claim of current V26 whole-system certification. A carried experiment retains its original version tag. The GPU controller is byte-identical across V25 and V26; that does not prove the physical GPU effect carries across a changed environment.
7. **Existing adverse performance matters:** the V25 KAI batch/queue source `docs/LOSS_CAUSES_2026-11-06.md` records queue completions up to 6.8% later in a subset. Reducing target writes alone is not a sufficient repair unless those adverse outcomes disappear in fresh closed-loop tests.

## Freeze what is tested; do not silently revert or combine engine files

**Current engineering identity remains the fingerprinted V26 release**, with V25 preserved as a reproducible comparator. Neither is hereby declared the globally best-performing version. **No engine code is changed by this record.** A V27 or hybrid choice requires an independently fingerprinted complete candidate, not copying attractive individual files from incompatible versions without a new full integration, parity and benchmark campaign.

Use `tools/carry.py` to locate exactly which runner imports changed dependencies. A byte-identical imported governor supports a code-equivalence claim; it does not prove a universal physical performance equivalence. Preserve historical `OMNI_V*.json`, measured tables, report versions and raw receipts.

## Champion–challenger evaluation matrix

| Candidate and environment | Direct paired comparator | Required metrics and decision |
|---|---|---|
| **V25 Kubernetes** | native, V25, V26 under same fixed load, SLO and cluster | Baseline throughput/goodput, p50/p95/p99, error/SLO, pod waiting, batch completion, target flips, replica/machine-hours; V25 remains a comparator |
| **V26 Kubernetes** | same two baselines and competing-batch workloads | Demonstrate the target-flip repair **and** no material SLO, batch-completion, availability or total-cost regression; include KAI, Koordinator, Kueue, KEDA and scheduler interactions |
| **GPU A10 / A100** | native and unchanged candidate governor on same card, same workload and meter | Energy per successful request, useful work/time, p95/p99, throttling, bill, kill restores limits; include adverse A10 work-per-dollar third run; V26 Kubernetes patch cannot itself be called a new chip improvement |
| **Azure, AWS, GCP** | native and Omni on real matched cloud stacks | Completed successful work and total permitted bill together; disclose node-hour, control overhead, p95, failed work and repetitions; Azure V18 work/$ not measured |
| **Databases / messaging** | native and same fingerprinted engine for PostgreSQL, MySQL, MongoDB, Redis, Kafka | Native/Omni raw throughput, queue/backlog, p95 and resource costs; avoid promoting the extremely large Kafka composite to an undifferentiated system-wide claim |
| **Omni direct and supervisory stack** | native alone; Omni on native; direct Omni where actually supported | Never merge arms, versions or pricing; measure completed work, operating cost and hard health constraints separately |

## Mathematical selection rule

Let `E` be one **complete immutable candidate engine**, `p` its declared admissible factory profile and `d` the deployment/workload class. Let `W_d(E,p)` be useful work completed *within SLO* during equal measured duration, `C_d(E,p)>0` the total permitted cost, and `H_{d,j}` the safety/health metrics with declared directions and thresholds.

Choose a **champion only among qualified candidates**:
```text
Qualified(d) = { (E,p) :
    all mandatory safety and SLO bounds pass at their stated confidence;
    kill/restoration succeeds;
    evidence has sufficient paired reps and a current exact fingerprint;
    no material cost, throughput, latency, queue or fairness regression
        against the agreed native and frozen-champion baselines }
Champion(d) = argmax_(E,p in Qualified(d)) W_d(E,p) / C_d(E,p)
```
If `Qualified(d)` is empty, default to **native** in that domain rather than claiming an optimization. A controller may be configured to revert on observed safety violations; engineering cannot guarantee *zero observed negative samples on every metric* under noise, load changes and actuator delays without a specified deterministic invariant. Goodput/cost is not the same as bill reduction or increased throughput alone.

For a **single distributable product**, freeze one engine fingerprint `E*` with predeclared, version-controlled, domain-specific profiles `p_d`. Select `E*` only after the full required matrix clears; otherwise maintain a frozen comparison baseline and a candidate, without relabeling inherited results as V26. The winner is the **best among tested admissible alternatives**, not necessarily an unconstrained global optimum.

## Exact protocol to promote

1. Lock the V25 and V26 tree digests and all experimental parameters. Do not retune on the evaluation holdout.
2. Run short unit/fixture cases that intentionally activate V26's `_others_waiting` and `_hold_for_waiting` branches, DaemonSet, selector-unreadable, kill and recovery paths.
3. Execute paired native/V25/V26 Kubernetes on each preregistered scenario with randomized arm order, repeated equal-duration windows and the same worker resources, workload seeds, limits and logging.
4. Report absolute values and signed deltas for each metric. Treat smaller p95/failed requests/bill as gains, but a higher work or lower wait as a gain only under its declared aim. Never hide adverse results behind a geometric composite or 0.5% classification floor.
5. Test GPU and cloud separately, with source receipts. Use cross-version carry only for unchanged imported dependency bytes and keep original engine tags.
6. Build a cross-domain table of candidate eligibility, cost-adjusted goodput, uncertainty and all safety vetoes. Prefer robustness and guardrails to a single best-looking aggregate.
7. Only then create a new immutable release manifest, approved factory-profile file and signed release receipt, and publish the qualified claim to the website feed and manuals.

**Referee decision today:** V26's targeted controller repair has credible mechanistic support; its end-to-end service benefit and its superiority to V25 remain **not established**. The correct action is controlled challenger testing, not an unsupported claim of either a performance drop or a universal performance gain.

---
> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
