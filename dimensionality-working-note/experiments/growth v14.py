"""v14: de-registration / node death (pre-registered 5.23).
Death rule: a node whose every link falls below the instrument threshold
(S~ <= 1e-6) is removed at the epoch boundary. Address slots are reusable.
A dying node's flow dies with it. Panel: + deaths, N_ss, birth/death ratio.
Validity: conversion rate >= 10% AND deaths >= 10 AND N_ss < NMAX.
Cell (0.3, 0.05), pc in {0.01, 0.02}, seeds 5/6/7. Control: v13 (5.22).
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 600; PB = 0.02; THETA = 0.75; K = 2
LAM = 0.3; GAMMA = 0.05
TOTAL_EVENTS = 36_000; EVENTS_PER_EPOCH = 3_000
LINK_EPS = 1e-6   # instrument threshold reused as existence threshold

def solve_rho(H, lam, iters=500):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rn = (1 - np.exp(-lam*rho[:,None]*H)).sum(1)
        if np.allclose(rn, rho, atol=1e-12): break
        rho = 0.5*rho + 0.5*rn
    return rho

def panel(S, ngrown):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    mask = Sc > LINK_EPS; np.fill_diagonal(mask, False)
    cl = S[mask] if mask.sum() else np.array([0.0])
    medC = float(np.median(cl)); f09 = float((cl > 0.9).mean())
    E = int(mask.sum() // 2)
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax(); keep = lab == big
    gcf = keep.sum()/ngrown
    cyc = E - ngrown + nc
    D = shortest_path(Wg[np.ix_(keep,keep)], method='D', directed=False)
    n = D.shape[0]; fin = np.isfinite(D) & (D > 0)
    dq = np.quantile(D[fin], [0.5, 0.95]) if fin.sum() else (np.nan, np.nan)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    d_cal, cv = np.nan, np.nan
    if nn:
        unit = np.median(nn); rs = unit*np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs])
        sel = (counts > 5) & (counts < 0.5*n)
        if sel.sum() >= 4:
            bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
            rmid = rs[sel][len(rs[sel])//2]
            Ni = ((D <= rmid) & np.isfinite(D)).sum(1)
            cv = float(Ni.std()/Ni.mean())
            m = np.array([0.91,1.70,2.20]); t = np.array([1.,2.,3.])
            if bd > m[-1]: d_cal = t[-1]+(bd-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
            elif bd < m[0]: d_cal = t[0]+(bd-m[0])*(t[1]-t[0])/(m[1]-m[0])
            else: d_cal = float(np.interp(bd, m, t))
    if gcf < 0.6: ph = "FRAG"
    elif medC > 0.9: ph = "SAT "
    elif not np.isfinite(d_cal): ph = "SW  "
    else: ph = "METR"
    return ph, medC, f09, gcf, d_cal, cv, dq, cyc

def stball_paths(Cs, alive, w, k):
    m_ = Cs.shape[0]
    if w >= m_: return {}
    parent = {w: None}; frontier = [w]; out = {}
    depth = 0
    while frontier and depth < k:
        depth += 1
        nxt = []
        for u in frontier:
            if u >= m_: continue
            for v in np.where(Cs[u, :m_] >= THETA)[0]:
                v = int(v)
                if v not in parent and alive[v]:
                    parent[v] = u; nxt.append(v)
                    if depth >= 2:
                        cs = []; a, bb = v, parent[v]
                        while bb is not None:
                            cs.append(Cs[a, bb]); a, bb = bb, parent[bb]
                        out[v] = float(np.mean(cs))
        frontier = nxt
    return out

def run(seed, pc):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    alive = np.zeros(NMAX, dtype=bool)
    alive[0] = alive[1] = True
    H[0,1] = H[1,0] = 1.0
    flows = {0: 0, 1: 1}        # flow id -> node position (flow id = birth node)
    free = list(range(NMAX-1, 1, -1))   # reusable address stack
    nborn = 2; ndead = 0
    rho_full = np.ones(NMAX)
    def refresh():
        idx = np.where(alive)[0]
        r = solve_rho(H[np.ix_(idx, idx)], LAM)
        rho = np.zeros(NMAX); rho[idx] = r
        C = np.zeros((NMAX, NMAX))
        sub = 1 - np.exp(-LAM*r[:,None]*H[np.ix_(idx, idx)])
        C[np.ix_(idx, idx)] = 0.5*(sub + sub.T)
        return C
    Cs = refresh()
    ev = 0; evep = 0; nconv = 0; natt = 0; nmax_hit = False
    Nhist = []
    while ev < TOTAL_EVENTS:
        fids = list(flows.keys())
        rng.shuffle(fids)
        for f in fids:
            if ev >= TOTAL_EVENTS: break
            if f not in flows: continue
            w = flows[f]
            u = rng.random()
            if u < PB and free:
                a = free.pop()
                alive[a] = True; H[w, a] += 1.0; H[a, w] += 1.0
                flows[f] = a; flows[a] = a; nborn += 1
            elif u < PB + pc:
                cand = stball_paths(Cs, alive, w, K)
                if cand:
                    natt += 1
                    tgt = int(rng.choice(list(cand.keys())))
                    if rng.random() < cand[tgt] and free:
                        a = free.pop()
                        alive[a] = True
                        H[w, a] += 1.0; H[a, w] += 1.0
                        H[tgt, a] += 1.0; H[a, tgt] += 1.0
                        flows[a] = a; nborn += 1; nconv += 1
                    else:
                        c = Cs[w, tgt]
                        H[w, tgt] += (1.0 - c); H[tgt, w] += (1.0 - c)
            else:
                p = Cs[w].copy()
                p[~alive] = 0.0
                p += 1e-9*np.where(alive, H[w]+H[:, w], 0.0)
                p[w] = 0.0
                ss = p.sum()
                if ss < 1e-12:
                    nb = np.where(alive & ((H[w] + H[:, w]) > 0))[0]
                    nb = nb[nb != w]
                    nxt = int(rng.choice(nb)) if len(nb) else w
                else:
                    nxt = int(rng.choice(NMAX, p=p/ss))
                c = Cs[w, nxt]
                H[w, nxt] += (1.0 - c)
                flows[f] = nxt
            ev += 1; evep += 1
            if evep >= EVENTS_PER_EPOCH:
                H *= (1.0-GAMMA)
                Cs = refresh()
                # de-registration: nodes whose all links fall below threshold
                idx = np.where(alive)[0]
                Ssub = Cs[np.ix_(idx, idx)]
                haslink = (Ssub > LINK_EPS).sum(1) > 0
                dying = idx[~haslink]
                for dnode in dying:
                    alive[dnode] = False
                    H[dnode, :] = 0.0; H[:, dnode] = 0.0
                    flows.pop(int(dnode), None)
                    # flows standing on the dead node die too
                    for fk in [k_ for k_, v_ in flows.items() if v_ == dnode]:
                        flows.pop(fk, None)
                    free.append(int(dnode)); ndead += 1
                if not flows:   # total extinction
                    return None, nconv, natt, nborn, ndead, 0, False
                if not free: nmax_hit = True
                Nhist.append(int(alive.sum()))
                Cs = refresh()
                evep = 0
    res = panel(Cs[np.ix_(np.where(alive)[0], np.where(alive)[0])], int(alive.sum()))
    N_ss = int(np.mean(Nhist[-3:])) if len(Nhist) >= 3 else int(alive.sum())
    return res, nconv, natt, nborn, ndead, N_ss, nmax_hit

print(f"v14 de-registration, cell (l={LAM},g={GAMMA}); control v13 = SAT (5.22)")
for pc in (0.01, 0.02):
    for seed in (5, 6, 7):
        out = run(seed, pc)
        if out[0] is None:
            print(f"  pc={pc} s={seed}: TOTAL EXTINCTION conv={out[1]} dead={out[4]}")
            continue
        (ph, medC, f09, gcf, d, cv, dq, cyc), nconv, natt, nborn, ndead, N_ss, nmax_hit = out
        ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
        cs = f"{cv:4.2f}" if np.isfinite(cv) else " nan"
        rate = nconv/max(natt,1)
        v1 = rate >= 0.10; v2 = ndead >= 10 and N_ss < NMAX
        valid = "VALID" if (v1 and v2) else "INVALID"
        print(f"  pc={pc} s={seed}: {ph} d={ds} cv={cs} f09={f09:4.2f} cyc={cyc:4d} "
              f"conv={rate:4.0%} born={nborn:4d} dead={ndead:4d} N_ss={N_ss:3d} "
              f"NMAXhit={nmax_hit} [{valid}]")
