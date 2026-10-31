# The stacked run: Omni-Compass at every layer at once, preregistered

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 20 October 2026, before any stacked run. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs;
nothing was filed with any outside body.

## 1. What it measures

`results/WHOLE_SYSTEM.md` composes the layers by the product law from each layer's own table (class S over class P and L
tables). The stacked run is the measurement that replaces the composition: Omni-Compass on top of every layer in one arm,
every layer native in the other, paired, the same gauges. The question it answers is the one the composition assumes:
does a layer's factor stand when the layers around it also carry Omni-Compass? The stacked table and the composed total
are printed side by side, per gauge, as TOP ÷ composed with its 95% interval (`tools/whole_system.py`, section 3), read by
the one key: GAIN, STEADY or LOSS by the gauge's aim, never by the sign of the number.

## 2. The arms

Two arms, as every benchmark: **native** (every layer as its own controller runs it: the card's own limiter, the HPA, the
services' operator settings, the cloud's own autoscaler) and **omni** (Omni-Compass on top of every layer at once, each
layer wired as its own benchmark wires it, nothing added). Order rotated by repetition, a fresh stack per arm, ten paired
repetitions a run, three runs A, B and C (`tools/confirm_abc.py`).

## 3. The three stacks, in the order they run

1. **The cluster and the services on it, on GitHub's machines** (class L; costs nothing). The six-worker kind cluster of the
   Kubernetes tests with the HPA under the governor at the max, and on the same cluster PostgreSQL behind PgBouncer, Redis,
   Kafka and MongoDB with their knobs wired as rows 30, 27, 26 and 24 of the register wire them, under the all-four load (the load
   stepping one at a time) and each service's `burst` workload at once. Gauges: work inside the line (requests a second),
   the 95th percentile response, worker nodes in service, the declared-model energy, and each service's work inside the
   line, its 95th percentile and the resource it holds. This stack tests the composition of layers 3 and 4.
2. **The cloud, Azure, the whole engine at the max** (class L, the bill metered; the founder's order of 31 October struck the
   tune-down on the machines alone of 14 October: no hard rule, the bill judged beside the work; a run of this stack started
   before 31 October would have run the struck rule, and none had). The AKS steady set's cluster with the services of stack 1
   on it; the governor on top of Azure's own autoscaler with every muscle (`dial max`), the services' knobs wired at the max.
   Gauges: the bill at list price, machines billed, the 95th percentile, failed requests,
   and each service's rows. This stack tests the composition of layers 4 and 5, at the factory tune. Cost:
   about USD 2 a paired repetition at the steady set's size; 100 repetitions a run at most (the paid cap of 12 October).
3. **The card beside the cluster, on Lambda** (class P for the card, L for the rest; money). One GPU machine running the
   card bench (`scripts/gpu_paired.sh`) while the same machine hosts a kind cluster of stack 1; the card's governor and the
   cluster's governor are one body (one registry, one kill switch). Gauges: the card's primary (served requests per kJ),
   its energy, its 95th percentile, and stack 1's gauges. Starts only after the CPU side is done and on the founder's word,
   from one exact commit of `gpu-omni-v16`.

The machine layer (bare metal, Kepler and the machine's own meter; register row 79) joins stack 3 when its own benchmark
has run; until then it enters the composition as exactly 1 and the stacked run does not claim it.

## 4. The reading

Every judged row gets GAIN, STEADY or LOSS by the three-run rule (`tools/readings.py`). The composition test: for each gauge
present in both, log(R_stacked) − Σℓ log(Rℓ) with its interval (the stacked estimate's variance plus the composed sum's);
agree within the noise when the interval includes zero. A disagreement is reported as what it is: the layers interact
there, and the stacked number is the one that stands for that gauge. Nothing is re-aimed after a reading; a LOSS row stays
and its cause is found in the mechanism or the wiring (`DISCLOSURES.md`, section 4).

## 5. What is fixed before the first run

The engine that stands (omni-v23, or the newest that stands when the run starts; a run names its engine), the loads named
above, the gauges above, the stopping rule of the cloud stack (`tools/stop_rule.py`), and the arms. Any change after this
page is an amendment below it, dated, before the run it governs.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
