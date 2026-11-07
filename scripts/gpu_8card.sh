#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The 8-GPU result, one command on a rented machine with several NVIDIA cards (docs/GPU_RUN_GUIDE.md, section D):
#
#   sudo bash scripts/gpu_8card.sh            the whole design, about 17 to 18 hours
#   sudo POOLED=1 bash scripts/gpu_8card.sh   every stage, repetitions pooled across the cards, about 9 to 10 hours
#   sudo FAST=1 bash scripts/gpu_8card.sh     the short design, about 3.5 hours (what only a full server shows)
#
# Every card on the machine runs the whole card test at the same time (scripts/gpu_rented_run.sh with GPU=<card>): its
# own wire check, envelope, smoke, the two preregistered counted runs (compute and AI token generation) and the
# operator's power cap underneath, each card its own firmware alone against the firmware with Omni-Compass on top, on
# the same committed code. The cards share one machine, its power supply, its cooling and its neighbours' heat, as in a
# real server. Each card starts its arm rotation one step later than the card before it, so at any moment some cards
# run native and some run Omni-Compass, and no arm always meets the same neighbours.
# Then, with every card idle again: the GPU fault drill once, on card 0 (the master switch stops every governor on the
# machine, so it never runs while the cards measure). Then one pooled table per workload: every repetition of every
# card, paired within its own card (tools/gpu_reps.py), and each card's own table beside it.
#
# Last, the whole server as one: a language model served across every card at once (scripts/gpu_vllm.sh with GPU=all
# cards: vLLM tensor parallel, one Omni-Compass governor per card, the server's total GPU energy), SKIP_LLM=1 skips it.
# Then the whole stacks with a real card inside: the six organisms at 1x, 10x and 100x copies (no 1,000x), full
# repetitions, each organism on its own card at the same time (SKIP_HIL=1 skips it; HIL_ARGS passes options through).
# CARDS (default: every card nvidia-smi lists), SKIP_DECODE=1, SKIP_CAP=1, SKIP_DRILL=1 as in gpu_rented_run.sh.
set -uo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
cd "$(dirname "$0")/.."
SMI="${NVIDIA_SMI:-nvidia-smi}"; PY="${PYTHON:-python3}"
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
if [ -n "${POOLED:-}" ]; then
  # every stage of the whole design, with the repetitions pooled across the cards (amendment 10): each card 3
  # repetitions of each counted run (24 paired repetitions per test on 8 cards, pooled, against 10 on one card), 2 of
  # each power cap load, one smoke round, the six organisms one repetition per size on their own card, and the model
  # across every card 3 times. Nothing is skipped
  export SMOKE_REPS="${SMOKE_REPS:-1}" REPS_CONFIRM="${REPS_CONFIRM:-3}" REPS_CAP="${REPS_CAP:-2}" \
         HIL_REPS_BY_SCALE="${HIL_REPS_BY_SCALE:-1,1,1}" REPS_LLM="${REPS_LLM:-3}"
  echo "== POOLED: every stage; 3 repetitions per card per counted run, 2 per power cap load, 1 per organism size"
fi
if [ -n "${FAST:-}" ]; then
  # the short design (amendment 10): what only a full server shows, about 3.5 hours. Each card 3 repetitions of the
  # compute counted run (24 paired repetitions on 8 cards, pooled), one smoke round, one model across every card with
  # 3 repetitions. AI token generation and the power cap underneath are measured on the one-card machine
  export SMOKE_REPS="${SMOKE_REPS:-1}" REPS_CONFIRM="${REPS_CONFIRM:-3}" SKIP_DECODE="${SKIP_DECODE:-1}" \
         SKIP_CAP="${SKIP_CAP:-1}" REPS_LLM="${REPS_LLM:-3}" SKIP_HIL="${SKIP_HIL:-1}"
  echo "== FAST: 3 repetitions per card, compute, then one model across every card"
fi
[ "$(id -u)" = 0 ] || [ -n "${SIM:-}" ] || { echo "run with sudo: setting the power limit needs root"; exit 1; }
command -v "$SMI" >/dev/null || { echo "nvidia-smi not found: this machine has no NVIDIA driver"; exit 1; }
CARDS="${CARDS:-$($SMI --query-gpu=index --format=csv,noheader | tr -d ' ' | paste -sd, -)}"
IFS=, read -r -a C <<< "$CARDS"
echo "== $(( ${#C[@]} )) cards: ${CARDS}"
$SMI --query-gpu=index,name,power.limit,power.default_limit --format=csv,noheader
mkdir -p results/gpu
OUT="results/gpu/8card-$STAMP"; mkdir -p "$OUT"
echo "$CARDS" > "$OUT/cards.txt"

# The time budget: the run can never go past MAX_HOURS (default by design: POOLED 10.5, FAST 4, the whole design 26).
# At the budget the master switch is pulled (every governor hands its card back to the card's own settings), every
# stage still measuring is stopped, the stages not yet started are skipped, and what finished is packed as usual.
# Lambda bills until the instance is terminated: terminate it when the file to send back is printed.
if [ -n "${POOLED:-}" ]; then DEF_H=10.5; elif [ -n "${FAST:-}" ]; then DEF_H=4; else DEF_H=26; fi
MAX_HOURS="${MAX_HOURS:-$DEF_H}"
T_END=$(( $(date +%s) + $(python3 -c "print(int(float('$MAX_HOURS') * 3600))") ))
echo "== time budget: ${MAX_HOURS} hours; this run stops by $(date -u -d @"$T_END" +%H:%M) UTC whatever happens" | tee "$OUT/BUDGET.txt"
( while [ "$(date +%s)" -lt "$T_END" ]; do sleep 30; [ -f "$OUT/FINISHED" ] && exit 0; done
  echo "== TIME BUDGET REACHED ($MAX_HOURS h): handing every card back and stopping" | tee -a "$OUT/BUDGET.txt"
  touch "$OUT/TIME_UP"
  python3 tools/omni_switch.py off --reason "time budget reached" --wait 60 >> "$OUT/BUDGET.txt" 2>&1
  for pat in "scripts/gpu_rented_run.sh" "scripts/gpu_paired.sh" "tools/gpu_workload.py" "tools/run_hil.py" \
             "scripts/gpu_vllm.sh" "tools/llm_workload.py" "vllm.entrypoints" "scripts/gpu_fault_drill.sh" \
             "query-gpu=timestamp"; do
    pkill -f "$pat" 2>/dev/null || true
  done
  for g in "${C[@]}"; do $SMI -i "$g" -rgc >/dev/null 2>&1 || true; done
) &
budget_pid=$!
timeup() { [ -f "$OUT/TIME_UP" ]; }
pids=()
for i in "${!C[@]}"; do
  g="${C[$i]}"
  echo "== card $g: starting (log $OUT/card-$g.log)"
  GPU="$g" CARD_TAG="card$g" STAMP="$STAMP" SKIP_DRILL=1 SKIP_HIL=1 SKIP_LLM=1 ROT_OFFSET="$i" \
    bash scripts/gpu_rented_run.sh > "$OUT/card-$g.log" 2>&1 &
  pids+=($!)
  sleep 5
done
echo "== all cards running. Progress: tail -f $OUT/card-*.log   (each card prints its own '== rep N, arm X' lines)"
rc=0
for i in "${!pids[@]}"; do
  wait "${pids[$i]}" || { echo "card ${C[$i]} exited $? (see $OUT/card-${C[$i]}.log)"; rc=1; }
done
echo "== every card finished"

if [ -z "${SKIP_DRILL:-}" ] && ! timeup; then
  echo "== the GPU fault drill on card ${C[0]}, every other card idle"
  GPU="${C[0]}" OUT="results/gpu/drill-$STAMP-8card" bash scripts/gpu_fault_drill.sh || rc=1
fi

if [ -z "${SKIP_HIL:-}" ] && ! timeup; then
  # the whole stacks with a real card inside (tools/run_hil.py), every organism at 1x, 10x and 100x copies (no 1,000
  # copies, amendment 13), native and Omni, the full repetitions (5, 3, 2 by size): each organism on its own card, all
  # at once, so the stage takes the time of its longest organism instead of every organism in turn
  read -r -a ORGS <<< "${HIL_ORGS:-compute_ai_cloud physics_robotics_autonomous energy_facility_industrial distribution_specialized stack tower}"
  H="results/hil/run-$STAMP-8card"; mkdir -p "$H"
  echo "== the whole stacks with the card inside: ${#ORGS[@]} organisms, each on its own card, 1x to 100x"
  hpids=(); hcard=()
  for i in "${!ORGS[@]}"; do
    g="${C[$(( i % ${#C[@]} ))]}"
    [ "$i" -lt "${#C[@]}" ] || { wait "${hpids[$(( i - ${#C[@]} ))]}" || rc=1; }   # fewer cards than organisms: wait for a card
    ENV_FLOOR_W=$($PY -c "import json,sys; print(json.load(open(sys.argv[1]))['power_min_w'])" "results/gpu/envelope-$STAMP-card$g.json") \
      NVIDIA_SMI="$SMI" GPU="$g" $PY tools/run_hil.py --out "$H/${ORGS[$i]}" --organisms "${ORGS[$i]}" ${HIL_ARGS:-} \
      > "$H/${ORGS[$i]}.log" 2>&1 &
    hpids+=($!); hcard+=("$g")
    echo "   ${ORGS[$i]} on card $g (log $H/${ORGS[$i]}.log)"
  done
  for i in "${!hpids[@]}"; do wait "${hpids[$i]}" 2>/dev/null || true; done
  for o in "${ORGS[@]}"; do
    [ -f "$H/$o/HIL.md" ] && grep -E "^\| " "$H/$o/HIL.md" | head -12 || echo "   $o: no table (see $H/$o.log)"
  done
fi

if [ -z "${SKIP_LLM:-}" ] && ! timeup; then
  echo "== one model served across all ${#C[@]} cards (vLLM tensor parallel), one Omni-Compass governor per card"
  ENVELOPE="results/gpu/envelope-$STAMP-card${C[0]}.json" GPU="$CARDS" OUT="results/gpu/run-$STAMP-8card-llm" \
    bash scripts/gpu_vllm.sh || rc=1
fi

echo "== pooled tables: every card's repetitions, each paired within its own card"
for kind in "" -decode -cap -cap-full; do
  P="$OUT/pooled${kind:-}"; n=0
  for g in "${C[@]}"; do
    R="results/gpu/run-$STAMP-card$g$kind"
    [ -d "$R" ] || continue
    for r in "$R"/rep-*; do
      [ -d "$r" ] || continue
      mkdir -p "$P"; cp -r "$r" "$P/rep-$(( (g + 1) * 100 + ${r##*/rep-} ))"; n=$((n + 1))   # card 3, rep 7 -> rep-407
    done
  done
  [ "$n" -gt 0 ] || continue
  echo "-- ${kind#-}${kind:+ }(${kind:-compute}) $n repetitions"
  $PY tools/gpu_reps.py "$P" > "$P/table.log" 2>&1 || true
  $PY -c "import json,sys; h=json.load(open(sys.argv[1])).get('headline',{}); print('RESULT, BY RULE, ALL CARDS:', h.get('verdict','(no verdict)'))" \
    "$P/GPU_REPS.json" 2>/dev/null || echo "no pooled table (see $P/table.log)"
done

touch "$OUT/FINISHED"; kill "$budget_pid" 2>/dev/null || true
if timeup; then
  python3 tools/omni_switch.py on >/dev/null 2>&1 || true
  for g in "${C[@]}"; do
    d=$($SMI -i "$g" --query-gpu=power.default_limit --format=csv,noheader,nounits | tr -d ' ' | cut -d. -f1)
    [ -n "${SIM:-}" ] || $SMI -i "$g" -pl "$d" >/dev/null 2>&1 || true
  done
  echo "== stopped at the time budget: the stages that finished are in the file below; the rest did not run" | tee -a "$OUT/BUDGET.txt"
fi
PACK=("$OUT")
for d in results/gpu/*-"$STAMP"-card* results/gpu/drill-"$STAMP"-8card results/gpu/run-"$STAMP"-8card-llm results/hil/run-"$STAMP"-8card; do [ -e "$d" ] && PACK+=("$d"); done
tar czf "results/gpu/omni-8card-$STAMP.tar.gz" "${PACK[@]}"
echo "== send this one file back: results/gpu/omni-8card-$STAMP.tar.gz"
exit $rc
