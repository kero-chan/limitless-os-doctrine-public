# Slot Product Complete Handover -- AI Operator Knowledge Base

_For Chris's AI orchestrator. Ingest this doc to reach full context on every slot mechanic, task category, insight, and artifact produced by David's team (Nov 2025 -- May 2026)._

_Last updated: 2026-05-12_

---

## 1. PROJECT TIMELINE

| Phase | Dates | What happened |
|-------|-------|---------------|
| Discovery | Nov 2025 | David created the Universal Scrubber for Mahjong Ways 1 (MJW1). First teardown of cascade/slot mechanics. |
| Mockup | Nov--Dec 2025 | MJW1 mockups produced. Kung-fu theme variant. Multiple jam versions explored. |
| Element Slot | Dec 2025--Jan 2026 | Element-themed slot prototype built as mechanic testbed. |
| FoodSlot Kickoff | Jan 15 2026 | First GitHub issue (#4). Bach starts slot-mjw1-frontend repo. 6-skin cuisine theming (Chinese, French, Mexican, Japanese, Italian, Korean). |
| Core Build | Jan--Feb 2026 | Grid engine, cascade mechanics, multiplier ladder, bet system, autoplay, paytable, basic SFX. ~20 issues closed. |
| FX Revamp Sprint | Mar 2026 | 25+ issues. Near-miss hesitation, cascade escalation VFX, sound-visual sync (<16ms), shatter explosions, win tiers, dopamine timing. |
| Scrub Cycle | Mar 29--Apr 2 | Scrubs #1--#8. Tile edge bleeding, FX overload fix, button icons, idle animation, multiplier fit, turbo mode dopamine, history sync. |
| Asset Pipeline | Mar 30 | #198: Map 173 pipeline assets to live game displays. #200: Asset prompt upgrade for 20-theme scalability. |
| Match-3 Mode | Apr 8--10 | 11 issues (#175--#185). Full CCS+Royal Match hybrid: swipe-to-swap, 3-in-a-row detection, special pieces (striped/wrapped/color bomb), combo matrix, level system, RTP controller, blitz mode, dopamine reward architecture, pipeline integration. |
| 6-Skin Rollout | Apr 2026 | #303--#323: All 6 skins receive cascade timing config, sticky multiplier, multiplier merge, scatter anticipation, biome progression, extra-spin pricing. |
| Horizontal UI | Apr--May 2026 | #355: Horizontal layout for multi-mode landing surface. Chinese + French live builds deployed. |
| Orchestration OS | May 9 | Boot v2 cutover. Comet AI orchestrator installed. Daily Orchestration Loop (DOL v1). Baseline score 62/100, target 81/100. |
| USS Doctrine | May 10--11 | 9 public doctrine artifacts published: schema, engine, configs, sprint plan, anticipation research. |
| Scope Lock | May 10 | 37 open / 246 closed issues. 2 milestones. Backlog re-anchored to Chris Resolution Sprint. |

---

## 2. NUMBERS AT A GLANCE

- **Total GitHub issues lifetime:** 284 (246 closed + 38 open)
- **Issues closed per week (avg):** ~14.5 over 17 weeks
- **Live playable builds:** 3 (Chinese, French, Mexican) + Asset Pipeline Dashboard
- **Themed skins:** 6 (Chinese, French, Mexican, Japanese, Italian, Korean)
- **Game modes built:** Cascade Slot + Match-3/Tap-Blast hybrid
- **Grid sizes tested:** 5x4 and 5x5 (dynamic grid mechanism designed but not yet shipped)
- **Doctrine artifacts (public):** 9 files incl. reference RTP engine (Python) + JSON schema
- **Quality baseline:** 62/100 at Boot v2 cutover (May 9)

---

## 3. TASK CATEGORIES -- WHAT WAS SOLVED AND HOW

Every closed issue falls into one of these categories. Each entry describes the mechanic so Chris's AI can reuse the pattern.

### 3A. CASCADE ENGINE (issues #21--#31, #166--#172, #307, #318)
What it is: Vertical tile-drop system. Tiles match, dissolve, remaining tiles fall, new tiles fill from top, repeat. Each cascade step can trigger new matches.
Mechanics solved:
- Cascade intensity escalation: particles increase, glow brightens, shake intensifies per cascade depth
- Post-win evaluation pauses ("the breath"): 200--400ms silence between cascade resolve and next drop for dopamine buildup
- Near-miss hesitation on final columns: last 1--2 reels slow down, creating anticipation before resolve/fail
- Sound-visual sync precision: all hit FX fire within 16ms of audio cue
- Sequential reel stops with bounce: reels stop left-to-right with 80ms stagger + 2-frame overshoot bounce
- Pre-freeze frame: 150ms hold before cascade resolves, player sees the board state
- Cascade tempo config per skin: timing values (drop speed, dissolve duration, pause length) stored in JSON config per theme

### 3B. MULTIPLIER SYSTEM (#30, #168, #319, #320)
What it is: Escalating reward multiplier tied to cascade depth.
Mechanics solved:
- 4-state multiplier ladder: x1 -> x2 -> x4 -> x8 (normal), x2 -> x4 -> x8 -> x10 (bonus)
- Sticky multiplier per cell: spoon icon marks cells, multiplier persists across cascades until board clears
- Multiplier merge: adjacent sticky multipliers combine values
- Color lifecycle: multiplier cell changes color at each tier (grey -> blue -> purple -> gold)
- Buy Bonus with dynamic pricing: bet multiplier x25/x50/x100 for instant bonus-round entry

### 3C. ANIMATION AND VFX (#25, #29, #33--#36, #172, #303--#306)
Mechanics solved:
- Symbol removal pop-burst before tumble animation
- New symbol drop physics: bounce + compression on landing
- Animated border trace + staggered pulse on win highlights
- Win tier banner differentiation: Small/Medium/Big/Mega with escalating animation intensity
- Scatter smoke columns replacing generic lightning
- Tile hit opacity flash + chrome frame polish
- Top-row peek reveal: 10% of incoming tile visible above grid before drop
- HUD repositioned to clear chef head-space (character art integration)

### 3D. AUDIO AND SFX (#5, #32, #170, #199, #203, #299, #321)
Mechanics solved:
- Sound sandbox / lab mode: force-trigger testing environment for 100+ sounds
- 3-tier win sound system: small/medium/big mapped to payout thresholds
- Cascade escalation audio: pitch and intensity increase per cascade depth
- Audio ducking on scatter anticipation: ambient drops 60% when scatter symbol appears
- Ambient mix rebalance: background reduced to let cascade SFX dominate
- Mouth-talk removal: chef animations stripped of lip-sync when no audio plays

### 3E. SKIN AND THEME SYSTEM (#303--#323)
What it is: Same mechanic, different visual/audio wrapper. 6 cuisine themes share one engine.
Mechanics solved:
- Per-skin config files: each skin defines tile assets, background, chef character, color palette, SFX set
- Biome progression renderer: 3-tier background dimming system (dawn -> day -> dusk) tied to cascade depth
- Scatter anticipation per skin: reel slowdown timing + audio ducking tuned per theme's rhythm
- "One More Course?" dynamic extra-spin pricing: per-skin pricing UI with culturally appropriate imagery
- All 6 skins receive identical mechanic upgrades in batch (cascade timing, multiplier, scatter, biome, pricing)

### 3F. ASSET PIPELINE (#186, #198, #200)
What it is: AI-generated visual assets mapped to live game displays.
Mechanics solved:
- 173 pipeline assets mapped to live game displays (#198)
- Slot frame generation via pipeline: AI replaces hand-drawn frames (#186)
- Asset prompt upgrade spec: 5 asset categories (tiles, backgrounds, characters, UI, effects) structured for 20-theme scalability (#200)
- Pipeline dashboard live at slot-assets-pipeline.kero.io

### 3G. UI AND UX POLISH (#7, #9, #10, #166--#169, #194--#196, #314, #355)
Mechanics solved:
- Bet range expansion: 2--500 with 15+ increments
- Autoplay stop-rules + pre-start summary (Duck Hunters benchmark)
- Secondary page unification: Paytable/HowToPlay/History/Settings all themed to match game
- 9-area UX/UI overhaul to NoLimit-tier standard (#314)
- Tile edge bleeding fixes, button icon polish, idle animation
- Grid fit corrections for PC vs mobile viewports
- Horizontal layout for multi-mode landing surface (#355)

### 3H. GAME MODES (#175--#185, #315, #328--#339)
Match-3 / Tap-Blast mode (separate game mode sharing same asset pipeline):
- Core swipe-to-swap + 3-in-a-row pattern detection (#176)
- Special piece creation: striped, wrapped, color bomb + rim-glow (#177)
- Special piece combo matrix: all interaction rules (#178)
- Game loop + level system + move counter + objectives (jelly/ingredients/orders) (#179)
- Level design schema + 10 starter levels in JSON (#180)
- RTP controller + tile weight system + 3 play modes (Slot/PvP/F2P) (#181)
- Blitz mode: 3+ scatter trigger + boosted cascade bonus round (#182)
- Dopamine reward architecture: cascade praise + near-miss + variable ratio scheduling (#183)
- Pipeline integration: slot-to-puzzle asset conversion + reskin support (#184)
- Tap-Blast engine: cluster detection + tap-to-pop (#337)
- Scoring engine with dopamine calibration (#338)
- Level selector (Candy Crush style) + 10 levels + persistence (#328, #329, #330, #339)
- Chef's Gala Bonus Mode: 3-tier bonus system benchmarked against Duck Hunters (#315)

### 3I. SCRUB CYCLES (#166--#172, #194--#198)
8 numbered scrub passes (Scrub #1 through #8), each a batch of 5--15 fixes:
- Scrub #7: FX overload fix, button icons, idle animation, layout + multiplier fit
- Scrub #8: Turbo mode dopamine timing, tile edge bleeding, UI button audit, history sync
- All scrubs targeted a measurable quality score improvement

### 3J. ORCHESTRATION AND DOCTRINE (May 9--12)
- Comet Boot Protocol v2: AI orchestration law stack, daily loop, CI gates
- USS (Universal Slot Solver) schema v0.1: JSON contract for slot configs
- Reference RTP engine v0.1: pure Python stdlib, verifies payout math
- 3 MVP configs: Ways 6x5 RTP 0.96, Cluster+Cascade 7x7, Dynamic-Grid
- Anticipation meta-research: dopamine/near-miss/VR-schedule, 4 pillars, 6-phase curve
- Anticipation API: renderer callback hooks for Bach's code
- Sprint plan + Bach time-split document

---

## 4. LIVE ARTIFACTS -- LINKS FOR CHRIS'S AI

### Playable Builds
- Chinese slot (5x5, dev): https://slot-chinese-dev.kero.io/trial
- French slot: https://slot-french.kero.io/trial
- Mexican slot: https://slot-mexican.kero.io/trial
- Asset Pipeline Dashboard: https://slot-assets-pipeline.kero.io

### GitHub
- Main repo (slot-mjw1-frontend): https://github.com/kero-chan/slot-mjw1-frontend
- All 246 closed issues (full task history): https://github.com/kero-chan/slot-mjw1-frontend/issues?q=is%3Aissue+is%3Aclosed
- All 38 open issues (current backlog): https://github.com/kero-chan/slot-mjw1-frontend/issues
- Chris Resolution Sprint (milestone 1): https://github.com/kero-chan/slot-mjw1-frontend/milestone/1
- Parked Photoreal Sprint (milestone 2): https://github.com/kero-chan/slot-mjw1-frontend/milestone/2
- Epic anchor #341 (pipeline spine): https://github.com/kero-chan/slot-mjw1-frontend/issues/341

### Public Doctrine (USS)
- Full directory: https://github.com/kero-chan/limitless-os-doctrine-public/tree/main/doctrine/uss
- USS Schema v0.1 (JSON): https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/uss.schema.v0.1.json
- Reference RTP Engine (Python): https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/uss_engine_v0.1.py
- MVP Configs: https://github.com/kero-chan/limitless-os-doctrine-public/tree/main/doctrine/uss/configs
- Anticipation Meta (dopamine research): https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/anticipation_meta.md
- Anticipation API (renderer hooks): https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/anticipation_api.md
- Sprint Plan: https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/sprint_plan.md
- Bach Time Split: https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/bach_time.md
- MVP Mockups (ASCII grids): https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/mvp_mockups.md
- Bach Handover: https://github.com/kero-chan/limitless-os-doctrine-public/blob/main/doctrine/uss/bach_handover.md

### Google Docs (Source of Truth)
- Master Dashboard: https://docs.google.com/spreadsheets/d/1suJZIslpT9Ph39ZjIsN-l8ci7jIPBhbXEDBb9libSfc
- Knowledge Bank (quantified research): https://docs.google.com/document/d/1KTE_E0bIRN_nuIg6yxLaaiV9d2aAftt4td5orvHXYUg
- FoodSlot Iteration Log: https://docs.google.com/document/d/1j6DRtRa0AhKOCHAzACnFh50eqwDPsP104I1uHA4MWGc
- Master Asset and Task Overview: https://docs.google.com/document/d/1BlHS3LemouMQ8IPaBzXo_g1DKEhDbWMrRSA_nxprBdo
- Comet Boot Protocol v2: https://docs.google.com/document/d/1CZ0bWXyrPMLpcUx3HvYM12zHqp5IPAMg7vEwwvEOAmk

---

## 5. WHAT IS NOT YET DONE (OPEN GAPS)

- **Dynamic grid mechanism (#368):** 1 mechanic -> N grid sizes. Designed, not shipped. This is the single blocker Bach identified.
- **Multi-game unified landing surface:** Horizontal layout built (#355) but Chris wants vertical for mobile URL-bar clearance. Needs rebuild.
- **Photoreal art layer:** Hailuo DNA spec written (#359), asset generation wired (#358), but full photoreal skin not live.
- **Anticipation timing in live build:** Research done (anticipation_meta.md), API defined (anticipation_api.md), not yet integrated into cascade engine.
- **Product launch / market test:** Zero revenue. No public release. No RTP certification.

---

## 6. WHAT CHRIS'S AI CAN REUSE IMMEDIATELY

1. **Cascade engine config pattern:** JSON configs per skin define all timing values. Clone a config, change the values, get a new feel.
2. **6-skin architecture:** Add a 7th skin by duplicating a config + swapping assets in the pipeline. The engine doesn't change.
3. **RTP engine (Python):** Verify any payout table offline before wiring it into the frontend.
4. **USS schema:** Machine-readable contract. Any AI agent can validate a slot config against it.
5. **Anticipation research:** 4 pillars, 6-phase dopamine curve, timing budget. Use as constraints for any new slot mechanic.
6. **Match-3 mode code:** Full game loop, level system, special pieces, combo matrix. Can be forked for puzzle-slot hybrids.
7. **Asset pipeline:** Feed a theme name, get tile assets, backgrounds, characters, UI kit. Scales to 20+ themes.
8. **173 mapped assets:** Already wired. No re-mapping needed for existing skins.
9. **Scrub methodology:** 8 numbered passes with defined scope. Reproducible quality-improvement pattern.
10. **Master Dashboard:** One-page view of all agents, atoms, statuses, and gates. Replicate the orchestration model.

---

## 7. NOTE ON HORIZONTAL VS VERTICAL

The horizontal layout (#355) was built to serve as a multi-mode landing surface (slot + match-3 + future modes on one screen) and to maintain desktop/mobile parity. Chris has requested revert to vertical for mobile due to URL-bar occlusion on older phones. The vertical revert is a UI task, not an engine task -- the cascade engine, multiplier system, and all mechanics are orientation-agnostic. The config-driven skin system means layout is a parameter, not a rebuild.

---

_End of handover. This document plus the linked artifacts constitute the complete knowledge transfer for the slot product as of May 12, 2026._
