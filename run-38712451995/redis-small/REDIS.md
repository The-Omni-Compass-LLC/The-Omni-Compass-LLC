# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -3.15 to 0.000696 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0177 to 0.00917 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00205 to 7.52e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.0% | -0.0145 to 0.0177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% | -0.00265 to 0.0254 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.28 | +0.4% | -0.00647 to 0.0234 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | -1.14 to 3.78 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.7 | -0.1% | -0.57 to 0.506 | EVEN, no difference beyond the noise |
| keys evicted | 243,138 | 244,398 | +0.5% | -336 to 2,857 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.152 | +9.3% | -0.0178 to 0.0437 | EVEN, no difference beyond the noise |
| host CPU-seconds | 232 | 257 | +10.9% | -35.2 to 85.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.557 | 0.618 | +11.1% | -0.0838 to 0.207 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 13.9 to 31.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
