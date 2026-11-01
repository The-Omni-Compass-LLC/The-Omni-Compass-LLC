# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% | -1.75 to 0.697 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | -0.0% | -2.08 to 0.736 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.319 | -1.2% | -0.0178 to 0.00983 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.577 | -1.3% | -0.0174 to 0.00271 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.195 | -2.1% | -0.0103 to 0.00216 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | +0.1% | -5.17 to 6.08 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 699,368 | 721,068 | +3.1% | -201,597 to 244,996 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.193 | -3.6% | -0.0771 to 0.0629 | STEADY, no difference beyond the noise |
| host CPU-seconds | 351 | 337 | -4.0% | -165 to 137 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.254 | -4.0% | -0.124 to 0.103 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 198 | 193 | -2.5% | -11.3 to 1.34 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 195 | 190 | -2.8% | -11.9 to 0.779 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 3.05 | +23.4% | 0.528 to 0.63 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 351 | 337 | -4.0% | -165 to 137 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,880 | +0.0% | -3.04 to 3.31 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -3.02 to 3.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.454 | 0.448 | -1.2% | -0.0282 to 0.0169 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.644 | 0.636 | -1.2% | -0.0246 to 0.00924 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.212 | -1.8% | -0.00907 to 0.00126 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 401 | 399 | -0.4% | -7.22 to 3.83 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 280,336 | 262,105 | -6.5% | -34,071 to -2,392 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.161 | -22.3% | -0.0856 to -0.00665 | GAIN |
| host CPU-seconds | 148 | 108 | -26.5% | -76.4 to -1.81 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.204 | -26.5% | -0.144 to -0.00347 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80.1 | 77.9 | -2.8% | -4.9 to 0.44 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79.1 | 76.7 | -3.1% | -5.17 to 0.256 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.999 | 1.22 | +22.6% | 0.145 to 0.306 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 148 | 108 | -26.5% | -76.4 to -1.83 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,938 | -0.0% | -2.87 to 1.97 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,939 | -0.0% | -2.55 to 1.95 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0963 | 0.1 | +3.8% | -0.0175 to 0.0248 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.31 | 0.316 | +1.7% | -0.0413 to 0.052 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0595 | 0.0608 | +2.2% | -0.00449 to 0.00715 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 419 | -0.5% | -12.8 to 8.75 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 681,579 | 739,355 | +8.5% | -54,177 to 169,728 | shown, not judged |
| host CPU busy (share of the run) | 0.0994 | 0.0721 | -27.5% | -0.0751 to 0.0206 | STEADY, no difference beyond the noise |
| host CPU-seconds | 184 | 130 | -29.6% | -148 to 38.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.137 | 0.0967 | -29.6% | -0.111 to 0.0291 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50.9 | 52.9 | +4.0% | -3.75 to 7.79 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 49.2 | 50.7 | +3.0% | -4.11 to 7.09 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.67 | 2.21 | +31.8% | 0.363 to 0.704 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 184 | 130 | -29.6% | -148 to 38.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,669 | 5,743 | +1.3% | -167 to 315 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,687 | 5,761 | +1.3% | -163 to 311 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.318 | -1.3% | -0.0119 to 0.00326 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.496 | -0.1% | -0.0666 to 0.0653 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.189 | -3.3% | -0.0197 to 0.00665 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,176 | +129.6% | 159 to 1,168 | power given |
| bytes in the cache, mean (MB) | 413 | 911 | +120.5% | 116 to 880 | power given |
| pages read into the cache (misses) | 688,416 | 227,820 | -66.9% | -661,684 to -259,508 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.245 | +1.8% | -0.0135 to 0.0222 | STEADY, no difference beyond the noise |
| host CPU-seconds | 434 | 443 | +2.1% | -37.7 to 55.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.166 | +0.7% | -0.0235 to 0.0258 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 270 | 269 | -0.2% | -18.5 to 17.6 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 266 | 265 | -0.4% | -18.8 to 16.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.44 | 4.12 | +19.5% | 0.277 to 1.07 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 434 | 443 | +2.1% | -37.7 to 55.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,900 | +0.1% | -2.78 to 8.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,910 | +0.1% | -0.264 to 5.63 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.324 | -5.6% | -0.0504 to 0.0117 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.587 | 0.568 | -3.2% | -0.0645 to 0.0265 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.158 | 0.147 | -7.0% | -0.0145 to -0.00749 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,341 | +162.0% | 402 to 1,257 | power given |
| bytes in the cache, mean (MB) | 417 | 1,043 | +150.4% | 306 to 947 | power given |
| pages read into the cache (misses) | 673,134 | 180,558 | -73.2% | -638,145 to -347,008 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.204 | -1.0% | -0.0442 to 0.0399 | STEADY, no difference beyond the noise |
| host CPU-seconds | 379 | 379 | -0.1% | -102 to 101 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.285 | 0.285 | -0.1% | -0.0766 to 0.0759 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 12.3 |  | 2.29 to 22.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 190 | 175 | -7.6% | -24.1 to -4.76 | GAIN |
| the server's own CPU-seconds (mongod) | 187 | 172 | -8.0% | -24.5 to -5.39 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.43 | 2.96 | +21.9% | 0.437 to 0.627 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 379 | 379 | -0.1% | -102 to 101 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
