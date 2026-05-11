# Anticipation Meta — why the MVP configs feel good

This file records the *meta of feeling* behind the USS MVP configs. It is the "why does this hit?" layer that math configs alone don't carry. Bach's team and any reviewer should read this before judging mvp1/2/3.

The thesis: anticipation in slots is not vibes. It is **dopamine response to conditioned cues under variable-ratio reinforcement**, and the timing, geometry, and chain length of those cues can be designed. The three MVPs are three different stacks of those cues.

---

## 1. The four pillars (peer-reviewed, not folk wisdom)

### Pillar A — Variable-ratio reinforcement is the strongest reinforcement schedule known to behavioral science
Skinner showed that intermittent, unpredictable reward produces the most persistent, hardest-to-extinguish behavior in operant conditioning. Slot machines are the canonical real-world implementation. This is what makes a player take spin N+1 after losing on spin N. See Mindway AI summary of Skinner schedules and Lumen Learning psychology coursebook.

### Pillar B — Dopamine fires on the CUE, not (only) the reward
Anselme & Robinson (PMC3920462, 2014) and the broader temporal-difference learning literature show that after conditioning, dopamine release shifts from the reward delivery itself onto the *onset of cues that predict reward* — i.e., the spinning reels, the cascade animation, the multiplier badge climbing. That is why the spin animation, not the payout, is what players are actually chasing in the moment.

**Critical number:** dopamine response is strongest when reward probability is ~50%. Commercial slots over thousands of spins land at payoff > 0 around 45.8% (Tremblay et al. 2011, cited in PMC3920462). The industry already tunes to this band. Our MVPs do too — see hit-rate targets in each config.

### Pillar C — Near-miss exploits the dopamine system
Clark et al. (PMC2658737, 2009, Neuron) used fMRI on a simplified slot task and found that near-misses recruit the same ventral striatum / insula reward circuits as actual wins, *despite no money being delivered*. Chase & Clark (PMC3077261, 2011) confirmed this is D2-receptor mediated. Habib & Dixon (PMC2861872) showed players play longer on machines tuned for near-misses. Industry tuning sits near **~30% near-miss frequency** (Discover Magazine summary of Clark research).

This is the single most important psychology finding for slot design. **A near-miss is a positive prediction error rapidly followed by a negative prediction error**, and the brain registers the first hit before the correction lands.

### Pillar D — Cascade chains stack micro-rewards inside a single spin
Each cascade in a cluster/tumble game is an independent micro-cue: explosion + sound + multiplier tick. Industry data shows cascade slots increase retention measurably over fixed-line slots because each spin contains multiple reward predictions instead of one (Ido.design industry analysis; AAA Game Art Studio on animation pacing — "microbursts of pleasure that sustain engagement"). Pragmatic Play's Sugar Rush explicitly engineers a multiplier-spot snowball where re-hits on the same square escalate 2x → 4x → 8x ... → 128x. That is Pillar D operationalized.

---

## 2. The anticipation curve (six phases) and how each MVP hits them

Industry-standard anticipation arc has six recognizable phases. Each is a designable beat.

| # | Phase | What the player feels | Trigger |
|---|---|---|---|
| 1 | Tension | "What's about to happen?" | spin start, reel-height tease, board pre-shake |
| 2 | Relief | "OK, something happened." | first win lands |
| 3 | Building hope | "It's actually going." | second cascade / chain extends |
| 4 | Peak anticipation | "This could be huge." | multiplier climbs, scatter near-miss |
| 5 | Climax | "It WAS huge." | top-tier symbol + max multiplier hit |
| 6 | Re-engagement | "Spin again, now." | FS retrigger, persistent multiplier carried over |

### Where each MVP delivers each phase

**MVP #1 — ways, 6×5 fixed** *(reference: Mahjong Ways)*
- Phase 1: last-reel stop delay (~600–900 ms hold on near-misses).
- Phase 2: ways-win pays at 1x bet, fires often.
- Phase 3: weak — no cascade.
- Phase 4: scatter near-miss only.
- Phase 5: rare 100x H1 line.
- Phase 6: scatter-triggered FS.
- **Strength:** simplest, math-proven (10M-spin sim ~96% RTP). Best for "we can do math" credibility.
- **Weakness:** flat compared to #2/#3. One reward per spin.

**MVP #2 — cluster cascade, 7×7 fixed** *(reference: Sugar Rush)*
- Phase 1: board pre-shake before settle.
- Phase 2: first cluster pop (>=5 connected).
- Phase 3: cascade 2 → 3 with multiplier climb (1x → 2x → 4x → 8x → 16x).
- Phase 4: multiplier 8x+ with board still loaded.
- Phase 5: 16x cluster on full board.
- Phase 6: FS where multiplier persists across spins (snowball).
- **Strength:** five reward-prediction beats per winning spin instead of one. Strongest Pillar D stack.
- **Reference data:** Sugar Rush sits at 96.5% RTP, x5000 max win, 128x multiplier cap. Mobile-first design. Top-20 grossing slot 2023–2026.

**MVP #3 — dynamic-grid ways cascade, 6 cols × 2–7 rows variable** *(reference: Mahjong Ways 2 / Megaways / Wild Swarm)*
- Phase 1: **reel heights animate visibly BEFORE drop.** Tall column = high ways count = pre-cognitive "big win possible" signal. Strongest Phase-1 stack of the three.
- Phase 2: first ways win at 1x bet.
- Phase 3: cascade + re-roll of column heights between cascades — multiple Phase-1 → Phase-3 micro-cycles inside a single spin.
- Phase 4: scatter near-miss with tall reels still up.
- Phase 5: 10x FS multiplier on 117,649-ways grid (max-ways climax).
- Phase 6: **FS climbing multiplier never resets within the FS session.** Once you reach 10x, you stay at 10x for the rest of FS. Long FS sessions are themselves a meta-anticipation arc.
- **Strength:** stacks Pillar B (cue-driven dopamine) on Pillar D (cascade chain) on Pillar C (variable grid = continual near-miss potential). This is the highest-anticipation config of the three.

---

## 3. Timing budget (what the renderer must hit)

These are the animation timings the frontend team needs to honor for the math anticipation to actually be felt. Sourced from industry animation studio writeups and slot reel mechanics guides; not invented.

| Beat | Target duration | Why |
|---|---|---|
| Reel spin (base) | 1.8–2.2 s | long enough to load tension, short enough to not bore turbo players |
| Last reel stop delay (near-miss) | +600–900 ms hold | the Phase-1 dopamine spike lives here |
| Cluster explosion | 250–350 ms | fast enough to chain, slow enough to register |
| Tile drop after cascade | 300–450 ms | gravity feel — too fast reads as glitch |
| Multiplier badge punch | 150–250 ms with audio sting | each tick is a micro-reward cue |
| FS transition | 1.5–2.0 s with held audio note | Phase 6 hand-off |
| Big-win celebration | 2.5–4.0 s scaled to multiple of bet | Phase 5 climax |
| Turbo / quick-spin mode | 0.4–0.6 s total | for high-frequency players; trades anticipation for spin volume |

If Bach's team compresses these timings to "make it faster," they will mechanically destroy the dopamine curve. The math will still pay 96% RTP, but it will *feel* like a worse game. This is the most important hand-off note.

---

## 4. Honest gaps and what would close them

What we have:
- Math configs grounded in shipped top-grossing reference games.
- Anticipation phases mapped explicitly in `anticipation_design.player_state_map` in mvp2/mvp3 configs.
- Peer-reviewed dopamine/near-miss/VR-schedule literature cited above.
- Industry animation timing budget above.

What we do NOT have (be honest in the meeting):
- No clinical fMRI study on *our specific* configs. We are pattern-matching against games that have been tested in the literature.
- No live A/B retention data yet — we have not shipped any of the three to real players.
- No formal psychologist sign-off. The closest equivalent is citing the underlying research, which is what this doc does.

What would close those gaps post-meeting:
1. A/B test MVP #1 vs MVP #3 on the same skin (Food Slot). Compare 7-day retention, average session length, spins-per-session.
2. Recruit a paid consultant (behavioral-economics PhD) for a 4-hour review of the configs. Cheap relative to the build, high-credibility for B2B pitches.
3. Add a `psychological_profile` block to the USS schema so every future MVP must declare its dopamine targets explicitly. This locks the design discipline into the engine.

---

## 5. References (all externally accessible)

- Clark L. et al. (2009). *Gambling Near-Misses Enhance Motivation to Gamble and Recruit Win-Related Brain Circuitry.* Neuron. PMC2658737. https://pmc.ncbi.nlm.nih.gov/articles/PMC2658737/
- Chase H.W. & Clark L. (2011). *Dopamine Modulates Reward Expectancy During Performance of a Slot Machine Task.* PMC3077261. https://pmc.ncbi.nlm.nih.gov/articles/PMC3077261/
- Habib R. & Dixon M.R. *Neurobehavioral Evidence for the "Near-Miss" Effect.* PMC2861872. https://pmc.ncbi.nlm.nih.gov/articles/PMC2861872/
- Anselme P. & Robinson M.J.F. (2014). *Chronic exposure to a gambling-like schedule of reward.* PMC3920462. https://pmc.ncbi.nlm.nih.gov/articles/PMC3920462/
- Mindway AI. *Hooked on a Feeling — Psychology of Gambling.* https://mindway.ai/news_and_knowledge/hooked-on-a-feeling-high-on-believing-the-psychology-of-gambling/
- Lumen Learning. *Reinforcement Schedules (variable-ratio).* https://courses.lumenlearning.com/waymaker-psychology/chapter/reading-reinforcement-schedules/
- Discover Magazine. *Slot Machine Near Misses Are Perfectly Tuned to Stoke the Addiction.* https://www.discovermagazine.com/slot-machine-near-misses-are-perfectly-tuned-to-stoke-the-addiction-13214
- Ido.design. *The Evolution of Slot Machine Mechanics: Cascading Wins.* https://ido.design/the-evolution-of-slot-machine-mechanics-harnessing-cascading-wins/
- AAA Game Art Studio. *Animation Studio — emotional pacing in slots.* https://aaagameartstudio.com/blog/animation-studio
- Pragmatic Play Sugar Rush mechanic analysis. https://vodds.com/slots-and-games/sugar-rush/ and https://plg.bet/blog/sugar-rush-slot-review/

---

## 6. One-line summary for Chris

> The configs aren't guesses. Each anticipation beat in mvp1/2/3 maps to a published dopamine finding, and the timing budget for the renderer is documented. If we hit the timings, the math will feel like the reference games it's modeled on.
