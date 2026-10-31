# Omni-Compass: the state of play as it stood on 16 October 2026 (omni-v7), moved here whole on 17 October

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Moved here whole from `docs/STATE_OF_PLAY.md` on 17 October 2026 when the page was rewritten for the engine that stands (omni-v8). Every number below is named with the engine it ran on (omni-v7, omni-v6 or omni-v3); the tables it cites stay in `results/` under their engine's name and run again on the engine that stands.

## In one paragraph (2026-10-16, the engine that stands is omni-v7)

**The engine that stands is omni-v7** (`OMNI_V7.json`, digest `d6d467b824c585f1`, 46 files; `docs/OMNI_V7.md`), on main since
16 October by the founder's order: the v5 law at the max on the 1,107-muscle catalog with every muscle's own card, the shared-host
capacity repair in the Kubernetes controller, conveyance bounded by each namespace's CPU quota (an unreadable quota is no budget
known, Kubernetes admission is the authority), the verdict reading a trial in the reports' words, every rule in seconds, the
cloud's rule as one flag. Its first trials as pushed on 15 October found a fault in its quota budget (an unreadable ResourceQuota
read as a zero allowance, so conveyance never raised a limit), fixed on 16 October in the model gate first and then in the engine;
the corrected trials are its first runs (below). Every benchmark runs again on the engine that stands (`scripts/reruns.txt`,
released a few a tick by the grid conductor, A of every benchmark, then B, then C; the grid and every Azure set restarted on it
the same day); every row stands as its own engine's result (omni-v6 for the four Kubernetes add-on tables of 15 October, omni-v3
for the rest, named in its Engine column on `docs/BENEFIT_SHEET.md` and in the standing block above) until its three runs on v7
land. Results are never read across engines. The standing block at the top of this page is written from the result files by
`tools/summary.py --fix` and checked on every push; the prose below says the same in words.

**On omni-v7, the engine that stands, real Kubernetes (evidence class L), ten pairs × three runs each**
(`results/live/V7_*.md`, runs 38843260818 to 38843289946, every one omni-v7; no row reads LOSS on the three-run rule):

- **A service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top** (`V7_GOLDILOCKS.md`): response time
  **−45% to −47% mean, −60% to −62% at the 95th percentile, −67% to −69% at the 99th**, time over the response line −100%,
  GAIN in all three of our runs; machines (node-hours) and failed requests STEADY; replicas, pods started, pod start wait and
  alert minutes STEADY (each clear of the noise in one run only, and there on the GAIN side except replicas +3.4%, power given);
  parked-worker energy +1.6% to +2.3%, power given; 14 to 18 settings commands a run. One number: **+18% GAIN, power given**.
- **KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top** (`V7_KEDA_REQUESTS.md`): response time **−57% to
  −58% mean, −71% to −75% at the 95th percentile**, time over the line −94% to −95%, alert minutes **−93% to −96%**, HPA
  replicas **−15% to −19%**, pods started **−17% to −23%**, all GAIN in all three of our runs; machines and failed requests
  STEADY; parked-worker energy +2.2% to +2.3%, power given; 4 to 5 settings commands a run. One number: **+78% GAIN, power given**.
- **KEDA on the CPU target and the live requests in flight, Omni-Compass on top** (`V7_KEDA_CPU_REQUESTS.md`): response time
  **−36% to −38% mean, −52% to −54% at the 95th percentile, −57% to −59% at the 99th**, time over the line −98% to −100%,
  GAIN in all three of our runs; machines, failed requests, replicas and alert minutes STEADY; parked-worker energy +1.1% to
  +1.7%, power given; 17 to 20 settings commands a run. One number: **+45% GAIN, power given**.
- **A service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top** (`V7_CRUISEKUBE.md`): every
  gauge STEADY; CruiseKube's own rightsizing leaves Omni-Compass nothing to move and it wrote no setting. Run A alone read the
  99th percentile +3.1% and run B the node-hours +1.0%, each inside the noise in the other two runs. One number: **0%, STEADY**.
- **Fixed capacity, four CPU caps, Omni-Compass on top at native's cap** (`V7_CAPACITY.md`): completed work and work inside the
  response line STEADY at every cap (run A alone read +3.8% completed work at 1 core, inside the noise in B and C): the cap is a
  quota on the service's CPU and blocks the one lever Omni-Compass has there.

**On omni-v6, the engine of 15 October, real Kubernetes (evidence class L), ten pairs × three runs each** (`results/live/V6_*.md`;
that engine's own record, run again on v7 above):

- **A service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top** (`V6_GOLDILOCKS.md`): response
  time **-45% to -47% mean, -58% to -61% at the 95th percentile, -65% to -69% at the 99th**, time over the response line
  -99% to -100%, GAIN in all three of our runs; machines, node-hours, failed requests and the alert minutes STEADY; the
  parked-worker energy +1.8% to +2.7%, power given; HPA replicas STEADY. One number: **+54% GAIN, power given**.
- **KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top** (`V6_KEDA_REQUESTS.md`): response time
  **-59% mean, -73% to -75% at the 95th percentile**, time over the line -97% to -99%, alert minutes -98% to -100%, HPA
  replicas **-11% to -18%**, all GAIN in all three of our runs; parked-worker energy +1.6% to +2.1%, power given. One
  number: **+105% GAIN, power given**.
- **KEDA on the CPU target and the live requests in flight, Omni-Compass on top** (`V6_KEDA_CPU_REQUESTS.md`): response
  time **-37% to -41% mean, -55% to -57% at the 95th percentile, -59% to -63% at the 99th**, GAIN in all three of our
  runs; machines, failed requests, alert minutes and replicas STEADY; parked-worker energy +1.2% to +1.6%, power given. One
  number: **+15% GAIN, power given**.
- **A service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top** (`V6_CRUISEKUBE.md`):
  every gauge STEADY, no difference beyond the noise: CruiseKube's own rightsizing leaves Omni-Compass nothing to move on
  this service. One number: **0%, STEADY**.

In every one of these the governor ran on autopilot: no person touched a setting in either arm; the settings commands it
wrote on its own (15 to 17 a run on Goldilocks and on KEDA with the CPU target, 4 to 5 on KEDA's HTTP add-on) are in each
run's audit with their reasons, and the alert minutes (a whole minute over the line, when an on-call page would be open)
are judged in every table.

**Still on omni-v3, each named as that engine's result and queued to run again on v6** (`docs/BENEFIT_SHEET.md`): the
seven real-Kubernetes demands (steady +31%, faults +37%, wandering +37%, all four at once +42%, a queue of jobs +16%, the
Google day of 2011 +46%, all GAIN; a noisy neighbour STEADY), the five live stacks (PostgreSQL +0.9% GAIN with power given,
MongoDB +1.7% GAIN, Kafka +0.1% GAIN, MySQL STEADY, Redis STEADY), robustness (the governor killed mid-run +8.6% GAIN; the
two-hour run STEADY), the six organisms with the real cluster inside at 10 and 100 copies (+5.3% GAIN, power given), the
big organisms at 1,000 copies on Azure (+155% GAIN), the modelled tower of that engine's 945 muscles (+0.3% GAIN), the robot
arms (+3.8% GAIN), the power grids (+5.8% GAIN, power given), the drone swarms (+5.9% GAIN) and the buildings with batteries
(+0.8%, GAIN AND LOSS: the bill in the 2023 districts read power given), and the Omni index over the real tests (+5.2% GAIN,
power given). None of these is shown in front of a v6 result, and none is read beside one.

**The muscles and the seven organisms, modelled (evidence class S, our own models, never counted in the headline)**, on
the engine that stands, omni-v7, at the max (run again on 16 October, commit `1637d32cd26c`, with the spine as the seventh
organism; every reading reproduces the 13 October table to the digit): 1,107 muscles in 70 families (`realms/catalog_v5.csv`),
every muscle its own card (`realms/muscle_cards_v5.csv`), every muscle alone over its loads STEADY 580 and GAIN 527, LOSS 0; every
one of the seven organisms (the spine 267, the muscles every stack runs on; Compute / AI / Cloud 540, Physics / Robotics /
Autonomous 404, Energy / Facility / Industrial 480, Distribution / Specialized 484, the four stacked 1,908, the whole tower
1,107) GAIN (fewer misses, and under the climb more work) under the normal, climb and line loads, not one plant with less work
or more misses in any of them, the power given +0.00% to +0.05%; the spine alone cuts its misses 6.1% under its own load, 7.9%
under the climb (with more work) and 8.8% with work waiting in line, power given +0.01% to +0.04%
(`results/realms_v5/REALMS_V5.md`, `docs/THE_SPINE.md`); the grid, 36 of 36 squares of 10 and 100 runs GAIN with the six
organisms run so far alone and, with the real cluster inside, the organism's time over the line GAIN in 36 of 36; the spine's
squares are in the conductor's queue (`results/grid_v5/GRID.md`). Every
muscle is written out, organism by organism, the spine first, in `docs/REALM_MUSCLES.md`, and explained, wired and carded in
`docs/MUSCLE_CATALOG.md` (the manuals' muscle appendix, with every family's wiring on a real stack from
`docs/wiring_recipes.csv`).

**The cloud (Azure), the bill at native's work.** The founder's order of 14 October: in a cloud Omni-Compass shows one
thing, the same work as native for a smaller bill, at the tune-down on the machines alone. The sets ran at the tune-down on
14 October (steady, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real day on 1 to 9; `aks-metered`, every run's title
carrying `dial save`), and a full-wiring burst (`aks-metered-full`, the pod autoscaler moved too) ran on 15 October; their
receipts are archived by this push and their tables follow, each on the engine it ran on. The only Azure tables up so far
are v1's 4-worker fleet (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): every gauge STEADY, a fleet too small to show
one machine. Google (GKE) and Amazon (EKS) are built (`gke-metered`, `eks-metered`; the Operator's Manual's appendices G
and H, click by click) and run only when the founder opens the accounts and says so.

**The card (evidence class P)**: every earlier card result is obsolete; the founder's runs on rented cards come after the
CPU and cloud work, at one named commit. **Linux's own CPU governor and meter** (`cpu-power`): built and preregistered; it
waits for a machine on the metal, because GitHub's machines are virtual and expose neither.

**What is shown and what is not.** Shown, on the engine that stands and on real Kubernetes: a faster tail and more work
inside the response line on the same machines, on top of the operator's own rightsizers and autoscalers (Goldilocks, KEDA),
three times each. Shown on the older engine and queued to run again: the same on seven demands, memory and connections
given back on real databases and a broker at no measured cost, the governor's hand-back when killed. Not yet shown: an
energy or cloud-bill saving on real machines (energy on kind is a declared model; the Azure tables at the tune-down are
being made), and anything on a real card.

## Open

1. **Every benchmark on omni-v7**: 4 of 26 benchmarks have their three-run table on it (Goldilocks, KEDA's two add-on tests,
   CruiseKube; the fixed-capacity test too, which carries no sheet row); the rest released A, then B, then C by the conductor
   from `scripts/reruns.txt`; each table replaces its older row on the sheet when its three runs land.
2. **The grid and Azure on omni-v7**: restarted on 16 October; the v6 shards still running and the queued Azure set finish and
   stand as that engine's record, nothing cancelled.
3. **Azure at the tune-down**: the receipts of 14 and 15 October into tables (archive requested), checked against the
   cloud model's finding that the machines-only setting barely cuts the bill while pods wait for a place.
4. **Google and Amazon**: on the founder's word; the accounts and secrets are his to make (appendices G and H).
5. **The card**: the founder's runs on Lambda, one exact commit, after the CPU and cloud work.
6. **Linux**: a machine on the metal for `cpu-power`.
7. **More room**: of the 159 muscles that read SAME AS NATIVE on omni-v7's realms table, the room search of 16 October
   (`docs/OMNI_V7.md`) found none under the max's gauges within each muscle's own knob: 147 have no native misses to cut and
   fixed work; the 12 battery power knobs miss only while the charge sits at the operator's reserve, which the power knob may
   not spend. Six process loops miss at most 0.56% of decisions: a card candidate for a later version. The 14 of 26 knob-cases
   on the real stacks that read watch stay the next engine's question, in the model gate first.
8. **Omni-Compass 1.0**: when the founder declares the engine final, the engine that stands then is published as 1.0 and
   the older fingerprints go to `docs/history` as the road to it.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
