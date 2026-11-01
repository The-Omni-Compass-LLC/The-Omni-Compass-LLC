# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | -0.0% | -6.78 to 4.99 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% | -4.3 to 3.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.303 | -0.2% | -0.0183 to 0.017 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.573 | 0.574 | +0.2% | -0.00739 to 0.0101 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.188 | -0.3% | -0.00631 to 0.00531 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,364 | -0.0% | -0.95 to 0.332 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,753 | 61,802 | +0.1% | -244 to 342 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.177 | -2.9% | -0.0295 to 0.0191 | STEADY, no difference beyond the noise |
| host CPU-seconds | 317 | 306 | -3.3% | -61.5 to 40.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.238 | 0.23 | -3.2% | -0.0459 to 0.0305 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 181 | 180 | -0.6% | -9.72 to 7.45 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 179 | 178 | -0.7% | -9.67 to 7.28 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.34 | 2.4 | +2.5% | -0.0545 to 0.173 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 317 | 306 | -3.3% | -61.5 to 40.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -1.64 to 2.74 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,891 | +0.0% | -0.993 to 2.02 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.404 | 0.406 | +0.7% | -0.0101 to 0.0154 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.547 | 0.547 | +0.1% | -0.0183 to 0.019 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.207 | +1.5% | -0.000321 to 0.00657 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,515 | -0.0% | -3.82 to 3.28 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,639 | 77,692 | +0.1% | -213 to 319 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.217 | +21.3% | -0.0877 to 0.164 | STEADY, no difference beyond the noise |
| host CPU-seconds | 124 | 159 | +28.4% | -80.8 to 151 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.299 | +28.4% | -0.152 to 0.284 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 75.7 | 77.3 | +2.0% | 0.412 to 2.66 | power given |
| the server's own CPU-seconds (mongod) | 74.8 | 76.3 | +2.0% | 0.313 to 2.69 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.983 | 1.02 | +3.3% | -0.0503 to 0.115 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 124 | 159 | +28.4% | -80.8 to 151 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,914 | 2,912 | -0.1% | -6.79 to 3.81 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,915 | -0.1% | -6.87 to 3.89 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.178 | 0.178 | +0.2% | -0.00254 to 0.0032 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.34 | 0.341 | +0.3% | -0.0238 to 0.0258 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.127 | 0.128 | +0.7% | -0.00236 to 0.00422 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | -0.1% | -7.02 to 5.24 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,649 | 61,629 | -0.0% | -228 to 187 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.133 | -9.8% | -0.0605 to 0.0316 | STEADY, no difference beyond the noise |
| host CPU-seconds | 268 | 236 | -11.8% | -133 to 69.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.177 | -11.8% | -0.0994 to 0.0523 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 127 | 127 | -0.1% | -3.07 to 2.74 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 125 | 125 | -0.2% | -3.19 to 2.71 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.94 | 2.01 | +4.0% | -0.0332 to 0.187 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 268 | 236 | -11.8% | -133 to 69.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,679 | 5,685 | +0.1% | -0.907 to 12.3 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,692 | 5,698 | +0.1% | -0.863 to 11.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.415 | 0.415 | +0.0% | -0.0043 to 0.0043 | STEADY, the same |
| latency, 99th percentile (ms) | 0.639 | 0.637 | -0.3% | -0.0149 to 0.0109 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.237 | 0.237 | -0.1% | -0.00075 to 0.00027 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,362 | +0.0% | -4.67 to 5.36 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,082 | 62,977 | -0.2% | -942 to 732 | shown, not judged |
| host CPU busy (share of the run) | 0.297 | 0.292 | -2.0% | -0.0183 to 0.00635 | STEADY, no difference beyond the noise |
| host CPU-seconds | 534 | 519 | -2.9% | -50 to 19.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.196 | -3.0% | -0.019 to 0.00699 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 314 | 314 | -0.1% | -1.12 to 0.809 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 310 | 310 | -0.1% | -1.07 to 0.567 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.23 | 4.32 | +2.3% | -0.118 to 0.31 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 534 | 519 | -2.9% | -50 to 19.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,881 | +0.1% | -3.39 to 6.67 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,888 | +0.1% | -4.07 to 7.43 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.341 | 0.341 | +0.1% | -0.0142 to 0.0149 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.634 | 0.631 | -0.5% | -0.0356 to 0.0296 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.207 | +0.4% | -0.00605 to 0.00759 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,484 | 7,484 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | -0.0% | -4.68 to 4.46 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,006 | 63,135 | +0.2% | -1,478 to 1,735 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.231 | +1.8% | -0.0522 to 0.0603 | STEADY, no difference beyond the noise |
| host CPU-seconds | 401 | 411 | +2.3% | -118 to 137 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.302 | 0.309 | +2.3% | -0.089 to 0.103 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 229 | 231 | +0.9% | -5.57 to 9.89 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 226 | 228 | +0.9% | -5.72 to 9.87 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 2.56 | +3.5% | 0.0205 to 0.154 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 401 | 411 | +2.3% | -118 to 137 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
