# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,884 | +0.1% | -8.59 to 13 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,888 | +0.1% | -7.06 to 10.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.353 | 0.341 | -3.6% | -0.0793 to 0.054 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.551 | 0.542 | -1.8% | -0.0661 to 0.0468 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.193 | -1.7% | -0.0185 to 0.0118 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -3.85 to 3.84 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,774 | 61,817 | +0.1% | -326 to 411 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.195 | +7.9% | -0.155 to 0.184 | STEADY, no difference beyond the noise |
| host CPU-seconds | 309 | 343 | +11.0% | -331 to 399 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.258 | +10.9% | -0.248 to 0.299 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 190 | 188 | -1.3% | -23 to 18 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 188 | 185 | -1.3% | -22.8 to 17.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.68 | 2.7 | +0.4% | -0.321 to 0.344 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 309 | 343 | +11.0% | -331 to 399 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,907 | +0.0% | -4.34 to 5.98 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,916 | +0.0% | -3.76 to 3.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.342 | +1.9% | -0.0446 to 0.0573 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.471 | 0.47 | -0.3% | -0.0415 to 0.0388 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.149 | 0.15 | +1.0% | -0.00528 to 0.00837 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,519 | 1,519 | +0.0% | -1.75 to 2.14 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,675 | 77,714 | +0.1% | -297 to 375 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.174 | +21.0% | -0.118 to 0.178 | STEADY, no difference beyond the noise |
| host CPU-seconds | 104 | 129 | +24.2% | -105 to 155 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.195 | 0.242 | +24.2% | -0.196 to 0.291 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 58.1 | 58.4 | +0.6% | -1.26 to 1.96 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 57.3 | 57.6 | +0.6% | -1.27 to 1.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.765 | 0.78 | +2.0% | -0.0378 to 0.0677 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 104 | 129 | +24.2% | -105 to 155 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,911 | +0.1% | -2.58 to 6.24 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,915 | +0.1% | -4.36 to 7.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.18 | 0.18 | +0.2% | -0.0011 to 0.00177 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.356 | 0.355 | -0.3% | -0.0458 to 0.0438 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.14 | 0.135 | -3.4% | -0.00668 to -0.00271 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,347 | 1,348 | +0.1% | -2.52 to 4.77 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,669 | 61,644 | -0.0% | -178 to 129 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.149 | -0.8% | -0.0861 to 0.0838 | STEADY, no difference beyond the noise |
| host CPU-seconds | 273 | 270 | -0.8% | -183 to 178 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.204 | 0.202 | -0.8% | -0.137 to 0.133 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 128 | 129 | +0.6% | 0.183 to 1.46 | power given |
| the server's own CPU-seconds (mongod) | 126 | 127 | +0.6% | 0.36 to 1.11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.01 | 2.1 | +4.3% | -0.183 to 0.355 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 273 | 270 | -0.8% | -183 to 178 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,753 | 5,755 | +0.0% | -6.96 to 11.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,764 | 5,766 | +0.0% | -4.56 to 9.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.312 | +0.6% | -0.00297 to 0.00697 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.462 | +2.4% | -0.052 to 0.074 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.179 | 0.179 | +0.0% | -0.0109 to 0.011 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -8.24 to 5.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,191 | 63,084 | -0.2% | -865 to 652 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.239 | -0.3% | -0.0706 to 0.0691 | STEADY, no difference beyond the noise |
| host CPU-seconds | 442 | 440 | -0.3% | -172 to 170 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.166 | 0.165 | -0.3% | -0.0646 to 0.0635 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 242 | 242 | +0.3% | -4.89 to 6.51 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 238 | 239 | +0.3% | -4.69 to 6.21 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.47 | 3.52 | +1.5% | -0.203 to 0.306 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 442 | 440 | -0.3% | -172 to 170 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,936 | +0.0% | -5.03 to 5.48 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,938 | +0.0% | -4.64 to 5.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.138 | 0.144 | +4.8% | -0.0194 to 0.0328 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.344 | 0.362 | +5.3% | -0.0399 to 0.0766 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0735 | 0.0742 | +0.9% | -0.0014 to 0.00278 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,364 | -0.1% | -6.15 to 4.02 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,506 | 63,447 | -0.1% | -1,247 to 1,129 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.0925 | -20.4% | -0.132 to 0.0846 | STEADY, no difference beyond the noise |
| host CPU-seconds | 216 | 165 | -23.5% | -283 to 181 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.124 | -23.5% | -0.211 to 0.135 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83.8 | 83.8 | +0.0% | -3.64 to 3.71 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82 | 82 | -0.1% | -3.46 to 3.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.74 | 1.82 | +4.6% | -0.185 to 0.345 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 216 | 165 | -23.5% | -283 to 181 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
