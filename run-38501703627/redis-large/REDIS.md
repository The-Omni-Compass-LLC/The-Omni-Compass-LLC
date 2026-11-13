# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,307 | +3.2% | 31.4 to 48.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -6.77e-05 to 0.00152 | EVEN, the same |
| cache hit rate | 0.845 | 0.872 | +3.2% | 0.0209 to 0.0324 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.72 | -0.2% | -0.019 to 0.0014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.0% | -0.00821 to 0.00893 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.9 | -13.9% | -0.18 to -0.111 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.2 | +5.1% | 0.277 to 6.21 | power given |
| memory used, mean (MB) | 61.3 | 63.1 | +2.9% | -0.399 to 3.92 | EVEN, no difference beyond the noise |
| keys evicted | 103,401 | 85,872 | -17.0% | -21,107 to -13,951 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.107 | -8.0% | -0.0191 to 0.000596 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 178 | -8.6% | -34.6 to 1.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.302 | -11.3% | -0.072 to -0.00523 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 31 |  | 31 to 31 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
