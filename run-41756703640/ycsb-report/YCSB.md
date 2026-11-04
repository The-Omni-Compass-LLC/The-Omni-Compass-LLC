# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,935 | -0.0% | -5.4 to 4.19 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -4.74 to 3.61 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.186 | 0.199 | +7.2% | -0.0433 to 0.07 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.37 | 0.376 | +1.5% | -0.0143 to 0.0256 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0716 | 0.072 | +0.6% | -0.0061 to 0.00694 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 419 | -0.4% | -7.46 to 3.71 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 715,724 | 716,371 | +0.1% | -117,519 to 118,813 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.0767 | -29.7% | -0.124 to 0.0596 | STEADY, no difference beyond the noise |
| host CPU-seconds | 202 | 136 | -32.6% | -253 to 122 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.151 | 0.102 | -32.5% | -0.189 to 0.0909 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 66.3 | 67.4 | +1.7% | -6.02 to 8.29 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 64.5 | 65.1 | +0.9% | -6.32 to 7.52 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.78 | 2.32 | +30.1% | 0.301 to 0.771 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 202 | 136 | -32.6% | -253 to 122 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,883 | -0.0% | -1.03 to 0.846 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | +0.0% | -1.22 to 1.72 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.416 | 0.423 | +1.7% | -0.0182 to 0.0322 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.573 | +0.9% | -0.0171 to 0.0271 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.213 | +1.6% | -0.000884 to 0.00745 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 404 | 403 | -0.3% | -27.1 to 25 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 274,066 | 277,616 | +1.3% | -47,765 to 54,866 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.212 | +3.5% | -0.19 to 0.205 | STEADY, no difference beyond the noise |
| host CPU-seconds | 146 | 154 | +5.3% | -174 to 190 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.274 | 0.289 | +5.3% | -0.327 to 0.356 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 79.1 | 81.3 | +2.7% | -1.88 to 6.17 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 78.1 | 80.1 | +2.5% | -2.08 to 5.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.977 | 1.19 | +21.8% | 0.173 to 0.253 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 146 | 154 | +5.3% | -174 to 190 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,914 | +0.0% | -2.55 to 4.81 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,917 | +0.0% | -1.29 to 1.86 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.187 | 0.187 | +0.4% | -0.0045 to 0.00584 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.347 | 0.34 | -1.8% | -0.0191 to 0.00642 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.135 | 0.133 | -1.3% | -0.00573 to 0.00232 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 422 | 422 | +0.1% | -8.48 to 8.96 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 717,259 | 757,984 | +5.7% | -121,451 to 202,900 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.13 | -15.9% | -0.0946 to 0.0455 | STEADY, no difference beyond the noise |
| host CPU-seconds | 279 | 229 | -18.1% | -192 to 91.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.209 | 0.171 | -18.1% | -0.144 to 0.0682 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 138 | 139 | +1.0% | -3.78 to 6.43 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 136 | 137 | +0.6% | -4.32 to 5.96 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.96 | 2.47 | +25.7% | 0.473 to 0.536 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 279 | 229 | -18.1% | -192 to 91.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,841 | 5,838 | -0.0% | -17.1 to 12.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,850 | 5,847 | -0.0% | -17.9 to 12.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.162 | 0.163 | +0.8% | -0.0123 to 0.015 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.375 | 0.373 | -0.4% | -0.0241 to 0.0207 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0848 | 0.085 | +0.2% | -0.00388 to 0.00419 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 699 | +36.6% | -295 to 669 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 562 | +34.2% | -224 to 511 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 690,223 | 536,122 | -22.3% | -568,007 to 259,805 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.13 | -2.0% | -0.0287 to 0.0235 | STEADY, no difference beyond the noise |
| host CPU-seconds | 240 | 235 | -2.5% | -59.7 to 47.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0898 | 0.0876 | -2.5% | -0.0224 to 0.018 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 122 | 124 | +1.1% | -6.59 to 9.32 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 120 | 121 | +0.6% | -6.97 to 8.49 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.62 | 3.22 | +23.1% | 0.38 to 0.829 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 240 | 235 | -2.5% | -59.7 to 47.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,873 | -0.0% | -8.39 to 7.47 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -9.2 to 7.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.375 | 0.365 | -2.7% | -0.0312 to 0.0112 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.661 | 0.654 | -1.0% | -0.0592 to 0.0458 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.22 | -2.2% | -0.0133 to 0.0033 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,274 | +148.8% | 273 to 1,251 | power given |
| bytes in the cache, mean (MB) | 417 | 1,003 | +140.2% | 211 to 959 | power given |
| pages read into the cache (misses) | 678,110 | 325,806 | -52.0% | -509,336 to -195,271 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.255 | -4.8% | -0.0539 to 0.028 | STEADY, no difference beyond the noise |
| host CPU-seconds | 478 | 449 | -6.1% | -129 to 70.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.361 | 0.339 | -6.1% | -0.0966 to 0.0524 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | -1.5 to 12.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 270 | -2.5% | -20.4 to 6.59 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 275 | 267 | -2.8% | -21.1 to 5.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.29 | +26.4% | 0.617 to 0.758 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 478 | 449 | -6.1% | -129 to 70.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
