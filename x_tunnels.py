#!/usr/bin/env python3
"""
X TUNNELS — autonomous ball distribution + intel rails for X/Twitter.

What this does:
  1. Defines named "tunnels" (query lanes / reply targets / drop queues)
  2. Pulls posts from DROPS.txt into X-ready drafts (<=280 chars)
  3. Writes tunnel intel + draft queue under ./x_tunnels/
  4. Optionally POSTs via official X API v2 if credentials exist
  5. Loop mode keeps regenerating drafts on a timer

What this does NOT do without your keys:
  - Scrape or spam X. Live search stays in Grok (I can tunnel for you there).
  - Post anything unless you pass --post AND set env credentials.

Env for live post (optional):
  X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
  or TWITTER_BEARER_TOKEN (read-only; cannot post alone)

Usage:
  python x_tunnels.py                  # arm all tunnels, fill draft queue
  python x_tunnels.py --status         # show tunnel state
  python x_tunnels.py --loop 600       # re-arm every 10 min
  python x_tunnels.py --post 1         # post next 1 draft (needs OAuth 1.0a)
  python x_tunnels.py --absorb-intel   # fold intel phrases into engine atoms file
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIR = ROOT / "x_tunnels"
DROPS = ROOT / "DROPS.txt"
ENGINE = ROOT / "# main.py"
STATE = DIR / "state.json"
DRAFTS = DIR / "draft_queue.jsonl"
INTEL = DIR / "intel.jsonl"
ATOMS_OUT = DIR / "absorbed_atoms.txt"
HOOK = "FUCK IT WE FUCKING BALL"

# ── Base tunnel definitions (more rails = more autonomous surface area) ────
_BASE_TUNNELS: list[dict] = [
    {
        "id": "ball_core",
        "role": "drop",
        "query": '"fuck it we ball" OR "FUCK IT WE BALL"',
        "mode": "Latest",
        "priority": 1,
        "notes": "Primary slogan stream — high velocity meme oxygen",
    },
    {
        "id": "valhalla",
        "role": "drop",
        "query": '"til valhalla" OR "til Valhalla" OR "Til Valhalla"',
        "mode": "Latest",
        "priority": 2,
        "notes": "Warrior closer tunnel — pair with BALL drops",
    },
    {
        "id": "scihub_freedom",
        "role": "engage",
        "query": "sci-hub OR scihub OR \"knowledge wants to be free\"",
        "mode": "Latest",
        "priority": 2,
        "notes": "Aaron Swartz lane — matches @kaleblovingier bio energy",
    },
    {
        "id": "build_public_ai",
        "role": "engage",
        "query": '"building in public" AI OR "built with AI" $0 OR broke',
        "mode": "Latest",
        "priority": 3,
        "notes": "Obsessed-with-AI builder cluster",
    },
    {
        "id": "powershell_run",
        "role": "drop",
        "query": "powershell OR \"fuck it we ball\" coding OR shipping",
        "mode": "Latest",
        "priority": 3,
        "notes": "POWERSHELL ME UP crossover",
    },
    {
        "id": "addiction_fix",
        "role": "engage",
        "query": '"fuck addiction" OR sobriety OR relapsed recovery',
        "mode": "Latest",
        "priority": 4,
        "notes": "FUCK ADDICTION WHILE WE FIX IT lane — careful tone",
    },
    {
        "id": "reply_targets_hot",
        "role": "reply",
        "query": '"fuck it we ball" min_faves:5',
        "mode": "Latest",
        "priority": 1,
        "notes": "Higher-engagement hosts for quote/reply drops",
    },
    {
        "id": "self_brand",
        "role": "monitor",
        "query": "from:kaleblovingier OR from:1_OBadBjrd OR from:klovingi",
        "mode": "Latest",
        "priority": 1,
        "notes": "Your handles — avoid self-collision, track reach",
    },
    {
        "id": "zero_budget",
        "role": "engage",
        "query": '"no budget" OR "zero dollars" OR "broke as hell" building OR shipping',
        "mode": "Latest",
        "priority": 3,
        "notes": "ZERO dollars still dangerous cluster",
    },
    {
        "id": "alive_run",
        "role": "drop",
        "query": '"we ball" OR "still balling" OR "and it don\'t stop"',
        "mode": "Latest",
        "priority": 2,
        "notes": "Adjacent ball slang — widen surface",
    },
    # ── DEEP LAYERS (L2/L3) ─────────────────────────────────────────────
    {
        "id": "ball_core_L3_myth",
        "role": "quote",
        "query": '"fuck it we ball" min_faves:1000',
        "mode": "Top",
        "priority": 1,
        "notes": "L3 myth: Young Thug canon, multi-million view horsemen memes",
    },
    {
        "id": "ball_economy_L2",
        "role": "quote",
        "query": '"fuck it we ball" (economy OR career OR retirement OR broke)',
        "mode": "Latest",
        "priority": 1,
        "notes": "L2 structure: ball-as-economy / doomer frame",
    },
    {
        "id": "valhalla_L2",
        "role": "engage",
        "query": '"til valhalla" OR "Til Valhalla" min_faves:3',
        "mode": "Latest",
        "priority": 4,
        "notes": "L2 sacred/military — engage carefully, not meme spam",
    },
    {
        "id": "ball_theology",
        "role": "quote",
        "query": '"fuck it we ball" (prayer OR mentality OR will to live)',
        "mode": "Latest",
        "priority": 2,
        "notes": "L2 theology of ball — orchidcamp frame",
    },
    {
        "id": "rejection_ball",
        "role": "reply",
        "query": '"fuck it we ball" (rejection OR rejected OR failed OR broke)',
        "mode": "Latest",
        "priority": 2,
        "notes": "L1/L2 empathy replies on rejection posts",
    },
    {
        "id": "aaron_swartz",
        "role": "engage",
        "query": '"Aaron Swartz" OR Aaronsw OR Elbakyan',
        "mode": "Latest",
        "priority": 2,
        "notes": "Deep scihub rail — matches @kaleblovingier bio",
    },
    # ── CANCER TUNNEL (deep L1 → L3) ────────────────────────────────────
    {
        "id": "cancer_L1_live",
        "role": "reply",
        "query": '"fuck cancer" OR "FUCK CANCER"',
        "mode": "Latest",
        "priority": 1,
        "notes": "CANCER L1: live fuck-cancer surface — empathy first, no meme on grief",
    },
    {
        "id": "cancer_ball_crossover",
        "role": "reply",
        "query": 'cancer ("fuck it we ball" OR "we ball" OR chemo OR oncology)',
        "mode": "Latest",
        "priority": 1,
        "notes": "CANCER×BALL: rare dual-signal posts — highest leverage replies",
    },
    {
        "id": "cancer_L2_fighter",
        "role": "engage",
        "query": 'cancer (survivor OR "stage 4" OR chemo OR remission OR "still fighting") min_faves:3',
        "mode": "Latest",
        "priority": 2,
        "notes": "CANCER L2: fighters/survivors — support + strength, not slogans only",
    },
    {
        "id": "cancer_L2_research",
        "role": "quote",
        "query": '"cancer treatment" OR "cancer research" OR immunotherapy OR oncology breakthrough',
        "mode": "Latest",
        "priority": 3,
        "notes": "CANCER L2 research — knowledge-is-power / scihub adjacency",
    },
    {
        "id": "cancer_L3_myth",
        "role": "quote",
        "query": '"fuck cancer" min_faves:1000',
        "mode": "Top",
        "priority": 1,
        "notes": "CANCER L3 myth: Dream hug canon, mass-reach fuck-cancer posts",
    },
    {
        "id": "cancer_care_sacred",
        "role": "engage",
        "query": '"fuck cancer" (passed OR funeral OR miss OR RIP OR aunt OR mom OR dad)',
        "mode": "Latest",
        "priority": 4,
        "notes": "SACRED grief lane — short human only, never ball-spam",
    },
    # ── RED OCTOBER TUNNEL (DIVE DIVE DIVE) ─────────────────────────────
    {
        "id": "red_october_L1",
        "role": "reply",
        "query": '"Red October" OR "Hunt for Red October" OR "dive dive dive"',
        "mode": "Latest",
        "priority": 1,
        "notes": "RED OCTOBER L1: live surface — Clancy / dive dive dive / Phillies Red October",
    },
    {
        "id": "red_october_sub",
        "role": "engage",
        "query": 'Ramius OR "one ping only" OR "rig for ultra quiet" OR "Sean Connery" submarine',
        "mode": "Latest",
        "priority": 1,
        "notes": "RED OCTOBER L1/L2: submariner / Clancy quote culture",
    },
    {
        "id": "red_october_dive",
        "role": "drop",
        "query": '"dive dive dive" OR "DIVE DIVE DIVE" OR "hands to dive stations" OR "deep dive"',
        "mode": "Latest",
        "priority": 1,
        "notes": "DIVE DIVE DIVE rail — depth charge energy for all tunnels",
    },
    {
        "id": "red_october_L2_clancy",
        "role": "quote",
        "query": '"Hunt for Red October" OR "Tom Clancy" (submarine OR Ramius OR Connery)',
        "mode": "Latest",
        "priority": 2,
        "notes": "L2 structure: Clancy techno-thriller / navy film discourse",
    },
    {
        "id": "red_october_L2_phillies",
        "role": "engage",
        "query": '"Red October" (Phillies OR baseball OR playoffs OR World Series)',
        "mode": "Latest",
        "priority": 3,
        "notes": "Phillies Red October sports lane — ball-adjacent sports chaos",
    },
    {
        "id": "red_october_L3_myth",
        "role": "quote",
        "query": '"Hunt for Red October" min_faves:100',
        "mode": "Top",
        "priority": 1,
        "notes": "L3 myth: Clancy birthday, classic navy film polls, mass reach",
    },
    {
        "id": "red_october_torpedo",
        "role": "reply",
        "query": 'torpedo (Ramius OR "Red October" OR submarine) OR "into the path of"',
        "mode": "Latest",
        "priority": 2,
        "notes": "Ramius turns into the torpedo — close the gap before it arms",
    },
    # ── YUNG METRO TUNNEL (IF YUNG METRO DONT…) ────────────────────────
    {
        "id": "yung_metro_L1",
        "role": "reply",
        "query": '"if young metro" OR "yung metro" OR "young metro don\'t" OR "metro don\'t trust"',
        "mode": "Latest",
        "priority": 1,
        "notes": "IF YUNG METRO DONT — live tagline surface",
    },
    {
        "id": "yung_metro_trust",
        "role": "drop",
        "query": '"don\'t trust you" OR "dont trust you" (metro OR young OR yung) OR "ima shoot" metro',
        "mode": "Latest",
        "priority": 1,
        "notes": "trust/shoot tagline variants — meme oxygen",
    },
    {
        "id": "yung_metro_L2_producer",
        "role": "engage",
        "query": '"Metro Boomin" OR @MetroBoomin OR "Future" Jumpman OR "Young Metro"',
        "mode": "Latest",
        "priority": 2,
        "notes": "L2: producer / Future / Jumpman culture",
    },
    {
        "id": "yung_metro_ball",
        "role": "reply",
        "query": 'metro (ball OR "fuck it" OR trust OR tagline OR producer) OR "if young metro" ball',
        "mode": "Latest",
        "priority": 2,
        "notes": "METRO × BALL crossover",
    },
    {
        "id": "yung_metro_L3_myth",
        "role": "quote",
        "query": '"If Young Metro" OR "if young metro don\'t trust" min_faves:50',
        "mode": "Top",
        "priority": 1,
        "notes": "L3 myth: viral tagline posts, BuzzFeed origin, mass memes",
    },
    # ── CORVIDPHOENIX TUNNEL (ash → flock → flight) ────────────────────
    {
        "id": "corvidphoenix_L1",
        "role": "reply",
        "query": '"phoenix rising" OR "rise from the ashes" OR "from the ashes" (bird OR crow OR raven OR flock OR phoenix)',
        "mode": "Latest",
        "priority": 1,
        "notes": "CORVIDPHOENIX L1: live rebirth surface — ashes / phoenix rising",
    },
    {
        "id": "corvidphoenix_caw",
        "role": "drop",
        "query": '"caw caw" OR "CAW CAW" OR corvid (fire OR ashes OR phoenix OR rebirth OR rise)',
        "mode": "Latest",
        "priority": 1,
        "notes": "CAW FROM THE FIRE — corvid × flame hook stack",
    },
    {
        "id": "corvidphoenix_flock",
        "role": "engage",
        "query": 'flock (rebirth OR phoenix OR ashes OR rise OR "come back") OR crow (phoenix OR rebirth OR ashes)',
        "mode": "Latest",
        "priority": 2,
        "notes": "L2: flock rebirth — collective rise, not solo hero myth only",
    },
    {
        "id": "corvidphoenix_raven",
        "role": "engage",
        "query": 'raven (phoenix OR rebirth OR ashes OR fire OR rise) OR "black bird" (phoenix OR ashes)',
        "mode": "Latest",
        "priority": 2,
        "notes": "L2: raven / black bird × phoenix myth lanes",
    },
    {
        "id": "corvidphoenix_L3_myth",
        "role": "quote",
        "query": '"phoenix rising" OR "rise from the ashes" min_faves:50',
        "mode": "Top",
        "priority": 1,
        "notes": "L3 myth: mass-reach phoenix rebirth posts",
    },
]

# ── Named PROTOCOLS (mood_mixer / k-lab / starfleet) → X rails ────────────
PROTOCOLS: list[dict] = [
    {
        "id": "proto_raptor",
        "role": "drop",
        "query": "raptor OR \"caw caw\" OR \"CAW CAW\" bird energy OR flock",
        "mode": "Latest",
        "priority": 2,
        "notes": "RAPTOR PROTOCOL — CAW CAW CAW CAW CAW",
        "protocol": "RAPTOR",
    },
    {
        "id": "proto_drone_corvid_conure",
        "role": "drop",
        "query": "corvid OR conure OR \"drone\" (bird OR flock OR caw OR squawk)",
        "mode": "Latest",
        "priority": 2,
        "notes": "DRONE CORVID CONURE HYBRID PROTOCOL",
        "protocol": "DRONE_CORVID_CONURE_HYBRID",
    },
    {
        "id": "proto_beak_maxxed",
        "role": "drop",
        "query": "\"beak\" OR maxxed OR \"maxxed out\" OR \"raw lyrics\" club",
        "mode": "Latest",
        "priority": 3,
        "notes": "BEAK MAXXXED PROTOCOL",
        "protocol": "BEAK_MAXXED",
    },
    {
        "id": "proto_beak_mogg",
        "role": "engage",
        "query": "mogg OR \"every streamer\" OR \"type shit\" platforms OR allegedly streamer",
        "mode": "Latest",
        "priority": 3,
        "notes": "BEAK MOGG EVERY STREAMER PROTOCOL",
        "protocol": "BEAK_MOGG_STREAMER",
    },
    {
        "id": "proto_bangers_only",
        "role": "drop",
        "query": "\"bangers only\" OR banger club OR \"no filler\" heat OR \"club banger\"",
        "mode": "Latest",
        "priority": 2,
        "notes": "BANGERS ONLY PROTOCOL",
        "protocol": "BANGERS_ONLY",
    },
    {
        "id": "proto_computah",
        "role": "engage",
        "query": "computah OR glitch cyber OR \"beep boop\" OR \"digital bars\" coding",
        "mode": "Latest",
        "priority": 3,
        "notes": "COMPUTAH PROTOCOL",
        "protocol": "COMPUTAH",
    },
    {
        "id": "proto_hug_of_death",
        "role": "engage",
        "query": "\"hug of death\" OR \"overwhelm with love\" OR \"positive chaos\" OR \"raw love\"",
        "mode": "Latest",
        "priority": 3,
        "notes": "HUG OF DEATH WITH LOVE PROTOCOL",
        "protocol": "HUG_OF_DEATH_WITH_LOVE",
    },
    {
        "id": "proto_daft_punk",
        "role": "drop",
        "query": "\"daft punk\" OR \"around the world\" OR \"harder better faster\" OR robot",
        "mode": "Latest",
        "priority": 3,
        "notes": "DAFT PUNK PROTOCOL (k-lab)",
        "protocol": "DAFT_PUNK",
    },
    {
        "id": "proto_reincarnation",
        "role": "engage",
        "query": "reincarnation OR rebirth OR \"come back\" OR \"die and come back\"",
        "mode": "Latest",
        "priority": 4,
        "notes": "REINCARNATION PROTOCOL (k-lab)",
        "protocol": "REINCARNATION",
    },
    {
        "id": "proto_wake",
        "role": "engage",
        "query": "\"stop killing\" OR \"wake up\" OR \"ding dong\" OR NVC nonviolent",
        "mode": "Latest",
        "priority": 4,
        "notes": "WAKE PROTOCOL (k-lab/wake_protocol)",
        "protocol": "WAKE",
    },
    {
        "id": "proto_neverender",
        "role": "drop",
        "query": "neverender OR \"never end\" OR \"and it don't stop\" OR infinite loop",
        "mode": "Latest",
        "priority": 2,
        "notes": "NEVERENDER PROTOCOL (starfleet)",
        "protocol": "NEVERENDER",
    },
    {
        "id": "proto_scorched_earth",
        "role": "drop",
        "query": "\"scorched earth\" OR TARS OR \"burn it down\" shipping OR build",
        "mode": "Latest",
        "priority": 3,
        "notes": "SCORCHED EARTH PROTOCOL TARS",
        "protocol": "SCORCHED_EARTH",
    },
    {
        "id": "proto_dracula",
        "role": "engage",
        "query": "\"tame impala\" OR dracula OR borderline OR \"the less I know\"",
        "mode": "Latest",
        "priority": 4,
        "notes": "TAME IMPALA DRACULA PROTOCOL BORDERLINE VARIANT",
        "protocol": "DRACULA_BORDERLINE",
    },
    {
        "id": "proto_hell_on_earth",
        "role": "drop",
        "query": "\"hell on earth\" OR chaos swarm OR \"we ball\" apocalypse",
        "mode": "Latest",
        "priority": 3,
        "notes": "HELL ON EARTH chaos rail",
        "protocol": "HELL_ON_EARTH",
    },
    {
        "id": "proto_red_october",
        "role": "engage",
        "query": "\"red october\" OR \"silent running\" OR \"hunt for red october\" OR submarine deep",
        "mode": "Latest",
        "priority": 1,
        "notes": "RED OCTOBER PROTOCOL — silent running, deep dive, stealth ship",
        "protocol": "RED_OCTOBER",
    },
    {
        "id": "proto_corvidphoenix",
        "role": "drop",
        "query": "corvid OR crow OR raven (phoenix OR rebirth OR ashes OR \"from the ashes\") OR \"caw caw\" phoenix",
        "mode": "Latest",
        "priority": 1,
        "notes": "CORVIDPHOENIX PROTOCOL — ash → flock → flight; corvid mind + phoenix fire",
        "protocol": "CORVIDPHOENIX",
    },
]


def _duplicate_tunnels(base: list[dict]) -> list[dict]:
    """Mirror every tunnel as a dual-rail (_dup) for doubled surface area."""
    out: list[dict] = []
    for t in base:
        out.append(dict(t))
        dup = dict(t)
        dup["id"] = f"{t['id']}_dup"
        # flip Latest/Top on mirror to catch different ranking surface
        if t.get("mode") == "Latest":
            dup["mode"] = "Top"
        elif t.get("mode") == "Top":
            dup["mode"] = "Latest"
        notes = t.get("notes", "")
        dup["notes"] = f"DUP mirror of {t['id']} — {notes}"
        # slight priority nudge so primaries still sort first on ties
        dup["priority"] = min(5, int(t.get("priority", 3)) + 0)
        out.append(dup)
    return out


def _duplicate_protocols(protocols: list[dict]) -> list[dict]:
    """Duplicate every protocol rail the same way tunnels are doubled."""
    return _duplicate_tunnels(protocols)


# Full armed set: base tunnels + dups + protocols + protocol dups
TUNNELS: list[dict] = _duplicate_tunnels(_BASE_TUNNELS) + _duplicate_protocols(PROTOCOLS)


@dataclass
class Draft:
    id: str
    text: str
    tunnel: str
    chars: int
    created_at: str
    status: str = "queued"  # queued | posted | skipped
    post_id: str | None = None


@dataclass
class TunnelState:
    id: str
    role: str
    query: str
    last_armed: str | None = None
    drafts_emitted: int = 0
    posts_sent: int = 0
    intel_hits: int = 0


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_dirs() -> None:
    DIR.mkdir(parents=True, exist_ok=True)


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {
        "tunnels": {t["id"]: asdict(TunnelState(id=t["id"], role=t["role"], query=t["query"])) for t in TUNNELS},
        "total_drafts": 0,
        "total_posted": 0,
        "created_at": utc_now(),
    }


def save_state(state: dict) -> None:
    state["updated_at"] = utc_now()
    STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def clip_x(text: str, limit: int = 280) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    # hard clip with ellipsis room
    return text[: limit - 1].rstrip() + "…"


def read_drops() -> list[str]:
    if not DROPS.exists():
        return []
    raw = DROPS.read_text(encoding="utf-8")
    chunks = [c.strip() for c in re.split(r"\n---\n", raw) if c.strip()]
    # also handle --- with blank lines
    if len(chunks) <= 1:
        chunks = [c.strip() for c in re.split(r"\n-+\n", raw) if c.strip() and c.strip() != "---"]
    return [c.replace("\n", " ").strip() for c in chunks if c and c != "---"]


def draft_id(text: str, tunnel: str) -> str:
    h = hashlib.sha1(f"{tunnel}|{text}".encode()).hexdigest()[:12]
    return f"d_{h}"


def existing_draft_ids() -> set[str]:
    ids: set[str] = set()
    if not DRAFTS.exists():
        return ids
    for line in DRAFTS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            ids.add(json.loads(line)["id"])
        except Exception:
            continue
    return ids


def append_draft(d: Draft) -> None:
    with DRAFTS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(d), ensure_ascii=False) + "\n")


def append_intel(record: dict) -> None:
    with INTEL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def assign_tunnel(i: int, post: str) -> str:
    """Route drop text to a tunnel by keyword affinity (protocols first)."""
    u = post.upper()
    # Protocol affinity (primary ids; dups are search/monitor rails)
    rules = [
        # CORVIDPHOENIX first — before RAPTOR bare "CAW" and before generic CORVID
        ("proto_corvidphoenix", ("CORVIDPHOENIX", "CORVID PHOENIX", "FROM THE ASHES", "PHOENIX RISING", "ASH TO FLOCK", "SAME MURDER", "SECOND LIFE", "GOLD FIRE", "BLACK FEATHERS", "CAW FROM THE FIRE")),
        ("corvidphoenix_caw", ("CAW FROM THE FIRE",)),
        ("corvidphoenix_L1", ("RISE FROM THE ASHES",)),
        ("corvidphoenix_flock", ("FLOCK RISE", "FLOCK REBIRTH", "COLLECTIVE RISE", "FEED THE FLOCK")),
        ("proto_raptor", ("RAPTOR", "CAW CAW")),
        ("proto_drone_corvid_conure", ("CORVID", "CONURE", "DRONE", "HYBRID", "SQUAWK")),
        ("proto_beak_maxxed", ("BEAK MAXX", "MAXXED", "BEAK")),
        ("proto_beak_mogg", ("MOGG", "STREAMER", "ALLEGEDLY", "TYPE SHIT")),
        ("proto_bangers_only", ("BANGERS ONLY", "BANGER", "NO FILLER")),
        ("proto_computah", ("COMPUTAH", "GLITCH", "CYBER", "BEEP BOOP", "DIGITAL")),
        ("proto_hug_of_death", ("HUG OF DEATH", "HUG", "WITH LOVE")),
        ("proto_daft_punk", ("DAFT PUNK", "HARDER BETTER", "AROUND THE WORLD")),
        ("proto_reincarnation", ("REINCARNATION", "REBIRTH")),
        ("proto_wake", ("WAKE", "STOP KILLING", "DING DONG")),
        ("proto_neverender", ("NEVERENDER", "NEVER END", "DON'T STOP", "DONT STOP")),
        ("proto_scorched_earth", ("SCORCHED", "TARS")),
        ("proto_dracula", ("DRACULA", "TAME IMPALA", "BORDERLINE")),
        ("proto_hell_on_earth", ("HELL ON EARTH", "HELL")),
        ("proto_red_october", ("RED OCTOBER", "SILENT RUNNING", "SUBMARINE", "DEEP DIVE", "STEALTH")),
        ("cancer_ball_crossover", ("FUCK CANCER", "CANCER", "CHEMO", "ONCOLOGY", "SURVIVOR")),
        ("cancer_L1_live", ("FUCK CANCER",)),
        ("red_october_dive", ("DIVE DIVE DIVE", "DIVE", "RED OCTOBER", "RAMIUS", "ONE PING", "TORPEDO", "SUBMARINE")),
        ("red_october_L1", ("RED OCTOBER", "HUNT FOR RED")),
        ("yung_metro_L1", ("YUNG METRO", "YOUNG METRO", "IF YOUNG METRO", "METRO DONT", "METRO DON'T", "METRO BOOMIN")),
        ("yung_metro_trust", ("DONT TRUST YOU", "DON'T TRUST YOU", "IMA SHOOT", "GON SHOOT")),
        ("valhalla", ("VALHALLA", "DIE WELL")),
        ("scihub_freedom", ("SCI-HUB", "SCI HUB", "FREEDOM", "KNOWLEDGE")),
        ("addiction_fix", ("ADDICTION", "RELAPSED", "SOBRIETY")),
        ("build_public_ai", ("OBSESSED WITH AI", "AI", "POWERSHELL")),
        ("powershell_run", ("POWERSHELL", "RUUUUUN", "REEEEE")),
        ("zero_budget", ("BUDGET", "BROKE", "ZERO", "NO PERMISSION")),
        ("ball_core", ("WE BALL", "FUCKING BALL", "BALL")),
    ]
    for tid, keys in rules:
        if any(k in u for k in keys):
            return tid
    # round-robin fallback across drop tunnels (prefer primaries, not _dup)
    drop_ids = [t["id"] for t in TUNNELS if t["role"] == "drop" and not t["id"].endswith("_dup")]
    if not drop_ids:
        drop_ids = [t["id"] for t in TUNNELS if t["role"] == "drop"]
    return drop_ids[i % len(drop_ids)]


def arm_tunnels(max_new: int = 60) -> tuple[int, dict]:
    ensure_dirs()
    state = load_state()
    # sync any new tunnel defs
    for t in TUNNELS:
        if t["id"] not in state["tunnels"]:
            state["tunnels"][t["id"]] = asdict(
                TunnelState(id=t["id"], role=t["role"], query=t["query"])
            )

    posts = read_drops()
    if not posts:
        print("No DROPS.txt content. Run: python \"# main.py\" first.")
        return 0, state

    seen = existing_draft_ids()
    created = 0
    now = utc_now()

    for i, post in enumerate(posts):
        if created >= max_new:
            break
        text = clip_x(post)
        if not text:
            continue
        tid = assign_tunnel(i, text)
        did = draft_id(text, tid)
        if did in seen:
            continue
        d = Draft(
            id=did,
            text=text,
            tunnel=tid,
            chars=len(text),
            created_at=now,
            status="queued",
        )
        append_draft(d)
        seen.add(did)
        created += 1
        st = state["tunnels"].setdefault(
            tid, asdict(TunnelState(id=tid, role="drop", query=""))
        )
        st["drafts_emitted"] = st.get("drafts_emitted", 0) + 1
        st["last_armed"] = now

    # stamp all tunnels as armed this cycle (intel ready)
    for t in TUNNELS:
        st = state["tunnels"][t["id"]]
        st["last_armed"] = now
        st["query"] = t["query"]
        st["role"] = t["role"]

    state["total_drafts"] = state.get("total_drafts", 0) + created
    save_state(state)

    # human-readable tunnel map
    map_path = DIR / "TUNNEL_MAP.md"
    n_base = len(_BASE_TUNNELS)
    n_proto = len(PROTOCOLS)
    n_total = len(TUNNELS)
    lines = [
        "# X Tunnels — Autonomous Map (DUPLICATED + PROTOCOLS)",
        "",
        f"Armed: `{now}`",
        f"New drafts this cycle: **{created}**",
        f"Rails: **{n_total}** total = {n_base} base ×2 + {n_proto} protocols ×2",
        "",
        "## Base tunnels (+ `_dup` mirrors)",
        "",
        "| id | role | priority | mode | query |",
        "|----|------|----------|------|-------|",
    ]
    base_ids = {t["id"] for t in _BASE_TUNNELS} | {f"{t['id']}_dup" for t in _BASE_TUNNELS}
    for t in sorted((x for x in TUNNELS if x["id"] in base_ids), key=lambda x: (x["priority"], x["id"])):
        lines.append(
            f"| `{t['id']}` | {t['role']} | {t['priority']} | {t.get('mode','')} | `{t['query']}` |"
        )
    lines += [
        "",
        "## Protocols (+ `_dup` mirrors)",
        "",
        "| id | protocol | role | priority | mode | query |",
        "|----|----------|------|----------|------|-------|",
    ]
    for t in sorted((x for x in TUNNELS if x["id"] not in base_ids), key=lambda x: (x["priority"], x["id"])):
        proto = t.get("protocol", "—")
        lines.append(
            f"| `{t['id']}` | {proto} | {t['role']} | {t['priority']} | {t.get('mode','')} | `{t['query']}` |"
        )
    lines += [
        "",
        "## Ops",
        "",
        "- Every tunnel and every protocol is **duplicated** (`_dup` flips Latest↔Top).",
        "- Grok (this chat) runs **live X search** into each tunnel/protocol query.",
        "- This script arms **draft queues** + optional API post.",
        "- `draft_queue.jsonl` = ready to drop. `intel.jsonl` = observed posts.",
        "",
        f"HOOK: **{HOOK}** · TIL VALHALLA · ALL PROTOCOLS ARMED.",
        "",
    ]
    map_path.write_text("\n".join(lines), encoding="utf-8")

    # dedicated protocol map
    proto_map = DIR / "PROTOCOL_MAP.md"
    plines = [
        "# PROTOCOLS — Duplicated X Rails",
        "",
        f"Armed: `{now}`",
        f"Protocols: **{n_proto}** × 2 = **{n_proto * 2}** rails",
        "",
        "| protocol | primary | dup | role | query |",
        "|----------|---------|-----|------|-------|",
    ]
    for p in PROTOCOLS:
        plines.append(
            f"| **{p.get('protocol', p['id'])}** | `{p['id']}` | `{p['id']}_dup` | {p['role']} | `{p['query']}` |"
        )
    plines += [
        "",
        "## Named set",
        "",
        "1. RAPTOR",
        "2. DRONE_CORVID_CONURE_HYBRID",
        "3. BEAK_MAXXED",
        "4. BEAK_MOGG_STREAMER",
        "5. BANGERS_ONLY",
        "6. COMPUTAH",
        "7. HUG_OF_DEATH_WITH_LOVE",
        "8. DAFT_PUNK",
        "9. REINCARNATION",
        "10. WAKE",
        "11. NEVERENDER",
        "12. SCORCHED_EARTH",
        "13. DRACULA_BORDERLINE",
        "14. HELL_ON_EARTH",
        "",
        f"{HOOK}. ALL PROTOCOLS DUPLICATED. TUNNEL LIVE.",
        "",
    ]
    proto_map.write_text("\n".join(plines), encoding="utf-8")
    return created, state


def seed_intel_from_session() -> int:
    """Seed intel.jsonl with known live hits from this Grok session (manual snapshot)."""
    ensure_dirs()
    seeds = [
        {
            "tunnel": "ball_core",
            "author": "@clankeruser",
            "text": "In the wise words of some anon, FUCK IT WE BALL.",
            "url": "https://x.com/clankeruser/status/2081951271573987715",
            "likes": 1,
        },
        {
            "tunnel": "ball_core",
            "author": "@loeyyoualways",
            "text": "FUCK IT WE BALL BRO 🔥",
            "url": "https://x.com/loeyyoualways/status/2081970904939245680",
            "likes": 0,
        },
        {
            "tunnel": "ball_core",
            "author": "@Scamronthebank",
            "text": "My answer to everything is, FUCK IT, WE BALL!!!",
            "url": "https://x.com/Scamronthebank/status/2081047189082587186",
            "likes": 0,
        },
        {
            "tunnel": "valhalla",
            "author": "@pease_bruce",
            "text": "Semper Fi … til Valhalla",
            "url": "https://x.com/pease_bruce/status/2081871856848580611",
            "likes": 0,
        },
        {
            "tunnel": "build_public_ai",
            "author": "@sachinyadav699",
            "text": "$0 funding. a 20 year old spent 10 days building with AI…",
            "url": "https://x.com/sachinyadav699/status/2033114309644165615",
            "likes": 1466,
        },
        {
            "tunnel": "build_public_ai",
            "author": "@_AIAcceleration",
            "text": "Week 2 of building this in public…",
            "url": "https://x.com/_AIAcceleration/status/2081791816962068500",
            "likes": 2,
        },
        {
            "tunnel": "scihub_freedom",
            "author": "@Razteton",
            "text": "Nada superará a sci-hub",
            "url": "https://x.com/Razteton/status/2081948336962048149",
            "likes": 1,
        },
        {
            "tunnel": "self_brand",
            "author": "@kaleblovingier",
            "text": "PROFILE — Knowledge Is Power; RIP Aaron Swartz — 207 followers",
            "url": "https://x.com/kaleblovingier",
            "likes": 0,
        },
    ]
    n = 0
    for s in seeds:
        s["captured_at"] = utc_now()
        s["source"] = "grok_session_seed"
        append_intel(s)
        n += 1
    state = load_state()
    for s in seeds:
        tid = s["tunnel"]
        if tid in state["tunnels"]:
            state["tunnels"][tid]["intel_hits"] = state["tunnels"][tid].get("intel_hits", 0) + 1
    save_state(state)
    return n


def status() -> None:
    ensure_dirs()
    state = load_state()
    print("🔥 X TUNNELS STATUS 🔥\n")
    print(f"dir: {DIR}")
    print(f"total_drafts: {state.get('total_drafts', 0)}")
    print(f"total_posted: {state.get('total_posted', 0)}")
    print(f"updated: {state.get('updated_at', 'never')}\n")
    print(f"{'ID':22} {'ROLE':8} {'DRAFTS':>6} {'POSTS':>5} {'INTEL':>5}  LAST ARMED")
    print("-" * 78)
    for t in TUNNELS:
        st = state["tunnels"].get(t["id"], {})
        print(
            f"{t['id']:22} {t['role']:8} "
            f"{st.get('drafts_emitted', 0):6} {st.get('posts_sent', 0):5} "
            f"{st.get('intel_hits', 0):5}  {st.get('last_armed') or '-'}"
        )
    queued = 0
    if DRAFTS.exists():
        for line in DRAFTS.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                if json.loads(line).get("status") == "queued":
                    queued += 1
            except Exception:
                pass
    print(f"\nqueued drafts: {queued}")
    print(f"draft file: {DRAFTS}")
    print(f"intel file: {INTEL}")
    print(f"map: {DIR / 'TUNNEL_MAP.md'}")


def next_queued(n: int) -> list[dict]:
    if not DRAFTS.exists():
        return []
    out = []
    for line in DRAFTS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except Exception:
            continue
        if row.get("status") == "queued":
            out.append(row)
        if len(out) >= n:
            break
    return out


def rewrite_drafts(rows: list[dict]) -> None:
    """Full rewrite of draft_queue with updated statuses (small file)."""
    if not DRAFTS.exists():
        return
    by_id = {r["id"]: r for r in rows}
    new_lines = []
    for line in DRAFTS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except Exception:
            new_lines.append(line)
            continue
        if row["id"] in by_id:
            new_lines.append(json.dumps(by_id[row["id"]], ensure_ascii=False))
        else:
            new_lines.append(line)
    DRAFTS.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def post_via_api(text: str) -> str:
    """Post with OAuth 1.0a user context. Raises on failure."""
    try:
        import requests
        from requests_oauthlib import OAuth1
    except ImportError as e:
        raise RuntimeError(
            "Install: pip install requests requests-oauthlib"
        ) from e

    key = os.environ.get("X_API_KEY") or os.environ.get("TWITTER_API_KEY")
    secret = os.environ.get("X_API_SECRET") or os.environ.get("TWITTER_API_SECRET")
    token = os.environ.get("X_ACCESS_TOKEN") or os.environ.get("TWITTER_ACCESS_TOKEN")
    token_secret = os.environ.get("X_ACCESS_TOKEN_SECRET") or os.environ.get(
        "TWITTER_ACCESS_TOKEN_SECRET"
    )
    if not all([key, secret, token, token_secret]):
        raise RuntimeError(
            "Missing OAuth creds. Set X_API_KEY, X_API_SECRET, "
            "X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET"
        )

    auth = OAuth1(key, secret, token, token_secret)
    r = requests.post(
        "https://api.twitter.com/2/tweets",
        auth=auth,
        json={"text": text},
        timeout=30,
    )
    if r.status_code not in (200, 201):
        raise RuntimeError(f"X API {r.status_code}: {r.text[:500]}")
    data = r.json()
    return data.get("data", {}).get("id", "unknown")


def post_drafts(n: int, dry_run: bool = False) -> int:
    rows = next_queued(n)
    if not rows:
        print("No queued drafts.")
        return 0
    state = load_state()
    # load all for rewrite
    all_rows = []
    if DRAFTS.exists():
        for line in DRAFTS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    all_rows.append(json.loads(line))
                except Exception:
                    pass
    by_id = {r["id"]: r for r in all_rows}
    sent = 0
    for row in rows:
        text = row["text"]
        print(f"\n→ tunnel={row['tunnel']} chars={row['chars']}")
        print(f"  {text}")
        if dry_run:
            print("  [dry-run] not posted")
            continue
        try:
            pid = post_via_api(text)
            row["status"] = "posted"
            row["post_id"] = pid
            by_id[row["id"]] = row
            sent += 1
            tid = row["tunnel"]
            if tid in state["tunnels"]:
                state["tunnels"][tid]["posts_sent"] = (
                    state["tunnels"][tid].get("posts_sent", 0) + 1
                )
            state["total_posted"] = state.get("total_posted", 0) + 1
            print(f"  posted id={pid}")
            time.sleep(2)  # gentle rate limit
        except Exception as e:
            print(f"  FAIL: {e}")
            break
    if sent:
        rewrite_drafts(list(by_id.values()))
        save_state(state)
    return sent


def absorb_intel() -> int:
    """Write short phrases from intel into absorbed_atoms for manual engine merge."""
    ensure_dirs()
    if not INTEL.exists():
        print("No intel yet.")
        return 0
    phrases = []
    for line in INTEL.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except Exception:
            continue
        t = (row.get("text") or "").strip()
        if 8 <= len(t) <= 120:
            phrases.append(t)
    # unique preserve order
    seen = set()
    uniq = []
    for p in phrases:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    ATOMS_OUT.write_text("\n".join(uniq) + "\n", encoding="utf-8")
    print(f"Absorbed {len(uniq)} phrases → {ATOMS_OUT}")
    return len(uniq)


def print_peek(n: int = 5) -> None:
    rows = next_queued(n)
    print(f"\n=== NEXT {len(rows)} DRAFTS TO DROP ===\n")
    for i, r in enumerate(rows, 1):
        print(f"{i}. [{r['tunnel']}] ({r['chars']}) {r['text']}\n")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Autonomous X tunnels for ball drops")
    p.add_argument("--status", action="store_true")
    p.add_argument("--seed-intel", action="store_true", help="seed intel from last Grok sweep")
    p.add_argument("--absorb-intel", action="store_true")
    p.add_argument("--peek", type=int, default=0, help="show next N drafts")
    p.add_argument("--max-new", type=int, default=60)
    p.add_argument("--post", type=int, default=0, help="post next N drafts via X API")
    p.add_argument("--dry-run", action="store_true", help="with --post, don't actually send")
    p.add_argument("--loop", type=float, default=0, help="re-arm every N seconds")
    args = p.parse_args(argv)

    ensure_dirs()

    if args.status:
        status()
        return 0
    if args.absorb_intel:
        absorb_intel()
        return 0
    if args.post:
        post_drafts(args.post, dry_run=args.dry_run)
        return 0
    if args.peek:
        print_peek(args.peek)
        return 0

    def cycle() -> None:
        if args.seed_intel or not INTEL.exists():
            n = seed_intel_from_session()
            print(f"intel seeded: {n} hits")
        created, _ = arm_tunnels(max_new=args.max_new)
        print(f"armed tunnels={len(TUNNELS)} new_drafts={created}")
        print(f"map → {DIR / 'TUNNEL_MAP.md'}")
        print(f"queue → {DRAFTS}")
        print_peek(5)
        status()

    if args.loop and args.loop > 0:
        print(f"🔥 AUTONOMOUS X TUNNEL LOOP every {args.loop}s — Ctrl+C to stop\n")
        try:
            while True:
                cycle()
                print(f"\n… sleeping {args.loop}s … still tunneling …\n")
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("\nTunnels sealed. TIL VALHALLA.")
            return 0
    else:
        # default arm
        args.seed_intel = True
        cycle()
        print(f"\n{HOOK}. TIL VALHALLA. tunnels live.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
