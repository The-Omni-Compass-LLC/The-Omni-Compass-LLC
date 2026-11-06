# Every muscle its own card: the search, the confirmation and the bodies

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The engine's cards (`realms/muscle_cards_v5.csv`) and how they were found (`tools/tune_cards.py`,
`docs/FORMAL_V5.md` section 5). Development seeds only: chosen on seeds 7100-7109, confirmed on seeds 7200-7209; the preregistered seeds
3000-3009 were never read. A card is kept only if it read GAIN against today's global setting on both sets (fewer
misses, more work or faster, beyond the noise), read LOSS on none of the three, and never fell behind native: on no
seed of either set and under no load over its line more often, doing less work or clearing its line later (the key
to the words: `docs/HOW_TO_READ_THE_RESULTS.md`). Evidence class **S** (modelled).

| Plant | Knob | Muscles searched | Won on the first seeds | Won again (the engine's cards) |
|---|---|---:|---:|---:|
| compute_pool | capacity | 422 | 342 | 305 |
| compute_pool | setpoint | 36 | 31 | 28 |
| energy_storage | power | 23 | 15 | 10 |
| energy_storage | setpoint | 8 | 8 | 8 |
| energy_storage | capacity | 13 | 13 | 13 |
| motion_axis | capacity | 48 | 0 | 0 |
| **All** | | **550** | **409** | **364** |

**What the cards chose** (the number of muscles at each setting; the global setting in brackets):

- compute_pool, edge_util (0.95): 0.7: 256, 0.75: 39, 0.8: 19, 0.85: 13, 0.9: 6
- compute_pool, window (20): 10: 124, 20: 95, 40: 85, 60: 29
- energy_storage, hold_margin (0.05): 0: 9, 0.05: 1
- energy_storage, hold_window (20): 3: 8, 5: 1, 10: 1
- energy_storage, line_z (3.09): 0: 24, 0.25: 1, 0.75: 1, 1: 3, 1.5: 2

**Inside the six organisms** (every plant against native; misses: the share of plant decisions over their
line, removed against native, in percentage points):

| Seeds | Load | Misses removed, global setting | Misses removed, cards | Plants with less work or more misses, global / cards | Power given, global / cards |
|---|---|---:|---:|---:|---:|
| 7100-7109 | normal | 0.078 | 0.094 | 0 / 0 | +0.000% / +0.000% |
| 7100-7109 | climb | 0.153 | 0.293 | 0 / 0 | +0.000% / +0.000% |
| 7100-7109 | line | 0.088 | 0.161 | 0 / 0 | +0.000% / +0.000% |
| 7200-7209 | normal | 0.074 | 0.087 | 0 / 0 | +0.000% / +0.000% |
| 7200-7209 | climb | 0.145 | 0.282 | 0 / 0 | +0.000% / +0.000% |
| 7200-7209 | line | 0.086 | 0.149 | 0 / 0 | +0.000% / +0.000% |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
