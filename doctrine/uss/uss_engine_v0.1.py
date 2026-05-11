"""
USS Engine v0.1 — Universal Slot Solver reference engine (public mirror).

Consumes uss.schema.v0.1.json + a config (e.g. configs/mvp1.config.json) and
runs a deterministic Monte-Carlo to verify RTP. Pure-Python stdlib only so
Bach's team can drop it in without dependency drama.

Usage:
    python uss_engine_v0.1.py configs/mvp1.config.json

Output:
    target_rtp, measured_rtp, |diff|, pass/fail (<= 0.30 percentage-point tolerance).

This is the SAME contract the live frontend will speak to. The frontend just
feeds spin outcomes through `evaluate_grid` instead of generating them.
"""
import json, random, sys

RTP_TOLERANCE = 0.003  # 0.30 percentage points

def load_config(path):
    with open(path) as f:
        return json.load(f)

def build_reels(cfg):
    reels = []
    for strip in cfg["reels"]:
        flat = []
        for sym, weight in strip:
            flat.extend([sym] * int(weight))
        reels.append(flat)
    return reels

def spin(reels, rows, rng):
    grid = []
    for i, reel in enumerate(reels):
        start = rng.randrange(len(reel))
        col = [reel[(start + r) % len(reel)] for r in range(rows[i])]
        grid.append(col)
    return grid

def evaluate_ways(grid, cfg):
    paytable = cfg["paytable"]
    wild_enabled = cfg["wild"]["enabled"]
    wild_syms = set(cfg["wild"]["substitutes"]) if wild_enabled else set()
    counts_as_win = cfg["wild"].get("counts_as_win", False)
    k_min = cfg["k_min"]
    scalar = cfg["scalar"]
    cols = cfg["grid"]["cols"]

    total = 0.0
    for sym in paytable.keys():
        if sym == "WILD" and not counts_as_win:
            continue
        match = {sym}
        if wild_enabled:
            match.add("WILD")
        counts = []
        for c in range(cols):
            hit = sum(1 for s in grid[c] if s in match)
            if hit == 0:
                break
            counts.append(hit)
        k = len(counts)
        if k < k_min:
            continue
        ways = 1
        for h in counts:
            ways *= h
        pay_k = paytable[sym].get(str(k))
        if pay_k is None:
            continue
        total += pay_k * ways * scalar
    return total

def evaluate_grid(grid, cfg):
    if cfg["evaluation"] == "ways":
        return evaluate_ways(grid, cfg)
    raise NotImplementedError(f"evaluation={cfg['evaluation']} not in v0.1 (cluster/cascade in v0.2)")

def run(cfg):
    rng = random.Random(cfg["seed"])
    reels = build_reels(cfg)
    rows = cfg["grid"]["rows"]
    spins = cfg["spins"]
    bet = cfg["bet"]["cost"]
    total_pay, total_bet = 0.0, 0.0
    for _ in range(spins):
        g = spin(reels, rows, rng)
        total_pay += evaluate_grid(g, cfg)
        total_bet += bet
    return total_pay / total_bet

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "configs/mvp1.config.json"
    cfg = load_config(path)
    measured = run(cfg)
    target = cfg["target_rtp"]
    diff = abs(measured - target)
    ok = diff <= RTP_TOLERANCE
    print(f"config={cfg['id']} target_rtp={target:.4f} measured_rtp={measured:.4f} |diff|={diff:.4f} {'PASS' if ok else 'FAIL'}")
    sys.exit(0 if ok else 1)
