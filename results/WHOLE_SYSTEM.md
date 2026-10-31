# The whole system: Omni-Compass at every layer, composed by the product law

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's question of 20 October 2026: the cloud is the wire between the chip at one end and the software at the other; Omni-Compass sits at both ends and at every layer between; what is the total? This page answers it from the tables that stand, by one rule written once in `tools/whole_system.py`, which rebuilds the page and `results/WHOLE_SYSTEM.json` from them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The equation

For a gauge g with its declared aim a(g) (higher for work; lower for a wait; spent for a resource or a bill) and a layer ℓ measured native nℓ and with Omni-Compass oℓ, the layer's ratio is oriented toward the aim, so that above 1 is a GAIN at every layer alike:

  Rℓ(g) = oℓ / nℓ when a(g) is higher;  Rℓ(g) = nℓ / oℓ when a(g) is lower or spent.

Each layer is measured with the layer under it running as native runs it (the cluster's tests against the HPA; the governors' against the orchestrator as shipped; the cloud's against Azure's own autoscaler; the card's against the card's own limiter). The layers compose by multiplication, because each ratio is taken on what the layer under it hands up:

  R(g) = ∏ℓ Rℓ(g),   G(g) = R(g) − 1,   log R(g) = Σℓ log Rℓ(g).

The interval. A table gives, per run, the paired difference d = o − n with its 95% interval [lo, hi] over n paired repetitions (the exact Student t), so SE(d) = (hi − lo) / (2 t₀.₉₇₅,ₙ₋₁), and by the delta method SE(log R) = SE(d) / o. The three runs A, B and C of one test are pooled by inverse variance (μ = Σwᵢμᵢ / Σwᵢ, Var = 1 / Σwᵢ, wᵢ = 1/σᵢ²). A layer with k tests takes the mean of their log ratios (the geometric mean of the ratios, the Omni index's rule), Var = Σσᵢ² / k². The layers add in the log and their variances add, because every layer was measured in its own runs. The total's 95% interval is exp(μ ± 1.96 σ). The index over the gauges is the mean of the gauge logs; its interval is given under two bounds, the gauges independent (Var = Σσ² / k²) and the gauges perfectly correlated inside a run (σ = Σσ / k).

What is composed (the founder's order of 31 October 2026). The whole organism is shown at the software end: **work, speed and machines are composed**. **The energy and the bill are held at native's** (exactly 1, shown beside, never composed): on the cluster the energy is a declared model of the machines row, never a meter, so composing it would count the fewer machines twice and claim a saving at the chip that no meter read; the cloud is the wire and its bill is kept exactly as native's, the benefit being more work for the same bill. **The chip and the wire enter as exactly 1 on every gauge**: the chip is kept exactly as native runs it (its own meter at the factory tune reads it so, section 2), and the cloud's runs are the check that the software end's benefit holds through the wire. The index over the gauges is the mean of the three composed gauges' logs: more work, faster, on fewer machines, for the same power and the same bill.

Two readings of the same numbers. **By the index's rule** a gauge of a test enters only when its three-run reading is GAIN, LOSS or power given in all three of our runs; a STEADY gauge, a disagreement, or a table of one run enters as exactly 1 with no variance (nothing inside the noise is claimed either way). **With every interval carried**, every measured gauge enters with its pooled estimate and its variance whatever its reading, and the total's interval says what the noise allows.

What the composition is, and is not. No run here stacked the layers: each factor is one layer's own measurement with the layer under it native. The product is a modelled composition (**class S**) of class P and class L measurements, under the assumption that a layer's ratio does not change when the layers under or over it also carry Omni-Compass (separability). Section 4 tests that assumption where the tables can (the governors' four ways). The stacked run, Omni-Compass at every layer at once against native at every layer, is the measurement that would replace this composition; until it exists this page is the answer the standing tables give, with its assumptions in the open. The layers also stand on different engines, each named in its row below (the card on omni-v21's card governor, the A100 three runs), so the composition is across engines, said so here, and remade as each layer's three runs on the engine that stands land.

## 2. The layers, each from its own table

Each layer's own measurement, read two ways, and what it enters the composition as (section 1).

| Layer | Tests | Gauge | Measured, by the index's rule | Measured, every interval carried | Word (carried) | Enters the composition as |
|---|---:|---|---|---|---|---|
| 1. the card (the chip), class P | 1 | work (more) | ×1.0000 (+0.00%; +0.00% to +0.00%) | ×1.0000 (+0.00%; +0.00% to +0.00%) | STEADY | the chip, kept exactly as native runs it: enters as exactly 1, its three runs shown beside |
|  |  | speed (the 95th percentile response, lower) | ×1.0000 (+0.00%; +0.00% to +0.00%) | ×0.9997 (-0.03%; -1.2% to +1.1%) | STEADY | the chip, kept exactly as native runs it: enters as exactly 1, its three runs shown beside |
|  |  | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0000 (+0.00%; +0.00% to +0.00%) | ×0.9989 (-0.1%; -0.6% to +0.4%) | STEADY | the chip, kept exactly as native runs it: enters as exactly 1, its three runs shown beside |
| 3. the cluster (Kubernetes, its add-ons, its governors), class L | 22 | work (more) | ×1.1701 (+17.0%; +14.9% to +19.1%) | ×1.1701 (+17.0%; +14.9% to +19.1%) | GAIN | its own factor |
|  |  | speed (the 95th percentile response, lower) | ×1.4298 (+43.0%; +39.6% to +46.4%) | ×1.4304 (+43.0%; +39.6% to +46.5%) | GAIN | its own factor |
|  |  | machines (fewer) | ×1.0697 (+7.0%; +6.2% to +7.7%) | ×1.0697 (+7.0%; +6.2% to +7.7%) | GAIN | its own factor |
|  |  | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0449 (+4.5%; +4.0% to +5.0%) | ×1.0452 (+4.5%; +4.0% to +5.0%) | GAIN | held at native's, the same power: on the cluster a declared model of the machines row, never a meter, so it is shown, not composed |
| 4. the services on the cluster, class L | 17 | work (more) | ×1.0014 (+0.1%; +0.1% to +0.1%) | ×1.0055 (+0.5%; -0.5% to +1.6%) | GAIN | its own factor |
|  |  | speed (the 95th percentile response, lower) | ×1.0014 (+0.1%; -0.1% to +0.4%) | ×1.0011 (+0.1%; -0.5% to +0.7%) | STEADY | its own factor |
|  |  | machines (fewer) | ×1.0232 (+2.3%; +2.0% to +2.7%) | ×1.0224 (+2.2%; +1.8% to +2.7%) | GAIN | its own factor |
|  |  | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0054 (+0.5%; +0.1% to +1.0%) | ×1.0071 (+0.7%; +0.2% to +1.2%) | GAIN | held at native's, the same power: on the cluster a declared model of the machines row, never a meter, so it is shown, not composed |
| 5. the cloud (Azure, the bill metered), class L | 4 | speed (the 95th percentile response, lower) | ×1.0000 (+0.00%; +0.00% to +0.00%) | ×1.0434 (+4.3%; -15.8% to +29.3%) | GAIN | the wire, its bill kept exactly as native's: enters as exactly 1, its runs shown beside as the check that the benefit holds |
|  |  | machines (fewer) | ×1.0000 (+0.00%; +0.00% to +0.00%) | ×0.9790 (-2.1%; -7.9% to +4.0%) | power given | the wire, its bill kept exactly as native's: enters as exactly 1, its runs shown beside as the check that the benefit holds |
|  |  | the bill (the cloud's metered bill) | ×1.0000 (+0.00%; +0.00% to +0.00%) | ×0.9899 (-1.0%; -10.5% to +9.5%) | power given | the wire, its bill kept exactly as native's: enters as exactly 1, its runs shown beside as the check that the benefit holds |
| 2. the machine (the kernel, bare metal, Kepler) | 0 | every gauge | not yet run (register row 79) | not yet run | not measured | exactly 1 |

The card's primary gauge, work per energy (served requests per kJ): ×0.9989 (-0.1%; -0.6% to +0.4%) over its 3 runs, STEADY, under the floor (the three runs' mean 0.11%); the same runs read the 95th percentile response +0.03% (the runs disagree) and the energy drawn +0.1% (STEADY, under the floor (the three runs' mean 0.12%)). It is omni-v21's card governor at the factory tune (the dial at the max) on top of native's power cap at 70% of the card's top, read by the card's own meter (class P). The chip's work and energy read STEADY at the factory tune, so the chip enters the composition as exactly 1: the chip kept exactly as native runs it is what its own meter reads. The tune-down's three runs (results/gpu/V21_A100_SAVE_ABC.md) read the same requests served for 0.7% to 0.85% less of the card's energy in each run, GAIN by the mean of the three runs: a changed tune, its own record, shown and never composed.

### Every test behind the layers

**1. the card (the chip), class P**

- NVIDIA A100 (SXM4, 40 GB) on Lambda, the card's own meter, Omni-Compass on the power limit and the clock ceiling at the factory tune (the dial at the max), native's power cap at 70% of the card's top, 5 paired repetitions in each of three runs (omni-v21; `results/gpu/V21_A100_CAP_ABC.md`): work: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; speed: ×0.9997 (-0.03%; -1.2% to +1.1%), the runs disagree; energy: ×0.9989 (-0.1%; -0.6% to +0.4%), STEADY, under the floor

**3. the cluster (Kubernetes, its add-ons, its governors), class L**

- Steady same work: the load in steps at a fixed rate, ten pairs, three runs (omni-v21; `results/live/V21_STEADY.json`): work: the same by design; speed: ×2.9422 (+194.2%; +113.7% to +305.1%), GAIN in all three of our runs; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×1.0015 (+0.2%; +0.04% to +0.3%), STEADY, under the floor
- Demand that wanders: up and down one step at a time, ten pairs, three runs (omni-v21; `results/live/V21_WANDERING.json`): speed: ×2.3322 (+133.2%; +102.2% to +169.0%), GAIN in all three of our runs; machines: ×1.0000 (+0.00%; -0.00% to +0.00%), STEADY, the same; energy: ×1.0030 (+0.3%; +0.2% to +0.4%), STEADY, under the floor
- All four in one run: load up and down one step at a time, ten pairs, three runs (omni-v21; `results/live/V21_ALL_FOUR.json`): work: ×1.3691 (+36.9%; +32.1% to +42.0%), GAIN in all three of our runs; speed: ×2.2239 (+122.4%; +83.6% to +169.4%), GAIN in all three of our runs; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×1.0010 (+0.1%; -0.01% to +0.2%), STEADY, under the floor
- Fairness: a noisy neighbour, ten pairs, three runs (omni-v21; `results/live/V21_FAIRNESS.json`): speed: ×1.0899 (+9.0%; +2.7% to +15.7%), GAIN by the mean of our three runs, beyond the noise in 1 of 3; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×0.9999 (-0.01%; -0.1% to +0.1%), STEADY, under the floor
- Faults: machine down, spike, runaway pod, blind probe, ten pairs, three runs (omni-v21; `results/live/V21_FAULTS.json`): speed: ×2.2005 (+120.0%; +92.5% to +151.5%), GAIN in all three of our runs; machines: ×1.0004 (+0.04%; -0.02% to +0.1%), STEADY, under the floor; energy: ×1.0049 (+0.5%; +0.2% to +0.8%), GAIN by the mean of our three runs, beyond the noise in 1 of 3
- A queue of jobs: cruise, then the emergency brake, ten pairs, three runs (omni-v21; `results/live/V21_BATCH.json`): speed: ×1.1402 (+14.0%; +11.4% to +16.7%), GAIN in all three of our runs; machines: ×1.1642 (+16.4%; +10.0% to +23.2%), GAIN in all three of our runs; energy: ×1.1076 (+10.8%; +6.6% to +15.0%), GAIN in all three of our runs
- A public day of demand: the Google cluster trace of 2011 replayed one step at a time, ten pairs, three runs (omni-v21; `results/live/V21_TRACE_GOOGLE2011.json`): speed: ×2.4845 (+148.4%; +118.3% to +182.7%), GAIN in all three of our runs; machines: ×1.0000 (+0.00%; -0.00% to +0.00%), STEADY, the same; energy: ×1.0036 (+0.4%; +0.3% to +0.5%), STEADY, under the floor
- With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs (omni-v21; `results/live/V21_KEDA_CPU_REQUESTS.json`): speed: ×2.0662 (+106.6%; +91.3% to +123.2%), GAIN in all three of our runs; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×0.9844 (-1.6%; -1.9% to -1.3%), power given in all three of our runs
- With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs (omni-v21; `results/live/V21_KEDA_REQUESTS.json`): speed: ×3.7262 (+272.6%; +209.3% to +349.0%), GAIN in all three of our runs; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×0.9784 (-2.2%; -2.4% to -1.9%), power given in all three of our runs
- Goldilocks and the VPA's recommender, Omni-Compass on top (omni-v21; `results/live/V21_GOLDILOCKS.json`): speed: ×2.4675 (+146.8%; +119.5% to +177.4%), GAIN in all three of our runs; machines: ×1.0000 (+0.00%; -0.00% to +0.00%), STEADY, the same; energy: ×0.9836 (-1.6%; -1.9% to -1.4%), power given in all three of our runs
- CruiseKube applying its own recommendations, Omni-Compass on top (omni-v21; `results/live/V21_CRUISEKUBE.json`): speed: ×0.9894 (-1.1%; -1.8% to -0.3%), LOSS by the mean of our three runs, beyond the noise in 1 of 3; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×1.0010 (+0.1%; -0.1% to +0.3%), STEADY, under the floor
- Omni-Compass on top of the Kubernetes scheduler as shipped (omni-v12; `results/live/V12_VANILLA.json`): speed: ×0.9536 (-4.6%; -7.1% to -2.1%), LOSS by the mean of our three runs, beyond the noise in 1 of 3; machines: ×1.1623 (+16.2%; +10.0% to +22.8%), GAIN in all three of our runs; energy: ×1.1099 (+11.0%; +6.8% to +15.3%), GAIN in all three of our runs
- Omni-Compass on top of Kueue (the four ways, compass against native) (omni-v12; `results/live/V12_KUEUE_4W_TOP.json`): speed: ×0.9884 (-1.2%; -4.8% to +2.6%), the runs disagree; machines: ×1.1172 (+11.7%; +6.1% to +17.6%), GAIN in all three of our runs; energy: ×1.0785 (+7.9%; +4.2% to +11.6%), GAIN in all three of our runs
- Omni-Compass on top of Volcano (the four ways, compass against native) (omni-v12; `results/live/V12_VOLCANO_4W_TOP.json`): speed: ×0.9183 (-8.2%; -16.3% to +0.7%), LOSS by the mean of our three runs, beyond the noise in 0 of 3; machines: ×1.1738 (+17.4%; +9.1% to +26.3%), GAIN in all three of our runs; energy: ×1.1146 (+11.5%; +6.2% to +17.0%), GAIN by the mean of our three runs, beyond the noise in 2 of 3
- Omni-Compass on top of the KAI scheduler (the four ways, compass against native) (omni-v12; `results/live/V12_KAI_4W_TOP.json`): speed: ×0.9667 (-3.3%; -7.0% to +0.5%), LOSS by the mean of our three runs, beyond the noise in 0 of 3; machines: ×1.0861 (+8.6%; +4.5% to +12.9%), GAIN by the mean of our three runs, beyond the noise in 2 of 3; energy: ×1.0584 (+5.8%; +3.1% to +8.7%), GAIN by the mean of our three runs, beyond the noise in 2 of 3
- Omni-Compass on top of Koordinator (the four ways, compass against native) (omni-v12; `results/live/V12_KOORDINATOR_4W_TOP.json`): speed: ×1.0746 (+7.5%; +5.1% to +9.9%), GAIN by the mean of our three runs, beyond the noise in 2 of 3; machines: ×1.0055 (+0.6%; -0.1% to +1.2%), GAIN by the mean of our three runs, beyond the noise in 0 of 3; energy: ×1.0046 (+0.5%; +0.1% to +0.9%), GAIN by the mean of our three runs, beyond the noise in 0 of 3
- Omni-Compass on top of the scheduler's bin-packing profile (the four ways, compass against native) (omni-v12; `results/live/V12_BINPACK_4W_TOP.json`): speed: ×1.0108 (+1.1%; -2.5% to +4.8%), the runs disagree; machines: ×1.1523 (+15.2%; +8.1% to +22.9%), GAIN in all three of our runs; energy: ×1.1004 (+10.0%; +5.5% to +14.8%), GAIN in all three of our runs
- Omni-Compass on top of Crane (the four ways, compass against native) (omni-v12; `results/live/V12_CRANE_4W_TOP.json`): speed: ×1.0105 (+1.0%; -0.5% to +2.6%), the runs disagree; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×0.9963 (-0.4%; -0.6% to -0.1%), STEADY, under the floor
- Omni-Compass on top of KubeRay (the four ways, compass against native) (omni-v12; `results/live/V12_KUBERAY_4W_TOP.json`): speed: ×0.9754 (-2.5%; -6.3% to +1.6%), LOSS by the mean of our three runs, beyond the noise in 0 of 3; machines: ×1.0134 (+1.3%; +0.4% to +2.3%), GAIN by the mean of our three runs, beyond the noise in 1 of 3; energy: ×1.0085 (+0.9%; +0.2% to +1.5%), GAIN by the mean of our three runs, beyond the noise in 0 of 3
- Omni-Compass on top of Karmada (the four ways, compass against native) (omni-v12; `results/live/V12_KARMADA_4W_TOP.json`): speed: ×0.9125 (-8.8%; -13.6% to -3.7%), LOSS by the mean of our three runs, beyond the noise in 2 of 3; machines: ×1.1118 (+11.2%; +4.5% to +18.3%), GAIN by the mean of our three runs, beyond the noise in 1 of 3; energy: ×1.0743 (+7.4%; +2.9% to +12.2%), GAIN by the mean of our three runs, beyond the noise in 1 of 3
- Omni-Compass on top of Open Cluster Management (the four ways, compass against native) (omni-v12; `results/live/V12_OCM_4W_TOP.json`): speed: ×0.9197 (-8.0%; -13.9% to -1.7%), LOSS by the mean of our three runs, beyond the noise in 1 of 3; machines: ×1.0257 (+2.6%; +0.7% to +4.4%), GAIN by the mean of our three runs, beyond the noise in 1 of 3; energy: ×1.0181 (+1.8%; +0.4% to +3.2%), GAIN by the mean of our three runs, beyond the noise in 0 of 3
- Omni-Compass on top of Armada (the four ways, compass against native) (omni-v12; `results/live/V12_ARMADA_4W_TOP.json`): speed: ×1.7951 (+79.5%; +70.0% to +89.5%), GAIN in all three of our runs; machines: ×1.7059 (+70.6%; +66.4% to +74.9%), GAIN in all three of our runs; energy: ×1.4476 (+44.8%; +42.4% to +47.1%), GAIN in all three of our runs

**4. the services on the cluster, class L**

- pgbench `select`: the pooler's pool size, three paired repetitions, three runs (omni-v21; `results/live/V21_PGBENCH.json`): work: ×0.9999 (-0.01%; -0.1% to +0.04%), STEADY, under the floor; speed: ×0.9634 (-3.7%; -8.8% to +1.7%), the runs disagree; machines: ×1.0757 (+7.6%; +6.6% to +8.6%), GAIN in all three of our runs; energy: ×0.9934 (-0.7%; -1.1% to -0.2%), power given by the mean of our three runs, beyond the noise in 0 of 3
- pgbench `simple_update`: the pooler's pool size, three paired repetitions, three runs (omni-v21; `results/live/V21_PGBENCH.json`): work: ×0.9988 (-0.1%; -0.3% to +0.1%), STEADY, under the floor; speed: ×0.9948 (-0.5%; -3.3% to +2.3%), the runs disagree; machines: ×1.0131 (+1.3%; +1.0% to +1.7%), GAIN by the mean of our three runs, beyond the noise in 1 of 3; energy: ×0.9990 (-0.1%; -0.2% to +0.01%), STEADY, under the floor
- pgbench `tpcb_hot`: the pooler's pool size, three paired repetitions, three runs (omni-v21; `results/live/V21_PGBENCH.json`): work: ×1.0005 (+0.1%; -0.1% to +0.2%), STEADY, under the floor; speed: ×1.0034 (+0.3%; -2.6% to +3.3%), GAIN by the mean of our three runs, beyond the noise in 0 of 3; machines: ×1.0467 (+4.7%; +3.9% to +5.4%), GAIN by the mean of our three runs, beyond the noise in 1 of 3; energy: ×0.9998 (-0.02%; -1.1% to +1.0%), STEADY, under the floor
- Kafka `burst`: the consumer group's size, three paired repetitions, three runs (omni-v21; `results/live/V21_KAFKA.json`): work: ×1.0015 (+0.2%; +0.1% to +0.2%), STEADY, under the floor; speed: ×0.9962 (-0.4%; -1.8% to +1.0%), the runs disagree; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×1.0193 (+1.9%; +0.4% to +3.5%), GAIN by the mean of our three runs, beyond the noise in 0 of 3
- Kafka `heavy`: the consumer group's size, three paired repetitions, three runs (omni-v21; `results/live/V21_KAFKA.json`): work: ×0.9982 (-0.2%; -0.4% to +0.02%), STEADY, under the floor; speed: ×0.9933 (-0.7%; -2.6% to +1.3%), the runs disagree; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), power given by the mean of our three runs, beyond the noise in 1 of 3; energy: ×1.0043 (+0.4%; -0.4% to +1.3%), the runs disagree
- Kafka `light`: the consumer group's size, three paired repetitions, three runs (omni-v21; `results/live/V21_KAFKA.json`): work: ×0.9969 (-0.3%; -0.6% to -0.1%), STEADY, under the floor; speed: ×1.0017 (+0.2%; -1.6% to +2.0%), the runs disagree; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), power given by the mean of our three runs, beyond the noise in 0 of 3; energy: ×1.0045 (+0.4%; +0.3% to +0.6%), STEADY, under the floor
- Redis `burst`: the cache's memory ceiling, three paired repetitions, three runs (omni-v21; `results/live/V21_REDIS.json`): work: ×0.9997 (-0.03%; -0.04% to -0.01%), STEADY, under the floor; speed: ×1.0002 (+0.02%; -0.02% to +0.1%), STEADY, under the floor; machines: ×1.0136 (+1.4%; +1.4% to +1.4%), GAIN in all three of our runs
- Redis `large`: the cache's memory ceiling, three paired repetitions, three runs (omni-v21; `results/live/V21_REDIS.json`): work: ×1.0168 (+1.7%; +1.6% to +1.7%), GAIN in all three of our runs; speed: ×1.0005 (+0.05%; +0.00% to +0.1%), STEADY, under the floor; machines: ×0.9867 (-1.3%; -1.8% to -0.9%), power given by the mean of our three runs, beyond the noise in 1 of 3
- Redis `small`: the cache's memory ceiling, three paired repetitions, three runs (omni-v21; `results/live/V21_REDIS.json`): work: ×1.0067 (+0.7%; +0.6% to +0.7%), GAIN by the mean of our three runs, beyond the noise in 2 of 3; speed: ×0.9996 (-0.04%; -0.1% to -0.01%), STEADY, under the floor; machines: ×0.9922 (-0.8%; -0.8% to -0.8%), power given by the mean of our three runs, beyond the noise in 2 of 3
- YCSB `b`: the storage engine's cache size, three paired repetitions, three runs (omni-v21; `results/live/V21_YCSB.json`): work: ×1.0000 (+0.00%; -0.02% to +0.03%), STEADY, under the floor; speed: ×0.9979 (-0.2%; -1.2% to +0.8%), the runs disagree; machines: ×1.0032 (+0.3%; +0.3% to +0.3%), STEADY, under the floor
- YCSB `burst`: the storage engine's cache size, three paired repetitions, three runs (omni-v21; `results/live/V21_YCSB.json`): work: ×0.9999 (-0.01%; -0.1% to +0.03%), STEADY, under the floor; speed: ×0.9934 (-0.7%; -1.4% to +0.1%), LOSS by the mean of our three runs, beyond the noise in 0 of 3; machines: ×1.0037 (+0.4%; +0.3% to +0.4%), power given by the mean of our three runs, beyond the noise in 1 of 3
- YCSB `c`: the storage engine's cache size, three paired repetitions, three runs (omni-v21; `results/live/V21_YCSB.json`): work: ×1.0001 (+0.01%; -0.00% to +0.03%), STEADY, under the floor; speed: ×1.0004 (+0.04%; -0.3% to +0.4%), STEADY, under the floor; machines: ×1.0045 (+0.5%; +0.3% to +0.6%), the runs disagree
- YCSB `f`: the storage engine's cache size, three paired repetitions, three runs (omni-v21; `results/live/V21_YCSB.json`): work: ×1.0000 (-0.00%; -0.1% to +0.1%), STEADY, under the floor; speed: ×1.0044 (+0.4%; -0.5% to +1.4%), the runs disagree; machines: ×0.9570 (-4.3%; -7.9% to -0.5%), power given by the mean of our three runs, beyond the noise in 0 of 3
- sysbench `burst`: the buffer pool's size, three paired repetitions, three runs (omni-v21; `results/live/V21_SYSBENCH.json`): work: ×0.9981 (-0.2%; -0.6% to +0.2%), STEADY, under the floor; speed: ×1.0270 (+2.7%; +0.4% to +5.0%), GAIN by the mean of our three runs, beyond the noise in 0 of 3; machines: ×1.1017 (+10.2%; +10.0% to +10.3%), GAIN in all three of our runs; energy: ×0.9902 (-1.0%; -2.1% to +0.1%), power given by the mean of our three runs, beyond the noise in 0 of 3
- sysbench `read_only`: the buffer pool's size, three paired repetitions, three runs (omni-v21; `results/live/V21_SYSBENCH.json`): work: ×0.9998 (-0.02%; -0.3% to +0.3%), STEADY, under the floor; speed: ×0.9999 (-0.01%; -0.9% to +0.9%), the runs disagree; machines: ×1.2331 (+23.3%; +17.8% to +29.1%), GAIN by the mean of our three runs, beyond the noise in 1 of 3; energy: ×0.9932 (-0.7%; -0.9% to -0.5%), power given by the mean of our three runs, beyond the noise in 1 of 3
- sysbench `read_write`: the buffer pool's size, three paired repetitions, three runs (omni-v21; `results/live/V21_SYSBENCH.json`): work: ×1.0008 (+0.1%; -0.2% to +0.4%), STEADY, under the floor; speed: ×1.0196 (+2.0%; +0.04% to +3.9%), the runs disagree; machines: ×0.9797 (-2.0%; -5.6% to +1.6%), the runs disagree; energy: ×1.0091 (+0.9%; -1.0% to +2.9%), the runs disagree
- sysbench `update_index`: the buffer pool's size, three paired repetitions, three runs (omni-v21; `results/live/V21_SYSBENCH.json`): work: ×1.0779 (+7.8%; -9.4% to +28.2%), the runs disagree; speed: ×1.0255 (+2.5%; -3.1% to +8.5%), the runs disagree; machines: ×1.0000 (+0.00%; +0.00% to +0.00%), STEADY, the same; energy: ×1.0599 (+6.0%; +1.6% to +10.5%), GAIN by the mean of our three runs, beyond the noise in 0 of 3

**5. the cloud (Azure, the bill metered), class L**

- Azure Kubernetes Service, Azure's own cluster autoscaler underneath, the compass law, 4 paired repetitions, one run (the engine of commit 5b2832f (4 October 2026); `results/live/AKS_BILL.md`): speed: ×1.2537 (+25.4%; -24.3% to +107.6%), one run: the interval includes zero; machines: ×0.9918 (-0.8%; -18.8% to +21.2%), one run: the interval includes zero; bill: ×0.9918 (-0.8%; -18.8% to +21.2%), one run: the interval includes zero
- Azure Kubernetes Service, Azure's own cluster autoscaler underneath, the steady set, 98 paired repetitions in one run (Omni-Compass at the tune-down on the machines alone) (omni-v18; `results/live/AKS_STEADY_100_OMNI_V18.md`): speed: ×1.0418 (+4.2%; -2.4% to +11.2%), one run: the interval includes zero; machines: ×0.9880 (-1.2%; -3.6% to +1.2%), one run: the interval includes zero; bill: ×0.9880 (-1.2%; -3.6% to +1.2%), one run: the interval includes zero
- Azure Kubernetes Service, a 4-worker fleet, the steady set, 5 paired repetitions, one run (omni-v1; `results/live/V1_AKS_STEADY.json`): speed: ×1.0215 (+2.2%; -20.9% to +32.0%), one run: the interval includes zero; machines: ×0.9623 (-3.8%; -15.6% to +9.7%), one run: the interval includes zero
- Azure Kubernetes Service, a 4-worker fleet, the burst, 5 paired repetitions, one run (omni-v1; `results/live/V1_AKS_BURST.json`): speed: ×0.8884 (-11.2%; -53.2% to +68.7%), one run: the interval includes zero; machines: ×0.9744 (-2.6%; -6.0% to +1.0%), one run: the interval includes zero

## 3. The total

| Scope | Reading | Gauge | R(g) | G(g), 95% interval | Word |
|---|---|---|---:|---|---|
| with the card (the chip held exactly as native runs it) | by the index's rule | work (more) | ×1.1717 | +17.2% (+15.1% to +19.3%) | GAIN |
| with the card (the chip held exactly as native runs it) | by the index's rule | speed (the 95th percentile response, lower) | ×1.4317 | +43.2% (+39.8% to +46.6%) | GAIN |
| with the card (the chip held exactly as native runs it) | by the index's rule | machines (fewer) | ×1.0945 | +9.5% (+8.6% to +10.3%) | GAIN |
| with the card (the chip held exactly as native runs it) | by the index's rule | energy (held at native's: the same power) | ×1 | exactly 1: held at native's, the same power: on the cluster a declared model of the machines row, never a meter, so it is shown, not composed | held |
| with the card (the chip held exactly as native runs it) | by the index's rule | the bill (held at native's: the same bill) | ×1 | exactly 1: held at native's, the same bill: the cloud is the wire, and the benefit is more work for the same bill | held |
| with the card (the chip held exactly as native runs it) | by the index's rule | **the index over work, speed and machines** | **×1.2245** | **+22.5%** (gauges independent +21.2% to +23.7%; gauges correlated +20.4% to +24.5%) | GAIN |
| with the card (the chip held exactly as native runs it) | every interval carried | work (more) | ×1.1765 | +17.6% (+15.2% to +20.1%) | GAIN |
| with the card (the chip held exactly as native runs it) | every interval carried | speed (the 95th percentile response, lower) | ×1.4320 | +43.2% (+39.7% to +46.8%) | GAIN |
| with the card (the chip held exactly as native runs it) | every interval carried | machines (fewer) | ×1.0937 | +9.4% (+8.5% to +10.3%) | GAIN |
| with the card (the chip held exactly as native runs it) | every interval carried | energy (held at native's: the same power) | ×1 | exactly 1: held at native's, the same power: on the cluster a declared model of the machines row, never a meter, so it is shown, not composed | held |
| with the card (the chip held exactly as native runs it) | every interval carried | the bill (held at native's: the same bill) | ×1 | exactly 1: held at native's, the same bill: the cloud is the wire, and the benefit is more work for the same bill | held |
| with the card (the chip held exactly as native runs it) | every interval carried | **the index over work, speed and machines** | **×1.2260** | **+22.6%** (gauges independent +21.2% to +24.0%; gauges correlated +20.4% to +24.8%) | GAIN |
| without the card (the cluster, the services and the cloud) | by the index's rule | work (more) | ×1.1717 | +17.2% (+15.1% to +19.3%) | GAIN |
| without the card (the cluster, the services and the cloud) | by the index's rule | speed (the 95th percentile response, lower) | ×1.4317 | +43.2% (+39.8% to +46.6%) | GAIN |
| without the card (the cluster, the services and the cloud) | by the index's rule | machines (fewer) | ×1.0945 | +9.5% (+8.6% to +10.3%) | GAIN |
| without the card (the cluster, the services and the cloud) | by the index's rule | energy (held at native's: the same power) | ×1 | exactly 1: held at native's, the same power: on the cluster a declared model of the machines row, never a meter, so it is shown, not composed | held |
| without the card (the cluster, the services and the cloud) | by the index's rule | the bill (held at native's: the same bill) | ×1 | exactly 1: held at native's, the same bill: the cloud is the wire, and the benefit is more work for the same bill | held |
| without the card (the cluster, the services and the cloud) | by the index's rule | **the index over work, speed and machines** | **×1.2245** | **+22.5%** (gauges independent +21.2% to +23.7%; gauges correlated +20.4% to +24.5%) | GAIN |
| without the card (the cluster, the services and the cloud) | every interval carried | work (more) | ×1.1765 | +17.6% (+15.2% to +20.1%) | GAIN |
| without the card (the cluster, the services and the cloud) | every interval carried | speed (the 95th percentile response, lower) | ×1.4320 | +43.2% (+39.7% to +46.8%) | GAIN |
| without the card (the cluster, the services and the cloud) | every interval carried | machines (fewer) | ×1.0937 | +9.4% (+8.5% to +10.3%) | GAIN |
| without the card (the cluster, the services and the cloud) | every interval carried | energy (held at native's: the same power) | ×1 | exactly 1: held at native's, the same power: on the cluster a declared model of the machines row, never a meter, so it is shown, not composed | held |
| without the card (the cluster, the services and the cloud) | every interval carried | the bill (held at native's: the same bill) | ×1 | exactly 1: held at native's, the same bill: the cloud is the wire, and the benefit is more work for the same bill | held |
| without the card (the cluster, the services and the cloud) | every interval carried | **the index over work, speed and machines** | **×1.2260** | **+22.6%** (gauges independent +21.2% to +24.0%; gauges correlated +20.4% to +24.8%) | GAIN |

Read: the headline is the row **without the card, by the index's rule**: it counts only what held the same way in all three of our runs, on real machines (class L), at the software end (the cluster and the services on it): **+22.5%** over work, speed and machines; work +17.2%, speed +43.2% (native's 95th percentile response over Omni-Compass's), machines +9.5% (native's machines over Omni-Compass's), for the same power and the same bill (both held at native's, section 1). With every interval carried the same layers read **+22.6%** (gauges correlated: +20.4% to +24.8%). With the card the index reads **+22.6%** carried: the chip enters as exactly 1, so the two scopes read alike, and they are kept apart so the chip's own record stays in view.

The cloud is the wire. Its bill is kept exactly as native's and the layer enters as exactly 1 on every gauge: the benefit lives at the software end and the wire carries it. The cloud's own runs are the check that it holds: on Azure's own autoscaler the bill read STEADY (four paired repetitions on the compass law, one run; the v1 fleet's steady set and burst STEADY too), shown in section 2 and never composed. Read through the cloud, the same index is more work for the same bill: the cost of each unit of work falls by the work's own factor while the bill stays native's.

## 3b. What the benefit cost: the chip, the energy and the wire against native

The benefit above is the software end's. This section is the other half a buyer asks for: what it cost. Each hardware piece and the wire is read against native, every row of its own record, so it can be seen whether the software end's gain was bought by heating or wearing the chip, by drawing more power, by serving less, or by a bigger bill (do no harm, `DISCLOSURES.md` section 3). Nothing here is composed into the index; a LOSS row is shown and named, never cut.

**the chip (an NVIDIA A100, the card's own meter, class P, omni-v21)** (`results/gpu/V21_A100_CAP_ABC.md`, `results/gpu/V21_A100_CAP_FULL_ABC.md`, `results/gpu/V21_A100_SAVE_ABC.md`)

| Part | Gauge | Reading against native |
|---|---|---|
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | work per energy (served requests per kJ) | STEADY, under the floor (the three runs' mean 0.11%) |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | energy, GPU (J) | STEADY, under the floor (the three runs' mean 0.12%) |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | energy per served request (J) | STEADY, under the floor (the three runs' mean 0.12%) |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | power, GPU mean (W) | STEADY, under the floor (the three runs' mean 0.15%) |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | requests served | STEADY, the same |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | requests not served | STEADY, the same |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | response time, mean (ms) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | response time, 95th percentile (ms) | the runs disagree |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | response time, 99th percentile (ms) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.25%) |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | temperature, mean (C) | STEADY, under the floor (the three runs' mean 0.21%) |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | energy, GPU device counter (J) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| the factory tune (the dial at the max), native's power cap at 70% of the card's top | power-capped share of samples | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| the factory tune, the same runs' full-load part | work per energy (served requests per kJ) | STEADY, under the floor (the three runs' mean 0.07%) |
| the factory tune, the same runs' full-load part | energy, GPU (J) | STEADY, under the floor (the three runs' mean 0.23%) |
| the factory tune, the same runs' full-load part | energy per served request (J) | STEADY, under the floor (the three runs' mean 0.07%) |
| the factory tune, the same runs' full-load part | power, GPU mean (W) | STEADY, under the floor (the three runs' mean 0.26%) |
| the factory tune, the same runs' full-load part | requests served | STEADY, under the floor (the three runs' mean 0.15%) |
| the factory tune, the same runs' full-load part | requests not served | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| the factory tune, the same runs' full-load part | response time, mean (ms) | STEADY, under the floor (the three runs' mean 0.47%) |
| the factory tune, the same runs' full-load part | response time, 95th percentile (ms) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| the factory tune, the same runs' full-load part | response time, 99th percentile (ms) | STEADY, under the floor (the three runs' mean 0.50%) |
| the factory tune, the same runs' full-load part | temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.23%) |
| the factory tune, the same runs' full-load part | temperature, mean (C) | STEADY, under the floor (the three runs' mean 0.25%) |
| the factory tune, the same runs' full-load part | energy, GPU device counter (J) | STEADY, under the floor (the three runs' mean 0.23%) |
| the factory tune, the same runs' full-load part | power-capped share of samples | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| the tune-down (the dial at save), its own three runs | work per energy (served requests per kJ) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| the tune-down (the dial at save), its own three runs | energy, GPU (J) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| the tune-down (the dial at save), its own three runs | energy per served request (J) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| the tune-down (the dial at save), its own three runs | power, GPU mean (W) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| the tune-down (the dial at save), its own three runs | requests served | STEADY, the same |
| the tune-down (the dial at save), its own three runs | requests not served | STEADY, the same |
| the tune-down (the dial at save), its own three runs | response time, mean (ms) | STEADY, under the floor (the three runs' mean 0.19%) |
| the tune-down (the dial at save), its own three runs | response time, 95th percentile (ms) | STEADY, under the floor (the three runs' mean 0.04%) |
| the tune-down (the dial at save), its own three runs | response time, 99th percentile (ms) | STEADY, under the floor (the three runs' mean 0.02%) |
| the tune-down (the dial at save), its own three runs | temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.22%) |
| the tune-down (the dial at save), its own three runs | temperature, mean (C) | the runs disagree |
| the tune-down (the dial at save), its own three runs | energy, GPU device counter (J) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| the tune-down (the dial at save), its own three runs | power-capped share of samples | GAIN in all three of our runs |

39 rows: 9 GAIN, 24 STEADY, 0 power given, 4 LOSS, 2 where the runs disagree. The LOSS rows: response time, mean (ms) (the factory tune (the dial at the max), native's power cap at 70% of the card's top): LOSS by the mean of our three runs, beyond the noise in 0 of 3; response time, 99th percentile (ms) (the factory tune (the dial at the max), native's power cap at 70% of the card's top): LOSS by the mean of our three runs, beyond the noise in 0 of 3; requests not served (the factory tune, the same runs' full-load part): LOSS by the mean of our three runs, beyond the noise in 0 of 3; response time, 95th percentile (ms) (the factory tune, the same runs' full-load part): LOSS by the mean of our three runs, beyond the noise in 0 of 3.

**the energy the software end drew (class L inputs, no meter)** (`results/live (the cluster and service tables)`)

| Part | Gauge | Reading against native |
|---|---|---|
| the cluster: a declared model of the machines row, never a meter | energy, parked workers at standby power (Wh) | GAIN: Omni-Compass 4.3% less than native (95%: 4.8% less to 3.9% less) |
| the services: the host's own count of processor time, a stand-in for energy, never a meter | the host's processor seconds | GAIN: Omni-Compass 0.7% less than native (95%: 1.2% less to 0.2% less) |

2 rows: 2 GAIN, 0 STEADY, 0 power given, 0 LOSS, 0 where the runs disagree. No LOSS row.

**the wire (the cloud's metered bill, class L)** (`results/live/AKS_STEADY_100_OMNI_V18.md`, `results/live/AKS_BILL.md`, `results/live/V1_AKS_STEADY.json`, `results/live/V1_AKS_BURST.json`)

| Part | Gauge | Reading against native |
|---|---|---|
| Azure: the steady set's 100 paired repetitions (one run), the compass law's four (one run) and the v1 fleet's one-run sets, their mean | the compute bill at list price | power given: Omni-Compass 1.0% more than native (95%: 8.7% less to 11.7% more); its 95% interval includes no change |
| the same runs | machines billed | power given: Omni-Compass 2.1% more than native (95%: 3.9% less to 8.5% more); its 95% interval includes no change |

2 rows: 0 GAIN, 0 STEADY, 2 power given, 0 LOSS, 0 where the runs disagree. No LOSS row.

**the machine (the kernel, bare metal, Kepler and the machine's own meter)**: not yet run.

## 4. The assumption tested where the tables allow: separability, from the governors' four ways

Omni-Compass on the organism alone (compassbare against nativebare) and on top of the orchestrator (compass against native), in the same repetitions, on omni-v12. If the layers did not interact the two ratios would agree; a difference clear of the noise says the orchestrator changes what Omni-Compass has to work with (a layer's factor is not a constant of the layer alone).

| Governor | Gauge | On top of the orchestrator (TOP) | On the organism alone (BARE) | TOP ÷ BARE, 95% interval | Agree within the noise |
|---|---|---|---|---|---|
| Kueue | speed (the 95th percentile response, lower) | ×0.9884 (-1.2%; -4.8% to +2.6%) | ×0.9696 (-3.0%; -6.2% to +0.3%) | ×1.0194 (-3.1% to +7.2%) | yes |
| Kueue | machines (fewer) | ×1.1172 (+11.7%; +6.1% to +17.6%) | ×1.1308 (+13.1%; +8.0% to +18.4%) | ×0.9879 (-7.8% to +5.9%) | yes |
| Kueue | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0785 (+7.9%; +4.2% to +11.6%) | ×1.0855 (+8.5%; +5.3% to +11.9%) | ×0.9936 (-5.1% to +4.1%) | yes |
| Volcano | speed (the 95th percentile response, lower) | ×0.9183 (-8.2%; -16.3% to +0.7%) | ×0.9467 (-5.3%; -8.3% to -2.3%) | ×0.9699 (-12.0% to +7.0%) | yes |
| Volcano | machines (fewer) | ×1.1738 (+17.4%; +9.1% to +26.3%) | ×1.1748 (+17.5%; +11.2% to +24.1%) | ×0.9991 (-8.8% to +9.5%) | yes |
| Volcano | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.1146 (+11.5%; +6.2% to +17.0%) | ×1.1139 (+11.4%; +7.4% to +15.5%) | ×1.0006 (-5.8% to +6.3%) | yes |
| the KAI scheduler | speed (the 95th percentile response, lower) | ×0.9667 (-3.3%; -7.0% to +0.5%) | ×0.9708 (-2.9%; -6.9% to +1.2%) | ×0.9958 (-5.9% to +5.4%) | yes |
| the KAI scheduler | machines (fewer) | ×1.0861 (+8.6%; +4.5% to +12.9%) | ×1.1445 (+14.4%; +8.9% to +20.3%) | ×0.9490 (-10.9% to +1.1%) | yes |
| the KAI scheduler | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0584 (+5.8%; +3.1% to +8.7%) | ×1.0955 (+9.5%; +6.0% to +13.2%) | ×0.9661 (-7.4% to +0.8%) | yes |
| Koordinator | speed (the 95th percentile response, lower) | ×1.0746 (+7.5%; +5.1% to +9.9%) | ×0.9437 (-5.6%; -8.1% to -3.1%) | ×1.1388 (+10.0% to +17.9%) | no |
| Koordinator | machines (fewer) | ×1.0055 (+0.6%; -0.1% to +1.2%) | ×1.2062 (+20.6%; +13.5% to +28.2%) | ×0.8336 (-21.6% to -11.4%) | no |
| Koordinator | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0046 (+0.5%; +0.1% to +0.9%) | ×1.1344 (+13.4%; +8.9% to +18.2%) | ×0.8856 (-15.0% to -7.7%) | no |
| the scheduler's bin-packing profile | speed (the 95th percentile response, lower) | ×1.0108 (+1.1%; -2.5% to +4.8%) | ×0.9482 (-5.2%; -8.3% to -1.9%) | ×1.0660 (+1.5% to +12.0%) | no |
| the scheduler's bin-packing profile | machines (fewer) | ×1.1523 (+15.2%; +8.1% to +22.9%) | ×1.1631 (+16.3%; +8.6% to +24.6%) | ×0.9908 (-9.8% to +8.8%) | yes |
| the scheduler's bin-packing profile | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.1004 (+10.0%; +5.5% to +14.8%) | ×1.1072 (+10.7%; +5.9% to +15.8%) | ×0.9939 (-6.6% to +5.7%) | yes |
| Crane | speed (the 95th percentile response, lower) | ×1.0105 (+1.0%; -0.5% to +2.6%) | ×1.0354 (+3.5%; +1.6% to +5.5%) | ×0.9759 (-4.8% to -0.01%) | no |
| Crane | machines (fewer) | ×1.0000 (+0.00%; +0.00% to +0.00%) | ×1.0000 (+0.00%; -0.00% to +0.00%) | ×1.0000 (+0.00% to +0.00%) | yes |
| Crane | energy (a declared model on the cluster, the card's own meter on the chip) | ×0.9963 (-0.4%; -0.6% to -0.1%) | ×0.9984 (-0.2%; -0.3% to -0.01%) | ×0.9979 (-0.5% to +0.1%) | yes |
| KubeRay | speed (the 95th percentile response, lower) | ×0.9754 (-2.5%; -6.3% to +1.6%) | ×0.9500 (-5.0%; -7.1% to -2.8%) | ×1.0268 (-2.0% to +7.6%) | yes |
| KubeRay | machines (fewer) | ×1.0134 (+1.3%; +0.4% to +2.3%) | ×1.2021 (+20.2%; +11.5% to +29.6%) | ×0.8430 (-21.9% to -9.0%) | no |
| KubeRay | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0085 (+0.9%; +0.2% to +1.5%) | ×1.1306 (+13.1%; +7.7% to +18.7%) | ×0.8921 (-15.1% to -6.3%) | no |
| Karmada | speed (the 95th percentile response, lower) | ×0.9125 (-8.8%; -13.6% to -3.7%) | ×0.9309 (-6.9%; -9.8% to -3.9%) | ×0.9802 (-7.9% to +4.4%) | yes |
| Karmada | machines (fewer) | ×1.1118 (+11.2%; +4.5% to +18.3%) | ×1.1304 (+13.0%; +5.7% to +20.9%) | ×0.9836 (-10.3% to +7.8%) | yes |
| Karmada | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0743 (+7.4%; +2.9% to +12.2%) | ×1.0893 (+8.9%; +4.0% to +14.1%) | ×0.9862 (-7.5% to +5.1%) | yes |
| Open Cluster Management | speed (the 95th percentile response, lower) | ×0.9197 (-8.0%; -13.9% to -1.7%) | ×0.9632 (-3.7%; -6.8% to -0.5%) | ×0.9548 (-11.3% to +2.8%) | yes |
| Open Cluster Management | machines (fewer) | ×1.0257 (+2.6%; +0.7% to +4.4%) | ×1.0748 (+7.5%; +3.0% to +12.1%) | ×0.9544 (-8.8% to -0.1%) | no |
| Open Cluster Management | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.0181 (+1.8%; +0.4% to +3.2%) | ×1.0542 (+5.4%; +2.3% to +8.6%) | ×0.9658 (-6.5% to -0.2%) | no |
| Armada | speed (the 95th percentile response, lower) | ×1.7951 (+79.5%; +70.0% to +89.5%) | ×0.9572 (-4.3%; -7.0% to -1.5%) | ×1.8754 (+76.4% to +99.4%) | no |
| Armada | machines (fewer) | ×1.7059 (+70.6%; +66.4% to +74.9%) | ×1.1192 (+11.9%; +4.7% to +19.6%) | ×1.5242 (+42.0% to +63.6%) | no |
| Armada | energy (a declared model on the cluster, the card's own meter on the chip) | ×1.4476 (+44.8%; +42.4% to +47.1%) | ×1.0872 (+8.7%; +3.8% to +13.9%) | ×1.3315 (+26.8% to +39.9%) | no |

18 of 30 governor-gauge pairs agree within the noise. Where they do not, the orchestrator under Omni-Compass changed its factor, and a product built from the organism-alone factor would misstate the stacked result there by the TOP ÷ BARE shown; the composition in section 3 uses the TOP factors (Omni-Compass on top of what is actually there), which is the stacked measurement for that pair of layers.

## 5. Beside the total, never inside it

- The organisms, our own models (class S, `results/realms_v5/REALMS_V5.md`, commit 9819a903cba3): the spine (267 muscles) under its own load: fewer misses, misses -0.145 pp (-0.176 to -0.115), work +0.00%, power given +0.011%. A model's energy is not a meter's; these rows are shown, not composed.
- The organisms, our own models (class S, `results/realms_v5/REALMS_V5.md`, commit 9819a903cba3): the whole tower (1107 muscles) under its own load: fewer misses, misses -0.051 pp (-0.062 to -0.040), work +0.00%, power given +0.000%. A model's energy is not a meter's; these rows are shown, not composed.
- The organisms with the real cluster inside (omni-v3, `results/live/V3_SIX_KUBE.md`), tower at 10 copies, 5 paired repetitions: the 95th percentile ×1.7118 (+71.2%; +8.2% to +170.9%); an older engine's result, the road to this one, never composed with the rows above.
- The organisms with the real cluster inside (omni-v3, `results/live/V3_SIX_KUBE.md`), tower at 100 copies, 5 paired repetitions: the 95th percentile ×1.4077 (+40.8%; -25.7% to +166.8%); an older engine's result, the road to this one, never composed with the rows above.
- The organisms with the real cluster inside (omni-v3, `results/live/V3_SIX_KUBE.md`), stack at 10 copies, 5 paired repetitions: the 95th percentile ×1.0124 (+1.2%; -41.1% to +74.0%); an older engine's result, the road to this one, never composed with the rows above.
- The organisms with the real cluster inside (omni-v3, `results/live/V3_SIX_KUBE.md`), stack at 100 copies, 5 paired repetitions: the 95th percentile ×1.1893 (+18.9%; +3.8% to +36.2%); an older engine's result, the road to this one, never composed with the rows above.

## 6. What is missing, and what replaces what

- **The machine** (the kernel, bare metal, Kepler and the machine's own meter; register row 79): not yet run. It enters as exactly 1.
- **The card on the engine that stands**: the omni-v23 runs on Lambda (one exact commit, on the founder's word) replace the omni-v21 rows; the chip enters as exactly 1 whatever they read, and they stand beside it.
- **The cloud at the tune-down**: the omni-v12 Azure sets (A, B and C of the steady set, the two bursts and the real day) give the bill its three-run reading; Google and Amazon follow on the same harness.
- **Every cluster and service table on omni-v12**: the campaign (`scripts/reruns.txt`) reruns every benchmark; each row above is replaced by its omni-v12 table as it lands, and this page is rebuilt (`python3 tools/whole_system.py`).
- **The stacked run**: Omni-Compass at every layer at once against native at every layer, the one measurement that makes the total class L and P instead of a composition. Preregistered before any run in `docs/WHOLE_SYSTEM_PREREGISTRATION.md` (three stacks: the cluster and its services on GitHub's machines; the cloud at the tune-down on Azure; the card beside the cluster on Lambda); its place is written here before its result exists.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
