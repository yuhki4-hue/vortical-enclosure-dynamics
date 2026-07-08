"""v16b (memoryless fast layer per 5.31.3): two-layer dynamics (pre-registered 5.30).
Changes from v15b (only two):
  1. rho = recent registration-event rate at node i (K1 implementation):
     rho_i += 1 per event touching i; rho *= (1-gamma) at epoch boundary.
  2. C is a state variable with delayed relaxation:
     C <- C + kappa*(C_eq - C), C_eq = 1-exp(-lam*rho*H), kappa = gamma
     (convention, not a free parameter). New links start at C = 0.
Everything else per 5.26/5.27: Poisson firing mean |d rho| per link (H>0),
one-quantum degenerate fallback, conversion prob = C -> subdivision,
death on instrument C-threshold, H decay. Parameters: lambda, gamma ONLY.
Validity additions: C-delay actually operating (>=3 epochs to equilibrium).
"""
import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 300
LINK_EPS = 1e-6

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

def run(seed, lam, gamma, epochs):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    C = np.zeros((NMAX, NMAX))          # state variable, starts cold
    rho = np.zeros(NMAX)                # fast layer: last epoch's event rate
    rho_next = np.zeros(NMAX)           # current epoch's counter
    alive = np.zeros(NMAX, dtype=bool); alive[0] = alive[1] = True
    H[0,1] = H[1,0] = 1.0
    free = list(range(NMAX-1, 1, -1))
    nsub = 0; ndead = 0; ndegen = 0; nev = 0
    Nhist = []
    # C-delay validity probe: track epochs-to-90%-equilibrium for new links
    probe = {}   # (i,j) -> birth epoch ; resolved when C >= 0.9*C_eq
    delay_samples = []
    kappa = gamma
    for ep in range(epochs):
        idx = np.where(alive)[0]
        A = H[np.ix_(idx, idx)] > 1e-12
        iu, ju = np.where(np.triu(A, 1))
        if len(iu) == 0:
            return None, nsub, ndead, ndegen, nev, 0, delay_samples
        li, lj = idx[iu], idx[ju]
        wts = np.abs(rho[li] - rho[lj])
        tot = wts.sum()
        if tot < 1e-12:
            ndegen += 1
            counts = np.zeros(len(li), dtype=int)
            counts[rng.integers(len(li))] = 1
        else:
            counts = rng.poisson(wts)
        if counts.sum() > 200_000:
            return "RUNAWAY", nsub, ndead, ndegen, nev, 0, delay_samples
        for k in np.where(counts > 0)[0]:
            for _ in range(int(counts[k])):
                i, j = int(li[k]), int(lj[k])
                c = C[i, j]
                if rng.random() < c and free:
                    a = free.pop()
                    alive[a] = True
                    H[i, a] += 1.0; H[a, i] += 1.0
                    H[j, a] += 1.0; H[a, j] += 1.0
                    rho_next[i] += 1; rho_next[j] += 1; rho_next[a] += 2
                    probe[(min(i,a), max(i,a))] = ep
                    nsub += 1
                else:
                    H[i, j] += (1.0 - c); H[j, i] += (1.0 - c)
                    rho_next[i] += 1; rho_next[j] += 1
                nev += 1
        # epoch boundary
        H *= (1.0 - gamma)
        rho[:] = rho_next          # fast layer: last epoch's rate, memoryless
        rho_next = np.zeros(NMAX)
        idx = np.where(alive)[0]
        Ceq = np.zeros((NMAX, NMAX))
        sub = 1 - np.exp(-lam * rho[idx][:,None] * H[np.ix_(idx, idx)])
        Ceq[np.ix_(idx, idx)] = 0.5*(sub + sub.T)
        C += kappa * (Ceq - C)
        C[~alive, :] = 0.0; C[:, ~alive] = 0.0
        # probe resolution
        done = []
        for (pi, pj), b in probe.items():
            if alive[pi] and alive[pj] and Ceq[pi, pj] > 1e-6:
                if C[pi, pj] >= 0.9 * Ceq[pi, pj]:
                    delay_samples.append(ep - b); done.append((pi, pj))
            else:
                done.append((pi, pj))
        for kk in done: probe.pop(kk, None)
        # death on instrument threshold of C
        Ssub = C[np.ix_(idx, idx)]
        haslink = (Ssub > LINK_EPS).sum(1) > 0
        for dnode in idx[~haslink]:
            alive[dnode] = False
            H[dnode, :] = 0.0; H[:, dnode] = 0.0
            C[dnode, :] = 0.0; C[:, dnode] = 0.0
            rho[dnode] = 0.0; rho_next[dnode] = 0.0
            free.append(int(dnode)); ndead += 1
        if alive.sum() < 2:
            return None, nsub, ndead, ndegen, nev, 0, delay_samples
        Nhist.append(int(alive.sum()))
    idx = np.where(alive)[0]
    res = panel(C[np.ix_(idx, idx)], len(idx))
    N_ss = int(np.mean(Nhist[-3:])) if len(Nhist) >= 3 else int(alive.sum())
    return res, nsub, ndead, ndegen, nev, N_ss, delay_samples

mode = sys.argv[1]
if mode == "scan":
    for lam in (0.3, 0.9, 2.0):
        for g in (0.05, 0.15, 0.4):
            out = run(5, lam, g, epochs=120)
            if out[0] == "RUNAWAY":
                print(f"l={lam:4} g={g:4}: RUNAWAY (activity explosion) nev={out[4]}")
                continue
            if out[0] is None:
                print(f"l={lam:4} g={g:4}: EXTINCT sub={out[1]} dead={out[2]} nev={out[4]}")
                continue
            (ph, medC, f09, gcf, d, cv, dq, cyc), nsub, ndead, ndeg, nev, N_ss, dl = out
            ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
            mdl = f"{np.mean(dl):4.1f}" if dl else " n/a"
            print(f"l={lam:4} g={g:4}: {ph} medC={medC:4.2f} f09={f09:4.2f} d={ds} "
                  f"cyc={cyc:4d} sub={nsub:4d} dead={ndead:4d} N_ss={N_ss:3d} "
                  f"delay={mdl}ep nev={nev}")
else:
    lam, g, epochs = float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    for seed in (5, 6, 7):
        out = run(seed, lam, g, epochs=epochs)
        if out[0] is None:
            print(f"  s={seed}: EXTINCT sub={out[1]} dead={out[2]}")
            continue
        (ph, medC, f09, gcf, d, cv, dq, cyc), nsub, ndead, ndeg, nev, N_ss, dl = out
        ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
        cs = f"{cv:4.2f}" if np.isfinite(cv) else " nan"
        mdl = np.mean(dl) if dl else np.nan
        v = (nsub >= 10) and (ndead >= 10 and N_ss < NMAX) and (ndeg/max(nev,1) < 0.5) and (mdl >= 3 if np.isfinite(mdl) else False)
        print(f"  s={seed}: {ph} d={ds} cv={cs} f09={f09:4.2f} cyc={cyc:4d} "
              f"sub={nsub:4d} dead={ndead:4d} N_ss={N_ss:3d} delay={mdl:4.1f}ep "
              f"[{'VALID' if v else 'INVALID'}]")
