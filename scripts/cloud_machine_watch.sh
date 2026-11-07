#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Watch one rented Google Cloud or Amazon machine running the detached big-organism test (.github/workflows/
# cloud-organism.yml, scripts/organism_detached.sh) for at most MINUTES, and give it back the moment the test is over:
#   every repetition finished (ALL_DONE): fetch every cell, give the machine back;
#   the hour budget has passed (the deadline): fetch whatever cells exist, give the machine back;
#   the machine is already gone: nothing to do.
# Each GitHub job makes its own key and lets it in through the cloud's API (scripts/cloud_machine.py key); the private key
# never leaves this job. Writes the state (done, deadline, gone or watching) to OUT/state.
# Usage: bash scripts/cloud_machine_watch.sh ID DEADLINE_EPOCH MINUTES OUT
set -uo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
ID="$1"; DEADLINE="$2"; MINUTES="$3"; OUT="$4"
EVERY="${EVERY:-600}"
CM=(python3 scripts/cloud_machine.py)
mkdir -p "$OUT"
K="${RUNNER_TEMP:-/tmp}/watch-key-$$"
rm -f "$K" "$K.pub"; ssh-keygen -q -t ed25519 -N "" -f "$K" -C "omni-watch"
USER_ON=$("${CM[@]}" user "$ID")
let_in() { "${CM[@]}" key "$ID" --pubkey "$K.pub" >/dev/null 2>&1; }
addr() { "${CM[@]}" status "$ID" 2>/dev/null | awk '{print $3}'; }
give_back() { "${CM[@]}" terminate "$ID" || "${CM[@]}" terminate "$ID"; }
fetch() {   # every cell, the detached log, and the commit the machine ran; partial if the test was cut
  let_in; local ip; ip=$(addr)
  [ -n "$ip" ] || return 0
  local S=(ssh -i "$K" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 -o ServerAliveInterval=30 "$USER_ON@$ip")
  "${S[@]}" "cd omni && tar czf /tmp/omni-cells.tar.gz cells detached.log COMMIT 2>/dev/null; true" || true
  let_in
  scp -i "$K" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 "$USER_ON@$ip:/tmp/omni-cells.tar.gz" "$OUT/" 2>/dev/null || true
  if [ -f "$OUT/omni-cells.tar.gz" ]; then tar xzf "$OUT/omni-cells.tar.gz" -C "$OUT" && rm -f "$OUT/omni-cells.tar.gz"; fi
  ( cd "$OUT" && find . -type f ! -name SHA256SUMS.txt -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt 2>/dev/null ) || true
}
T_END=$(( $(date +%s) + MINUTES * 60 ))
while :; do
  st=$("${CM[@]}" status "$ID" 2>/dev/null | awk '{print $2}')
  if [ "$st" = gone ]; then echo gone > "$OUT/state"; echo "machine $ID is already given back"; rm -f "$K" "$K.pub"; exit 0; fi
  let_in; ip=$(addr)
  S=(ssh -i "$K" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 -o ServerAliveInterval=30 "$USER_ON@$ip")
  if [ -n "$ip" ] && "${S[@]}" "test -f omni/ALL_DONE" 2>/dev/null; then
    echo "every repetition is over: fetching the cells"; fetch; give_back; echo done > "$OUT/state"; rm -f "$K" "$K.pub"; exit 0
  fi
  if [ "$(date +%s)" -ge "$DEADLINE" ]; then
    echo "the hour budget has passed: fetching what exists and giving the machine back"; fetch; give_back
    echo deadline > "$OUT/state"; rm -f "$K" "$K.pub"; exit 0
  fi
  if [ "$(date +%s)" -ge "$T_END" ]; then echo watching > "$OUT/state"; echo "still running; the next watch carries on"; rm -f "$K" "$K.pub"; exit 0; fi
  [ -n "$ip" ] && "${S[@]}" "tail -n 2 omni/detached.log" 2>/dev/null | sed 's/^/  run: /' || echo "  (no answer from the machine this time)"
  sleep "$EVERY"
done
