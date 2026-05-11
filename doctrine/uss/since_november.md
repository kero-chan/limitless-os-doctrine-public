# Since November — What the team has actually built

**Audience:** Chris
**Owner:** dFun
**Status:** Living evidence log
**Repo (private, source of truth):** github.com/kero-chan/slot-mjw1-frontend (Issues: 39 open, 245 closed)
**Public doctrine mirror:** github.com/kero-chan/limitless-os-doctrine-public/tree/main/doctrine/uss

This doc answers one question only: *what work, with which GitHub issues, proves we are building a mechanism and not just tuning visuals?*

---

## 1. The thesis we've been executing

1. Cosmetic revamp alone does not move retention — cascade rhythm, anticipation, and dopamine pacing do.
2. A single hand-tuned game does not scale — we need a Universal Slot Solver (USS) so grid size / RTP / cascade ratios / multipliers / scatters become **config**, not code.
3. The art pipeline must accept a style-swap contract so one mechanic ships as N skins (food, French, Mexican, Chinese, photoreal).

Every issue below maps to one of these three.

---

## 2. Phase 1 — Foundations (Jan)

Frontend bring-up, local assets, layout, bet controls, input text.

- #4 Local assets instead of server served (Jan 15)
- #5 Actions/animations sound + duration list (Jan 15)
- #7 Long-click on bet buttons (Jan 21)
- #9 WINS/BET input text (Jan 21)
- #10 PC layout (Jan 21)
- #14 App behavior update (Jan 22)

---

## 3. Phase 2 — FX Revamp / cascade anticipation engine (Mar)

This is the block Chris keeps asking about. It is **not cosmetic polish** — it is the cascade + anticipation timing layer.

P0-critical:
- #25 Near-miss hesitation system on final cascade columns
- #26 Cascade chain audio escalation (pitch + layers + volume)
- #27 Win tier audio differentiation (eyes-closed distinguishable)
- #28 Big-win anticipation build sequence before banners

P1 cascade rhythm:
- #29 Post-win evaluation pauses ("the breath")
- #30 Win counter tick-up animation per tier
- #31 Cascade intensity escalation (particles, glow, shake per depth)
- #32 Sound–visual sync < 16 ms
- #33 Pop-burst before tumble
- #34 New-symbol drop physics (bounce + compression)
- #35 Win-tier banner differentiation
- #36 Animated border trace + staggered pulse
- #43 Cascade cycle time tuning (1.4–1.8s normal / 0.7–1.0s turbo)
- #47 Cascade audio escalation spec (pitch/speed/volume/layers per depth)
- #61 Cascade audio tension layers

This is where "dopamine" stops being a buzzword and becomes timing budgets in milliseconds.

---

## 4. Phase 3 — Dopamine + RTP + Asset DNA (Mar)

The documents Chris asked whether we had:
- **#64 — Dopamine Reward Psychology Research Brief — Cascade Timing & LDW Specs**
- **#52 — Final delivery checklist (rollback, mobile, RTP, production)**
- **#65 — MJW1 Art DNA Style Guide — Visual Coherence & Asset Pipeline Specs**
- **#171 — Enforce 5-color DNA palette across all visual elements** (Asset Pipeline label)
- **#172 — SHATTER explosion + win celebration tiers + multiplier popup (Score 1→10)**

---

## 5. Phase 4 — Mechanic exploration (Match-3 hybrid, Apr)

Proof we are exploring mechanic space, not copying one game:

- #175 [NEW MODE] Match-3 — Hybrid CCS + Royal Match MVP
- #176 Core swipe-to-swap + 3-in-a-row pattern detection
- #177 Special piece creation — striped / wrapped / color bomb / rim-glow
- #178 Special piece combo matrix — all piece interaction rules
- #179 Game loop + level system + move counter + objectives (Jelly / Ingredients / Orders)

---

## 6. Phase 5 — Pipeline + Style-Swap (current week)

This is the layer that addresses Chris directly: **mechanism + multi-game pipeline.**

- **#360 [EPIC] Photorealistic Revamp — 3-Style Art-Bible Swap + Duck Hunters Anticipation**
- **#361 [P0 SPEC] Art Bible Schema v1 — generalization contract for style-swap pipeline**
- #362 [P0 SPEC] Art Bible — Arcade v1
- #363 [P0 SPEC] Art Bible — Minimax-Clean v1
- #364 [P0 SPEC] Art Bible — Photoreal-Hailuo v1
- **#365 [P0 ANIM] Duck Hunters Anticipation Beat-Capture v1**
- **#366 Orchestration Loop — 3 Clean Cycles (Bach lane)**
- **#368 [BLOCKER] Dynamic Grid Mechanism — pipeline spike**

---
## 7. Public doctrine artifacts (no login required)

These are mirrored so Bach's team and Chris can read without GitHub access:

- `doctrine/uss/README.md` — entry point
- `doctrine/uss/uss.schema.v0.1.json` — Universal Slot Solver schema
- `doctrine/uss/configs/mvp1.config.json` — ways-only baseline
- `doctrine/uss/configs/mvp2.config.json` — cluster + cascade
- `doctrine/uss/configs/mvp3.config.json` — dynamic-grid ways cascade
- `doctrine/uss/anticipation_meta.md` — dopamine / near-miss timing
- `doctrine/uss/anticipation_api.md` — engine ↔ renderer event contract
- `doctrine/uss/mvp_mockups.md` — MVP layouts
- `doctrine/uss/uss_engine_v0.1.py` — runnable reference engine
- `doctrine/uss/sprint_plan.md` — sprint plan
- `doctrine/uss/bach_time.md` — Bach lane one-pager

---

## 8. How to read this in 60 seconds

- **Mechanism work:** §3, §4, §6 (cascade engine, Match-3 hybrid, dynamic grid, art-bible schema)
- **Math / RTP / dopamine:** §4 (issues #52, #64)
- **Pipeline / multi-game:** §6 (issues #360, #361, #368)
- **Public proof for non-repo readers:** §7

If any line above is unclear, the GitHub issue number is the ground truth — open it and the timing budgets, specs, and acceptance criteria are there.
