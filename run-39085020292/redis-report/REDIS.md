# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.112 to 0.121 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0109 to 0.00909 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% | -6.55e-06 to 4.08e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.0109 to 0.0165 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.0141 to 0.0201 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.813 | 0.816 | +0.3% | -0.0104 to 0.016 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.0172 to 0.0627 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0947 | 0.115 | +21.1% | -0.0833 to 0.123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63.1 | 78.1 | +23.9% | -62.6 to 92.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.264 | 0.327 | +23.9% | -0.262 to 0.388 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,471 | +0.0% | -0.612 to 0.742 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00131 to 0.000836 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -1.14e-06 to 3.11e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.156 | 0.155 | -1.1% | -0.00709 to 0.00369 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.45 | 5.45 | -0.0% | -0.0196 to 0.0164 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.226 | -0.4% | -0.00531 to 0.00364 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.0076 to 0.0426 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0941 | 0.0827 | -12.2% | -0.0785 to 0.0556 | EVEN, no difference beyond the noise |
| host CPU-seconds | 167 | 145 | -12.9% | -151 to 108 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.22 | -12.9% | -0.228 to 0.163 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,172 | -0.0% | -1.47 to 0.465 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00775 to -0.00263 | LOSS |
| cache hit rate | 0.783 | 0.783 | +0.0% | -1.14e-06 to 3.11e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.0% | -0.00899 to 0.00404 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | +0.2% | -0.0862 to 0.104 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.2 | +0.1% | -0.0172 to 0.0192 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00559 to 0.0567 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0545 | 0.043 | -21.1% | -0.0244 to 0.00149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 95.8 | 74.7 | -22.0% | -45 to 2.81 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.181 | 0.142 | -22.0% | -0.0851 to 0.00529 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -1.16 to 1.51 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0111 to 0.0061 | EVEN, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.19 | 5.2 | +0.1% | -0.0101 to 0.0192 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.23 | +0.2% | -0.0111 to 0.0327 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.443 | 0.444 | +0.1% | -0.00883 to 0.00992 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0614 to 0.102 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.061 | 0.0409 | -32.9% | -0.0765 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 71.5 | -34.4% | -142 to 66.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.174 | 0.114 | -34.4% | -0.226 to 0.106 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
