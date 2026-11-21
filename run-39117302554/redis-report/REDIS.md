# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.545 to 0.695 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00441 to 0.00215 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | -4.08e-06 to 6.55e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.47 | 5.47 | -0.1% | -0.0317 to 0.0255 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.0% | -0.0127 to 0.0122 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.731 | 0.731 | -0.1% | -0.0134 to 0.0119 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0277 to 0.0773 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0995 | 0.0768 | -22.8% | -0.125 to 0.0798 | EVEN, no difference beyond the noise |
| host CPU-seconds | 70.7 | 53.3 | -24.7% | -95.6 to 60.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.296 | 0.223 | -24.7% | -0.4 to 0.254 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,472 | +0.0% | -0.497 to 0.643 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0278 to 0.0177 | EVEN, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | -0.0% | -3.23e-06 to 1.18e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.228 | 0.225 | -1.1% | -0.0122 to 0.00702 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | -0.0% | -0.0204 to 0.0147 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.287 | 0.285 | -0.6% | -0.00589 to 0.00257 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.0193 to 0.044 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0931 | 0.0916 | -1.7% | -0.0199 to 0.0168 | EVEN, no difference beyond the noise |
| host CPU-seconds | 157 | 154 | -1.8% | -37.8 to 32.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.237 | 0.233 | -1.8% | -0.057 to 0.0485 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.0492 to 0.0102 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0164 to 0.0196 | EVEN, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | -6.37e-06 to 6.37e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.0% | -0.0217 to 0.0187 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.02 to 0.0146 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | +0.0% | -0.00785 to 0.00831 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00327 to 0.0576 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.104 | -13.0% | -0.0262 to -0.00478 | GAIN |
| host CPU-seconds | 201 | 172 | -14.6% | -51.5 to -7.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.381 | 0.325 | -14.6% | -0.0975 to -0.014 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -0.581 to 0.733 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00631 to 0.00499 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | 1.48e-06 to 1.48e-06 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.1% | -0.0188 to 0.00914 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0178 to 0.013 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.568 | 0.567 | -0.2% | -0.00448 to 0.00215 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.011 to 0.0657 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0973 | 0.0942 | -3.2% | -0.0348 to 0.0287 | EVEN, no difference beyond the noise |
| host CPU-seconds | 164 | 158 | -3.7% | -64.8 to 52.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.261 | 0.252 | -3.7% | -0.103 to 0.0841 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
