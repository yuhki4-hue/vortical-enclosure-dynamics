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
from collections import Counter

def betti1_support(H, alive, eps=1e-12):
    """(V, E, C, b1) of the UNDIRECTED support graph {H>eps} on alive nodes.
    b1 = E - V + C  (first Betti number = number of independent cycles).
    Uses eps=1e-12 to match the firing/outgoing support convention."""
    idx = np.where(alive)[0]
    V = int(idx.size)
    if V == 0:
        return 0, 0, 0, 0
    Hs = H[np.ix_(idx, idx)]
    A = (Hs > eps) | (Hs.T > eps)
    np.fill_diagonal(A, False)
    E = int(A.sum() // 2)
    ncomp, _ = connected_components(A, directed=False)
    return V, E, int(ncomp), E - V + int(ncomp)

NMAX = 300
TRULE = 'T1'
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
    # --- per-event betti ledger: Counter[(label, dV, dE, db1)] -> count ---
    evledger = Counter()      # registration-event transitions (T1/T2/T3_*/REG/DYAD/FLOOR)
    decledger = Counter()     # continuous decay H*=(1-g): (dV, dE, db1) per epoch
    deathledger = Counter()   # isolated-death removals: (dV, dE, db1) per epoch
    b1_epoch = []             # (ep+1, settled b1 after death) per epoch
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
                _vb, _eb, _cb, _b1b = betti1_support(H, alive)
                a = free.pop(); b = free.pop()
                alive[a] = alive[b] = True
                H[a, b] = 1.0                 # directed first difference
                _va, _ea, _ca, _b1a = betti1_support(H, alive)
                evledger[("DYAD", _va-_vb, _ea-_eb, _b1a-_b1b)] += 1
                events.append((a, b)); ndyad += 1
        else:
            L = live_links[rng.integers(len(live_links))]
            events.append(L)
        if len(events) > 100_000:
            return "RUNAWAY", snaps, asym_hist, nsub, ndead, audit_ok, evledger, decledger, deathledger, b1_epoch, (b1_epoch[-1][1] if b1_epoch else 0)
        Wnext = {}
        rng.shuffle(events)
        for (i, j) in events:
            if not (alive[i] and alive[j]): continue
            c = 0.5*(C[i, j] + C[j, i])   # conversion on symmetric part
            if rng.random() < c and (free or TRULE == "T3"):
                _vb, _eb, _cb, _b1b = betti1_support(H, alive)
                _lab = None
                if TRULE == "T1":            # subdivision: new node, degree 2
                    a = free.pop(); alive[a] = True
                    H[i, a] += 1.0; H[a, j] += 1.0
                    nsub += 1; dst = outgoing(a); _lab = "T1"
                elif TRULE == "T2":          # budding: new node, degree 1
                    a = free.pop(); alive[a] = True
                    H[i, a] += 1.0
                    nsub += 1; dst = outgoing(a); _lab = "T2"
                else:                        # T3 face-filling: link a common neighbour, no new node
                    common = np.where((H[i,:]+H[:,i] > 1e-12) & (H[j,:]+H[:,j] > 1e-12) & alive)[0]
                    common = [int(k) for k in common if k != i and k != j]
                    if common:
                        k2 = int(rng.choice(common))
                        H[i, j] += 1.0        # close the firing pair (fill triangle i-k2-j)
                        nsub += 1; dst = outgoing(j, exclude=i) or [(j, i)]; _lab = "T3_main"
                    else:
                        if not free: continue
                        a = free.pop(); alive[a] = True   # fallback: subdivision
                        H[i, a] += 1.0; H[a, j] += 1.0
                        nsub += 1; dst = outgoing(a); _lab = "T3_fallback"
                if _lab is not None:
                    _va, _ea, _ca, _b1a = betti1_support(H, alive)
                    evledger[(_lab, _va-_vb, _ea-_eb, _b1a-_b1b)] += 1
            else:
                _existed = (H[i, j] > 1e-12) or (H[j, i] > 1e-12)   # firing pair already an edge?
                if _existed:
                    H[i, j] += (1.0 - c)      # DIRECTED registration (strengthen existing edge)
                    evledger[("REG", 0, 0, 0)] += 1
                else:                         # refutation watch: does REG ever CREATE an edge?
                    _vb, _eb, _cb, _b1b = betti1_support(H, alive)
                    H[i, j] += (1.0 - c)
                    _va, _ea, _ca, _b1a = betti1_support(H, alive)
                    evledger[("REG", _va-_vb, _ea-_eb, _b1a-_b1b)] += 1
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
        _vb_d, _eb_d, _cb_d, _b1b_d = betti1_support(H, alive)
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
        _va_d, _ea_d, _ca_d, _b1a_d = betti1_support(H, alive)
        decledger[(_va_d-_vb_d, _ea_d-_eb_d, _b1a_d-_b1b_d)] += 1
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
            _vb_x, _eb_x, _cb_x, _b1b_x = betti1_support(H, alive)
            for dnode in idx[~haslink]:
                alive[dnode] = False
                H[dnode, :] = 0.0; H[:, dnode] = 0.0
                C[dnode, :] = 0.0; C[:, dnode] = 0.0
                free.append(int(dnode)); ndead += 1
            _va_x, _ea_x, _ca_x, _b1a_x = betti1_support(H, alive)
            deathledger[(_va_x-_vb_x, _ea_x-_eb_x, _b1a_x-_b1b_x)] += 1
        b1_epoch.append((ep + 1, betti1_support(H, alive)[3]))
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
                _b1snap = betti1_support(H, alive)[3]
                snaps.append((ep+1,) + panel(Sn, len(idx2)) + (phic, ntri, _b1snap))
            else:
                _b1snap = betti1_support(H, alive)[3]
                snaps.append((ep+1, "DEAD", np.nan, np.nan, np.nan, np.nan, np.nan, 0, _b1snap))
    final_b1 = b1_epoch[-1][1] if b1_epoch else 0
    return "ok", snaps, asym_hist, nsub, ndead, audit_ok, evledger, decledger, deathledger, b1_epoch, final_b1

lam = 0.9
g = float(sys.argv[1])
epochs = int(sys.argv[2])
seeds = [int(s) for s in sys.argv[3].split(",")]
if len(sys.argv) > 4: globals()['NMAX'] = int(sys.argv[4])
globals()['TRULE'] = sys.argv[5] if len(sys.argv) > 5 else 'T1'
globals()['SNAPS'] = tuple(range(10, epochs + 1, 10))

import os
PERSEED_TSV = os.environ.get("PERSEED_TSV", "")

def sig_keys(evl, lab):
    sub = {(k[1], k[2], k[3]): v for k, v in evl.items() if k[0] == lab}
    return sum(sub.values()), sub

def sink_sum(cnt):
    sdV = sdE = sdb1 = nnzV = tot = 0
    for k, v in cnt.items():
        dV, dE, db1 = k
        sdV += dV*v; sdE += dE*v; sdb1 += db1*v; tot += v
        if dV != 0: nnzV += v
    return sdV, sdE, sdb1, nnzV, tot

EV = Counter(); DEC = Counter(); DX = Counter()
perseed = []
for seed in seeds:
    status, snaps, asym, nsub, ndead, audit, evl, decl, deathl, b1_epoch, final_b1 = run(seed, lam, g, True, epochs=epochs, protect=False)
    EV.update(evl); DEC.update(decl); DX.update(deathl)
    windows = []; curw = []
    for s in snaps:
        if s[1] == "METR": curw.append(s)
        else:
            if curw: windows.append(curw); curw = []
    if curw: windows.append(curw)
    occ = sum(len(w) for w in windows)
    t1n, t1k = sig_keys(evl, "T1"); t2n, t2k = sig_keys(evl, "T2")
    regn, regk = sig_keys(evl, "REG"); t3mn, _ = sig_keys(evl, "T3_main")
    t3fbn, _ = sig_keys(evl, "T3_fallback")
    t1_pure = (t1k == {(1, 2, 1): t1n}) if t1n else None
    t2_pure = (t2k == {(1, 1, 0): t2n}) if t2n else None
    reg_newedge = sum(v for kk, v in regk.items() if kk != (0, 0, 0))
    dc_dV, dc_dE, dc_db1, dc_nnzV, _ = sink_sum(decl)
    dx_dV, dx_dE, dx_db1, dx_nnzV, _ = sink_sum(deathl)
    b1map = dict(b1_epoch)
    b1_metr = [b1map[s[0]] for s in snaps if s[1] == "METR" and s[0] in b1map]
    b1_non  = [b1map[s[0]] for s in snaps if s[1] not in ("METR", "DEAD") and s[0] in b1map]
    mean = lambda a: (sum(a) / len(a)) if a else float('nan')
    src = t1n + t3fbn                 # cycles minted by triangle insertions
    net = src + dc_db1 + dx_db1       # predicted net b1 from source+sink (start empty)
    closes = (net == final_b1)        # ledger-closure audit: is every db1 accounted for?
    dratio = (dx_dE / dx_dV) if dx_dV != 0 else float('nan')  # expect ~2 (degree-2 death)
    rec = dict(N=NMAX, rule=TRULE, seed=seed, occ=occ, nwin=len(windows),
               t1n=t1n, t1_pure=t1_pure, t2n=t2n, t2_pure=t2_pure,
               regn=regn, reg_newedge=reg_newedge, t3mn=t3mn, t3fbn=t3fbn,
               decay_dVnz=dc_nnzV, decay_dE=dc_dE, decay_db1=dc_db1,
               death_dV=dx_dV, death_dE=dx_dE, death_db1=dx_db1, death_EV=round(dratio, 3),
               src=src, net_b1=net, final_b1=final_b1, closes=closes,
               b1_metr=round(mean(b1_metr), 3), b1_non=round(mean(b1_non), 3),
               nmetr=len(b1_metr), nnon=len(b1_non))
    perseed.append(rec)
    print(f"[SEED] N={NMAX} {TRULE} s={seed} | occ={occ} win={len(windows)} "
          f"| T1 n={t1n} pure={t1_pure} | T2 n={t2n} pure={t2_pure} "
          f"| REG n={regn} newedge={reg_newedge} | T3m={t3mn} T3fb={t3fbn} "
          f"| decay(dVnz={dc_nnzV},dE={dc_dE},db1={dc_db1}) "
          f"| death(dV={dx_dV},dE={dx_dE},db1={dx_db1},E/V={dratio:.2f}) "
          f"| src={src} net={net} final_b1={final_b1} closes={closes} "
          f"| b1_METR={mean(b1_metr):.2f}(n{len(b1_metr)}) b1_nonMETR={mean(b1_non):.2f}(n{len(b1_non)})")

allT1 = {k: v for k, v in EV.items() if k[0] == "T1"}
allT2 = {k: v for k, v in EV.items() if k[0] == "T2"}
allREGbad = sum(v for k, v in EV.items() if k[0] == "REG" and (k[1], k[2], k[3]) != (0, 0, 0))
t1_ok = all((k[1], k[2], k[3]) == (1, 2, 1) for k in allT1)
t2_ok = all((k[1], k[2], k[3]) == (1, 1, 0) for k in allT2)
closes_all = all(r["closes"] for r in perseed)
print(f"\n[VERDICT N={NMAX} {TRULE}] T1_pure={t1_ok}(n={sum(allT1.values())}) "
      f"T2_pure={t2_ok}(n={sum(allT2.values())}) REG_newedge_total={allREGbad} "
      f"ledger_closes_all={closes_all}")

if PERSEED_TSV and perseed:
    import csv
    newfile = not os.path.exists(PERSEED_TSV)
    with open(PERSEED_TSV, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(perseed[0].keys()), delimiter="\t")
        if newfile: w.writeheader()
        for r in perseed: w.writerow(r)

def show_ledger(name, C_):
    print(f"\n### {name}: total {sum(C_.values())} events")
    if not C_:
        print("    (none)"); return
    keyed_by_label = isinstance(next(iter(C_))[0], str)
    if keyed_by_label:
        order = ["DYAD", "T1", "T2", "T3_main", "T3_fallback", "REG", "FLOOR"]
        labels = [l for l in order if any(k[0] == l for k in C_)]
        labels += sorted({k[0] for k in C_ if k[0] not in order})
        for lab in labels:
            sub = {k: v for k, v in C_.items() if k[0] == lab}
            n = sum(sub.values())
            parts = [f"(dV={k[1]:+d},dE={k[2]:+d},db1={k[3]:+d})x{v}"
                     for k, v in sorted(sub.items(), key=lambda kv: -kv[1])]
            print(f"    {lab:13s} n={n:8d}  " + "  ".join(parts))
    else:
        for k, v in sorted(C_.items(), key=lambda kv: -kv[1]):
            print(f"    (dV={k[0]:+d},dE={k[1]:+d},db1={k[2]:+d}) x{v}")

print("\n" + "=" * 72)
print(f"AGGREGATE OVER SEEDS  rule={TRULE} g={g} N={NMAX} epochs={epochs} seeds={seeds}")
print("=" * 72)
show_ledger("REGISTRATION EVENTS (label, dV, dE, db1)", EV)
show_ledger("DECAY per-epoch  H*=(1-g)", DEC)
show_ledger("DEATH per-epoch  isolated removal", DX)
