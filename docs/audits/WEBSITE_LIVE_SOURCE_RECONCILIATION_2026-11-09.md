# LIVE versus FALLBACK website source: numerical reconciliation and acceptance contract

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Date:** November 9, 2026. **Scope:** GitHub source-of-truth verification for the website's disputed benchmark values. This document does not claim to have changed or redeployed the separate website. Do not use a source-indicator color as evidence of benchmark correctness.

## Findings established on `main`

1. `results/OMNI_INDEX.json` exists, parses, and publishes `headline_pct=20.354306904733164` and `service_headline_pct=93.97457452769498` with 26 named source tests. An independent geometric-mean calculation on those published test scores reproduces **both** figures and all six present category scores. The scoring procedure and evidence must still be independently reviewed against raw results. Reproducibility of an aggregation is not external replication of an experiment.
2. The proposed “fix” of changing `headline_pct` to `5.0186`, `service_headline_pct` to `12.8508` and Kubernetes to `28.0351` is inconsistent with the published score rows. The suggested PostgreSQL `4.1658`, Redis `0.112` and MySQL `2.205` also differ from the current category calculations. **Do not overwrite measured-source summaries without the corrected underlying source or a reviewed new scoring rule.**
3. results/ABC_TABLE.json (retired) is **intentionally absent**. The previous A/B/C model has been moved to `docs/history/model_tables/ABC_TABLE_MODEL.json`. The repository's `tests/test_site_numbers.py` explicitly requires that the legacy path not exist so modeled (class S) data is not served as a measured benchmark. A website request to `/api/github-data?file=ABC_TABLE` must not be considered proof of a GitHub data corruption or a missing measurement.
4. `results/SITE_NUMBERS.json` is the authoritative machine-readable website contract; `tools/site_numbers.py --check` checks it against underlying source files. Each entry in `show` identifies the exact version, class P or L, source receipt and intended wording. `four_arms` contains the native/Omni chip and cloud comparisons, preserving the original GPU V23 and Azure V18 labels. `not_for_the_site` identifies misleading or unsupported claims.
5. Current frozen engine V26 is separate from software evidence V25, GPU evidence V23 and Azure cloud evidence V18. A current-engine banner must not automatically reassign a historical measurement to V26.

## Website acceptance criteria for a genuine LIVE indicator

- The server fetches `results/SITE_NUMBERS.json` from a pinned or clearly identified live GitHub revision, validates the schema, verifies that the API response matches that revision, and reports the source revision and fetch time. A GitHub content endpoint and the website's API proxy are different failure domains.
- The site renders the relevant `show[].sentence` and `four_arms` fields without reinterpreting a composite index as a single throughput or total-bill gain, without altering a category score and without hiding negative results.
- On a valid source and successful fetch, the UI may display **LIVE**. On network failure, malformed response, unsupported schema, or stale/unknown revision it must say **UNAVAILABLE** or **STALE**, retaining provenance; it may display clearly labeled historical data but **never claim those numbers are freshly live**.
- Retire the `ABC_TABLE` endpoint request from the Receipts tab if it expects experimental data. The old JSON file is a synthetic modeling artifact, not a valid measured feed. Where modeled evidence is useful, explicitly identify it as class S and point to its archived location, separate from measured evidence.
- Verify end-to-end: capture the website API status, decoded schema, GitHub commit SHA, payload version and UI label on the same occasion; test a simulated 503, a corrupt payload, a source update and a negative-result row. Do not infer a repaired UI from a GitHub commit alone.

## Independent arithmetic validation

The website's numbers must reproduce the repository's declared composition, without hardcoded replacement percentages. If `r_{cj} = 1 + g_{cj}/100` is the scored positive ratio for test `j` in real category `c`, then

```text
R_c = exp( (1/n_c) * sum_j log(r_cj) )
Headline % = 100 * ( exp( (1/C) * sum_c log(R_c) ) - 1 )
```

The service-only reading substitutes each test's `service_pct`. This is an index under the project's equal-category and test-weighting policy, not a system-wide physical efficiency estimator. See `tools/omni_index.py` and `tests/test_public_benchmark_contract.py`; category membership and scoring guards are material assumptions requiring separate referee scrutiny.

**Next required action outside this repository:** Correct the website provider/endpoint mapping to the maintained `SITE_NUMBERS` contract, update its version/schema validation, and remove its dependency on the intentionally withdrawn `ABC_TABLE` measured endpoint. Only a successful browser/API integration test can establish the Receipts indicator is truly LIVE.

---

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
