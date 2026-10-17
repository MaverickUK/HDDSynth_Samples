#!/usr/bin/env python3
"""Preview HDD Synth sample packs: spin up, idle loops, then spin down.

The samples are joined into a single WAV before playback so the idle loop
plays gaplessly, as it does on the device.

    python3 preview.py PB_WD_Raptor
    python3 preview.py                      # every pack in turn
    python3 preview.py PB_WD_Raptor --loops 5 --access
    python3 preview.py PB_WD_Raptor --save out.wav
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import wave

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
REQUIRED = ("spinup.wav", "idle.wav", "spindown.wav")


def find_packs():
    packs = []
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name)
        if name.startswith(".") or not os.path.isdir(path):
            continue
        if all(os.path.isfile(os.path.join(path, f)) for f in REQUIRED):
            packs.append(name)
    return packs


def load_frames(path):
    with wave.open(path, "rb") as w:
        return w.getparams(), w.readframes(w.getnframes())


def build(pack, loops, access):
    """Return (params, frames) for spinup -> idle x loops -> spindown."""
    pack_dir = os.path.join(ROOT, pack)
    sounds = {}
    names = list(REQUIRED) + (["access.wav"] if access else [])
    for name in names:
        sounds[name] = load_frames(os.path.join(pack_dir, name))

    base = sounds["spinup.wav"][0]
    for name, (params, _) in sounds.items():
        if (params.nchannels, params.sampwidth, params.framerate) != (
            base.nchannels, base.sampwidth, base.framerate
        ):
            sys.exit(f"{pack}/{name}: format differs from spinup.wav "
                     f"({params.nchannels}ch {params.sampwidth * 8}bit {params.framerate}Hz)")

    idle = sounds["idle.wav"][1]
    middle = [idle] * loops
    if access:
        middle.insert(loops // 2, sounds["access.wav"][1])
    frames = b"".join([sounds["spinup.wav"][1], *middle, sounds["spindown.wav"][1]])
    return base, frames


def write_wav(path, params, frames):
    with wave.open(path, "wb") as w:
        w.setnchannels(params.nchannels)
        w.setsampwidth(params.sampwidth)
        w.setframerate(params.framerate)
        w.writeframes(frames)


def play(path):
    if sys.platform == "darwin":
        subprocess.run(["afplay", path], check=True)
    elif sys.platform == "win32":
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    elif shutil.which("aplay"):
        subprocess.run(["aplay", "-q", path], check=True)
    elif shutil.which("ffplay"):
        subprocess.run(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", path], check=True)
    else:
        sys.exit("No audio player found (tried aplay, ffplay)")


def preview(pack, loops, access, save):
    params, frames = build(pack, loops, access)
    seconds = len(frames) / (params.nchannels * params.sampwidth * params.framerate)
    if save:
        write_wav(save, params, frames)
        print(f"Saved {pack} ({seconds:.1f}s) to {save}")
        return

    print(f"Playing {pack} ({seconds:.1f}s)")
    fd, tmp = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    try:
        write_wav(tmp, params, frames)
        play(tmp)
    finally:
        os.remove(tmp)


def main():
    parser = argparse.ArgumentParser(description="Preview HDD Synth sample packs.")
    parser.add_argument("pack", nargs="?", help="sample pack directory (default: all packs)")
    parser.add_argument("--loops", type=int, default=3, help="number of idle loops (default: 3)")
    parser.add_argument("--access", action="store_true", help="include access.wav mid-idle")
    parser.add_argument("--save", metavar="PATH", help="write the combined WAV instead of playing")
    args = parser.parse_args()

    packs = find_packs()
    if args.pack:
        pack = os.path.basename(args.pack.rstrip("/\\"))
        if pack not in packs:
            print(f"Unknown pack '{pack}'. Available packs:", file=sys.stderr)
            for p in packs:
                print(f"  {p}", file=sys.stderr)
            sys.exit(1)
        packs = [pack]
    elif args.save:
        sys.exit("--save needs a pack name")

    try:
        for pack in packs:
            preview(pack, args.loops, args.access, args.save)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
