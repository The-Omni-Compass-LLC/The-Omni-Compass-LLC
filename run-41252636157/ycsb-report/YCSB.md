# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,940 | 2,940 | -0.0% | -3.23 to 1.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,941 | -0.0% | -3.53 to 2.37 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.121 | 0.125 | +3.9% | -0.0451 to 0.0544 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.324 | 0.336 | +3.8% | -0.0498 to 0.0745 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0583 | 0.0592 | +1.5% | -0.00684 to 0.00861 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | -0.0% | -3.15 to 2.35 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,776 | 61,848 | +0.1% | -218 to 364 | shown, not judged |
| host CPU busy (share of the run) | 0.0885 | 0.0826 | -6.7% | -0.023 to 0.0111 | STEADY, no difference beyond the noise |
| host CPU-seconds | 162 | 150 | -7.3% | -45.3 to 21.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.121 | 0.112 | -7.3% | -0.0338 to 0.0162 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 49.3 | 49.8 | +0.9% | -6.16 to 7.08 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 47.8 | 48.2 | +0.8% | -5.99 to 6.76 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.53 | 1.6 | +4.7% | -0.179 to 0.322 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 162 | 150 | -7.3% | -45.3 to 21.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,877 | +0.0% | 0.389 to 2.47 | GAIN |
| throughput (operations a second) | 2,885 | 2,887 | +0.0% | 0.694 to 1.73 | GAIN |
| latency, 95th percentile (ms) | 0.432 | 0.433 | +0.3% | -0.0132 to 0.0159 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.633 | 0.63 | -0.6% | -0.0314 to 0.024 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.218 | +1.2% | -0.00179 to 0.00715 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,512 | -0.2% | -4.65 to -0.822 | GAIN |
| pages read into the cache (misses) | 77,712 | 77,710 | -0.0% | -273 to 269 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.202 | -4.6% | -0.0627 to 0.0434 | STEADY, no difference beyond the noise |
| host CPU-seconds | 150 | 142 | -5.7% | -55.3 to 38.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.283 | 0.267 | -5.7% | -0.104 to 0.0719 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 78.9 | 80.3 | +1.8% | -2.02 to 4.82 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 77.9 | 79.2 | +1.7% | -2.1 to 4.82 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.06 | 1.09 | +3.6% | -0.0201 to 0.0952 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 150 | 142 | -5.7% | -55.3 to 38.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,892 | +0.0% | -2.2 to 3.73 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,894 | +0.0% | -1.77 to 3.02 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.283 | 0.28 | -1.1% | -0.0224 to 0.0164 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.43 | -0.8% | -0.0244 to 0.017 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.164 | 0.163 | -0.9% | -0.00296 to 4.89e-05 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -1.73 to 2.21 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,623 | 61,619 | -0.0% | -120 to 112 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.18 | -6.0% | -0.0411 to 0.018 | STEADY, no difference beyond the noise |
| host CPU-seconds | 348 | 323 | -7.4% | -90.5 to 38.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.261 | 0.242 | -7.4% | -0.0678 to 0.0289 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 163 | 162 | -0.7% | -3.54 to 1.15 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 161 | 160 | -0.8% | -3.71 to 1.21 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 2.53 | +2.3% | -0.0594 to 0.175 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 348 | 323 | -7.4% | -90.5 to 38.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,767 | 5,771 | +0.1% | -5.48 to 11.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,777 | 5,781 | +0.1% | -4.75 to 12.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.28 | 0.283 | +1.2% | -0.0108 to 0.0175 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.505 | +1.5% | -0.0251 to 0.0405 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.142 | 0.144 | +0.9% | -0.00372 to 0.00639 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,362 | -0.2% | -4.54 to -0.644 | GAIN |
| pages read into the cache (misses) | 63,113 | 62,998 | -0.2% | -953 to 723 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.204 | -0.7% | -0.0114 to 0.00849 | STEADY, no difference beyond the noise |
| host CPU-seconds | 376 | 373 | -0.9% | -23.5 to 16.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.141 | 0.14 | -0.9% | -0.00874 to 0.00625 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 179 | 179 | -0.0% | -6.2 to 6.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 176 | 175 | -0.1% | -6.21 to 5.89 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.83 | 3.92 | +2.2% | -0.101 to 0.267 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 376 | 373 | -0.9% | -23.5 to 16.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -1.01 to -0.557 | LOSS |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -1.33 to -0.316 | LOSS |
| latency, 95th percentile (ms) | 0.341 | 0.344 | +1.0% | -0.00465 to 0.0113 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.533 | 0.535 | +0.5% | -0.0117 to 0.017 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.205 | +0.0% | -0.00532 to 0.00542 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.1% | -7.79 to 5.92 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,166 | 63,245 | +0.1% | -1,300 to 1,459 | shown, not judged |
| host CPU busy (share of the run) | 0.223 | 0.224 | +0.3% | -0.0643 to 0.0658 | STEADY, no difference beyond the noise |
| host CPU-seconds | 389 | 392 | +0.8% | -145 to 151 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.293 | 0.295 | +0.8% | -0.109 to 0.114 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233 | 233 | +0.0% | -7.75 to 7.82 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 230 | 230 | -0.0% | -7.8 to 7.63 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 2.6 | +4.8% | 0.0209 to 0.219 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 389 | 392 | +0.7% | -145 to 151 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
