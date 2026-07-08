"""v15: gradient-driven link-event model (pre-registered 5.26).
No agents. Events fire on existing links with weight |rho_i - rho_j|
(multinomial; uniform fallback if all weights zero -- sampling stochasticity
breaks symmetry, no added noise parameter).
Firing link: prob (1-C) register dH=(1-C); prob C convert to SUBDIVISION
(new node k, H_ik=H_jk=1). Closure emerges as subdivision's byproduct.
Death: all links below instrument threshold -> node removed (5.23.1).
Parameters: lambda, gamma ONLY.
Stage 1: 3x3 mini-scan. Stage 2: band cells, death-scale time budget.
Validity: subdivisions>=10, deaths>=10 & N_ss<NMAX, degeneracy rate<50%.
"""
import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 300
LINK_EPS = 1e-6

def solve_rho(H, lam, iters=120):
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
    gcf = keep.sum()/max(ngrown,1)
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

def run(seed, lam, gamma, epochs, ev_per_epoch):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    alive = np.zeros(NMAX, dtype=bool); alive[0] = alive[1] = True
    H[0,1] = H[1,0] = 1.0
    free = list(range(NMAX-1, 1, -1))
    nsub = 0; ndead = 0; ndegen = 0; nev = 0
    Nhist = []
    idx = np.where(alive)[0]
    rho_v = np.zeros(NMAX)
    r = solve_rho(H[np.ix_(idx, idx)], lam); rho_v[idx] = r
    C = np.zeros((NMAX, NMAX))
    sub = 1 - np.exp(-lam*r[:,None]*H[np.ix_(idx, idx)])
    C[np.ix_(idx, idx)] = 0.5*(sub+sub.T)
    for ep in range(epochs):
        # link list (upper triangle of alive-alive links above eps)
        idx = np.where(alive)[0]
        A = H[np.ix_(idx, idx)] > 1e-12
        iu, ju = np.where(np.triu(A, 1))
        if len(iu) == 0:
            return None, nsub, ndead, ndegen, nev, 0
        li, lj = idx[iu], idx[ju]
        wts = np.abs(rho_v[li] - rho_v[lj])
        for _ in range(ev_per_epoch):
            tot = wts.sum()
            if tot < 1e-12:
                ndegen += 1
                k = rng.integers(len(li))
            else:
                k = rng.choice(len(li), p=wts/tot)
            i, j = int(li[k]), int(lj[k])
            c = C[i, j]
            if rng.random() < c and free:
                a = free.pop()
                alive[a] = True
                H[i, a] += 1.0; H[a, i] += 1.0
                H[j, a] += 1.0; H[a, j] += 1.0
                nsub += 1
            else:
                H[i, j] += (1.0 - c); H[j, i] += (1.0 - c)
            nev += 1
        # epoch boundary: decay, rho refresh, death
        H *= (1.0 - gamma)
        idx = np.where(alive)[0]
        r = solve_rho(H[np.ix_(idx, idx)], lam)
        rho_v[:] = 0.0; rho_v[idx] = r
        C[:] = 0.0
        sub = 1 - np.exp(-lam*r[:,None]*H[np.ix_(idx, idx)])
        C[np.ix_(idx, idx)] = 0.5*(sub+sub.T)
        Ssub = C[np.ix_(idx, idx)]
        haslink = (Ssub > LINK_EPS).sum(1) > 0
        for dnode in idx[~haslink]:
            alive[dnode] = False
            H[dnode, :] = 0.0; H[:, dnode] = 0.0
            free.append(int(dnode)); ndead += 1
        if alive.sum() < 2:
            return None, nsub, ndead, ndegen, nev, 0
        Nhist.append(int(alive.sum()))
    idx = np.where(alive)[0]
    res = panel(C[np.ix_(idx, idx)], len(idx))
    N_ss = int(np.mean(Nhist[-3:])) if len(Nhist) >= 3 else int(alive.sum())
    return res, nsub, ndead, ndegen, nev, N_ss

mode = sys.argv[1]
if mode == "scan":
    # stage 1: short scan (death-scale not required for phase ID)
    for lam in (0.1, 0.3, 0.9):
        for g in (0.05, 0.15, 0.4):
            out = run(5, lam, g, epochs=60, ev_per_epoch=500)
            if out[0] is None:
                print(f"l={lam:4} g={g:4}: EXTINCT sub={out[1]} dead={out[2]}")
                continue
            (ph, medC, f09, gcf, d, cv, dq, cyc), nsub, ndead, ndeg, nev, N_ss = out
            ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
            print(f"l={lam:4} g={g:4}: {ph} medC={medC:4.2f} f09={f09:4.2f} d={ds} "
                  f"cyc={cyc:4d} sub={nsub:4d} dead={ndead:4d} degen={ndeg/max(nev,1):4.0%} N_ss={N_ss:3d}")
else:
    lam, g, epochs = float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    for seed in (5, 6, 7):
        out = run(seed, lam, g, epochs=epochs, ev_per_epoch=500)
        if out[0] is None:
            print(f"  s={seed}: EXTINCT sub={out[1]} dead={out[2]}")
            continue
        (ph, medC, f09, gcf, d, cv, dq, cyc), nsub, ndead, ndeg, nev, N_ss = out
        ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
        cs = f"{cv:4.2f}" if np.isfinite(cv) else " nan"
        v = (nsub >= 10) and (ndead >= 10 and N_ss < NMAX) and (ndeg/max(nev,1) < 0.5)
        print(f"  s={seed}: {ph} d={ds} cv={cs} f09={f09:4.2f} cyc={cyc:4d} "
              f"sub={nsub:4d} dead={ndead:4d} degen={ndeg/max(nev,1):4.0%} "
              f"N_ss={N_ss:3d} [{'VALID' if v else 'INVALID'}]")
