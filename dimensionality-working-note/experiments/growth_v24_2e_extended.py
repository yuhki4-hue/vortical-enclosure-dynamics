"""v24.2e: extended-epochs run (Working Note II sec 12-2, post offline test).

v24.2e additions over v24.2 (model dynamics still byte-identical to v24),
pre-registered in sec 12 with the discriminating prediction
  thinning hypothesis  => low redundancy (tree-like) inside contraction BSW
  readability hypothesis => high redundancy inside contraction BSW
  G. per-interval edge evaporation count (true rate instrument; the offline
     test used -dV as a proxy).
  H. S-support edge count and mean degree (thinning instruments).
  I. path redundancy on the S-support giant component: bridge fraction and
     2-edge-connected component occupancy (occ2ecc; tree => 0).

MODEL DYNAMICS ARE BYTE-IDENTICAL TO v24 (growth_v24_betti.py).
No new rng calls; all instruments are pure reads. Verified by matching
occ/windows/dead against v24 on the same seeds.

v24.2 additions over v24.1 (model dynamics still byte-identical to v24):
  A. W_scale(t): log(r_max_sel / r_min_sel), continuous scaling-range width
     (sec 5.3); recorded in all phases whenever >=2 selected radii exist.
  B. beta1(S, 1e-12): closure-support b1 at low theta -> full ladder
     SCC(Wl) -> b1(H,1e-12) -> b1(H,1e-6) -> b1(S,1e-12) -> b1(S,1e-6).
  C. rung 1->2 transformation efficiency: fraction of SCC(>=2) nodes that
     survive into the undirected 2-core of the H support (sec 9.3).
  D. n_dst statistics per inter-snapshot period (mean/p50/p90) - dilution
     bookkeeping ahead of v24.3.
  E. offline H->S lag correlation report: corr(b1_H(t), b1_S(t+tau)),
     tau in -3..3 snapshots, split by rising / falling b1_H (hysteresis
     probe, sec 9.3).
  F. headroom check: V_max vs NMAX warning at 95%; first-saturation epoch.

v24.1 instruments (all retained):
  1. exit reason per BSW window: label immediately after the window
     closes (FRAG / SAT / SW / DEAD / END-of-run).
  2. SW breakdown: fit failure reason
     (NO_GIANT, FEW_RADII, DEGENERATE_NN, NO_SCALING_PTS, OTHER).
  3. fit quality: n points, raw slope, R^2, calibrated d.
  4. multi-support beta1: b1 on H-support at 1e-12 (v24 topology
     instrument), H-support at 1e-6, S-support at LINK_EPS=1e-6
     (the BSW metric graph). Sec 9.3 threshold mismatch.
  5. directed instruments (function 1, registration maintenance):
     SCC stats of the Wl support digraph -- node occupancy of SCCs,
     fraction of Wl edges inside SCC>=3 (nontrivial directed cycle),
     inside SCC==2 (reflection dyad / mutual pair), open otherwise;
     reflection-fallback event rate. Sec 2.2.1 / 2.2.2.
  6. edge lifetime ledger on H-support (theta=1e-12), births/deaths
     per epoch, lifetime distribution (dead + right-censored alive).
  7. paired directed / symmetric runs on identical seeds
     (asymmetric-prediction pre-test, sec 2.2).

Usage: python growth_v24_1_instruments.py g epochs seeds [NMAX] [TRULE]
       (same CLI as v24)
"""
import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components
from collections import Counter

NMAX = 300
TRULE = 'T1'
LINK_EPS = 1e-6
SNAPS = tuple(range(25, 301, 25))


# ----------------------------------------------------------------------
# topology instruments (pure reads)
# ----------------------------------------------------------------------
def betti1_support(H, alive, eps=1e-12):
    """(V, E, C, b1) of the UNDIRECTED support graph {H>eps} on alive nodes."""
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


def betti1_matrix(M, alive, eps):
    """b1 of undirected support {M_sym > eps} on alive nodes (for S-support)."""
    idx = np.where(alive)[0]
    if idx.size == 0:
        return 0
    Ms = M[np.ix_(idx, idx)]
    A = (0.5 * (Ms + Ms.T)) > eps
    np.fill_diagonal(A, False)
    E = int(A.sum() // 2)
    ncomp, _ = connected_components(A, directed=False)
    return E - int(idx.size) + int(ncomp)


def scc_stats(Wl, alive, nmax):
    """SCC statistics of the directed Wl support graph (function-1 instruments).
    Returns dict:
      n_nodes  : nodes incident to any live Wl edge
      occ_scc  : fraction of those nodes in SCC size>=2
      occ_scc3 : fraction in SCC size>=3 (nontrivial circulation)
      e_total  : live Wl edges
      fe_cyc   : fraction of edges with both ends in same SCC>=3
      fe_dyad  : fraction with both ends in same SCC==2 (reflection dyad)
      fe_open  : remainder (open-chain / transient edges)
      max_scc  : largest SCC size
    """
    edges = [(i, j) for (i, j), w in Wl.items()
             if w > 0 and alive[i] and alive[j]]
    if not edges:
        return dict(n_nodes=0, occ_scc=np.nan, occ_scc3=np.nan, e_total=0,
                    fe_cyc=np.nan, fe_dyad=np.nan, fe_open=np.nan, max_scc=0)
    nodes = sorted({i for e in edges for i in e})
    pos = {v: k for k, v in enumerate(nodes)}
    n = len(nodes)
    A = np.zeros((n, n), dtype=bool)
    for (i, j) in edges:
        A[pos[i], pos[j]] = True
    ncomp, lab = connected_components(A, directed=True, connection='strong')
    size = np.bincount(lab, minlength=ncomp)
    nsz = size[lab]                       # SCC size per node
    occ_scc = float((nsz >= 2).sum()) / n
    occ_scc3 = float((nsz >= 3).sum()) / n
    ec = ed = 0
    for (i, j) in edges:
        a, b = lab[pos[i]], lab[pos[j]]
        if a == b and size[a] >= 3:
            ec += 1
        elif a == b and size[a] == 2:
            ed += 1
    et = len(edges)
    return dict(n_nodes=n, occ_scc=occ_scc, occ_scc3=occ_scc3, e_total=et,
                fe_cyc=ec / et, fe_dyad=ed / et, fe_open=(et - ec - ed) / et,
                max_scc=int(size.max()))


def redundancy_stats(Sn, ngiant_mask=None):
    """Bridge fraction and 2-edge-connected occupancy of the S-support
    giant component. Sn: symmetrized closure on alive nodes.
    Returns (bridge_frac, occ2ecc, E_S, kmean) computed on the giant
    component of {Sn > LINK_EPS}. Tree => bridge_frac=1, occ2ecc=0."""
    A = Sn > LINK_EPS
    np.fill_diagonal(A, False)
    n_all = A.shape[0]
    E_all = int(A.sum() // 2)
    kmean = 2.0 * E_all / n_all if n_all else np.nan
    ncomp, lab = connected_components(A, directed=False)
    if n_all == 0 or E_all == 0:
        return np.nan, np.nan, E_all, kmean
    big = np.bincount(lab).argmax()
    keep = np.where(lab == big)[0]
    if keep.size < 3:
        return np.nan, np.nan, E_all, kmean
    pos = {int(v): k for k, v in enumerate(keep)}
    n = keep.size
    adj = [[] for _ in range(n)]
    iu, ju = np.where(np.triu(A[np.ix_(keep, keep)], 1))
    for a, b in zip(iu, ju):
        adj[int(a)].append(int(b)); adj[int(b)].append(int(a))
    E = len(iu)
    # iterative Tarjan bridge finding (simple graph)
    disc = [-1]*n; low = [0]*n
    bridges = set()
    timer = 0
    for root in range(n):
        if disc[root] != -1: continue
        disc[root] = low[root] = timer; timer += 1
        stack = [(root, -1, 0)]
        while stack:
            u, pe, i = stack.pop()
            if i < len(adj[u]):
                stack.append((u, pe, i+1))
                v = adj[u][i]
                if v == pe:
                    continue
                if disc[v] == -1:
                    disc[v] = low[v] = timer; timer += 1
                    stack.append((v, u, 0))
                else:
                    low[u] = min(low[u], disc[v])
            else:
                if pe != -1:
                    low[pe] = min(low[pe], low[u])
                    if low[u] > disc[pe]:
                        bridges.add((min(u, pe), max(u, pe)))
    bridge_frac = len(bridges)/E if E else np.nan
    # 2ecc occupancy: components after bridge removal, size>=3
    A2 = np.zeros((n, n), dtype=bool)
    for a, b in zip(iu, ju):
        e = (min(int(a), int(b)), max(int(a), int(b)))
        if e not in bridges:
            A2[a, b] = A2[b, a] = True
    nc2, lab2 = connected_components(A2, directed=False)
    sz2 = np.bincount(lab2, minlength=nc2)
    occ2ecc = float((sz2[lab2] >= 3).sum())/n
    return bridge_frac, occ2ecc, E_all, kmean


def two_core_nodes(H, alive, eps=1e-12):
    """node set of the undirected 2-core of the H support graph."""
    idx = np.where(alive)[0]
    if idx.size == 0:
        return set()
    A = ((H > eps) | (H.T > eps))
    A = A[np.ix_(idx, idx)].copy()
    np.fill_diagonal(A, False)
    keep = np.ones(len(idx), dtype=bool)
    while True:
        deg = A[np.ix_(keep, keep)].sum(1)
        drop = deg < 2
        if not drop.any():
            break
        kidx = np.where(keep)[0]
        keep[kidx[drop]] = False
        if not keep.any():
            break
    return {int(idx[k]) for k in np.where(keep)[0]}


def scc_nodes(Wl, alive, min_size=2):
    """nodes belonging to SCCs of size >= min_size in the Wl support digraph."""
    edges = [(i, j) for (i, j), w in Wl.items()
             if w > 0 and alive[i] and alive[j]]
    if not edges:
        return set()
    nodes = sorted({i for e in edges for i in e})
    pos = {v: k for k, v in enumerate(nodes)}
    n = len(nodes)
    A = np.zeros((n, n), dtype=bool)
    for (i, j) in edges:
        A[pos[i], pos[j]] = True
    ncomp, lab = connected_components(A, directed=True, connection='strong')
    size = np.bincount(lab, minlength=ncomp)
    return {v for v in nodes if size[lab[pos[v]]] >= min_size}


def edge_set_H(H, alive, eps=1e-12):
    """frozen set of undirected support pairs (i<j) on H at eps."""
    idx = np.where(alive)[0]
    if idx.size == 0:
        return set()
    A = (H > eps) | (H.T > eps)
    live = np.zeros(NMAX, dtype=bool)
    live[idx] = True
    iu, ju = np.where(np.triu(A, 1))
    return {(int(a), int(b)) for a, b in zip(iu, ju) if live[a] and live[b]}


# ----------------------------------------------------------------------
# dimension instruments (identical fits to v24, plus diagnostics)
# ----------------------------------------------------------------------
def dual_dims(D, n):
    fin = np.isfinite(D) & (D > 0)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    bd = kd = np.nan
    b = kraw = np.nan
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
    return bd, kd, b, kraw


def panel(S, ngrown):
    """v24 phase classifier with unselective fit diagnostics.
    Label logic is IDENTICAL to v24. Extra returns never feed back.
    Returns (ph, medC, d_cal, bd, kd, diag) with diag =
      dict(gcf, npts, slope, r2, fail, bd_all, kd_all)
    fail in {None, NO_GIANT, DEGENERATE_NN, FEW_RADII, NO_SCALING_PTS}."""
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
    diag = dict(gcf=float(gcf), npts=0, slope=np.nan, r2=np.nan, fail=None,
                bd_all=np.nan, kd_all=np.nan, wscale=np.nan, wcont=np.nan)
    nn = []
    for i in range(n):
        v = D[i][fin[i]]
        if v.size: nn.append(v.min())
    d_cal = np.nan
    if n < 3:
        diag['fail'] = "NO_GIANT"
    elif not nn:
        diag['fail'] = "DEGENERATE_NN"
    else:
        unit = np.median(nn); rs = unit*np.arange(1, 40)
        counts = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs])
        sel = (counts > 5) & (counts < 0.5*n)
        diag['npts'] = int(sel.sum())
        if sel.sum() >= 2:
            diag['wscale'] = float(np.log(rs[sel].max()/rs[sel].min()))
        # continuous width: interpolated crossings on a fine geometric grid
        # (pure read; label pipeline above is untouched)
        rs_f = unit * (1.1 ** np.arange(0, 41))
        cf = np.array([((D <= r) & np.isfinite(D)).sum(1).mean() for r in rs_f])
        lo_ok = cf > 5; hi_ok = cf < 0.5*n
        if lo_ok.any() and hi_ok.any():
            i_lo = int(np.argmax(lo_ok))          # first crossing above 5
            i_hi = int(len(cf) - 1 - np.argmax(hi_ok[::-1]))  # last below 0.5n
            def _x(i0, i1, thr):
                c0, c1 = cf[i0], cf[i1]
                if c1 == c0: return rs_f[i0]
                t = (thr - c0) / (c1 - c0)
                return float(np.exp(np.log(rs_f[i0]) + t*(np.log(rs_f[i1]) - np.log(rs_f[i0]))))
            r_lo = _x(i_lo-1, i_lo, 5.0) if i_lo > 0 else rs_f[0]
            r_hi = _x(i_hi, i_hi+1, 0.5*n) if i_hi < len(cf)-1 else rs_f[-1]
            if r_hi > r_lo:
                diag['wcont'] = float(np.log(r_hi/r_lo))
        if sel.sum() >= 4:
            x, y = np.log(rs[sel]), np.log(counts[sel])
            bd = float(np.polyfit(x, y, 1)[0])
            yy = np.polyval(np.polyfit(x, y, 1), x)
            ss_res = float(((y-yy)**2).sum()); ss_tot = float(((y-y.mean())**2).sum())
            diag['slope'] = bd
            diag['r2'] = 1.0 - ss_res/ss_tot if ss_tot > 0 else np.nan
            m = np.array([0.91,1.70,2.20]); t = np.array([1.,2.,3.])
            if bd > m[-1]: d_cal = t[-1]+(bd-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2])
            elif bd < m[0]: d_cal = t[0]+(bd-m[0])*(t[1]-t[0])/(m[1]-m[0])
            else: d_cal = float(np.interp(bd, m, t))
        else:
            diag['fail'] = "FEW_RADII" if sel.sum() > 0 else "NO_SCALING_PTS"
    # v24 label logic, unchanged
    if gcf < 0.6: ph = "FRAG"
    elif medC > 0.9: ph = "SAT"
    elif not np.isfinite(d_cal): ph = "SW"
    else: ph = "METR"
    # dual dims in ALL phases (sec 9.2), read-only
    if n >= 3:
        bd2, kd2, _, _ = dual_dims(D, n)
        diag['bd_all'], diag['kd_all'] = bd2, kd2
    if ph == "METR":
        return ph, medC, d_cal, diag['bd_all'], diag['kd_all'], diag
    return ph, medC, d_cal, np.nan, np.nan, diag


def support_weights(S):
    """Return -log(S) weights on the same support graph used by panel()."""
    Sc = np.clip(S, 1e-12, 1 - 1e-12)
    mask = Sc > LINK_EPS
    np.fill_diagonal(mask, False)
    if not mask.any():
        return np.array([])
    return -np.log(Sc[mask])


# ----------------------------------------------------------------------
# model (dynamics identical to v24; instruments are pure reads/counts)
# ----------------------------------------------------------------------
def run(seed, lam, gamma, directed, epochs=300, protect=False):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX)); C = np.zeros((NMAX, NMAX))
    Wl = {}
    alive = np.zeros(NMAX, dtype=bool)
    free = list(range(NMAX-1, -1, -1))
    kappa = gamma
    nsub = ndead = ndyad = 0
    audit_ok = True
    snaps = []; asym_hist = []
    bsw_weights = []
    evledger = Counter(); decledger = Counter(); deathledger = Counter()
    # --- v24.1 instruments state ---
    refl_count = 0                 # reflection fallbacks since last snapshot
    ndst_list = []                 # len(dst) per event since last snapshot
    evap_count = 0                 # H-support edge deaths since last snapshot
    refl_hist = []                 # (epoch, count in inter-snapshot period)
    edge_birth = {}                # (i<j) -> birth epoch, H-support 1e-12
    edge_lifetimes = []            # completed lifetimes (epochs)
    prev_edges = set()
    inst = []                      # per-snapshot instrument records

    def outgoing(j, exclude=None):
        nb = np.where(((H[j, :] > 1e-12) | (H[:, j] > 1e-12)) & alive)[0]
        return [(j, int(k)) for k in nb if k != j and (exclude is None or k != exclude)]

    for ep in range(epochs):
        events = []
        for L, w in list(Wl.items()):
            i, j = L
            if not (alive[i] and alive[j]) or H[i, j] <= 1e-12:
                continue
            k = rng.poisson(w)
            events += [L]*int(k)
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
                H[a, b] = 1.0
                _va, _ea, _ca, _b1a = betti1_support(H, alive)
                evledger[("DYAD", _va-_vb, _ea-_eb, _b1a-_b1b)] += 1
                events.append((a, b)); ndyad += 1
        else:
            L = live_links[rng.integers(len(live_links))]
            events.append(L)
        if len(events) > 100_000:
            return ("RUNAWAY", snaps, asym_hist, nsub, ndead, audit_ok,
                    evledger, decledger, deathledger, inst, refl_hist, edge_lifetimes, edge_birth, ep)
        Wnext = {}
        rng.shuffle(events)
        for (i, j) in events:
            if not (alive[i] and alive[j]): continue
            c = 0.5*(C[i, j] + C[j, i])
            if rng.random() < c and (free or TRULE == "T3"):
                _vb, _eb, _cb, _b1b = betti1_support(H, alive)
                _lab = None
                if TRULE == "T1":
                    a = free.pop(); alive[a] = True
                    H[i, a] += 1.0; H[a, j] += 1.0
                    nsub += 1; dst = outgoing(a); _lab = "T1"
                elif TRULE == "T2":
                    a = free.pop(); alive[a] = True
                    H[i, a] += 1.0
                    nsub += 1; dst = outgoing(a); _lab = "T2"
                else:
                    common = np.where((H[i,:]+H[:,i] > 1e-12) & (H[j,:]+H[:,j] > 1e-12) & alive)[0]
                    common = [int(k) for k in common if k != i and k != j]
                    if common:
                        k2 = int(rng.choice(common))
                        H[i, j] += 1.0
                        nsub += 1; dst = outgoing(j, exclude=i) or [(j, i)]; _lab = "T3_main"
                    else:
                        if not free: continue
                        a = free.pop(); alive[a] = True
                        H[i, a] += 1.0; H[a, j] += 1.0
                        nsub += 1; dst = outgoing(a); _lab = "T3_fallback"
                if _lab is not None:
                    _va, _ea, _ca, _b1a = betti1_support(H, alive)
                    evledger[(_lab, _va-_vb, _ea-_eb, _b1a-_b1b)] += 1
            else:
                _existed = (H[i, j] > 1e-12) or (H[j, i] > 1e-12)
                if _existed:
                    H[i, j] += (1.0 - c)
                    evledger[("REG", 0, 0, 0)] += 1
                else:
                    _vb, _eb, _cb, _b1b = betti1_support(H, alive)
                    H[i, j] += (1.0 - c)
                    _va, _ea, _ca, _b1a = betti1_support(H, alive)
                    evledger[("REG", _va-_vb, _ea-_eb, _b1a-_b1b)] += 1
                if directed:
                    dst = outgoing(j, exclude=i)
                    if not dst:
                        dst = [(j, i)]           # reflection
                        refl_count += 1          # instrument: pure count
                else:
                    dst = outgoing(i) + outgoing(j)
            if not dst: continue
            ndst_list.append(len(dst))
            cw = np.array([max(C[a_, b_], 1e-9) for (a_, b_) in dst])
            sh = cw/cw.sum()
            for L, s in zip(dst, sh):
                Wnext[L] = Wnext.get(L, 0.0) + s
        nvalid = len([e for e in events if alive[e[0]] and alive[e[1]]])
        if events and abs(sum(Wnext.values()) - nvalid) > 1 + 0.05*len(events):
            audit_ok = False
        Wl = Wnext
        num = den = 0.0
        seen = set()
        for (i, j), w in Wl.items():
            if (j, i) in seen or (i, j) in seen: continue
            seen.add((i, j))
            w2 = Wl.get((j, i), 0.0)
            num += abs(w - w2); den += w + w2
        asym_hist.append(num/den if den > 0 else 0.0)
        _vb_d, _eb_d, _cb_d, _b1b_d = betti1_support(H, alive)
        if protect:
            idx0 = np.where(alive)[0]
            Cn = C[np.ix_(idx0, idx0)]
            mx = Cn.max()
            Chat = Cn/mx if mx > 1e-12 else Cn
            n0 = len(idx0)
            M = np.zeros((n0, n0))
            for k_ in range(n0):
                M = np.maximum(M, np.minimum(Chat[:, k_][:, None], Chat[k_, :][None, :]))
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
        # --- v24.1: edge lifetime ledger (H-support, theta=1e-12) ---
        cur_edges = edge_set_H(H, alive)
        for e in cur_edges - prev_edges:
            edge_birth[e] = ep
        for e in prev_edges - cur_edges:
            edge_lifetimes.append(ep - edge_birth.pop(e))
            evap_count += 1
        prev_edges = cur_edges
        # --- snapshots ---
        if (ep + 1) in SNAPS:
            d_cal = bd = kd = np.nan
            idx2 = np.where(alive)[0]
            if len(idx2) >= 3:
                Sm = 0.5*(C + C.T)
                Amat = 0.5*(C - C.T)
                Sn = Sm[np.ix_(idx2, idx2)]; An = Amat[np.ix_(idx2, idx2)]
                Adj = Sn > LINK_EPS
                num = den = 0.0; ntri = 0
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
                ph, medC, d_cal, bd, kd, diag = panel(Sn, len(idx2))
                if ph == "METR" and diag['npts'] >= 5:
                    bsw_weights.extend(support_weights(Sn).tolist())
                snaps.append((ep+1, ph, medC, d_cal, bd, kd, phic, ntri))
                brfrac, occ2ecc, E_S, kmean = redundancy_stats(Sn)
            else:
                ph, diag = "DEAD", dict(gcf=np.nan, npts=0, slope=np.nan,
                                        r2=np.nan, fail=None,
                                        bd_all=np.nan, kd_all=np.nan)
                snaps.append((ep+1, "DEAD", np.nan, np.nan, np.nan, np.nan, np.nan, 0))
                brfrac = occ2ecc = E_S = kmean = np.nan
            # multi-support b1 + directed instruments (pure reads)
            _, _, _, b1_H12 = betti1_support(H, alive, eps=1e-12)
            _, _, _, b1_H6 = betti1_support(H, alive, eps=1e-6)
            b1_S6 = betti1_matrix(C, alive, eps=LINK_EPS)
            b1_S12 = betti1_matrix(C, alive, eps=1e-12)
            sc = scc_stats(Wl, alive, NMAX)
            sccN = scc_nodes(Wl, alive, min_size=2)
            core2 = two_core_nodes(H, alive, eps=1e-12)
            r12 = (len(sccN & core2)/len(sccN)) if sccN else np.nan
            nd = np.array(ndst_list, float) if ndst_list else np.array([np.nan])
            inst.append(dict(ep=ep+1, ph=ph, diag=diag,
                             b1_H12=b1_H12, b1_H6=b1_H6,
                             b1_S12=b1_S12, b1_S6=b1_S6,
                             d_cal=d_cal, bd=bd, kd=kd,
                             rung12=r12,
                             ndst_mean=float(np.nanmean(nd)),
                             ndst_p90=float(np.nanpercentile(nd, 90)) if ndst_list else np.nan,
                             evapE=evap_count,
                             E_S=E_S if np.isfinite(np.asarray(E_S, float)) else np.nan,
                             kmean=kmean, brfrac=brfrac, occ2ecc=occ2ecc,
                             V=int(alive.sum()), refl=refl_count, **sc))
            refl_hist.append((ep+1, refl_count)); refl_count = 0
            ndst_list = []; evap_count = 0
    return ("ok", snaps, asym_hist, nsub, ndead, audit_ok,
            evledger, decledger, deathledger, inst, refl_hist, edge_lifetimes,
            edge_birth, epochs, bsw_weights)


# ----------------------------------------------------------------------
# reporting
# ----------------------------------------------------------------------
def windows_and_exits(snaps):
    """BSW windows + exit reason (label right after the window)."""
    wins = []
    cur = []
    for k, s in enumerate(snaps):
        if s[1] == "METR":
            cur.append((k, s))
        else:
            if cur:
                wins.append((cur, snaps[k][1]))
                cur = []
    if cur:
        wins.append((cur, "END"))
    return wins


def pearson(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 3: return np.nan
    x, y = x[m], y[m]
    if x.std() == 0 or y.std() == 0: return np.nan
    return float(np.corrcoef(x, y)[0, 1])


def report(tag, out):
    (status, snaps, asym, nsub, ndead, audit,
     evl, decl, deathl, inst, refl_hist, lifetimes, births, ep_end,
     bsw_weights) = out
    wins = windows_and_exits(snaps)
    occ = sum(len(w) for w, _ in wins)
    vmax = max((r['V'] for r in inst), default=0)
    sat = [r['ep'] for r in inst if r['V'] >= NMAX]
    print(f"[{tag}] status={status} snaps={len(snaps)} BSW_occ={occ} "
          f"windows={len(wins)} dead={ndead} audit={'OK' if audit else 'FAIL'} "
          f"V_max={vmax}/{NMAX} first_sat={sat[0] if sat else '-'}"
          + ("  *** HEADROOM WARNING: V_max >= 0.95*NMAX ***" if vmax >= 0.95*NMAX else ""))
    # per-snapshot instrument table
    print(f"    ep    ph    V  b1_H12 b1_H6 b1_S12 b1_S6  occSCC3 feCYC rung12 refl ndstM evapE  E_S  kmean brfrac occ2ecc  gcf  npts wscale wcont slope   r2    fail")
    for r in inst:
        d = r['diag']
        eS = int(r['E_S']) if np.isfinite(np.asarray(r.get('E_S', np.nan), float)) else -1
        print(f"    {r['ep']:4d} {r['ph']:>5s} {r['V']:4d}  "
              f"{r['b1_H12']:5d} {r['b1_H6']:5d} {r['b1_S12']:5d} {r['b1_S6']:5d}  "
              f"{_f(r['occ_scc3'])} {_f(r['fe_cyc'])} {_f(r['rung12'])} {r['refl']:5d} {_f(r['ndst_mean'])} "
              f"{r['evapE']:5d} {eS:5d} {_f(r['kmean'])} {_f(r['brfrac'])} {_f(r['occ2ecc'])}  "
              f"{_f(d['gcf'])} {d['npts']:4d} {_f(d['wscale'])} {_f(d['wcont'])} {_f(d['slope'])} {_f(d['r2'])}  "
              f"{d['fail'] or '-'}")
    # windows + exit reasons
    exit_ctr = Counter()
    for w, ex in wins:
        span = f"ep{w[0][1][0]}-{w[-1][1][0]}"
        exit_ctr[ex] += 1
        print(f"    window {span} len={len(w)} exit={ex}")
    print(f"    exit reasons: {dict(exit_ctr) if exit_ctr else '(no windows)'}")
    # SW breakdown
    sw = Counter(r['diag']['fail'] for r in inst if r['ph'] == 'SW')
    print(f"    SW breakdown: {dict(sw) if sw else '(no SW snapshots)'}")
    # edge lifetimes
    lt = np.array(lifetimes, float)
    cens = len(births)
    if lt.size:
        print(f"    edge lifetimes (theta=1e-12): n_dead={lt.size} "
              f"median={np.median(lt):.0f} mean={lt.mean():.1f} "
              f"p90={np.percentile(lt,90):.0f} max={lt.max():.0f} "
              f"censored_alive={cens}")
    else:
        print(f"    edge lifetimes: none completed; censored_alive={cens}")
    # coupling pre-test (unselective: report all, directed instruments primary)
    bsw = [1.0 if r['ph'] == 'METR' else 0.0 for r in inst]
    print(f"    coupling with BSW indicator (point-biserial):")
    for key in ('occ_scc3', 'fe_cyc', 'occ_scc', 'fe_dyad', 'rung12',
                'b1_H12', 'b1_H6', 'b1_S12', 'b1_S6',
                'evapE', 'kmean', 'brfrac', 'occ2ecc'):
        vals = [r[key] for r in inst]
        print(f"      {key:8s}: r = {_f(pearson(vals, bsw))}")
    # coupling with continuous scaling width (sec 5.3: BSW as thresholded W_scale)
    for target, tname in (([r['diag']['npts'] for r in inst], 'npts'),
                          ([r['diag']['wcont'] for r in inst], 'wcont')):
        print(f"    coupling with {tname}(t) (Pearson):")
        for key in ('occ_scc3', 'fe_cyc', 'b1_H12', 'b1_S6', 'rung12',
                    'evapE', 'kmean', 'brfrac', 'occ2ecc'):
            vals = [r[key] for r in inst]
            print(f"      {key:8s}: r = {_f(pearson(vals, target))}")
    # pre-registered discrimination (sec 12): redundancy inside contraction BSW
    vs = [(r['ep'], r['V']) for r in inst]
    if vs:
        pk = max(vs, key=lambda t: t[1])[0]
        cb = [r for r in inst if r['ep'] > pk and r['ph'] == 'METR']
        cn = [r for r in inst if r['ep'] > pk and r['ph'] != 'METR']
        def med(rows, k):
            v = np.array([x[k] for x in rows], float)
            v = v[np.isfinite(v)]
            return f"{np.median(v):5.3f}(n={len(v)})" if v.size else "   - (n=0)"
        print(f"    DISCRIMINATION (contraction, V_peak@ep{pk}):")
        print(f"      occ2ecc  BSW: {med(cb,'occ2ecc')}  non-BSW: {med(cn,'occ2ecc')}")
        print(f"      brfrac   BSW: {med(cb,'brfrac')}  non-BSW: {med(cn,'brfrac')}")
        print(f"      kmean    BSW: {med(cb,'kmean')}  non-BSW: {med(cn,'kmean')}")
    # H->S geometrization lag (sec 9.3): corr(b1_H(t), b1_S(t+tau))
    bh = np.array([r['b1_H12'] for r in inst], float)
    bs = np.array([r['b1_S6'] for r in inst], float)
    dh = np.diff(bh)
    print(f"    H->S lag correlation corr(b1_H12(t), b1_S6(t+tau)) [tau in snapshots]:")
    row_all, row_up, row_dn = [], [], []
    for tau in range(-3, 4):
        if tau >= 0:
            x, y = bh[:len(bh)-tau or None], bs[tau:]
        else:
            x, y = bh[-tau:], bs[:tau]
        row_all.append(pearson(x, y))
        if tau >= 0:
            mm = min(len(bh) - tau, len(dh))
            if mm >= 3:
                xh, ys = bh[:mm], bs[tau:tau+mm]
                up = dh[:mm] > 0; dn = dh[:mm] < 0
                row_up.append(pearson(xh[up], ys[up]) if up.sum() >= 3 else np.nan)
                row_dn.append(pearson(xh[dn], ys[dn]) if dn.sum() >= 3 else np.nan)
            else:
                row_up.append(np.nan); row_dn.append(np.nan)
    print("      all    : " + " ".join(_f(v) for v in row_all) + "   (tau=-3..3)")
    print("      rising : " + " ".join(_f(v) for v in row_up) + "   (tau=0..3, b1_H increasing)")
    print("      falling: " + " ".join(_f(v) for v in row_dn) + "   (tau=0..3, b1_H decreasing)")
    return dict(inst=inst, wins=wins, evl=evl, decl=decl, deathl=deathl,
                bsw_weights=bsw_weights)


def write_run_exports(prefix, rep):
    with open(prefix + "_snapshots.tsv", "w") as fo:
        fo.write("epoch\tV\tb1H\tb1S\tlabel\tnpts\td_cal\tslope\twcont\tocc2ecc\n")
        for r in rep['inst']:
            d = r['diag']
            fo.write(
                f"{r['ep']}\t{r['V']}\t{r['b1_H12']}\t{r['b1_S6']}\t"
                f"{r['ph']}\t{d['npts']}\t{r.get('d_cal', np.nan)}\t"
                f"{d.get('slope', np.nan)}\t{d.get('wcont', np.nan)}\t"
                f"{r.get('occ2ecc', np.nan)}\n"
            )
    with open(prefix + "_bsw_weights.txt", "w") as fo:
        for w in rep['bsw_weights']:
            fo.write(f"{w:.17g}\n")
    print(f"    -> {prefix}_snapshots.tsv")
    print(f"    -> {prefix}_bsw_weights.txt (robust BSW weights n={len(rep['bsw_weights'])})")


def _f(x):
    return f"{x:5.2f}" if (x is not None and np.isfinite(x)) else "   - "


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


# ----------------------------------------------------------------------
if __name__ == "__main__":
    lam = 0.9
    g = float(sys.argv[1])
    epochs = int(sys.argv[2])
    seeds = [int(s) for s in sys.argv[3].split(",")]
    if len(sys.argv) > 4: NMAX = int(sys.argv[4])
    TRULE = sys.argv[5] if len(sys.argv) > 5 else 'T1'
    SNAPS = tuple(range(10, epochs + 1, 10))

    EV = Counter(); DEC = Counter(); DX = Counter()
    for seed in seeds:
        print("=" * 100)
        print(f"SEED {seed}  rule={TRULE} g={g} N={NMAX} epochs={epochs} "
              f"(paired directed / symmetric, identical seed)")
        print("=" * 100)
        out_d = run(seed, lam, g, True, epochs=epochs, protect=False)
        rep_d = report("directed ", out_d)
        write_run_exports(f"v24_2e_directed_g{g}_s{seed}", rep_d)
        EV.update(out_d[6]); DEC.update(out_d[7]); DX.update(out_d[8])
        out_s = run(seed, lam, g, False, epochs=epochs, protect=False)
        rep_s = report("symmetric", out_s)
        write_run_exports(f"v24_2e_symmetric_g{g}_s{seed}", rep_s)
        # asymmetric prediction pre-test summary (sec 2.2)
        print(f"    --- asymmetric prediction pre-test (directed minus symmetric, "
              f"point-biserial r with BSW) ---")
        for key in ('occ_scc3', 'fe_cyc', 'b1_H12'):
            rd = pearson([r[key] for r in rep_d['inst']],
                         [1.0 if r['ph'] == 'METR' else 0.0 for r in rep_d['inst']])
            rs = pearson([r[key] for r in rep_s['inst']],
                         [1.0 if r['ph'] == 'METR' else 0.0 for r in rep_s['inst']])
            d_ = (rd - rs) if np.isfinite(rd) and np.isfinite(rs) else np.nan
            print(f"      {key:8s}: r_dir={_f(rd)}  r_sym={_f(rs)}  diff={_f(d_)}")

    print("\n" + "=" * 72)
    print(f"AGGREGATE (directed runs)  rule={TRULE} g={g} N={NMAX} epochs={epochs} seeds={seeds}")
    print("=" * 72)
    show_ledger("REGISTRATION EVENTS (label, dV, dE, db1)", EV)
    show_ledger("DECAY per-epoch  H*=(1-g)", DEC)
    show_ledger("DEATH per-epoch  isolated removal", DX)
