# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -3.28 to -0.637 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0481 to 0.0156 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.616 | -0.2% | -0.00196 to -0.00055 | LOSS |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0192 to 0.0175 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.2% | -0.0158 to 0.0371 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.27 | +0.3% | -0.0115 to 0.0263 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.536 to 1.2 | power given |
| memory used, mean (MB) | 60.7 | 60.8 | +0.2% | 0.107 to 0.123 | power given |
| keys evicted | 243,039 | 243,940 | +0.4% | 417 to 1,384 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.15 | +4.6% | -0.0179 to 0.0312 | EVEN, no difference beyond the noise |
| host CPU-seconds | 240 | 253 | +5.4% | -34.2 to 60.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.576 | 0.608 | +5.6% | -0.0815 to 0.146 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 19.5 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
