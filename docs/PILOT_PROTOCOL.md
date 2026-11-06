# Pilot Protocol

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Before you wire anything:** read [`DISCLOSURES.md`](../DISCLOSURES.md). Omni-Compass acts only through the wires it is given; it cannot be slapped on. If your paired receipts differ from the published benchmarks in direction, the first presumption is wiring: check the installation with section 4.5 of the manual (*Wired right or wired wrong*).

A pilot is the one proof our own runs cannot give: Omni-Compass on top of the licensee's own native controllers, on the
licensee's own systems and work, read against native by the licensee's own engineers. Every result The Omni-Compass LLC
publishes was run and scored by its own code, and every table says that no outside party has reviewed or approved it. A
pilot run by this protocol is how that changes. The protocol was rewritten on 31 October 2026 for the engine that stands:
native stays on in every arm, Omni-Compass moves native's knobs and never replaces native, and the readings are the
receipts and the service gauges, read by the one key.

## Before day one: the agreement and the license

- The evaluation license covers evaluation and simulation: test and staging systems, the models and `verify.py`.
- Governing live, customer-facing traffic is production use, and production use needs the signed, paid Omni-Compass
  Enterprise License first.
- A pilot on a production system, the read-only shadow included, runs only under a pilot agreement signed with The
  Omni-Compass LLC before day one. The agreement names the systems, the dates, the rules on this page and who receives
  the readings.

## What runs, and what does not

- **The governor** (`omni_controller/controller.py`; on a graphics card, `omni_controller/gpu_governor.py`) sits on top
  of the native controllers already there: Kubernetes' pod autoscaler and cluster autoscaler, the card's own power
  management. Native stays on in both arms. Omni-Compass sets native's knobs (the autoscaler's target and range, the
  machines in service, the CPU limits, the card's power limit) and never takes native's place.
- **The engine at its factory tune**, as shipped (`docs/FACTORY_PROFILE.md`), at the factory beat. Any knob may be
  turned. A changed tune's readings are its own, and turning a knob can change every metric in either direction
  (`DISCLOSURES.md`, section 3).
- **Not the pilot:** the C++ engine and `verify.py`. They check that the engine's two copies compute the same and that
  the code does what its rules say (phase 0). They govern nothing.
- **Omni-Compass by itself** (the third arm: native's autoscalers off, Omni-Compass the only controller on those knobs)
  runs only where the licensee chooses it, after phase 2, preregistered as `docs/SOLO_PREREGISTRATION.md` is.

## Phase 0: the code checked (one day, the evaluator's own machine)

Run `python3 verify.py`. Pass: `VERIFICATION: PASS`. This includes the parity tests of the C++ engine against the Python
(`tests/test_cpp_*_parity.py`), the shield's invariants and the reading rules. `python3 tools/reproduce.py` rebuilds every
published table from its archived raw runs and exits 1 on any difference.

## Phase 1: shadow (one week, no write rights)

- The shadow kit (`docs/PILOT_KIT.md`, `scripts/pilot_shadow.sh`): the governor in observe mode at the factory beat,
  under an identity that can read and cannot write. The kit proves this with `kubectl auth can-i` and stops if any write
  right exists.
- Logged at every decision: what Omni-Compass would set, what native did and what followed (`shadow_out/audit.jsonl`),
  with the count of writes, which must be 0.
- Pass, agreed before the start: no write, and no logged decision that breaks the shield's invariants I1 to I5 (claim C7,
  `docs/CLAIMS_REGISTER.md`).

## The handover (one day)

One muscle at a time, in this order: the power cap, the machines in service, the pod autoscaler's target and range, then
the CPU limits. `--native MUSCLE[,...]` leaves every muscle not yet handed over where native runs it. At each handover
the reset is tested: everything goes back to native, and the native settings are read back equal to the snapshot taken
at the start.

## Phase 2: the paired pilot (30 days: three runs of 10 days, A, B and C)

- **The pairing:** two matched pools at the same time, the same work split between them: native alone on one,
  Omni-Compass on top of native on the other. Where one pool is all there is, alternate whole days between the arms,
  with the same days of the week in each.
- **The three runs:** days 1 to 10 are run A, days 11 to 20 run B, days 21 to 30 run C. Each run is read on its own, and
  the three are read together by the three-run rule (`tools/confirm_abc.py`).
- **The stops:** the kill switch is tested on the first day and the last. It is instant, for security only, and puts
  every setting back to native (`omnicompass/master.py`, `tools/omni_switch.py`). The lease is tested once: stop the
  governor's process and watch the plug walk every setting back to native gradually.
- **Pass:** the pilot holds. Nothing the service is judged on reads LOSS against native in run A, B or C by the one key,
  and every resource that rose is read beside the work it bought, as power given.

## What to read: the receipts and the service gauges

| Where | The receipt, native against Omni-Compass | Read from |
|---|---|---|
| Through the cloud | the work per dollar: the work completed over the provider's bill for each arm's machines | the provider's own cost export and the licensee's request or job counts |
| The chip | the work per joule: the work completed over the card's own energy counter, with its clocks, temperature and throttle reasons beside it | the card's published interface (`nvidia-smi`, NVML) |
| On site | the work per machine-hour: the pool is the owner's, so its hours are no bill | the capture below |
| The service, every place | the 95th percentile response time (the 90th and 99th beside it), the minutes over the response line, the pods waiting for a place, the failed requests, the work completed | the licensee's own monitoring |
| Oversight, every place | the alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line: the minutes an on-call page would be open), and the operations engineer-hours where the licensee logs them, each turned into dollars only at the licensee's own rates | the alert history and the licensee's own time records |
| Omni-Compass itself | every write it made, read back, and every reason | its audit (`--audit`) |

Capture both arms read-only with `fleet/capture/kube_capture.sh`, then score each run:

`python3 pilot/score.py --baseline native.csv --omni omni.csv [--idle-w W --dyn-w W]`

It reports node-hours and energy per used CPU core-hour, utilisation, pending-pod minutes and the autoscaler's shortfall
minutes, each with a bootstrap 95% interval over hourly blocks. Energy is measured only where the capture holds a meter's
`power_w`; where no meter reads it, energy is not scored. Each run needs at least 24 hourly blocks per arm (a 10-day run
holds about 240).

### The paired audit sheet

One sheet a run, filled in only from that run's own records, both columns measured, nothing written before the run and
every LOSS row kept. The licensee's own engineers fill it in; the one key reads it across the three runs.

```
OMNI-COMPASS PAIRED AUDIT — native against Omni-Compass on native
Window: ____ days     Place: bare metal / through the cloud     Engine: omni-v__ (fingerprint ________)
Run: A / B / C  (each run paired; the same work offered to both arms)

                                         NATIVE          OMNI-COMPASS ON NATIVE
WORK      Work completed (requests/jobs) __________      __________
BILL      Machine-hours billed           __________      __________
          Rate per machine-hour ($)      __________      __________   (the same rate in both)
          Other metered line items ($)   __________      __________
          Bill, B ($)                    __________      __________
FOR THE   E = W / B (work per dollar)    __________      __________
BILL      G = E(Omni) / E(native) − 1    ____________   read across the three runs: GAIN, STEADY or LOSS
OVERSIGHT Alert minutes (p95 over line)  __________      __________
          Operations engineer-hours      __________      __________   (the licensee's own logs)
          Labor at the licensee's rate   __________      __________
HEALTH    Failed requests                __________      __________
          95th-percentile response (ms)  __________      __________
```

On bare metal the bill is fixed for the window, so a benefit shows as more work inside it (W); through the cloud it may
show as more work, a smaller bill (B), or both. Either way it is read in G, the one equation of `results/TWO_BILLS.md`.
The labor line is the licensee's: the record of this repository counts alert minutes and the governor's own commands, never
people, and no rate or share is assumed for it.

## Reading it

Every gauge is read by the one key (`tools/readings.py`, `docs/HOW_TO_READ_THE_RESULTS.md`): GAIN, STEADY or LOSS by what
the gauge is for, never by the sign of its number. Time waited, missed or failed that fell is a GAIN; work that rose is a
GAIN; a resource spent or held that fell is a cut, a GAIN, and one that rose is power given, never a LOSS. A mean change
under 0.5% reads STEADY. Across the three runs a reading is GAIN or LOSS in all three when every run moved the same way
clear of zero; the runs disagree when clear runs moved in opposite directions, and that is a finding to look into, not a
result.

## Reporting

Every row is reported, LOSS included, in the key's words, with the run it came from. The readings, the captures and their
SHA-256 sums go to the licensee and to The Omni-Compass LLC as the pilot agreement says. Where the pilot's direction
differs from the published benchmarks, the first presumption is the wiring (section 4.5 of the manual), and the pilot
goes on once the wiring is checked.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
