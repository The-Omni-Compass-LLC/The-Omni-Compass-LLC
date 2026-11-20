# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,910 | +0.0% | -0.613 to 1.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,913 | +0.0% | -0.469 to 1.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.282 | 0.28 | -0.6% | -0.0174 to 0.0141 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.477 | +0.1% | -0.027 to 0.0277 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.125 | 0.124 | -0.6% | -0.0026 to 0.00107 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 418 | -0.7% | -6.54 to 0.381 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 726,283 | 701,537 | -3.4% | -101,242 to 51,749 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.145 | -11.8% | -0.0489 to 0.0102 | STEADY, no difference beyond the noise |
| host CPU-seconds | 303 | 261 | -13.7% | -103 to 19.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.196 | -13.7% | -0.0771 to 0.015 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 115 | 115 | -0.4% | -2.62 to 1.69 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 113 | 112 | -0.9% | -3.18 to 1.08 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.33 | 2.92 | +25.1% | 0.491 to 0.683 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 303 | 261 | -13.7% | -103 to 19.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,871 | 2,870 | -0.0% | -3.59 to 1.01 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,882 | -0.0% | -4.96 to 2.96 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.521 | 0.521 | -0.1% | -0.0147 to 0.014 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.724 | 0.727 | +0.4% | -0.0247 to 0.0307 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.233 | 0.231 | -0.7% | -0.00818 to 0.00477 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 653 | +27.5% | -240 to 521 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 509 | +27.2% | -169 to 387 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 270,370 | 247,535 | -8.4% | -68,973 to 23,303 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.197 | -13.3% | -0.0971 to 0.0368 | STEADY, no difference beyond the noise |
| host CPU-seconds | 163 | 136 | -16.4% | -86.5 to 33 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.307 | 0.257 | -16.4% | -0.163 to 0.0627 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83.6 | 82.4 | -1.5% | -3.92 to 1.49 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82.5 | 81.1 | -1.8% | -4.26 to 1.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.08 | 1.33 | +23.1% | 0.132 to 0.368 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 163 | 136 | -16.4% | -86.5 to 33 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,889 | +0.0% | -1.14 to 1.94 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,892 | +0.0% | -1.62 to 2.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.306 | +0.2% | -0.00313 to 0.00446 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.482 | 0.482 | -0.1% | -0.00607 to 0.0054 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.189 | +0.1% | -0.00179 to 0.00219 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 418 | -0.1% | -8.85 to 7.78 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 664,685 | 683,542 | +2.8% | -80,898 to 118,612 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.171 | -0.1% | -0.0551 to 0.0547 | STEADY, no difference beyond the noise |
| host CPU-seconds | 292 | 291 | -0.2% | -112 to 110 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.219 | 0.219 | -0.2% | -0.0837 to 0.083 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 188 | +0.7% | -0.648 to 3.16 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 185 | +0.4% | -1.14 to 2.49 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.42 | 3 | +23.9% | 0.447 to 0.713 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 292 | 291 | -0.2% | -112 to 110 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,745 | 5,700 | -0.8% | -175 to 85.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,763 | 5,720 | -0.7% | -169 to 83 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.321 | -1.3% | -0.0131 to 0.00439 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.518 | 0.532 | +2.6% | -0.0396 to 0.067 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.193 | +0.8% | -0.016 to 0.019 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,254 | +145.0% | 694 to 791 | power given |
| bytes in the cache, mean (MB) | 416 | 903 | +117.4% | 316 to 659 | power given |
| pages read into the cache (misses) | 699,229 | 222,194 | -68.2% | -509,508 to -444,563 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.256 | +4.8% | 0.000927 to 0.0224 | power given |
| host CPU-seconds | 438 | 468 | +6.9% | 7.43 to 53.1 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.164 | 0.177 | +7.8% | 0.00825 to 0.0173 | power given |
| cache size changes written (the knob's moves) | 0 | 32.3 |  | -1.58 to 66.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 268 | -3.1% | -11.7 to -5.37 | GAIN |
| the server's own CPU-seconds (mongod) | 273 | 264 | -3.3% | -12.2 to -6.08 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.69 | 4.29 | +16.2% | 0.469 to 0.727 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 438 | 468 | +6.9% | 7.45 to 53.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,903 | -0.0% | -5.48 to 3.46 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,912 | -0.0% | -2.63 to 1.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.223 | 0.222 | -0.3% | -0.0206 to 0.0193 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.423 | 0.424 | +0.2% | -0.0272 to 0.0292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.163 | 0.16 | -1.4% | -0.0132 to 0.00857 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 818 | +59.7% | -15.1 to 626 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 648 | +55.0% | -14.7 to 474 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 676,888 | 417,798 | -38.3% | -472,936 to -45,243 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.2 | +6.1% | -0.0313 to 0.0542 | STEADY, no difference beyond the noise |
| host CPU-seconds | 335 | 361 | +7.7% | -68.7 to 121 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.251 | 0.271 | +7.8% | -0.052 to 0.0909 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.67 |  | -13 to 28.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 212 | 210 | -0.8% | -6.44 to 2.91 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 209 | 207 | -1.1% | -6.95 to 2.32 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.1 | 2.65 | +26.1% | 0.458 to 0.639 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 335 | 361 | +7.7% | -68.7 to 121 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
