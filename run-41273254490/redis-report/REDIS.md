# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.889 to 0.15 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00297 to 0.00867 | STEADY, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | -4.08e-06 to 6.55e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.71 | 5.72 | +0.2% | -0.00174 to 0.0195 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.79 | +0.2% | -0.0115 to 0.037 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.804 | 0.81 | +0.7% | -0.00595 to 0.018 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.0209 to 0.0674 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.108 | +4.2% | -0.0517 to 0.0604 | STEADY, no difference beyond the noise |
| host CPU-seconds | 69.2 | 72 | +4.1% | -39.2 to 44.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.29 | 0.302 | +4.1% | -0.164 to 0.188 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 102 | 104 | +2.0% | -0.209 to 4.31 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.8 | 13.1 | +1.8% | -0.293 to 0.753 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 89.5 | 91.3 | +2.0% | 0.0689 to 3.56 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0899 | 0.0927 | +3.1% | -0.0021 to 0.00763 | shown, not judged |
| host CPU-seconds without steal | 69.2 | 72 | +4.1% | -39.2 to 44.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,469 | 1,470 | +0.0% | -1.11 to 1.66 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0113 to 0.0182 | STEADY, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.38e-06 to 5.43e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.11 | 0.113 | +3.2% | -0.00519 to 0.0122 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.21 | 5.22 | +0.1% | -0.00882 to 0.0206 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.184 | 0.185 | +0.5% | -0.00267 to 0.00458 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.024 to 0.0698 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0506 | 0.0509 | +0.5% | -0.0578 to 0.0583 | STEADY, no difference beyond the noise |
| host CPU-seconds | 88.8 | 89.4 | +0.7% | -107 to 108 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.134 | 0.135 | +0.7% | -0.162 to 0.164 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 110 | 113 | +2.3% | 0.793 to 4.31 | power given |
| the server's own CPU-seconds (redis-server) | 14.8 | 15.4 | +3.5% | 0.0238 to 1.02 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 95.2 | 97.2 | +2.1% | 0.728 to 3.33 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.127 | +3.0% | -0.00704 to 0.0143 | shown, not judged |
| host CPU-seconds without steal | 88.8 | 89.4 | +0.7% | -107 to 108 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | +0.0% | -0.832 to 1.08 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.131 to 0.198 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | -0.0% | -1.96e-05 to 1.22e-05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.1% | -0.0125 to 0.0218 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.24 | +0.1% | -0.0225 to 0.0367 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.2 | +0.0% | -0.0144 to 0.0147 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00381 to 0.0552 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0584 | 0.0568 | -2.7% | -0.0287 to 0.0256 | STEADY, no difference beyond the noise |
| host CPU-seconds | 103 | 100 | -3.0% | -54.9 to 48.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.196 | 0.19 | -3.0% | -0.104 to 0.0922 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 112 | 113 | +1.2% | -7.71 to 10.4 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 14.4 | 14.6 | +1.3% | -1.1 to 1.49 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 97.2 | 98.3 | +1.2% | -6.61 to 8.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.118 | 0.122 | +3.0% | -0.0198 to 0.0268 | shown, not judged |
| host CPU-seconds without steal | 103 | 100 | -3.0% | -54.9 to 48.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.0457 to 0.0506 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00117 to 8.81e-05 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.47 | 5.49 | +0.4% | -0.0321 to 0.074 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.68 | +0.1% | -0.0123 to 0.0266 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.507 | 0.51 | +0.7% | -0.00465 to 0.0114 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0138 to 0.0582 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0945 | 0.0999 | +5.7% | -0.0498 to 0.0605 | STEADY, no difference beyond the noise |
| host CPU-seconds | 169 | 178 | +5.4% | -96.6 to 115 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.269 | 0.284 | +5.4% | -0.154 to 0.183 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 170 | 174 | +2.2% | -3.1 to 10.7 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 20 | 20.2 | +0.7% | -0.732 to 1.02 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 150 | 154 | +2.5% | -3.04 to 10.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.197 | 0.199 | +0.6% | -0.00424 to 0.00647 | shown, not judged |
| host CPU-seconds without steal | 169 | 178 | +5.4% | -96.6 to 115 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
