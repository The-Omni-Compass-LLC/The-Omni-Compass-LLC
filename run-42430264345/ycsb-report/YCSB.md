# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,939 | +0.0% | -2.22 to 4.29 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,940 | +0.0% | -2.14 to 4.32 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.127 | 0.128 | +0.8% | -0.0326 to 0.0346 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.302 | 0.321 | +6.2% | -0.00622 to 0.0436 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0591 | 0.0591 | +0.0% | -0.00387 to 0.00389 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | -0.0% | -1.25 to 0.84 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,819 | 61,868 | +0.1% | -171 to 269 | shown, not judged |
| host CPU busy (share of the run) | 0.0915 | 0.0782 | -14.5% | -0.0507 to 0.0242 | STEADY, no difference beyond the noise |
| host CPU-seconds | 168 | 142 | -15.3% | -100 to 48.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.125 | 0.106 | -15.3% | -0.0748 to 0.0364 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 51.8 | 50.5 | -2.4% | -3.79 to 1.35 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 49.9 | 48.6 | -2.5% | -3.83 to 1.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.89 | 1.9 | +0.4% | -0.0234 to 0.0376 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 168 | 142 | -15.3% | -100 to 48.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,903 | +0.1% | -3.58 to 10.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | 0.439 to 3.88 | GAIN |
| latency, 95th percentile (ms) | 0.328 | 0.332 | +1.2% | -0.0184 to 0.0264 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.51 | 0.489 | -4.1% | -0.118 to 0.0769 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.165 | 0.163 | -1.2% | -0.0263 to 0.0222 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,512 | 1,518 | +0.4% | -10.5 to 22.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,663 | 77,715 | +0.1% | -105 to 210 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.148 | +4.4% | -0.0814 to 0.0938 | STEADY, no difference beyond the noise |
| host CPU-seconds | 100 | 105 | +4.3% | -66.1 to 74.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.188 | 0.196 | +4.3% | -0.125 to 0.141 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 60.7 | 60.9 | +0.4% | -1.35 to 1.8 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 59.9 | 60.1 | +0.4% | -1.3 to 1.73 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.819 | 0.827 | +1.0% | -0.0713 to 0.0869 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 100 | 105 | +4.3% | -66.1 to 74.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,940 | 2,941 | +0.0% | -4.54 to 5.21 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,942 | +0.0% | -4.9 to 5.62 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0793 | 0.0773 | -2.5% | -0.00857 to 0.00457 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.27 | 0.267 | -1.1% | -0.0267 to 0.0207 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.051 | 0.0501 | -1.9% | -0.00338 to 0.00141 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,351 | +0.1% | -1.05 to 2.83 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,654 | 61,696 | +0.1% | -114 to 199 | shown, not judged |
| host CPU busy (share of the run) | 0.0783 | 0.0669 | -14.6% | -0.12 to 0.0972 | STEADY, no difference beyond the noise |
| host CPU-seconds | 144 | 121 | -15.8% | -235 to 190 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.107 | 0.0904 | -15.8% | -0.176 to 0.142 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 41.4 | 40.2 | -2.9% | -3.6 to 1.19 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 39.6 | 38.4 | -3.0% | -3.44 to 1.06 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.8 | 1.78 | -1.0% | -0.164 to 0.13 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 144 | 121 | -15.8% | -235 to 190 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,674 | 5,676 | +0.0% | -12.2 to 17.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,687 | 5,690 | +0.1% | -10.6 to 16.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.424 | +0.7% | -0.00357 to 0.00957 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.652 | 0.659 | +1.1% | -0.00438 to 0.0184 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.24 | 0.242 | +0.8% | -0.00436 to 0.00802 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,359 | 1,362 | +0.2% | -0.831 to 6.32 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,016 | 63,169 | +0.2% | -99.2 to 404 | shown, not judged |
| host CPU busy (share of the run) | 0.314 | 0.316 | +0.6% | -0.00689 to 0.0104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 569 | 572 | +0.5% | -21.6 to 27.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.216 | +0.5% | -0.0078 to 0.00985 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 313 | 316 | +0.9% | -4.47 to 10.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 309 | 311 | +0.9% | -4.4 to 9.93 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.34 | 4.4 | +1.2% | -0.236 to 0.342 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 569 | 572 | +0.5% | -21.6 to 27.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,881 | +0.0% | -0.568 to 1.49 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,887 | +0.0% | -0.241 to 2.09 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.346 | +1.1% | -0.01 to 0.0173 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.539 | 0.547 | +1.5% | -0.0205 to 0.0371 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.209 | -0.5% | -0.00925 to 0.00729 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,362 | -0.0% | -11.5 to 10.2 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,230 | 63,163 | -0.1% | -442 to 307 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.218 | -12.4% | -0.192 to 0.13 | STEADY, no difference beyond the noise |
| host CPU-seconds | 447 | 378 | -15.3% | -439 to 302 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.336 | 0.285 | -15.3% | -0.33 to 0.228 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 237 | 234 | -1.1% | -14.6 to 9.18 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 234 | 231 | -1.2% | -14.6 to 9.02 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.6 | 2.68 | +3.0% | -0.0768 to 0.234 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 447 | 378 | -15.3% | -439 to 302 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
