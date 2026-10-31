# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The extended fault test (FAULTS=2, scripts/kind_faults.sh; amendment of 18 October in docs/K8S_COMPASS_PREREGISTRATION.md):
the four preregistered faults keep their moments, the two that blind a governor follow them, the API server's process is
found and signalled by name with nothing the node image may lack, the table reads the two new faults like the four, and the
campaign's window is long enough for the last fault's 300 seconds of recovery."""
import os, re, signal, shutil, subprocess, sys, tempfile, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.live_reps as LR
from tools.omni_switch import process_directory

SCRIPT = (ROOT / "scripts/kind_faults.sh").read_text()


def test_the_four_keep_their_moments_and_the_two_follow_only_with_faults_2():
    moments = [int(m) for m in re.findall(r"^\s*wait_until (\d+)$", SCRIPT, re.M)]
    assert moments == [15, 35, 55, 75, 82, 88], moments
    block = SCRIPT[SCRIPT.index('if [ "${FAULTS:-1}" = "2" ]; then'):]
    assert "wait_until 15" not in block and "wait_until 82" in block and "wait_until 88" in block
    for said in ('say "api frozen"', 'say "api back"', 'say "metrics down"', 'say "metrics back"'):
        assert said in block, said
    # each outage is said only once it took hold, so a fault that did not happen is never read as one that did
    assert block.index('apiserver_signal STOP') < block.index('say "api frozen"')
    assert block.index('--replicas=0') < block.index('say "metrics down"')


def test_the_api_server_is_found_by_name_and_frozen_and_continued():
    fn = re.search(r"^\s*(apiserver_signal\(\) \{.*\})$", SCRIPT, re.M).group(1)
    name = f"omnitst{os.getpid() % 100000}"            # a name of our own: a real API server on this machine is never touched
    fn = fn.replace("kube-apiserver", name)
    d = Path(tempfile.mkdtemp())
    shutil.copy(shutil.which("sleep"), d / name)
    p = subprocess.Popen([str(d / name), "60"])
    try:
        time.sleep(0.3)

        def run(sig):
            return subprocess.run(["bash", "-c", f"{fn}; sh -c \"$(apiserver_signal {sig})\""]).returncode

        def state():
            directory = process_directory(p.pid)
            assert directory is not None, 'the child must be visible in this PID namespace'
            return (directory / 'stat').read_text().rsplit(")", 1)[1].split()[0]
        assert run("STOP") == 0
        time.sleep(0.2)
        assert state() == "T", state()
        assert run("CONT") == 0
        time.sleep(0.2)
        assert state() in ("S", "R"), state()
    finally:
        p.send_signal(signal.SIGKILL); p.wait(); shutil.rmtree(d)
    # with no such process the signal fails, and the script says the fault failed instead of saying it happened
    assert subprocess.run(["bash", "-c", f"{fn}; sh -c \"$(apiserver_signal STOP)\""]).returncode != 0


def test_the_table_reads_the_two_new_faults_and_a_four_fault_run_is_unchanged():
    keys = [k for k, _ in LR.FAULTS]
    assert keys[:4] == ["machine down", "spike:", "runaway pod started", "probe blind"]
    assert ("api frozen", "api back") in LR.FAULTS and ("metrics down", "metrics back") in LR.FAULTS
    f = Path(tempfile.mkdtemp())
    for arm, bad in (("native", 90), ("compass", 30)):
        d = f / f"bench-{arm}-1"; d.mkdir()
        (d / "window_start.txt").write_text("1000\n")
        rows = ["elapsed_seconds,latency_ms,ok"] + [f"{t},{900 if 100 <= t < 100 + bad else 100},1" for t in range(0, 600, 5)]
        (d / "latency.csv").write_text("\n".join(rows) + "\n")
        (d / "faults.log").write_text("1100 api frozen\n1130 api back\n")
    tab = "\n".join(LR.fault_table(f, ["native", "compass"]))
    assert "| api frozen | native | 90 |" in tab and "| api frozen | omni | 30 |" in tab and "-60 s" in tab, tab
    assert "metrics down" not in tab and "machine down" not in tab     # a fault that did not happen has no row


def test_the_campaign_runs_the_extended_test_with_room_for_the_last_recovery():
    rows = [l for l in (ROOT / "scripts/reruns.txt").read_text().splitlines() if l.startswith("kubernetes faults extended|")]
    assert len(rows) == 1, rows
    _, wf, params = rows[0].split("|")
    p = dict(kv.split("=", 1) for kv in params.split(";"))
    assert wf == "benchmark-reps.yml" and p["faults"] == "2" and p["loadgen"] == "open"
    d = int(p["duration_s"])
    assert d * (100 - 88) // 100 >= 300, d          # the metrics outage starts at 88%: its 300 s window ends inside the run
    assert 2 * d < 150 * 60 - 1800, d               # both arms and their set-up inside the job's 150-minute limit
