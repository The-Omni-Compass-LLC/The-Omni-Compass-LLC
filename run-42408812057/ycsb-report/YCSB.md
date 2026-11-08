# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -1.7 to 1.27 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -1.53 to 1.32 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.334 | +0.4% | -0.0044 to 0.00707 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.495 | 0.498 | +0.6% | -0.0121 to 0.0181 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.202 | +0.6% | -0.00141 to 0.00367 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | +0.1% | -5.37 to 5.92 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 696,620 | 723,470 | +3.9% | -78,964 to 132,663 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.207 | +10.2% | -0.0329 to 0.0712 | STEADY, no difference beyond the noise |
| host CPU-seconds | 322 | 362 | +12.5% | -71.7 to 152 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.272 | +12.5% | -0.0539 to 0.114 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 202 | 204 | +0.9% | -2.87 to 6.49 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 200 | 201 | +0.6% | -3.56 to 5.85 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 3.2 | +26.0% | 0.61 to 0.71 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 322 | 362 | +12.5% | -71.7 to 152 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,902 | 2,902 | -0.0% | -3.14 to 2.65 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,905 | -0.0% | -3.26 to 2.86 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.352 | 0.355 | +0.9% | -0.00445 to 0.0105 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.509 | 0.514 | +1.0% | -0.00471 to 0.0154 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.167 | 0.169 | +1.0% | -0.00231 to 0.00569 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 406 | 404 | -0.7% | -18.9 to 13.2 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 267,290 | 269,643 | +0.9% | -11,657 to 16,364 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.182 | +4.0% | -0.0634 to 0.0774 | STEADY, no difference beyond the noise |
| host CPU-seconds | 127 | 133 | +4.7% | -55.9 to 67.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.25 | +4.7% | -0.105 to 0.127 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 61.5 | 62.4 | +1.4% | -0.0991 to 1.85 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 60.6 | 61.2 | +1.0% | -0.325 to 1.58 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.979 | 1.22 | +24.8% | 0.16 to 0.326 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 127 | 133 | +4.7% | -55.9 to 67.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,937 | +0.0% | -3.52 to 4.08 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,938 | +0.0% | -3.74 to 4.35 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0913 | 0.0957 | +4.7% | -0.00935 to 0.018 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.273 | 0.286 | +5.0% | -0.0188 to 0.0461 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0585 | 0.0597 | +2.0% | -0.00147 to 0.00386 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 421 | +0.2% | -3.25 to 5.08 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 688,628 | 717,325 | +4.2% | -97,830 to 155,225 | shown, not judged |
| host CPU busy (share of the run) | 0.0763 | 0.0874 | +14.5% | -0.0287 to 0.0509 | STEADY, no difference beyond the noise |
| host CPU-seconds | 138 | 160 | +15.9% | -58.7 to 103 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.103 | 0.12 | +15.9% | -0.0439 to 0.0766 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50 | 52.5 | +5.0% | -1.21 to 6.24 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 48.1 | 50.1 | +4.1% | -1.47 to 5.39 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.85 | 2.4 | +30.1% | 0.259 to 0.853 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 138 | 160 | +15.9% | -58.7 to 103 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,672 | 5,674 | +0.0% | -32.2 to 37.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,690 | 5,693 | +0.0% | -31.8 to 36.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.451 | 0.445 | -1.3% | -0.0137 to 0.00232 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.714 | 0.711 | -0.4% | -0.00892 to 0.00359 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.247 | -1.4% | -0.00389 to -0.00322 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,425 | +178.3% | 688 to 1,137 | power given |
| bytes in the cache, mean (MB) | 416 | 1,111 | +167.1% | 526 to 865 | power given |
| pages read into the cache (misses) | 679,199 | 241,999 | -64.4% | -553,246 to -321,155 | shown, not judged |
| host CPU busy (share of the run) | 0.331 | 0.33 | -0.1% | -0.0146 to 0.0141 | STEADY, no difference beyond the noise |
| host CPU-seconds | 598 | 600 | +0.3% | -30 to 33.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.226 | +0.2% | -0.013 to 0.0141 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | -7.01 to 21.7 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 358 | 351 | -1.9% | -10.1 to -3.73 | GAIN |
| the server's own CPU-seconds (mongod) | 354 | 346 | -2.2% | -10.6 to -4.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.51 | 5.18 | +15.0% | 0.455 to 0.895 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 598 | 600 | +0.3% | -30 to 33.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,886 | -0.5% | -69.9 to 41.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,897 | -0.4% | -68.3 to 42.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.227 | 0.225 | -0.9% | -0.0232 to 0.0192 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.429 | 0.437 | +2.0% | -0.00359 to 0.0209 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.178 | 0.174 | -2.3% | -0.0269 to 0.0185 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,200 | +134.3% | 386 to 989 | power given |
| bytes in the cache, mean (MB) | 416 | 901 | +116.8% | 309 to 662 | power given |
| pages read into the cache (misses) | 682,025 | 223,246 | -67.3% | -573,035 to -344,523 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.195 | +1.1% | -0.0148 to 0.019 | STEADY, no difference beyond the noise |
| host CPU-seconds | 344 | 350 | +1.8% | -31.4 to 43.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.258 | 0.264 | +2.4% | -0.0231 to 0.0353 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 30 |  | -5.22 to 65.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 215 | 208 | -3.0% | -12.5 to -0.329 | GAIN |
| the server's own CPU-seconds (mongod) | 213 | 206 | -3.3% | -13 to -1.04 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.17 | 2.82 | +29.6% | 0.569 to 0.719 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 344 | 350 | +1.8% | -31.5 to 43.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
