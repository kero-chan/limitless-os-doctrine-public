# MVP Grid Mockups — visual reference for Bach's team

Goal: show the three MVP grid layouts so the frontend team can **edit the existing slot-chinese/slot-french/slot-mexican panel rather than rebuild**. The dark-panel + gold-accent frame stays; only the reel area changes per MVP.

Visual framework (already shipped in the current slot demos):
- Dark navy/black panel with rounded corners, subtle gold rim glow
- Gold "SCATTER" / title bar at top
- Yellow/gold progress meter under the reels
- Player meter % + "READY TO PLAY!" label
- Soft pagination dots, ambient gold particles

What changes between MVPs is **only the reel grid inside the panel**.

---

## MVP #1 — Ways, 6 cols × 5 rows fixed (30 tiles)

```
+---------------------------- SLOT PANEL -----------------------------+
|                            < TITLE BAR >                            |
|  +-------------------------------------------------------------+    |
|  |  [H1] [H2] [L1] [L2] [H3] [L3]   <- row 5                  |    |
|  |  [L2] [H1] [H2] [L1] [H3] [WLD]  <- row 4                  |    |
|  |  [H3] [L1] [L2] [SCT] [H1] [H2]  <- row 3                  |    |
|  |  [L2] [H1] [L3] [L1] [H2] [H1]   <- row 2                  |    |
|  |  [H1] [WLD] [H2] [H1] [L1] [L2]  <- row 1                  |    |
|  +-------------------------------------------------------------+    |
|     col1   col2   col3   col4   col5   col6                         |
|                                                                     |
|  ===== meter =================================== 96%  READY ====    |
+---------------------------------------------------------------------+
```

- Tile pixel target on 1080×1920 portrait: ~150×150 px
- Grid block size: ~900×750 px (≈ 47% of screen)
- Tiles uniform, never change size or count
- Reel-stop delay 600–900 ms on near-miss = Phase-1 dopamine spike

## MVP #2 — Cluster cascade, 7 cols × 7 rows fixed (49 tiles)

```
+---------------------------- SLOT PANEL -----------------------------+
|                            < TITLE BAR >                            |
|  +-----------------------------------------------------------+      |
|  | [H1][H2][L1][L2][H3][L3][L1]                              |      |
|  | [L2][H1][H2][L1][H3][WLD][H2]                             |      |
|  | [H3][L1][L2][SCT][H1][H2][L3]                             |      |
|  | [L2][H1][L3][L1][H2][H1][L2]      <- cluster of 5 here    |      |
|  | [H1][WLD][H2][H1][L1][L2][H3]         (highlighted gold)   |      |
|  | [L1][H1][H2][H1][L2][H2][L1]                              |      |
|  | [H2][L3][H1][L1][L2][H3][WLD]                             |      |
|  +-----------------------------------------------------------+      |
|     [ x1 ] -> [ x2 ] -> [ x4 ] -> [ x8 ] -> [ x16 ]  multiplier     |
|  ===== meter =================================== 96%  READY ====    |
+---------------------------------------------------------------------+
```

- Tile pixel target: ~128×128 px
- Grid block size: ~900×900 px square (≈ 50–55% of screen)
- Multiplier badge above meter, climbs per cascade
- Cluster explosion 250–350 ms + tile drop 300–450 ms = chained Pillar-D micro-rewards

## MVP #3 — Dynamic-grid ways cascade, 6 cols × 2–7 rows variable

Two example spins to show the variable-height tease:

**Spin A — low ways (192 ways, "small build" feel):**
```
+---------------------------- SLOT PANEL -----------------------------+
|                            < TITLE BAR >                            |
|  +-------------------------------------------------------------+    |
|  |                              [H1]                            |   |
|  |              [L2] [H1]       [WLD]                           |   |
|  | [H2]        [L1] [H2]  [L3]  [H1]                            |   |
|  | [H1] [L1]   [H3] [L1]  [H2]  [L2]                            |   |
|  | [L2] [H2]   [L2] [H3]  [H1]  [H2]                            |   |
|  +-------------------------------------------------------------+    |
|    col1  col2  col3  col4  col5  col6                                |
|                                                                     |
|    192 WAYS  <- ways count badge                                     |
+---------------------------------------------------------------------+
```

**Spin B — max ways (117,649 ways, "TALL REELS" climax tease):**
```
+---------------------------- SLOT PANEL -----------------------------+
|                            < TITLE BAR >                            |
|  +-------------------------------------------------------------+    |
|  | [H1] [H2] [L1] [L2] [H3] [L3]                                |   |
|  | [L2] [H1] [H2] [L1] [H3] [WLD]                               |   |
|  | [H3] [L1] [L2] [SCT][H1] [H2]                                |   |
|  | [L2] [H1] [L3] [L1] [H2] [H1]                                |   |
|  | [H1] [WLD][H2] [H1] [L1] [L2]                                |   |
|  | [H2] [L3] [H1] [L1] [L2] [H3]                                |   |
|  | [L1] [H1] [H2] [H1] [L2] [H2]                                |   |
|  +-------------------------------------------------------------+    |
|    col1  col2  col3  col4  col5  col6                                |
|                                                                     |
|    117,649 WAYS  <- glows gold, audio sting before drop              |
|    [ x2 ] -> [ x3 ] -> [ x5 ] -> [ x10 ]  FS climbing multiplier     |
+---------------------------------------------------------------------+
```

- Tile pixel target: ~128×128 px constant; column heights animate up/down
- Grid block flexes: ~400×900 px (low) → ~900×900 px (max)
- Column-height tease BEFORE drop = strongest Phase-1 dopamine cue we have
- FS multiplier 2x→3x→5x→10x **never resets** within FS session

---

## Renderer timing budget (must hit for the math to FEEL right)

| Beat | Target ms | MVP |
|---|---|---|
| Reel spin base | 1800–2200 | all |
| Last-reel near-miss hold | +600–900 | #1 #3 |
| Column-height tease animation | 400–700 | #3 only |
| Cluster explosion | 250–350 | #2 |
| Tile drop after cascade | 300–450 | #2 #3 |
| Multiplier badge punch + sting | 150–250 | #2 #3 |
| FS transition | 1500–2000 | all |
| Big-win celebration | 2500–4000 | all |
| Turbo / quick-spin total | 400–600 | all |

See `anticipation_meta.md` for the dopamine research behind these numbers.

---

## What Bach's team actually does (handoff in one paragraph)

Keep the dark-panel + gold-accent frame from `slot-chinese-dev.kero.io/trial`. Replace the current reel block with one of three layouts above. Tile artwork comes from the asset pipeline (`slot-assets-pipeline.kero.io`), keyed to the symbol contract `H1/H2/H3/L1–L4/WILD/SCAT`. Honor the timing budget. Math comes from `configs/mvpN.config.json`. Same skin can be mounted on any of the three configs — that is the one-click reskin promise.
