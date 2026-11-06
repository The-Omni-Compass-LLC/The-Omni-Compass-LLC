# The Omni index: more for the same, or the same for less

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every measure of every test is a ratio oriented so that above 1 is better for Omni-Compass on top of native: work (more is better), speed (a lower response time), machines (fewer), energy (less). A test's index is the geometric mean of its ratios; a category is the geometric mean of its tests; the headline is the geometric mean of the real categories, each weighted the same. Modelled muscles are shown beside it, never inside it. Every number is read from the test's own result file (`tools/omni_index.py`).

## Headline: Omni-Compass on top of native, real machines: **+12.9%** (more for the same, or the same for less, across work, speed, machines and energy)

| Category | Index | Work | Speed | Machines | Energy | Tests |
|---|---:|---:|---:|---:|---:|---:|
| Real Kubernetes (GitHub) | **+18.5%** | +6.5% | +68.8% | +2.9% | +1.5% | 12 |
| Real cloud (Azure AKS, billed) | **+7.5%** | +0.0% | +25.4% | -0.8% |  | 1 |
| Real card (NVIDIA, its own meter) | pending | | | | | the rerun on the current card controller (the 2026-10-02 run used the replaced one) |
| Modelled muscles (evidence S) | **+0.1%** | +0.0% |  |  | +0.1% | 6 |

Read: +10% in a column means 10% better for Omni-Compass in that measure (more work, a faster answer, fewer machines, less energy). The energy figure on GitHub's Kubernetes is a declared model, not a meter; Azure's machines are its own billed count.

## Every test

| Category | Test | Index | Work | Speed | Machines | Energy | Source |
|---|---|---:|---:|---:|---:|---:|---|
| Real Kubernetes (GitHub) | Steady same work: the load in steps at a fixed rate, ten pairs | **+29.9%** | +0.0% | +179.1% | +1.9% | +0.1% | `results/live/STEADY.md` |
| Real Kubernetes (GitHub) | Demand that wanders: up and down one step at a time, ten pairs | **+35.2%** | not taken | +141.5% | +2.0% | +0.3% | `results/live/WANDERING.md` |
| Real Kubernetes (GitHub) | All four in one run: load up and down one step at a time, ten pairs | **+40.5%** | +41.7% | +171.4% | +1.1% | +0.2% | `results/live/ALL_FOUR.md` |
| Real Kubernetes (GitHub) | Fairness: a noisy neighbour, ten pairs | **+5.6%** | not taken | +17.8% | +0.0% | +0.1% | `results/live/FAIRNESS.md` |
| Real Kubernetes (GitHub) | Faults: machine down, spike, runaway pod, blind probe, ten pairs | **+35.9%** | not taken | +150.4% | +0.2% | +0.1% | `results/live/FAULTS.md` |
| Real Kubernetes (GitHub) | A queue of jobs: cruise, then the emergency brake, ten pairs | **+18.5%** | not taken | +13.3% | +26.0% | +16.7% | `results/live/BATCH.md` |
| Real cloud (Azure AKS, billed) | Steady load, Azure's autoscaler underneath, five pairs (earlier engine; the rerun is running) | **+7.5%** | +0.0% | +25.4% | -0.8% | not taken | `results/live/AKS_BILL.md` |
| Real Kubernetes (GitHub) | Six organisms: Compute / AI / Cloud, the cluster inside, five pairs | **+11.1%** | +1.9% | +49.6% | +0.0% | +0.1% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Compute / AI / Cloud: the modelled stacks around the real cluster | **+0.0%** | +0.0% | not taken | not taken | +0.1% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: Physics / Robotics / Autonomous, the cluster inside, five pairs | **+9.3%** | +0.8% | +38.1% | +2.2% | +0.2% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Physics / Robotics / Autonomous: the modelled stacks around the real cluster | **+0.0%** | +0.0% | not taken | not taken | +0.1% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: Energy / Facility / Industrial, the cluster inside, five pairs | **+7.8%** | +0.5% | +31.6% | +1.9% | +0.3% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Energy / Facility / Industrial: the modelled stacks around the real cluster | **+0.1%** | +0.0% | not taken | not taken | +0.2% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: Distribution / Specialized, the cluster inside, five pairs | **+10.6%** | +2.0% | +45.6% | +0.1% | +0.6% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Distribution / Specialized: the modelled stacks around the real cluster | **+0.0%** | +0.0% | not taken | not taken | +0.1% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: the whole tower (656), the cluster inside, five pairs | **+15.5%** | +4.2% | +67.2% | +1.7% | +0.3% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | the whole tower (656): the modelled stacks around the real cluster | **+0.1%** | +0.0% | not taken | not taken | +0.2% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: the four stacked (1,226), the cluster inside, five pairs | **+8.9%** | +6.1% | +32.1% | +0.0% | +0.2% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | the four stacked (1,226): the modelled stacks around the real cluster | **+0.1%** | +0.0% | not taken | not taken | +0.2% | `results/live/SIX_KUBE.json` |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
