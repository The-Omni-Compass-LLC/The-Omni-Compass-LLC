# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.171 to 0.822 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00764 to 0.00649 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% | -6.55e-06 to 4.08e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.48 | 5.48 | -0.1% | -0.0408 to 0.0283 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.1% | -0.0143 to 0.00655 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.735 | 0.731 | -0.4% | -0.0146 to 0.00811 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0341 to 0.0634 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0955 | 0.0967 | +1.2% | -0.0736 to 0.0759 | STEADY, no difference beyond the noise |
| host CPU-seconds | 67.7 | 68 | +0.6% | -57.9 to 58.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.283 | 0.285 | +0.5% | -0.243 to 0.246 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 72 | 71.5 | -0.6% | -2.99 to 2.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 8.82 | 8.76 | -0.6% | -0.458 to 0.351 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 63.1 | 62.7 | -0.6% | -2.62 to 1.83 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0656 | 0.0648 | -1.1% | -0.00279 to 0.00134 | shown, not judged |
| host CPU-seconds without steal | 67.7 | 68 | +0.6% | -57.9 to 58.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,471 | -0.0% | -0.763 to 0.411 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00169 to 0.00195 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.202 | 0.203 | +0.0% | -0.00859 to 0.00868 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.00493 to 0.00286 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.263 | 0.263 | +0.1% | -0.00332 to 0.00402 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00561 to 0.0335 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.117 | +8.0% | -0.0016 to 0.0188 | STEADY, no difference beyond the noise |
| host CPU-seconds | 188 | 204 | +9.0% | -3.01 to 36.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.283 | 0.309 | +9.0% | -0.0046 to 0.0556 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 215 | 216 | +0.2% | -1.6 to 2.65 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 28.4 | 28.4 | -0.1% | -0.598 to 0.551 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 186 | 187 | +0.3% | -1.52 to 2.62 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.215 | 0.213 | -0.5% | -0.00435 to 0.00214 | shown, not judged |
| host CPU-seconds without steal | 188 | 204 | +9.0% | -3.01 to 36.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.0334 to 0.02 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0215 to 0.00847 | STEADY, no difference beyond the noise |
| cache hit rate | 0.782 | 0.783 | +0.0% | -6.59e-06 to 1.23e-05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.000118 to 0.00239 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00757 to 0.00926 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | +0.0% | -0.00232 to 0.00339 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0137 to 0.0444 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.143 | +5.9% | -0.0447 to 0.0607 | STEADY, no difference beyond the noise |
| host CPU-seconds | 229 | 245 | +6.8% | -88.1 to 119 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.434 | 0.464 | +6.8% | -0.167 to 0.226 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 277 | 278 | +0.4% | -8.1 to 10 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32.6 | 32.6 | -0.1% | -1.1 to 1.04 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 244 | 245 | +0.4% | -9.13 to 11.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.232 | 0.232 | +0.1% | -0.00661 to 0.00707 | shown, not judged |
| host CPU-seconds without steal | 229 | 245 | +6.8% | -88.1 to 119 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -0.237 to 0.273 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0173 to 0.0197 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -1.32e-05 to 8.38e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.0% | -0.0146 to 0.0129 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0146 to 0.0118 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.564 | 0.562 | -0.3% | -0.00697 to 0.0039 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.00258 to 0.053 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.104 | -5.8% | -0.0468 to 0.0339 | STEADY, no difference beyond the noise |
| host CPU-seconds | 188 | 176 | -6.7% | -89.4 to 64.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.3 | 0.28 | -6.7% | -0.143 to 0.102 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 246 | 246 | -0.1% | -5.59 to 5.06 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 30.9 | 30.2 | -2.4% | -2.27 to 0.798 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 215 | 215 | +0.2% | -3.31 to 4.26 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.224 | 0.223 | -0.7% | -0.00842 to 0.00551 | shown, not judged |
| host CPU-seconds without steal | 188 | 176 | -6.7% | -89.4 to 64.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
