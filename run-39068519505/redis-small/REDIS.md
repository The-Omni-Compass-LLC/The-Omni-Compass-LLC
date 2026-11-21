# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 10.1 to 13.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0133 to -0.00463 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.0066 to 0.00879 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | -0.0% | -0.00858 to 0.00614 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.59 | +0.0% | -0.00421 to 0.00862 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.11 | -1.9% | -0.0519 to -0.0304 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 0.899 to 2.58 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 0.999 to 1.47 | power given |
| keys evicted | 243,164 | 235,612 | -3.1% | -10,361 to -4,741 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.108 | +1.7% | -0.0514 to 0.055 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 189 | +2.3% | -101 to 109 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.444 | 0.448 | +1.0% | -0.245 to 0.253 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 11.5 to 17.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
