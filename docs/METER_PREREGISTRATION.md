# The machine's own meter and Kepler beside the Kubernetes sets (preregistration)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 13 October 2026, before any run with a meter. It is register row 79, the first of the nine pieces the founder
listed on 12 October (`docs/THE_SEAT.md`): Kepler, the shared energy meter of the Kubernetes sets.

## Why

On GitHub's machines every Kubernetes set reports energy from a declared model (class S): kind has no power meter, and
GitHub's virtual machines show no processor counters. Kepler 0.10 and later carry no model of their own: they read the
processor's RAPL counters, and without them have only a stand-in development meter. So the meter runs where the counters
are: a rented bare-metal machine. There the energy rows become a measurement (class P).

## What is measured

- **The machine's own meter** (`tools/rapl.py`): the processor's RAPL counters through Linux's powercap files, its package
  zones and its memory (dram) zones summed; the core and uncore zones are parts of a package and are never added again;
  a platform (psys) zone is recorded, never added. Read every 2 s from just before each measured window opens to just
  after it closes, each step's increase added and a counter's wrap counted as a wrap, and read at the window's two marks.
  It is the energy the whole machine under the cluster drew in the window, Omni-Compass's own process included.
- **Kepler 0.11.4** (`scripts/kind_addons_kepler.sh`; the project's own manifests at the release tag, every file SHA-256
  pinned, its image the release's): its node counter (package and memory) on the control plane, and its counters of the
  service's pods, read through the API server at the window's two marks.

## The arms and the set

Unchanged: the set is the standard Kubernetes set of every earlier kind run (`scripts/kind_paired.sh` through
`scripts/metal_kind_run.sh`: the six-worker kind cluster, a fresh cluster per arm, both arms back to back on the same
machine in an order rotated by repetition, the closed-loop load stepping 1 2 3 1 2 1, 120 s warm-up, 900 s measured, ten
paired repetitions a run). Native is Kubernetes with its HPA; omni is Omni-Compass on top of it, the engine that stands
at the run's commit. The meter and Kepler read both arms the same way; neither is an arm, and neither is read by
Omni-Compass.

## How it is read

- **Judged**: "energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P)", the aim
  is lower, by the rule of every gauge: the paired mean difference and its 95% interval, and over three runs (A, B, C on
  one commit) the three readings of `tools/confirm_abc.py`. Every other gauge of `tools/live_reps.py` is reported as in
  every set, losses included; the declared-model energy rows stay beside the meter.
- **Shown, never judged**: Kepler's reading of the same counters (a cross-check of the meter) and the energy Kepler
  attributes to the service's pods (its split of the meter by each pod's CPU time; a pod gone before the window closes
  takes its share with it, so this row is a floor).
- The energy the machine draws is the power given for the work it does: it is shown beside the work, the speed and the
  misses, never called a loss on its own.

## When a run does not count

A machine that is a virtual machine, or shows no readable package zone, runs nothing (`scripts/metal_kind_run.sh`
stops). A repetition counts only with the meter's samples covering its whole window; a Kepler manifest that does not
match its pin, or a Kepler that reports no node energy, stops the run. As in every set, a repetition that fails any of
its checks is marked invalid, kept in the raw files and not counted.

## Known limits, said before the result

- On one machine running kind, the six workers are containers on the same processor: Omni-Compass's node pool closes
  workers, but a closed worker draws next to nothing on its own, so "fewer machines" shows in the meter only through
  the work no longer running there. The meter measures what the metal draws, no more.
- RAPL covers the processor packages and memory, not the fans, disks, network or power supply. A wall meter would add
  them; the CPU power kit can read one (`docs/CPU_POWER_PREREGISTRATION.md`).
- Reading RAPL needs root (Linux 5.10 and later); the kit runs under sudo.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
