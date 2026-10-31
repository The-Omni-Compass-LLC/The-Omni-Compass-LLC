# Paired SLO goodput: inference and cloud comparison admission

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Why this benchmark exists

NVIDIA Dynamo publishes controlled comparisons for inference routing, KV caching, disaggregated serving and SLO goodput. Microsoft CLEO targets compute, power and placement efficiency. Omni must test the *incremental* effect of its supervisory layer over an identical native deployment, not compare unlike chips, traffic, models or configurations.

## Paired experiment

For each frozen workload trace and hardware allocation, record native and Omni-on-native under the same model, batch policy, arrival process, measurement window, input/output token distribution, memory constraints, clock and power measurement method, and software versions. Rotate arm order and record thermal and cache warmup. Add a separate watch-only arm where supported; never count watch as a governed gain. For LLM inference, also retain TTFT, inter-token latency, token-level goodput and request-level SLO violations. For distributed inference, report routing and KV-cache hit rate, prefill/decode topology and cross-node transfer costs.

The executable evaluator is `python3 tools/paired_slo_goodput.py input.json --output verdict.json`. Its minimal required JSON has `native` and `omni` arrays of paired records. Each record has `workload_id`, `hardware_id`, `offered_requests`, `completed`, `failed`, `p95_ms`, `energy_j`, and `cost_usd`. Optional `limits` keys are `max_p95_ratio`, `min_completed_ratio`, and `max_failed_delta`. Defaults require non-worse P95, non-worse completed work and no extra failures. Set a different margin *before* collecting results, not afterward.

For each pair, report
`goodput_per_joule = completed / energy_j`,
`goodput_per_dollar = completed / cost_usd`,
and signed relative differences against native. A lower energy bill is not an admitted improvement if service guardrails fail. Every pair must pass for the overall admission signal to pass. The tool provides descriptive ratios only, not uncertainty estimates or proof of causal advantage.

## Evidence and execution gates

1. Run `python3 -m unittest -v tests.test_paired_slo_goodput` and preserve the exit code.
2. Capture matched, independent raw traces, hardware and model IDs, engine SHA, run IDs, clocks, energy-meter provenance, provider invoice rates, and frozen guardrails.
3. Run randomized or counterbalanced paired repetitions. Compute confidence intervals and show every loss; do not infer exact equality from a tolerance band.
4. Compare native to native-plus-Omni on the *same* inference engine, e.g. vLLM/Dynamo, and on the same physical resources. Do not claim a Dynamo comparison without actually deploying and measuring Dynamo.
5. Separate hardware P measurements from software L, simulation S and theorem T evidence. No GPU/cloud benefit is claimed by this benchmark's existence.

## References

- NVIDIA Dynamo feature benchmark recipes: https://docs.nvidia.com/dynamo/dev/recipes/benchmarks
- NVIDIA Dynamo benchmarking guide: https://github.com/ai-dynamo/dynamo/blob/main/docs/fern/pages/recipes/feature-benchmarks/benchmarking-guide.md
- Microsoft CLEO: https://www.microsoft.com/en-us/research/project/cloud-efficiency-optimization-cleo/

This is a new benchmark *evaluation protocol and comparator*, not a completed external-system benchmark or a result.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
