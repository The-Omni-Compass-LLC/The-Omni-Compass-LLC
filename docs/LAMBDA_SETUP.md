# The GPU on Lambda: setting it up, click by click

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This connects GitHub to a Lambda Cloud account so one button, the **`lambda-gpu`** workflow, can rent one GPU machine, run
the GPU test on it at the exact commit the button is pressed on (`scripts/gpu_8card.sh` on eight cards, or
`scripts/gpu_rented_run.sh` on one), bring every result file back as the run's artifact, and give the machine back. The GPU
runs start from the branch **`gpu-omni-v18`** (the engine that stands; the run's page prints the exact commit). The design is
`docs/GPU_PREREGISTRATION.md`; what each stage measures is `docs/GPU_RUN_GUIDE.md`, sections C and D.

About ten minutes, once. Lambda bills the card on file from the moment a machine starts until it is given back; nothing
here starts a machine until a dry run has shown the price and the run is started again with `dry_run` set to `no`.

## 1. A Lambda account with a card

1. On the laptop, open **cloud.lambda.ai** and click **Sign up** (or **Log in**).
2. Add a card under **Settings**, **Billing**. Lambda rents no machine to an account without one.

## 2. The two keys, made in Lambda

**The API key** (it lets GitHub rent and give back a machine):

1. In Lambda's menu on the left, click **API keys**, then **Generate API key**. Name it `omni-github`.
2. Lambda shows the key once. Leave that page open for step 3.

**The SSH key** (it lets GitHub log in to the machine it rented):

1. In the menu on the left, click **SSH keys**, then **Add SSH key**, then **Generate a new key**.
2. Name it `omni-key`. Lambda downloads a file, **omni-key.pem**, to the laptop's **Downloads** folder. That file is the
   private half; Lambda keeps the public half under the name `omni-key`.

Never copy either key from a screen by selecting it: a long block is cut short when it is selected (on 18 October the
Google key was stored cut short that way, and every Google set failed at the login). Use the copy button for the API key
and the downloaded file for the SSH key.

## 3. Put the three secrets in GitHub

1. Open the repository on GitHub, click **Settings** (the repository's tab, at the top right), then on the left
   **Secrets and variables**, then **Actions**.
2. **New repository secret**. Name: `LAMBDA_API_KEY`. Secret: the API key from step 2. **Add secret**.
3. On the laptop, open **Downloads**, right-click **omni-key.pem**, **Open with**, **Notepad** (on a Mac: **TextEdit**).
   Press **Ctrl+A** (select all), then **Ctrl+C** (copy): the whole file, from `-----BEGIN` to `PRIVATE KEY-----`.
4. **New repository secret**. Name: `LAMBDA_SSH_PRIVATE_KEY`. Secret: click in the box, **Ctrl+V**. **Add secret**.
5. **New repository secret**. Name: `LAMBDA_SSH_KEY_NAME`. Secret: `omni-key` (exactly the name given in step 2).
   **Add secret**.

Keep **omni-key.pem** in a safe folder on the laptop (it also lets you log in to a rented machine yourself) and never send
it to anyone. These three are passwords for this one purpose: never paste them anywhere but GitHub.

## 4. The dry run (free)

1. On GitHub, **Actions**, then **lambda-gpu** on the left, then **Run workflow** (on the right).
2. Branch: **gpu-omni-v18**. `test`: `1card`. `mode`: `fast`. Leave `dry_run` at **yes**. Click **Run workflow**.
3. In about a minute the run's page shows, at no cost:
   - the SSH key check: "SSH key omni-key: Lambda holds it, and the stored private key is its other half";
   - the price an hour, the regions with a machine free now, and the estimate for the hour budget plus one hour;
   - "Dry run: the secrets and the key pair are ready; nothing rented."

   A red run says which of the three secrets to fix (a missing secret, a key name Lambda does not hold, a private key that
   is not the other half of `omni-key`), and nothing is rented. "No machine of this type is free in any region now" is
   Lambda's stock at that moment: try again later, or name another `region` or `instance_type`.

## 5. The real runs

The same button with `dry_run` set to **no**. The `max_cost` box (400 by default) is a ceiling in US dollars for the hour
budget plus one hour: above it nothing is rented.

| `test` `mode` | What runs | Hour budget (given back by) | At Lambda's list price |
|---|---|---|---|
| `1card` `fast` | the compute counted run on one A10 | 8 h (9 h) | one A10 $1.29 an hour on 24 October: about $12 |
| `1card` `stacks` | the whole stacks with the card inside: the wire check and smoke, then the seven organisms at 1, 10 and 100 copies, native and Omni-Compass, the preregistered 5, 3 and 2 repetitions by size (`hil_profile` `standard`) | 32 h (33 h) | about $43 a run at most; A, B and C (`tag`) each rent their own A10 and run side by side |
| `1card` `stacks-full` | the same stacks with the card fully loaded inside them (`docs/GPU_PREREGISTRATION.md`, amendment 16): more requests offered than the card serves, so the work done inside the same rented time can rise | 32 h (33 h) | about $43 a run at most; A, B and C side by side |
| `8card` `pooled` (default) | every stage on eight A100 cards, repetitions pooled across the cards | 10.5 h (11.5 h) | $22.32 an hour on 1 November (the price the launch printed; it was $14.32 earlier): about $257 at most |
| `8card` `fast` | a short look, never the result to show | 4 h (5 h) | about $112 at most |
| `1card` `full` | the whole one-card test | 32 h (33 h) | about $43 |
| `8card` `full` | the whole design on eight cards | 26 h (27 h) | about $603 at most (over the button's default $400 ceiling: raise `max_cost` to run it) |

The price the dry run prints is Lambda's own at that moment; the table is an example. The one-card and the eight-card tests
may run at the same time (one run of each at once; a second press of the same test waits for the first, unless its `tag`,
A, B or C, differs: each tag is its own machine).

The machine is given back when the run prints its last line, or at the hour budget plus one hour whatever happens, or at the
end of the workflow if anything before it failed. Each give-back is acknowledged by Lambda; if Lambda does not acknowledge it,
the run turns red and says so. Then, by hand: **cloud.lambda.ai**, **Instances**, tick the machine (its name starts
`omni-`), **Terminate**.

A run cancelled by hand keeps watching its machine (the watch jobs run on through a cancel, so a give-back is never lost),
and a run whose test stopped early is given back at once by the watch since 24 October. For a machine still left billing
under an older run: **Actions**, **lambda-gpu**, **Run workflow**, **test** `giveback`, **give_back** `omni-1card-` (or
`omni-8card-`, or the machine's whole name). It gives back every machine whose name starts so, rents nothing, and never
touches a machine launched by hand on Lambda's page; the stuck run then sees its machine gone and ends, and the next run of
that test starts.

## 6. Afterwards

The results are the run's artifacts (`lambda-gpu-watch*-<run id>`); the founder hears what they say before anything goes up.
To remove GitHub's access: in Lambda, **API keys**, delete `omni-github`, and **SSH keys**, delete `omni-key`; then delete
the three secrets in GitHub.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
