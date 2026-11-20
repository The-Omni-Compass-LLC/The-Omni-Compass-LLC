# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,889 | +0.0% | -1.23 to 1.86 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | +0.0% | -0.933 to 1.34 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.312 | 0.317 | +1.7% | -0.00407 to 0.0147 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.491 | 0.493 | +0.5% | -0.000535 to 0.0052 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.19 | +0.7% | 0.000575 to 0.00213 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,366 | -0.0% | -2.74 to 2.56 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,763 | 61,850 | +0.1% | -219 to 392 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.182 | +3.9% | -0.0375 to 0.0513 | STEADY, no difference beyond the noise |
| host CPU-seconds | 300 | 314 | +4.8% | -79.5 to 108 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.236 | +4.8% | -0.0598 to 0.0814 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 183 | 185 | +0.8% | -1.63 to 4.66 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 181 | 182 | +0.8% | -1.65 to 4.51 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 2.55 | +3.2% | 0.0137 to 0.143 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 300 | 314 | +4.8% | -79.5 to 108 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,927 | 2,933 | +0.2% | 0.285 to 11.7 | GAIN |
| throughput (operations a second) | 2,933 | 2,937 | +0.1% | -0.761 to 7.62 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.254 | 0.258 | +1.4% | -0.0362 to 0.0435 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.418 | 0.405 | -3.2% | -0.0937 to 0.067 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0827 | 0.0786 | -5.0% | -0.0161 to 0.00793 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,519 | 1,520 | +0.0% | -3.18 to 4.31 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,653 | 77,732 | +0.1% | -89.2 to 246 | shown, not judged |
| host CPU busy (share of the run) | 0.092 | 0.0915 | -0.5% | -0.0793 to 0.0784 | STEADY, no difference beyond the noise |
| host CPU-seconds | 67.1 | 66.9 | -0.3% | -63.3 to 62.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.125 | 0.125 | -0.5% | -0.118 to 0.117 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 24 | 23.3 | -3.3% | -4.48 to 2.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 23.2 | 22.4 | -3.4% | -4.37 to 2.81 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.813 | 0.803 | -1.2% | -0.134 to 0.114 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 67.1 | 66.9 | -0.3% | -63.3 to 62.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,909 | 2,905 | -0.1% | -7.79 to 0.0453 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,908 | -0.1% | -7.34 to -0.413 | LOSS |
| latency, 95th percentile (ms) | 0.182 | 0.182 | +0.0% | -0.00657 to 0.00657 | STEADY, the same |
| latency, 99th percentile (ms) | 0.368 | 0.366 | -0.4% | -0.0252 to 0.0225 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.136 | 0.136 | +0.4% | -0.00774 to 0.00877 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,345 | -0.2% | -8.3 to 3.3 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,660 | 61,654 | -0.0% | -130 to 120 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.141 | -4.4% | -0.013 to 2.3e-05 | STEADY, no difference beyond the noise |
| host CPU-seconds | 266 | 252 | -5.1% | -26.1 to -1.28 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.199 | 0.189 | -5.1% | -0.0198 to -0.000414 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 128 | 129 | +0.5% | -2.71 to 4.07 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 126 | 127 | +0.5% | -2.66 to 3.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.03 | 2.12 | +4.5% | -0.0583 to 0.24 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 266 | 252 | -5.1% | -26.1 to -1.24 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,670 | 5,669 | -0.0% | -11.1 to 8.2 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,685 | 5,683 | -0.0% | -11.7 to 8.87 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.42 | 0.416 | -0.9% | -0.0113 to 0.00392 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.657 | 0.655 | -0.3% | -0.0131 to 0.00981 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.241 | 0.239 | -0.9% | -0.00903 to 0.00462 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,359 | 1,361 | +0.1% | -2.12 to 5.33 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,932 | 62,959 | +0.0% | -384 to 438 | shown, not judged |
| host CPU busy (share of the run) | 0.318 | 0.315 | -0.9% | -0.0259 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 576 | 571 | -0.9% | -60.3 to 50.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.218 | 0.216 | -0.8% | -0.0231 to 0.0194 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 317 | 312 | -1.4% | -17.5 to 8.44 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 313 | 308 | -1.5% | -17.6 to 8.43 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.42 | 4.48 | +1.4% | -0.0408 to 0.163 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 576 | 571 | -0.9% | -60.3 to 50.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -6.52 to 4.69 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -6.62 to 4.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.347 | +0.9% | -0.0149 to 0.0209 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.527 | 0.524 | -0.6% | -0.00957 to 0.00357 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.208 | -0.9% | -0.00921 to 0.0054 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.0% | -12.4 to 11.9 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,210 | 63,139 | -0.1% | -1,697 to 1,556 | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.245 | +5.3% | -0.042 to 0.0667 | STEADY, no difference beyond the noise |
| host CPU-seconds | 406 | 434 | +7.0% | -98.8 to 156 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.305 | 0.327 | +7.0% | -0.0744 to 0.117 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 238 | 235 | -0.9% | -10.8 to 6.4 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 235 | 233 | -1.0% | -10.9 to 6.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.56 | 2.67 | +4.4% | -0.0082 to 0.233 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 406 | 434 | +7.0% | -98.8 to 156 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
