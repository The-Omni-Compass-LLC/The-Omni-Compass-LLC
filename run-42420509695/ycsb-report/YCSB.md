# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,904 | -0.0% | -1.76 to 1.16 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,906 | -0.0% | -1.5 to 0.704 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.304 | 0.31 | +1.9% | -0.0123 to 0.0236 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.468 | 0.477 | +1.9% | -0.0234 to 0.0407 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.151 | 0.153 | +0.9% | -0.00376 to 0.00644 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.0% | -0.81 to 0.677 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,774 | 61,843 | +0.1% | -289 to 428 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.171 | +5.7% | -0.068 to 0.0864 | STEADY, no difference beyond the noise |
| host CPU-seconds | 288 | 308 | +6.9% | -147 to 187 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.231 | +6.9% | -0.11 to 0.14 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 142 | 143 | +1.0% | -1.93 to 4.86 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 139 | 141 | +1.0% | -1.94 to 4.59 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 2.65 | +5.7% | 0.0101 to 0.274 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 288 | 308 | +6.9% | -147 to 187 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,875 | -0.0% | -4.21 to 3.41 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | -0.0% | -4.16 to 4.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.525 | 0.526 | +0.1% | -0.000768 to 0.0021 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.7 | 0.705 | +0.7% | -0.00494 to 0.0149 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.223 | +0.4% | -0.00437 to 0.00596 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,502 | 1,501 | -0.1% | -3.22 to 1.02 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,578 | 77,567 | -0.0% | -290 to 268 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.157 | -17.8% | -0.113 to 0.0455 | STEADY, no difference beyond the noise |
| host CPU-seconds | 134 | 105 | -21.4% | -95.1 to 37.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.253 | 0.199 | -21.4% | -0.179 to 0.0705 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 76.4 | 76.2 | -0.3% | -3.85 to 3.41 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 75.4 | 75.2 | -0.3% | -3.84 to 3.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.02 | +1.6% | -0.0256 to 0.0586 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 134 | 105 | -21.4% | -95.1 to 37.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,909 | 2,912 | +0.1% | 0.955 to 3.97 | GAIN |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | 0.677 to 3.99 | GAIN |
| latency, 95th percentile (ms) | 0.167 | 0.166 | -0.6% | -0.00845 to 0.00645 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.386 | 0.39 | +1.1% | -0.0206 to 0.0292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.103 | 0.101 | -1.8% | -0.00295 to -0.000717 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,348 | -0.0% | -2.54 to 1.59 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,656 | 61,648 | -0.0% | -161 to 145 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.126 | +8.2% | -0.0141 to 0.0332 | STEADY, no difference beyond the noise |
| host CPU-seconds | 209 | 229 | +9.8% | -28.1 to 69.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.156 | 0.172 | +9.8% | -0.0211 to 0.0517 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 88.9 | 87.2 | -1.9% | -2.98 to -0.438 | GAIN |
| the server's own CPU-seconds (mongod) | 86.3 | 84.5 | -2.1% | -3.06 to -0.497 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.64 | 2.71 | +2.6% | -0.0657 to 0.203 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 209 | 229 | +9.8% | -28.1 to 69.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,673 | 5,680 | +0.1% | -7.04 to 21.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,685 | 5,692 | +0.1% | -7.22 to 21.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.42 | -0.2% | -0.00597 to 0.00397 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.627 | 0.627 | -0.1% | -0.0124 to 0.0111 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.241 | -0.2% | -0.00163 to 0.000879 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,360 | 1,360 | +0.0% | -5.86 to 6.57 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,708 | 62,798 | +0.1% | -1,637 to 1,818 | shown, not judged |
| host CPU busy (share of the run) | 0.302 | 0.301 | -0.4% | -0.0141 to 0.012 | STEADY, no difference beyond the noise |
| host CPU-seconds | 542 | 540 | -0.4% | -37.2 to 32.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.204 | -0.5% | -0.0148 to 0.0127 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 318 | 317 | -0.1% | -3.66 to 3.13 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 313 | 313 | -0.1% | -3.58 to 3.12 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.38 | 4.35 | -0.7% | -0.0804 to 0.0184 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 542 | 540 | -0.4% | -37.2 to 32.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,883 | +0.0% | -5.68 to 6.91 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -5.08 to 6.25 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.337 | -0.4% | -0.0138 to 0.0112 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.492 | 0.497 | +1.1% | 0.000162 to 0.0105 | LOSS |
| latency, mean (ms) | 0.201 | 0.203 | +1.1% | -0.00505 to 0.00933 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | -0.0% | -3.69 to 3.63 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,260 | 62,981 | -0.4% | -789 to 231 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.227 | +8.3% | -0.022 to 0.0569 | STEADY, no difference beyond the noise |
| host CPU-seconds | 359 | 398 | +10.8% | -54.4 to 132 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.27 | 0.299 | +10.8% | -0.0404 to 0.0987 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 230 | 233 | +1.1% | -7.28 to 12.5 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 228 | 230 | +1.1% | -7.28 to 12.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 2.56 | +2.3% | -0.000197 to 0.117 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 359 | 398 | +10.8% | -54.4 to 132 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
