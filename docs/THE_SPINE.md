# The spine: the base every stack runs on

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The **spine** is the set of muscles every real stack runs on: the 267 muscles of the 1,107-muscle catalog
(`realms/catalog_v5.csv`) whose realm list names all four realms. A robot fleet, a trading system, a hospital's critical
environment and an AI training pool differ in every muscle of their own trade, and they are alike in this: their work runs
on computers that are scheduled, placed, given processors and memory, connected, stored, watched, kept alive, powered and
cooled. Those thirteen families are the spine. Since 16 October (the founder's order) the spine is an **organism in its own
right**, the seventh, run native and with Omni-Compass on top of native exactly as the other six are, because the base of a
stack deserves its own reading before any trade is put on it. The relation is the one between an operating system and the
programs that run on it: no program re-implements scheduling, memory or the disk, it stands on the system that does them;
no realm's trade muscles re-implement the cluster, the fleet, the power or the cooling, they stand on the spine.

## What the spine is made of

| Family | Muscles | Plant model | Native controller class | The knob |
|---|---:|---|---|---|
| Kubernetes Workload Scaling | 32 | compute pool (server) | the pod autoscaler, KEDA, the operator's rightsizers | replicas, targets |
| Container Resources | 25 | compute pool (server) | the vertical autoscaler, the scheduler's requests and limits | capacity, admission |
| Kubernetes Placement & Scheduling | 21 | compute pool (server) | the scheduler, descheduler, topology and affinity rules | admission, capacity |
| Node Fleet & Karpenter-Class Control | 24 | compute pool (node) | the cluster autoscaler, Karpenter-class provisioners | machines |
| Cloud VM & Capacity | 21 | compute pool (node) | the cloud's own scaling sets and capacity reservations | machines |
| Host CPU & Memory | 26 | compute pool (CPU host) | the kernel's frequency governor, memory and cgroup controls | capacity, power |
| GPU Hardware | 22 | compute pool (GPU) | the card's firmware: clocks, power limit, partitioning | clock ceiling, power cap |
| Network Routing & Switching | 19 | compute pool (network) | routing, queueing and buffer controls | capacity, admission |
| Storage Block/File/Object | 20 | compute pool (storage) | tiering, caching and throughput controls | capacity, admission |
| Observability & Telemetry | 9 | compute pool (server) | sampling, retention and scrape controls | admission |
| Reliability, Security & Recovery | 12 | compute pool (server) | disruption budgets, recovery and admission controls | admission |
| PDU, UPS & Electrical Distribution | 18 | energy storage (UPS) | the UPS and PDU controllers, their reserves and line limits | power, setpoint |
| Cooling, Chillers & Thermodynamics | 18 | thermal zone (data hall) | the chillers, air handlers and their setpoints | setpoint |

Two hundred and sixty-seven muscles in thirteen families: 156 capacity knobs, 48 admission knobs, 35 power knobs and 28
setpoints. Every one is listed, with its knob, in `docs/REALM_MUSCLES.md` (the spine first), and explained, wired and carded
in `docs/MUSCLE_CATALOG.md` (the manuals' muscle appendix, with every family's wiring recipe from `docs/wiring_recipes.csv`:
the native controller, the wire out, the wire in, the restore, and whether the wire has run live in this repository or only
on a model). The muscles of the spine's Kubernetes families are the ones the live Kubernetes benchmarks run on real
clusters (evidence class L); the spine as an organism is modelled (class S), and nothing in it is presented as proof of a
real stack.

## Why the spine is an organism

An **organism** is a set of muscles stepped on one clock, each from its own plant model with its own native controller,
the whole fed one demand from one seed, so that the heat the machines make is load on the rooms, the power swing of the
body is load on every site's line, and one brain judges every step against every other muscle's cushion. Run alone, the
spine is a data center with nothing of any one trade in it: clusters, fleets, processors, cards, network, storage, power
and cooling, and the governor on top of their native controllers. Three readings come from it that the realms alone cannot
give:

1. **The base before the trade.** Whether Omni-Compass helps the machines every stack runs on, before any realm's own
   muscles are put on them. A buyer wiring only a cluster and its site wires the spine and nothing else.
2. **What a trade adds.** Each realm's organism is its own families on the spine. Read beside the spine's reading, a
   realm's reading shows what that realm's trade muscles add to, or take from, the base they stand on.
3. **The same base under four trades.** The four stacked carry the spine once in each realm's body, the tower carries it
   once in all. The spine run alone is the control for both: the same muscles, the same native controllers, no trade on
   top.

The spine is run under the same three loads as every organism (its own load; the climb, 1 2 3 2 3 4 …; work waiting in
line), is judged by the same rule (work, speed and misses against native, the energy the max takes shown as power given), and
has the same two arms and no other: **native**, every native controller alone, and **omni**, Omni-Compass on top of those
same controllers, moving only the settings they expose, within their own ranges, and handing every setting back at the end.

## How the spine is wired on a real stack

The spine is wired as any organism is: one governor per body, every shared resource a muscle or a gauge, a muscle with
nothing to gain kept wired and watched (the Operator's Manual, chapter 2). The order is the order of the levels in the
Operator's Manual, chapter 6, which is the order of the spine's own families: the cluster first (its workloads, then their
resources and placement, then the machines under them), then the processors and the cards, then network and storage, then
the site under all of them (electrical distribution and cooling), with observability and recovery wired from the first
level, because the governor reads through them. Each family's wire is one row of `docs/wiring_recipes.csv`: which native
controller owns the setting, where the reading is tapped, where the setting is written, and how it is restored. A realm's
own muscles are wired after the spine they stand on, never instead of it.

## The spine in the runners and the pages

The organisms are groupings of catalog rows made in the runners; no engine file names them, so the spine entered the runners
without changing the engine that stands (`python3 tools/omni_version.py` prints the same fingerprint before and after). In
every runner the spine is `spine`; in `tools/run_scale.py` and the grid conductor (`scripts/dispatch_grid.py`) it is
organism **7**, after the six that were numbered before it, so that every grid run already started reads back under its
own number. Every table lists the spine first, because the other six stand on it.

| Where | The spine |
|---|---|
| `tools/run_realms_v5.py` | every muscle alone, then the seven organisms under three loads; the spine's row first in every organisms table (`results/realms_v5/REALMS_V5.md`) |
| `tools/run_scale.py --organisms 7`, workflow `six` | the spine at 1, 10, 100 and, on GitHub's own machines, 1,000 copies, over 1 to 1,000 paired runs |
| `tools/run_kil.py --organism spine`, workflows `six-kube`, `aks-metered`, `gke-metered`, `eks-metered`, `cloud-organism` | the spine with the real Kubernetes cluster inside it as one more muscle |
| `tools/run_hil.py` | the spine with the real card inside it (the GPU Hardware family is a spine family) |
| `scripts/dispatch_grid.py` | the spine's squares started, read back and never started twice like every other organism's |
| `docs/REALM_MUSCLES.md`, `docs/MUSCLE_CATALOG.md` | the spine's 267 muscles listed first; each muscle's organisms column names the spine |
| `results/realms_v5/`, `results/grid_v5/`, `docs/STATE_OF_PLAY.md` | the spine's readings, native against Omni-Compass on top, each named for the engine it ran on |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
