# The wiring search, development seeds

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Seeds 7100-7109 (development; the preregistered seeds 3000-3009 untouched), 1097 muscles, 14 cards, both muscle loads; 1409 s. Evidence class S (our own models). Nothing here changes the engine: the cards enter it only as the next version, run again on the preregistered seeds.

## The rule (fixed before any result was read)

1. A card is out if the lease did not hand its knob back on every seed, if under either load it did less work, more misses or cleared its line later (95% intervals over the seeds, clear of zero), or if it spent more energy with no gain in work, speed or misses.
2. Gains rank: more work, then faster, then fewer misses, then less energy (the same work, speed and misses on less energy).
3. The card with the best set of gains is chosen; the max (the engine's default) is kept wherever it gives that set, so another card replaces it only where it adds a gain the max does not give.
4. A muscle no card improves keeps the max, and says why.

## What it found

| | Muscles with a gain | Muscles with none |
|---|---:|---:|
| The max alone (every muscle on the default card) | 503 | 594 |
| Each muscle on its own card | 670 | 427 |

### Muscles given another card

| Template | Knob | Card | Gains | Muscles |
|---|---|---|---|---:|
| process_loop | setpoint | `save` | LESS ENERGY | 82 |
| process_loop | setpoint | `compass` | LESS ENERGY | 25 |
| compute_pool | power | `compass` | LESS ENERGY | 16 |
| compute_pool | power | `compass` | FEWER MISSES + LESS ENERGY | 15 |
| thermal_zone | setpoint | `save_precool` | LESS ENERGY | 11 |
| thermal_zone | setpoint | `save` | LESS ENERGY | 8 |
| motion_axis | capacity | `compass` | LESS ENERGY | 5 |
| compute_pool | power | `save` | LESS ENERGY | 3 |
| compute_pool | capacity | `max_full85` | FASTER + FEWER MISSES | 1 |
| compute_pool | setpoint | `save_free` | MORE WORK + FASTER + FEWER MISSES | 1 |
| compute_pool | capacity | `max_full90` | FASTER + FEWER MISSES | 1 |
| compute_pool | setpoint | `max_full85` | FEWER MISSES | 1 |
| energy_storage | setpoint | `save_shave` | FEWER MISSES | 1 |
| compute_pool | capacity | `max_full85` | MORE WORK + FASTER + FEWER MISSES | 1 |

### Muscles no card improves

| Template | Knob | Muscles |
|---|---|---:|
| compute_pool | admission | 194 |
| process_loop | capacity | 39 |
| motion_axis | power | 38 |
| process_loop | admission | 33 |
| motion_axis | admission | 30 |
| energy_storage | power | 23 |
| thermal_zone | capacity | 17 |
| process_loop | power | 12 |
| energy_storage | admission | 10 |
| thermal_zone | admission | 7 |
| motion_axis | capacity | 6 |
| energy_storage | capacity | 5 |
| thermal_zone | power | 4 |
| process_loop | setpoint | 4 |
| compute_pool | power | 3 |
| energy_storage | setpoint | 2 |

Every muscle, every card: `WIRING_DEV.csv`; the frozen choice: `WIRING_CARDS.json`.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
