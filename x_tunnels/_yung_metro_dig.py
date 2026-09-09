#!/usr/bin/env python3
"""IF YUNG METRO DONT — deep dig intel seed."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).resolve().parent
INTEL = DIR / "intel.jsonl"
now = datetime.now(timezone.utc).isoformat()

hits = [
    {
        "tunnel": "yung_metro_L1",
        "layer": 1,
        "author": "@niwekemia",
        "text": "If young metro doesn't trust you / He gon shoot you",
        "url": "https://x.com/niwekemia/status/2082501122279768540",
        "likes": 0,
        "views": 4,
        "note": "LIVE tagline",
    },
    {
        "tunnel": "yung_metro_L1",
        "layer": 1,
        "author": "@feelscrzy",
        "text": "If young metro don't trust you, I'm gon shoot you.",
        "url": "https://x.com/feelscrzy/status/2081142715501170822",
        "likes": 0,
        "views": 9,
    },
    {
        "tunnel": "yung_metro_L2_producer",
        "layer": 2,
        "author": "@iam_alfred7",
        "text": "Future on Young Metro >>>>>>>>>>>",
        "url": "https://x.com/iam_alfred7/status/2080993445347242300",
        "likes": 1,
        "views": 38,
    },
    {
        "tunnel": "yung_metro_L2_producer",
        "layer": 2,
        "author": "@jumpman_0206",
        "text": "Metro Boomin has to be one of the best beat producers",
        "url": "https://x.com/jumpman_0206/status/2077046243964891521",
        "likes": 1,
        "views": 27,
    },
    {
        "tunnel": "yung_metro_L2_producer",
        "layer": 2,
        "author": "@_STEPHENSTEPHEN",
        "text": "Metro Boomin Jumpman interpolation credits",
        "url": "https://x.com/_STEPHENSTEPHEN/status/2081772744266461589",
        "likes": 0,
        "views": 112,
    },
    {
        "tunnel": "yung_metro_L3_myth",
        "layer": 3,
        "author": "@chefmade_92",
        "text": "IF YOUNG METRO DOESNT TRUST YOU, IMA SHOOT YOU",
        "url": "https://x.com/chefmade_92/status/2071000181978374162",
        "likes": 3943,
        "views": 64264,
        "note": "L3 ALL CAPS canon",
    },
    {
        "tunnel": "yung_metro_L3_myth",
        "layer": 3,
        "author": "@slvppy",
        "text": "once i hear that if young metro don't trust you imma shoot you",
        "url": "https://x.com/slvppy/status/2006050877904187716",
        "likes": 322,
        "views": 45682,
    },
    {
        "tunnel": "yung_metro_L3_myth",
        "layer": 3,
        "author": "@BuzzFeed",
        "text": "story behind If young Metro don't trust you I'm gon shoot you",
        "url": "https://x.com/BuzzFeed/status/709757215679385601",
        "likes": 292,
        "note": "origin explainer",
    },
    {
        "tunnel": "yung_metro_L3_myth",
        "layer": 3,
        "author": "@Purv_909",
        "text": "Me after listening if young metro don't trust you",
        "url": "https://x.com/Purv_909/status/1438092733512503302",
        "likes": 4,
    },
    {
        "tunnel": "yung_metro_L3_myth",
        "layer": 3,
        "author": "@EarlyVibzz",
        "text": "If young Metro don't trust u I'm gon shoot you",
        "url": "https://x.com/EarlyVibzz/status/1679390499747004416",
        "likes": 7,
        "views": 485,
    },
    {
        "tunnel": "yung_metro_trust",
        "layer": 1,
        "author": "@3268654a",
        "text": "display name: IF YOUNG METRO DONT TRUST YOU IMA SUE",
        "url": "https://x.com/3268654a/status/2082488739176067500",
        "likes": 1,
        "views": 4,
        "note": "living tagline handle",
    },
]

with INTEL.open("a", encoding="utf-8") as f:
    for h in hits:
        h["dug_at"] = now
        h["dig"] = "if_yung_metro_dont"
        f.write(json.dumps(h, ensure_ascii=False) + "\n")

deep = DIR / "DEEP_MAP.md"
section = f"""

---

# IF YUNG METRO DONT — TUNNEL (L1 → L3)

Armed: `{now}`  
Intel: **{len(hits)}** hits

| Layer | id | Purpose |
|-------|-----|---------|
| L1 | `yung_metro_L1` | live tagline |
| L1 | `yung_metro_trust` | trust variants |
| L2 | `yung_metro_L2_producer` | Metro/Future/Jumpman |
| L2 | `yung_metro_ball` | metro × ball |
| L3 | `yung_metro_L3_myth` | viral + origin |

## Highest leverage

1. **QUOTE** @chefmade_92 ALL CAPS (64k)
2. **QUOTE** @slvppy once i hear that (45k)
3. **QUOTE** @BuzzFeed origin
4. **REPLY** live tagline posts
5. **SOLO** IF YUNG METRO DONT + ball stamp

→ `DROP_YUNG_METRO.md`

HOOK: **IF YUNG METRO DONT** · stamp approved · FUCK IT WE FUCKING BALL
"""
if deep.exists():
    deep.write_text(deep.read_text(encoding="utf-8").rstrip() + section, encoding="utf-8")
else:
    deep.write_text(section.lstrip(), encoding="utf-8")

print(f"YUNG METRO dig: {len(hits)} hits → DROP_YUNG_METRO.md")
