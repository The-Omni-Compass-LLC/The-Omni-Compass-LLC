# The bill on Google Cloud: setting it up, click by click

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Status (24 October): not yet run, its queue switched off.** The key has not been stored whole. Everything here stays ready, wired as Azure's sets run (the same harness and 60 s beat, 100 paired repetitions a set under the stopping rule, the $0 check first); the founder switches it on once the key is stored whole (section 4), and nothing is built or billed before.

This connects GitHub to a Google Cloud account so two workflows can run the same tests Azure runs:

- **`gke-metered`**: a real Google Kubernetes Engine cluster, native Kubernetes (with Google's own cluster autoscaler)
  against the same with Omni-Compass on top, the machines Google bills counted every 15 seconds, the organisms with the
  cluster inside at 1, 10 and 100 copies (`organism`, `organism_scale`), everything deleted at the end; every set with the
  whole engine at the max on top of the cloud's own autoscaler, the bill judged beside the work (31 October). The same
  design as Azure's `aks-metered` (`docs/K8S_COMPASS_PREREGISTRATION.md`).
- **`cloud-organism`** with `cloud` = `gcp`: the big organisms (the whole tower and the four stacked, the
  real cluster inside, at 100 copies) on one rented 8-processor machine, the same test Azure's `big-organism-detached` runs.
  With `test` = `direct` the same button runs Omni direct's three arms instead (native, Omni on native and Omni direct,
  no Kubernetes; `docs/OMNI_V18.md`), `reps` runs on the one machine; it starts only on the founder's word.

About fifteen minutes, once. New accounts get **$300 of free credit for 90 days**; Google does not charge the card during the
free trial.

## 1. A Google Cloud account with the free credit

1. On the laptop, open **cloud.google.com/free** and click **Get started for free**.
2. Sign in with a Google account (a Gmail address works), or make one.
3. Choose the country, tick the terms, click **Continue**.
4. Enter a card. Google uses it to confirm who you are; the $300 credit is used first.
5. Click **Start my free trial**. The Google Cloud console opens (**console.cloud.google.com**).
6. **Turn on the full account** (the credit stays and is still used first; the free trial otherwise limits how many
   machines run at once and refuses GPUs): at the top of the console click **Activate** (or open the menu ☰, **Billing**,
   then **Upgrade** / **Activate full account**) and confirm.

## 2. A project for Omni-Compass

1. At the top left of the console, click the project picker (next to "Google Cloud").
2. Click **New project**. Name: `omni-compass`. Click **Create**.
3. When it is made, pick it in the project picker. Under the name you see its **Project ID** (for example
   `omni-compass-123456`). Write it down: it is the second secret below.

## 3. Google's own terminal (nothing to install)

1. At the top right of the console, click the **>_** icon (**Activate Cloud Shell**).
2. A terminal opens at the bottom of the page. If it asks to authorize, click **Authorize**.

## 4. One paste: a login for GitHub

Paste this whole block into that terminal and press **Enter** (it takes about a minute). It is safe to paste again: a
login already made is kept, and a fresh key is made each time.

```bash
P=$(gcloud config get-value project)
gcloud services enable container.googleapis.com compute.googleapis.com iam.googleapis.com
gcloud iam service-accounts create omni-compass-github --display-name "Omni-Compass GitHub"
for r in roles/container.admin roles/compute.admin roles/iam.serviceAccountUser; do
  gcloud projects add-iam-policy-binding "$P" --member "serviceAccount:omni-compass-github@$P.iam.gserviceaccount.com" --role "$r" --quiet >/dev/null
done
gcloud iam service-accounts keys create key.json --iam-account "omni-compass-github@$P.iam.gserviceaccount.com"
cloudshell download key.json
```

The browser asks to download **key.json**: click **Download**. Never copy the key from the terminal's screen: a block that
long is cut short when it is selected there (on 18 October the stored key ended part of the way through, and every Google
set failed at the login). Then:

1. On the laptop, open the **Downloads** folder, right-click **key.json**, **Open with**, **Notepad** (on a Mac:
   **TextEdit**).
2. Press **Ctrl+A** (select all), then **Ctrl+C** (copy). The whole file is about 2,300 characters, from `{` to `}`.
3. Back in Cloud Shell, type `rm key.json` and press **Enter**; on the laptop, delete **key.json** from **Downloads** once
   the secret below is saved.

That file is a password for this one purpose: never paste it anywhere but the GitHub secret below. (If the project picker
showed no project, run `gcloud config set project YOUR-PROJECT-ID` first.)

**A new key file by clicks alone** (once the paste above has run, the login exists and only its key is needed again):

1. In the console menu ☰, **IAM & Admin**, then **Service Accounts**.
2. Click **omni-compass-github@…** (the address ends `.iam.gserviceaccount.com`).
3. Open the **Keys** tab, click **Add key**, then **Create new key**, choose **JSON**, click **Create**. The browser
   downloads the key file (its name is the Project ID and some letters, ending `.json`).
4. Open that file in Notepad as in step 1 above, **Ctrl+A**, **Ctrl+C**, and store it as below. On the same **Keys** tab,
   an older key can be deleted with its bin icon.

## 5. Put the two secrets in GitHub

1. Open the repository on GitHub, click **Settings** (the repository's tab, at the top right), then on the left
   **Secrets and variables**, then **Actions**.
2. **New repository secret** (or, when it is already there, the pencil beside it: **Update**). Name: `GCP_CREDENTIALS`.
   Secret: click in the box, **Ctrl+V** (the whole file from step 4). **Add secret** (or **Update secret**).
3. **New repository secret**. Name: `GCP_PROJECT`. Secret: the Project ID from step 2. **Add secret**.

That is all. Within the hour the conductor runs Google's check at no cost (**Actions**, **cloud-check**, the run titled
`cloud-check google`): the key's shape (only its length and missing parts are ever printed, never a character of it), the
login, the machine type and every quota a set needs. When it passes, the sets start on their own on the engine that stands
(branch `main`; `v11` is kept in step with it), and no result goes up before it has been read. When it fails, it says which
of these to fix, and nothing is built or billed.

## 6. Google's limits (quotas)

A set needs, at once, 5 machines of 2 processors (10 processors), their 5 boot disks of 100 GB (500 GB of solid-state disk)
and 6 external addresses in `us-central1`. The check reads each of Google's limits and names any that is short:

- **CPUS_ALL_REGIONS 8**: the free trial (8 processors at once). Activate the full account: at the top of the console
  click **Activate** (or ☰, **Billing**, **Activate full account**) and confirm. The $300 credit stays and pays first.
- **Any other limit short** (`CPUS`, `SSD_TOTAL_GB`, `IN_USE_ADDRESSES`): ☰, **IAM & Admin**, **Quotas & System Limits**;
  search the name the check printed, tick it (region `us-central1` where it asks), **Edit**, ask for what the check said
  is needed or more, **Submit**. Google usually answers within minutes to a day. The set is never shrunk to fit.

## 7. What it costs

Google's list prices (us-central1, on demand): a worker of the Kubernetes test (`e2-standard-2`) about $0.067 an hour, up to
4 workers an arm, about $5 to $15 for a full five-repetition set; the big-organism machine (`e2-standard-8`) about $0.27 an
hour, about $10 for its 39-hour ceiling. All of it comes out of the $300 credit first. Every cluster and machine is
deleted when its run ends, whatever happens.

## 8. Afterwards

To remove GitHub's access: in the console menu ☰ **IAM & Admin**, **Service Accounts**, tick **omni-compass-github**,
**Delete**; and delete the two secrets in GitHub.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
