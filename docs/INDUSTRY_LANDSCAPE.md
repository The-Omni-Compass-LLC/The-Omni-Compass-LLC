# The Industry's Three-Layer Attack, and Where Omni-Compass Sits

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The cost of computing is being attacked in three layers at once: the chip, the cloud and the software. This page says what each
layer's tools act on and what, by their construction, they leave to the other layers; where Omni-Compass sits in that picture, in
the terms of control engineering; and how far each of its three benefits is shown on the record today. The products named in each
layer, each from its own public material and graded on the same seven measures as Omni-Compass, are in `docs/LANDSCAPE.md`. No
product of anyone else was benchmarked by us: nothing here says another product falls short, only what layer it acts in.

## The three layers and what each acts on

| Layer | What is built there | The actuator it moves | The signal it closes its loop on | What its construction leaves to the other layers |
|---|---|---|---|---|
| **The chip** | chiplets and stacked high-bandwidth memory; custom accelerators; the card's own firmware (power capping, clock and voltage scaling, thermal limits); vendor power profiles | the silicon's capacity, and the card's power limit, clocks and fans | the card's own power, temperature and utilization | how many machines and replicas the work is offered, and when; the service's own queues and targets |
| **The cloud** | cost visibility and FinOps tools; node autoscalers and provisioners; rightsizing and purchase planning; bare-metal repatriation for steady loads | the machine fleet: its count, its instance types, its purchase model | machine utilization and the bill | the card's power limit; the service's own controllers inside each pod |
| **The software** | orchestrators and schedulers (Kubernetes, batch schedulers); pod autoscalers (the HPA, KEDA); each service's own controllers (a database's pool, a cache's memory, a broker's consumers) | placement, replicas, a service's own setting | each controller its own signal (the HPA its utilization, a pool its waits) | each loop sees only its own signal; none reads the others or the layers beside it |

Each layer's controllers are **inner loops**: every one closes its own loop, on its own signal, at its own clock. That is the
problem the front matter names: capacity held idle by worst-case margins, reaction after the line is crossed, loops at cross
purposes, and demand outrunning power and hardware.

## Where Omni-Compass sits: a supervisory outer loop on top of the inner loops

Omni-Compass is a **supervisory controller** in a **cascade**: the native controllers stay the inner loops, in charge of their own
actuation; Omni-Compass is the outer loop that reads the whole body and moves the **setpoints** those inner loops already accept.
It works in the **control plane** only, never the data plane: through a two-way plug it reads each controller's own meters (one
wire in) and writes the one setting that controller accepts (one wire out), recording the setting before its first write, reading
back every write, and restoring the setting at the end; a lease walks every setting back to native if it stops. No request or byte
of the workload passes through it, and it removes no controller: on Kubernetes the scheduler, the kubelet and the autoscalers stay
in every arm.

Its actuators reach into all three layers, each through that layer's own published interface:

| Layer | What Omni-Compass moves there | Through |
|---|---|---|
| The chip | the card's power limit and clock ceiling, under the operator's own cap | the card's management interface |
| The cloud | machines the cloud's own autoscaler made and the work does not need, closed and parked for that autoscaler to remove (it asks the cloud for none and holds no cloud credential); the autoscalers' ranges | the Kubernetes API |
| The software | the pod autoscalers' targets, replicas ahead of the load, the processor a machine can spare given to its pods, a database's pool, a cache's memory, a broker's consumers | the Kubernetes API and each service's own administrative interface |

The law that moves them is one law for every muscle (the compass law, `omnicompass/compass_law.py`): a band with cushions, two
antagonist forces, a smooth response, every muscle driven toward its own limit and never past it, never below native.

## Side by side

| | Chip-layer tools | Cloud-layer tools | Software-layer controllers | Omni-Compass, on top of native |
|---|---|---|---|---|
| Acts on | the silicon and the card's controls | the machine fleet and its price | placement, replicas, each service's setting | the setpoints of the native controllers in all three layers |
| Reads | the card | the fleet and the bill | its own signal | every controller's own meters, as one body |
| Loop | inner, its own clock | inner or advisory | inner, its own clock | outer, supervisory, one decision every factory beat |
| Replaces a native controller | no | some replace the node autoscaler | they are the native controllers | never |
| If it stops | — | — | — | every setting walks back to native on its lease |
| Published decision law | vendor-specific | mostly not published | published (each project's own rule) | published in full, with its mathematics and source (the Owner's Manual) |
| Evidence against native | vendor claims | vendor claims | — | paired runs against native on the same machines, every gauge reported, losses included (class L, P and S, named on each table) |

## The three benefits, and how far the record shows each

| Benefit | How Omni-Compass produces it | On the record today | Source |
|---|---|---|---|
| **More work** | replicas ready ahead of the load, the processor a machine can spare given to its pods, every muscle driven to its own limit | shown at the software end: the Omni index **GAIN 20.4%** on omni-v25's tables (work, speed and machines, the machines it took shown beside them as power given), **GAIN 94.0%** on work and speed alone, on real software on GitHub's own machines | `results/OMNI_INDEX.md` |
| **More work for the bill** | idle machines parked for the cloud's own autoscaler to remove; the same lease doing more work on bare metal | **being measured**: on one A10 card the work for each dollar went up 1.46% and 0.73% in two runs and down 0.69% in the third, so the three runs disagree; in the cloud the work is not yet counted. No bill saving is claimed yet | `docs/WORK_PER_BILL.md` |
| **Less oversight** | it acts as a reading nears its line, not after; every change logged with its reason and read back; a hand-back to native on a crash | shown as **fewer alert minutes** (the minutes an on-call page would be open) in the Kubernetes tests on GitHub's machines (omni-v25's tables): down 59% to 63% on a public day of demand and down 18% to 20% with Omni-Compass killed mid-run, GAIN in all three of our runs; down 12.5% to 21.3% under faults, GAIN by the mean of our three runs (beyond the noise in one); on the batch queue up 0.9% and 3.7% in two runs and unchanged in the third, more minutes over the line, LOSS by the mean of our three runs (beyond the noise in one) | `results/live/V25_TRACE_GOOGLE2011.md`, `results/live/V25_ROBUST_KILL.md`, `results/live/V25_FAULTS.md`, `results/live/V25_BATCH.md` |

**On trade-offs.** The engine that stands keeps do no harm in its strictest form: every muscle judged on itself, never below native
on a judged gauge (the work done, the response time, the minutes over the line, the pods waiting, the failures). A resource it spends
to get there is shown beside the work it bought as power given, never hidden: in our own model of the cloud at the max the
machine-hours rise 8% to 34% across the beats, 15% at 60 s, with the work held by the model's own load (omni-v23's rules on the
corrected model, `results/model_gate/V23_LADDER_CORRECTED.md`, class S). That is why the cloud is judged by work for the bill, and why no "no trade-off" claim is made.

## What this page does not claim

- That any other product falls short, or that Omni-Compass is the only approach: no other product was benchmarked by us.
- A smaller bill: work for the bill is still being measured.
- Fewer people: what is measured is fewer alert minutes.
- Anything in the data plane: Omni-Compass touches no data, cache, network or silicon.

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
