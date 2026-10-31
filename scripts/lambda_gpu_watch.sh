#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Watch one rented Lambda machine running an Omni-Compass GPU run (.github/workflows/lambda-gpu.yml), for at most
# MINUTES, and give it back the moment the run is over:
#   the run printed its last line ("send this one file back"): fetch every result file, give the machine back;
#   the hour budget plus one hour has passed (the deadline): fetch whatever results exist, give the machine back;
#   the run stopped without its last line (it refused to start, or died): fetch what exists, give the machine back;
#   the machine is already gone: nothing to do.
# Writes the state (done, deadline, gone or watching) to OUT/state. The key never leaves the environment.
# Usage: bash scripts/lambda_gpu_watch.sh ID IP DEADLINE_EPOCH MINUTES OUT     (SSH_KEY: the private key file; LOGIN: the
# machine's login user, ubuntu by default; GIVE_BACK=no keeps a machine launched by hand on Lambda's page after the run,
# .github/workflows/lambda-attach.yml)
set -uo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
ID="$1"; IP="$2"; DEADLINE="$3"; MINUTES="$4"; OUT="$5"
EVERY="${EVERY:-600}"
mkdir -p "$OUT"
LOGIN="${LOGIN:-ubuntu}"
SSH=(ssh -i "${SSH_KEY:?set SSH_KEY}" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 -o ServerAliveInterval=30 "$LOGIN@$IP")
SCP=(scp -i "$SSH_KEY" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20)
give_back() { if [ "${GIVE_BACK:-yes}" = no ]; then echo "the machine is kept (GIVE_BACK=no): it bills until its owner gives it back"; return 0; fi
  python3 scripts/lambda_gpu.py terminate "$ID" || python3 scripts/lambda_gpu.py terminate "$ID"; }
fetch() {   # every result file the run packed, its log, the machine's own card list, and always the live result folders as they
            # stand: the whole stacks (results/hil) write each arm as it ends but are packed only when they finish, so a run cut
            # at its deadline came back without one arm of them (lambda-gpu runs 40143765437, 40143770324, 40143775773: 24 hours
            # of stacks on each card, none fetched)
  "${SCP[@]}" "$LOGIN@$IP:omni/results/gpu/omni-*.tar.gz" "$OUT/" 2>/dev/null || true
  "${SCP[@]}" "$LOGIN@$IP:omni/run.log" "$OUT/run.log" 2>/dev/null || true
  "${SSH[@]}" "nvidia-smi --query-gpu=index,name,power.limit,power.default_limit --format=csv" > "$OUT/cards.csv" 2>/dev/null || true
  "${SSH[@]}" "cd omni && tar czf /tmp/omni-live.tar.gz --ignore-failed-read --exclude='results/gpu/omni-*.tar.gz' results/gpu results/hil run.log 2>/dev/null; true" || true
  "${SCP[@]}" "$LOGIN@$IP:/tmp/omni-live.tar.gz" "$OUT/omni-live.tar.gz" 2>/dev/null || true
  ( cd "$OUT" && sha256sum ./* > SHA256SUMS.txt 2>/dev/null ) || true
}
T_END=$(( $(date +%s) + MINUTES * 60 ))
while :; do
  st=$(python3 scripts/lambda_gpu.py status "$ID" 2>/dev/null | awk '{print $3}')
  if [ "$st" = terminated ]; then echo gone > "$OUT/state"; echo "machine $ID is already given back"; exit 0; fi
  if "${SSH[@]}" "grep -q 'send this one file back' omni/run.log" 2>/dev/null; then
    echo "the run is over: fetching the results"; fetch; give_back; echo done > "$OUT/state"; exit 0
  fi
  # the run stopped without its last line (it refused to start, or died): nothing more will come, so the card goes back now
  # instead of billing to the deadline; only a clear answer counts (a lost connection is not a stopped run)
  # the brackets keep the pattern from matching the shell that runs this very check (its own command line holds the
  # names; unbracketed, every check read "running" and a stopped run kept its card to the deadline: 24 October)
  alive=$("${SSH[@]}" "pgrep -f '[g]pu_rented_run.sh|[g]pu_8card.sh' > /dev/null && echo running || echo stopped" 2>/dev/null)
  if [ "$alive" = stopped ] && ! "${SSH[@]}" "grep -q 'send this one file back' omni/run.log" 2>/dev/null; then
    echo "the run stopped before its last line: fetching what exists and giving the machine back"
    "${SSH[@]}" "tail -n 5 omni/run.log" 2>/dev/null | sed 's/^/  run: /'
    fetch; give_back; echo done > "$OUT/state"; exit 0
  fi
  if [ "$(date +%s)" -ge "$DEADLINE" ]; then
    echo "the deadline has passed: fetching what exists and giving the machine back"; fetch; give_back
    echo deadline > "$OUT/state"; exit 0
  fi
  # a watch that hands over to the next takes what exists first, so every watch's artifact holds the run so far
  if [ "$(date +%s)" -ge "$T_END" ]; then fetch; echo watching > "$OUT/state"; echo "still running; the run so far fetched; the next watch carries on"; exit 0; fi
  "${SSH[@]}" "tail -n 2 omni/run.log" 2>/dev/null | sed 's/^/  run: /' || echo "  (no answer from the machine this time)"
  sleep "$EVERY"
done
