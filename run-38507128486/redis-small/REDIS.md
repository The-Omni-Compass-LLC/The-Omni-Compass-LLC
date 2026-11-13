# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 926 | +0.0% | -6.67 to 6.98 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00826 to -0.00188 | LOSS |
| cache hit rate | 0.617 | 0.618 | +0.0% | -0.00458 to 0.00471 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.51 | 5.51 | +0.1% | -0.00578 to 0.012 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.57 | +0.1% | -0.000429 to 0.00838 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.13 | 2.14 | +0.1% | -0.0302 to 0.0347 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 71.5 | +11.7% | 5.48 to 9.55 | power given |
| memory used, mean (MB) | 60.7 | 65.1 | +7.2% | 3.86 to 4.9 | power given |
| keys evicted | 243,086 | 246,275 | +1.3% | 4.01 to 6,374 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.104 | -4.5% | -0.0295 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 182 | -5.2% | -57.2 to 37.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.436 | -5.2% | -0.141 to 0.0932 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 21.4 to 34.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
