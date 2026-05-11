# limitless-os-doctrine-public

Public mirror of `doctrine/uss/` from `kero-chan/limitless-os`. External-access surface for LLM agents and team members. Source of truth remains the private repo.

## Purpose

This repo exists so Bach's team and LLM cross-check agents can fetch the locked USS (Universal Slot Solver) v0.1 specs **without GitHub login**. Every link here is verifiable from an incognito browser.

## File index (USS v0.1)

| Artifact | Path | Raw URL |
|---|---|---|
| Schema | `doctrine/uss/uss.schema.v0.1.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/uss.schema.v0.1.json |
| MVP #1 config (ways, locked) | `doctrine/uss/configs/mvp1.config.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp1.config.json |
| MVP #2 config (cluster, 7x8, draft) | `doctrine/uss/configs/mvp2.config.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp2.config.json |
| MVP #3 config (cascade+scatter, draft) | `doctrine/uss/configs/mvp3.config.json` | https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp3.config.json |

## Quick verify (no login)

```
curl -sSfL https://raw.githubusercontent.com/kero-chan/limitless-os-doctrine-public/main/doctrine/uss/configs/mvp1.config.json | head
```

If that prints JSON, the link is externally accessible. That is the contract for every link this repo publishes.

## Scope

- v0.1 engine supports `evaluation: "ways"` only.
- `mvp2` (cluster) and `mvp3` (cascade + scatter) are JSON-only specs targeting v0.2 of the engine.
- The reference engine (`uss_engine_v0.1.py`) and cross-check harness live in the private repo and will be mirrored once stabilized.

## Access protocol

- All artifacts referenced from external chat (Telegram, ChatGPT, Claude, Minimax) must resolve from this public mirror.
- Never share `kero-chan/limitless-os` blob URLs externally; they require login.
- Never share Hailuo `/my-work-detail/` URLs; use Share -> Copy Link.
