#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The guided tour's recorded voice: every stop of the tour (tools/tour_script.py) read aloud once by a neural voice and kept
beside the page as a small MP3 (docs/engine/tour/<stop>.mp3), so the tour sounds like a person on every device, not like the
browser's built-in voice. The voice is Kokoro-82M v1.0 (Apache-2.0), its American English female voice `af_heart`, run by
kokoro-onnx (MIT) on the processor; FFmpeg encodes the clips. Only the clips are kept in the repository, never the model.

Each clip is stored with the SHA-256 of the exact words it reads (docs/engine/tour/TOUR_VOICE.json). The page builder plays a
clip only while its words are the stop's words today; a stop whose words changed is read by the browser's own voice until this
tool is run again. So the voice never says what the page and the manual do not.

    python3 tools/tour_voice.py            reads aloud every stop whose clip is missing or no longer matches its words
    python3 tools/tour_voice.py --status   says how many stops have a matching clip and changes nothing; exits 3 when a
                                           stop waits to be read (the live-engine workflow reads the voice only then)

Needs: pip install kokoro-onnx soundfile; ffmpeg on the path. The model files (about 120 MB) are fetched once from the
kokoro-onnx project's release on GitHub into $KOKORO_DIR (default ~/.cache/kokoro) and checked against their SHA-256 below.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "engine" / "tour"
INDEX = OUT / "TOUR_VOICE.json"
sys.path.insert(0, str(ROOT / "tools"))
import tour_script  # noqa: E402

VOICE, LANG, SPEED, BITRATE = "af_heart", "en-us", 1.0, "40k"
RELEASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FILES = {"kokoro-v1.0.int8.onnx": "6e742170d309016e5891a994e1ce1559c702a2ccd0075e67ef7157974f6406cb",
         "voices-v1.0.bin": "bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d"}
ABOUT = {"voice": VOICE, "language": LANG, "speed": SPEED,
         "model": "Kokoro-82M v1.0, int8 ONNX (hexgrad/Kokoro-82M; the ONNX files of thewh1teagle/kokoro-onnx)",
         "model_license": "Apache-2.0", "runtime": "kokoro-onnx (MIT), on the processor", "encoder": f"FFmpeg, MP3 mono {BITRATE}bit/s",
         "model_sha256": FILES, "made_with": "tools/tour_voice.py", "words_from": "tools/tour_script.py"}


def _sha_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def model_dir() -> pathlib.Path:
    d = pathlib.Path(os.environ.get("KOKORO_DIR") or pathlib.Path.home() / ".cache" / "kokoro")
    d.mkdir(parents=True, exist_ok=True)
    for name, want in FILES.items():
        p = d / name
        if not p.exists() or _sha_file(p) != want:
            print(f"fetching {name} …", flush=True)
            urllib.request.urlretrieve(RELEASE + name, p)
            got = _sha_file(p)
            if got != want:
                p.unlink()
                raise SystemExit(f"{name}: SHA-256 {got} is not the pinned {want}")
    return d


def load() -> dict:
    if INDEX.exists():
        return json.loads(INDEX.read_text(encoding="utf-8"))
    return {"clips": {}}


def status(steps: list, idx: dict) -> tuple:
    ok, stale = [], []
    for s in steps:
        c = idx.get("clips", {}).get(s["id"])
        (ok if c and c.get("sha") == s["sha"] and (OUT / c["file"]).exists() else stale).append(s["id"])
    return ok, stale


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args(argv)
    steps, idx = tour_script.steps() + [tour_script.nav()], load()   # every stop and the line between the stops
    ok, stale = status(steps, idx)
    print(f"guided tour: {len(ok)} of {len(steps)} stops have a clip that reads their words today; {len(stale)} to read")
    if a.status:
        return 3 if stale else 0
    if not stale:
        return 0
    from kokoro_onnx import Kokoro  # noqa: E402  (only when a clip is to be read)
    import soundfile as sf  # noqa: E402
    d = model_dir()
    k = Kokoro(str(d / "kokoro-v1.0.int8.onnx"), str(d / "voices-v1.0.bin"))
    OUT.mkdir(parents=True, exist_ok=True)
    clips = {sid: c for sid, c in idx.get("clips", {}).items() if sid in {s["id"] for s in steps}}
    by_id = {s["id"]: s for s in steps}
    with tempfile.TemporaryDirectory() as tmp:
        for sid in stale:
            s = by_id[sid]
            audio, rate = k.create(s["say"], voice=VOICE, speed=SPEED, lang=LANG)
            wav, mp3 = pathlib.Path(tmp) / f"{sid}.wav", OUT / f"{sid}.mp3"
            sf.write(wav, audio, rate)
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-ac", "1", "-b:a", BITRATE,
                            "-map_metadata", "-1", "-metadata", "title=Omni-Compass Live Engine, guided tour: " + s["title"],
                            "-metadata", "copyright=" + tour_script.PLAIN, str(mp3)], check=True)
            clips[sid] = {"file": mp3.name, "sha": s["sha"], "seconds": round(len(audio) / rate, 2), "bytes": mp3.stat().st_size,
                          "mp3_sha256": _sha_file(mp3)}
            print(f"  {sid}: {clips[sid]['seconds']} s, {clips[sid]['bytes']} bytes", flush=True)
    keep = {c["file"] for c in clips.values()}
    for p in OUT.glob("*.mp3"):
        if p.name not in keep:
            p.unlink()
    order = [s["id"] for s in steps]
    INDEX.write_text(json.dumps({**ABOUT, "clips": {sid: clips[sid] for sid in order if sid in clips}}, indent=1) + "\n", encoding="utf-8")
    total = sum(c["seconds"] for c in clips.values())
    print(f"guided tour: {len(clips)} clips, {total / 60:.1f} minutes, {sum(c['bytes'] for c in clips.values()) / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
