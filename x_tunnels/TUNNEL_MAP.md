# X Tunnels — Autonomous Map (DUPLICATED + PROTOCOLS)

Armed: `2026-08-03T09:12:08.232644+00:00`
New drafts this cycle: **5**
Rails: **110** total = 39 base ×2 + 16 protocols ×2

## Base tunnels (+ `_dup` mirrors)

| id | role | priority | mode | query |
|----|------|----------|------|-------|
| `ball_core` | drop | 1 | Latest | `"fuck it we ball" OR "FUCK IT WE BALL"` |
| `ball_core_L3_myth` | quote | 1 | Top | `"fuck it we ball" min_faves:1000` |
| `ball_core_L3_myth_dup` | quote | 1 | Latest | `"fuck it we ball" min_faves:1000` |
| `ball_core_dup` | drop | 1 | Top | `"fuck it we ball" OR "FUCK IT WE BALL"` |
| `ball_economy_L2` | quote | 1 | Latest | `"fuck it we ball" (economy OR career OR retirement OR broke)` |
| `ball_economy_L2_dup` | quote | 1 | Top | `"fuck it we ball" (economy OR career OR retirement OR broke)` |
| `cancer_L1_live` | reply | 1 | Latest | `"fuck cancer" OR "FUCK CANCER"` |
| `cancer_L1_live_dup` | reply | 1 | Top | `"fuck cancer" OR "FUCK CANCER"` |
| `cancer_L3_myth` | quote | 1 | Top | `"fuck cancer" min_faves:1000` |
| `cancer_L3_myth_dup` | quote | 1 | Latest | `"fuck cancer" min_faves:1000` |
| `cancer_ball_crossover` | reply | 1 | Latest | `cancer ("fuck it we ball" OR "we ball" OR chemo OR oncology)` |
| `cancer_ball_crossover_dup` | reply | 1 | Top | `cancer ("fuck it we ball" OR "we ball" OR chemo OR oncology)` |
| `corvidphoenix_L1` | reply | 1 | Latest | `"phoenix rising" OR "rise from the ashes" OR "from the ashes" (bird OR crow OR raven OR flock OR phoenix)` |
| `corvidphoenix_L1_dup` | reply | 1 | Top | `"phoenix rising" OR "rise from the ashes" OR "from the ashes" (bird OR crow OR raven OR flock OR phoenix)` |
| `corvidphoenix_L3_myth` | quote | 1 | Top | `"phoenix rising" OR "rise from the ashes" min_faves:50` |
| `corvidphoenix_L3_myth_dup` | quote | 1 | Latest | `"phoenix rising" OR "rise from the ashes" min_faves:50` |
| `corvidphoenix_caw` | drop | 1 | Latest | `"caw caw" OR "CAW CAW" OR corvid (fire OR ashes OR phoenix OR rebirth OR rise)` |
| `corvidphoenix_caw_dup` | drop | 1 | Top | `"caw caw" OR "CAW CAW" OR corvid (fire OR ashes OR phoenix OR rebirth OR rise)` |
| `red_october_L1` | reply | 1 | Latest | `"Red October" OR "Hunt for Red October" OR "dive dive dive"` |
| `red_october_L1_dup` | reply | 1 | Top | `"Red October" OR "Hunt for Red October" OR "dive dive dive"` |
| `red_october_L3_myth` | quote | 1 | Top | `"Hunt for Red October" min_faves:100` |
| `red_october_L3_myth_dup` | quote | 1 | Latest | `"Hunt for Red October" min_faves:100` |
| `red_october_dive` | drop | 1 | Latest | `"dive dive dive" OR "DIVE DIVE DIVE" OR "hands to dive stations" OR "deep dive"` |
| `red_october_dive_dup` | drop | 1 | Top | `"dive dive dive" OR "DIVE DIVE DIVE" OR "hands to dive stations" OR "deep dive"` |
| `red_october_sub` | engage | 1 | Latest | `Ramius OR "one ping only" OR "rig for ultra quiet" OR "Sean Connery" submarine` |
| `red_october_sub_dup` | engage | 1 | Top | `Ramius OR "one ping only" OR "rig for ultra quiet" OR "Sean Connery" submarine` |
| `reply_targets_hot` | reply | 1 | Latest | `"fuck it we ball" min_faves:5` |
| `reply_targets_hot_dup` | reply | 1 | Top | `"fuck it we ball" min_faves:5` |
| `self_brand` | monitor | 1 | Latest | `from:kaleblovingier OR from:1_OBadBjrd OR from:klovingi` |
| `self_brand_dup` | monitor | 1 | Top | `from:kaleblovingier OR from:1_OBadBjrd OR from:klovingi` |
| `yung_metro_L1` | reply | 1 | Latest | `"if young metro" OR "yung metro" OR "young metro don't" OR "metro don't trust"` |
| `yung_metro_L1_dup` | reply | 1 | Top | `"if young metro" OR "yung metro" OR "young metro don't" OR "metro don't trust"` |
| `yung_metro_L3_myth` | quote | 1 | Top | `"If Young Metro" OR "if young metro don't trust" min_faves:50` |
| `yung_metro_L3_myth_dup` | quote | 1 | Latest | `"If Young Metro" OR "if young metro don't trust" min_faves:50` |
| `yung_metro_trust` | drop | 1 | Latest | `"don't trust you" OR "dont trust you" (metro OR young OR yung) OR "ima shoot" metro` |
| `yung_metro_trust_dup` | drop | 1 | Top | `"don't trust you" OR "dont trust you" (metro OR young OR yung) OR "ima shoot" metro` |
| `aaron_swartz` | engage | 2 | Latest | `"Aaron Swartz" OR Aaronsw OR Elbakyan` |
| `aaron_swartz_dup` | engage | 2 | Top | `"Aaron Swartz" OR Aaronsw OR Elbakyan` |
| `alive_run` | drop | 2 | Latest | `"we ball" OR "still balling" OR "and it don't stop"` |
| `alive_run_dup` | drop | 2 | Top | `"we ball" OR "still balling" OR "and it don't stop"` |
| `ball_theology` | quote | 2 | Latest | `"fuck it we ball" (prayer OR mentality OR will to live)` |
| `ball_theology_dup` | quote | 2 | Top | `"fuck it we ball" (prayer OR mentality OR will to live)` |
| `cancer_L2_fighter` | engage | 2 | Latest | `cancer (survivor OR "stage 4" OR chemo OR remission OR "still fighting") min_faves:3` |
| `cancer_L2_fighter_dup` | engage | 2 | Top | `cancer (survivor OR "stage 4" OR chemo OR remission OR "still fighting") min_faves:3` |
| `corvidphoenix_flock` | engage | 2 | Latest | `flock (rebirth OR phoenix OR ashes OR rise OR "come back") OR crow (phoenix OR rebirth OR ashes)` |
| `corvidphoenix_flock_dup` | engage | 2 | Top | `flock (rebirth OR phoenix OR ashes OR rise OR "come back") OR crow (phoenix OR rebirth OR ashes)` |
| `corvidphoenix_raven` | engage | 2 | Latest | `raven (phoenix OR rebirth OR ashes OR fire OR rise) OR "black bird" (phoenix OR ashes)` |
| `corvidphoenix_raven_dup` | engage | 2 | Top | `raven (phoenix OR rebirth OR ashes OR fire OR rise) OR "black bird" (phoenix OR ashes)` |
| `red_october_L2_clancy` | quote | 2 | Latest | `"Hunt for Red October" OR "Tom Clancy" (submarine OR Ramius OR Connery)` |
| `red_october_L2_clancy_dup` | quote | 2 | Top | `"Hunt for Red October" OR "Tom Clancy" (submarine OR Ramius OR Connery)` |
| `red_october_torpedo` | reply | 2 | Latest | `torpedo (Ramius OR "Red October" OR submarine) OR "into the path of"` |
| `red_october_torpedo_dup` | reply | 2 | Top | `torpedo (Ramius OR "Red October" OR submarine) OR "into the path of"` |
| `rejection_ball` | reply | 2 | Latest | `"fuck it we ball" (rejection OR rejected OR failed OR broke)` |
| `rejection_ball_dup` | reply | 2 | Top | `"fuck it we ball" (rejection OR rejected OR failed OR broke)` |
| `scihub_freedom` | engage | 2 | Latest | `sci-hub OR scihub OR "knowledge wants to be free"` |
| `scihub_freedom_dup` | engage | 2 | Top | `sci-hub OR scihub OR "knowledge wants to be free"` |
| `valhalla` | drop | 2 | Latest | `"til valhalla" OR "til Valhalla" OR "Til Valhalla"` |
| `valhalla_dup` | drop | 2 | Top | `"til valhalla" OR "til Valhalla" OR "Til Valhalla"` |
| `yung_metro_L2_producer` | engage | 2 | Latest | `"Metro Boomin" OR @MetroBoomin OR "Future" Jumpman OR "Young Metro"` |
| `yung_metro_L2_producer_dup` | engage | 2 | Top | `"Metro Boomin" OR @MetroBoomin OR "Future" Jumpman OR "Young Metro"` |
| `yung_metro_ball` | reply | 2 | Latest | `metro (ball OR "fuck it" OR trust OR tagline OR producer) OR "if young metro" ball` |
| `yung_metro_ball_dup` | reply | 2 | Top | `metro (ball OR "fuck it" OR trust OR tagline OR producer) OR "if young metro" ball` |
| `build_public_ai` | engage | 3 | Latest | `"building in public" AI OR "built with AI" $0 OR broke` |
| `build_public_ai_dup` | engage | 3 | Top | `"building in public" AI OR "built with AI" $0 OR broke` |
| `cancer_L2_research` | quote | 3 | Latest | `"cancer treatment" OR "cancer research" OR immunotherapy OR oncology breakthrough` |
| `cancer_L2_research_dup` | quote | 3 | Top | `"cancer treatment" OR "cancer research" OR immunotherapy OR oncology breakthrough` |
| `powershell_run` | drop | 3 | Latest | `powershell OR "fuck it we ball" coding OR shipping` |
| `powershell_run_dup` | drop | 3 | Top | `powershell OR "fuck it we ball" coding OR shipping` |
| `red_october_L2_phillies` | engage | 3 | Latest | `"Red October" (Phillies OR baseball OR playoffs OR World Series)` |
| `red_october_L2_phillies_dup` | engage | 3 | Top | `"Red October" (Phillies OR baseball OR playoffs OR World Series)` |
| `zero_budget` | engage | 3 | Latest | `"no budget" OR "zero dollars" OR "broke as hell" building OR shipping` |
| `zero_budget_dup` | engage | 3 | Top | `"no budget" OR "zero dollars" OR "broke as hell" building OR shipping` |
| `addiction_fix` | engage | 4 | Latest | `"fuck addiction" OR sobriety OR relapsed recovery` |
| `addiction_fix_dup` | engage | 4 | Top | `"fuck addiction" OR sobriety OR relapsed recovery` |
| `cancer_care_sacred` | engage | 4 | Latest | `"fuck cancer" (passed OR funeral OR miss OR RIP OR aunt OR mom OR dad)` |
| `cancer_care_sacred_dup` | engage | 4 | Top | `"fuck cancer" (passed OR funeral OR miss OR RIP OR aunt OR mom OR dad)` |
| `valhalla_L2` | engage | 4 | Latest | `"til valhalla" OR "Til Valhalla" min_faves:3` |
| `valhalla_L2_dup` | engage | 4 | Top | `"til valhalla" OR "Til Valhalla" min_faves:3` |

## Protocols (+ `_dup` mirrors)

| id | protocol | role | priority | mode | query |
|----|----------|------|----------|------|-------|
| `proto_corvidphoenix` | CORVIDPHOENIX | drop | 1 | Latest | `corvid OR crow OR raven (phoenix OR rebirth OR ashes OR "from the ashes") OR "caw caw" phoenix` |
| `proto_corvidphoenix_dup` | CORVIDPHOENIX | drop | 1 | Top | `corvid OR crow OR raven (phoenix OR rebirth OR ashes OR "from the ashes") OR "caw caw" phoenix` |
| `proto_red_october` | RED_OCTOBER | engage | 1 | Latest | `"red october" OR "silent running" OR "hunt for red october" OR submarine deep` |
| `proto_red_october_dup` | RED_OCTOBER | engage | 1 | Top | `"red october" OR "silent running" OR "hunt for red october" OR submarine deep` |
| `proto_bangers_only` | BANGERS_ONLY | drop | 2 | Latest | `"bangers only" OR banger club OR "no filler" heat OR "club banger"` |
| `proto_bangers_only_dup` | BANGERS_ONLY | drop | 2 | Top | `"bangers only" OR banger club OR "no filler" heat OR "club banger"` |
| `proto_drone_corvid_conure` | DRONE_CORVID_CONURE_HYBRID | drop | 2 | Latest | `corvid OR conure OR "drone" (bird OR flock OR caw OR squawk)` |
| `proto_drone_corvid_conure_dup` | DRONE_CORVID_CONURE_HYBRID | drop | 2 | Top | `corvid OR conure OR "drone" (bird OR flock OR caw OR squawk)` |
| `proto_neverender` | NEVERENDER | drop | 2 | Latest | `neverender OR "never end" OR "and it don't stop" OR infinite loop` |
| `proto_neverender_dup` | NEVERENDER | drop | 2 | Top | `neverender OR "never end" OR "and it don't stop" OR infinite loop` |
| `proto_raptor` | RAPTOR | drop | 2 | Latest | `raptor OR "caw caw" OR "CAW CAW" bird energy OR flock` |
| `proto_raptor_dup` | RAPTOR | drop | 2 | Top | `raptor OR "caw caw" OR "CAW CAW" bird energy OR flock` |
| `proto_beak_maxxed` | BEAK_MAXXED | drop | 3 | Latest | `"beak" OR maxxed OR "maxxed out" OR "raw lyrics" club` |
| `proto_beak_maxxed_dup` | BEAK_MAXXED | drop | 3 | Top | `"beak" OR maxxed OR "maxxed out" OR "raw lyrics" club` |
| `proto_beak_mogg` | BEAK_MOGG_STREAMER | engage | 3 | Latest | `mogg OR "every streamer" OR "type shit" platforms OR allegedly streamer` |
| `proto_beak_mogg_dup` | BEAK_MOGG_STREAMER | engage | 3 | Top | `mogg OR "every streamer" OR "type shit" platforms OR allegedly streamer` |
| `proto_computah` | COMPUTAH | engage | 3 | Latest | `computah OR glitch cyber OR "beep boop" OR "digital bars" coding` |
| `proto_computah_dup` | COMPUTAH | engage | 3 | Top | `computah OR glitch cyber OR "beep boop" OR "digital bars" coding` |
| `proto_daft_punk` | DAFT_PUNK | drop | 3 | Latest | `"daft punk" OR "around the world" OR "harder better faster" OR robot` |
| `proto_daft_punk_dup` | DAFT_PUNK | drop | 3 | Top | `"daft punk" OR "around the world" OR "harder better faster" OR robot` |
| `proto_hell_on_earth` | HELL_ON_EARTH | drop | 3 | Latest | `"hell on earth" OR chaos swarm OR "we ball" apocalypse` |
| `proto_hell_on_earth_dup` | HELL_ON_EARTH | drop | 3 | Top | `"hell on earth" OR chaos swarm OR "we ball" apocalypse` |
| `proto_hug_of_death` | HUG_OF_DEATH_WITH_LOVE | engage | 3 | Latest | `"hug of death" OR "overwhelm with love" OR "positive chaos" OR "raw love"` |
| `proto_hug_of_death_dup` | HUG_OF_DEATH_WITH_LOVE | engage | 3 | Top | `"hug of death" OR "overwhelm with love" OR "positive chaos" OR "raw love"` |
| `proto_scorched_earth` | SCORCHED_EARTH | drop | 3 | Latest | `"scorched earth" OR TARS OR "burn it down" shipping OR build` |
| `proto_scorched_earth_dup` | SCORCHED_EARTH | drop | 3 | Top | `"scorched earth" OR TARS OR "burn it down" shipping OR build` |
| `proto_dracula` | DRACULA_BORDERLINE | engage | 4 | Latest | `"tame impala" OR dracula OR borderline OR "the less I know"` |
| `proto_dracula_dup` | DRACULA_BORDERLINE | engage | 4 | Top | `"tame impala" OR dracula OR borderline OR "the less I know"` |
| `proto_reincarnation` | REINCARNATION | engage | 4 | Latest | `reincarnation OR rebirth OR "come back" OR "die and come back"` |
| `proto_reincarnation_dup` | REINCARNATION | engage | 4 | Top | `reincarnation OR rebirth OR "come back" OR "die and come back"` |
| `proto_wake` | WAKE | engage | 4 | Latest | `"stop killing" OR "wake up" OR "ding dong" OR NVC nonviolent` |
| `proto_wake_dup` | WAKE | engage | 4 | Top | `"stop killing" OR "wake up" OR "ding dong" OR NVC nonviolent` |

## Ops

- Every tunnel and every protocol is **duplicated** (`_dup` flips Latest↔Top).
- Grok (this chat) runs **live X search** into each tunnel/protocol query.
- This script arms **draft queues** + optional API post.
- `draft_queue.jsonl` = ready to drop. `intel.jsonl` = observed posts.

HOOK: **FUCK IT WE FUCKING BALL** · TIL VALHALLA · ALL PROTOCOLS ARMED.
