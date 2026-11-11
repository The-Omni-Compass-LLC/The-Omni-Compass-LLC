# Every level: Omni-Compass on top of the muscle, the organism, the cluster, the service, the plant, the cloud

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's order of 17 October: Omni-Compass is shown on top at every level, on every gauge, and every level's gauges should go the same way; where one does not, it is named here and taken to the founder. Each row is built from its result files by `tools/levels.py`; nothing is typed in. A count is of judged gauges (a table's rows that read a word), each under its own table's rule (the three runs, or the realms result's ten seeds); **power given** is a resource put in, shown and never called a loss. Every row names the engine its tables ran on, and no reading is carried from one engine to another.

| Level | Engine | Evidence | GAIN | STEADY | power given | LOSS | runs disagree | Goes the other way? |
|---|---|---|---:|---:|---:|---:|---:|---|
| The muscle, alone (1,107 muscles, each on its own native controller, under its own load) | omni-v8 | S (our model) | 530 | 577 | 0 | 0 | 0 | no: every judged gauge GAIN or STEADY |
| The organism, the stack: the seven organisms under three loads (own load, the climb, work waiting in line) | omni-v8 | S (our model) | 21 | 0 | 0 | 0 | 0 | no: every judged gauge GAIN or STEADY |
| The cluster: real Kubernetes, native its own HPA and scheduler | omni-v26 | L | 36 | 41 | 14 | 19 | 19 | **yes: 38, listed below** |
| The cluster with its add-ons native: KEDA, Goldilocks, CruiseKube | omni-v26 | L | 18 | 20 | 11 | 8 | 7 | **yes: 15, listed below** |
| A muscle inside a running service: database, broker, cache | omni-v26 | L | 170 | 81 | 83 | 6 | 32 | **yes: 38, listed below** |
| A physical plant in an independent simulator: buildings, power grids, robot arms, drone swarms | omni-v26 | independent simulator | 101 | 164 | 10 | 0 | 0 | no LOSS; resources put in shown as power given |
| The organism with the real cluster inside (the grid, at 1, 10, 100 and on GitHub's machines 1,000 copies) | older engines' tables; the grid runs again on the engine that stands | L, the cluster; S, the organism | – | – | – | – | – | no table on the engine that stands yet; the grid's runs on it are dispatched (results/grid_v26/DISPATCHED.json) |
| The cluster in a cloud: Azure Kubernetes Service, the bill | single runs, omni-v5 to omni-v7; one set on omni-v18 | L, the bill metered | – | – | – | – | – | no three-run table yet: eight single runs at the tune-down, machines billed from down 6.5% to up 7.6%, every one STEADY, inside the noise; the fleet (about 1.9 of 4 machines busy) leaves no whole machine to give back; one set of 97 paired repetitions on omni-v18 read the bill up 1.21%, power given, inside the noise (results/live/AKS_STEADY_100_OMNI_V18.md) |
| A group of clusters | not run | none yet | – | – | – | – | – | no run at this level yet, real or modelled, on the engine that stands (`k8s_fleet/` holds a model of an earlier engine) |

## Each level

### The muscle, alone (1,107 muscles, each on its own native controller, under its own load)

Native at this level: each muscle's native controller. Engine: omni-v8. Evidence: S (our model).
421 of the STEADY are at their limit on native (nothing to push).
Tables: `results/realms_v5/MUSCLES_V5.csv`.

### The organism, the stack: the seven organisms under three loads (own load, the climb, work waiting in line)

Native at this level: every muscle on its native controller, coupled in one body. Engine: omni-v8. Evidence: S (our model).
The organism's own reading; inside them no plant did less work or missed its line more often than native, under any load (the realms result's stricter look, plant by plant).
Tables: `results/realms_v5/REALMS_V5.md`.

### The cluster: real Kubernetes, native its own HPA and scheduler

Native at this level: Kubernetes as shipped with the operator's HPA target. Engine: omni-v26. Evidence: L.
Tables: `results/live/V26_ALL_FOUR.md`, `results/live/V26_BATCH.md`, `results/live/V26_CAPACITY.md`, `results/live/V26_FAIRNESS.md`, `results/live/V26_FAULTS.md`, `results/live/V26_TRACE_GOOGLE2011.md`, `results/live/V26_ROBUST_KILL.md`, `results/live/V26_ROBUST_LONG.md`.

Goes the other way:

- V26_ALL_FOUR.md: All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v26): response time (ms), 99th percentile (the runs disagree)
- V26_ALL_FOUR.md: All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v26): failed requests (%) (the runs disagree)
- V26_ALL_FOUR.md: All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_ALL_FOUR.md: All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v26): pod start wait, mean (s) (LOSS)
- V26_BATCH.md: Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v26): response time (ms), 99th percentile (the runs disagree)
- V26_BATCH.md: Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v26): time over the response line (% of samples) (the runs disagree)
- V26_BATCH.md: Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v26): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) (LOSS)
- V26_BATCH.md: Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_BATCH.md: Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (LOSS)
- V26_BATCH.md: Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v26): batch: queue finished (s) (LOSS)
- V26_CAPACITY.md: The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v26): 1 (the runs disagree)
- V26_CAPACITY.md: The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v26): 1.5 (LOSS)
- V26_CAPACITY.md: The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v26): 1.5 (LOSS)
- V26_CAPACITY.md: The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v26): 2 (LOSS)
- V26_CAPACITY.md: The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v26): 2 (the runs disagree)
- V26_CAPACITY.md: The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v26): 3 (the runs disagree)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): response time (ms), 95th percentile (LOSS)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): response time (ms), 99th percentile (the runs disagree)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): time over the response line (% of samples) (the runs disagree)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): failed requests (%) (the runs disagree)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) (the runs disagree)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (the runs disagree)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): second app: response time (ms), 95th percentile (LOSS)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): second app: response time (ms), 99th percentile (the runs disagree)
- V26_FAIRNESS.md: Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v26): second app: failed requests (%) (LOSS)
- V26_FAULTS.md: Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C three-run table (Omni v26): failed requests (%) (the runs disagree)
- V26_FAULTS.md: Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_FAULTS.md: Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (the runs disagree)
- V26_TRACE_GOOGLE2011.md: A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4): the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_TRACE_GOOGLE2011.md: A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4): the A/B/C three-run table (Omni v26): pod start wait, mean (s) (the runs disagree)
- V26_ROBUST_KILL.md: Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v26): response time (ms), 99th percentile (the runs disagree)
- V26_ROBUST_KILL.md: Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_ROBUST_KILL.md: Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (the runs disagree)
- V26_ROBUST_KILL.md: Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v26): robust: failed requests in the 300 s after the kill (%) (LOSS)
- V26_ROBUST_KILL.md: Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v26): robust: time over the line in the 300 s after the kill (% of samples) (the runs disagree)
- V26_ROBUST_LONG.md: Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_ROBUST_LONG.md: Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (LOSS)

### The cluster with its add-ons native: KEDA, Goldilocks, CruiseKube

Native at this level: Kubernetes with the add-on as shipped and as used, its own recommendations applied. Engine: omni-v26. Evidence: L.
Tables: `results/live/V26_KEDA_REQUESTS.md`, `results/live/V26_KEDA_CPU_REQUESTS.md`, `results/live/V26_GOLDILOCKS.md`, `results/live/V26_CRUISEKUBE.md`.

Goes the other way:

- V26_KEDA_REQUESTS.md: Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v26): pods started (the runs disagree)
- V26_KEDA_REQUESTS.md: Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v26): pod start wait, total (s) (the runs disagree)
- V26_KEDA_REQUESTS.md: Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (the runs disagree)
- V26_KEDA_CPU_REQUESTS.md: Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v26): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) (the runs disagree)
- V26_KEDA_CPU_REQUESTS.md: Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_KEDA_CPU_REQUESTS.md: Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (the runs disagree)
- V26_GOLDILOCKS.md: Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_GOLDILOCKS.md: Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (LOSS)
- V26_CRUISEKUBE.md: CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v26): response time (ms), mean (LOSS)
- V26_CRUISEKUBE.md: CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v26): response time (ms), 95th percentile (LOSS)
- V26_CRUISEKUBE.md: CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v26): response time (ms), 99th percentile (LOSS)
- V26_CRUISEKUBE.md: CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v26): failed requests (%) (LOSS)
- V26_CRUISEKUBE.md: CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v26): HPA replicas, mean (the runs disagree)
- V26_CRUISEKUBE.md: CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v26): pod start wait, total (s) (LOSS)
- V26_CRUISEKUBE.md: CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v26): pod start wait, mean (s) (the runs disagree)

### A muscle inside a running service: database, broker, cache

Native at this level: the server as shipped but for the one setting an operator sets (each table names it). Engine: omni-v26. Evidence: L.
Tables: `results/live/V26_REDIS.md`, `results/live/V26_REDIS_SERVICE.md`, `results/live/V26_KAFKA.md`, `results/live/V26_KAFKA_SERVICE.md`, `results/live/V26_PGBENCH.md`, `results/live/V26_SYSBENCH.md`, `results/live/V26_YCSB.md`.

Goes the other way:

- V26_REDIS.md: large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run: host CPU busy (share of the run) (the runs disagree)
- V26_REDIS.md: large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run: host CPU-seconds (the runs disagree)
- V26_REDIS.md: large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run: host CPU-seconds per 1,000 requests inside the line (the runs disagree)
- V26_REDIS.md: small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run: latency, 99th percentile (ms) (the runs disagree)
- V26_KAFKA_SERVICE.md: light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run: host CPU-seconds per 1,000 messages inside the line (the runs disagree)
- V26_PGBENCH.md: select (-S, scale 20): line 50 ms, 3 paired repetitions a run: latency, 95th percentile (ms, lag included) (LOSS)
- V26_PGBENCH.md: select (-S, scale 20): line 50 ms, 3 paired repetitions a run: latency, 99th percentile (ms) (the runs disagree)
- V26_PGBENCH.md: select (-S, scale 20): line 50 ms, 3 paired repetitions a run: latency, mean (ms) (LOSS)
- V26_PGBENCH.md: simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run: latency, 95th percentile (ms, lag included) (the runs disagree)
- V26_PGBENCH.md: simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run: latency, 99th percentile (ms) (the runs disagree)
- V26_PGBENCH.md: simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run: latency, median (ms) (the runs disagree)
- V26_PGBENCH.md: simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run: host CPU-seconds per 1,000 transactions inside the line (the runs disagree)
- V26_SYSBENCH.md: tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted): latency, 95th percentile (ms) (the runs disagree)
- V26_SYSBENCH.md: tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted): latency, 99th percentile (ms) (the runs disagree)
- V26_SYSBENCH.md: tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted): latency, mean (ms) (the runs disagree)
- V26_SYSBENCH.md: tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted): host CPU busy (share of the run) (the runs disagree)
- V26_SYSBENCH.md: tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted): host CPU-seconds (the runs disagree)
- V26_SYSBENCH.md: tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted): host CPU-seconds per 1,000 transactions inside the line (the runs disagree)
- V26_SYSBENCH.md: burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run: work inside the response line (transactions a second answered within the line) (the runs disagree)
- V26_SYSBENCH.md: burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run: throughput (transactions a second) (the runs disagree)
- V26_SYSBENCH.md: burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run: queries a second (the runs disagree)
- V26_SYSBENCH.md: read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run: work inside the response line (transactions a second answered within the line) (the runs disagree)
- V26_SYSBENCH.md: update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run: latency, 95th percentile (ms) (the runs disagree)
- V26_SYSBENCH.md: update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run: latency, 99th percentile (ms) (the runs disagree)
- V26_YCSB.md: tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted): latency, 99th percentile (ms) (the runs disagree)
- V26_YCSB.md: b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, 99th percentile (ms) (LOSS)
- V26_YCSB.md: b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, mean (ms) (the runs disagree)
- V26_YCSB.md: b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: host CPU busy (share of the run) (the runs disagree)
- V26_YCSB.md: b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: host CPU-seconds (the runs disagree)
- V26_YCSB.md: b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: host CPU-seconds per 1,000 operations inside the line (the runs disagree)
- V26_YCSB.md: burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, 95th percentile (ms) (LOSS)
- V26_YCSB.md: burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, 99th percentile (ms) (LOSS)
- V26_YCSB.md: burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, mean (ms) (the runs disagree)
- V26_YCSB.md: burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: bytes in the cache, mean (MB) (the runs disagree)
- V26_YCSB.md: burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) (the runs disagree)
- V26_YCSB.md: c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, 95th percentile (ms) (the runs disagree)
- V26_YCSB.md: c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, 99th percentile (ms) (the runs disagree)
- V26_YCSB.md: c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run: latency, mean (ms) (LOSS)

### A physical plant in an independent simulator: buildings, power grids, robot arms, drone swarms

Native at this level: the simulator's own controller, unchanged. Engine: omni-v26. Evidence: independent simulator.
Tables: `results/live/V26_CITYLEARN.md`, `results/live/V26_PANDAPOWER.md`, `results/live/V26_MUJOCO.md`, `results/live/V26_SWARM.md`.

### The organism with the real cluster inside (the grid, at 1, 10, 100 and on GitHub's machines 1,000 copies)

Native at this level: the organism's native controllers around Kubernetes with its HPA. Engine: older engines' tables; the grid runs again on the engine that stands. Evidence: L, the cluster; S, the organism.
No table on the engine that stands yet; the grid's runs on it are dispatched (results/grid_v26/DISPATCHED.json).
Tables: `results/live/SIX_KUBE.md`, `results/live/V3_SIX_KUBE.md`, `results/live/V3_BIG_ORGANISM.md`.

### The cluster in a cloud: Azure Kubernetes Service, the bill

Native at this level: Azure's own cluster autoscaler and the HPA. Engine: single runs, omni-v5 to omni-v7; one set on omni-v18. Evidence: L, the bill metered.
No three-run table yet: eight single runs at the tune-down, machines billed from down 6.5% to up 7.6%, every one STEADY, inside the noise; the fleet (about 1.9 of 4 machines busy) leaves no whole machine to give back; one set of 97 paired repetitions on omni-v18 read the bill up 1.21%, power given, inside the noise (results/live/AKS_STEADY_100_OMNI_V18.md).
Tables: `results/live/AKS_BILL.md`, `results/live/raw/run-38981149348/`.

### A group of clusters

Native at this level: each cluster's own autoscaler. Engine: not run. Evidence: none yet.
No run at this level yet, real or modelled, on the engine that stands (`k8s_fleet/` holds a model of an earlier engine).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
