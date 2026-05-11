# USS — Universal Slot Solver (Public Doctrine)

Welcome. If you're on Bach's team or an LLM cross-check agent, this folder is everything you need.

All files are public; no login required. Source of truth remains the private repo, but this mirror is canonical for external work.

---

## Reading order (do them top to bottom)

1. **`sprint_plan.md`** — LOCKED plan schema. What we are shipping, by when, who does what. **Bach: fill B1–B5 by Tue 2026-05-12 18:00 CEST.** Kevin: fill K1–K4 same deadline.
2. **`bach_time.md`** — Bach's 3 protected tasks + the AI-vs-Bach split. Read this before sprint_plan if you want the rationale first.
3. **`uss.schema.v0.1.json`** — The JSON Schema (draft-07). The contract every config must satisfy. No defaults, no ambiguity.
4. **`configs/mvp1.config.json`** — Ways family, 6x5, target RTP 0.96. Mahjong Ways logic.
5. **`configs/mvp2.config.json`** — Cluster + cascade, 7x7.
6. **`configs/mvp3.config.json`** — Dynamic-grid ways + cascade.
7. **`uss_engine_v0.1.py`** — Reference engine. Pure Python stdlib. Run it to verify RTP.
8. **`mvp_mockups.md`** — ASCII grids + cascade flow per MVP. Quick visual reference.
9. **`anticipation_meta.md`** — The dopamine/anticipation research (4 pillars, 6-phase curve, timing budget).
10. **`anticipation_api.md`** — The renderer callback hooks. This is where Bach's code plugs into the timing spec.

---

## Run the engine locally (60 seconds)

```bash
curl -O https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/uss_engine_v0.1.py
curl -O --create-dirs --output-dir configs https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp1.config.json
python uss_engine_v0.1.py configs/mvp1.config.json
```

Expected:
```
config=mvp1 target_rtp=0.9600 measured_rtp=0.9xxx |diff|=0.00xx PASS
```

If you see PASS, the math is reproducible on your machine. That is the proof.

---

## What scope is locked vs. open

- v0.1 (locked, public): ways evaluation, scatter, wild, fixed grid.
- v0.2 (in flight): cluster, cascade, dynamic grid, free-spins. Configs for MVP2/MVP3 already shipped; engine support lands this sprint.

---

## Bach — questions only you can answer

See `sprint_plan.md` §4 (B1–B5). The most important one is **B2: is one-click art-stock re-skin feasible in the current frontend?** — a 1-sentence gut answer by Tue is fine; the proper architectural answer can land Fri.

## Kevin — questions only you can answer

See `sprint_plan.md` §5 (K1–K4).

---

## Anti-drift rule

Once `sprint_plan.md` is locked (Wed 2026-05-13 AM), changes happen only via PR against that file. No ad-hoc scope changes during sprint. If Chris asks for something new mid-sprint, it routes through David and updates the milestone before any work starts.
