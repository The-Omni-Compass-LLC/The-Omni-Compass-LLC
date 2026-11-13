# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,349 | +6.5% | 35.9 to 129 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00112 to 0.00175 | EVEN, the same |
| cache hit rate | 0.845 | 0.9 | +6.5% | 0.0242 to 0.0856 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.45 | -1.0% | -0.111 to -0.000583 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0512 to 0.00986 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.96 | 0.666 | -30.6% | -0.464 to -0.123 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 75.2 | +17.4% | 0.957 to 21.4 | power given |
| memory used, mean (MB) | 61.3 | 69.1 | +12.7% | 2.05 to 13.5 | power given |
| keys evicted | 103,336 | 66,796 | -35.4% | -57,182 to -15,897 | shown, not judged |
| host CPU busy (share of the run) | 0.0985 | 0.0962 | -2.4% | -0.0203 to 0.0156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 173 | 169 | -2.1% | -37.7 to 30.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.303 | 0.278 | -8.1% | -0.0899 to 0.0411 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 37.7 |  | 8.87 to 66.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
