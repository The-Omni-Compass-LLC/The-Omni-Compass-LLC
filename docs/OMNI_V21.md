# Omni v21: the immune system knows itself, knob by knob

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v21 (`OMNI_V21.json`, digest `b658f05d43c1e602`, 63 files) stood on main from the evening of 25 October to 30 October, when
omni-v22 (`docs/OMNI_V22.md`, the data stores' wires at the max) landed on it; its tables stand as its own record. It is omni-v20 with
the immune system's self-knowledge, the founder's order of 25 October:

> "OmniCompass's mechanism must know when something is redlining out of its band when OmniCompass is on it. And if OmniCompass
> couldn't fix it to stop it redlining, then OmniCompass's own mechanism must know that if native is better, then it switches
> itself to native. If native is not better, well, then it'll stay wherever and redline there, because redlining less with
> OmniCompass than something else is still a benefit ... against native ... This code and mechanism need to be built within the
> C++ harness, within the immune system ... The immune system has to be activated in nervous system to propagate."

## The rule, in plain words

| Term | What it is |
|---|---|
| **Redlining** | A knob Omni-Compass holds whose gauge is over its own line (the reading divided by the line is over 1) for three decisions in a row. |
| **Stuck** | Redlining, and Omni-Compass's own pushing has not brought it back: the knob is at its own limit, or the reading has not fallen by 5% of where the redline began. |
| **Native is stronger** | Native's twin, the same moment under native's own setting, reads lower than Omni-Compass by more than 5%. |
| **Hand back** | Stuck and native stronger: the knob goes to native and stays there 10 decisions, the hold doubling for each hand-back in a row (up to 160) and halving after a quiet hold. |
| **Stay** | Stuck and native not stronger: Omni-Compass keeps the knob and says so in its audit. It redlines less than native would, which is still a benefit against native. |
| **Return** | After the hold, Omni-Compass takes the knob back only when its own twin reads lower than native's by the same margin and nothing redlines with it. |
| **The nervous system carries it** | An organ every governed knob of which is handed to native has none of Omni-Compass's authority (`native_hold`) until it is returned. |

## Where it is written

| Place | What |
|---|---|
| `omnicompass/immune.py` | the rule, one knob at a time |
| `cpp/src/immune.cpp`, `cpp/include/omnicompass/immune.hpp` | its C++ twin, line for line, proven alike to the last bit on 200 seeded scripts (`tests/test_cpp_immune_parity.py`, sealed by `tools/seal.py`) |
| `omnicompass/nervous_system.py`, `cpp/src/nervous_system.cpp` | `native_hold`: the hand-back carried to the organ's authority, in both twins |
| `omni_controller/controller.py` | each service's autoscaler target: the response time over its line is the redline; native's twin is the same demand under the operator's target, the replicas native's own rule would ask and the M/M/1 wait they would give |

omni-v19's immune rules come with it onto omni-v20: the hand-back on a pod that waits, the immune memory, native's line, immune
maturity and the step back (`tests/test_immune_system.py`).

## What the model gate read

The model gate against omni-v20 (`results/model_gate/V21_VS_V20.md`, eight seeds, every model, our own models,
evidence class S): no LOSS against omni-v20 in any model.

| Model | Against omni-v20 |
|---|---|
| the cluster (the cloud's setting), at 60 s, at 15 s, with blinks, as shipped | pods waiting for a place down 12.9% to 13.3%, fewer waiting, GAIN; machine-hours up 0.9% to 1.3% and energy per core-hour up 0.8% to 1.0%, power given; the power cap's moves, reversals and travel down 1.3% to 1.4%, GAIN |
| the conveyance, its quota cases, the batch beside the service | every gauge the same as omni-v20, STEADY |
| the card, the card near its floor | every gauge the same as omni-v20, STEADY |
| the verdict | the same as omni-v20, STEADY |

Against native the gate reads the LOSS rows omni-v18, omni-v19 and omni-v20 carry, none caused by this version and each on the
next version's list: the pod start wait in the conveyance models (up 9.0% and 10.0%), the batch beside the service (requests
served down 2.1%, alert minutes up 9.8%), and the card's 95th and 99th percentiles (up 0.9% to 5.8%).

Every benchmark runs again on omni-v21 from the moment it reaches main; nothing is read across engines.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
