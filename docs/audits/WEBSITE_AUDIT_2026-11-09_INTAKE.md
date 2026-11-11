# Website referee audit: November 9, 2026 — external assessment intake and reconciliation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Provenance:** A website audit supplied by the owner on November 9, 2026, attributed in the supplied text to "Airo", timestamped 9:50 AM EST. This file records its findings and the repository evidence reviewed during intake. **The external assessment is not an independent certification, and reported live endpoint checks were not repeated here.** A reported A+ means an assessor's opinion, not verified passing tests. Site source code may live in a separate deployment repository.

## External audit scorecard (as reported)

| Audit category | Assessor grade | Reported state |
| --- | --- | --- |
| Videos | A+ | 28 video slots claimed populated |
| Images | A | 191 image slots claimed; `pages/hero/slide-3-kubernetes` reportedly uploaded but unused |
| Links | B | Two nonexistent routes and three external Claude artifact destinations |
| Email and registry | A | Contact form, download gate, admin registry, download notification and analytics said to function |
| Tabs | B+ | `/benchmark-results` Arm D reported as placeholder |
| Homepage | A+ | All reported tour sections and homepage live-data components present |
| Landing pages | B+ | Missing route error boundaries in three named landing pages |
| Other pages | A | Some routes said to lack `errorElement` |
| Live data engine | C | `OMNI_INDEX` flagged as corrupted by assessor; `ABC_TABLE` returned 503; fallback reportedly used |
| APIs | A | Most endpoints reportedly returned HTTP 200; `ABC_TABLE` reported HTTP 503 |
| SEO | A+ | Metadata, indexing, sitemap, robots, llms.txt reported present |
| Tour and guide | A+ | Homepage walkthrough, TTS and page guides reportedly operational |
| **Overall** | **A−** | **External assessor's composite, not independently verified** |

## Media coverage to verify on website

- **Videos:** Hero slide 3 benchmark background and catalog background; slide 4 AI and alternative video; slide 5; slide 6 government technology and five options; slide 7 six supervisor options; slide 8 catalog; footer; paired videos for aerospace, AI, autonomous fleets, cloud, defense, energy, enterprise, Linux kernel, manufacturing and robotics; additional biology, closed-circle, control-engine, four-stack, governance, grand-theory, infrastructure, Monte Carlo, omni-AI, peer-review, and scale-invariance pages. Report claims all placements are populated but does not furnish asset-by-asset HTTP proofs.
- **Images:** Logo horizontal/primary/vertical/favicon/wordmark; 10 hero slides and variants; five hero alternates; OG artwork; ten domain heroes and sections; major page heroes; homepage bento/proof/evidence/upload; blog covers and imported assets. Report identifies `pages/hero/slide-3-kubernetes` as uploaded but unused. Do not force it into the carousel without the approved slide specification.
- **Links:** Audit reports valid principal menus, footer and social links, but asserts `/company/products` and `/company/apparel` do not exist. Verify whether routes have since been deployed before removing or redirecting. The DD World Studios menu allegedly targets a Claude artifact, as do BenchmarkEngine and LiveEnginePanel gated downloads. Replace only after confirming an approved stable destination and any access-control requirements.
- **Email/registry:** Audit reports `POST /api/contact/contact`, `POST /api/download-gate`, download registry, notifications and GA4 event tracking working. Test with safe non-production data and verify delivery, permission boundaries, retention and security. Do not disclose or rename secret values merely because a secret key looks non-standard.

## Site structure to verify

- `/benchmark-results`: overview, baseline Arm A, Omni Arm B, composition Arm C, web Arm D, per-category/GPU, receipts, and methodology were reported, though the assessor inconsistently called this “7 tabs” while listing eight entries.
- `/platform/qa`: virtual guide and six Q&A tabs, claimed 55 questions.
- `/docs`: documentation tabs claimed populated.
- `/market/licensing`: six-step PageTourGuide and Virtual Guide claimed in place.
- **Homepage:** hero, solution, scale invariance, proof, benchmark, domains, biology, receipts, blueprint, blueprint cards, IP, IP cards, engagement path, four-stack, grand theory, literature, competitive landscape, numbers, engine, pillars, statistics, stack-tax band, docs and testimonial were enumerated. The audit called this 22 covered sections, while its enumeration contains 23 entries. Recount from actual tour configuration.
- **Landing pages:** `/lp/competitive-takedown` reportedly has error boundary; `/lp/enterprise`, `/lp/defense`, `/lp/acquisition` reportedly lack `errorElement`. Confirm framework routing semantics before changing.
- **Other routes:** Assessor enumerated core, 14 docs, 8 legal, 7 platform/engine, 5 theory, 3 validation, 11 domain, 4 market, about/contact/pilot, blog, theory subpages, miscellaneous, admin and SEO monitor. It reported missing `errorElement` for the theory subpages and miscellaneous routes. The closing fix list gives a different set of 11 specific paths: `theory/noether`, `theory/lyapunov`, `theory/renormalization`, `domains`, `pilot/program`, the website route /docs/github, the website route /docs/color-key-guide, `contact/success`, `lp/enterprise`, `lp/defense`, `lp/acquisition`. The route counts and lists must be reconciled against the actual source; they should not be taken as exhaustive.
- **SEO:** Helmet, canonicals, Open Graph, Twitter cards, JSON-LD, noindex rules, Google Search Console, IndexNow, llms.txt, robots.txt and sitemap were reported A+; require URL-level verification and Search Console evidence.
- **Tour/TTS:** TourFAB, HUD, introduction, tour stops, Nova voice, chunking, auto-advance, guides and `omni:start-tour` event were reported A+. Validate mobile/desktop accessibility and automated failure states.

## Live data and endpoint observations (external report, unconfirmed as of this commit)

| Named source or endpoint | External audit observation | Required verification |
| --- | --- | --- |
| `GET /api/github-data?file=OMNI_INDEX` | 200, `headline_pct=20.35`, `service_headline_pct=93.97`; assessor calls these corrupted | Compare exact version, engine, receipt lineage and site parsing rules; **do not alter the record to fit a legacy site range guard** |
| `GET /api/github-data?file=ABC_TABLE` | 503 | Determine whether the endpoint is requesting a deliberately retired model-table path; inspect proxy mapping, status and cache headers |
| `GET /api/github-data?file=SEAL` | 200 | Verify response schema and seal integrity |
| `GET /api/health`, `GET /api/analytics/config` | 200 | Validate healthy dependencies, not HTTP status alone |
| `GET/POST /api/tts`, contact, download gate, download registry, ScriptForge generator | 200 claimed | Test appropriate verbs, authenticated access, side effects and failure cases |

## Material conflicts with the actual repository record

1. **Do not overwrite legitimate computed results.** On November 9 intake, repository `results/OMNI_INDEX.json` on `main` actually contains `headline_pct: 20.354306904733164` and `service_headline_pct: 93.97457452769498`. The repository's own `docs/WEBSITE_CLAIMS.md` states those are Omni-v25 readings, with a 20.4% main index and 94.0% second reading. The external audit's instruction to replace these with `5.0186` and `12.8508` is **rejected pending evidence that the source computation is wrong**. Its requested `Kubernetes: 28.0351` is likewise not authorized; `results/OMNI_INDEX.json` currently reads approximately 20.4633% for real Kubernetes. No test receipts were re-run as part of this document.
2. **`ABC_TABLE.json` was deliberately withdrawn from `results/`.** Repository `tests/test_site_numbers.py` explicitly asserts results/ABC_TABLE.json (retired) must not exist. Repository `docs/WEBSITE_CLAIMS.md` explains that this was a class-S model table formerly misrepresented as measured results, archived at `docs/history/model_tables/ABC_TABLE_MODEL.json`. Restoring it to `results/` or inventing `web.D` to satisfy the website would violate that safeguard. The website should use `results/SITE_NUMBERS.json` and show missing data honestly.
3. **Do not present fallbacks as real-time receipts.** Repository `docs/WEBSITE_CLAIMS.md` directs that unavailable data be labeled “the record could not be read just now,” not silently replaced with cached or typed results. If the website's V25 guard rejects legitimate V25 values, update the website compatibility contract with validation and failure tests; do not rewrite the benchmark.
4. **Four-arm terminology must be coherent.** The archived model table's A/B/C labels do not constitute physically measured four-arm chip/cloud experiments. Class P = physical meter; L = live software; S = own model. All public numbers require explicit workload, engine version, provenance, units, three-run interpretation and direction-aware GAIN/STEADY/LOSS reading.
5. **The external assessor's reported “GitHub-side” 503 is unproven.** A 503 from a website proxy does not by itself localize the defect to GitHub, especially when the requested file was intentionally removed. Verify application routing before changing repository files.

## Website implementation queue (requires website source and tests)

1. Resolve two dead nav links only if still dead; preserve user experience with a valid replacement route or intentionally remove the menu entries.
2. Replace three reported Claude artifact destinations with owner-approved durable assets/pages while retaining legal gates.
3. Add and test route-level error boundaries where the website framework needs them; reconcile competing route inventories.
4. Remove or accurately label the Arm D placeholder; only add data backed by an actual measured run and receipt.
5. Change live feed to consume `results/SITE_NUMBERS.json`, disclose provenance and failure status; distinguish source failures from application defects.
6. Confirm asset mapping, accessibility, SEO, links, forms, downloads, tour and mobile behavior with repeatable checks.
7. Test every public benchmark number against repository receipts and `docs/WEBSITE_CLAIMS.md` before publication.

**Scope of this commit:** documentary intake and source reconciliation only. It does **not** change production website code, assert a 200/503 retest, alter measured percentages, or claim the site has been deployed or repaired. The external report's observations remain findings to verify.

**Authoritative repository references:** `AGENTS.md`, `LICENSE`, `NOTICE`, `DISCLOSURES.md`, `docs/WEBSITE_CLAIMS.md`, `results/OMNI_INDEX.json`, `results/SITE_NUMBERS.json`, `results/SITE_NUMBERS.md`, `tests/test_site_numbers.py`.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
