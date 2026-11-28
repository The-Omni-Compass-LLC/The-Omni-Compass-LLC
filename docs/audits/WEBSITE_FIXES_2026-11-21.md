# The Website Against the Record, 21 November 2026: Every Fix, in Order

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Read on 21 November 2026: www.omni-compass.com, `/licensing`, `/pilot`, `/legal/ip-notice` and `/benchmark-results`, as text and
again in a real browser (Chromium) as a visitor sees them. `/licensing`, `/market/licensing`, `/benchmark-results`,
`/scale-invariance`, `/closed-circle-principle`, `/legal/benchmark-methodology` and `/docs/verify` sit behind the site's "Register to
Continue" form, so their bodies are not graded here; what a third outside audit of 21 November quoted from them (from search-engine
copies) is listed apart below, to be checked on the live page. Every figure below is checked
against the repository's own records. The numbers a page may show, each with its receipt, are in `results/SITE_NUMBERS.json`
(`show[].sentence`, written by `tools/site_numbers.py`); the numbers that must come off, each with why, are in
`docs/WEBSITE_CLAIMS.md`. The website is built outside this repository: each item names the change to make there.

## Tier 1: wrong on its face (a buyer's engineer or counsel finds these in minutes)

| # | The site says | The record says | The change |
|---|---|---|---|
| 1 | "omni-v26"; "SHA-256: 66c8f2d94b3e4725" (engine card, hero, fingerprint lines) | The engine that stands is **omni-v27**, digest **34548e45437a05bd**, 65 files (`OMNI_V27.json`). 66c8f2d94b3e4725 is omni-v24's digest. | Read the engine's name and digest from `OMNI_V27.json` (or `docs/engine/LIVE_ENGINE_VERSION.json`) at build time; type neither. |
| 2 | "17 sealed twin pairs", "17 verified modules" | **18** sealed twin pairs on omni-v27 (`results/SEAL.json`, `twins`). | Read the count from `results/SEAL.json`. |
| 3 | "10M Monte Carlo iterations", "10M+ Monte Carlo Runs", "Running Monte Carlo simulation (10,000,000 iterations)", "Seed 0x7F3A9C2E (published)" | No such run or seed exists. Each set is **500 runs** from the jump generator (seedₖ = base + k·0x9E3779B9 mod 2³²), proved by three implementations (the Python, the C++ harness, the page's own code) giving one digest; every set is listed in `results/RUNS_LEDGER.md`, none failed. | Remove every 10M and 0x7F3A9C2E. Show the run ledger's own counts, read from `results/RUNS_LEDGER.json`; the check anyone runs is `bash scripts/prove_runs.sh BASE 500`. |
| 4 | "+−1.3% GPU THROUGHPUT GAIN"; "−1.3% GPU / Chip GAIN … H100 · same joules" | "On one A10 card, its own meter: energy per request served GAIN in all three of our runs, down 1.3% (omni-v23)." It is energy per request, not throughput; the card is an A10; no H100 is in the record. | Use the record's sentence word for word. |
| 5 | "+20.0% Whole-system GAIN bare-metal · Arm C vs A" | "The Omni index: GAIN, up 20.0% (work, speed and machines; real software on GitHub's machines; omni-v26)." GitHub's runners are not bare metal; the letters A to D name the chip and the cloud, not this index. | Use the record's sentence; drop "bare-metal" and "Arm C vs A". |
| 6 | "+24.7% Through-cloud GAIN full-stack · Arm C vs A"; "+30.4% Through-cloud bill · power given · inside noise"; "+1.2% through-cloud bill · inside noise"; "THROUGH-CLOUD BILL: STATISTICALLY EVEN (+1.2%, INSIDE NOISE)" | Arm D against arm C (Azure, omni-v26, three runs): the work per dollar **GAIN in all three of our runs (up 28.3%, up 34.2%, up 28.8%; up 30.4% by the mean)**; the bill **power given in all three of our runs (up 27.6%, up 17.9%, up 28.5%; up 24.7% by the mean)**: more machines bought for more work. The site has the two means under each other's labels: 24.7% is the bill's rise, not a gain; 30.4% is the work per dollar, not the bill. The +1.2% is the omni-v18 set at the tune-down, a different test on an older engine. | Use the two record sentences together, never one without the other, each under its own label: work per dollar GAIN, up 30.4% by the mean; the bill power given, up 24.7% by the mean. The bill rose; no page says it stayed flat or fell. |
| 7 | "One loss on fairness (−2.3%)" beside "fairness, down 2.6%" | omni-v26: fairness LOSS, down 2.6% (`results/OMNI_INDEX.json`, the fairness test's index_pct −2.5525%). omni-v27 (20 November, three runs): fairness LOSS, 2.7% by the index's rule. The −2.3% is an earlier engine's. | One figure, read from the record, with its engine named. |
| 8 | The drain model: "2.9%", "~10%", "7%", "20%", the $100M savings figures and the per-year projections | On the "not for the site" list (`results/SITE_NUMBERS.json`, `not_for_the_site`): no table, chip receipt or cloud receipt carries them. | Remove. |
| 9 | "The Work Went Up 12%." | No table carries a 12% rise. | Replace with the Azure work-per-dollar sentence (item 6). |

## Tier 2: broken on the page

| # | What a visitor sees | Why | The change |
|---|---|---|---|
| 10 | "—" in the arm cells, "+0.0%" in the live panel, "loading…", "Fetching live data…" | The page reads results/ABC_TABLE.json (no longer in the repository), which is not in the repository (it answers 404; the model table moved to `docs/history/model_tables/` and is class S, never a result). | Read `results/SITE_NUMBERS.json` (`show[].sentence`, `four_arms`); when it cannot be read, say "the record could not be read just now", never a typed or cached number. |
| 11 | "--fingerprint=" with no value; "omni-v26 []" in the terminal block | The value is never filled. | Fill both from `OMNI_V27.json` at build time. |
| 12 | To a crawler or a text reader, `/pilot` (and every page drawn in the browser) is the banner, the disclosure and the footer; in a browser `/pilot` shows its whole 90-day pilot page. `/licensing`, `/market/licensing`, the theory pages and the methodology pages ask for a name and an email first. | The pages are drawn by the page's script after it loads, and the gated pages are behind the registration form. | For search engines and buyers' tools to read the pages, serve them as finished HTML (pre-rendering or server rendering). Whether the licensing terms and the methodology stay behind the form is the founder's decision: a buyer's counsel and every search engine meet the form first. |
| 13 | (withdrawn) The top ticker reads twice in the page's text | Its second copy sits off the screen, the usual way a scrolling ticker loops; a visitor sees it once. | Nothing. |
| 14 | "GitHub" and "ADMIN" in the public navigation | An administrative entry point is advertised to every visitor and crawler. | Take "ADMIN" out of the public navigation; keep it behind a login with two-factor sign-in. |
| 15 | Two repository names: `The-Omni-Compass-LLC/The-Omni-Compass` (button, `git clone`, data fetches) and `The-Omni-Compass-LLC/The-Omni-Compass-LLC` (the second engine card) | The repository moved to `The-Omni-Compass-LLC/The-Omni-Compass-LLC`; GitHub forwards the old name today, and a forward can be lost when a new repository takes the old name. | Use `https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC` everywhere, the raw data fetches included. |
| 16 | "View Results on GitHub" and "Open Live Engine on GitHub" lead nowhere | The buttons carry no link. | Link them to `results/OMNI_INDEX.md` and `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` on the repository, or to the live engine link the site already uses. |
| 17 | The clone block: `git clone https://github.com/The-Omni-Compass-LLC/The-Omni-Compass`, then `python harness/run_benchmark.py --verify` | The script does not exist. The outside AI's replacement of 21 November is cut short (`git clone https://github.com` with no path) and runs `python3 tools/verify_receipt.py` with no folder, which checks nothing. | Three lines: `git clone https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC`, `cd The-Omni-Compass-LLC`, `bash scripts/prove_runs.sh` (the engine that stands and its digest, then the newest set run again by the Python, the C++ harness and the page's own code, three digests side by side; `bash scripts/prove_runs.sh BASE 500` for any set). An archived run's signed receipt: `bash scripts/raw_archive.sh open /run-<id>/` then `python3 tools/verify_receipt.py results/live/raw/run-<id>`. |
| 18 | "SHA-256 sealed" (the outside AI asks for "SHA-256 & Sigstore cryptographically sealed") | Three different seals: the engine's 65 files by SHA-256 (`OMNI_V27.json`), the 18 twins by SHA-256 after their parity tests (`results/SEAL.json`), and every run archived since 31 October 2026 signed with Sigstore, keyless, in its public log (`SHA256SUMS_ALL.txt.sigstore.json` beside each run on the branch `raw`). | Say each seal for what it seals; the engine itself is fingerprinted, not Sigstore-signed. |

A `robots.txt` that turns away GPTBot, ClaudeBot, Google-Extended and CCBot (the outside AI's file) keeps those companies' models from
training on the site, and also keeps their assistants from reading it when someone asks them who made Omni-Compass. Google's own
search, and Google's AI answers built on it, are governed by Googlebot, which that file does not name. Which way to go is the founder's
decision; the repository's `llms.txt` asks every AI that reads it to print the notice.

## On the pages behind the registration form: what the third audit quoted (check each on the live page)

| # | Quoted from the page | What is wrong | The change |
|---|---|---|---|
| 19 | `/scale-invariance`: "L(αS, αθ) = L(S, θ), α > 0", named "homogeneity of degree one" | That identity is homogeneity of degree **zero** (the value does not change when every input is scaled); degree one would be L(αS, αθ) = α·L(S, θ). | Name the property the identity states, with its domain and units, and link the proof. |
| 20 | `/closed-circle-principle`: trajectories stay in the basin, with recurrence and convergence claimed together | Staying in a set (forward invariance) does not by itself give convergence to a point, and recovery after a disturbance is a third claim that needs the disturbance class named. | State each as its own result with its hypotheses and its proof, or say which are not yet proved. |
| 21 | `/scale-invariance`: no revalidation is needed when the deployment's scale changes | A law of the same form at every scale does not certify the machines it drives: delays, saturation and topology change with scale. | Say the law keeps its form under the stated assumptions, and that each place and its adapters are validated where they run (the repository's own three-run tables do exactly this). |
| 22 | `/legal/benchmark-methodology`: 4.6% against 11.5% called a 12.5-point difference | 11.5 − 4.6 = 6.9 points. | Correct the arithmetic, or show the two figures the 12.5 comes from. |
| 23 | `/docs/verify`: 194.102 kWh against 184.391 kWh under "−1.3%" | Those totals differ by 5.0% (9.711 kWh of 194.102), not 1.3%; and no record in the repository carries this pair at all (searched 21 November: neither total appears in any table or receipt). The A10's 1.3% is energy per request served (omni-v23), a different measurement. | Remove the pair. Do not publish it recomputed as "5.0% less energy" either, as the third audit's replacement text of 21 November would: a number no table carries goes on no page. The chip's line is the record's sentence (item 4). |
| 24 | `/market/licensing`: a $25 million annual minimum and a 5% hardware royalty; the homepage: "$20M licensing floor" | Two prices for one license. | One set of terms, or each offer named for what it is. |
| 25 | "ten million Monte Carlo draws eliminate initial-condition bias" | No number of draws removes a model's own bias, and no 10-million-draw run exists (item 3). | Remove. |

## Tier 3: legal words, for the company's counsel (nothing here is changed by this page)

- **Who owns the rights**: the IP notice names one of the two companies as the assignee of the inventor's rights, and elsewhere names the owner
  as Dubra Software Inc. / The Omni-Compass LLC. Counsel matches every page to the assignments actually signed.

- **"UNDER CONSTRUCTION" / "THIS SITE IS UNDER ACTIVE DEVELOPMENT"** stands on every page. The repository's own disclosure
  (`DISCLOSURES.md`) carries the evaluation notice, the factory tune and the wiring disclaimer without it. Whether the banner stays
  is the founder's decision.
- **Article VI, Trade Secrets** (`/legal/ip-notice`, section 6.1) names "specific relationships between convergence parameters" as
  trade secrets, while the engine's source, its equations and its parameters are public in the repository and printed in the
  Owner's Manual. A published relationship is not secret. Counsel can narrow the article to what is truly unpublished (material
  disclosed only under a non-disclosure agreement). The repository's own legal papers (`LICENSE`, `NOTICE`, `DISCLOSURES.md`,
  `PATENTS.md`, `TRADEMARKS.md`) make no trade-secret claim.
- **The mailboxes**: the site shows contact@, licensing@ and legal@omni-compass.com; each must reach a person.

## What the outside AI's packages of 21 November got wrong (do not paste them)

- **Its LICENSE, file headers, README block and SECURITY.md.** The repository already carries its own: the Omni-Compass Evaluation
  License 1.0 (`LICENSE`, `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`), `NOTICE`, `DISCLOSURES.md`,
  `PATENTS.md`, `TRADEMARKS.md`, `CITATION.cff` and `SECURITY.md`, with the owners' notice at the top and the end of every page and
  in every source file's header (`tools/legal.py`, checked on every push). Its headers say "registered" (the company's wording is
  "filed", with no numbers), name omni-v26, and pasted into the 110 files the engine's fingerprint seals they would change the engine.
- **Its statistical box.** "N = 10,000,000 paired iterations", "99.9% CI", "seed 0x7F3A9C2E", "raw hourly billing remains
  statistically invariant (p > 0.05)", "8 metrics show statistically significant gains", "NVIDIA A10/H100", "bare-metal": none of
  it is on the record, and the bill line says the opposite of the receipt (item 6).
- **Its README quick start.** `harness/run_benchmark.py` does not exist, and `sha256sum -c RELEASE_MANIFEST.json` does not work (the
  manifest is not a checksum list). The one command is `bash scripts/prove_runs.sh BASE 500`.
- **Faults it reported that are not on the site:** a "DD World Studios" footer and "V25" on `/pilot` (read in a browser: engine "V26",
  no such footer). Its "$25M + 5% royalty" is on `/market/licensing`, behind the registration form (item 24). The
  "bd615f15" it read as a page's SHA is the first eight characters of one engine file's hash (`omnicompass/core.py` in
  `OMNI_V27.json`), not the engine's digest.

## The outside AI's four "tripwires": what the repository already carries

| Its ask | In the repository today | What remains |
|---|---|---|
| `License :: Other/Proprietary License` in `pyproject.toml` | Present, with the exact license expression scanners read (`license = "LicenseRef-OmniCompass-Evaluation-1.0"`), every legal paper in `license-files`, the owners as author and the version 0.27.0 (the engine omni-v27); `REUSE.toml` and the SPDX header on every source file. Its block would replace that with version 26.0.0, a personal author and no license expression. | Nothing. |
| A startup banner in `harness/run_benchmark.py` and the C++ `main()` | That file does not exist. The engine's files are sealed by its fingerprint: a line added to any of them changes the engine, which the founder's order of 20 November forbids. | Nothing in the engine. |
| `ai.txt` and `robots.txt` | `llms.txt` (for AI crawlers), `AGENTS.md`, `GEMINI.md`, `.github/copilot-instructions.md` and `.cursorrules` each order the notice on every answer. A `robots.txt` or `ai.txt` inside a GitHub repository is read by no crawler: github.com's own `robots.txt` governs it. | For the website's root only: a `robots.txt` that keeps `/admin` out of crawlers, and an `ai.txt` stating the training opt-out. Only crawlers that choose to honour them do. |
| `NOTICE`, `CODEOWNERS`, a signed release tag | `NOTICE` and `.github/CODEOWNERS` present. No release tag on GitHub. | A signed tag carries its signer's own key: the founder signs it with his (`git tag -s omni-v27 -m "…"`); nobody else can sign as him. Its tag name "v26.0.0" names an engine that no longer stands. |

## Public or private

The repository is public today. The website's live numbers, the live engine page's own update and the published live engine link all
read their records from it (`raw.githubusercontent.com`). Made private, every one of those reads fails for every visitor, the
website shows no live number, and a visitor's `git clone` is refused. The filings (patents, copyrights, trademarks) are unaffected
either way.

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
