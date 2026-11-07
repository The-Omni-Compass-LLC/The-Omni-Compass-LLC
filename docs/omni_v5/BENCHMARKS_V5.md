# Omni v5 — every benchmark: where it runs, what it needs, what it costs, which law it runs (nothing left out)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every benchmark Omni-Compass has, in one map, with **one button that starts them all**:
`.github/workflows/v5-all-benchmarks.yml` (Actions → v5-all-benchmarks → Run workflow). By default it starts every free
benchmark on GitHub's own machines; the GPU runner and the paid clouds start only when you choose them **and** their
secrets are in place (a missing secret is reported and skipped, never billed). Credentials live only in GitHub secrets.

## First, the plain truth about which law each benchmark runs today

- **The v5 law runs today in the modelled realms** (`tools/run_realms_v5.py`, workflow `realms-v5`): 1,097 muscles in 70
  families, all six organisms *superior within guardrails*, **0 muscles behind native**; the whole tower saves 0.99% of its energy against v3's 0.33% on the same seeds (3.0 times), the four stacked 0.99% against 0.33% (3.0 times), Energy / Facility 1.00% against 0.33% (3.0 times)
  (`results/realms_v5/REALMS_V5.md`). Evidence class **S** (modelled): a model is not proof.
- **Every live benchmark** (real Kubernetes, the GPU, the clouds, the six organisms with a real cluster or card inside)
  now runs v5: the live Kubernetes controller's compass law and the GPU governor hold their balance point at the v5 edge
  (`omnicompass/edge.py`, the same code the modelled law uses), with their own measured guards (the verdict on every
  machine given back or clock step taken, the release gate, the shields); the six organisms with a real cluster or card
  inside run the v5 law on the v5 catalog, and their four stacked keep each realm's own body. Each live benchmark is
  rerun on v5, A/B/C, and the founder hears each result before it goes up. The databases' own adapters (PostgreSQL,
  MySQL, MongoDB, Redis, Kafka) keep their live laws until their own v5 port (stage 11).

## A. The v5 law, modelled (free, on GitHub)

| Benchmark | What it measures | Workflow | Cost |
|---|---|---|---|
| Realms on v5 | every one of the 1,097 muscles alone and the six organisms, native vs the v5 law, seeds 3000–3009, the no-harm check | `realms-v5` | free |

## B. Free benchmarks on GitHub's own machines (23, all started by the button)

| Benchmark | What it measures | Workflow |
|---|---|---|
| Kubernetes, steady | Omni on top of the HPA and cluster autoscaler on a real kind cluster | `live-kind` |
| Kubernetes, every lever | the same with every Kubernetes lever wired | `live-kind-levers` |
| Kubernetes, full | the full Kubernetes set | `live-kind-full` |
| Kubernetes, shadow | Omni watching only (writes nothing) beside native | `live-shadow` |
| Kubernetes add-ons | Omni on top of KEDA and the other add-ons | `kind-addons` |
| Kubernetes at scale | 10 and 100 nodes (KWOK): decision time and correctness | `kwok-scale` |
| Six organisms | the six organisms at 1, 10 and 100 copies × 1, 10 and 100 runs | `six` |
| Six organisms, cluster inside | the six organisms with the real cluster inside | `six-kube` |
| Realms (v3 table) | v3's published 945-muscle table, reproduced | `realms` |
| Benchmark protocol | the paired protocol and its repetitions | `benchmark`, `benchmark-reps` |
| CPU power | the CPU frequency ceiling on Linux (cpufreq), energy from the processor's own meter | `cpu-power` |
| PostgreSQL | pgbench, Omni on top of the operator's settings | `pgbench` |
| MySQL | sysbench | `sysbench` |
| MongoDB | YCSB, the WiredTiger cache | `ycsb` |
| Redis | memory and eviction | `redis` |
| Kafka | messaging and streaming | `kafka` |
| Buildings and grid | CityLearn, on top of its baseline controllers | `citylearn` |
| Power grid | pandapower, the tap changer and the feeder | `pandapower` |
| Robot arms | MuJoCo Menagerie | `mujoco` |
| Drones | PX4 swarms | `swarm` |
| Robustness | Omni killed mid-run (the lease hands back), the long run, Omni's own cost | `robustness` |

## C. The GPU — one chip, the organisms with the card inside, eight chips, the APU

| Benchmark | What it measures | How it runs | Cost (check prices on the day) |
|---|---|---|---|
| GitHub GPU | native / watch / Omni on a real NVIDIA T4, energy from the card's own meter | `gpu-bench` (needs the `gpu-t4` runner) | billed per minute |
| One chip, the whole test | wire check, envelope, smoke, two preregistered counted runs (compute, AI token generation), the operator's power cap underneath, the fault drill, AI serving (vLLM) | `scripts/gpu_rented_run.sh` on a rented card (`docs/GPU_RUN_GUIDE.md`, C) | one A10 is about $0.75 an hour; the whole test is about 36 hours |
| The organisms with the card inside | the six organisms at 1, 10 and 100 copies on one clock with the real card inside (no 1,000 copies: the founder's order of 12 October) | step 8 of the one-chip and eight-chip runs (`tools/run_hil.py`) | inside the runs above |
| Eight chips | every card of one server at once, sharing its power and cooling, then one language model across all eight | `scripts/gpu_8card.sh` (`docs/GPU_RUN_GUIDE.md`, D), or one button: `lambda-gpu` (below) | 8×A100 about $14 an hour, 8×H100 about $24; full design 17–18 h, pooled 9–10 h, fast 3.5 h |
| AMD APU / AMD GPU | the same preregistered protocol on an AMD chip; on an APU the package's power (CPU and GPU together) | `scripts/apu_run.sh` (AMD's `amd-smi` through `scripts/apu/nvidia-smi`; checked by `tests/test_apu_shim.py`) | the machine's rate |

The standing order holds: GPU money is spent only after the CPU side is done, on **one exact commit** the founder is given,
with the click-by-click steps in `docs/GPU_RUN_GUIDE.md`.

### The 8-GPU benchmark, one button (Lambda)

The eight-chip run (and the one-chip test) can be started from GitHub without logging in to the machine. The workflow
`lambda-gpu` rents one Lambda machine, ships it the exact committed tree, starts `scripts/gpu_8card.sh` (or
`scripts/gpu_rented_run.sh`), watches it for up to 34 hours, brings every result file back as the run's artifact, and
**always gives the machine back**: when the run prints its last line, at the hour budget plus one hour whatever happens,
or at the very end of the workflow if anything before it failed. A dry run (the default) shows the price and rents
nothing. The launcher is `scripts/lambda_gpu.py` (tested against a stand-in for Lambda's API, `tests/test_lambda_gpu.py`);
the watch is `scripts/lambda_gpu_watch.sh`.

| Mode | What runs | Hour budget (given back by) | 8×A100 at about $14 an hour |
|---|---|---|---|
| `8card` `pooled` (default) | every stage, repetitions pooled across the cards | 10.5 h (11.5 h) | about $165 at most |
| `8card` `fast` | what only a full server shows | 4 h (5 h) | about $72 at most |
| `8card` `full` | the whole design | 26 h (27 h) | about $387 at most |
| `1card` `fast` | the compute counted run on one A10 | 8 h (9 h) | one A10 about $0.75 an hour: about $7 |
| `1card` `full` | the whole one-card test | 32 h (33 h) | about $25 |

The price shown by the dry run is Lambda's own, read at that moment; the table above is an example. GitHub's own minutes
for the watch are free on a public repository.

**Click by click (once):**
1. Lambda Cloud (cloud.lambda.ai) → **API keys** → **Generate API key** → copy it.
2. Lambda Cloud → **SSH keys** → **Add SSH key** → **Generate a new key** → name it (for example `omni-key`) → save the
   private key file it downloads.
3. GitHub → the repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**, three
   times: `LAMBDA_API_KEY` (the key from step 1), `LAMBDA_SSH_PRIVATE_KEY` (the whole private key file from step 2, opened
   in a text editor and pasted), `LAMBDA_SSH_KEY_NAME` (the name from step 2, for example `omni-key`).

**Every run:** GitHub → **Actions** → **lambda-gpu** → **Run workflow** → choose the branch → leave `dry_run` at `yes` the
first time and press **Run workflow**: the run's page shows the price per hour, where a machine is free, and the most it
can cost. To run for real, start it again with `dry_run` set to `no`. The results arrive as the run's artifacts; the
founder hears what they say before anything goes up.

## D. The metered clouds — Azure, Google, Amazon

| Cloud | What it measures | Workflow | Secrets (names only) | Cost |
|---|---|---|---|---|
| Azure (AKS) | native Kubernetes against Omni on top, the bill counted every 15 s at the list price | `aks-metered` | `AZURE_CREDENTIALS` | about $0.096 per worker-hour (Standard_D2s_v4) |
| Google (GKE) | the same design on Google Kubernetes Engine | `gke-metered` | `GCP_CREDENTIALS`, `GCP_PROJECT` | about $0.067 per worker-hour (e2-standard-2) |
| Amazon (EKS) | the same design on Elastic Kubernetes Service | `eks-metered` | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | about $0.096 per worker-hour (m5.large), plus about $0.10 an hour per control plane |
| Big organisms, Azure | the whole tower and the four stacked at up to 100 copies (no 1,000 copies from 12 October; the grid runs every square on GitHub's own machines), the real cluster inside, on a rented 8-processor Azure machine | `big-organism`, `big-organism-detached` | `AZURE_CREDENTIALS` | about $0.35 an hour (Standard_D8as_v4), about $7 to $14 a machine |
| Big organisms, Google | the same test on a rented Google machine | `cloud-organism`, cloud `gcp` | `GCP_CREDENTIALS`, `GCP_PROJECT` | about $0.27 an hour (e2-standard-8), at most about $10 for its 39-hour ceiling |
| Big organisms, Amazon | the same test on a rented Amazon machine | `cloud-organism`, cloud `aws` | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | about $0.38 an hour (m6i.2xlarge), at most about $15 for its 39-hour ceiling |

The Google and Amazon runs are written to the AKS run's design (`scripts/gke_paired.sh`, `scripts/eks_paired.sh`; the big
machine: `scripts/cloud_machine.py`, `scripts/organism_detached.sh`, the same test as Azure's) and have not yet run: their
first repetition is a shakedown, and any arm that fails its own checks is marked INVALID and never counted. Each cluster
is deleted when its arm ends, and every cluster a run made is deleted at its end whatever happens; a rented machine is
given back when its test ends, at its hour ceiling, or at the end of its workflow whatever happens. Setting up each cloud,
click by click: `docs/AZURE_SETUP.md`, `docs/GOOGLE_SETUP.md`, `docs/AMAZON_SETUP.md`. What runs where: the managed
Kubernetes bill and the biggest organisms need a cloud; every other benchmark (robot arms, drones, buildings, the grid, the
databases, the messaging, the modelled realms and the grid of organisms) runs on GitHub's own machines, the same code on
every engine, free.

## E. How to start them

1. GitHub → the repository → **Actions** → **v5-all-benchmarks** → **Run workflow** → choose the branch.
2. Leave **free = yes** for everything on GitHub's machines. Type `aks,gke,eks` under **clouds** only once those secrets
   are in place, and `gcp,aws` under **big_machines** for the big organisms on Google's and Amazon's machines. **gpu = yes** only once the GPU runner exists. Type `8card` (or `1card`) under **lambda_gpu** only once
   the three Lambda secrets are in place; it starts the rented-machine run for real (pooled), so try `lambda-gpu` with its
   own dry run first.
3. Each benchmark runs as its own workflow and writes its own table; nothing is published until the founder has heard it.

© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercialization or
monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the
USA. www.omni-compass.com

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
