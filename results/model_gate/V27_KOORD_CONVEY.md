# Koordinator's best-effort queue through the conveyance: omni-v27 against omni-v26 (our own model, class S)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

`tools/convey_owed_model.py` replays, open loop, the native arm's own timelines of both Koordinator batch-stream tables on omni-v25 (`results/model_gate/KOORD_CONVEY_INPUTS.json`: the host's busy share, each best-effort pod's machine and its times made, placed and done, and the web service's replicas; 60 repetitions of runs 42173258848, 42173278954, 42185612749, 41800261877, 41800269022 and 41802293120) through each engine's own conveyance every 15 s, as the governor's fast check calls it. The conveyance's writes move neither the host's busy share nor the queue, so the model reads the rule alone. The web service's and the queue's own gauges are read only by the benchmarks' runs (`docs/LOSS_CAUSES_2026-11-07.md`).

| Gauge | omni-v26, mean a repetition | omni-v27, mean a repetition | Reading | 95% interval of the paired change |
|---|---|---|---|---|
| limits written | 19.13 | 23.07 | power given, up 20.6%, inside the noise | raw −1.88 writes to +9.74 writes |
| limits lowered | 7.03 | 10.53 | power given, up 49.8% | raw +0.86 writes to +6.14 writes |
| limits raised again after a lowering (the cycle) | 6.85 | 2.70 | GAIN, down 60.6% | raw −6.32 turns to −1.98 turns |
| processor-seconds above the operator's limit while a best-effort pod waited for a place | 7743.48 | 4.21 | GAIN, down 99.9% | raw −7912.83 core-s to −7565.70 core-s |
| processor-seconds above the operator's limit in all | 8720.62 | 181.60 | GAIN, down 97.9% | raw −8679.85 core-s to −8398.20 core-s |
| the largest single raise of one pod's limit | 3100.00 | 626.67 | GAIN, down 79.8% | raw −2727.81 m to −2218.85 m |

Errors in the conveyance's audit: omni-v26 0, omni-v27 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
