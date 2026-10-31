# The receipts, in their totality: what every result shows, and what it does not

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

A **receipt** here is a result file in this repository made by a paired run: the system as it runs on its own
(native) and the same system with Omni-Compass on top, the same work in both arms, the rules written down before the
counted runs, the engine identified by its fingerprint (`tools/omni_version.py --commit`), every row reported, losses
included. A receipt is read in the class of evidence it is: **P** a physical meter, **L** real software (a real
Kubernetes cluster, a real database), **S** our own models, **V** a property of the code. S is never presented as
proof of a physical saving. A result belongs to the engine it ran on and is never read across engines. Each test is read from its own newest three-run table, and every row names its engine: omni-v11's where its three runs have landed, omni-v10's where they have not. omni-v23, the engine that stands since 31 October, runs every benchmark again, and its tables replace these as they land (omni-v22 brought the five data stores' wires to the max, each spend gated on the store's own account of a miss, and changed nothing the Kubernetes governor runs; omni-v21 gave the immune system its self-knowledge, knob by knob; omni-v20 fixed the five data stores' wires at their causes; omni-v19 gave the Kubernetes governor a pod muscle of its own for a workload no autoscaler governs, which writes nothing unless a workload is named to it; omni-v18 took Omni direct into the fingerprint and changed nothing the Kubernetes governor runs; omni-v17 changed the Kubernetes governor's default beat, from 15 to 60 s, the heartbeat a dial, and kept its cruise wait at two readings or more at a slow beat; omni-v16 changed only the Kubernetes governor's clocks, each now counted in seconds, identical to omni-v15 at a 60 s decision, and set its full decision every 15 s, omni-v15 only the brain's power-cap request and the fingerprint's scope, omni-v14 only the Kubernetes governor's knob and its commands, omni-v13 added only the Kubernetes governor's hand-back of the CPU limits it gave on a shared host at its top, omni-v12 only the governor's hold on a raise the cluster refused and the swarm's reflex at once, omni-v11 only the governor's hold on a reading with no machine in service, omni-v10 only the CityLearn battery's glide). The earlier engines' receipts are the road, in `docs/history`.
How to read a single table: `docs/HOW_TO_READ_THE_RESULTS.md`. The wording of every three-run row: `tools/readings.py`.

## 1. What the receipts say, read together

1. **More work in time, and a faster tail, on the same machines (L).** On a real Kubernetes cluster, Omni-Compass on top of
   the pod autoscaler cut the 95th-percentile response by 54% to 66% in the steady, wandering, all-four, fault and
   public-trace tests, in all three runs each (omni-v10). Where demand outran what native served in time, the work done
   inside the response line rose 47% to 79% (the all-four test). Failed requests fell 9% to 18% and the alert minutes 16% to
   100% where demand stepped, swung or machines failed. On top of Goldilocks the 95th percentile fell 61% to 64%, on top of
   KEDA on CPU and requests 52% to 53%, and on top of KEDA's HTTP add-on 72% to 74% (omni-v11); in all 90 paired repetitions
   of those three tests Omni-Compass's 95th and 99th percentiles were below native's (`docs/TAIL_LATENCY.md`). Read
   together: the governor turns capacity the native controller leaves unused into service, on the same machines.
2. **The same work on less, where less is enough (L).** A queue of batch jobs ran on 6% to 14% fewer machines with 4% to 10%
   less standby energy and a 10% to 12% faster mean response, and the queue finished no later (omni-v10). Kafka held 0.8%
   fewer consumers on `burst`, MongoDB's cache gave back 0.9% to 1.0% on `f`, and Redis's ceiling fell 2.3% to 2.6% on
   `burst` (omni-v11). PostgreSQL read STEADY on every judged row but one (power given) and MySQL on every row but its
   update throughput (the runs disagree): under the brain's verdict no give-back that would cost service was written.
3. **What it cost, shown beside it.** The replicas the faster recovery took (faults +14% to +20%; the Google day: pods
   started +120% to +193%), the energy of workers left on at idle power on top of Goldilocks and KEDA (+1.1% to +2.3%, a
   declared model), Redis's memory on `small` (+1.7% to +1.9%), PgBouncer's most connections open (+8% to +10%) and MySQL's
   pool from its factory size (+5% to +16%), each power given in all three runs, beside the service it bought.
4. **Everything handed back (L, omni-v11).** The kill test: the governor killed outright in the middle of the window in 30
   repetitions over three runs, every setting back at the operator's 8 to 11 s later (the allowance is 60 s), a second
   governor governing to the end in every one, and the 120 s after the kill STEADY against native. The long run, two hours an
   arm: the governor's memory up 2.3% at most (no leak), 97.5% of the decisions its interval predicts, none failed, its
   decision time not growing, and every setting handed back at the end.
5. **On our own models and the independent simulators (S).** The 1,107 muscles each alone: 527 GAIN, 580 STEADY, none LOSS;
   every one of the seven organisms GAIN (fewer misses) under all three loads. The power grids: 67 gauge-rows GAIN, 14 power
   given, no LOSS. The robot arm the trial moved: torque −28.6%, tracking error −21.3%. The buildings with batteries: 27
   score-rows GAIN (the bill −16.1% in the one district with a price), 1 power given, no LOSS, the outage districts'
   batteries left native. The drone swarms: energy a mission −7% to −20%, missions a charge +8% to +25%, no near miss or
   collision in the counted cells. **On a mission draw outside those cells, two drones collided**: the wire's proximity
   reflex slowed a drone over about a second where its own rule says at once. That is a fault in the wire, root-caused; its
   fix (the reflex at once, reaching out with the square of the speed) landed in omni-v12 (`docs/OMNI_V12.md`,
   `results/model_gate/V12_SWARM_REFLEX.md`), and the swarm runs again on it.
6. **What is not yet shown.** No energy saving on a real chip: the physical receipt (P), the GPU's own meter on the current
   governor, is the decisive one still to be produced; every earlier card result is obsolete. No cloud-bill result on the
   engine that stands yet: the Azure sets run one at a time on it, up to 100 repetitions each under the preregistered
   stopping rule. More completed work at one fixed resource cap: the capacity test reads STEADY at all four caps.

## 2. Receipt by receipt

Newest engine first within each class. "In all three" means the same sign in runs A, B and C with every 95% interval clear
of zero; STEADY means an interval includes zero. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results.

### Real software (L)

| Test | Engine | Native | What moved | Reading | It shows | It does not show | File |
|---|---|---|---|---|---|---|---|
| The governor killed outright mid-run | omni-v11 | HPA | handed back 8 to 11 s after the kill in 30 of 30 repetitions; p95 −39% to −58%; failed requests −7% to −12%; alert minutes −16% to −23%; replicas +3% to +6% | GAIN in all three; hand-back in every repetition; replicas power given | a governor that can die without leaving a setting behind | the 99th percentile (STEADY: +25% in run A, −25% to −27% in B and C) | `results/live/V11_ROBUST_KILL.md` |
| The long run, two hours an arm | omni-v11 | HPA | no leak (memory +2.3% at most); decisions valid; none failed; every setting handed back; mean response −34% to −36%; replicas +49% to +52% | held in every repetition; GAIN in all three; replicas power given | it runs for hours unchanged | the tails (STEADY, three pairs a run) | `results/live/V11_ROBUST_LONG.md` |
| On top of Goldilocks and the VPA's recommender | omni-v11 | the service rightsized by Goldilocks, HPA | p95 −61% to −64%; time over the line −98% to −100%; alert minutes −100%; pods started −53% to −61%; energy +1.7% to +2.3% (model) | GAIN in all three; energy power given | a faster service on top of a rightsizer | a measured energy saving | `results/live/V11_GOLDILOCKS.md` |
| On top of KEDA's HTTP add-on | omni-v11 | KEDA 2.21, HTTP add-on 0.16 | p95 −72% to −74%; alert minutes −100%; replicas −11% to −20%; energy +1.6% to +2.2% (model) | GAIN in all three; energy power given; the pod start wait STEADY | faster service on top of a second autoscaler | a measured energy saving | `results/live/V11_KEDA_REQUESTS.md` |
| On top of KEDA on CPU and requests | omni-v11 | KEDA 2.21 | p95 −52% to −53%; replicas +2% to +3%; energy +1.1% to +1.8% (model) | GAIN in all three; replicas and energy power given | as above | as above | `results/live/V11_KEDA_CPU_REQUESTS.md` |
| Capacity at a fixed cap (four caps) | omni-v11 | HPA under a CPU quota | — | STEADY at every cap | no harm under a cap | more work under the cap | `results/live/V11_CAPACITY.md` |
| Redis | omni-v11 | the operator's 64 MB ceiling; also as shipped | work inside the 2 ms line and hit rate +1.3% to +1.6%; mean latency −1.7% to −7.3%; ceiling −2.3% to −2.6% on `burst`; memory +1.7% to +1.9% on `small` | GAIN in all three; memory power given on `small`; as shipped STEADY (at its limit on native) | a faster cache, its price shown | a tail gain (the 99th percentile STEADY, `docs/TAIL_LATENCY.md`) | `results/live/V11_REDIS.md`, `V11_REDIS_SERVICE.md`, `V11_REDIS_SHIPPED.md` |
| Kafka | omni-v11 | the operator's 2 consumers | consumers −0.8% on `burst` | GAIN in all three under both objectives; the rest STEADY | no harm, a fraction given back | a service gain | `results/live/V11_KAFKA.md`, `V11_KAFKA_SERVICE.md` |
| PostgreSQL, MySQL, MongoDB | omni-v11 | the operators' pool, buffer pool and cache; MySQL and MongoDB also as shipped | MongoDB's cache −0.9% to −1.0% on `f`; PgBouncer's most connections open +8% to +10%; MySQL as shipped: the pool +5% to +16%; at the max, PgBouncer's connections held −10% to −22% and MongoDB's cache −0.4% to −0.8% | GAIN and power given as named; STEADY on every other judged row but MySQL's update throughput (the runs disagree) | no harm under the verdict | memory given back on the pool and the buffer pool | `results/live/V11_PGBENCH*.md`, `V11_SYSBENCH*.md`, `V11_YCSB*.md` |
| On top of CruiseKube | omni-v10 | CruiseKube 0.3.4 | — | STEADY on every row; no command written | no harm on a rightsized service | a gain there | `results/live/V10_CRUISEKUBE.md` |
| Steady work in steps | omni-v10 | HPA | p95 −64% to −65%; p99 −69% to −73%; time over the line −98% to −100%; alert minutes −100% | GAIN in all three; machines and energy STEADY | a faster service on the same machines | fewer machines | `results/live/V10_STEADY.md` |
| Demand that wanders | omni-v10 | HPA | p95 −57% to −66%; time over the line −38% to −45%; alert minutes −21% to −32%; energy −0.3% to −0.4% | GAIN in all three | service held through wandering demand | a measured energy saving (model) | `results/live/V10_WANDERING.md` |
| All four at once | omni-v10 | HPA | work inside the line +47% to +79%; p95 −56% to −61%; failed requests −9% to −14%; alert minutes −16% to −34% | GAIN in all three; machines the same | more work in time on the same machines | energy (STEADY, model) | `results/live/V10_ALL_FOUR.md` |
| Faults: a machine down, a spike, a runaway pod, a blind probe | omni-v10 | HPA | p95 −54% to −63%; p99 −43% to −51%; replicas +14% to +20% | GAIN in all three; replicas power given | service held through faults | machines (STEADY) | `results/live/V10_FAULTS.md` |
| The Google cluster trace of 2011, replayed | omni-v10 | HPA | p95 −56% to −62%; time over the line −74% to −77%; failed requests −15% to −18%; alert minutes −61% to −66%; pods started +120% to +193% | GAIN in all three; pods power given | a public day of real demand served faster | machines (the same), a cloud bill | `results/live/V10_TRACE_GOOGLE2011.md` |
| A queue of batch jobs | omni-v10 | Jobs and HPA | machines −6% to −14%; node-hours −6% to −14%; standby energy −4% to −10%; mean response −10% to −12%; queue finish STEADY | GAIN in all three | the same queue on fewer machines | a measured energy saving (model) | `results/live/V10_BATCH.md` |
| A noisy neighbour | omni-v10 | HPA | time over the line −11% | GAIN in all three; every other row STEADY, the neighbour's own included | no harm beside a noisy neighbour | — | `results/live/V10_FAIRNESS.md` |
| Azure's managed Kubernetes, its own bill | v1 | AKS with its cluster autoscaler | bill −4.7% steady, +5.0% burst | STEADY on every gauge | the method on a real cloud bill | a bill saving (the omni-v11 sets run now) | `results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md` |

### Our own models and the independent simulators (S)

| Test | Engine | Reading | File |
|---|---|---|---|
| Power grids: 11 SimBench grids in pandapower | omni-v11 | 67 gauge-rows GAIN, 14 power given, no LOSS: energy drawn and net import lower in all 11 (ZIP loads); losses lower in 7, power given in 4; tap operations fewer in 10, more in 1 | `results/live/V11_PANDAPOWER.md` |
| CityLearn districts | omni-v11 | 27 score-rows GAIN, 1 power given, no LOSS: in the four districts whose batteries moved, electricity bought −3.0% to −13.6%, the daily peak −3.2% to −16.9%, ramping −3.4% to −10.1%; the bill −16.1% in the one district with a price; the seven 2023 districts' batteries native (each charge is its building's reserve), every score there STEADY | `results/live/V11_CITYLEARN.md` |
| Robot arms, MuJoCo Menagerie | omni-v11 | Gen3 peak torque −28.6%, tracking error −21.3%, GAIN; UR5e and iiwa left native | `results/live/V11_MUJOCO.md` |
| Drone swarms, 20 drones in three cells | omni-v11 | energy a mission −7% to −20%, missions a charge +8% to +25%, GAIN in all three; no late mission, reserve breach, near miss or collision in the counted cells; the closest approach spent to about 0.16 m (shown, not judged); collisions on a draw outside the cells, the wire's fault, fixed in omni-v12 (its three runs under way) | `results/live/V11_SWARM.md`, `results/model_gate/V12_SWARM_REFLEX.md` |
| The 1,107 muscles and the seven organisms, preregistered seeds | omni-v8 (omni-v9's exact Student t moved no reading; omni-v10 to omni-v16 changed files it does not run, or, in omni-v16's edge, nothing at the organisms' own step) | 527 GAIN, 580 STEADY, none LOSS; every organism GAIN (fewer misses) under all three loads; reproduced exactly in three GitHub runs | `results/realms_v5/REALMS_V5.md` |

### A physical meter (P)

| Test | Status |
|---|---|
| One card, the card inside the organisms, eight cards, on the current governor | to be run by the founder on rented cards, at one exact commit, after the CPU side (`docs/GPU_RUN_GUIDE.md`); every earlier card result is obsolete |

### The code (V)

The max's guarantees, one by one, with the code path that makes each one true: `docs/FORMAL_V5.md`. The budget law's
conservation and convergence, the safety shield's 2,000,000 adversarial cases, the C++ twins equal to the Python: 
`docs/STATE_OF_PLAY.md`, "Verified in code".

## 3. What would change these readings

- A P run on a real card that shows no difference in the card's own energy at the same work would leave the energy
  claim at "not shown"; it is not claimed now.
- An A, B or C run that disagrees with the others turns a row into "the runs disagree"; it is looked into, never
  dropped.
- A loss in all three runs is reported as it stands, its cause looked for in our own wiring, setup and scoring first,
  and the next set run on the fix.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.
Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any
outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
