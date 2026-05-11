# Limitless Slot Team — Sprint Plan (LOCKED SCHEMA)

> Locked: 2026-05-11 12:00 CEST, Amsterdam.
> Owner of this doc: David. Bach + Kevin fill in their fields by **Tue 2026-05-12 18:00 CEST**.
> If a field is empty by cutoff, David locks the plan with the last known value and Bach/Kevin patch via PR.

---

## 0. North-Star Mission

Ship a Mahjong-Ways-class MVP in **~2 months** powered by USS, with one-click re-skin into 3 art stocks. Prove to Chris that the team delivers **mechanism + scalability**, not just one game.

Target ship date: **Fri 2026-07-11**.

---

## 1. Priority Tier (frozen from Milestone #2 re-tier)

- **P0** — USS (Universal Slot Solver) engine + schema + MVP1/2/3 configs.
- **P1** — Art-Bible Schema (#361). Bridge between USS and the 3 art stocks.
- **P2** — The 3 art stocks (parallel, equal): #362 Arcade, #363 Minimax-Clean, #364 Photoreal-Hailuo.
- **P3** — Hailuo→asset pipeline wiring (#358) + Hailuo DNA spec (#359).
- **P4** — Photoreal Revamp execution (#360 EPIC, #365 Duck Hunters anticipation).
- **P5** — Polish FX (#356 3D tile motion, #357 fire/smoke). Demoted from P0-critical.

**Merge rules:** No skin merges before P1 lands. No FX merges before P4 lands.

---

## 2. Work Decomposition (every step tagged)

Legend: 🟢 = AI fully owns. 🟡 = AI drafts, human reviews. 🔴 = Bach (or Kevin) manual, irreducible.

### A. USS Engine (P0)
| Step | Tag | Owner | Status |
|---|---|---|---|
| Schema (uss.schema.v0.1.json) | 🟢 | David/AI | DONE |
| MVP1/2/3 configs | 🟢 | David/AI | DONE |
| RTP Monte-Carlo harness | 🟢 | AI | TODO this sprint |
| RTP regression test on every commit | 🟢 | AI | TODO this sprint |
| Engine ↔ live frontend wiring | 🔴 | **Bach** | NEEDS TIMELINE |
| Dynamic-grid cascade renderer hooks | 🟡 | AI spec + Bach impl | NEEDS TIMELINE |

### B. Art-Bible Schema & 3 Art Stocks (P1–P2)
| Step | Tag | Owner | Status |
|---|---|---|---|
| #361 Art-Bible Schema draft | 🟡 | AI draft → Bach sign-off | DRAFT THIS WEEK |
| #359 Hailuo DNA quantification | 🟢 | AI (NotebookLM + Perplexity) | IN PROGRESS |
| #364 Photoreal-Hailuo bible | 🟢 | AI | TODO |
| #363 Minimax-Clean bible | 🟢 | AI | TODO |
| #362 Arcade bible (docs current look) | 🟢 | AI | TODO |
| #358 Asset-pipeline contract confirm | 🟡 | AI → Bach confirms | NEEDS CONFIRM |
| One-click re-skin in live game | 🔴 | **Bach** | NEEDS FEASIBILITY ANSWER |

### C. Photoreal Revamp (P4)
| Step | Tag | Owner | Status |
|---|---|---|---|
| anticipation_meta.md | 🟢 | AI | DONE |
| Duck Hunters beat-capture extraction | 🟡 | AI extract → Bach impl | TODO |
| #356 3D tile motion shader | 🔴 | Bach | DEMOTED P5 |
| #357 Fire/Smoke FX | 🔴 | Bach | DEMOTED P5 |
| Chris-facing swap demo | 🟡 | AI builds → Bach hosts | TODO before Chris call |

### D. Communication Layer
| Step | Tag | Owner |
|---|---|---|
| Chris-facing summaries/decks | 🟢 | AI → David approves |
| Weekly status reports (auto from GitHub + Fireflies) | 🟢 | AI |
| Kevin ↔ Chris relationship | 🔴 | **Kevin** |
| David ↔ Chris alignment calls | 🔴 | **David** |
| Bach-voice tech replies (drafted for Bach to approve) | 🟡 | AI draft → Bach 1-click approve |

### E. Process Ops
| Step | Tag | Owner |
|---|---|---|
| GitHub labels/priorities | 🟢 | AI |
| Doc sync across Google Docs + GitHub + Telegram | 🟢 | AI (daily pass) |
| Fireflies → GitHub-issue auto-pipeline | 🟢 | AI (TO BE SET UP) |
| Scope-drift flagging in real time | 🟡 | AI flags → David decides |

---

## 3. Timeline (frozen, no drift)

| Date | Owner | Deliverable |
|---|---|---|
| Mon 2026-05-11 (today) | David | Lock plan schema (this doc) + Bach-time one-pager |
| Tue 2026-05-12 18:00 CEST | **Bach** | Timeline for USS↔frontend wiring + re-skin feasibility answer |
| Tue 2026-05-12 18:00 CEST | **Kevin** | Thought on plan + Chris-call timing |
| Wed 2026-05-13 AM | David | Single doc + GitHub update pass (no second pass) |
| Wed 2026-05-13 PM | David | Chris green-light meeting |
| Thu 2026-05-14 | Team | Sprint 1 starts |
| Fri 2026-05-23 | Team | Sprint 1 ends: USS wired into frontend + Art-Bible Schema (#361) merged |
| Fri 2026-06-06 | Team | Sprint 2 ends: 3 art-stock skins drafted, parallel, on same USS game |
| Fri 2026-07-11 | Team | **MVP ship** for market-fit read |

---

## 4. Bach — Fill These In By Tue 18:00 CEST

- [ ] B1. Timeline to wire USS into the live frontend: ____ days
- [ ] B2. Is one-click re-skin feasible in current frontend architecture? YES / NO / NEEDS REFACTOR
- [ ] B3. Estimated time to implement cascade + anticipation timing hooks in the renderer: ____ days
- [ ] B4. Any task in the milestone you want re-scoped or dropped: ____
- [ ] B5. Anything you want AI to fully own that is currently on your plate: ____

## 5. Kevin — Fill These In By Tue 18:00 CEST

- [ ] K1. Best date/time to meet Chris in person: ____
- [ ] K2. Things David should NOT say to Chris: ____
- [ ] K3. Visa / on-the-ground blockers in next 30 days: ____
- [ ] K4. Your sentiment on the re-tier (agree / push back / partial): ____

---

## 6. Definition of Done (this sprint cycle)

- USS engine running inside the live frontend.
- Art-Bible Schema merged.
- 1 working art-stock swap demo Chris can click.
- RTP regression test green on all 3 MVP configs.
- No FX work merged.

---

## 7. Anti-Drift Rules

1. Plan is locked Wed AM. After that, only PRs against this doc.
2. Bach's three protected tasks (see `bach_time.md`) are the only things on his plate. Everything else is AI or AI-assisted.
3. If Chris asks for anything outside this scope mid-sprint, route through David. Do not start work without a milestone update.
4. Weekly status report auto-generated every Friday. No human-written status updates.
