# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,938 | +0.1% | -3.3 to 6.64 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,939 | +0.1% | -3.42 to 6.78 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.148 | 0.136 | -7.9% | -0.0662 to 0.0429 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.327 | 0.321 | -1.7% | -0.0496 to 0.0382 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0674 | 0.0656 | -2.7% | -0.0076 to 0.00397 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 417 | 417 | -0.1% | -9.84 to 9.05 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 687,476 | 713,226 | +3.7% | -61,362 to 112,863 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0742 | -25.8% | -0.0684 to 0.0167 | STEADY, no difference beyond the noise |
| host CPU-seconds | 183 | 133 | -27.6% | -134 to 32.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.137 | 0.0991 | -27.6% | -0.0999 to 0.0243 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.9 | 61.1 | -2.9% | -8.02 to 4.42 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61 | 58.8 | -3.6% | -8.21 to 3.87 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.99 | 2.36 | +18.5% | 0.165 to 0.571 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 183 | 133 | -27.6% | -134 to 32.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,897 | -0.0% | -0.803 to -0.317 | LOSS |
| throughput (operations a second) | 2,907 | 2,906 | -0.0% | -1.57 to -0.104 | LOSS |
| latency, 95th percentile (ms) | 0.442 | 0.441 | -0.2% | -0.00692 to 0.00559 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.649 | 0.646 | -0.4% | -0.0141 to 0.00881 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.16 | 0.158 | -1.5% | -0.00766 to 0.003 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 578 | +13.0% | -76.4 to 209 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 404 | 458 | +13.3% | -60.2 to 168 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 273,501 | 256,588 | -6.2% | -48,857 to 15,031 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.121 | -33.4% | -0.222 to 0.101 | STEADY, no difference beyond the noise |
| host CPU-seconds | 139 | 84.7 | -39.0% | -195 to 86.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.261 | 0.159 | -39.0% | -0.366 to 0.162 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 51.2 | 50.6 | -1.1% | -2.78 to 1.64 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50.2 | 49.4 | -1.6% | -3.02 to 1.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.97 | 1.21 | +24.7% | 0.178 to 0.302 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 139 | 84.7 | -39.0% | -195 to 86.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | +0.0% | -0.905 to 1.78 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -1.19 to 2.19 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.313 | 0.312 | -0.2% | -0.00826 to 0.00692 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.494 | 0.495 | +0.2% | -0.0211 to 0.0231 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.192 | +0.5% | -0.00504 to 0.00712 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 417 | -0.7% | -5.41 to -0.437 | GAIN |
| pages read into the cache (misses) | 724,787 | 690,054 | -4.8% | -67,538 to -1,927 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.201 | +9.4% | -0.00797 to 0.0423 | STEADY, no difference beyond the noise |
| host CPU-seconds | 316 | 353 | +11.5% | -24.9 to 97.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.238 | 0.265 | +11.5% | -0.0187 to 0.0734 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 187 | 190 | +1.5% | -5.63 to 11.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 187 | +1.2% | -6.3 to 10.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 3.1 | +23.4% | 0.496 to 0.682 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 316 | 353 | +11.5% | -24.9 to 97.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,838 | 5,839 | +0.0% | -15.9 to 17.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,847 | 5,847 | +0.0% | -16.2 to 17.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.156 | 0.157 | +0.9% | -0.00492 to 0.00759 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.363 | 0.362 | -0.4% | -0.0486 to 0.0459 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0817 | 0.0823 | +0.8% | -0.00302 to 0.00432 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 669 | +30.7% | -181 to 495 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 536 | +27.9% | -138 to 372 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 711,499 | 535,137 | -24.8% | -519,964 to 167,242 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.145 | +16.0% | -0.00244 to 0.0424 | STEADY, no difference beyond the noise |
| host CPU-seconds | 226 | 268 | +18.5% | -6.56 to 90.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0845 | 0.1 | +18.4% | -0.00235 to 0.0335 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -2.84 to 7.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 117 | 120 | +1.8% | -3.43 to 7.56 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 114 | 116 | +1.3% | -3.65 to 6.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.03 | 3.56 | +17.5% | 0.207 to 0.85 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 226 | 268 | +18.5% | -6.58 to 90.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,904 | -0.1% | -7.69 to 4.38 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,914 | 2,914 | -0.0% | -3.01 to 1.82 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.217 | 0.218 | +0.3% | -0.00937 to 0.0107 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.412 | 0.416 | +1.1% | -0.0415 to 0.0508 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.158 | 0.157 | -0.3% | -0.00834 to 0.00751 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 702 | +37.2% | 30 to 351 | power given |
| bytes in the cache, mean (MB) | 418 | 564 | +34.9% | 23.8 to 268 | power given |
| pages read into the cache (misses) | 669,137 | 488,766 | -27.0% | -314,970 to -45,773 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.192 | -2.2% | -0.043 to 0.0345 | STEADY, no difference beyond the noise |
| host CPU-seconds | 353 | 343 | -3.0% | -98.4 to 77.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.265 | 0.257 | -2.9% | -0.0735 to 0.058 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 209 | 208 | -0.5% | -6.17 to 4.26 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 207 | 205 | -0.7% | -6.77 to 3.74 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.02 | 2.58 | +27.5% | 0.464 to 0.648 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 353 | 343 | -3.0% | -98.4 to 77.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
