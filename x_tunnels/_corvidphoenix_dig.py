#!/usr/bin/env python3
"""CORVIDPHOENIX deep dig — seed intel + DEEP_MAP section."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).resolve().parent
INTEL = DIR / "intel.jsonl"
DEEP = DIR / "DEEP_MAP.md"
now = datetime.now(timezone.utc).isoformat()

hits = [
    {
        "tunnel": "corvidphoenix_L1",
        "layer": 1,
        "author": "@Awakenthyself33",
        "text": "The Phoenix's Rebirth — rise from ashes of past trials",
        "url": "https://x.com/Awakenthyself33/status/2083115450502959543",
        "likes": 36,
        "views": 1360,
        "note": "L1 rebirth surface — spiritual phoenix, human tone",
    },
    {
        "tunnel": "corvidphoenix_L1",
        "layer": 1,
        "author": "@Awakenthyself33",
        "text": "Rising from the ashes — phoenix golden light rebirth",
        "url": "https://x.com/Awakenthyself33/status/2082103788526060019",
        "likes": 326,
        "views": 4955,
        "note": "HOT rebirth video — quote/reply window",
    },
    {
        "tunnel": "corvidphoenix_L3_myth",
        "layer": 3,
        "author": "@A_doubleC_D",
        "text": "clothe herself in flame — Phoenix her own salvation",
        "url": "https://x.com/A_doubleC_D/status/2075638117390856243",
        "likes": 3418,
        "views": 65235,
        "note": "L3 mass — respect, light touch only",
    },
    {
        "tunnel": "corvidphoenix_L1",
        "layer": 1,
        "author": "@MissSasah",
        "text": "failure wakes the Phoenix bird — rise from the ashes",
        "url": "https://x.com/MissSasah/status/2084198537940586924",
        "likes": 7,
        "views": 51,
        "note": "failure→phoenix doctrine — ball-adjacent",
    },
    {
        "tunnel": "corvidphoenix_caw",
        "layer": 1,
        "author": "@jom_simple_GKN",
        "text": "Smoke and ashes · Crow fanart",
        "url": "https://x.com/jom_simple_GKN/status/2084183144794628108",
        "likes": 30,
        "views": 338,
        "note": "crow + ashes visual — CAW rail",
    },
    {
        "tunnel": "corvidphoenix_L1",
        "layer": 2,
        "author": "@lensonskin",
        "text": "D.H. Lawrence phoenix ash poem — burnt to flocculent ash",
        "url": "https://x.com/lensonskin/status/2083604302136811901",
        "likes": 15,
        "views": 163,
        "note": "literary ash doctrine — depth lane",
    },
    {
        "tunnel": "corvidphoenix_flock",
        "layer": 2,
        "author": "@DexOlesa",
        "text": "reincarnate as raven/crow — flock in yard, intelligence",
        "url": "https://x.com/DexOlesa/status/2069793924315590723",
        "likes": 0,
        "views": 19,
        "note": "corvid reincarnation + flock loyalty",
    },
    {
        "tunnel": "corvidphoenix_L3_myth",
        "layer": 3,
        "author": "@SicklyTheNinJa",
        "text": "Legendary Phoenix + flock of baby birds — resurrects",
        "url": "https://x.com/SicklyTheNinJa/status/2042102495884013695",
        "likes": 1087,
        "views": 76733,
        "note": "L3 game myth — phoenix with flock (doctrine gold)",
    },
    {
        "tunnel": "corvidphoenix_flock",
        "layer": 2,
        "author": "@OhAIoBirdMan",
        "text": "flock filter — Avril Crow + Xena Raven pair",
        "url": "https://x.com/OhAIoBirdMan/status/2076829208530018666",
        "likes": 15,
        "views": 195,
        "note": "crow/raven named flock members",
    },
    {
        "tunnel": "corvidphoenix_raven",
        "layer": 1,
        "author": "@overkill_1008",
        "text": "RAVEN RISE live event (LOFT X)",
        "url": "https://x.com/overkill_1008/status/2084202627965821071",
        "likes": 5,
        "views": 157,
        "note": "RAVEN RISE cultural surface — JP music",
    },
    {
        "tunnel": "proto_corvidphoenix",
        "layer": 2,
        "author": "@grok",
        "text": "crows recognize faces 10-20 years — flock grudge/warn",
        "url": "https://x.com/grok/status/2081324901609214453",
        "likes": 1,
        "views": 38,
        "note": "corvid memory science — doctrine anchor",
    },
    {
        "tunnel": "corvidphoenix_L3_myth",
        "layer": 3,
        "author": "@Gardavwar",
        "text": "A phoenix rising from the ashes. And Kiara too.",
        "url": "https://x.com/Gardavwar/status/1913958203475575092",
        "likes": 7254,
        "views": 47806,
        "note": "L3 art myth — quote only",
    },
]

with INTEL.open("a", encoding="utf-8") as f:
    for h in hits:
        rec = {
            **h,
            "dig": "corvidphoenix_protocol",
            "ts": now,
            "dug_at": now,
        }
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

section = f"""
## CORVIDPHOENIX PROTOCOL dig ({now[:10]})

**Doctrine:** ash → flock → flight · black feathers · gold fire · caw from the fire

| layer | hits seeded | top surface |
|-------|-------------|-------------|
| L1 live ash | rebirth + crow/ashes art | @Awakenthyself33, @MissSasah, @jom_simple_GKN |
| L2 flock | crow/raven pairs, reincarnate-as-crow | @OhAIoBirdMan, @DexOlesa, face-memory science |
| L3 myth | mass phoenix | @A_doubleC_D 65k, @SicklyTheNinJa 76k, @Gardavwar art |

**Rails armed:** `proto_corvidphoenix` + layer tunnels + dups  
**Drop pack:** `DROP_CORVIDPHOENIX.md`  
**Protocol:** `CORVIDPHOENIX_PROTOCOL.md`

CAW FROM THE FIRE. FUCK IT WE FUCKING BALL.
"""

if DEEP.exists():
    text = DEEP.read_text(encoding="utf-8")
    if "CORVIDPHOENIX PROTOCOL dig" not in text:
        DEEP.write_text(text.rstrip() + "\n" + section, encoding="utf-8")
else:
    DEEP.write_text("# DEEP MAP\n" + section, encoding="utf-8")

print(f"CORVIDPHOENIX dig: seeded {len(hits)} intel hits @ {now}")
print("Wrote intel.jsonl + DEEP_MAP.md section")
