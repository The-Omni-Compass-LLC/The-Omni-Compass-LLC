# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,284 | +1.4% | 0.908 to 33.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0223 to 0.0136 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.000907 to 0.0224 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0239 to 0.0162 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.83 | 5.83 | +0.0% | -0.0155 to 0.0177 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1 | -5.7% | -0.121 to -0.000324 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.8% | -0.434 to 2.75 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.1 | +1.4% | -0.231 to 1.89 | EVEN, no difference beyond the noise |
| keys evicted | 103,389 | 95,749 | -7.4% | -14,840 to -440 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.115 | -4.8% | -0.0114 to -0.000208 | GAIN |
| host CPU-seconds | 201 | 190 | -5.4% | -20.2 to -1.43 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.353 | 0.329 | -6.6% | -0.0429 to -0.00394 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 9.94 to 27.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
