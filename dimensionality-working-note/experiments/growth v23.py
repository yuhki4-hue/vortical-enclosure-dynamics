"""v18: directed ledger -- restoring the antisymmetric sector
(pre-registered 5.41).

Ledger is DIRECTED: w[i->j] != w[j->i]. An event i->j deposits its total
1 unit into OUTGOING links of j (j->k, k != i); if j's only exit is j->i,
reflect (deposit on j->i). The fired link itself receives nothing:
persistence requires re-feeding from upstream => circulation.
Distribution: C-weighted (directed version of variant C... per 5.41.2
"分配形は C 重み" -- variant B weighting on directed exits).
Slow layer (H, C) symmetric, unchanged. sigma=1 by total-1 invariance.
Control: v17-C same seeds with dense snapshots.
Panel: window occupancy, consecutive-METR lengths, ledger asymmetry,
sigma audit, standard panel. Snapshots every 25 epochs.
"""
import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

NMAX = 300
LINK_EPS = 1e-6
SNAPS = tuple(range(25, 301, 25))

def dual_dims(D, n):
    fin = np.isfinite(D) & (D > 0)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    bd = kd = np.nan
    if nn:
        unit = np.median(nn); rs = unit*np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs])
        sel = (counts > 5) & (counts < 0.5*n)
        if sel.sum() >= 4:
            b = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
            m = np.array([0.912,1.700,2.204,2.526]); t = np.array([1.,2.,3.,4.])
            if b > m[-1]: bd = t[-1]+(b-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
            elif b < m[0]: bd = t[0]+(b-m[0])*(t[1]-t[0])/(m[1]-m[0])
            else: bd = float(np.interp(b, m, t))
    # kernel powerlaw on exp(-D/med)
    if fin.sum() > 100:
        med = np.median(D[fin])
        Dc = np.where(np.isfinite(D), D, D[np.isfinite(D)].max()*2)
        K = np.exp(-Dc/med)
        ev = np.linalg.eigvalsh(K)[::-1]
        ev = ev[ev > 1e-12*ev[0]]
        k = np.arange(1, len(ev)+1)
        sel2 = (k >= 5) & (k <= max(11, len(ev)//4))
        if sel2.sum() >= 4:
            s_ = np.polyfit(np.log(k[sel2]), np.log(ev[sel2]), 1)[0]
            if abs(s_) > 1.0:
                kraw = 1.0/(abs(s_)-1.0)
                m2 = np.array([0.943, 1.802, 2.979, 4.804]); t2 = np.array([1.,2.,3.,4.])
                if kraw > m2[-1]: kd = t2[-1]+(kraw-m2[-1])*(t2[-1]-t2[-2])/(m2[-1]-m2[-2])
                elif kraw < m2[0]: kd = t2[0]+(kraw-m2[0])*(t2[1]-t2[0])/(m2[1]-m2[0])
                else: kd = float(np.interp(kraw, m2, t2))
    return bd, kd, (b if 'b' in dir() else np.nan), (kraw if 'kraw' in dir() else np.nan)

def panel(S, ngrown):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    mask = Sc > LINK_EPS; np.fill_diagonal(mask, False)
    cl = S[mask] if mask.sum() else np.array([0.0])
    medC = float(np.median(cl)); f09 = float((cl > 0.9).mean())
    Wg = np.where(mask, W, 0.0)
    nc, lab = connected_components((Wg > 0), directed=False)
    big = np.bincount(lab).argmax(); keep = lab == big
    gcf = keep.sum()/max(ngrown,1)
    D = shortest_path(Wg[np.ix_(keep,keep)], method='D', directed=False)
    n = D.shape[0]; fin = np.isfinite(D) & (D > 0)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    d_cal = np.nan
    if nn:
        unit = np.median(nn); rs = unit*np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs])
        sel = (counts > 5) & (counts < 0.5*n)
        if sel.sum() >= 4:
            bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
            m = np.array([0.91,1.70,2.20]); t = np.array([1.,2.,3.])
            if bd > m[-1]: d_cal = t[-1]+(bd-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
            elif bd < m[0]: d_cal = t[0]+(bd-m[0])*(t[1]-t[0])/(m[1]-m[0])
            else: d_cal = float(np.interp(bd, m, t))
    if gcf < 0.6: ph = "FRAG"
    elif medC > 0.9: ph = "SAT"
    elif not np.isfinite(d_cal): ph = "SW"
    else: ph = "METR"
    if ph == "METR":
        bd, kd, braw, kraw = dual_dims(D, n)
        return ph, medC, d_cal, bd, kd
    return ph, medC, d_cal, np.nan, np.nan

def run(seed, lam, gamma, directed, epochs=300, protect=False):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); C = np.zeros((NMAX, NMAX))
    Wl = {}   # directed: (i,j) ordered -> weight ; symmetric mode: same dict, key ordered pair too
    alive = np.zeros(NMAX, dtype=bool)
    free = list(range(NMAX-1, -1, -1))
    kappa = gamma
    nsub = ndead = ndyad = 0
    audit_ok = True
    snaps = []; asym_hist = []
    def outgoing(j, exclude=None):
        nb = np.where(((H[j, :] > 1e-12) | (H[:, j] > 1e-12)) & alive)[0]
        return [(j, int(k)) for k in nb if k != j and (exclude is None or k != exclude)]
    for ep in range(epochs):
        # fire
        events = []
        for L, w in list(Wl.items()):
            i, j = L
            if not (alive[i] and alive[j]) or H[i, j] <= 1e-12:
                continue
            k = rng.poisson(w)
            events += [L]*int(k)
        # floor
        live_links = [(i, j) for (i, j) in Wl.keys() if alive[i] and alive[j] and H[i,j] > 1e-12]
        if not live_links:
            all_pairs = np.argwhere(np.triu(H, 1) > 1e-12)
            live = [(int(a), int(b)) for a, b in all_pairs if alive[a] and alive[b]]
            if live:
                a_, b_ = live[rng.integers(len(live))]
                events.append((a_, b_) if rng.random() < 0.5 else (b_, a_))
            elif len(free) >= 2:
                a = free.pop(); b = free.pop()
                alive[a] = alive[b] = True
                H[a, b] = 1.0                 # directed first difference
                events.append((a, b)); ndyad += 1
        else:
            L = live_links[rng.integers(len(live_links))]
            events.append(L)
        if len(events) > 100_000:
            return "RUNAWAY", snaps, asym_hist, nsub, ndead, audit_ok
        Wnext = {}
        rng.shuffle(events)
        for (i, j) in events:
            if not (alive[i] and alive[j]): continue
            c = 0.5*(C[i, j] + C[j, i])   # conversion on symmetric part
            if rng.random() < c and free:
                a = free.pop(); alive[a] = True
                H[i, a] += 1.0                # flow-through: i -> a -> j
                H[a, j] += 1.0
                nsub += 1
                dst = outgoing(a)
            else:
                H[i, j] += (1.0 - c)          # DIRECTED registration
                if directed:
                    dst = outgoing(j, exclude=i)
                    if not dst: dst = [(j, i)]   # reflection
                else:
                    # symmetric control (v17-C style): incident links of i and j
                    dst = outgoing(i) + outgoing(j)
            if not dst: continue
            cw = np.array([max(C[a_, b_], 1e-9) for (a_, b_) in dst])
            sh = cw/cw.sum()
            for L, s in zip(dst, sh):
                Wnext[L] = Wnext.get(L, 0.0) + s
        nvalid = len([e for e in events if alive[e[0]] and alive[e[1]]])
        if events and abs(sum(Wnext.values()) - nvalid) > 1 + 0.05*len(events):
            audit_ok = False
        Wl = Wnext
        # asymmetry diagnostic
        num = den = 0.0
        seen = set()
        for (i, j), w in Wl.items():
            if (j, i) in seen or (i, j) in seen: continue
            seen.add((i, j))
            w2 = Wl.get((j, i), 0.0)
            num += abs(w - w2); den += w + w2
        asym_hist.append(num/den if den > 0 else 0.0)
        # slow layer: protected decay (v20) or plain (control)
        if protect:
            idx0 = np.where(alive)[0]
            Cn = C[np.ix_(idx0, idx0)]
            mx = Cn.max()
            Chat = Cn/mx if mx > 1e-12 else Cn
            # phi[i,j] = max_k min(Chat[j,k], Chat[k,i])  (directed return path)
            n0 = len(idx0)
            Phi = np.zeros((n0, n0))
            for a_ in range(n0):
                # min(Chat[j,k], Chat[k,i]) over k: vectorized per (j->i)
                pass
            # vectorized: M[j,i] = max_k min(Chat[j,k], Chat[k,i])
            M = np.zeros((n0, n0))
            for k_ in range(n0):
                M = np.maximum(M, np.minimum(Chat[:, k_][:, None], Chat[k_, :][None, :]))
            # phi for link (i->j) uses return path j->..->i : phi_ij = M[j, i]
            phi_full = np.zeros((NMAX, NMAX))
            phi_full[np.ix_(idx0, idx0)] = M.T
            H *= (1.0 - gamma*(1.0 - np.clip(phi_full, 0, 1)))
        else:
            H *= (1.0 - gamma)
        idx = np.where(alive)[0]
        if len(idx):
            rho = np.zeros(NMAX)
            for (i, j) in events:
                rho[i] += 1; rho[j] += 1
            Ceq = np.zeros((NMAX, NMAX))
            Ceq[np.ix_(idx, idx)] = 1 - np.exp(-lam * rho[idx][:,None] * H[np.ix_(idx, idx)])
            C += kappa*(Ceq - C)
            C[~alive, :] = 0.0; C[:, ~alive] = 0.0
            Sfull = 0.5*(C + C.T)
            Ssub = Sfull[np.ix_(idx, idx)]
            haslink = (Ssub > LINK_EPS).sum(1) > 0
            for dnode in idx[~haslink]:
                alive[dnode] = False
                H[dnode, :] = 0.0; H[:, dnode] = 0.0
                C[dnode, :] = 0.0; C[:, dnode] = 0.0
                free.append(int(dnode)); ndead += 1
        if (ep + 1) in SNAPS:
            idx2 = np.where(alive)[0]
            if len(idx2) >= 3:
                Sm = 0.5*(C + C.T)
                Amat = 0.5*(C - C.T)
                Sn = Sm[np.ix_(idx2, idx2)]; An = Amat[np.ix_(idx2, idx2)]
                # triangles on symmetric support
                Adj = Sn > LINK_EPS
                num = den = 0.0; ntri = 0
                n2 = len(idx2)
                # sample triangles via common-neighbor scan (cap for cost)
                iu2, ju2 = np.where(np.triu(Adj, 1))
                order = np.arange(len(iu2))
                if len(order) > 800: order = np.random.default_rng(0).choice(len(iu2), 800, replace=False)
                for t_ in order:
                    a_, b_ = int(iu2[t_]), int(ju2[t_])
                    ks = np.where(Adj[a_] & Adj[b_])[0]
                    for k_ in ks[:6]:
                        F = An[a_, b_] + An[b_, int(k_)] + An[int(k_), a_]
                        scale = abs(An[a_, b_]) + abs(An[b_, int(k_)]) + abs(An[int(k_), a_])
                        if scale > 1e-12:
                            num += abs(F); den += scale; ntri += 1
                phic = num/den if den > 0 else np.nan
                snaps.append((ep+1,) + panel(Sn, len(idx2)) + (phic, ntri))
            else:
                snaps.append((ep+1, "DEAD", np.nan, np.nan, np.nan, np.nan, np.nan, 0))
    return "ok", snaps, asym_hist, nsub, ndead, audit_ok

lam = 0.9
g = float(sys.argv[1])
epochs = int(sys.argv[2])
seeds = [int(s) for s in sys.argv[3].split(",")]
if len(sys.argv) > 4: globals()['NMAX'] = int(sys.argv[4])
globals()['SNAPS'] = tuple(range(10, epochs + 1, 10))
for seed in seeds:
    status, snaps, asym, nsub, ndead, audit = run(seed, lam, g, True, epochs=epochs, protect=False)
    # collect windows: consecutive METR snapshots
    windows = []; curw = []
    for s in snaps:
        if s[1] == "METR":
            curw.append(s)
        else:
            if curw: windows.append(curw); curw = []
    if curw: windows.append(curw)
    occ = sum(len(w) for w in windows)
    print(f"g={g} s={seed} [{status}] snaps={len(snaps)} occ={occ} windows={len(windows)} "
          f"dead={ndead} audit={'OK' if audit else 'FAIL'}")
    for w in windows:
        span = f"ep{w[0][0]}-{w[-1][0]}"
        ds = ", ".join(f"({x[3]:.2f}/{x[4]:.2f})" if np.isfinite(x[3]) or np.isfinite(x[4])
                       else "(-/-)" for x in w)
        print(f"    window {span} len={len(w)}: d(ball/kern) = {ds}")
