"""v17: registerability conservation + quantum floor + dyad genesis
(pre-registered 5.35).

Ledger w_ij = registerability measure on links. Events fire Poisson(w_ij).
Each realized event deposits TOTAL 1 unit into links incident to its
endpoints (distribution variants A equal / B C-weighted / C w-weighted).
w is rebuilt each epoch purely from this epoch's deposits (memoryless fast
layer) => sigma = 1 in expectation, by construction.
Quantum floor: 1 event/epoch, uniform on existing links; if none exist,
DYAD GENESIS (2 new nodes + link, H=1). System starts EMPTY.
Slow layer: H decay gamma; C delayed relaxation kappa=gamma; conversion
prob = C -> subdivision; death on instrument C-threshold.
Panel: ledger audit (sum w vs events), activity trace, dyad count.
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
    return ph, medC, f09, gcf, d_cal, cv, cyc

def run(seed, lam, gamma, variant, epochs):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); C = np.zeros((NMAX, NMAX))
    Wl = {}                      # ledger: (i,j) i<j -> registerability weight
    alive = np.zeros(NMAX, dtype=bool)
    free = list(range(NMAX-1, -1, -1))
    kappa = gamma
    nsub = ndead = ndyad = 0
    act = []; audit_ok = True
    def key(i, j): return (min(i,j), max(i,j))
    def incident_links(x, links):
        return [L for L in links if x in L]
    for ep in range(epochs):
        links = [L for L in Wl.keys()
                 if alive[L[0]] and alive[L[1]] and H[L[0], L[1]] > 1e-12]
        # --- fire events from ledger
        events = []
        for L in links:
            k = rng.poisson(Wl.get(L, 0.0))
            events += [L]*int(k)
        # --- quantum floor: 1 event/epoch
        if links:
            events.append(links[rng.integers(len(links))])
        else:
            # dyad genesis: the world begins (or re-begins) from nothing
            if len(free) >= 2:
                a = free.pop(); b = free.pop()
                alive[a] = alive[b] = True
                H[a, b] = H[b, a] = 1.0
                events.append(key(a, b)); ndyad += 1
        if len(events) > 100_000:
            return "RUNAWAY", ep, nsub, ndead, ndyad, act, audit_ok
        # --- process events; deposits build next ledger
        Wnext = {}
        rng.shuffle(events)
        for (i, j) in events:
            if not (alive[i] and alive[j]):
                continue
            c = C[i, j]
            if rng.random() < c and free:
                a = free.pop()
                alive[a] = True
                H[i, a] += 1.0; H[a, i] += 1.0
                H[j, a] += 1.0; H[a, j] += 1.0
                nsub += 1
                epts = (i, a)  # deposit around the new structure's endpoints
                dep_nodes = (a,)
            else:
                H[i, j] += (1.0 - c); H[j, i] += (1.0 - c)
                dep_nodes = (i, j)
            # deposit TOTAL 1 into links incident to dep_nodes
            cand = set()
            for x in dep_nodes:
                nb = np.where((H[x, :] > 1e-12) & alive)[0]
                for y in nb:
                    if y != x: cand.add(key(x, int(y)))
            cand = list(cand)
            if not cand: continue
            if variant == "A":
                sh = np.full(len(cand), 1.0/len(cand))
            elif variant == "B":
                cw = np.array([max(C[a_, b_], 1e-9) for (a_, b_) in cand])
                sh = cw/cw.sum()
            else:  # C: current-ledger weighted
                ww = np.array([max(Wl.get(L, 0.0), 1e-9) for L in cand])
                sh = ww/ww.sum()
            for L, s in zip(cand, sh):
                Wnext[L] = Wnext.get(L, 0.0) + s
        # ledger audit: conservation
        if events and abs(sum(Wnext.values()) - len([e for e in events
                if alive[e[0]] and alive[e[1]]])) > 1 + 0.05*len(events):
            audit_ok = False
        Wl = Wnext
        act.append(len(events))
        # --- slow layer
        H *= (1.0 - gamma)
        idx = np.where(alive)[0]
        if len(idx):
            # rho for C_eq: event rate per node this epoch
            rho = np.zeros(NMAX)
            for (i, j) in events:
                rho[i] += 1; rho[j] += 1
            Ceq = np.zeros((NMAX, NMAX))
            sub = 1 - np.exp(-lam * rho[idx][:,None] * H[np.ix_(idx, idx)])
            Ceq[np.ix_(idx, idx)] = 0.5*(sub + sub.T)
            C += kappa*(Ceq - C)
            C[~alive, :] = 0.0; C[:, ~alive] = 0.0
            Ssub = C[np.ix_(idx, idx)]
            haslink = (Ssub > LINK_EPS).sum(1) > 0
            for dnode in idx[~haslink]:
                alive[dnode] = False
                H[dnode, :] = 0.0; H[:, dnode] = 0.0
                C[dnode, :] = 0.0; C[:, dnode] = 0.0
                free.append(int(dnode)); ndead += 1
    idx = np.where(alive)[0]
    if len(idx) < 3:
        return "EMPTY", epochs, nsub, ndead, ndyad, act, audit_ok
    res = panel(C[np.ix_(idx, idx)], len(idx))
    return res, epochs, nsub, ndead, ndyad, act, audit_ok

mode = sys.argv[1]
if mode == "scan":
    for lam in (0.3, 0.9):
        for g in (0.05, 0.15, 0.4):
            out = run(5, lam, g, "A", epochs=200)
            res, ep, nsub, ndead, ndyad, act, audit = out
            a1 = np.mean(act[:len(act)//3]) if act else 0
            a3 = np.mean(act[-len(act)//3:]) if act else 0
            if res == "RUNAWAY":
                print(f"l={lam:4} g={g:4}: RUNAWAY at ep={ep}")
            elif res == "EMPTY":
                print(f"l={lam:4} g={g:4}: EMPTY  sub={nsub} dead={ndead} dyad={ndyad} "
                      f"act(1st/3rd)={a1:.1f}/{a3:.1f} audit={'OK' if audit else 'FAIL'}")
            else:
                ph, medC, f09, gcf, d, cv, cyc = res
                ds = f"{d:5.2f}" if np.isfinite(d) else "  nan"
                print(f"l={lam:4} g={g:4}: {ph} medC={medC:4.2f} f09={f09:4.2f} d={ds} "
                      f"cyc={cyc:3d} sub={nsub} dead={ndead} dyad={ndyad} "
                      f"act={a1:.1f}/{a3:.1f} audit={'OK' if audit else 'FAIL'}")
