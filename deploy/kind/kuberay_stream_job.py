# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""One job of the batch stream on Ray (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 7; deploy/kind/kuberay-job.yaml): TASKS
tasks, at most PARALLEL at a time, each hashing MB megabytes of zeros as one pod of the Kubernetes stream does
(deploy/kind/batch-stream-job.yaml), each asking one Ray processor, which the Ray autoscaler meets by adding worker pods.
Its last line, OMNI_TIMES, gives the moment its first task began and its last task ended, read by the harness at the
window's end (scripts/kind_batch_queue.sh, PHASE=end). Runs on the head, in the Ray image; reads nothing else."""
import argparse
import json
import subprocess
import time

import ray

ap = argparse.ArgumentParser()
ap.add_argument("--tasks", type=int, default=10)
ap.add_argument("--parallel", type=int, default=5)
ap.add_argument("--mb", type=int, default=3000)
a = ap.parse_args()
ray.init()


@ray.remote(num_cpus=1)
def work(mb):
    t0 = time.time()
    subprocess.run(f"dd if=/dev/zero bs=1M count={mb} 2>/dev/null | sha256sum", shell=True, check=True,
                   stdout=subprocess.DEVNULL)
    return t0, time.time()


pending, times, sent = [], [], 0
while sent < a.tasks or pending:
    while sent < a.tasks and len(pending) < a.parallel:
        pending.append(work.remote(a.mb))
        sent += 1
    done, pending = ray.wait(pending, num_returns=1)
    times += ray.get(done)
print("OMNI_TIMES " + json.dumps({"first": min(t[0] for t in times), "last": max(t[1] for t in times), "tasks": len(times)}),
      flush=True)

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
