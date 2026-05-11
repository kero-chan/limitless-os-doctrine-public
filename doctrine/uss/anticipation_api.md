# Anticipation API — Renderer Callback Hooks (v0.1)

> Companion to `anticipation_meta.md`.
> Audience: Bach + frontend devs. This is the interface you plug into.
> Locked: 2026-05-11.

---

## Why this file exists

`anticipation_meta.md` defines *what* the timing/dopamine curve should be.
This file defines *how* the renderer plugs in. 4 callbacks, ordered by spin lifecycle.

The engine emits these events. The renderer subscribes and decides what visual/audio/haptic to play. The engine never knows about pixels; the renderer never knows about RTP. Clean seam.

---

## Lifecycle

```
spinStart → reelsLand → [evaluate] → onCascadeStart? → onNearMiss? → onResolve → onFinalHit
```

Within a single spin, the order is fixed. With cascades enabled, `onCascadeStart → onResolve` may repeat N times before `onFinalHit`.

---

## The 4 hooks

### 1. `onCascadeStart(payload)`

Fires the moment the engine has determined the current grid contains at least one win and a cascade is about to remove winning tiles.

```json
{
  "event": "onCascadeStart",
  "cascadeIndex": 0,
  "winningCells": [[col, row], ...],
  "projectedRemoval": [[col, row], ...],
  "timing_budget_ms": 420
}
```

Renderer responsibility: dim non-winning tiles, glow winning tiles, schedule the removal animation inside the timing budget.

### 2. `onNearMiss(payload)`

Fires when the grid contained k = (k_min - 1) of a paid symbol on the leftmost-anchored prefix. No payout, but the dopamine layer matters more here than on actual wins.

```json
{
  "event": "onNearMiss",
  "symbol": "H1",
  "reachedReel": 4,
  "requiredReel": 5,
  "timing_budget_ms": 600
}
```

Renderer responsibility: anticipation reel spin-out (slow the last reel), suspense audio swell, no payout banner. See `anticipation_meta.md` §3.2 for the curve.

### 3. `onResolve(payload)`

Fires after every cascade step (including the first) once payout for that step is computed.

```json
{
  "event": "onResolve",
  "cascadeIndex": 0,
  "stepPayout": 12.5,
  "runningTotal": 12.5,
  "willCascadeAgain": true,
  "timing_budget_ms": 300
}
```

Renderer responsibility: payout tick-up animation, glow ramp proportional to stepPayout. If `willCascadeAgain`, queue the next cascade without resetting the meter.

### 4. `onFinalHit(payload)`

Fires once per spin, after all cascades are resolved. This is the dopamine punctuation.

```json
{
  "event": "onFinalHit",
  "totalPayout": 47.5,
  "tier": "win|big|mega|none",
  "cascadeCount": 3,
  "timing_budget_ms": 800
}
```

Renderer responsibility: tier-appropriate celebration, audio sting, then return to idle state. **Hard rule: no celebration before this fires.** Otherwise we waste the dopamine peak on a mid-cascade step.

---

## Timing budget (must match anticipation_meta.md §4)

| Phase | Budget (ms) | Hook |
|---|---|---|
| Spin in | 600–1200 | (none, engine internal) |
| Reels land | 200 | (none) |
| Near-miss anticipation | 400–800 | onNearMiss |
| Cascade removal | 300–500 | onCascadeStart |
| Cascade resolve tick | 200–400 per step | onResolve |
| Final celebration | 600–1200 (tier-dependent) | onFinalHit |

Total worst-case spin: ~4.2s. Idle state must be reached by 4.5s.

---

## Reference implementation skeleton (frontend side)

```js
uss.on("onCascadeStart", (p) => renderer.dimNonWinners(p.winningCells, p.timing_budget_ms));
uss.on("onNearMiss",     (p) => renderer.anticipateReel(p.reachedReel, p.timing_budget_ms));
uss.on("onResolve",      (p) => renderer.tickPayout(p.stepPayout, p.runningTotal));
uss.on("onFinalHit",     (p) => renderer.celebrate(p.tier, p.totalPayout));
```

That's the contract. The engine guarantees the events fire in order with the timing budgets above. The renderer guarantees it returns to idle within budget.

---

## Bach — what we need from you

- Confirm the 4-hook surface is enough. If you need a 5th (e.g. `onScatterTrigger`), say so by Tue 18:00.
- Confirm the timing budgets are achievable in the current renderer. If not, propose what's realistic and we adjust `anticipation_meta.md` to match.
- These hooks are the ONLY surface area between engine and renderer for v0.1. No back-channels.

## Open questions for v0.2

- Free-spins entry/exit hooks (`onFreeSpinsStart`, `onFreeSpinsEnd`).
- Dynamic grid resize hooks (`onGridExpand`, `onGridContract`).
- Multi-symbol scatter wins.

These are scoped for v0.2 and will be added here, not in a new file.
