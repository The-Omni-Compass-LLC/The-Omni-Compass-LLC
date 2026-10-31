# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The watchdog trusts the registry only as far as its files (tools/omni_switch.py, 18 October). It runs the restore
commands it finds there and stops a hung governor's process, so a record another user could write would be a command run,
or a process stopped, with the watchdog's rights; and a pid the system gave to another process after the governor died
would be stopped in the governor's place. Each case is set up in a registry of its own, with a restore command that only
leaves a mark."""
import contextlib, errno, json, os, stat, subprocess, sys, tempfile, time
from unittest.mock import patch
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.omni_switch as SW


def registry():
    d = Path(tempfile.mkdtemp())
    os.environ["OMNI_REGISTRY"] = str(d / "running")
    (d / "running").mkdir()
    return d, d / "running"


def record(reg, name, pid, mark, started=None, lease=0.0):
    rec = {"pid": pid, "name": name, "started": time.time() if started is None else started, "lease": lease,
           "stale_s": 60.0, "restore": [[sys.executable, "-c", f"open({str(mark)!r}, 'w').write('back')"]]}
    p = reg / f"{name}.json"
    p.write_text(json.dumps(rec))
    os.chmod(p, 0o644)
    return p


def test_a_record_of_its_own_user_is_handed_back():
    d, reg = registry()
    record(reg, "gone", 2 ** 22 + 7, d / "mark")                     # a pid no process holds: the governor died
    done = SW.reclaim(None)
    assert [x["watchdog"] for x in done] == ["handed back"] and done[0]["ok"], done
    assert (d / "mark").read_text() == "back" and not list(reg.glob("*.json"))


def test_a_record_any_user_can_write_is_refused_and_left_in_place():
    d, reg = registry()
    p = record(reg, "planted", 2 ** 22 + 7, d / "mark")
    os.chmod(p, 0o666)
    done = SW.reclaim(None)
    assert [x["watchdog"] for x in done] == ["refused"] and "writable by every user" in done[0]["refused"], done
    assert not (d / "mark").exists() and p.exists()


def test_a_registry_any_user_can_write_is_refused_whole():
    d, reg = registry()
    record(reg, "a", 2 ** 22 + 7, d / "mark")
    os.chmod(reg, 0o777)
    done = SW.reclaim(None)
    assert len(done) == 1 and done[0]["watchdog"] == "refused" and "the registry is writable by every user" in done[0]["refused"]
    assert not (d / "mark").exists()


def test_a_record_reached_through_a_link_is_refused():
    d, reg = registry()
    elsewhere = record(d, "real", 2 ** 22 + 7, d / "mark")
    os.symlink(elsewhere, reg / "linked.json")
    done = SW.reclaim(None)
    assert [x["watchdog"] for x in done] == ["refused"] and "following a link" in done[0]["refused"], done
    assert not (d / "mark").exists()


def test_a_record_of_another_user_is_refused():
    d, reg = registry()
    p = record(reg, "theirs", 2 ** 22 + 7, d / "mark")
    ownership = contextlib.nullcontext()
    try:
        os.chown(p, 54321, 54321)
    except OSError as error:
        if error.errno not in (errno.EINVAL, errno.EPERM):
            raise
        # A non-root user or a single-UID user namespace cannot represent uid
        # 54321. Exercise the same descriptor-owner checks with that metadata;
        # keep both refusal and explicit-trust assertions, never skip the test.
        identity = p.stat(); actual_fstat = os.fstat
        def foreign_owner(fd):
            observed = actual_fstat(fd)
            if (observed.st_dev, observed.st_ino) == (identity.st_dev, identity.st_ino):
                fields = list(observed); fields[4] = 54321
                return os.stat_result(fields)
            return observed
        ownership = patch.object(SW.os, 'fstat', side_effect=foreign_owner)
    with ownership:
        done = SW.reclaim(None)
        assert [x["watchdog"] for x in done] == ["refused"] and "owned by uid 54321" in done[0]["refused"], done
        assert not (d / "mark").exists()
        done = SW.reclaim(None, SW.owners([54321]))                       # a watchdog told to trust that user acts on it
        assert [x["watchdog"] for x in done] == ["handed back"] and (d / "mark").exists()


def test_a_pid_given_to_another_process_is_never_stopped():
    # the record's governor registered an hour before this process started: whoever holds the pid now is not it. Before
    # 18 October the watchdog took the pid as the governor's, hung, and killed it (here: this very test)
    d, reg = registry()
    record(reg, "reused", os.getpid(), d / "mark", started=time.time() - 3600)
    assert SW.started_at(os.getpid()) is None or not SW.governor_alive(json.loads((reg / "reused.json").read_text()))
    done = SW.reclaim(None)
    assert [x["watchdog"] for x in done] == ["handed back"] and done[0]["hung"] is False, done
    assert (d / "mark").read_text() == "back"


def test_a_hung_governor_is_still_stopped_and_handed_back():
    d, reg = registry()
    p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
    try:
        time.sleep(0.5)
        record(reg, "hung", p.pid, d / "mark")                        # registered after its process began; lease long stale
        done = SW.reclaim(None)
        assert [x["watchdog"] for x in done] == ["handed back"] and done[0]["hung"] is True, done
        assert p.wait(10) == -9 and (d / "mark").read_text() == "back"
    finally:
        if p.poll() is None:
            p.kill()


def test_status_names_what_it_refused_and_a_shared_switch_directory():
    d, reg = registry()
    p = record(reg, "planted", 2 ** 22 + 7, d / "mark")
    os.chmod(p, 0o666)
    shared = d / "shared"; shared.mkdir(); os.chmod(shared, 0o777)
    env = dict(os.environ, OMNI_MASTER_OFF=str(shared / "OFF"), OMNI_REGISTRY=str(reg), PYTHONPATH=str(ROOT))
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_switch.py"), "status"], env=env, capture_output=True,
                         text=True, timeout=60).stdout
    assert "REFUSED, NOT ACTED ON" in out and "writable by every user" in out, out
    assert f"WARNING: {shared} is writable by every user" in out, out
    assert not (d / "mark").exists()


def test_off_never_writes_through_a_link_planted_at_the_switch():
    d, reg = registry()
    victim = d / "victim.txt"; victim.write_text("keep")
    sw = d / "switch"; sw.mkdir()
    os.symlink(victim, sw / "OFF")
    env = dict(os.environ, OMNI_MASTER_OFF=str(sw / "OFF"), OMNI_REGISTRY=str(reg), PYTHONPATH=str(ROOT))
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_switch.py"), "off", "--wait", "1"], env=env,
                       capture_output=True, text=True, timeout=60)
    assert victim.read_text() == "keep", victim.read_text()
    assert "was not written" in r.stdout and r.returncode == 0, r.stdout + r.stderr
