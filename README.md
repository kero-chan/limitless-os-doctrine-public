# limitless-os-doctrine-public

Public mirror of `doctrine/uss/` from `kero-chan/limitless-os`. External-access surface for LLM agents and team members. Source of truth remains the private repo.

## Purpose

This repo exists so Bach's team and LLM cross-check agents can fetch the locked USS (Universal Slot Solver) specs **without GitHub login**. Every link here is verifiable from an incognito browser.

## File index

| Artifact | Path | Raw URL |
|---|---|---|
| Schema | `doctrine/uss/uss.schema.v0.1.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/uss.schema.v0.1.json |
| MVP #1 config (ways, 6x5, locked v0.1) | `doctrine/uss/configs/mvp1.config.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp1.config.json |
| MVP #2 config (cluster cascade, 7x7, FS multiplier, draft v0.2) | `doctrine/uss/configs/mvp2.config.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp2.config.json |
| MVP #3 config (dynamic-grid ways cascade, variable cols, FS climbing multiplier, draft v0.2) | `doctrine/uss/configs/mvp3.config.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp3.config.json |

## Quick verify (no login)

```
curl -sSfL https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp1.config.json | head
```

If that prints JSON, the link is externally accessible. That is the contract for every link this repo publishes.

## Scope

- v0.1 engine supports `evaluation: "ways"` only and is proven against MVP #1 (RTP ~96%).
- `mvp2` (cluster cascade with free-spins multiplier ladder, ref: Sugar Rush) and `mvp3` (dynamic-grid ways cascade with FS climbing multiplier, ref: Mahjong Ways 2 / Megaways / Wild Swarm) are JSON-only specs targeting v0.2 of the engine.
- v0.2 engine adds: cascade loop, cluster evaluation, variable column heights (ways_count per spin), scatter-triggered free spins, persistent FS multiplier.
- The reference engine (`uss_engine_v0.1.py`) and cross-check harness live in the private repo and will be mirrored once stabilized.

## Anticipation focus (why cascade matters)

Chris's core ask is the **mechanism**, not the visual layer. The cascade + climbing-multiplier loop is what produces the anticipation curve (tension -> relief -> building hope -> peak -> climax -> re-engagement). MVP #2 and MVP #3 specs encode that curve explicitly under `anticipation_design.player_state_map`.

## Access protocol

- All artifacts referenced from external chat (Telegram, ChatGPT, Claude, Minimax) must resolve from this public mirror.
- Never share `kero-chan/limitless-os` blob URLs externally; they require login.
- Never share Hailuo `/my-work-detail/` URLs; use Share -> Copy Link.
