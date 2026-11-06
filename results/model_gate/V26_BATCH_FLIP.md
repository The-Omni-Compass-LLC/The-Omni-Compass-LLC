# The batch queue's waiting pods through the governor's decision: omni-v26 against omni-v25 (our own model, class S)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

`tools/batch_flip_model.py` replays, open loop, the native arm's own timelines of the KAI scheduler's four ways on the organism alone (`results/model_gate/BATCH_FLIP_INPUTS.json`: the cluster's waiting pods from each repetition's capture and the web service's 95th percentile in 10 s windows, 30 repetitions of runs 41809041712, 41810759693 and 41812560443) through each engine's own governor, a decision every 10 s and a fast check every 5 s on the replay's own clock. The governor's writes move neither the replayed pods nor the response times, so the model reads the decision rule alone. The service's and the queue's own gauges are read only by the benchmarks' runs (`docs/LOSS_CAUSES_2026-11-06.md`).

| Gauge | omni-v25, mean a repetition | omni-v26, mean a repetition | Reading | 95% interval of the paired change |
|---|---|---|---|---|
| writes of the web service's target | 16.13 | 2.67 | GAIN, down 83.5% | raw −16.49 writes to −10.45 writes |
| changes of the target after the first | 15.20 | 1.73 | GAIN, down 88.6% | raw −16.49 changes to −10.45 changes |
| seconds below native's target while another workload's pods waited | 22.17 | 4.83 | GAIN, down 78.2% | raw −21.93 s to −12.74 s |
| holds of native's target started | 0.03 | 1.43 | power given, up 4200.0% | raw +1.21 holds to +1.59 holds |

Errors in the governor's audit: omni-v25 0, omni-v26 0.

A hold is the fix itself: native's target kept for ten minutes, doubled for each hold in a row, while another workload's pods wait for the room; its count rising is the mechanism working, power given by the key.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
