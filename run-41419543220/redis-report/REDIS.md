# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,328 | +0.0% | 0.00816 to 0.051 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0062 to 0.00608 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 95th percentile (ms) | 5.29 | 5.3 | +0.1% | -0.0382 to 0.0436 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.1% | -0.0171 to 0.0228 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.708 | 0.709 | +0.1% | -0.00883 to 0.0102 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00172 to 0.0355 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0623 | 0.07 | +12.3% | -0.0702 to 0.0855 | STEADY, no difference beyond the noise |
| host CPU-seconds | 43.7 | 49.1 | +12.5% | -52 to 62.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.183 | 0.206 | +12.5% | -0.218 to 0.263 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 59.2 | 59.1 | -0.2% | -3.27 to 3.03 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 7.53 | 7.51 | -0.4% | -0.241 to 0.188 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 51.6 | 51.5 | -0.2% | -3.38 to 3.19 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0667 | 0.0668 | +0.2% | -0.00492 to 0.00514 | shown, not judged |
| host CPU-seconds without steal | 43.7 | 49.1 | +12.5% | -52 to 62.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.664 to 0.425 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000446 to 0.00131 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -1.14e-06 to 3.11e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.169 | 0.166 | -1.9% | -0.0258 to 0.0195 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.49 | 5.48 | -0.3% | -0.0971 to 0.0681 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.231 | 0.23 | -0.2% | -0.0111 to 0.0103 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00452 to 0.0406 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0842 | 0.0738 | -12.4% | -0.0349 to 0.0141 | STEADY, no difference beyond the noise |
| host CPU-seconds | 147 | 127 | -13.3% | -66.1 to 26.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.222 | 0.192 | -13.3% | -0.0998 to 0.0405 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 173 | 172 | -0.4% | -8.81 to 7.44 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 23.7 | 23.5 | -1.1% | -2.35 to 1.83 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 149 | 148 | -0.3% | -6.51 to 5.66 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.175 | 0.174 | -0.5% | -0.0089 to 0.00717 | shown, not judged |
| host CPU-seconds without steal | 147 | 127 | -13.3% | -66.1 to 26.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | -0.0% | -0.894 to 0.666 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0931 to 0.0564 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | 1.48e-06 to 1.48e-06 | GAIN |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.00656 to 0.00995 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.26 | +0.3% | -0.0499 to 0.0796 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.21 | +0.2% | 0.000794 to 0.00394 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00223 to 0.0677 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0541 | 0.0545 | +0.9% | -0.0134 to 0.0144 | STEADY, no difference beyond the noise |
| host CPU-seconds | 94.7 | 95.7 | +1.1% | -24.7 to 26.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.18 | 0.181 | +1.1% | -0.0468 to 0.0507 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 118 | 118 | +0.3% | -2.88 to 3.65 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 14.8 | 14.7 | -0.4% | -1.02 to 0.898 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 103 | +0.4% | -2.15 to 3.04 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.122 | -1.2% | -0.0173 to 0.0143 | shown, not judged |
| host CPU-seconds without steal | 94.7 | 95.7 | +1.1% | -24.7 to 26.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.0538 to 0.0582 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00425 to 0.00101 | STEADY, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.62 | 5.63 | +0.3% | -0.0124 to 0.0435 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.00842 to 0.0285 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.543 | 0.549 | +1.0% | -0.004 to 0.015 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.000545 to 0.0562 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.134 | +7.0% | -0.00271 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 221 | 237 | +7.3% | -6.88 to 39.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.353 | 0.379 | +7.3% | -0.011 to 0.0628 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 220 | 228 | +4.0% | 3.66 to 13.7 | power given |
| the server's own CPU-seconds (redis-server) | 24.9 | 25.5 | +2.7% | -0.0256 to 1.37 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 195 | 203 | +4.1% | 3.68 to 12.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.225 | 0.229 | +2.2% | -0.00325 to 0.013 | shown, not judged |
| host CPU-seconds without steal | 221 | 237 | +7.3% | -6.88 to 39.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
