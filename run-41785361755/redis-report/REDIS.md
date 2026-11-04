# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -2.54 to 2.43 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0892 to 0.0571 | STEADY, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | -0.0% | -6.67e-06 to 4.4e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.0102 to 0.0069 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.1% | -0.01 to 0.00427 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.793 | 0.791 | -0.3% | -0.0231 to 0.019 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0464 to 0.102 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.121 | -6.1% | -0.0491 to 0.0333 | STEADY, no difference beyond the noise |
| host CPU-seconds | 90.1 | 83.9 | -6.8% | -38.5 to 26.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.377 | 0.351 | -6.8% | -0.161 to 0.109 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 94.6 | 94.6 | +0.0% | -1.33 to 1.39 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 11.7 | 11.4 | -2.3% | -0.76 to 0.227 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 82.8 | 83.1 | +0.4% | -1.02 to 1.61 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.088 | 0.0874 | -0.7% | -0.00807 to 0.00687 | shown, not judged |
| host CPU-seconds without steal | 90.1 | 83.9 | -6.8% | -38.5 to 26.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.0268 to 0.021 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00482 to 0.00335 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -1.14e-06 to 3.11e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.23 | 0.232 | +0.8% | -0.00391 to 0.00765 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.73 | +0.1% | -0.00856 to 0.0211 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.284 | 0.285 | +0.3% | -0.00199 to 0.00353 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.00474 to 0.0483 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.107 | -13.0% | -0.0431 to 0.0111 | STEADY, no difference beyond the noise |
| host CPU-seconds | 212 | 180 | -14.8% | -83.4 to 20.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.32 | 0.272 | -14.8% | -0.126 to 0.0313 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 242 | 244 | +1.0% | 1.68 to 3.03 | power given |
| the server's own CPU-seconds (redis-server) | 32.8 | 32.7 | -0.1% | -0.487 to 0.454 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 209 | 211 | +1.1% | 1.29 to 3.44 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.25 | 0.254 | +1.7% | 0.00104 to 0.0073 | shown, not judged |
| host CPU-seconds without steal | 212 | 180 | -14.8% | -83.4 to 20.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,173 | +0.0% | -0.0733 to 0.247 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0118 to 0.0234 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | -0.0% | -2.62e-06 to 1.63e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.19 | 5.19 | -0.0% | -0.00398 to 0.000157 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0131 to 0.000932 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.19 | 1.18 | -0.1% | -0.00607 to 0.00329 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00541 to 0.0362 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.064 | 0.0397 | -37.9% | -0.0432 to -0.00535 | GAIN |
| host CPU-seconds | 114 | 69 | -39.5% | -80.8 to -9.29 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.216 | 0.131 | -39.5% | -0.153 to -0.0177 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 108 | 107 | -0.7% | -3.4 to 1.91 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 13.5 | 13.2 | -1.8% | -0.695 to 0.208 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 94.5 | 94 | -0.5% | -2.82 to 1.81 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.104 | 0.103 | -0.2% | -0.00316 to 0.00272 | shown, not judged |
| host CPU-seconds without steal | 114 | 69 | -39.5% | -80.8 to -9.29 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,390 | 1,390 | +0.0% | -3.02 to 3.71 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.219 to 0.141 | STEADY, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | -0.0% | -4.99e-06 to 2.1e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.24 | 5.2 | -0.8% | -0.139 to 0.0522 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.36 | -5.0% | -1.01 to 0.444 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.494 | 0.462 | -6.3% | -0.125 to 0.0623 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | -0.0% | -0.186 to 0.129 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0729 | 0.0538 | -26.1% | -0.0293 to -0.0088 | GAIN |
| host CPU-seconds | 128 | 95.1 | -25.8% | -47.9 to -18.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.205 | 0.152 | -25.9% | -0.0771 to -0.029 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 143 | 116 | -18.8% | -93.2 to 39.2 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 18.1 | 14.7 | -18.5% | -10.1 to 3.47 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 125 | 101 | -18.9% | -83 to 35.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.14 | 0.121 | -13.6% | -0.0666 to 0.0284 | shown, not judged |
| host CPU-seconds without steal | 128 | 95.1 | -25.8% | -47.9 to -18.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
