# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,901 | -0.1% | -4.61 to 0.776 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,908 | -0.0% | -3.51 to 2.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.333 | 0.339 | +2.0% | -0.0258 to 0.0391 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.546 | 0.566 | +3.7% | -0.0671 to 0.107 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.138 | 0.14 | +1.3% | -0.0057 to 0.00936 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -122 to 196 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 447 | +6.6% | -94.4 to 150 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 704,357 | 641,076 | -9.0% | -221,819 to 95,258 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.167 | +9.0% | -0.0247 to 0.0523 | STEADY, no difference beyond the noise |
| host CPU-seconds | 274 | 304 | +10.9% | -52.2 to 112 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.206 | 0.228 | +10.9% | -0.0393 to 0.0843 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 126 | 128 | +1.2% | -3.84 to 6.96 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 124 | 125 | +0.7% | -4.53 to 6.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.22 | +28.7% | 0.624 to 0.808 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 274 | 304 | +10.9% | -52.2 to 112 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -21.8 to 17.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,907 | -0.1% | -12.9 to 9.83 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.327 | +1.6% | -0.0398 to 0.0498 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.54 | 0.551 | +2.0% | -0.065 to 0.087 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.174 | 0.179 | +2.9% | 0.000571 to 0.00957 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 715 | +39.6% | 70.5 to 335 | power given |
| bytes in the cache, mean (MB) | 404 | 557 | +38.0% | 59.1 to 248 | power given |
| pages read into the cache (misses) | 277,488 | 227,924 | -17.9% | -87,240 to -11,889 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.151 | -17.0% | -0.114 to 0.0518 | STEADY, no difference beyond the noise |
| host CPU-seconds | 133 | 107 | -19.7% | -97.7 to 45.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.201 | -19.7% | -0.183 to 0.0845 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 65.1 | 64.9 | -0.3% | -3.8 to 3.45 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 64.2 | 63.8 | -0.6% | -4.07 to 3.25 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.894 | 1.12 | +25.7% | 0.194 to 0.267 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 133 | 107 | -19.7% | -97.7 to 45.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,943 | -0.0% | -1.45 to 1.42 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,944 | 2,944 | -0.0% | -1.55 to 1.52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0783 | 0.0797 | +1.7% | -0.00492 to 0.00759 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.257 | 0.261 | +1.3% | -0.0181 to 0.0248 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0515 | 0.0519 | +0.7% | -0.00162 to 0.00236 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 420 | +0.4% | -2.36 to 5.72 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 684,625 | 742,997 | +8.5% | -107,662 to 224,405 | shown, not judged |
| host CPU busy (share of the run) | 0.0736 | 0.0665 | -9.6% | -0.048 to 0.0339 | STEADY, no difference beyond the noise |
| host CPU-seconds | 134 | 120 | -10.3% | -93.3 to 65.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0998 | 0.0896 | -10.3% | -0.0696 to 0.049 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 43.7 | 44.7 | +2.1% | -1.39 to 3.24 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 42.1 | 42.7 | +1.4% | -1.71 to 2.91 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.58 | 1.91 | +20.5% | 0.271 to 0.379 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 134 | 120 | -10.3% | -93.3 to 65.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,834 | 5,832 | -0.0% | -13.5 to 8.72 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,842 | 5,840 | -0.0% | -10.8 to 6.39 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.157 | 0.157 | +0.4% | -0.00692 to 0.00826 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.341 | 0.338 | -1.0% | -0.0268 to 0.0201 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.082 | 0.0824 | +0.5% | -0.0068 to 0.00768 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 717 | +40.0% | -272 to 682 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 575 | +37.3% | -211 to 523 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 694,218 | 510,732 | -26.4% | -628,183 to 261,210 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.128 | +2.7% | -0.0356 to 0.0423 | STEADY, no difference beyond the noise |
| host CPU-seconds | 226 | 233 | +3.1% | -78 to 92.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0845 | 0.0872 | +3.1% | -0.029 to 0.0343 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | -2.13 to 5.46 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 120 | 121 | +0.6% | -6.09 to 7.59 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 117 | 117 | +0.2% | -6.22 to 6.58 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.26 | 3.83 | +17.4% | 0.0535 to 1.08 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 226 | 233 | +3.1% | -77.9 to 92.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,899 | +0.0% | -2.47 to 3.33 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,909 | +0.0% | -2.82 to 3.77 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.324 | -4.8% | -0.0201 to -0.0125 | GAIN |
| latency, 99th percentile (ms) | 0.589 | 0.583 | -1.1% | -0.0246 to 0.012 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.157 | 0.149 | -5.0% | -0.00958 to -0.00624 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,613 | +215.1% | 1,083 to 1,119 | power given |
| bytes in the cache, mean (MB) | 417 | 1,244 | +198.5% | 814 to 841 | power given |
| pages read into the cache (misses) | 683,696 | 115,297 | -83.1% | -598,271 to -538,528 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.183 | -6.6% | -0.0404 to 0.0144 | STEADY, no difference beyond the noise |
| host CPU-seconds | 356 | 329 | -7.5% | -88 to 34.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.268 | 0.248 | -7.5% | -0.0663 to 0.026 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 16 |  | 11 to 21 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 177 | -5.8% | -13.9 to -7.93 | GAIN |
| the server's own CPU-seconds (mongod) | 185 | 174 | -6.2% | -14.7 to -8.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.38 | 3.02 | +26.8% | 0.476 to 0.803 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 356 | 329 | -7.5% | -88 to 34.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
