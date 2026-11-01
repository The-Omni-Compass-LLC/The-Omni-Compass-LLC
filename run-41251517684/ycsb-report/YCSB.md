# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,899 | +0.0% | -3.69 to 4.12 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,904 | 2,904 | -0.0% | -1.06 to 0.659 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.354 | -0.8% | -0.0307 to 0.0247 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.572 | -2.1% | -0.0495 to 0.0255 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.169 | 0.169 | -0.4% | -0.00697 to 0.00559 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -4.92 to 3.16 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 709,624 | 702,712 | -1.0% | -80,603 to 66,779 | shown, not judged |
| host CPU busy (share of the run) | 0.174 | 0.17 | -2.1% | -0.0229 to 0.0156 | STEADY, no difference beyond the noise |
| host CPU-seconds | 311 | 303 | -2.6% | -48.7 to 32.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.227 | -2.6% | -0.0366 to 0.0245 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 160 | 161 | +0.3% | -5.12 to 6.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 158 | 158 | -0.1% | -5.69 to 5.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.27 | +25.0% | 0.491 to 0.817 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 311 | 303 | -2.6% | -48.7 to 32.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,909 | 2,907 | -0.1% | -11.3 to 8.07 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,911 | -0.1% | -10.1 to 7.15 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.193 | 0.187 | -3.3% | -0.0115 to -0.00116 | GAIN |
| latency, 99th percentile (ms) | 0.365 | 0.361 | -1.0% | -0.0298 to 0.0224 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.148 | 0.146 | -1.7% | -0.0135 to 0.00848 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 962 | +87.9% | 13.8 to 887 | power given |
| bytes in the cache, mean (MB) | 419 | 762 | +81.9% | -8.12 to 694 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 734,491 | 343,090 | -53.3% | -410,076 to -372,725 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.163 | +3.3% | -0.0425 to 0.0528 | STEADY, no difference beyond the noise |
| host CPU-seconds | 285 | 298 | +4.5% | -90.9 to 117 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.223 | +4.6% | -0.0677 to 0.0873 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -1.13 to 6.46 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 142 | 135 | -4.8% | -9 to -4.73 | GAIN |
| the server's own CPU-seconds (mongod) | 140 | 133 | -5.3% | -9.56 to -5.25 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.07 | 2.61 | +26.1% | 0.392 to 0.691 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 285 | 298 | +4.5% | -90.9 to 117 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,752 | 5,753 | +0.0% | -3.78 to 5.43 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,767 | 5,768 | +0.0% | -2.53 to 4.71 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.311 | -2.2% | -0.0136 to -0.000427 | GAIN |
| latency, 99th percentile (ms) | 0.48 | 0.473 | -1.5% | -0.0276 to 0.0129 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.178 | -1.4% | -0.0036 to -0.00133 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 996 | +94.6% | 298 to 670 | power given |
| bytes in the cache, mean (MB) | 418 | 785 | +87.7% | 232 to 502 | power given |
| pages read into the cache (misses) | 687,160 | 307,967 | -55.2% | -523,974 to -234,411 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.246 | +0.2% | -0.0297 to 0.0307 | STEADY, no difference beyond the noise |
| host CPU-seconds | 444 | 447 | +0.7% | -68.6 to 74.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.166 | 0.167 | +0.7% | -0.0255 to 0.0277 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | -2.84 to 11.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 271 | 265 | -2.1% | -7.23 to -4.32 | GAIN |
| the server's own CPU-seconds (mongod) | 268 | 261 | -2.3% | -7.74 to -4.78 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.45 | 3.93 | +14.1% | 0.267 to 0.704 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 444 | 447 | +0.7% | -68.6 to 74.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,877 | +0.1% | -7.44 to 12.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,887 | +0.1% | -6.33 to 9.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.375 | 0.359 | -4.3% | -0.025 to -0.00704 | GAIN |
| latency, 99th percentile (ms) | 0.596 | 0.577 | -3.2% | -0.0531 to 0.0144 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.217 | -3.4% | -0.0144 to -0.00107 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,383 | +170.1% | 665 to 1,077 | power given |
| bytes in the cache, mean (MB) | 417 | 1,085 | +160.1% | 522 to 815 | power given |
| pages read into the cache (misses) | 676,817 | 265,707 | -60.7% | -520,446 to -301,774 | shown, not judged |
| host CPU busy (share of the run) | 0.263 | 0.246 | -6.5% | -0.0794 to 0.0452 | STEADY, no difference beyond the noise |
| host CPU-seconds | 467 | 432 | -7.5% | -176 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.352 | 0.325 | -7.5% | -0.133 to 0.0802 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 1.7 to 10.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 278 | 267 | -3.8% | -16.7 to -4.1 | GAIN |
| the server's own CPU-seconds (mongod) | 275 | 264 | -4.0% | -17.2 to -4.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.58 | 3.17 | +22.8% | 0.423 to 0.757 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 467 | 432 | -7.5% | -176 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
