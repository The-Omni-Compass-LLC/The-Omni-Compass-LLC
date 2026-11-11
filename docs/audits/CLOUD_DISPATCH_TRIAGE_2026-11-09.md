# AWS and Google Cloud dispatch triage — 9 November 2026

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Read from GitHub repository `main`; the workflow run ledger is a historical snapshot, not a live GitHub Actions status endpoint. No credentials or paid resources were accessed.**

## Current source facts

- The current standing engine is **omni-v26**, as identified in `OMNI_V26.json`, `docs/OMNI_V26.md` and the conductor `scripts/dispatch_grid.py`. The main published software index still reports **omni-v25**; physical A10 results remain labelled **omni-v23**, and the earlier Azure steady measurements **omni-v18**.
- Both `scripts/amazon_queue.txt` and `scripts/google_queue.txt` now end with **`switch=on`**, with comments recording November 1 re-enablement. This directly contradicts the obsolete “switched off” descriptions in `docs/RUN_LEDGER.md` and the October 24 headings in `docs/AMAZON_SETUP.md` and `docs/GOOGLE_SETUP.md`. The current queue configuration is **on**, but “on” is not proof of successful preflight, job dispatch, hardware rental or benchmark completion.
- `.github/workflows/cloud-check.yml` checks credential presence, key format, provider login, capacity/quota or permissions at no rental cost. `.github/workflows/eks-metered.yml` and `gke-metered.yml` are **manual-dispatch** workflows. `scripts/dispatch_grid.py` is designed to dispatch sets only after successful preflight. `.github/workflows/grid.yml` schedules the conductor at `7 */3 * * *` in UTC; it is not itself a daily benchmark result.
- Historical `docs/engine/github_ledger.json` is dated **2026-10-30T00:22:00Z**. It records `cloud-check both` run **40471452017** on October 27 as failed, with the GitHub job reporting `GCP_CREDENTIALS` + `GCP_PROJECT` and `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY` missing in that repository context. Earlier `eks-metered` attempts **39105258741**, **39104347206**, **39103446883** failed October 18. Earlier `gke-metered` attempts **39101574903**, **39100686388**, **39099797654** failed October 18. These failures do not prove secrets are *still* absent on November 9.
- The October 18 AWS failure is documented as an account-level **explicit deny from a service-control policy** while the account was on a restricted plan; correct credentials alone do not lift an organization policy. The October 18 Google failure is documented as a **truncated service-account JSON key**. A new zero-cost preflight is needed to distinguish unchanged blockers from repaired access.

## Required evidence before publishing a cloud number

1. Inspect fresh GitHub Actions lists for `cloud-check`, `eks-metered`, `gke-metered`, and conductor runs, including the newest timestamps and job-level conclusions; do not rely on the October ledger.
2. Confirm queue switches remain on; examine the latest cloud preflight job **without exposing any secret values**. If the check is absent or stale, use only an authorized **zero-cost** preflight, not a metered cluster creation. Check account-level AWS service-control-policy restriction separately from IAM access and regional EC2/EKS quotas.
3. On Google, verify service-account JSON format, active project, login, GKE API enablement, roles, quota and machine availability. On AWS, verify account/organization policy, plan eligibility, authentication, EKS/EC2/CloudFormation access, quota and region.
4. Only after a successful preflight and cost approval, dispatch a one-repetition native/Omni shakedown for each provider. Preserve GitHub run URL, execution SHA, V26 engine fingerprint, workload, watch arm where relevant, measured work, p95/p99, failures, node-hours, billed-resource model, uncertainty and teardown receipt. Then run the preregistered repetitions subject to cost gates.
5. Update the generated state of play, run ledger and website benefit feed **from new receipts**, never by editing benchmark percentages or borrowing Azure numbers to stand for AWS or GCP.

**Unverified on November 9:** whether the repository currently has the complete four provider secrets, whether an AWS paid/eligible plan exists, whether fresh checks have passed, and whether a new AWS or GCP measurement run has succeeded. The available GitHub connector in this review could read repository files but did not furnish an exhaustive live workflow-runs listing. No current absence or success is inferred.

**Workflow links:** [cloud-check](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/workflows/cloud-check.yml), [AWS EKS](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/workflows/eks-metered.yml), [Google GKE](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/workflows/gke-metered.yml), [grid conductor](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/workflows/grid.yml).

---

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
