# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,318 | +4.1% | 8.11 to 95 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000215 to 0.00102 | EVEN, the same |
| cache hit rate | 0.844 | 0.879 | +4.1% | 0.00558 to 0.0634 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.2% | -0.0318 to 0.00372 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.0% | -0.0359 to 0.0318 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.868 | -17.9% | -0.342 to -0.0368 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.9 | +6.2% | -2.4 to 10.3 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 64.1 | +4.6% | -2.99 to 8.63 | EVEN, no difference beyond the noise |
| keys evicted | 103,656 | 80,984 | -21.9% | -41,999 to -3,345 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.118 | -3.3% | -0.0225 to 0.0145 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 199 | -2.9% | -42.1 to 30.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.36 | 0.336 | -6.6% | -0.0935 to 0.0456 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33.7 |  | 21.9 to 45.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
