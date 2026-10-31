# The bill on Amazon Web Services: setting it up, click by click

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Status (24 October): not yet run, its queue switched off.** The account is on Amazon's Free plan, which Amazon will not raise before the $100 credit is spent or the account is six months old. Everything here stays ready, wired as Azure's sets run (the same harness and 60 s beat, 100 paired repetitions a set under the stopping rule, the $0 check first); the founder switches it on once the account is on the Paid plan (section 1a), and nothing is built or billed before.

This connects GitHub to an Amazon Web Services (AWS) account so two workflows can run the same tests Azure runs:

- **`eks-metered`**: a real Amazon Elastic Kubernetes Service cluster, native Kubernetes (with its own cluster autoscaler)
  against the same with Omni-Compass on top, the machines Amazon bills counted every 15 seconds, the organisms with the
  cluster inside at 1, 10 and 100 copies (`organism`, `organism_scale`), everything deleted at the end; every set with the
  whole engine at the max on top of the cloud's own autoscaler, the bill judged beside the work (31 October). The same
  design as Azure's `aks-metered` (`docs/K8S_COMPASS_PREREGISTRATION.md`).
- **`cloud-organism`** with `cloud` = `aws`: the big organisms (the whole tower and the four stacked, the
  real cluster inside, at 100 copies) on one rented 8-processor machine, the same test Azure's `big-organism-detached` runs.
  With `test` = `direct` the same button runs Omni direct's three arms instead (native, Omni on native and Omni direct,
  no Kubernetes; `docs/OMNI_V18.md`), `reps` runs on the one machine; it starts only on the founder's word.

About fifteen minutes, once. New accounts get **$100 of credit at sign-up and up to $100 more** for trying services, used
before the card.

## 1. An AWS account

1. On the laptop, open **aws.amazon.com/free** and click **Create a Free Account** (or **Create an AWS account**).
2. Enter an e-mail address and an account name (`Omni-Compass`), click **Verify email address**, and type the code Amazon
   e-mails you.
3. Choose a password for the root user.
4. Contact information: **Business** (The Omni-Compass LLC) or **Personal**, the address and phone.
5. **Choose the Paid plan** if Amazon asks you to pick a plan. Your credits still pay first; the Free plan blocks services
   these tests need (the Kubernetes service among them).
6. Enter a card, then confirm the phone number with the code Amazon sends.
7. Support plan: **Basic support - Free**. Click **Complete sign up**, then **Go to the AWS Management Console** and sign in
   as the root user.

## 1a. An account already on the Free plan: move it to the Paid plan

An account that chose the Free plan cannot run these tests: Amazon puts a policy above every login of the account that
refuses every machine read and every machine (on 18 October each Amazon set stopped there, at no cost, with "explicit deny
in a service control policy"). Moving to the Paid plan removes it; the credits stay and still pay first.

1. Sign in to the console as the root user (the e-mail and password of step 1).
2. At the top of the console click **Upgrade plan** (beside the Free plan's credit and days left), or search
   **Billing and Cost Management**, open it, and click **Upgrade plan** on its home page.
3. Read the page, and click **Upgrade to paid plan** (or **Upgrade plan**) to confirm.

Nothing else changes: the login made for GitHub (step 2) and the two secrets (step 3) stay as they are. Within the hour the
conductor's check reads the account again and the sets start on their own.

## 2. A login for GitHub (an IAM user)

1. In the search bar at the top of the console type **IAM** and open it.
2. On the left, **Users**, then **Create user**. User name: `omni-compass-github`. Do **not** tick console access.
   **Next**.
3. **Attach policies directly**. Tick **AdministratorAccess** (the tests build whole Kubernetes clusters, which needs EKS,
   EC2, CloudFormation and roles; this user is used only by GitHub, and you delete it when the tests are done). **Next**,
   **Create user**.
4. Click the new user **omni-compass-github**, open the **Security credentials** tab, and under **Access keys** click
   **Create access key**.
5. Choose **Application running outside AWS** (or **Other**), **Next**, **Create access key**.
6. The page shows an **Access key** (starts with `AKIA`) and a **Secret access key**. Keep the page open for the next step;
   the secret is shown only once. These two are passwords for this one purpose: never paste them anywhere but GitHub.

## 3. Put the two secrets in GitHub

1. Open the repository on GitHub, click **Settings** (the repository's tab, at the top right), then on the left
   **Secrets and variables**, then **Actions**.
2. **New repository secret**. Name: `AWS_ACCESS_KEY_ID`. Secret: the Access key. **Add secret**.
3. **New repository secret**. Name: `AWS_SECRET_ACCESS_KEY`. Secret: the Secret access key. **Add secret**.

That is all. Within the hour the conductor runs Amazon's check at no cost (**Actions**, **cloud-check**, the run titled
`cloud-check amazon`): the keys log in, the account can read and rent machines (not the Free plan), the instance type is
offered and the processor quota holds a set. When it passes, the sets start on their own on the engine that stands (branch
`main`; `v11` is kept in step with it), and no result goes up before it has been read. When it fails, it says which of
these to fix, and nothing is built or billed.

## 4. What it costs

Amazon's list prices (us-east-1, on demand): a worker of the Kubernetes test (`m5.large`) about $0.096 an hour, up to 4
workers an arm, plus about $0.10 an hour for each cluster's control plane, about $10 to $25 for a full five-repetition set;
the big-organism machine (`m6i.2xlarge`) about $0.38 an hour, about $15 for its 39-hour ceiling. The credits pay first.
Every cluster and machine is deleted when its run ends, whatever happens.

A set needs 10 processors at once (5 machines of 2). New accounts can start with less. When the check finds the quota
short it asks Amazon for the increase itself (once; it waits for Amazon's answer before asking again), and Amazon usually
answers within a day. To ask by hand: in the console search **Service Quotas**, open **Amazon Elastic Compute Cloud (Amazon
EC2)**, **Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances**, **Request increase at account level**, ask for
64, **Request**. The set is never shrunk to fit.

## 5. Afterwards

To remove GitHub's access: in IAM, **Users**, tick **omni-compass-github**, **Delete**; and delete the two secrets in
GitHub.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
