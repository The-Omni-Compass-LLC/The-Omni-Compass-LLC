#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The robustness test (ROBUST=kill or ROBUST=long in scripts/kind_bench.sh; docs/ROBUSTNESS_PREREGISTRATION.md).
#   kill   at 40% of the window the governor is killed outright (SIGKILL): it cannot hand back. The watchdog running beside
#          it (tools/omni_switch.py watchdog) must find the dead lease and run the governor's recorded restore command. This
#          script asks the cluster every 2 s from the moment of the kill until EVERY setting is at the operator's (HPA target
#          50, the replica range as set, every serving pod's CPU limit as shipped, every worker in service, no
#          omnicompass.io/ record left) and writes the seconds it took. At 50% a second governor is started with the same
#          command line (start_controller, exported by kind_bench.sh) and governs to the end; its pid goes to omni2.pid.
#          Native gets the same time marks and nothing else, so the same window of both arms can be compared.
#   long   no kill; only the sampling below.
# In both, the governor's resident memory (every omni_controller.controller process) is sampled every 15 s from the process
# table into rss.csv; the governor itself is not touched (no engine file changes). Everything is written to robust.log.
set -u
D="${DURATION:?}"; OUT="${OUT_DIR:?}"; LOG="$OUT/robust.log"; MODE="${ROBUST:?}"
t0=$(date +%s)
say() { echo "$(date -u +%s) $*" | tee -a "$LOG"; }
wait_until() { local s=$(( t0 + D * $1 / 100 )); local now; now=$(date +%s); (( s > now )) && sleep $(( s - now )); }
settings() {   # one line: the knob state as the operator should find it
  local target range limits back left
  target=$(kubectl get hpa php-apache -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}' --request-timeout=10s 2>/dev/null)
  range=$(kubectl get hpa php-apache -o jsonpath='{.spec.minReplicas},{.spec.maxReplicas}' --request-timeout=10s 2>/dev/null)
  limits=$(kubectl get pods -l run=php-apache -o jsonpath='{range .items[*]}{.spec.containers[0].resources.limits.cpu}{"\n"}{end}' --request-timeout=10s 2>/dev/null | sort -u | tr '\n' ' ' | sed 's/ $//')
  back=$(kubectl get nodes -l "${WORKER_SEL:-!node-role.kubernetes.io/control-plane}" -o json --request-timeout=10s 2>/dev/null | jq '[.items[] | select(.spec.unschedulable != true and (any(.spec.taints[]?; .key == "omnicompass.io/idle") | not))] | length')
  left=$( { kubectl get hpa php-apache -o json --request-timeout=10s 2>/dev/null | jq -r '.metadata.annotations // {} | keys[] | select(startswith("omnicompass.io/"))'
           kubectl get deployment php-apache -o json --request-timeout=10s 2>/dev/null | jq -r '.metadata.annotations // {} | keys[] | select(startswith("omnicompass.io/"))'; } | tr '\n' ' ' | sed 's/ $//')
  echo "target=$target range=$range limits=$limits workers=$back/${WORKERS:?} left=${left:-none}"
}
native_state() { [ "$1" = "target=50 range=${HPA_RANGE:?} limits=500m workers=${WORKERS}/${WORKERS} left=none" ]; }
# the governor's resident memory, every 15 s, every governor process there is (the first, then the second)
( echo "epoch_s,rss_kb,processes"; while :; do
    pids=$(pgrep -f "omni_controller.controller" 2>/dev/null | paste -sd, -)
    if [ -n "$pids" ]; then rss=$(ps -o rss= -p "$pids" 2>/dev/null | awk '{s+=$1} END{print s+0}'); n=$(echo "$pids" | tr ',' '\n' | grep -c .); else rss=0; n=0; fi
    echo "$(date -u +%s),$rss,$n"; sleep 15; done ) > "$OUT/rss.csv" &
rss_pid=$!
say "robust $MODE: window $D s, start $t0"
if [ "$MODE" = kill ]; then
  wait_until 40
  if [ -n "${NATIVE:-}" ] || [ -z "${OMNI_PID:-}" ]; then
    say "kill mark (native: nothing to kill)"
  else
    say "kill: SIGKILL to governor pid $OMNI_PID (settings before: $(settings))"
    kill -9 "$OMNI_PID" 2>/dev/null || say "kill failed: governor pid $OMNI_PID not found"
    k0=$(date +%s); done_at=""
    while (( $(date +%s) - k0 < 300 )); do
      s=$(settings)
      if native_state "$s"; then done_at=$(date +%s); break; fi
      sleep 2
    done
    if [ -n "$done_at" ]; then say "handed back: every setting at the operator's after $(( done_at - k0 )) s ($s)"
    else say "NOT handed back after 300 s: $(settings)"; fi
    say "watchdog: $(grep -c '"watchdog"' "$OUT/watchdog.log" 2>/dev/null || echo 0) hand-back record(s) so far"
  fi
  wait_until 50
  if [ -z "${NATIVE:-}" ] && [ -n "${OMNI_PID:-}" ]; then
    left=$(( (t0 + D) - $(date +%s) )); iters=$(( left / ${OMNI_INTERVAL:-20} )); (( iters < 1 )) && iters=1
    p2=$(start_controller "$iters" "$OUT/controller2.log" 2>>"$LOG"); echo "$p2" > "$OUT/omni2.pid"
    sleep 2
    if [ -n "$p2" ] && kill -0 "$p2" 2>/dev/null; then say "second governor started: pid $p2, $iters decisions to the end of the window"
    else say "second governor did NOT start (pid '${p2}'): $(tail -3 "$OUT/controller2.log" 2>/dev/null | tr '\n' ' ')"; fi
  else
    say "second-governor mark (native: nothing to start)"
  fi
fi
# run to the end of the window, then stop the sampler
wait_until 100
kill "$rss_pid" 2>/dev/null || true
say "robust $MODE: window end"
