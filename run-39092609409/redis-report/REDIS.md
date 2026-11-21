# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,325 | 1,325 | -0.0% | -3.25 to 2.92 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0512 to 0.0864 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | -7.24e-06 to 8.09e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.2 | 5.21 | +0.0% | -0.00185 to 0.00346 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.0% | -0.0112 to 0.0129 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.674 | 0.675 | +0.2% | -0.0247 to 0.0268 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0268 to 0.118 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0476 | 0.0383 | -19.5% | -0.0451 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 33.4 | 26.6 | -20.6% | -33.3 to 19.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.14 | 0.111 | -20.5% | -0.139 to 0.0817 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.16 to 0.0775 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00251 to -0.00171 | LOSS |
| cache hit rate | 0.981 | 0.981 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 0.227 | 0.224 | -1.3% | -0.0176 to 0.0115 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.71 | -0.1% | -0.014 to 0.008 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.287 | 0.285 | -0.6% | -0.0075 to 0.00413 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00688 to 0.0465 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0925 | 0.0828 | -10.5% | -0.0967 to 0.0773 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 138 | -11.8% | -181 to 144 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.236 | 0.208 | -11.8% | -0.273 to 0.217 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.0697 to 0.0779 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0078 to 0.00498 | EVEN, the same |
| cache hit rate | 0.783 | 0.783 | +0.0% | -1.14e-06 to 3.11e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.56 | 5.55 | -0.2% | -0.0472 to 0.0301 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.64 | +0.0% | -0.0292 to 0.0335 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.29 | -0.2% | -0.0237 to 0.0174 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00414 to 0.0584 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0918 | -10.2% | -0.0217 to 0.000816 | EVEN, no difference beyond the noise |
| host CPU-seconds | 180 | 160 | -11.1% | -41.2 to 1.44 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.303 | -11.1% | -0.0781 to 0.00277 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | -0.0% | -0.275 to 0.195 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.000207 to 0.00138 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -2.62e-06 to 1.63e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.0141 to 0.0148 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.7 | +0.0% | -0.0104 to 0.0122 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.542 | 0.543 | +0.3% | -0.00357 to 0.00652 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.00366 to 0.0646 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.109 | -3.1% | -0.0375 to 0.0305 | EVEN, no difference beyond the noise |
| host CPU-seconds | 196 | 189 | -3.5% | -72.9 to 59.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.301 | -3.5% | -0.116 to 0.0948 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
