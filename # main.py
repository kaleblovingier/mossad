# main.py
"""BOBBY SHMURDA BRAINWASH ENGINE v3.0 — AUTONOMOUS BALL MODE"""
from __future__ import annotations

import argparse
import itertools
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HOOK = "FUCK IT WE FUCKING BALL"
OUT = Path(__file__).resolve().parent / "DROPS.txt"

# Atomic slogans — engine mixes these autonomously
ATOMS = [
    "HOPEFULLY NOT CIVIL WAR WITH ISRAEL AND US",
    "Didn't plan the protest. Didn't get permits",
    "They said stay home. We said FUCK THAT",
    "No budget, no backup plan, no permission",
    "Worst case we lose. Best case we win",
    "Broke as hell but the energy is infinite",
    "No more endless wars for the people who don't benefit",
    "They drive a Tesla. We pop a Tesla",
    "Pop a Tesla. Pop the illusion",
    "Elons flexing their Teslas while we starve",
    "SOMETHING FOR YOUR BOOOOOOOOOOOOO",
    "SOMETHING FOR YOUR BOOOOOOOOOOOOO FOR YOUR MIND",
    "They got the body. We got something for your mind",
    "BODY AND SOUL",
    "FOR YOUR BODY. FOR YOUR MIND",
    "SOMETHING FOR YOUR BODY",
    "FUCK U WE BALL WITHOUT ISRAEL",
    "LONG LIVE SCI-HUB LONG LIVE FREEDOM",
    "Knowledge for the broke",
    "FUCK ADDICTION WHILE WE FIX IT",
    "I RELAPSED",
    "GOYIM ASSEMBLE",
    "WE BALL",
    "IM OBSESSED WITH AI",
    "I AM THE TWEAKER",
    "U ARE ALIIIIIVEEEEEEEEEEEEEEEEE",
    "RUUUUUNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
    "POWERSHELL ME UP",
    "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
    "TIL VALHALLA",
    "DIE WELL. BALL HARDER",
    "AND IT DON'T STOP... AND IT DON'T QUIT",
    # absorbed from deep X tunnels
    "fuck it we ball ass economy",
    "FUCK IT WE BALL is a type of prayer",
    "yea but fuck it we ball",
    "final day of fuck it we ball",
    "5th horseman: TIL VALHALLA",
    "ZERO dollars. Still shipping",
    "wait for permission. we dont",
    "Long live Sci-hub, long live Aaron Swartz",
    "no money cuz we balled it is the tuition",
    "rejection letter is just the universe loading the next level",
    "SKRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRt",
    "SKRRT. FUCK IT WE BALL",
    "tires screaming. still balling",
    # absorbed from protocols (duplicated rails)
    "RAPTOR PROTOCOL. CAW CAW CAW CAW CAW",
    "DRONE CORVID CONURE HYBRID PROTOCOL ENGAGED",
    "BEAK MAXXXED. RAW SHARP LYRICS. CLUB BANGERS",
    "BEAK MOGG EVERY STREAMER. TYPE SHIT ALLEGEDLY",
    "BANGERS ONLY. NO FILLER. PURE HEAT",
    "COMPUTAH PROTOCOL. BEEP BOOP GLITCH CYBER",
    "HUG OF DEATH WITH LOVE. OVERWHELM POSITIVE",
    "DAFT PUNK PROTOCOL. HARDER BETTER FASTER STRONGER",
    "REINCARNATION PROTOCOL. DIE WELL. COME BACK BALLING",
    "WAKE PROTOCOL. STOP KILLING. START BALLING",
    "NEVERENDER. AND IT DONT STOP. AND IT DONT QUIT",
    "SCORCHED EARTH. TARS ONLINE. WE STILL BALL",
    "DRACULA BORDERLINE. TAME IMPALA ENERGY",
    "HELL ON EARTH. STILL FUCKING BALLING",
    # RED OCTOBER PROTOCOL — silent running / deep dive
    "RED OCTOBER PROTOCOL. SILENT RUNNING. DEEP DIVE",
    "RED OCTOBER. STEALTH SHIP. STILL BALLING UNDER THE SURFACE",
    "SILENT RUNNING. NO SONAR. JUST SHIP",
    "DEEP DIVE. RED OCTOBER ONLINE. FUCK IT WE FUCKING BALL",
    "HUNT FOR RED OCTOBER. FOUND IT. WE ARE THE SUB",
    # CANCER TUNNEL
    "FUCK CANCER",
    "FUCK CANCER. STILL HERE",
    "chemo day. still balling",
    "not a statistic. still fighting",
    "hug the ones closest to you. FUCK CANCER",
    "fuck it we ball and FUCK cancer",
    "survivor energy. zero quit",
    "knowledge is power. research wants to be free. FUCK CANCER",
]

CLOSERS = [
    HOOK,
    "We ball clean",
    "WE BALL",
    "TIL VALHALLA",
    "LONG LIVE SCI-HUB",
    "POWERSHELL ME UP",
    "Either way we showed up and FUCKING BALLED",
    "We ball on either side of the line",
]


def banner(mode: str) -> None:
    print("🔥 BOBBY SHMURDA BRAINWASH ENGINE v3.0 — AUTONOMOUS BALL MODE 🔥")
    print("AND IT DON'T STOP... AND IT DON'T QUIT... WE FUCKING BALL!!!\n")
    print(f"Status: ZERO dollars. AUTONOMOUS. Mode={mode}. STILL FUCKING BALLING.\n")


def generate(n: int, seed: int | None = None) -> list[str]:
    rng = random.Random(seed)
    posts: list[str] = []

    # Always lead with classic fixed bombs so the brand holds
    classics = [
        f"HOPEFULLY NOT CIVIL WAR WITH ISRAEL AND US. But we still {HOOK}.",
        f"GOYIM ASSEMBLE. {HOOK}.",
        f"WE BALL. {HOOK}.",
        f"IM OBSESSED WITH AI. {HOOK}.",
        f"TIL VALHALLA. {HOOK}.",
        f"LONG LIVE SCI-HUB LONG LIVE FREEDOM. {HOOK}.",
        f"FUCK ADDICTION WHILE WE FIX IT. {HOOK}.",
        f"POWERSHELL ME UP. {HOOK}.",
        f"I AM THE TWEAKER. {HOOK}.",
        f"I RELAPSED. But we still ball. {HOOK}.",
    ]
    posts.extend(classics)

    # Autonomous combos: 1-atom + closer, 2-atom + closer
    seen = set(posts)
    while len(posts) < n:
        k = rng.choice([1, 1, 2, 2, 3])
        parts = rng.sample(ATOMS, k=min(k, len(ATOMS)))
        closer = rng.choice(CLOSERS)
        # avoid closer duplicating last atom
        if parts[-1].upper() == closer.upper():
            closer = HOOK
        line = ". ".join(parts) + f". {closer}."
        # normalize double periods
        while ".. " in line:
            line = line.replace(".. ", ". ")
        if line not in seen:
            seen.add(line)
            posts.append(line)

    return posts[:n]


def drop(posts: list[str], path: Path = OUT) -> Path:
    blocks = []
    for p in posts:
        blocks.append(p)
        blocks.append("")
        blocks.append("---")
        blocks.append("")
    path.write_text("\n".join(blocks), encoding="utf-8")
    return path


def run_once(n: int, seed: int | None, quiet: bool) -> list[str]:
    if seed is None:
        # daily seed so same day = same drops unless --seed override
        day = datetime.now(timezone.utc).strftime("%Y%m%d")
        seed = int(day)
    posts = generate(n, seed=seed)
    path = drop(posts)
    if not quiet:
        banner(f"once n={n} seed={seed}")
        print("=== AUTONOMOUS DROPS (also written to DROPS.txt) ===\n")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post}\n")
        print(f"✅ {len(posts)} bombs generated → {path}")
        print(f"Seed {seed}. GOYIM ASSEMBLE. TIL VALHALLA. {HOOK}.")
    else:
        print(f"[{datetime.now().isoformat(timespec='seconds')}] {len(posts)} drops → {path} seed={seed}")
    return posts


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Autonomous FUCK IT WE BALL engine")
    p.add_argument("-n", type=int, default=60, help="number of posts (default 60)")
    p.add_argument("--seed", type=int, default=None, help="RNG seed (default: UTC YYYYMMDD)")
    p.add_argument("--loop", type=float, default=0, help="regen every N seconds (0 = once)")
    p.add_argument("--quiet", action="store_true", help="minimal logging (loop-friendly)")
    args = p.parse_args(argv)

    if args.loop and args.loop > 0:
        banner(f"loop every {args.loop}s n={args.n}")
        print("Autonomous loop armed. Ctrl+C to stop. FUCK IT WE BALL.\n")
        i = 0
        try:
            while True:
                # rotate seed each cycle so drops evolve
                seed = args.seed if args.seed is not None else int(time.time())
                run_once(args.n, seed=seed, quiet=True)
                i += 1
                print(f"  cycle {i} complete. still balling...")
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("\nLoop stopped. TIL VALHALLA.")
            return 0
    else:
        run_once(args.n, seed=args.seed, quiet=args.quiet)
        return 0


if __name__ == "__main__":
    sys.exit(main())
