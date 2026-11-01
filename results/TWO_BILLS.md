# The two bills: four arms, the bill and the work done inside it

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's design of 1 November 2026: the same work measured against what it cost, on the two bills a customer pays. **A**, the chip native, and **B**, the chip with Omni-Compass on native: a rented graphics card run directly, its bill the rental. **C**, the cloud native, and **D**, the cloud with Omni-Compass on native: Kubernetes on Azure's machines, its bill Azure's own at list price. The question for each bill: is it the same, and is more work done inside it. Each arm's runs are labelled run 1, 2 and 3 so the run letters never meet the arm letters. Every number is read from a table the repository already holds, each place on its own engine; nothing here is a new measurement.

## The chip: A against B (an NVIDIA A10 on Lambda, omni-v23, three runs)

From `results/gpu/V23_A10_CAP_FULL_ABC.md` (runs 41243352339, 41243355485, 41243358705): the full load, more requests offered than the card serves in its window, so the work done can rise inside the same rented time. The bill is the rental for each arm's own window (its energy over its mean power) at $1.29 an hour, the price each launch printed (`docs/RUN_LEDGER.md`); Lambda's billing page is the exact figure. Beside it, the same runs' fixed job (`results/gpu/V23_A10_CAP_ABC.md`, a set number of requests in each window, so the work cannot rise): requests served STEADY, the same; energy STEADY, under the floor (the three runs' mean 0.38%).

| Gauge | Three runs | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| bill ($, the rental for the arm's window) | **STEADY, under the floor (the three runs' mean 0.01%)** | STEADY, 0.04% | STEADY, 0.00% | STEADY, 0.01% |
| work done (requests served) | **the runs disagree** | GAIN, 1.51% | GAIN, 0.73% | LOSS, 0.70% |
| work per dollar (requests served per $) | **the runs disagree** | GAIN, 1.46% | GAIN, 0.73% | LOSS, 0.69% |
| energy, GPU (J) | **GAIN in all three of our runs** | STEADY, 0.31% | GAIN, 0.63% | GAIN, 1.48% |
| energy per served request (J) | **GAIN in all three of our runs** | GAIN, 1.79% | GAIN, 1.35% | GAIN, 0.78% |
| response time, 95th percentile (ms) | **the runs disagree** | GAIN, 3.68% | GAIN, 1.38% | LOSS, 2.25% |

| Run | Arm | Window (s) | Bill ($) | Requests served | Requests per $ |
|---|---|---:|---:|---:|---:|
| 1 | A, native | 333.2 | 0.1194 | 2,616 | 21,908.8 |
| 1 | B, Omni-Compass on native | 333.4 | 0.1195 | 2,656 | 22,229.5 |
| 2 | A, native | 331.8 | 0.1189 | 2,270 | 19,089.3 |
| 2 | B, Omni-Compass on native | 331.8 | 0.1189 | 2,286 | 19,229.1 |
| 3 | A, native | 331.9 | 0.1189 | 2,255 | 18,963.8 |
| 3 | B, Omni-Compass on native | 331.8 | 0.1189 | 2,239 | 18,832.8 |

## The cloud: C against D (Kubernetes on Azure's AKS, omni-v18, one set of 98 paired repetitions)

From `results/live/AKS_STEADY_100_OMNI_V18.md`, the newest cloud set with a metered bill. The engine that stands has not yet run in the cloud: its set starts when Azure's current long set ends, and this row is then read again on it.

| Gauge | C, native | D, Omni-Compass on native | The change | 95% interval | Beyond the noise |
|---|---:|---:|---|---|---|
| bill at list price ($ a window) | 0.05626 | 0.05694 | 1.21% (power given, inside the noise) | -0.00071 to +0.00208 | no |
| machines billed (machine-hours a window) | 0.5860 | 0.5931 | 1.21% (power given, inside the noise) | -0.0074 to +0.0216 | no |

This set counted no work done: the cloud's work meter came with the cloud sets after 31 October, so its work per dollar is not read here; the set on the engine that stands reads it.

## What the two bills say today

- **The chip:** the bill STEADY, under the floor (the three runs' mean 0.01%) (the same rented window in both arms); the work done inside it the runs disagree; the work per dollar the runs disagree; the energy for each request served GAIN in all three of our runs.
- **The cloud:** the bill 1.21% higher with Omni-Compass on native, inside the noise; the work done was not counted in that set, so the work per dollar waits for the set on the engine that stands.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
