#!/usr/bin/env python3
"""One-shot deep dig seeder — run from repo root: python x_tunnels/_deep_seed.py"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()

hits = [
    # L3 MYTH
    {
        "tunnel": "ball_core_L3_myth",
        "layer": 3,
        "author": "@youngthug",
        "text": "But fuck it we ball!!!",
        "url": "https://x.com/youngthug/status/664207204975845376",
        "likes": 26609,
        "reposts": 27562,
        "note": "ORIGIN ENERGY — 2015 canon",
    },
    {
        "tunnel": "ball_core_L3_myth",
        "layer": 3,
        "author": "@NeptuniusIII",
        "text": "Ball up top / Charge it / It is what it is / Fuck it we ball — 4 horsemen of mens mental health",
        "url": "https://x.com/NeptuniusIII/status/1834717139283968028",
        "likes": 139937,
        "reposts": 22975,
        "views": 3689003,
        "note": "3.6M VIEWS — quote-reply gold",
    },
    {
        "tunnel": "ball_core_L3_myth",
        "layer": 3,
        "author": "@svtxtism",
        "text": "final day of fuck it we ball folks!!!",
        "url": "https://x.com/svtxtism/status/1874027719761297781",
        "likes": 238810,
        "reposts": 20811,
        "views": 5520271,
        "note": "5.5M VIEWS — NYE ritual frame",
    },
    {
        "tunnel": "ball_core_L3_myth",
        "layer": 3,
        "author": "@__knf",
        "text": "yea but fuck it we ball",
        "url": "https://x.com/__knf/status/1426014869606785030",
        "likes": 37655,
        "reposts": 12089,
        "note": "reply-to-despair template",
    },
    {
        "tunnel": "ball_core_L3_myth",
        "layer": 3,
        "author": "@EgoDriv",
        "text": "Fuck it we ball",
        "url": "https://x.com/EgoDriv/status/1795407563229639089",
        "likes": 14571,
        "views": 1191380,
    },
    {
        "tunnel": "ball_core_L3_myth",
        "layer": 3,
        "author": "@AdrianDparody",
        "text": "fuck it we ball",
        "url": "https://x.com/AdrianDparody/status/2009450399724655091",
        "likes": 12327,
        "views": 180762,
    },
    # L2 ECONOMY
    {
        "tunnel": "ball_economy_L2",
        "layer": 2,
        "author": "@uncledoomer",
        "text": "living in a sort of fuck it we ball ass economy",
        "url": "https://x.com/uncledoomer/status/2077738289281311084",
        "likes": 2321,
        "reposts": 84,
        "views": 108080,
        "replies": 60,
        "note": "DEEP THREAD — career/retirement nihilism; 60 replies",
    },
    {
        "tunnel": "ball_economy_L2",
        "layer": 2,
        "author": "@DonShift3",
        "text": "bust out phase of the economy. staring down a civil war and world war",
        "url": "https://x.com/DonShift3/status/2077751641588334871",
        "likes": 61,
        "note": "reply under uncledoomer",
    },
    {
        "tunnel": "ball_economy_L2",
        "layer": 2,
        "author": "@orchidcamp",
        "text": "Fuck it we ball is a type of prayer. any resilience you lack u can make up by saying that enough times",
        "url": "https://x.com/orchidcamp/status/1821302183205224717",
        "likes": 686,
        "reposts": 126,
        "note": "THEOLOGY OF BALL",
    },
    # L1 LIVE HOT
    {
        "tunnel": "reply_targets_hot",
        "layer": 1,
        "author": "@cryptokillua99",
        "text": "I know @himgajria motion and im here for it. Fuck it we ball",
        "url": "https://x.com/cryptokillua99/status/2081949091248914894",
        "likes": 49,
        "replies": 13,
        "views": 5595,
        "note": "LIVE — open reply window",
    },
    {
        "tunnel": "reply_targets_hot",
        "layer": 1,
        "author": "@Calupoh_III",
        "text": "took a quirked up white boy to do it but fuck it we ball",
        "url": "https://x.com/Calupoh_III/status/2081913641927122998",
        "likes": 37,
        "views": 1867,
    },
    {
        "tunnel": "reply_targets_hot",
        "layer": 1,
        "author": "@NinetySvn97",
        "text": "One less than favorable PPV does not shake me. Fuck it, we ball",
        "url": "https://x.com/NinetySvn97/status/2081805626385072441",
        "likes": 54,
        "views": 671,
    },
    {
        "tunnel": "reply_targets_hot",
        "layer": 1,
        "author": "@sinennn000",
        "text": "got another rejection letter today but fuck it, we ball",
        "url": "https://x.com/sinennn000/status/2081799876283625861",
        "likes": 17,
        "note": "rejection → ball",
    },
    {
        "tunnel": "reply_targets_hot",
        "layer": 1,
        "author": "@bagel_leaf",
        "text": "fuck it we ball mentality is awesome until no money cuz u fucked and balled it",
        "url": "https://x.com/bagel_leaf/status/2076699498257219671",
        "likes": 301,
        "views": 12571,
        "note": "meta-ball",
    },
    # SCIHUB
    {
        "tunnel": "scihub_freedom",
        "layer": 2,
        "author": "@kaleblovingier",
        "text": "Long live Sci-hub, long live Aaron Swartz.",
        "url": "https://x.com/kaleblovingier/status/2081229240629116938",
        "likes": 0,
        "views": 18,
        "note": "YOUR VOICE",
    },
    {
        "tunnel": "scihub_freedom",
        "layer": 2,
        "author": "@scottrealengel",
        "text": "Always remember Aaron Swartz who died trying to help humanity",
        "url": "https://x.com/scottrealengel/status/2081937243380560329",
        "likes": 1,
    },
    {
        "tunnel": "scihub_freedom",
        "layer": 2,
        "author": "@NarcissusWaters",
        "text": "Alexandra Elbakyan hideout Kazakhstan; Aaron Swartz stain on Obama legacy",
        "url": "https://x.com/NarcissusWaters/status/2081903363172741580",
        "likes": 0,
    },
    {
        "tunnel": "scihub_freedom",
        "layer": 2,
        "author": "@coconut_jpgg",
        "text": "Lookup Aaron Swartz for a 10 on scary tech history scale",
        "url": "https://x.com/coconut_jpgg/status/2081957668726431934",
        "likes": 1,
        "views": 541,
    },
    # VALHALLA
    {
        "tunnel": "valhalla_L2",
        "layer": 2,
        "author": "@JeremiahGeiger2",
        "text": "TIL VALHALLA my brothers and sisters",
        "url": "https://x.com/JeremiahGeiger2/status/2080650093724610993",
        "likes": 10,
        "note": "memorial register — not meme spam",
    },
    {
        "tunnel": "valhalla_L2",
        "layer": 2,
        "author": "@BacksJim",
        "text": "Remember our heroes. Til Valhalla",
        "url": "https://x.com/BacksJim/status/2079905406545969536",
        "likes": 5,
    },
    # BUILDERS
    {
        "tunnel": "zero_budget",
        "layer": 2,
        "author": "@PashaBorsai",
        "text": "How to stay broke as a founder: Build without shipping / Scroll Twitter instead of coding",
        "url": "https://x.com/PashaBorsai/status/2081001566631248186",
        "likes": 29,
        "replies": 22,
    },
    {
        "tunnel": "zero_budget",
        "layer": 2,
        "author": "@starter_story",
        "text": "taught himself to ship by building 20 apps in 12 months; sold 2 for quarter million",
        "url": "https://x.com/starter_story/status/2049302600533881180",
        "likes": 363,
    },
    {
        "tunnel": "build_public_ai",
        "layer": 2,
        "author": "@aliceisaway_",
        "text": "fuck it we ball strategy has widespread adoption even from giants as big as OpenAI",
        "url": "https://x.com/aliceisaway_/status/2080701042275082354",
        "likes": 1,
    },
    {
        "tunnel": "build_public_ai",
        "layer": 2,
        "author": "@aliceisaway_",
        "text": "alternate budget-friendly approach of fuck it we ball",
        "url": "https://x.com/aliceisaway_/status/2080671130117881897",
        "likes": 1,
    },
]

targets = [
    {
        "rank": 1,
        "handle": "@uncledoomer",
        "post": "https://x.com/uncledoomer/status/2077738289281311084",
        "why": "108k views, 60 replies, economy-ball frame",
        "score": 95,
    },
    {
        "rank": 2,
        "handle": "@NeptuniusIII",
        "post": "https://x.com/NeptuniusIII/status/1834717139283968028",
        "why": "3.6M views evergreen — quote the 4 horsemen",
        "score": 92,
    },
    {
        "rank": 3,
        "handle": "@svtxtism",
        "post": "https://x.com/svtxtism/status/1874027719761297781",
        "why": "5.5M views ritual frame",
        "score": 90,
    },
    {
        "rank": 4,
        "handle": "@cryptokillua99",
        "post": "https://x.com/cryptokillua99/status/2081949091248914894",
        "why": "LIVE 5.5k views 13 replies — open window",
        "score": 88,
    },
    {
        "rank": 5,
        "handle": "@bagel_leaf",
        "post": "https://x.com/bagel_leaf/status/2076699498257219671",
        "why": "301 likes meta-ball",
        "score": 80,
    },
    {
        "rank": 6,
        "handle": "@orchidcamp",
        "post": "https://x.com/orchidcamp/status/1821302183205224717",
        "why": "ball as prayer theology",
        "score": 78,
    },
    {
        "rank": 7,
        "handle": "@NinetySvn97",
        "post": "https://x.com/NinetySvn97/status/2081805626385072441",
        "why": "live resilience ball",
        "score": 70,
    },
    {
        "rank": 8,
        "handle": "@sinennn000",
        "post": "https://x.com/sinennn000/status/2081799876283625861",
        "why": "rejection ball",
        "score": 68,
    },
    {
        "rank": 9,
        "handle": "@PashaBorsai",
        "post": "https://x.com/PashaBorsai/status/2081001566631248186",
        "why": "broke founder thread — 22 replies",
        "score": 65,
    },
    {
        "rank": 10,
        "handle": "@youngthug",
        "post": "https://x.com/youngthug/status/664207204975845376",
        "why": "canon — quote carefully",
        "score": 60,
    },
]

replies = [
    {
        "target": "@uncledoomer",
        "text": "FUCK IT WE BALL ASS ECONOMY. ZERO dollars. Still shipping. TIL VALHALLA.",
    },
    {
        "target": "@NeptuniusIII",
        "text": "5th horseman just pulled up: TIL VALHALLA. FUCK IT WE FUCKING BALL.",
    },
    {
        "target": "@cryptokillua99",
        "text": "Motion recognized. Zero dollars. Still dangerous. FUCK IT WE FUCKING BALL.",
    },
    {
        "target": "@bagel_leaf",
        "text": "no money cuz we balled it is the tuition. LONG LIVE SCI-HUB. FUCK IT WE FUCKING BALL.",
    },
    {
        "target": "@orchidcamp",
        "text": "it is a prayer. I RELAPSED. IM OBSESSED WITH AI. still praying: FUCK IT WE FUCKING BALL.",
    },
    {
        "target": "@sinennn000",
        "text": "rejection letter is just the universe loading the next level. POWERSHELL ME UP. FUCK IT WE BALL.",
    },
    {
        "target": "@PashaBorsai",
        "text": "missed one: wait for permission. we dont. ZERO budget. STILL FUCKING BALLING.",
    },
    {
        "target": "@svtxtism",
        "text": "every day is final day of fuck it we ball. AND IT DONT STOP. TIL VALHALLA.",
    },
]


def main() -> None:
    with (DIR / "intel.jsonl").open("a", encoding="utf-8") as f:
        for h in hits:
            h = dict(h)
            h["captured_at"] = now
            h["source"] = "deep_tunnel_dig"
            f.write(json.dumps(h, ensure_ascii=False) + "\n")

    (DIR / "REPLY_TARGETS.json").write_text(
        json.dumps(targets, indent=2), encoding="utf-8"
    )

    blocks = []
    for r in replies:
        blocks.extend([f"→ {r['target']}", r["text"], "", "---", ""])
    (DIR / "DEEP_REPLIES.txt").write_text("\n".join(blocks), encoding="utf-8")

    state_path = DIR / "state.json"
    state = (
        json.loads(state_path.read_text(encoding="utf-8"))
        if state_path.exists()
        else {"tunnels": {}}
    )
    for h in hits:
        tid = h["tunnel"]
        if tid not in state["tunnels"]:
            state["tunnels"][tid] = {
                "id": tid,
                "role": "deep",
                "query": "",
                "drafts_emitted": 0,
                "posts_sent": 0,
                "intel_hits": 0,
            }
        state["tunnels"][tid]["intel_hits"] = (
            state["tunnels"][tid].get("intel_hits", 0) + 1
        )
        state["tunnels"][tid]["last_armed"] = now

    bumps = {
        "ball_core": 6,
        "reply_targets_hot": 5,
        "scihub_freedom": 4,
        "valhalla": 2,
        "zero_budget": 2,
        "build_public_ai": 2,
    }
    for tid, n in bumps.items():
        if tid in state["tunnels"]:
            state["tunnels"][tid]["intel_hits"] = (
                state["tunnels"][tid].get("intel_hits", 0) + n
            )
            state["tunnels"][tid]["last_armed"] = now

    state["deep_dig_at"] = now
    state["deep_hits"] = len(hits)
    state["updated_at"] = now
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    md = f"""# X TUNNELS — DEEP MAP (L1 → L3)

Armed deep dig: `{now}`  
New intel this dig: **{len(hits)}** hits

## Layers

| Layer | Name | Purpose |
|-------|------|---------|
| L1 | Surface / live | last 48h ball posts, open reply windows |
| L2 | Structure | economy-ball, scihub, builders, valhalla memorial |
| L3 | Myth | Young Thug canon, multi-million-view horsemen memes |

## Highest-leverage moves RIGHT NOW

1. **Quote** @uncledoomer economy-ball (108k views) — frame: we ball because the timeline demands it
2. **Quote** @NeptuniusIII 4 horsemen (3.6M) — add 5th horseman TIL VALHALLA
3. **Reply live** @cryptokillua99 (open 13-reply thread, 5.5k views)
4. **Own lane** double down Sci-Hub / Aaron Swartz — already your bio + recent posts
5. **Do NOT spam** Til Valhalla under military memorials as meme — sacred register

## Your account (@kaleblovingier)

- Bio: Knowledge Is Power; RIP Aaron Swartz
- Recent: "Long live Sci-hub, long live Aaron Swartz."
- Reach: low views (9–33) — attach to L3 myths + live L1 windows

## Files

- `REPLY_TARGETS.json` — ranked hosts
- `DEEP_REPLIES.txt` — paste-ready replies
- `intel.jsonl` — full capture log
"""
    (DIR / "DEEP_MAP.md").write_text(md, encoding="utf-8")

    # absorb high-signal phrases for engine
    atoms = [
        "fuck it we ball ass economy",
        "4 horsemen of mens mental health",
        "final day of fuck it we ball",
        "yea but fuck it we ball",
        "Fuck it we ball is a type of prayer",
        "no money cuz u fucked and balled it",
        "got another rejection letter today but fuck it we ball",
        "Long live Sci-hub, long live Aaron Swartz",
        "ZERO dollars. Still shipping",
        "5th horseman: TIL VALHALLA",
        "wait for permission. we dont",
        "bust out phase of the economy",
    ]
    (DIR / "absorbed_atoms.txt").write_text("\n".join(atoms) + "\n", encoding="utf-8")

    print(f"DEEP DIG complete: {len(hits)} hits")
    print(f"Targets: {len(targets)}")
    print(f"Replies ready: {len(replies)}")
    print("Wrote DEEP_MAP.md REPLY_TARGETS.json DEEP_REPLIES.txt absorbed_atoms.txt")


if __name__ == "__main__":
    main()
