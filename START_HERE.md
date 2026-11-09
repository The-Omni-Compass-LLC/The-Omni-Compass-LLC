# Start here: Omni-Compass source, mathematics, runs and evidence hierarchy

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Purpose.** The stable entry point for engineers, independent referees, physicists, mathematicians, operators and counsel. Read from source and assumptions to run receipts and finally to claims. This map adds navigation rather than relocating historical files or silently breaking benchmark references. It reports the evidence state checked on **9 November 2026**, not a live telemetry feed.

## A. Identity, ownership and standing engine

1. [README and project orientation](README.md), [license](LICENSE), [notice](NOTICE), [disclosures](DISCLOSURES.md), and [agent rules](AGENTS.md).
2. [Frozen engine fingerprint: V26](OMNI_V26.json) and [V26 change explanation](docs/OMNI_V26.md). **V26 is the standing engine**; it fixes Kubernetes control behavior. Its SHA-256 program manifest is not, by itself, an experimental certificate.
3. [Release manifest](RELEASE_MANIFEST.json) and [last stored verification receipt](results/VERIFY_RECEIPT.txt). Inspect the receipt's commit and date before treating it as evidence for current `main`; a previous passing verifier cannot certify a subsequent commit.
4. [Change and version boundary](docs/REFEREE_VERSION_AND_BENCHMARK_STANDARD.md), including the conditions for functional inheritance and when physical reruns are necessary.

## B. Mathematical and physical statements

Read [mechanism of action](docs/MECHANISM_OF_ACTION.md), [canonical engine](docs/CANONICAL_ENGINE.md), [tracking theorem](docs/TRACKING_THEOREM.md), then [formal proof status](docs/FORMAL_STATUS.md). Consult the [evidence ledger](docs/EVIDENCE_LEDGER.md) for T (theorem), V (validated implementation), S (model), L (live software), and P (physical meter). Do not convert an invariant for an isolated channel into unconditional stability of every coupled plant. No unsolved mathematical problem is claimed proved by a benchmark.

## C. First-class empirical evidence, native against Omni

| Stage and claim | Source | Version / boundary |
|---|---|---|
| Current real-software composite index | [human-readable table](results/OMNI_INDEX.md), [JSON](results/OMNI_INDEX.json) | **V25** results; the composite is not a total-bill gain or a single throughput improvement. |
| Kubernetes and real software workloads | [index JSON](results/OMNI_INDEX.json), [how to interpret results](docs/HOW_TO_READ_THE_RESULTS.md) | Each test names its source and engine; adverse rows are part of the record. |
| Physical NVIDIA GPU | [A10 full-load paired receipt](results/gpu/V23_A10_CAP_FULL_ABC.md) and [chip interpretation](docs/THE_CHIPS.md) | **V23** A10 card; its work-per-dollar paired deltas include both gains and a loss. Older GPU receipts remain historical. |
| Linux CPU power | [run ledger](docs/RUN_LEDGER.md) | The ledger dated 27 October reports that bare-metal CPU power metering had **not** run; software CPU and Kubernetes checks do not replace a hardware power meter. |
| Azure AKS | [97 valid paired repetitions](results/live/AKS_STEADY_100_OMNI_V18.md) | **V18** cloud receipt; cloud work-per-dollar was not counted. |
| Amazon EKS and Google GKE | [run ledger](docs/RUN_LEDGER.md), [AWS queue](scripts/amazon_queue.txt), [AWS workflow](.github/workflows/eks-metered.yml), [GCP workflow](.github/workflows/gke-metered.yml) | Both queue files are now `switch=on`; historical preflight failures do **not** prove a new successful paid run. Check GitHub Actions and its raw artifacts. |
| Losses and limitations | [loss ledger](docs/LOSS_LEDGER.md), [claims register](docs/CLAIMS_REGISTER.md) | Disclose every adverse outcome and every still-open engineering or physical claim. |

**Never pool different versions or measurements into an invented “whole-system gain.”** Retain the underlying pairs, sample counts, confidence intervals, environments, cost boundaries and rejected/invalid attempts. Sign follows each metric's objective: lower latency is favorable, higher failed requests unfavorable. A policy deadband is not a statistical confidence interval.

## D. Execution and validation hierarchy

1. Read [referee checklist](docs/REFEREE_CHECKLIST.md), [run ledger](docs/RUN_LEDGER.md) and [state of play](docs/STATE_OF_PLAY.md); the latter two are dated/generated narratives and may lag new GitHub runs.
2. For a versioned source change, run `python3 tools/omni_version.py`, `python3 tools/site_numbers.py --check`, `python3 -m unittest -v tests.test_public_benchmark_contract` and `python3 verify.py --quick`. Record exact commit SHA and complete logs; **do not claim PASS without execution**.
3. For long-running and paid tests, review workflows and source commit before interpreting a result: [grid dispatcher](scripts/dispatch_grid.py), [GPU guide](docs/GPU_RUN_GUIDE.md), [cloud preflight](.github/workflows/cloud-check.yml), [AWS EKS](.github/workflows/eks-metered.yml), and [GCP GKE](.github/workflows/gke-metered.yml).
4. Compare native and Omni on identical permitted workloads. Distinguish P physical metering, L exercised software, and S simulations. A successful dispatch or workflow run is not a positive measured outcome.
5. Preserve historical result paths, versioned JSON manifests and run artifacts. Reorganize **navigation first**; migrate a file only with an explicit old-to-new mapping, reference scan, all affected generators/tests adjusted, and passing verification. A move that breaks an old receipt's citation destroys evidence rather than improving the hierarchy.

**Current ten-discipline referee assessment:** [November 9 ten-lens audit](docs/audits/TEN_LENS_REFEREE_AUDIT_2026-11-09.md), including separate grades, physical receipts, math/physics scope and A+ remediation thresholds.

## E. Presentation and due diligence

[Documentation index by reader](docs/README.md) → [evidence registry](docs/EVIDENCE_LEDGER.md) → [claims register](docs/CLAIMS_REGISTER.md) → [benchmark referee audit](docs/audit/README.md) → [referee cross-version standard](docs/REFEREE_VERSION_AND_BENCHMARK_STANDARD.md) → [report card](docs/REPORT_CARD.md). The original experiment remains the primary authority when a summary conflicts with it.

**Independence:** run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code unless a specific third-party replication receipt establishes otherwise. A++ is a target for review quality, not an independently conferred grade. Do not present a GitHub file move, check, or model as a physical benchmark.

---

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
