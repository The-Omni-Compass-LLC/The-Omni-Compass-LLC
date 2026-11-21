# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 10.7 to 17.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0253 to 0.0658 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00749 to 0.0107 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% | -0.0109 to 0.00125 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.1% | -0.0555 to 0.0473 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -4.6% | -0.0732 to -0.0336 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.22 to 2.12 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 1.02 to 1.42 | power given |
| keys evicted | 138,226 | 132,920 | -3.8% | -6,401 to -4,211 | shown, not judged |
| host CPU busy (share of the run) | 0.0688 | 0.0596 | -13.3% | -0.0843 to 0.066 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 106 | -13.9% | -159 to 125 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.231 | 0.197 | -14.9% | -0.301 to 0.232 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
