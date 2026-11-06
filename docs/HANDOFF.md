# Handoff: where everything is and how to run it

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The full manual: the book `docs/OMNI_COMPASS_MANUAL.pdf` (built by `python3 docs/book/build_book.py`; text in `docs/book/OMNI_COMPASS_BOOK.md`), and the short manual `docs/OMNI_COMPASS_MANUAL.md`. Everything below is on `main`. Anyone (a person or another AI) can pick it up from here.

**Written on 6 October, on Omni v2, and kept for its commands.** The engine that stands is omni-v25 (`OMNI_V25.json`);
where everything stands now is `docs/STATE_OF_PLAY.md`, and the figure of record, the Omni index, is in `results/OMNI_INDEX.md`.

## The engine

| Piece | File | What it is |
|---|---|---|
| Frozen engine | `omnicompass/core.py`, `omnicompass/adapter.py` | the 8-equation core and the governor; unchanged, with its proofs |
| The compass (new engine layer) | `omnicompass/compass_law.py` | one smooth law for every muscle: pull to the middle of the band, push against drift, tanh-bounded, fail up past 95%; and the plug (cover, one restore point, foreign-writer rule) |
| Two-wire GPU governor | `omni_controller/gpu_compass.py` | the compass on a real card: clock ceiling (`nvidia-smi -lgc`, up wire) and power limit (`-pl`, down wire) |
| Wire check | `tools/gpu_wire_check.py` | proves both card wires follow, read back and go home before anything runs |
| Realm muscles under the compass | `realms/compass_arm.py` | the compass on every one of the modelled muscles |

## The organisms

Seven since 16 October (`tools/run_realms_v5.py`, `realms/catalog_v5.csv`): the spine (267 muscles, every muscle in all
four realms) · Compute (540) · Physics (404) · Energy (480) · Distribution (484) · the four stacked (1,908) · the whole
tower, every muscle once (1,107 in 70 families). On 6 October, on Omni v2, there were six: 1 Compute (430 muscles) ·
2 Physics (376) · 3 Energy (470) · 4 Distribution (440) · 5 the four stacked with every duplicate kept (1,716) · 6 the
whole tower, every muscle once (945) (v1 was 345, 262, 282, 337, 1,226 and 656). Each is run native, then with Omni on top.

## How to run each benchmark

**Real card + the six organisms with the card inside + card's counted run (Lambda, about 12 hours, one command):**
```
sudo pkill -f gpu_
cd ~/the-omni-compass
git pull
sudo nohup bash scripts/gpu_rented_run.sh > run.log 2>&1 &
tail -f run.log
```
It runs: wire check -> card smoke -> six organisms with the card inside (`tools/run_hil.py`) -> card's counted run, and
ends with `send this one file back: results/gpu/omni-gpu-<stamp>.tar.gz`. Finished when `pgrep -f gpu_rented_run`
prints nothing. Upload that file to GitHub, then terminate the Lambda machine.

**The six organisms, simulated, the 1 / 10 / 100 / 1,000 grid (GitHub, free):** Actions -> `six` -> Run workflow.
Inputs: `runs_per_shard`, `scale` (1, 10, 100, 1000), `shards` (JSON list), `orgs` (JSON list of 1-6), `workers`
(use 1 at 1000x for memory). Total runs = shards x runs_per_shard. The receipt (`SIX.md`) shows the first 1, 10, 100
and 1,000 runs. Examples used: 1,000 runs at 1x = runs_per_shard 100, 10 shards; at 100x = 25 x 40 shards; 100 runs at
1000x = 5 x 20 shards, workers 1. The same grid on any machine: `bash scripts/scale_ladder.sh`.

**Real Kubernetes (GitHub, free, about 1 hour):** Actions -> `benchmark-reps` -> Run workflow, inputs
`duration_s 900`, `arms "native omni"`, `loadgen open`. Set 24 (run 36983865216, the engine before v1): `results/live/LIVE_REPS_24.md`.

## Results on 6 October (engines that no longer stand)

Each is its own engine's record, never read as omni-v25's; the engine that stands reads its own (`results/OMNI_INDEX.md`,
where the machines it takes are shown beside the work as power given, `results/WHOLE_SYSTEM.md`).

- Real Kubernetes on kind, sets 23 and 24 (the engine before v1): set 24 read machines in service down 31.6%, the 95th
  percentile down 60.1%, zero failed requests (`results/live/LIVE_REPS_24.md`).
- Real GPU (A10), 2 October: work per energy up 3.6%, the 95th percentile up 58.5%, slower, LOSS (wiring, corrected in GPU
  amendments 6-7), on a card controller since replaced: obsolete (`results/gpu/run-20261002T082232Z/GPU_REPS.md`). Modelled
  card, firmware alone vs firmware with Omni on top (`results/sim/gpu_two_wire/`, class S, the verdict with a 2% allowance):
  AI token generation energy down 3.3% / 3.7%, the median slower by under 1%; compute-bound energy down 0.7% / 0.5%. Read
  `DISCLOSURES.md` first.
- Six organisms, 1,000 runs at 1x (GitHub, before round 6): work per energy up 0.21% to 0.30%, every knob handed back;
  time over the service line about 0.2 points above native in every organism (not a win by the band-first rule). Round 6
  (`docs/REALMS_PREREGISTRATION.md`) found the cause and corrects it; checked on 20 paired seeds per organism, every
  organism then spent less time over the line than native with work per energy up 0.09% to 0.20%; the grid was run again
  on it (`results/scale/v1/GRID.md`).
- The real card on Lambda: the runs since are in `results/gpu/`.

## Open work

1. Bring the compass's time over the service line down to native or below (about +0.2 points today, every organism).
2. 1,000 runs at 1,000x and the two largest organisms at 1,000x need a bigger machine than GitHub's.
3. Kubernetes and the GPU together on one Lambda box (k3s), one set of receipts.
4. The C++ twin of the compass (the frozen engine already has one, `cpp/`).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
