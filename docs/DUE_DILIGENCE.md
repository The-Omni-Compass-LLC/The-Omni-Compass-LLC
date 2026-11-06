# Due Diligence

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Answers reference the Claims Register (C-numbers) and the Technical Manual.

## Engineering
**Does the mathematics hold?** Equations (1) to (8), Propositions 1 to 3 and their proofs are in Manual Chapters 2 and 3. The 500/500 CONVEY/CERT result is a property of the controller (Proposition 3), shown by counterfactuals: the controller aimed at the wrong basin also scores 500/500.
**Is Python the same as C++?** Yes (C1, C2). The verifier also builds a deliberately mutated C++ governor and checks that the parity test rejects it.
**Can every number be reproduced?** `python verify.py` rebuilds the C++, reruns parity, reruns the 100,000,000-decision soak and compares it with the recorded result, replays held-out scenarios and checks the pre-registered SHA-256 hashes (program fingerprints are additionally checked when the Python version matches the recorded one).

## Operations
**Against what we run today?** On real software, against the native controller as its project ships it: Kubernetes' own pod autoscaler and scheduler on real clusters, and the data stores as their vendors ship them, paired, three runs each (`results/OMNI_INDEX.md`, class L). In the models (class S, C8 to C12), against a documented-behaviour reference model of Kubernetes autoscaling (HPA tolerance 0.1, 300 s scale-down stabilization, HPA targets 0.5 to 0.8; simplified Cluster Autoscaler with 10-minute unneeded time, 0.5 utilization threshold, 10-minute delay after scale-up): C8 to C12, including where Omni-Compass read LOSS. The reference model is not the upstream controllers (C12b); running the upstream controllers against the same scenarios is the next baseline step.
**On real traffic?** Not yet: no production traffic. The live results run real software on GitHub's machines with generated load and a public day of demand replayed (the Google cluster trace of 2011, `results/live/V25_TRACE_GOOGLE2011.md`); the models use a synthetic stack model. The pilot protocol is the next evidence step (C14).
**What happens when it is wrong?** Observe mode changes nothing (C6). The reset returns control to the native managers at the next interval (omni_kill arm). The shield blocks actions that violate I1 to I5 (C7).
**Will it wear hardware?** Machine start/stop cycles, power-cap travel and thermal travel are measured for every arm (C12, Manual Chapter 8).

## Security
**What authority does it hold?** Capacity, replicas, power caps, rollback authorization and routing, only in AUTOPILOT, only through the shield.
**Can it expand capacity during a security block?** No: invariant I1 is enforced before execution.
**Does it replace encryption, identity or policy engines?** No. Those components are retained (fleet model, security role).

## Finance
**What does it save?** In the models, energy per run versus the reference autoscaling (C8, class S). On real software the record reads the work, the speed and the machines it took (the Omni index, `results/OMNI_INDEX.md`); more work for the bill is still being measured (`docs/WORK_PER_BILL.md`), and no bill saving is claimed. Fleet-scale figures are modelled (C13); the modelled saving comes from reduced idle and padded capacity, not from removing the decision components' own consumption.
**What does it cost to run?** C5.

## Adoption
**How is it introduced without risk?** A week of shadow with no write rights, then one muscle at a time with the reset tested at each handover, then 30 days paired against native in three runs, native on in every arm (docs/PILOT_PROTOCOL.md); on a production system only under a pilot agreement signed with The Omni-Compass LLC, and live customer traffic only under the Enterprise License.

## Referees
**Was it tuned on the test data?** No. Law, shield and baselines were frozen and fingerprinted before the held-out seeds 346410161 and 360555127 (results/PREREGISTRATION.json).
**Where does it fail?** Backlog violations against current autoscaling (C11); the engine-dynamics ablation (Manual Chapter 8); open obligations (Manual Chapter 10).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
