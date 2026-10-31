# CPU power: Omni-Compass on top of the Linux kernel's own frequency governor

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The machine as it runs is native: the kernel's frequency governor as shipped under the operator's ceiling (the top clock). Omni is the compass law on the ceiling through the kernel's own interface inside [half the top, the top], holding the service's own request latency at 40% of the 20 ms line, a notch given back only after a paired trial on the machine itself allowed it under the declared objective. The same requests in both arms. Energy is the processor's own meter (RAPL); the whole machine at the wall where a plug is fitted. Every row is reported, losses included.

## tuning: steps 3 3 3 3 3 3 × 10.0 s (the tuning workload)

Intel(R) Xeon(R) Processor, 4 CPUs, governor schedutil (modelled), kernel 6.18.44-fc-v140 — **a modelled machine, tests only**; 90.0 requests a second a step; the work unit 0 passes = 5.00 ms at the top clock; the cover 1400 to 2800 MHz by 140 MHz; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `19c6441659ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 270 | 270 | -0.0% | -0.325 to 0.2 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 270 | 270 | -0.0% | -0.0359 to 0.0219 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.93 | 6.23 | +5.2% | 0.078 to 0.537 | LOSS |
| latency, 99th percentile (ms) | 6.14 | 6.47 | +5.4% | -0.0303 to 0.693 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 5.53 | 5.72 | +3.4% | 0.074 to 0.305 | LOSS |
| failed requests (not answered by the end of the arm) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| energy, CPU package (J; the processor's own meter, the resource) | 1,922 | 1,841 | -4.2% | -117 to -45.2 | GAIN |
| power, CPU package mean (W) | 32 | 30.6 | -4.2% | -1.95 to -0.755 | GAIN |
| energy per 1,000 requests inside the line (J) | 119 | 114 | -4.2% | -7.15 to -2.83 | GAIN |
| frequency ceiling held, mean (MHz; the knob) | 2,800 | 2,706 | -3.4% | -137 to -51.9 | shown, not judged |
| frequency run at, mean (MHz; the governor's own choice under the ceiling) | 2,800 | 2,706 | -3.4% | -137 to -51.9 | shown, not judged |
| CPU busy (share of the run) | 0.0521 | 0.0575 | +10.5% | -0.017 to 0.0278 | shown, not judged |
| ceiling changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed the ceiling back to the operator's and read it back: yes; another writer seen: no; fail-ups: 0; the brain's verdict: rep 1: acting: 2660000 to 2800000; rep 2: acting: 2660000 to 2800000; rep 3: acting: 2520000 to 2800000.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
