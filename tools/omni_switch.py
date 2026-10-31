#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The kill switch, from the command line (security: Omni-Compass off everywhere at once).
The master switch for the whole Omni-Compass harness (omnicompass/master.py).

  python3 tools/omni_switch.py off [--reason TEXT] [--wait 60]
      turns every Omni-Compass governor on this machine off at once: sets the switch, signals every running governor
      (SIGTERM), and waits until each has put every setting back and exited. Exit 0 when all are gone, 1 if any is
      still running after --wait seconds (its name and pid are printed; the switch stays OFF).
  python3 tools/omni_switch.py on
      allows governors to be started again (nothing restarts by itself)
  python3 tools/omni_switch.py status
      OFF or ON, every governor running, and any that died without handing back
  python3 tools/omni_switch.py watchdog [--stale 60] [--every 10] [--once]
      puts back every setting of any governor that died or hung without doing it itself (its recorded restore commands),
      stopping a hung one first; run it as its own service next to the governors

OMNI_MASTER_OFF sets the switch file (default /tmp/omni-compass/OFF); every governor and this tool must agree on it.

The registry is trusted only as far as its files are (18 October). The watchdog runs the restore commands it finds there
and stops a hung governor's process, so a record another user could write would be a command run, or a process stopped,
with the watchdog's own rights. A record is acted on only when it and the registry directory are owned by this user (or
root, or a uid given with --trust-uid), are not a symbolic link, and are writable by no other user; each record is opened
inside the directory without following a link and checked on the open file, so nothing can be swapped in between. Any
other is refused, named in the output and left where it is. A pid is taken for the governor's only while the process
holding it started before the governor registered: a pid the system gave to another process after the governor died is
never signalled, and the governor's settings are handed back as for any governor that died. Put the switch and the
registry in a directory only the governors' user can write (OMNI_MASTER_OFF, OMNI_REGISTRY); `status` warns when they
are not.
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import stat
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omnicompass import master  # noqa: E402


def owners(extra=()):
    """The uids whose registry files are trusted: this process's own, root's, and any given."""
    return {os.geteuid(), 0, *extra}


def untrusted(st, trust):
    """Why a registry file may not be acted on, or '' when it may."""
    if stat.S_ISLNK(st.st_mode):
        return "a symbolic link"
    if st.st_uid not in trust:
        return f"owned by uid {st.st_uid}, not by {', '.join(map(str, sorted(trust)))}"
    if st.st_mode & stat.S_IWOTH:
        return "writable by every user"
    return ""


def trusted_records(trust):
    """(records, refused): the registry's records that may be acted on, each with its path, and every one that may not,
    with the reason. The directory is opened without following a link and checked on the open directory; each record is
    opened inside it without following a link, checked on the open file and read from it."""
    d = master.registry_dir()
    try:
        dfd = os.open(d, os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0))
    except FileNotFoundError:
        return [], []
    except OSError as e:
        return [], [{"path": d, "refused": f"the registry could not be opened as a directory without following a link ({e.strerror})"}]
    out, refused = [], []
    try:
        why = untrusted(os.fstat(dfd), trust)
        if why:
            return [], [{"path": d, "refused": "the registry is " + why}]
        for fn in sorted(os.listdir(dfd)):
            if not fn.endswith(".json"):
                continue
            path = os.path.join(d, fn)
            try:
                fd = os.open(fn, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0), dir_fd=dfd)
            except OSError as e:
                refused.append({"path": path, "refused": f"not opened without following a link ({e.strerror})"})
                continue
            with os.fdopen(fd) as f:
                why = untrusted(os.fstat(f.fileno()), trust)
                if why:
                    refused.append({"path": path, "refused": "the record is " + why})
                    continue
                try:
                    rec = json.loads(f.read())
                except ValueError:
                    continue                       # a record being written: read again at the next pass
            rec["_path"] = path
            out.append(rec)
    finally:
        os.close(dfd)
    return out, refused


def process_directory(pid):
    """Procfs directory for a PID in the caller's own PID namespace, or None."""
    try:
        proc = Path('/proc')
        target = proc / str(int(pid))
        # A host-mounted procfs names host PIDs; signals still take this namespace's
        # PIDs. Resolve only processes in our own PID namespace, never a matching
        # numeric ID in another namespace.
        if int((proc / 'self/stat').read_text().split()[0]) != os.getpid():
            namespace = (proc / 'self/ns/pid').stat().st_ino
            target = None
            for status in proc.glob('[0-9]*/status'):
                try:
                    if (status.parent / 'ns/pid').stat().st_ino != namespace:
                        continue
                    ids = next(line.split()[1:] for line in status.read_text().splitlines() if line.startswith('NSpid:'))
                    if ids and int(ids[-1]) == int(pid):
                        target = status.parent
                        break
                except (OSError, ValueError, StopIteration):
                    continue
            if target is None:
                return None
        return target
    except (OSError, ValueError, IndexError):
        return None


def started_at(pid):
    """When the process now holding pid started (epoch seconds), or None where the system does not say (no /proc)."""
    try:
        target = process_directory(pid)
        if target is None:
            return None
        fields = (target / 'stat').read_text().rsplit(")", 1)[1].split()
        boot = next(float(ln.split()[1]) for ln in open("/proc/stat") if ln.startswith("btime "))
        return boot + float(fields[19]) / os.sysconf("SC_CLK_TCK")
    except (OSError, ValueError, IndexError, StopIteration):
        return None


def governor_alive(r):
    """True while the record's governor runs: its pid is alive and the process holding it started before the governor
    registered (to the second /proc gives), so a pid the system gave to another process after the governor died is not
    taken for the governor's."""
    pid = r.get("pid", -1)
    if not master._alive(pid):
        return False
    began = started_at(pid)
    return began is None or began <= float(r.get("started", 0)) + 2.0


def reclaim(stale, trust=None):
    """Run the recorded restore commands of every governor that died or hung; returns what was done and what was refused."""
    done = []
    now = time.time()
    recs, refused = trusted_records(trust or owners())
    for x in refused:
        done.append({"watchdog": "refused", **x, "time": now})
    for r in recs:
        alive = governor_alive(r)
        limit = stale if stale is not None else r.get("stale_s", 60.0)
        if alive and now - r.get("lease", 0) <= limit:
            continue
        if alive:                                  # hung: stop it before its settings are put back over it
            try:
                os.kill(int(r["pid"]), signal.SIGKILL)
            except OSError:
                pass
        results = []
        for cmd in r.get("restore", []):
            try:
                c = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                results.append({"cmd": cmd, "rc": c.returncode, "stderr": c.stderr[-300:]})
            except (OSError, subprocess.SubprocessError) as e:
                results.append({"cmd": cmd, "rc": None, "error": str(e)})
        ok = all(x.get("rc") == 0 for x in results)
        if ok:
            try:
                os.remove(r["_path"])
            except OSError:
                pass
        done.append({"watchdog": "handed back", "name": r["name"], "pid": r["pid"], "hung": alive, "ok": ok,
                     "commands": results, "time": now})
    return done


def shared_dirs(trust):
    """The switch's and the registry's directories that another user could write, with the reason."""
    out = []
    for d in sorted({os.path.dirname(master.switch_path()) or ".", master.registry_dir()}):
        try:
            why = untrusted(os.lstat(d), trust)
        except OSError:
            continue
        if why:
            out.append((d, why))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["off", "on", "status", "watchdog"])
    ap.add_argument("--stale", type=float, default=None, help="watchdog: a lease older than this many seconds is hung (default: each governor's own)")
    ap.add_argument("--every", type=float, default=10.0, help="watchdog: seconds between passes")
    ap.add_argument("--once", action="store_true", help="watchdog: one pass")
    ap.add_argument("--reason", default="turned off by hand")
    ap.add_argument("--wait", type=float, default=60.0)
    ap.add_argument("--trust-uid", type=int, action="append", default=[],
                    help="also act on registry records owned by this uid (a watchdog run as another user than the governors)")
    a = ap.parse_args(argv)
    trust = owners(a.trust_uid)
    p = master.switch_path()
    if a.cmd == "watchdog":
        while True:
            for r in reclaim(a.stale, trust):
                print(json.dumps(r), flush=True)
            if a.once:
                return 0
            time.sleep(a.every)
    if a.cmd == "status":
        print(f"master switch: {'OFF' if master.is_off() else 'ON'} ({p})")
        recs, refused = trusted_records(trust)
        now = time.time()
        for r in recs:
            if governor_alive(r):
                print(f"  running: {r['name']} pid {r['pid']}")
        for r in recs:
            if not governor_alive(r) or now - r.get("lease", 0) > r.get("stale_s", 60.0):
                print(f"  DIED OR HUNG WITHOUT HANDING BACK: {r['name']} pid {r['pid']} (run: omni_switch.py watchdog --once)")
        for x in refused:
            print(f"  REFUSED, NOT ACTED ON: {x['path']}: {x['refused']}")
        for d, why in shared_dirs(trust):
            print(f"  WARNING: {d} is {why}; set OMNI_MASTER_OFF and OMNI_REGISTRY to a directory only the governors' user can write")
        return 0
    if a.cmd == "on":
        try:
            os.remove(p)
        except FileNotFoundError:
            pass
        print(f"master switch: ON ({p}); governors may be started again")
        return 0
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    try:                                           # never written through a link another user planted at the switch's path
        fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | getattr(os, "O_NOFOLLOW", 0), 0o644)
        with os.fdopen(fd, "w") as f:
            json.dump({"reason": a.reason, "time": time.time()}, f)
    except OSError as e:
        print(f"  WARNING: the switch file {p} was not written ({e.strerror}); every governor is still signalled")
    recs, refused = trusted_records(trust)
    procs = [r for r in recs if governor_alive(r)]
    for r in procs:
        try:
            os.kill(int(r["pid"]), signal.SIGTERM)
        except OSError:
            pass
    print(f"master switch: OFF ({p}); signalled {len(procs)} governor(s)")
    for x in refused:
        print(f"  REFUSED, NOT SIGNALLED: {x['path']}: {x['refused']}")
    t0 = time.time()
    left = procs
    while left and time.time() - t0 < a.wait:
        time.sleep(0.5)
        left = [r for r in trusted_records(trust)[0] if governor_alive(r)]
    for r in left:
        print(f"  STILL RUNNING after {a.wait:.0f} s: {r['name']} pid {r['pid']}")
    for r in reclaim(None, trust):
        if r["watchdog"] == "handed back":
            print(f"  handed back for a governor that had died: {r['name']} pid {r['pid']}, ok {r['ok']}")
    if not left:
        print("every governor has restored and exited")
    return 1 if left else 0


if __name__ == "__main__":
    sys.exit(main())
