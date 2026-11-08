# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | -0.0% | -1.38 to 0.825 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,916 | +0.0% | -0.578 to 0.693 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.206 | 0.207 | +0.5% | -0.00397 to 0.00597 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.394 | 0.399 | +1.2% | -0.0202 to 0.0296 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.142 | 0.144 | +1.3% | -0.00616 to 0.00998 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 417 | 419 | +0.7% | -0.0588 to 5.56 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 705,773 | 722,217 | +2.3% | -100,979 to 133,868 | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.162 | -7.8% | -0.0757 to 0.0481 | STEADY, no difference beyond the noise |
| host CPU-seconds | 325 | 294 | -9.6% | -174 to 112 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.244 | 0.22 | -9.6% | -0.13 to 0.0835 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 151 | 152 | +0.8% | -2.14 to 4.47 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 149 | 149 | +0.4% | -2.6 to 3.88 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.97 | 2.5 | +26.7% | 0.45 to 0.604 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 325 | 294 | -9.6% | -174 to 112 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,875 | -0.1% | -12.7 to 6.67 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -6.14 to 4.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.468 | 0.474 | +1.2% | -0.00468 to 0.016 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.65 | 0.679 | +4.5% | -0.0377 to 0.0957 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.228 | +1.7% | -0.00903 to 0.0167 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 523 | +2.1% | -35 to 56.3 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 410 | +2.1% | -24.8 to 41.7 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 268,149 | 261,793 | -2.4% | -25,709 to 12,996 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.221 | +10.1% | -0.0179 to 0.0584 | STEADY, no difference beyond the noise |
| host CPU-seconds | 140 | 158 | +12.9% | -14.1 to 50.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.297 | +13.0% | -0.0262 to 0.0945 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.7 | 83.6 | +1.0% | -5.76 to 7.46 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81.7 | 82.3 | +0.7% | -5.91 to 7.11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.04 | 1.29 | +24.6% | 0.155 to 0.355 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 140 | 158 | +12.9% | -14.1 to 50.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,932 | -0.0% | -5.25 to 3.91 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,934 | 2,933 | -0.0% | -5.06 to 3.84 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.198 | +0.2% | -0.0011 to 0.00177 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.406 | 0.409 | +0.6% | -0.0166 to 0.0213 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.111 | 0.11 | -0.3% | -0.00338 to 0.00265 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 417 | 418 | +0.1% | -4.37 to 4.78 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 712,252 | 671,684 | -5.7% | -164,409 to 83,273 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.124 | +3.2% | -0.0143 to 0.0221 | STEADY, no difference beyond the noise |
| host CPU-seconds | 220 | 227 | +3.5% | -28.7 to 44.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.164 | 0.17 | +3.5% | -0.0215 to 0.0331 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 85.3 | 85.7 | +0.5% | -1.47 to 2.32 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 83.4 | 83.3 | -0.2% | -2.03 to 1.74 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.92 | 2.49 | +29.7% | 0.547 to 0.594 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 220 | 227 | +3.5% | -28.7 to 44.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,717 | 5,728 | +0.2% | -76 to 97.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,733 | 5,744 | +0.2% | -71.7 to 93.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.324 | -2.0% | -0.0129 to -0.000415 | GAIN |
| latency, 99th percentile (ms) | 0.505 | 0.505 | -0.1% | -0.0408 to 0.0395 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.193 | -2.2% | -0.0113 to 0.00275 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,272 | +148.4% | 392 to 1,128 | power given |
| bytes in the cache, mean (MB) | 416 | 925 | +122.7% | 248 to 771 | power given |
| pages read into the cache (misses) | 681,804 | 198,935 | -70.8% | -632,997 to -332,742 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.249 | -2.7% | -0.0265 to 0.0124 | STEADY, no difference beyond the noise |
| host CPU-seconds | 465 | 450 | -3.2% | -59.4 to 29.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.175 | 0.169 | -3.4% | -0.0255 to 0.0134 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 41.3 |  | 24.4 to 58.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 279 | 275 | -1.5% | -7.59 to -0.713 | GAIN |
| the server's own CPU-seconds (mongod) | 275 | 270 | -1.8% | -8.1 to -1.58 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.74 | 4.43 | +18.4% | 0.452 to 0.927 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 465 | 450 | -3.2% | -59.4 to 29.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,872 | -0.1% | -7.86 to 2.08 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,882 | -0.1% | -7.8 to 1.76 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.36 | 0.355 | -1.6% | -0.0198 to 0.00846 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.583 | 0.577 | -1.0% | -0.0215 to 0.00951 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.215 | -1.7% | -0.0173 to 0.01 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,377 | +169.0% | 758 to 972 | power given |
| bytes in the cache, mean (MB) | 417 | 1,081 | +159.0% | 583 to 744 | power given |
| pages read into the cache (misses) | 674,617 | 284,888 | -57.8% | -455,626 to -323,832 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.268 | +3.3% | -0.00791 to 0.0253 | STEADY, no difference beyond the noise |
| host CPU-seconds | 461 | 484 | +5.0% | -27.3 to 73.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.347 | 0.365 | +5.1% | -0.0203 to 0.0561 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 3.52 to 8.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 271 | 266 | -1.9% | -25.8 to 15.4 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 268 | 262 | -2.2% | -26.4 to 14.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.53 | 3.15 | +24.6% | 0.46 to 0.784 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 461 | 484 | +5.0% | -27.3 to 73.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
