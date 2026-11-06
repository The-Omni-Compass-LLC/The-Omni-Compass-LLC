# Azure with Omni-Compass's replica room: preregistration

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written on 13 October 2026, before any of the runs it describes. Engine omni-v5 (digest `5648f290`), unchanged: the
lever below has been in the engine since the fourth amendment of `docs/K8S_COMPASS_PREREGISTRATION.md` (4 October),
off unless the operator grants it.

## Why

The Azure steady run A on the card version (run 38339858727, five paired repetitions, `results/live/raw/run-38339858727/`)
read no difference beyond the noise on any gauge. The service sat at its replica cap of 10 in both arms (9.4 and 9.5
replicas on average), its responses were over the line in 30% of the samples and 4.4% of requests failed in both arms,
while Azure's own autoscaler kept about 1.9 of the 4 work machines in service: the cap, not the machines, limited the
service. Omni-Compass has a lever for exactly this, its **replica room** (`omni_controller/controller.py`,
`_replica_room`): while the autoscaler stands at its cap, the compass is at or past its centre or the line is breached,
and the autoscaler's own arithmetic asks for more, the cap is raised to what that arithmetic asks, never past the
ceiling the operator grants; once the demand has held still for a window, the compass is under its centre and nothing
breaches, the cap returns to the operator's own. The operator's range is recorded before the first change, and the
reset restores it. In the Azure runs so far the lever was off (no ceiling granted), so the one lever that could serve
more was never in the test.

## What runs

The Azure bill test as preregistered (`.github/workflows/aks-metered.yml`, `scripts/aks_paired.sh`, the bill on a real
cloud): Azure Kubernetes Service with its own cluster autoscaler, a work pool of 1 to 4 machines, a fresh cluster for
each arm, five paired repetitions with the arms' order rotated, the machines Azure bills counted every 15 s at the list
price, every gauge reported. Two settings of their own, each labelled as such:

| Setting | Load | Measured window | Native | Omni-Compass on top |
|---|---|---:|---|---|
| Steady with replica room | the steady load (the load generator's replica count fixed) | 900 s | the operator's cap of 10, never moved | the replica room, its ceiling read live |
| Burst with replica room | `1 3 1 4 1 3`, the steps written on 5 October (amendment 11) | 1,800 s | the operator's cap of 10, never moved | the replica room, its ceiling read live |

- **The ceiling, read live, never typed in** (correction of 13 October, before any run of this set: the first draft
  named 36, nine pods of 200m on each of the four 2-vCPU work machines, a number written by us, and the founder's order
  of 13 October is that a muscle runs from 1 up to one click under what the system itself can hold, read live). The
  ceiling is what the work pool's machines can hold at the service's own request, read from the cluster as it runs,
  one pod under it; the lever never asks for a machine the fleet does not have. The engine reads it live from Omni v5
  amendment 5 (digest `6093b2b88aa911b9`): the replica room is on by default, its ceiling what the work pool's machines
  and the cluster autoscaler's own room can hold, one pod under it. No run of this set started on an engine before it.
- **The burst steps.** `1 3 1 4 1 3`, the steps written on 5 October (amendment 11). The first draft of this page named
  `1 6 1 8 1 6`, the burst amendment 11 set aside; we do not choose a benchmark's settings, so the written steps stand.
- **The machines.** `Standard_D2_v4` (the Dv4 family: 2 vCPU and 8 GiB like `Standard_D2s_v4`, the same list price of
  $0.096 an hour), in eastus, so the set has its own 10-vCPU family allowance and runs beside the standard Azure sets
  (on `Standard_D2s_v4`) without sharing their quota or their queue. Both arms of a set run on the same family.
- **Everything else as preregistered**: native is Azure's autoscaler and the HPA alone; omni is Omni-Compass on top
  with the compass law, as in the standard Azure sets, and now the replica room granted; the control plane on the
  standard tier in both arms.

## Reading

Three separate runs of each setting, A, B and C (`tools/confirm_abc.py`), each row read as GAIN or LOSS in all three
of our runs, no difference beyond the noise, or the runs disagree. The extra pods and machines the replica room takes
are counted where they fall (HPA replicas, pods started, machine-hours, the bill), the power given, beside the response
times, the time over the line and the failed requests they buy. These settings are reported beside the standard ones,
never in their place.

## Disclosed with this preregistration

The burst run A on the card version (run 38339901189) was started on 13 October at `1 6 1 8 1 6` with the operator's cap
and no replica room, the setting amendment 11 replaced. It is reported as run at those steps, beside this, and not as the
standard burst result; the standard burst on the card version runs at `1 3 1 4 1 3`.

Cost: about $2 to $4 a steady run and $4 to $6 a burst run at list price; six runs, about $30 in all. Time: about six
hours a steady run and nine a burst run.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.


## The burst steps from 14 October

The founder's order of 14 October withdrew amendment 11 of `docs/K8S_COMPASS_PREREGISTRATION.md`: every Azure burst from
that date, this one included, runs at `1 6 1 8 1 6`, the steps first preregistered. The rest of this page stands.

## In the cloud, native's cap (the founder's order of 14 October, night)

From the founder's order of 14 October (night), the Azure sets aim at the bill at native's work: Omni-Compass on top runs
at the tune-down with native's own replica cap (`replica_ceiling 0`), so the replica room is off in every cloud set
(`docs/K8S_COMPASS_PREREGISTRATION.md`, last section). The room stays in the engine for the max, where the benefit is
the work.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
