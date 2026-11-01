# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | +0.0% | -0.79 to 1.28 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | +0.0% | -1.1 to 1.99 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.311 | -1.8% | -0.0193 to 0.00802 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 0.545 | +0.3% | -0.00981 to 0.0131 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.187 | -1.7% | -0.00601 to -0.000455 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 538 | +5.0% | -84.4 to 135 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 435 | +4.1% | -72.3 to 107 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 714,300 | 648,341 | -9.2% | -195,561 to 63,642 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.184 | -5.6% | -0.0726 to 0.0507 | STEADY, no difference beyond the noise |
| host CPU-seconds | 342 | 319 | -6.6% | -155 to 110 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.257 | 0.24 | -6.6% | -0.117 to 0.0827 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 192 | 189 | -1.7% | -6.88 to 0.302 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 190 | 186 | -2.0% | -7.4 to -0.215 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.01 | +20.7% | 0.406 to 0.628 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 342 | 320 | -6.6% | -155 to 110 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,876 | -0.0% | -7.12 to 6.35 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -1.2 to 0.787 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.508 | 0.513 | +0.9% | -0.0162 to 0.0255 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.671 | 0.685 | +2.0% | -0.0787 to 0.106 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.227 | 0.229 | +0.9% | -0.00644 to 0.0104 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 547 | +6.8% | -40.4 to 110 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 431 | +7.7% | -23.8 to 85.2 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 272,417 | 266,553 | -2.2% | -55,177 to 43,449 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.207 | +0.2% | -0.0885 to 0.0894 | STEADY, no difference beyond the noise |
| host CPU-seconds | 147 | 146 | -0.2% | -80 to 79.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.276 | -0.2% | -0.15 to 0.149 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81.3 | 82.3 | +1.3% | -2.94 to 4.99 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 80.2 | 81 | +1.0% | -3.08 to 4.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.25 | +23.6% | 0.0895 to 0.388 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 147 | 146 | -0.2% | -80 to 79.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,938 | +0.0% | -4.97 to 6.17 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,940 | +0.0% | -5.5 to 6.63 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0963 | 0.0947 | -1.7% | -0.0191 to 0.0158 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.305 | 0.311 | +2.0% | -0.0457 to 0.0577 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0603 | 0.0594 | -1.5% | -0.00645 to 0.00464 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 420 | -0.2% | -7.33 to 5.27 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 716,959 | 680,091 | -5.1% | -168,716 to 94,980 | shown, not judged |
| host CPU busy (share of the run) | 0.0807 | 0.0794 | -1.6% | -0.0975 to 0.095 | STEADY, no difference beyond the noise |
| host CPU-seconds | 147 | 144 | -1.6% | -194 to 189 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.11 | 0.108 | -1.6% | -0.145 to 0.141 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 52.5 | 51.8 | -1.3% | -6.68 to 5.28 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50.8 | 49.6 | -2.3% | -7.04 to 4.65 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.69 | 2.18 | +29.2% | 0.359 to 0.627 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 147 | 144 | -1.6% | -194 to 189 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,847 | 5,851 | +0.1% | -8.47 to 15.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,855 | 5,858 | +0.1% | -8.68 to 15.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.152 | 0.152 | +0.4% | -0.0111 to 0.0124 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.335 | 0.35 | +4.4% | -0.0552 to 0.0845 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0802 | 0.0796 | -0.8% | -0.00371 to 0.00239 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 630 | +23.0% | -176 to 411 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 508 | +21.2% | -130 to 308 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 699,562 | 577,534 | -17.4% | -440,691 to 196,635 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.121 | -14.3% | -0.105 to 0.0643 | STEADY, no difference beyond the noise |
| host CPU-seconds | 260 | 219 | -15.9% | -218 to 135 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0972 | 0.0817 | -16.0% | -0.0814 to 0.0503 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | -3.5 to 6.84 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 117 | 116 | -1.0% | -5.25 to 2.82 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 114 | 113 | -1.4% | -5.57 to 2.48 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 2.84 | +13.3% | 0.0139 to 0.652 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 260 | 219 | -15.9% | -218 to 135 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,933 | -0.0% | -3.48 to 0.88 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -3.63 to 1.71 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.151 | 0.157 | +4.2% | -0.0219 to 0.0346 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.349 | 0.359 | +2.8% | -0.0305 to 0.0498 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0796 | 0.0802 | +0.8% | -0.00646 to 0.00776 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 745 | +45.5% | 82.9 to 383 | power given |
| bytes in the cache, mean (MB) | 419 | 595 | +41.9% | 68.6 to 283 | power given |
| pages read into the cache (misses) | 696,189 | 462,299 | -33.6% | -366,542 to -101,238 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.115 | -13.3% | -0.0924 to 0.0571 | STEADY, no difference beyond the noise |
| host CPU-seconds | 245 | 207 | -15.5% | -192 to 116 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.183 | 0.155 | -15.5% | -0.143 to 0.0865 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 105 | 106 | +1.1% | -10.8 to 13 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 103 | 104 | +0.5% | -11.3 to 12.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.63 | 2.29 | +40.4% | 0.445 to 0.875 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 245 | 207 | -15.5% | -192 to 116 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
