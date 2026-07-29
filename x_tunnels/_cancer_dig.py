#!/usr/bin/env python3
"""Seed CANCER TUNNEL deep dig intel + refresh DEEP_MAP section."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).resolve().parent
INTEL = DIR / "intel.jsonl"
now = datetime.now(timezone.utc).isoformat()

hits = [
    {
        "tunnel": "cancer_ball_crossover",
        "layer": 1,
        "author": "@strxwbry_mxtcha",
        "text": "miss greyday for oncology but fuck it we ball and FUCK cancer",
        "url": "https://x.com/strxwbry_mxtcha/status/2078206098171887757",
        "likes": 55,
        "views": 6302,
        "note": "GOLD crossover template — quote priority",
    },
    {
        "tunnel": "cancer_ball_crossover",
        "layer": 1,
        "author": "@Jason______A",
        "text": "high grade follicular radiation doesnt work but fuck it we ball",
        "url": "https://x.com/Jason______A/status/2077163661718647036",
        "likes": 0,
        "views": 180,
        "note": "ball + cancer fighter reply",
    },
    {
        "tunnel": "cancer_L1_live",
        "layer": 1,
        "author": "@DammitBits",
        "text": "personal day. thinking about Shannon. Fuck cancer!",
        "url": "https://x.com/DammitBits/status/2082504170905706862",
        "likes": 30,
        "views": 206,
        "note": "LIVE support window",
    },
    {
        "tunnel": "cancer_L1_live",
        "layer": 1,
        "author": "@fant0ss",
        "text": "RAHHHHH FUCK CANCER, YOU SHOWED THAT MF WHO IS BOSS",
        "url": "https://x.com/fant0ss/status/2082507361927778621",
        "likes": 0,
        "views": 3,
    },
    {
        "tunnel": "cancer_L1_live",
        "layer": 1,
        "author": "@nemigami",
        "text": "FUCK CANCER!!!",
        "url": "https://x.com/nemigami/status/2082393055026430150",
        "likes": 44,
        "views": 703,
    },
    {
        "tunnel": "cancer_L1_live",
        "layer": 1,
        "author": "@LEEbot162",
        "text": "Fuck Cancer",
        "url": "https://x.com/LEEbot162/status/2082116256061141498",
        "likes": 67,
        "views": 7020,
    },
    {
        "tunnel": "cancer_L2_fighter",
        "layer": 2,
        "author": "@jasonmyrt",
        "text": "stage 4 colorectal metastatic. I am NOT a statistic. FIGHT of a Lion",
        "url": "https://x.com/jasonmyrt/status/2082307020749754667",
        "likes": 2071,
        "views": 105124,
        "note": "PRIMARY fighter host — careful strength reply",
    },
    {
        "tunnel": "cancer_L2_fighter",
        "layer": 2,
        "author": "@MagnoliaXRio",
        "text": "PET scan significant improvement. tumors shrinking. 10 rounds chemo",
        "url": "https://x.com/MagnoliaXRio/status/2081039950531764650",
        "likes": 387,
        "views": 11174,
    },
    {
        "tunnel": "cancer_L2_fighter",
        "layer": 2,
        "author": "@BirdieBittern",
        "text": "told NBD & its stage 4 cancer. dismissive doctors",
        "url": "https://x.com/BirdieBittern/status/2082507392080580643",
        "likes": 7,
        "views": 105,
    },
    {
        "tunnel": "cancer_L2_research",
        "layer": 2,
        "author": "@NextScience",
        "text": "cowpea mosaic virus wakes immune system against cancer",
        "url": "https://x.com/NextScience/status/2082493387903533393",
        "likes": 23,
        "views": 664,
        "note": "scihub-adjacent knowledge drop",
    },
    {
        "tunnel": "cancer_L2_fighter",
        "layer": 2,
        "author": "@WolfofX",
        "text": "9yo Oscar runs a mile a day for friend with stage 4",
        "url": "https://x.com/WolfofX/status/2082502121564565626",
        "likes": 16,
        "views": 1821,
    },
    {
        "tunnel": "cancer_L3_myth",
        "layer": 3,
        "author": "@dreamwastaken",
        "text": "fuck cancer. hug the ones closest to you",
        "url": "https://x.com/dreamwastaken/status/1542685240530968576",
        "likes": 528417,
        "note": "L3 CANON — quote gold",
    },
    {
        "tunnel": "cancer_L3_myth",
        "layer": 3,
        "author": "@fckeveryword",
        "text": "fuck cancer",
        "url": "https://x.com/fckeveryword/status/1415868805016870915",
        "likes": 11303,
    },
    {
        "tunnel": "cancer_L3_myth",
        "layer": 3,
        "author": "@HumanityChad",
        "text": "hockey team chemo day one then ring the bell",
        "url": "https://x.com/HumanityChad/status/2009269107665842367",
        "likes": 8573,
        "views": 173698,
    },
    {
        "tunnel": "cancer_care_sacred",
        "layer": 1,
        "author": "@BYRNEGRACES",
        "text": "funeral. want my auntie back. Fuck cancer.",
        "url": "https://x.com/BYRNEGRACES/status/2082506442267824582",
        "likes": 0,
        "views": 5,
        "note": "SACRED grief — short human only",
    },
    {
        "tunnel": "cancer_care_sacred",
        "layer": 1,
        "author": "@PhinneasJW",
        "text": "Ann would have been 73. #fuck cancer",
        "url": "https://x.com/PhinneasJW/status/2081792383146979810",
        "likes": 736,
        "views": 6311,
        "note": "SACRED memorial — no ball slogans",
    },
]

with INTEL.open("a", encoding="utf-8") as f:
    for h in hits:
        h["dug_at"] = now
        h["dig"] = "cancer_tunnel_deep"
        f.write(json.dumps(h, ensure_ascii=False) + "\n")

# append cancer section to DEEP_MAP
deep = DIR / "DEEP_MAP.md"
section = f"""

---

# CANCER TUNNEL — DEEP MAP (L1 → L3)

Armed: `{now}`  
Intel this dig: **{len(hits)}** hits

## Layers

| Layer | id | Purpose |
|-------|-----|---------|
| L1 | `cancer_L1_live` | live "fuck cancer" surface |
| L1×BALL | `cancer_ball_crossover` | dual-signal ball+cancer posts |
| L2 | `cancer_L2_fighter` | fighters / stage / chemo |
| L2 | `cancer_L2_research` | treatment breakthroughs |
| L3 | `cancer_L3_myth` | Dream hug canon, mass reach |
| SACRED | `cancer_care_sacred` | grief — short human only |

## Highest-leverage moves RIGHT NOW

1. **QUOTE** @strxwbry_mxtcha — "fuck it we ball and FUCK cancer" (brand fit gold)
2. **REPLY** @jasonmyrt — stage 4 fighter, 105k views — strength only
3. **QUOTE** @dreamwastaken — fuck cancer / hug canon (L3)
4. **REPLY** @DammitBits / @MagnoliaXRio — live support windows
5. **NEVER** ball-spam funerals (@BYRNEGRACES, @PhinneasJW = sacred)

## Fire sheet

→ `DROP_CANCER.md` (direct x.com links)

HOOK: **FUCK CANCER** · hug the ones closest to you · still show up on the hard days.
"""
if deep.exists():
    text = deep.read_text(encoding="utf-8")
    if "CANCER TUNNEL" not in text:
        deep.write_text(text.rstrip() + section, encoding="utf-8")
    else:
        deep.write_text(text + f"\n\n<!-- refresh {now} -->\n" + section, encoding="utf-8")
else:
    deep.write_text(section.lstrip(), encoding="utf-8")

print(f"cancer dig: {len(hits)} hits → {INTEL}")
print(f"fire sheet → {DIR / 'DROP_CANCER.md'}")
