#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The Gödel scheduler's image for the batch rig (BATCH_QUEUE=godel; docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 8;
# register row 93). Gödel publishes no release and no image, so its image is built once per runner, before the first arm,
# from its source at the pinned commit with the project's own Dockerfile (docker/godel-local.Dockerfile, which builds every
# component from the vendored modules), as its own setup guide builds it (make docker-images); the image is tagged
# godel-local:latest, the name its own manifests run with imagePullPolicy Never, and its ID is written beside the source
# (GODEL_SRC/IMAGE_ID), which scripts/kind_batch_queue.sh checks before it loads the image into each arm's control plane.
set -euo pipefail
GODEL_COMMIT="${GODEL_COMMIT:-$(sed -n 's/^GODEL_COMMIT="\${GODEL_COMMIT:-\([0-9a-f]\{40\}\)}"$/\1/p' scripts/kind_batch_queue.sh)}"
GODEL_SRC="${GODEL_SRC:-${RUNNER_TEMP:-/tmp}/godel-src}"
[ -n "$GODEL_COMMIT" ] || { echo "the pinned Gödel commit could not be read from scripts/kind_batch_queue.sh"; exit 1; }
rm -rf "$GODEL_SRC"; git init -q "$GODEL_SRC"
for t in 1 2 3; do   # GitHub serves a commit by its full SHA; a refused fetch is tried again
  git -C "$GODEL_SRC" fetch -q --depth 1 https://github.com/kubewharf/godel-scheduler "$GODEL_COMMIT" && break
  [ "$t" = 3 ] && { echo "Gödel's source at $GODEL_COMMIT could not be fetched"; exit 1; }; sleep 15
done
git -C "$GODEL_SRC" -c advice.detachedHead=false checkout -q FETCH_HEAD
[ "$(git -C "$GODEL_SRC" rev-parse HEAD)" = "$GODEL_COMMIT" ] || { echo "the fetched source is not the pinned commit"; exit 1; }
for t in 1 2; do   # the build's base images come from Docker Hub; a refused pull is tried once more
  (cd "$GODEL_SRC" && docker build -q -t godel-local:latest -f docker/godel-local.Dockerfile .) > "$GODEL_SRC/BUILD.log" 2>&1 && break
  [ "$t" = 2 ] && { echo "Gödel's image could not be built"; tail -40 "$GODEL_SRC/BUILD.log"; exit 1; }; sleep 30
done
docker image inspect godel-local:latest --format '{{.Id}}' > "$GODEL_SRC/IMAGE_ID"
echo "Gödel $GODEL_COMMIT built from docker/godel-local.Dockerfile: godel-local:latest $(cat "$GODEL_SRC/IMAGE_ID")"
# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
