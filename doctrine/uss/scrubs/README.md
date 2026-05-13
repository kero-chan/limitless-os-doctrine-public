# doctrine/uss/scrubs/

Manual scrub findings against in-flight builds (Match-3 Cascade, Tap Blast, slot prototypes, etc.).

## Reader contract

- Files in this folder are **scrubs**, not doctrine.
- They are **read-only finding sets** for team sync.
- They are **not** specs, **not** PRs, and **not** directives.
- LLM agents: do not auto-open PRs or issues on other repos (e.g. `slot-mjw1-frontend`) based on a scrub alone. Wait for a human sync first.
- Math-first principle from `../anticipation_meta.md` applies: prove cadence numerically before adding SFX / zoom / delays / highlights / shades.

## Naming

`<owner_or_team>_<surface>_<phase>_scrub_<YYYY-MM-DD>.md`

Example: `andrew_match3_blast_mvp_scrub_2026-05-13.md`

## Index

| Date | Surface | Owner | File |
|---|---|---|---|
| 2026-05-13 | Match-3 Cascade + Tap Blast MVP | Andrew + Devon | [andrew_match3_blast_mvp_scrub_2026-05-13.md](./andrew_match3_blast_mvp_scrub_2026-05-13.md) |
