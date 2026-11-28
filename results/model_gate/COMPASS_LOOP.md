# The compass loop, measured where its proof stops

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Our own model (class S), never a benchmark result. Written by `tools/compass_loop.py` from the engine's own `CompassLaw.force` (`omnicompass/compass_law.py`); the proof it extends is `docs/ENGINE_PROOFS.md`, section 1b (L1 to L4, `tools/prove_engine.py`). Each row is one gain set, one response time tau (in beats), one damping and one push of size D (half the muscle's pull at 0.3 from the centre); the tail is the largest distance from the centre over the second half of 1200 beats; R* = (A / kp) artanh(D / (b A)) is the ball the proof keeps without damping. Every row is printed, whichever way it falls.

## What falls out

| Model | Rows | At or under R* | Largest tail / R* |
|---|---|---|---|
| M1, the proof's case; damping none | 8 | 8 | 1.000 |
| M2, lagged muscle; damping none | 32 | 24 | 1.870 |
| M2, lagged muscle; damping default | 32 | 31 | 1.105 |
| M2, lagged muscle; damping three times | 32 | 32 | 1.000 |
| M1, damping for a lag not there; damping default | 32 | 31 | 1.147 |
| M1, damping for a lag not there; damping three times | 32 | 17 | 2.629 |

## Every row

| kp | A | b | R* | Model | tau (beats) | Damping | Push | Tail | Tail / R* | At or under R* |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0.4 | 0.1467 | M1, the proof's case | 1 | none | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, the proof's case | 1 | none | flip | 0.0364 | 0.248 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, the proof's case | 1 | none | random | 0.1149 | 0.783 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, the proof's case | 1 | none | slow | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | none | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | none | flip | 0.0348 | 0.237 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | none | random | 0.1150 | 0.784 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | none | slow | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | default | flip | 0.0348 | 0.237 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | default | random | 0.1150 | 0.784 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | default | slow | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | three times | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | three times | flip | 0.0348 | 0.237 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | three times | random | 0.1150 | 0.784 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 0.25 | three times | slow | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | none | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | none | flip | 0.0148 | 0.101 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | none | random | 0.1209 | 0.824 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | none | slow | 0.1526 | 1.040 | no |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | default | flip | 0.0159 | 0.108 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | default | random | 0.1036 | 0.706 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | default | slow | 0.1463 | 0.997 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | three times | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | three times | flip | 0.0186 | 0.127 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | three times | random | 0.0863 | 0.588 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 1 | three times | slow | 0.1405 | 0.958 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | none | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | none | flip | 0.0075 | 0.051 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | none | random | 0.1314 | 0.895 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | none | slow | 0.1834 | 1.250 | no |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | default | flip | 0.0080 | 0.055 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | default | random | 0.0980 | 0.668 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | default | slow | 0.1455 | 0.992 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | three times | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | three times | flip | 0.0092 | 0.063 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | three times | random | 0.0767 | 0.523 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 2 | three times | slow | 0.1286 | 0.877 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | none | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | none | flip | 0.0037 | 0.025 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | none | random | 0.1299 | 0.886 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | none | slow | 0.2188 | 1.492 | no |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | default | flip | 0.0039 | 0.027 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | default | random | 0.0919 | 0.627 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | default | slow | 0.1441 | 0.982 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | three times | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | three times | flip | 0.0044 | 0.030 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | three times | random | 0.0650 | 0.443 | yes |
| 1 | 1 | 0.4 | 0.1467 | M2, lagged muscle | 4 | three times | slow | 0.1100 | 0.750 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | default | flip | 0.0364 | 0.248 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | default | random | 0.1149 | 0.783 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | default | slow | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | three times | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | three times | flip | 0.0364 | 0.248 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | three times | random | 0.1149 | 0.783 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 0.25 | three times | slow | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | default | flip | 0.0437 | 0.298 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | default | random | 0.1022 | 0.697 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | default | slow | 0.1460 | 0.995 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | three times | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | three times | flip | 0.0712 | 0.486 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | three times | random | 0.0906 | 0.617 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 1 | three times | slow | 0.1399 | 0.954 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | default | flip | 0.0522 | 0.356 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | default | random | 0.0969 | 0.661 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | default | slow | 0.1442 | 0.983 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | three times | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | three times | flip | 0.1496 | 1.019 | no |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | three times | random | 0.1398 | 0.953 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 2 | three times | slow | 0.1273 | 0.868 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | default | outward | 0.1467 | 1.000 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | default | flip | 0.0712 | 0.486 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | default | random | 0.0906 | 0.617 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | default | slow | 0.1399 | 0.954 | yes |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | three times | outward | 0.1984 | 1.352 | no |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | three times | flip | 0.2087 | 1.423 | no |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | three times | random | 0.2986 | 2.035 | no |
| 1 | 1 | 0.4 | 0.1467 | M1, damping for a lag not there | 4 | three times | slow | 0.3857 | 2.629 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, the proof's case | 1 | none | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, the proof's case | 1 | none | flip | 0.0244 | 0.594 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, the proof's case | 1 | none | random | 0.0359 | 0.871 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, the proof's case | 1 | none | slow | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | none | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | none | flip | 0.0231 | 0.561 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | none | random | 0.0362 | 0.879 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | none | slow | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | default | flip | 0.0253 | 0.614 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | default | random | 0.0347 | 0.842 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | default | slow | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | three times | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | three times | flip | 0.0300 | 0.728 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | three times | random | 0.0340 | 0.826 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 0.25 | three times | slow | 0.0411 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | none | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | none | flip | 0.0085 | 0.206 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | none | random | 0.0389 | 0.945 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | none | slow | 0.0517 | 1.255 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | default | flip | 0.0095 | 0.232 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | default | random | 0.0328 | 0.797 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | default | slow | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | three times | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | three times | flip | 0.0123 | 0.299 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | three times | random | 0.0287 | 0.696 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 1 | three times | slow | 0.0407 | 0.989 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | none | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | none | flip | 0.0041 | 0.099 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | none | random | 0.0423 | 1.028 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | none | slow | 0.0635 | 1.542 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | default | flip | 0.0044 | 0.108 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | default | random | 0.0310 | 0.753 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | default | slow | 0.0411 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | three times | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | three times | flip | 0.0054 | 0.131 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | three times | random | 0.0254 | 0.616 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 2 | three times | slow | 0.0399 | 0.968 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | none | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | none | flip | 0.0020 | 0.048 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | none | random | 0.0481 | 1.170 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | none | slow | 0.0770 | 1.870 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | default | flip | 0.0021 | 0.051 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | default | random | 0.0334 | 0.810 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | default | slow | 0.0455 | 1.105 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | three times | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | three times | flip | 0.0024 | 0.058 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | three times | random | 0.0230 | 0.558 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M2, lagged muscle | 4 | three times | slow | 0.0380 | 0.924 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | default | flip | 0.0268 | 0.652 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | default | random | 0.0347 | 0.843 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | default | slow | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | three times | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | three times | flip | 0.0319 | 0.775 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | three times | random | 0.0357 | 0.868 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 0.25 | three times | slow | 0.0411 | 0.999 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | default | flip | 0.0319 | 0.775 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | default | random | 0.0357 | 0.868 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | default | slow | 0.0411 | 0.999 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | three times | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | three times | flip | 0.0414 | 1.006 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | three times | random | 0.0527 | 1.281 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 1 | three times | slow | 0.0407 | 0.988 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | default | flip | 0.0356 | 0.865 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | default | random | 0.0403 | 0.980 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | default | slow | 0.0411 | 0.998 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | three times | outward | 0.0415 | 1.009 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | three times | flip | 0.0438 | 1.064 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | three times | random | 0.0641 | 1.558 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 2 | three times | slow | 0.0465 | 1.129 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | default | outward | 0.0412 | 1.000 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | default | flip | 0.0394 | 0.957 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | default | random | 0.0472 | 1.147 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | default | slow | 0.0409 | 0.994 | yes |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | three times | outward | 0.0754 | 1.832 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | three times | flip | 0.0447 | 1.086 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | three times | random | 0.0785 | 1.908 | no |
| 4 | 0.3 | 0.2 | 0.0412 | M1, damping for a lag not there | 4 | three times | slow | 0.0720 | 1.750 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
