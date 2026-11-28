# The map: hardware

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every file below is the property of Dubra Software Inc. / The Omni-Compass LLC unless its row names a third party, and carries the owner's notice as its row says. The ID is the file's map ID, given once and never changed; each is an anchor: `docs/map/HARDWARE.md#<id in lower case>`. Written by `tools/repo_map.py` from `results/REPO_MAP.json`; back to [the map's index](README.md).

| Map ID | File | What it is | Engine | Owner | How it carries the owner's notice |
|---|---|---|---|---|---|
| <a id="oc-hw-00001"></a>OC-HW-00001 | [`hardware/SCHEDUTIL.md`](../../hardware/SCHEDUTIL.md) | schedutil and the Omni-Compass CPU ceiling |  | Dubra Software Inc. / The Omni-Compass LLC | the notice in the file |
| <a id="oc-hw-00002"></a>OC-HW-00002 | [`hardware/__init__.py`](../../hardware/__init__.py) | program (Python) |  | Dubra Software Inc. / The Omni-Compass LLC | the notice in the file |
| <a id="oc-hw-00003"></a>OC-HW-00003 | [`hardware/cpufreq.py`](../../hardware/cpufreq.py) | CPUFreq contract used by the Omni-Compass hardware ceiling muscle. |  | Dubra Software Inc. / The Omni-Compass LLC | the notice in the file |
| <a id="oc-hw-00004"></a>OC-HW-00004 | [`hardware/node_exchange.py`](../../hardware/node_exchange.py) | CPU and GPU on one conserved power budget: the conveyance law (omnicompass/conveyance.py) with CPU organs beside GPU organs, so watts a CPU … |  | Dubra Software Inc. / The Omni-Compass LLC | the notice in the file |
| <a id="oc-hw-00005"></a>OC-HW-00005 | [`hardware/plant.py`](../../hardware/plant.py) | Device plant: CPU frequency (DVFS) and GPU power-limit muscles, three architectures, 24 scenarios. |  | Dubra Software Inc. / The Omni-Compass LLC | the notice in the file |
| <a id="oc-hw-00006"></a>OC-HW-00006 | [`hardware/schedutil.py`](../../hardware/schedutil.py) | schedutil, kernel-shaped (kernel/sched/cpufreq_schedutil.c, frequency-invariant case), and the Omni-Compass ceiling. |  | Dubra Software Inc. / The Omni-Compass LLC | the notice in the file |
| <a id="oc-hw-00007"></a>OC-HW-00007 | [`hardware/site_exchange.py`](../../hardware/site_exchange.py) | Site power exchange: G GPU groups share one site power budget (power oversubscription: the budget is below the sum of TDPs). THEORETICAL SIM… |  | Dubra Software Inc. / The Omni-Compass LLC | the notice in the file |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
