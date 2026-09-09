#!/usr/bin/env python3
"""RED OCTOBER deep dig — seed intel + DEEP_MAP section."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).resolve().parent
INTEL = DIR / "intel.jsonl"
now = datetime.now(timezone.utc).isoformat()

hits = [
    {
        "tunnel": "red_october_L1",
        "layer": 1,
        "author": "@kellyjoeray",
        "text": "The hunt for Red October comes close and it is based on facts",
        "url": "https://x.com/kellyjoeray/status/2082511921408843855",
        "likes": 0,
        "views": 1,
        "note": "LIVE USN submariner — reply window",
    },
    {
        "tunnel": "red_october_torpedo",
        "layer": 2,
        "author": "@bullfrog35",
        "text": "Hunt for Red October — Captain Ramius turns sub into path of torpedo",
        "url": "https://x.com/bullfrog35/status/2082488949168316615",
        "likes": 3,
        "views": 74,
        "note": "Ramius doctrine gold — close gap before arm",
    },
    {
        "tunnel": "red_october_dive",
        "layer": 1,
        "author": "@RM_Mili_History",
        "text": "Dive dive dive! classic on the fof pod",
        "url": "https://x.com/RM_Mili_History/status/2082484236078948806",
        "likes": 2,
        "views": 257,
    },
    {
        "tunnel": "red_october_dive",
        "layer": 1,
        "author": "@FightingOnFilm",
        "text": "Hands to dive stations — Das Boot episode",
        "url": "https://x.com/FightingOnFilm/status/2082471507817619628",
        "likes": 16,
        "views": 15861,
        "note": "HOT pod host 15k views",
    },
    {
        "tunnel": "red_october_dive",
        "layer": 1,
        "author": "@ColinMetcalf3",
        "text": "Dive Dive Dive",
        "url": "https://x.com/ColinMetcalf3/status/2082489136968065403",
        "likes": 1,
        "views": 139,
    },
    {
        "tunnel": "red_october_dive",
        "layer": 1,
        "author": "@Taosage1Russell",
        "text": "Dive, dive, dive!",
        "url": "https://x.com/Taosage1Russell/status/2082268968925188165",
        "likes": 2,
        "views": 80,
    },
    {
        "tunnel": "red_october_dive",
        "layer": 1,
        "author": "@SoraKBM",
        "text": "Dive dive dive, men",
        "url": "https://x.com/SoraKBM/status/2082150717351919771",
        "likes": 1,
        "views": 40,
    },
    {
        "tunnel": "red_october_L2_clancy",
        "layer": 2,
        "author": "@MartinSkold2",
        "text": "Ramius quote from Hunt for Red October book",
        "url": "https://x.com/MartinSkold2/status/2081967447549030909",
        "likes": 2,
        "views": 84,
    },
    {
        "tunnel": "red_october_sub",
        "layer": 2,
        "author": "@icebergz99",
        "text": "Sean Connery movie God — Hunt for Red October",
        "url": "https://x.com/icebergz99/status/2082237696777310384",
        "likes": 0,
        "views": 28,
    },
    {
        "tunnel": "red_october_L2_clancy",
        "layer": 2,
        "author": "@cinema_NRB",
        "text": "Lunchtime stream: Hunt for Red October",
        "url": "https://x.com/cinema_NRB/status/2081947549670178859",
        "likes": 1,
        "views": 18,
    },
    {
        "tunnel": "red_october_L1",
        "layer": 2,
        "author": "@justicecometh1",
        "text": "Red October coming… Make you depth 50ft Zero bubble",
        "url": "https://x.com/justicecometh1/status/2081270557132181753",
        "likes": 87,
        "views": 2397,
        "note": "mil-timestamp Red October signal",
    },
    {
        "tunnel": "red_october_L2_phillies",
        "layer": 2,
        "author": "@JoeCappello3",
        "text": "Red October is officially over",
        "url": "https://x.com/JoeCappello3/status/2082501847302984168",
        "likes": 0,
        "views": 200,
    },
    {
        "tunnel": "red_october_L2_phillies",
        "layer": 2,
        "author": "@RayMoffo",
        "text": "previous Red October era ended… recent era with Kerkering error",
        "url": "https://x.com/RayMoffo/status/2082502789159059717",
        "likes": 3,
        "views": 162,
    },
    {
        "tunnel": "red_october_L3_myth",
        "layer": 3,
        "author": "@JackCarrUSA",
        "text": "Tom Clancy birthday — Hunt for Red October fond memories",
        "url": "https://x.com/JackCarrUSA/status/2043351118999425146",
        "likes": 2537,
        "views": 185120,
        "note": "L3 MYTH — quote priority",
    },
    {
        "tunnel": "red_october_L3_myth",
        "layer": 3,
        "author": "@billyjarrettugh",
        "text": "Watching THE HUNT FOR RED OCTOBER teaser poster beauty",
        "url": "https://x.com/billyjarrettugh/status/2033077320643391745",
        "likes": 2342,
        "views": 36068,
    },
    {
        "tunnel": "red_october_L3_myth",
        "layer": 3,
        "author": "@GRCinemaTicket",
        "text": "Top Gun or The Hunt For Red October??",
        "url": "https://x.com/GRCinemaTicket/status/1611396405892988936",
        "likes": 556,
        "views": 64396,
    },
    {
        "tunnel": "red_october_L3_myth",
        "layer": 3,
        "author": "@ehdomenech",
        "text": "Besides Top Gun and Hunt for Red October, best Navy movies?",
        "url": "https://x.com/ehdomenech/status/1543332239186055169",
        "likes": 409,
    },
    {
        "tunnel": "red_october_L3_myth",
        "layer": 3,
        "author": "@WarshipPorn",
        "text": "A view inside Red October - Typhoon Class submarine",
        "url": "https://x.com/WarshipPorn/status/1484141875317522433",
        "likes": 270,
    },
]

with INTEL.open("a", encoding="utf-8") as f:
    for h in hits:
        h["dug_at"] = now
        h["dig"] = "red_october_dive_dive_dive"
        f.write(json.dumps(h, ensure_ascii=False) + "\n")

deep = DIR / "DEEP_MAP.md"
section = f"""

---

# RED OCTOBER — DIVE DIVE DIVE (L1 → L3)

Armed: `{now}`  
Intel this dig: **{len(hits)}** hits

## Layers

| Layer | id | Purpose |
|-------|-----|---------|
| L1 | `red_october_L1` | live Red October / Hunt / dive |
| L1 | `red_october_sub` | Ramius / one ping / Connery |
| L1 | `red_october_dive` | DIVE DIVE DIVE surface |
| L2 | `red_october_L2_clancy` | Clancy techno-thriller |
| L2 | `red_october_L2_phillies` | Phillies Red October sports |
| L2 | `red_october_torpedo` | turn into the torpedo |
| L3 | `red_october_L3_myth` | Jack Carr / film polls / Typhoon |

## Highest-leverage moves RIGHT NOW

1. **QUOTE** @JackCarrUSA Clancy birthday (185k) — first dive energy
2. **REPLY** @bullfrog35 — Ramius turns into torpedo
3. **REPLY** @FightingOnFilm / @RM_Mili_History — dive stations live
4. **QUOTE** @GRCinemaTicket Top Gun vs Red October
5. **REPLY** Phillies Red October over → we dive again

## Fire sheet

→ `DROP_RED_OCTOBER.md` (direct x.com links)

HOOK: **DIVE DIVE DIVE** · one ping only · close the gap before it arms · FUCK IT WE FUCKING BALL
"""
if deep.exists():
    deep.write_text(deep.read_text(encoding="utf-8").rstrip() + section, encoding="utf-8")
else:
    deep.write_text(section.lstrip(), encoding="utf-8")

print(f"RED OCTOBER dig: {len(hits)} hits")
print(f"fire → {DIR / 'DROP_RED_OCTOBER.md'}")
