# The meter kit: the Kubernetes benchmark on a rented bare-metal machine, step by step

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

What it does: runs the same Kubernetes benchmark as GitHub's machines (native, and Omni-Compass on top of native), on
a machine whose processor has its own energy meter, and reads that meter and Kepler beside every run
(`docs/METER_PREREGISTRATION.md`). The energy rows then become a measurement (class P) instead of the declared model.

What it needs: one rented **bare-metal** server (a "dedicated server" or "bare metal", never a "VPS", "cloud server" or
"virtual machine": those have no meter), Intel or AMD, 8 cores and 32 GB of memory or more, Ubuntu 24.04.

How long: about 8 hours a run (10 paired repetitions, each arm about 25 minutes). Three runs on one commit (A, B, C)
make the result: about a day of machine time.

What it costs: the server's rent for those hours. Two kinds of offer work: a monthly dedicated server (Hetzner, OVHcloud
and others; roughly €40 to €70 a month with a setup fee) or an hourly bare-metal instance (for example an Amazon EC2
`c5.metal`, roughly $4 an hour). The order page shows today's price; these are not quotes.

## Step 1. Rent the server

1. On the provider's site, choose a dedicated (bare-metal) server with an Intel Xeon or AMD EPYC/Ryzen processor, at least
   8 cores and 32 GB of memory.
2. Operating system: **Ubuntu 24.04**.
3. Order it. The provider sends the server's address and a root password, or asks for an SSH key.

## Step 2. Log in

On your laptop, open a terminal (Terminal on a Mac; PowerShell on Windows) and type, with your server's address:

```bash
ssh root@SERVER_ADDRESS
```

Type `yes` the first time, then the password from the provider's email.

## Step 3. Get the code at the exact commit

Copy and paste these lines one at a time (the commit is the exact one named for the run; the archive of raw runs stays out, so
the download is small):

```bash
apt-get update && apt-get install -y git
git clone --filter=blob:none --no-checkout https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC.git
cd The-Omni-Compass-LLC
git sparse-checkout set --no-cone '/*' '!/results/live/raw/*'
git checkout COMMIT
```

## Step 4. Start the run

```bash
sudo nohup bash scripts/metal_kind_run.sh 10 900 > metal.log 2>&1 &
tail -f metal.log
```

The first lines check the machine. If it says *"this machine is a virtual machine"* or *"no processor meter here"*, the
server is not bare metal: cancel it and rent a dedicated one. Otherwise it installs what it needs and starts the 10
repetitions. `Ctrl+C` stops watching; the run keeps going. You can close the laptop and log in again later
(`ssh root@SERVER_ADDRESS`, then `cd The-Omni-Compass-LLC && tail -f metal.log`).

## Step 5. Send the result back

At the end the log prints one line:

```
== send this one file back: /root/The-Omni-Compass-LLC/metal-<time>.tar.gz
```

On your laptop (a new terminal, not the server):

```bash
scp root@SERVER_ADDRESS:/root/The-Omni-Compass-LLC/metal-*.tar.gz .
```

Send that file in the chat. Then run Step 4 again for run B, and again for run C (same server, same commit). After run
C, cancel or delete the server on the provider's site so it stops billing.

## What comes back

Each file holds every repetition's raw files, the run's table (`LIVE_REPS.md`) and SHA-256 sums. The three runs make the
three-run table with `tools/confirm_abc.py`: the machine's own energy reading judged like every other gauge (lower or
or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given), STEADY (no difference beyond the noise), or the runs disagree), Kepler's readings shown beside it.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
