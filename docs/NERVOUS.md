# Nervous system

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni-Compass is one field. Muscles are nerves.

```
telemetry  ->  afferent (per muscle)
           ->  one six-state engine
           ->  reflex (shield)
           ->  efferent (only WIRED + authority + not killed)
           ->  native controller on kill
```

`omnicompass/nervous.py` is the register. It does not invent GPU or chiller physics.

| Status | Meaning |
|---|---|
| wired | this tree can sense and push |
| sensed | this tree can sense; it does not push |
| open | named, no plant, no push |

Wired today: `nodes`, `hpa`, `power_cap`.  
Sensed: `heat`, `network`, `security`.  
Open: GPU, cooling, grid, queues, agents, …  
Never a muscle: value alignment.

```bash
python k8s_controlplane/test_nervous.py
```

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
