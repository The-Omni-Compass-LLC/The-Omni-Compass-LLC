# History

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Earlier states of play, kept whole. Nothing here is current status; the current state is `docs/STATE_OF_PLAY.md`.

---

## State of play as written on 27 September 2026 (with the update of 28 September)


> **Superseded for live results.** The live evidence below predates sets 19 and 20. The current live table is `results/live/LIVE_PAIRED.md`; energy on kind is a declared model, not a meter. The first metered test is `scripts/gpu_paired.sh` (`docs/GPU_BENCH.md`).


> **Update, 28 September 2026.** Added since this page was written, each with its evidence:
> - **Live, set 21** (conveyance only when response time needs it): p95 -37%, machines in service -21%, CPU used +26%
>   (unchanged from set 20; its source is still open). `results/live/LIVE_REPS_21.md`.
> - **GPU governor bounded** (0.70 share floor, busy gate, 2 s decisions): on the MLPerf-calibrated modelled card,
>   +5.1% and +1.3% work per kJ with p95 within +10% (the old governor failed that guardrail at +31% and +66%).
>   Model only. `results/gpu/sim/`.
> - **Speed lock** (opt-in): speed won elsewhere spent on GPU watts, every gauge kept at least 1% faster than
>   without Omni. Model only. `results/gpu/sim/pipeline/`.
> - **CPU and GPU on one conserved power budget** (conveyance law over CPU and GPU organs): +1.4% to +5.7% work
>   served against today's fixed caps, never over the site budget. Model only. `docs/CONVEYANCE_LAW.md`,
>   `results/hardware/NODE_EXCHANGE_*.json`.
> - **The manual in the box:** `docs/INTEGRATION_MANUAL.md`; every gauge: `docs/METRICS_CATALOG.md`; against what runs
>   today: `docs/COMPARISON.md`.

This is the whole repository at the commit named in `STATE_OF_PLAY_COMMIT.txt`. Everything below can be rerun from it.

**Run it live on real Kubernetes yourself:** on any machine with Docker, kind, kubectl and Python, run
`bash RUN_LIVE.sh 3`. It builds a fresh 7-node cluster per arm, runs native, Omni on top and Omni alone, and writes
`live_runs/LIVE_REPS.md`. GitHub Actions runs the same comparison with a pushed commit whose message contains `[reps]`.

**Rerun the whole thing:** `pip install -r requirements.txt && python verify.py`. It must end
`VERIFICATION: PASS`, and it does at this commit.

## Best measured results, and where each one comes from

| Claim | Evidence | Where |
|---|---|---|
| **B (Omni on top of each platform):** 0 losing cells on held-out scenarios; strictly GAIN on 27 of 28 platform-workload pairs | simulation, pre-registered | `tuning/B_FIX.json`, `tuning/B_TONE_HELDOUT.json` |
| **Four-cluster sites:** B 0 losses on all 7 platforms; C 0 losses vs GKE, AKS/Karpenter, CAST AI, Spot | simulation, held-out | `tuning/SITE_LEAGUE.json` |
| **C (Omni alone), one global setting, 400 never-used scenarios:** 153 toward their aims / 174 equal / 37 LOSS or power given of 364 cells (Holm-corrected) | simulation, held-out | `tuning/CONFIRMATORY.json` |
| **C with nervous-system coordination, 400 fresh scenarios:** 151 / 173 / 40 | simulation, held-out | `tuning/CONFIRMATORY_COORD.json` |
| **Controllers fighting each other:** lowest of all 8 systems on web (0.07 per day) and four-cluster sites (0.56 per day) | simulation, held-out | same file |
| **Real demand, 1,052 recorded PlanetLab machines:** 0 losing cells of 91 | simulation on real traces | `tuning/PLANETLAB_LEAGUE.json` |
| **Faults** (machines dying, spikes, crash loops, noisy neighbours): fewest pages to a human, fastest recovery | simulation, 500 runs per workload | `results/protocol/` |
| **GPU power law** (engine cap over the MLPerf-measured performance law), against native at equal work: energy -27% to -33%, time over the heat limit -73% to -78% | simulation, held-out | `results/hardware/SUMMARY_HELDOUT.json` |
| **Site power exchange (conveyance law, manuscript Ch. 29-31):** 4 GPU groups under one site budget: 0 minutes over the site limit at 70/60/50% budgets (native 10.5/45.6/106); least energy at every budget; 31-115 fewer backlog minutes than the static split | simulation, held-out; law proved (conservation, Lyapunov, exponential convergence) | `docs/CONVEYANCE_LAW.md`, `results/hardware/SITE_EXCHANGE_HELDOUT_*.json` |
| **Same-tower OFF / observe / ON receipt:** observe identical to OFF; ON ahead of the graded-reflex comparison build on healthy time, recovery, energy, violations and peak power (peak below OFF) | simulation, held-out | `results/tower_off_on/`, `results/external_review/CHATGPT2_REVIEW.md` |
| **Live levers under the nervous system:** 19 of 19 checks on real Kubernetes; reset restores everything | live, kind | `results/live/LIVE_LEVERS_2_NERVOUS.txt` |
| **Shadow pilot kit:** a read-only identity made 0 writes across 40 decisions | live, kind | `results/live/LIVE_SHADOW_1.txt` |
| **Safety shield:** 2,000,000 adversarial cases, 0 violations (the test found 2 real bugs, both fixed); C++ twin matches | test | `tests/test_shield_properties.py` |
| **C++ engine:** 100,000,000 decisions, no failures, about 2.3 µs per decision | test | `results/SOAK.json` |

## What still loses, measured

- **C, typical response time, web and four-cluster:** about 20% slower than every platform. Omni fills pods to 80%,
  where the others stop at 70%, and trades response time for energy.
- **C, machine starts and stops:** loses to plain Kubernetes and OpenShift, which hold machines steady and pay for it
  in machine-hours.
- **C, GPU and batch:** energy 1-2% lower and power and heat margins 1-4% lower than the tight packers (AKS/Karpenter,
  CAST AI, Spot).
- **Live, set 3, with a working probe:**
  - Omni kept all 6 machines. Latency near the 500 ms SLO blocks machine release.
  - There is no significant difference from native on anything else, except that C has more waiting pods.
  - The earlier live machine savings (sets 1-2) are withdrawn, because the broken probe had blinded the latency sense
    (`results/live/LIVE_REPS_PROBE_DEFECT.md`).
  - Set 4's decision trail showed why. Latency spikes from pod saturation at load steps kept the service from being
    clean, and the engine's calm stayed under the machine threshold (0.65 against 0.7). Both are addressed by the
    attribution gate and the two-way wiring above; the live test is pending (`results/live/LIVE_REPS_4_DIAGNOSIS.md`).
- **A bound, not a loss:** no controller, even one with perfect foresight, can match both the tightest packer's
  machine-hours and the calmest autoscaler's churn at once (`tuning/bound.py`).

## Two-way nervous system (new, live test pending)

Manuscript Appendix J names delay and dropout handling and feedback interpretation as the nervous system's job. The
live controller now wires both directions (`docs/TWO_WAY_NERVOUS_SYSTEM.md`).

- **Blind senses are detected against the wall clock.** A hung probe was the root cause of the live set 1-2 error.
  - A blind sense feeds the engine's `stale` channel.
  - It blocks every give-back.
- **Commands are read back.** Drift feeds the engine's `drift_ratio`. No new machine release goes out before the
  last one has landed.
- **The machine organ has its own engine view and a release gate.** Pods move first, and the headroom proof uses the
  engine's rho.

**Tests:** 75,000 blind states, 200,000 gate states, 300,000 nervous-system states.

**Live sets 5 and 6 could not run.** From 03:51 UTC GitHub refused every job, including `verify`: runner ID 0, no
steps, failed within about 2 seconds. That is GitHub declining to start runners, which on a private repository is
most often exhausted Actions minutes or a spending limit. It is not a code failure. `python verify.py` passes
locally at this commit.

## What came from the other AI builds, and what was tested

- **ChatGPT** (`results/external_review/CHATGPT_RELEASE_REVIEW.md`):
  - Its recovery reflex overrides the power envelope. Head to head, this engine read GAIN on 11 gauges in its default
    mode and its reflex on 1. Not adopted.
  - Its CPU-frequency connector was adopted, wired under the nervous system with a schedutil floor and exact restore.
- **Grok** (`results/external_review/GROK_HARNESS_REVIEW.md`):
  - It found that the GPU arms B and C were collapsed in the hardware plant. That is a real bug.
  - The fix was combined with the engine cap into one law, which beats both versions.

## Map

| Path | What it is |
|---|---|
| `omnicompass/core.py`, `cpp/` | six-state engine; C++ twin |
| `omnicompass/closure.py` | closure law: forward projection, boundary correction, turning point, muscle tone |
| `omnicompass/nervous_system.py` | one engine state grants each organ its authority and envelope |
| `omnicompass/shield.py` | safety shield, downstream of everything |
| `omni_controller/` | live Kubernetes controller and levers |
| `fleet/`, `hardware/` | simulation plants |
| `tuning/` | benchmarks, pre-registrations, results |
| `results/live/` | every live run, including the failed and withdrawn ones |
| `docs/history/OMNICOMPASS_BUYER_EDITION.md` | the buyer-facing report |
| `docs/history/CONSENSUS_AUDIT.md` | the five-reviewer audit (written inside the project; internal, not independent) |


## The state of play as it stood on 2026-10-10 (Omni v3), moved whole on 2026-10-16

Kept as its own page, `docs/history/STATE_OF_PLAY_2026-10-10.md`: the 10 October narrative, every number Omni v3's, named as such.

## The state of play as it stood on 2026-10-06 (moved here whole on 2026-10-07)

## In one paragraph (2026-10-06, Omni v1)

**Omni v1, the same in all three of our runs.** On real Kubernetes, every test ran three times as separate GitHub runs on the frozen
engine, ten pairs each (`docs/OMNI_V1.md`, the six `results/live/V1_*.md` tables). Work inside the response line **+42%
to +48%** in all three runs of the all-four test (18.6 → 27.6 requests a second in run A), GAIN in all three of our runs; the 95th
percentile **−57% to −69%** in every run of the steady, wandering, all-four and fault tests, GAIN in all three of our runs; failed
requests −12% to −13% where load swings, GAIN in all three of our runs; machines −1.5% to −3.4% at steady load and −15% to −24% on
the batch queue, GAIN in all three of our runs, no difference beyond the noise elsewhere; energy a declared model (kind never powers a
machine down); beside a noisy neighbour, no difference beyond the noise on every row. **The Omni index on v1: +26.2%**
on real Kubernetes (`results/OMNI_INDEX.md`; only rows the same in all three of our runs count, a row inside the noise counts
as zero; Azure and the card join when their v1 runs land). The paragraph below is the earlier engine's reading, kept as
the record it was.

Omni-Compass sits on top of Kubernetes and hardware and gets more out of what is already there. On real Kubernetes,
the engine before v1 (the live controller at rules 1-8, commit `353903683009`), ten pairs per test, native against
compass with the same work sent to both:
**41.7% more work handled inside the response line on the same machines** (capacity, all four in one run), responses
**59-64% faster** at the 95th percentile (steady, wandering, all four, faults), 12% fewer failed requests where load
swings, energy equal or lower, and not one pod left without a machine. Machines: up to 2% fewer. Omni gives a machine
back only when a paired trial shows the service no slower without it, and on these clusters one machine fewer made
requests 30-45% slower in most trials, so it kept them and spent them on speed and work (earlier engines without that
check parked 29-36%: `docs/history/`). All of it together, real software on real computers (the software end, not bare metal and not the chip): **the Omni index +12.9%**
(`results/OMNI_INDEX.md`).

**Omni v1** (`docs/OMNI_V1.md`): the engine is frozen and fingerprinted (`OMNI_V1.json`), and every test above runs
three times on it, as separate GitHub runs (A the result, B and C the replications); each table reads GAIN in all three of our runs,
LOSS in all three of our runs, no difference beyond the noise, or the runs disagree, and replaces the earlier engine's table as it
lands. Running on v1 now: the Kubernetes suite three times, the batch test, the six organisms at 1, 10, 100 and 1,000
copies with the real cluster inside, the big organisms on rented Azure machines, the Azure steady and burst bill tests,
CityLearn, and the power grid.

**What is shown and what is not.** Shown: more work inside the response line on the same machines (34-52% across the
three capacity runs on earlier engines) and a faster tail, on real Kubernetes. Not yet shown: an energy or cloud-bill
saving on real machines. On kind the machines are containers on one runner, so a machine out of service saves modelled
watts, not a metered bill, and Azure's bill did not move on the earlier engine (`results/live/AKS_BILL.md`); the v1 Azure
runs are the test of that. The current card governor has not run on a real GPU.

The card: the first real run (NVIDIA A10, 2026-10-02) used a card controller since replaced; it is not a result to
stand on. In simulation the current controller (amendment 12) is clearly faster under an operator's power cap (p95
6-7% faster, time over the line 1 point lower) and saves 0.5-3.7% energy on the card's own firmware with p95 even
(`results/sim/gpu_two_wire/`). The real card runs next: one card, the card inside the six organisms, then eight cards.

The 945 muscles (Omni v2; 656 in v1) are models of real control systems. With the real cluster or the real card inside, they show the
mechanism (work the same, energy 0.1-0.2% lower, time over the line lower than native in every organism); they are
never counted in the headline.

| Test (real) | Work | Speed | Machines | Energy | Source |
|---|---|---|---|---|---|
| All four in one run: load up and down one step at a time, 10 pairs | **+29%** | p95 -62% | **-3.6%** | -0.3% | `results/live/ALL_FOUR.md` |
| Capacity, load rising, 10 pairs | **+48%** | p95 -50% | -1% | -0.3% | `results/live/AMENDMENT_3_RUNS.md` |
| Sets 22-27, same work, 10 pairs each | same, none failed | p95 -55% to -65% | **-29% to -36%** | -0.1% to -0.5% | `results/live/LIVE_REPS_22.md` to `results/live/LIVE_REPS_27.md` |
| Six organisms, cluster inside, 5 pairs each | requests served +0.5% to +6% | p95 -24% to -40% | same to -2% | -0.1% to -0.6% | `results/live/SIX_KUBE.md` |
| Azure AKS, steady load, 5 pairs | same | p95 -20% | same | (billed) same | `results/live/AKS_BILL.md` |

All four in one run is done: every one a proven GAIN in the same run (`results/live/ALL_FOUR.md`). Running now: demand that wanders (up, spike, down, back up,
idle, 10 pairs), the Azure burst bill test, and the 1,000-copy grid of the six organisms on Lambda.

### The engine now, and what runs on it (2026-10-05)

The live controller is frozen at rules 1-8 (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendments 1-8): rules 5-8 were added
today (a pinned gauge is not a steady demand; coasting; cruise; the emergency brake). Every result above was measured on
an earlier version of the controller, and each names its commit. So that every number comes from one engine, the whole
Kubernetes suite runs again on the frozen engine: all four in one run, demand that wanders, the steady same-work set,
the fault and fairness tests, the batch test, and the six organisms at every size; the Azure burst bill test and the two
big organisms on rented Azure machines too. The card harness changed only in how it judges (amendment 11 of the GPU
preregistration), so the single card and the eight cards run once, on this engine, on Lambda.

Back on the frozen engine so far, ten pairs each:
- **Faults** (`results/live/FAULTS.md`): p95 −60%, mean response −35%, time over the line −23%, pending pods −77%.
  Recovery is faster after every fault: machine down 42 s against 70 s, a blind probe 54 s against 66 s, a runaway pod
  98 s against 105 s, a spike the same.
- **Fairness** (`results/live/FAIRNESS.md`): a noisy neighbour on the same cluster. Mean response −15%, no LOSS,
  and the neighbour's own app never behind. The earlier engine scored −0.3% on the index here; this engine scores +5.6%.

Independent simulator: CityLearn round 1 split (the 2022 battery districts lower on bill -4% to -11%, electricity -9%
to -17%, carbon -7% to -14%; the 2020-2021 water-tank districts higher on peaks and ramping), the fix (only the electric
batteries are steered), and round 2 on every untouched district (`docs/CITYLEARN_PREREGISTRATION.md`).

### Measured on real systems: the newest set, Omni-Compass against Kubernetes as it runs today

**Set 24 (2026-10-02, commit `c908054`) repeats it again: machines in service −31.6%, p95 −60.1%, p99 −64.1%, HPA
replicas −38.6%, 0 failed requests, total CPU including Omni-Compass's own −1.8% (not significant)**
(`results/live/LIVE_REPS_24.md`). Set 23 before it: p95 −62%, replicas −37%, pod starts −64%, 0 failed requests, no
energy or total-CPU difference (`results/live/LIVE_REPS_23.md`). The set-22 table below stands as first measured.

Set 22 (`results/live/LIVE_REPS_22.md`): 10 paired repetitions on real Kubernetes (kind), each pair on one machine,
Kubernetes with its autoscaler alone against the same Kubernetes with Omni-Compass on top. The load is sent at a fixed
rate, so both arms were given **the same work**.

| Result | Kubernetes alone | With Omni-Compass | Change (95% interval) |
|---|---:|---:|---|
| **Energy, parked machines still on at idle power** (declared model, no meter) | 160.3 Wh | 160.1 Wh | **−0.1%, no difference** |
| **Response time, 95th percentile** | 407.9 ms | 158.8 ms | **−61%** (proven) |
| Response time, 99th percentile | 639.4 ms | 245.1 ms | −62% (proven) |
| Response time, mean | 179.9 ms | 98.4 ms | −45% (proven) |
| Failed requests | 0 | 0 | equal |
| Pods waiting to start, pod-minutes | 0.265 | 0.025 | −91% (proven) |
| Replicas, mean | 8.93 | 6.91 | −23% (proven) |
| Machines in service, mean (all stayed powered) | 6 | 4.14 | −31% (proven) |
| CPU used by the service | 1.036 cores | 0.957 cores | −7.6% (proven) |
| Omni's own CPU (its controller and every command it ran) | 0 | 0.070 cores | +0.070 (proven) |
| **CPU used, service and Omni together** | 1.036 cores | 1.026 cores | **−0.9%, no difference** |

- **Same work, much faster answers**, with no failed requests and far less waiting.
- **No energy saving is shown on kind.** Every machine stays powered; energy is a declared model, and counted at the
  idle power a parked machine really draws it is unchanged.
- **No CPU saving once Omni's own cost is counted.** The service used 7.6% less CPU; the controller spent almost all
  of it. Cutting the controller's cost is the next improvement.
- The reset restored every setting in every run.

### Kubernetes sets 25 and 26 (2026-10-02, 10 paired repetitions each, equal work)

| Run | Machines in service | p95 | Failed | Total CPU incl. Omni's own | Receipt |
|---|---:|---:|---:|---:|---|
| Set 25, the engine's allocation law | **−32.3%** | **−57.3%** | 0 / 0 | −0.6% (not significant) | `results/live/LIVE_REPS_25.md` |
| Set 26, the engine's allocation law | **−35.8%** | **−55.4%** | 0 / 0 | −1.5% (not significant) | `results/live/LIVE_REPS_26.md` |
| Set 26, **the compass law in the live controller** | **−17.2%** | **−64.8%** | 0 / 0 | +1.0% (not significant) | same; label by the preregistered rule: **fewer machines within the band** |
| Set 27, the engine's allocation law | **−36.6%** | **−53.1%** | 0 / 0 | −0.0% (not significant) | `results/live/LIVE_REPS_27.md` |
| Set 27, **the compass law aligned with the GPU governor** | **−15.9%** | **−65.5%** | 0 / 0 | +0.2% (not significant) | same; label by the preregistered rule: **fewer machines within the band** |

Set 27 (running): the compass in the live controller reads the service as the corrected GPU compass does (mean response time,
center 0.4), against native and the allocation law (`docs/K8S_COMPASS_PREREGISTRATION.md`).

### Measured on a real GPU: the card's own meter (evidence class P)

**First counted run, NVIDIA A10 on Lambda, 2026-10-02** (`results/gpu/run-20261002T082232Z/GPU_REPS.md`, 10 paired
repetitions × native / watch / Omni, 600 s each, frozen at commit `c908054`, checksums verified). Wire check 7 of 7;
2,144 writes, none refused, every one read back, every arm ended at the start limit; watch equal to native.

| Gauge | Native | Omni | Change (95% interval) |
|---|---:|---:|---|
| **Work per energy** (requests per kJ) | 50.79 | 52.62 | **+3.6% (+2.7% to +4.5%), proven** |
| GPU energy | 69,180 J | 66,790 J | −3.5%, proven |
| Requests served / not served | 3,514 / 0 | 3,514 / 0 | equal |
| **Response time, 95th percentile** | 510 ms | 809 ms | **+58.5%, higher, proven** |

**Result, by rule: ENERGY IMPROVEMENT WITH SERVICE TRADEOFF** (the p95 guardrail of +10% failed). The six organisms
with the same card inside (`results/hil/run-20261002T082232Z/HIL.md`, 3 repetitions each): the card's work per energy
+1.6% to +2.8% in every organism, the same requests, its p95 500 to about 600-935 ms. The cause, from the card's own
samples, was wiring in the governor (amendment 6 of `docs/GPU_PREREGISTRATION.md`): busy bursts served at 736-768 MHz
against 861-889 MHz on its own. Corrected (amendments 6 and 7); the corrected governor has not yet run on a card.

### Simulated (models: they show the mechanism, not a measurement)

| Result | Where |
|---|---|
| GPU governor with share floor and busy gate (one wire, the power limit), MLPerf-calibrated card: +5.1% and +1.3% work per kJ, p95 within +10% | `results/gpu/sim/after` |
| **Two-wire GPU card under the compass law, corrected governor** (amendments 6-7), 10 seeds and 10 fresh seeds, geometric means: **service** profile work per energy **+6.9% / +3.8%**, energy −6.4% / −3.7%, p95 **−5.9% / −2.3%** (faster), time over the line −0.03 / −0.04 pp; **batch** profile +8.1% / +4.2%, p95 +7.0% / −2.3%; the one-wire governor +0.1%; both wires restored every seed | `results/sim/gpu_two_wire/RESULT.md`, `fresh/` |
| **The six organisms** (Compute 345, Physics 262, Energy 282, Distribution 337, the four stacked 1,226, the whole tower 656), native against the compass law on every muscle, 1,000 paired runs at 1× and at 10× size: work per energy +0.20% to +0.30%, energy −0.21% to −0.32%, work −0.01% to −0.02%, time over the service line **+0.19 to +0.27 pp in every cell (band first not held)**, every knob handed back. 100× and 1,000× are running | `results/scale/GRID.md` |
| Speed lock (speed won elsewhere spent on GPU watts) | `results/gpu/sim/pipeline/` |
| CPU and GPU on one conserved power budget: +1.4% to +5.7% work served against a fixed cap, never over the budget | `results/hardware/NODE_EXCHANGE_*.json`, `docs/CONVEYANCE_LAW.md` |
| GPU groups sharing a site budget: 0 minutes over the budget | `results/hardware/SITE_EXCHANGE_HELDOUT_*.json` |
| Platform leagues, faults, PlanetLab traces, stack benchmark | `tuning/`, `results/protocol/`, `results/` (see `docs/history/BENCHMARK_REPORT.md`) |
| **The 656-muscle tower as organisms**, round 3 (preregistered, 10 seeds; every realm carries the shared spine; Omni as the shipped controller commands): the whole tower native against one governor on top, work per energy **+0.1%, SUPERIOR WITHIN GUARDRAILS**; inside the realms the spine costs service: Energy +0.2% with +1.9 pp violations (tradeoff), Compute 0.0% (+2.1 pp, not established), Distribution −0.1% and Physics −0.7% (**AWAY FROM ITS AIM**). Rounds 1 and 2 kept, superseded | `results/realms/REALMS.md`, `docs/REALM_MUSCLES.md` |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
