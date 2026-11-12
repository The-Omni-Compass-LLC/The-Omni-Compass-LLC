#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One command that proves the jump generator's sets on the machine it is run on, with nothing taken on trust:
#   1. the engine that stands, named by its fingerprint (tools/omni_version.py);
#   2. the C++ harness built from source (the engine's C++ twins);
#   3. the ledger of every recorded set checked from the records themselves (tools/runs_ledger.py --check);
#   4. one set of 500 runs from a base seed, run three ways here: the Python, the C++ harness on the Python's draws, and the
#      live engine page's own code in node; the three SHA-256 digests printed side by side and compared;
#   5. the core's Monte Carlo from the same base, the same three ways;
#   6. where the base is a recorded set's, each digest compared with the record GitHub's machine wrote.
# Usage: scripts/prove_runs.sh [BASE] [RUNS]     BASE: a base seed (default: the newest recorded set's); RUNS: default 500
# Our own models (class S): it proves three implementations compute the same numbers; it is not a benchmark result.
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
RUNS="${2:-500}"
BASE="${1:-$($PY - <<'PYEOF'
import json, glob
recs = [json.load(open(f)) for f in glob.glob("results/engine_runs/ENGINE_RUNS_*.json")]
print(max(recs, key=lambda d: d.get("written", ""))["base"] if recs else 20261020)
PYEOF
)}"
OUT="$(mktemp -d)"
trap 'rm -rf "$OUT"' EXIT
PAGE=docs/engine/OMNI_COMPASS_LIVE_ENGINE.html

echo "== 1. the engine that stands"
$PY tools/omni_version.py | head -1

echo "== 2. the C++ harness, built from source"
cmake -S cpp -B cpp/build -DCMAKE_BUILD_TYPE=Release > "$OUT/cmake.log" 2>&1 || { tail -20 "$OUT/cmake.log"; exit 1; }
cmake --build cpp/build -j2 --target oc_engine_runs oc_core_runs > "$OUT/build.log" 2>&1 || { tail -20 "$OUT/build.log"; exit 1; }
echo "built: cpp/build/oc_engine_runs, cpp/build/oc_core_runs ($(c++ --version | head -1))"

echo "== 3. every recorded set, from the records themselves"
$PY tools/runs_ledger.py --check

echo "== 4. the engine's runs: $RUNS runs from base $BASE, three ways on this machine"
$PY tools/engine_runs.py --runs "$RUNS" --base "$BASE" --cpp cpp/build/oc_engine_runs --out "$OUT/engine.json"
$PY tools/engine_runs.py --verify "$PAGE" --all --runs "$RUNS" --base "$BASE" --out "$OUT/engine.json"

echo "== 5. the core's Monte Carlo: $RUNS runs from base $BASE, three ways on this machine"
$PY tools/core_runs.py --runs "$RUNS" --base "$BASE" --cpp cpp/build/oc_core_runs --out "$OUT/core.json"
$PY tools/core_runs.py --verify "$PAGE" --runs "$RUNS" --base "$BASE" --out "$OUT/core.json"

echo "== 6. the digests, side by side"
$PY - "$OUT" "$RUNS" "$BASE" <<'PYEOF'
import json, sys
from pathlib import Path
out, runs, base = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
ok = True
for name, here, rec in (("the engine's runs", out / "engine.json", Path(f"results/engine_runs/ENGINE_RUNS_{runs}_{base}.json")),
                        ("the core's Monte Carlo", out / "core.json", Path(f"results/core_runs/CORE_RUNS_{runs}_{base}.json"))):
    d = json.loads(here.read_text())
    three = {"the Python": d["digest"], "the C++ harness": (d.get("cpp") or {}).get("digest"), "the page's own code": (d.get("page") or {}).get("digest")}
    print(f"{name}:")
    for who, h in three.items():
        print(f"  {who:20s} {h}")
    same = len(set(three.values())) == 1 and None not in three.values()
    print(f"  the three are {'ONE digest' if same else 'NOT one digest'}")
    ok = ok and same
    if rec.exists():
        r = json.loads(rec.read_text())
        g = (r.get("github") or {})
        match = r["digest"] == d["digest"]
        print(f"  the record ({rec}, GitHub run {g.get('run_id', 'none')}): {r['digest']}: {'the same as this machine gives' if match else 'DIFFERENT from this machine'}")
        ok = ok and match
    else:
        print(f"  no record of base {base} in the repository: a set of your own")
print("PROVED: every digest agrees" if ok else "NOT PROVED: a digest differs")
sys.exit(0 if ok else 1)
PYEOF
