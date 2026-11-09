# Website ↔ GitHub alignment contract
> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Scope and authority (2026-11-09).** This document specifies the correspondence of public website content to repository evidence. It governs future edits across both sides; it does not claim that production website assets were modified or deployed from this GitHub repository. The current connected GitHub account exposes this engineering repository, not the website source. Source code, asset identifiers, accessibility state, backend secrets and publication readiness must be verified in the website project itself.

## One public identity and one mechanism

**Corporate publisher:** Dubra Software Inc. / The Omni-Compass LLC. **Product:** Omni-Compass, proprietary supervisory governance software. The published description may say: **“Pure software. Runs on existing hardware. No new hardware purchase required for the governor. No rip and replace of the native controller.”** A deployment may need integration, permissions or configuration. The governor reads the controllers' existing gauges and commands permitted settings; it is not a data-plane compressor, CPU replacement, or network intermediary. It does not imply that all optional domains already have production adapters.

## Evidence classes and hard references

| Claim family | Required source | Release interpretation |
|---|---|---|
| Software work, speed, machine-use score | `results/SITE_NUMBERS.json` → `show[omni_index]`; `results/OMNI_INDEX.json`; `tools/omni_index.py` | V25 composite index of work, speed and resources; 20.4%, **not** a raw 20.4% uplift in completed work |
| Service-only index | `show[work_and_speed]` | V25 +94.0% composite from work and response metrics, not bill savings or an end-to-end total |
| Kubernetes category | `show[kubernetes]` | V25 +20.5% category index; fairness `LOSS` of −2.3% included |
| Same-time actual work | `results/WORK_TODAY.md` plus its underlying named paired-run workload and denominator | Publish **only** a supported throughput/completed-work or goodput ratio with units, time window, environment, baseline and uncertainty; never substitute an index or response-time decrease |
| Physical GPU | `show[chip_energy_per_request]`, `show[chip_work_for_the_bill]`; `results/TWO_BILLS.json` | V23 A10 meter: energy per served request lower; work per dollar mixed over three runs |
| Cloud economics | `show[cloud_bill]`, `four_arms.C` / `four_arms.D`; `results/TWO_BILLS.json` | V18 Azure 97 paired comparisons; work per dollar not recorded |
| Composed full system | `results/WHOLE_SYSTEM.md` | Model composition, class S; not a simultaneous physical chip–cloud measurement |
| Company and rights | `LICENSE`, `NOTICE`, `DISCLOSURES.md`, `docs/COMPANY_ATTRIBUTION_STANDARD.md` | Proprietary terms; no unproved legal title-transfer or granted-patent claim |
| Proposed licensing economics | `docs/COMMERCIAL_TERMS_PROPOSAL.md` | Proposals/examples only until signed agreements establish contractual rates |

**Value provenance:** Every displayed metric carries value, unit, aim (higher/lower), baseline, evidence class, engine version, workload, sample count, confidence interval when measured, test/run IDs and a stable receipt. A source failure is rendered as “The record could not be read just now,” not an old typed number. Neither an HTTP 200 nor a green build certifies a benchmark.

## Website component-to-evidence mappings

| Website surface | Product communication | Mandatory alignment and acceptance |
|---|---|---|
| Homepage hero and supervisory description | One-line identity, architecture, existing hardware and native-controller retention | Product promise matches `docs/MECHANISM_OF_ACTION.md`; no invented throughput or bill claim |
| Ticker / animated statistics | Compact benchmark claims | Feed **only** `results/SITE_NUMBERS.json` data with receipt links; freeze or hide if unavailable, never silently substitute fallbacks |
| Homepage benchmark panel and carousels | Per-workload comparisons | Match engine and class on each card; show adverse rows, confidence and baseline; no cross-version percentage addition |
| Homepage 10-slide tour and PageTourGuide | Stepwise narrative from problem through mechanism, experiment, receipts and licensing | Each stop maps to a real section anchor, media ID and exact evidence; accessible next/back, reduced-motion and audio off |
| Virtual guide / TTS / Q&A | “What is it?”, “How does it work?”, “Where did numbers come from?”, “What is the bill?”, “What is not proved?” | Reuse the same canonical statements; TTS must say the version, what percentages mean and model-vs-meter distinction |
| Investor / press / awards | Commercial position and technical validation | Cite qualified software and physical measures; refrain from independent approval, global optimum or $ valuation as established facts |
| Whitepaper / mathematics / quantum claims | Theorems, equations and field-domain mappings | Match hypotheses and open problems in `docs/TRACKING_THEOREM.md`, `docs/ENGINE_PROOFS.md`, `docs/EVIDENCE_LEDGER.md`; analogies do not establish a quantum theory or external-plant realization |
| Case studies / deployment guides | Named native-vs-Omni workstreams | Three-run or specified sample protocol, reproducible versions, actual actuator rights and rollback, exact receipts |
| Licensing / market / SAAS | License tiers, saving share, hardware embedding rights | Display **proposed** 25% verified savings share and proposed 5% embedded hardware royalty with distinct denominators; never count a royalty as a measured saving |
| Images, slides, video, carousels | Technical visual explanation | Associate every media placement with asset manifest/hash, alt text, source/license, factual caption and correct route. No imagery implies hardware intervention contrary to actual mechanism |
| SEO / social / download links | Discoverability and engagement | Cross-check canonical names, valid site routes, stable download IDs, access gate and signed legal notices. No stale external artifact destinations |

## Spoken tour editorial sequence

1. **Identity:** “Omni-Compass is supervisory software from Dubra Software Inc. / The Omni-Compass LLC.”
2. **Place:** “It runs above the native controls already present. It does not move work through its own data path.”
3. **Rule:** “It observes approved gauges, proposes bounded settings, verifies writes and restores native settings under its rollback policy.”
4. **Comparison:** “Results compare native operation with Omni-Compass above that same native stack.”
5. **Evidence:** “A software index, physical GPU meter, cloud bill and simulation each answer a different question.”
6. **Limits:** “Performance varies by workload and configuration, and adverse observations stay visible.”
7. **Economics:** “More useful work in the same interval and lower total bill are separate measurable outcomes. Commercial royalties are separate contractual amounts.”
8. **Next action:** “Read a named receipt or request a controlled paired pilot.”

This is canonical reference dialogue, not proof that the website's virtual guide has been changed. Each route may expand it using a more detailed local script only if the same meaning and provenance survive.

## Referee arithmetic: throughput and savings are independent

With native useful completed work `W_N` and Omni work `W_O` over **the same duration** `T`, define:

```text
work_gain_pct = 100 * (W_O/T / (W_N/T) - 1)
bill_savings_pct = 100 * (C_N - C_O) / C_N
work_per_dollar_gain_pct = 100 * ((W_O/C_O)/(W_N/C_N) - 1)
```

Only compute where the denominator is positive and measurement windows, workload definitions and SLO success criteria are comparable. If the work itself is fixed, show “same work” rather than claiming a productivity uplift. Never automatically infer bill savings from latency or machine-use index values. For fixed `W`, throughput and runtime require a stated identical-completion experiment. Multi-layer percentages cannot be summed.

## Implementation acceptance

- One strongly typed site data adapter consuming the allowlisted `show[]` IDs and field metadata; no arbitrary remote claims, embedded model values or hidden fallback constants.
- Automated unit tests for valid, stale, missing, malformed and version-mismatched API responses and negative direction-aware readings.
- Route inventory: homepage, tour, hero slides, virtual guide scripts, ticker, stat tiles, benchmark results, cases, media, papers, licensing and downloads. Track each path, section anchor, locale, asset reference and test status.
- Accessibility: captions, TTS text/visual equivalence, keyboard stop navigation, mobile focus/ARIA, alternative text and prefers-reduced-motion.
- Build and preview on exact website commit; compare visible values and spoken strings to current `results/SITE_NUMBERS.json` and source documents; inspect a real device and final deployed URL.
- Keep code release, website deploy, and GitHub benchmark receipts as **three distinct identities** (SHA, time, environment); no claim of deployment before publishing the site artifact.

## Source of truth
`AGENTS.md`; `docs/WEBSITE_CLAIMS.md`; `docs/REFEREE_VERSION_AND_BENCHMARK_STANDARD.md`; `docs/audits/WEBSITE_AUDIT_2026-11-09_INTAKE.md`; `results/SITE_NUMBERS.json`; `docs/ENGINE_PROOFS.md`.

---
> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
