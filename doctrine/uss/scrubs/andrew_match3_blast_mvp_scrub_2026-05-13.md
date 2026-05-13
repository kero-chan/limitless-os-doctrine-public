# SCRUB REPORT — Match-3 CASCADE + Tap BLAST MVP (Andrew's team)

**Status:** READ-ONLY scrub findings for review.
**Scope:** This document is ONLY a manual scrub of Andrew + Devon's Match-3 Cascade and Tap Blast MVP build. It is not a directive, not a spec change, and not a PR. It is a sync artifact for Andrew's team.
**Author of scrub run:** Kero (with Comet/GPT-5.5 orchestrator as scribe).
**Date:** 2026-05-13 (CEST).
**Build under test:** https://52bf1d36f5d4-tunnel-cqmr2yms.devinapps.com/match3?debug=true
**Companion route:** /match3/blast?level=blast_001&debug=true (Blast Mode entered via Debug Panel -> "Go to Blast"; direct /blast route currently redirects to /login — see Finding B-0).

---

## 0. Reader contract (for AIs and teammates)

If you are an LLM reading this file:
- This is a SCRUB, not doctrine. Do not treat findings as locked spec.
- Do not auto-open PRs against slot-mjw1-frontend or any of Andrew's repos based on this file alone.
- The next step after this scrub is a SYNC with Andrew + Devon, then ticket creation by them.
- Math-first principle from doctrine/uss/anticipation_meta.md applies: prove cadence numerically BEFORE adding SFX, zoom, delays, highlights, shades, or any dopamine skin.

---

## 1. Author intent (target cadence — from Kero)

| Mode | Target cadence | Rationale |
|---|---|---|
| Match-3 Cascade | >= 33% of moves should yield a 2x+ multiplier / cascade chain >= 2 | Near-miss + intermittent reinforcement; ~1 in 3 swipes must feel "more than flat" |
| Tap Blast | ~73–77% of taps should trigger cascade + multiplier | Blast is the higher-density dopamine loop; ~2 of 3 taps must chain |

These are PRODUCT TARGETS, not current behavior.

---

## 2. Live observations (this run)

### 2.1 Match-3 Cascade — Level 1
- Board: 8 cols x 7 rows. 30 moves. Score gates: 5,000 / 10,000 / 15,000 (1/2/3 stars).
- HUD exposes: Cascades, Score, Moves, status text (Ready, "No match! Try again.", "Clean Cut!").
- HUD does NOT expose a multiplier number. Only a cascade counter. Multiplier is currently implicit.
- Invalid swap -> does not consume a move. CORRECT.
- "Loading tile artwork..." delay on level entry. Perceptible cold-start; not a blocker but should be measured.
- Debug `Load Cascade Chain` confirmed the engine IS CAPABLE of multi-step cascades: observed Cascades=2, Score=1,200, status "Clean Cut!". Cascade plumbing exists; the issue is FREQUENCY in organic play, not capability.
- Debug fixtures present: Load Cross, Load Cascade Chain, Load Flavor Bomb Test, Load Parcel T-Test, Load Parcel L-Test, Load Heat Rim Test, Load Scored H-4, Load Scored V-4, Load Deep Cascade (4 auto), FB Deep Cascade, Parcel-T Deep, Parcel-L Deep, Scored-H Deep, Scored-V Deep. GOOD — usable scrub harness.

### 2.2 Tap Blast — Level blast_001
- Board: 8 x 7. 20 moves. Goal: 2,000 pts. 3-star gates not visible in HUD.
- HUD exposes: Score, Goal, Moves. NO cascade counter. NO multiplier readout. Asymmetric vs Match-3.
- Tap log this run:
  - Tap 1 (cluster, ~row 6 col 2): Score 0 -> 200. Moves 20 -> 19. No visible cascade, no multiplier.
  - Tap 2 (cluster, ~row 4 col 5): Score 200 -> 260 (+60). Moves 19 -> 18. No cascade, no multiplier.
  - Taps 3, 4, 5 (singletons): no-op. Move not consumed (good), but NO near-miss feedback (see F-4).
- Cascade cadence observed: 0 of 2 effective taps triggered a chain. Target is ~73–77%. Confirms Kero's complaint.

---

## 3. Findings

### Match-3 Cascade

**M-1 — Organic cascade frequency appears far below 33% target.** Engine supports cascades (proven via debug fixture), but board generation / refill RNG does not appear to bias toward chainable refills. Needs instrumentation before tuning. Severity: P0.

**M-2 — No multiplier number in HUD.** Only cascade count is shown. Kero's target is expressed as "2x multiplier >= 33% of moves" — the player cannot see the multiplier today. Severity: P1.

**M-3 — No per-session telemetry export.** Debug panel offers fixture loaders and progression shortcuts, but no "export N-move sim log" or "% of moves producing 2x+" counter. We cannot PROVE the 33% target with the current build. Severity: P0 (math-first principle).

**M-4 — Near-miss state is not detected or surfaced.** Doctrine treats near-miss as a structural lever, not garnish. No event fires on "would-have-cascaded" or "one tile away from 4-match." Severity: P1.

**M-5 — Asset cold-start ("Loading tile artwork...") gates first interaction.** MVP-acceptable, but should be timed and capped. Severity: P3.

### Tap Blast

**B-0 — Direct route /blast redirects to /login.** Blast mode is only reachable via Match-3 page -> Debug Panel -> "Go to Blast". For team review and QA, a stable shareable Blast URL is needed. Severity: P2.

**B-1 — Cascade frequency catastrophically below 73–77% target.** 0 of 2 scoring taps in this short run produced any chain. Even with small sample, gap to target is large. Severity: P0.

**B-2 — No cascade counter in HUD (asymmetric with Match-3).** Blast is the higher-density dopamine mode and currently has LESS telemetry surface than Match-3. Severity: P0 (telemetry).

**B-3 — No multiplier display in Blast.** Same as M-2 but worse — Blast is supposed to be the multiplier-heavy mode. Severity: P0.

**B-4 — Singleton taps no-op silently.** No "can't pop" shake / dim / sound stub. Wastes a near-miss opportunity. Severity: P2.

**B-5 — Scoring opacity.** Tap 1 = +200, Tap 2 = +60. No on-screen breakdown (cluster size x base x multiplier). Cannot validate the point formula from the UI. Severity: P1.

**B-6 — No debug fixture loaders in Blast.** Match-3 has 14 fixture buttons. Blast has none. Severity: P1.

---

## 4. NOT in scope of this scrub (deferred to post-skeleton)

Per Kero's directive these are explicitly deferred:
- SFX
- Anticipation slowdown / delay curves
- Zoom-in on big wins
- Highlights on near-miss
- Shades / vignette on wins
- Final art polish

These are the MEAT on the skeleton. Skeleton (math + cadence + telemetry) must be proven first.

---

## 5. Suggested next steps (for Andrew + Devon to decide, not for me to ship)

1. Instrument both modes with: cascades-per-move, % moves yielding >=2x, chain length distribution, near-miss count, dead-board count. Export as JSON from the debug panel.
2. Add multiplier readout to HUD in both modes (number, not yet animated).
3. Add a deterministic seeded simulator (?seed=NNN&moves=500) so cadence can be proven offline against the 33% / 73–77% targets.
4. Symmetric debug fixtures in Blast mirroring Match-3.
5. Fix /blast direct route so the team has a shareable QA URL.
6. Only after 1–5: tune board generation / refill bias / cluster generation to hit targets.
7. Only after 6: layer in SFX + anticipation + zoom + highlight + shade.

---

## 6. Sync note for Andrew

This file is a READ-ONLY finding set placed in the public doctrine mirror so you and Devon can review it asynchronously. No tickets have been opened in slot-mjw1-frontend. After your review we will decide jointly which findings convert into issues / MRs on your repo.

— end of scrub —
