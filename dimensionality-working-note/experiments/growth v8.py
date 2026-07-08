"""v8: homogenization via the non-closure barrier (saturation).

Canonical sources: aDelta(1-C/C*) diffusion and -kappa_B/(Cmax-C) barrier.
Implemented minimally:
  - saturating registration: dH = (1 - Cs[w,tgt])  -- a saturated link cannot
    register new difference (difference already maximal registers nothing)
  - saturation-driven branching: pb_eff = pb * sat(w), sat(w) = mean C of w's
    existing links -- when local capacity is exhausted, difference spills
    into the creation of a NEW node (growth at the frontier)
Measure: ball_d (calibrated) + heterogeneity CV of local mass N_i(r*).
Control: v6-style rule (constant dH, constant pb) same seeds.
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

LAM = 1.0; GAMMA = 0.02; EPOCHS = 18; EV = 3000
NMAX = 900; LWIN = 50

def solve_rho(H, lam, iters=600):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rn = (1 - np.exp(-lam*rho[:,None]*H)).sum(1)
        if np.allclose(rn, rho, atol=1e-12): break
        rho = 0.5*rho + 0.5*rn
    return rho

def geodesic(S):
    Sc = np.clip(S, 1e-12, 1-1e-12)
    W = -np.log(Sc); np.fill_diagonal(W, 0.0)
    W[Sc < 1e-6] = 0.0
    nc, lab = connected_components((W > 0), directed=False)
    if nc > 1:
        big = np.bincount(lab).argmax()
        W = W[np.ix_(lab == big, lab == big)]
    return shortest_path(W, method='D', directed=False)

def ball_metrics(D):
    n = D.shape[0]; fin = np.isfinite(D)
    nn = []
    for i in range(n):
        v = D[i][fin[i] & (D[i] > 0)]
        if v.size: nn.append(v.min())
    if not nn: return np.nan, np.nan
    unit = np.median(nn)
    rs = unit * np.arange(1, 40)
    counts = np.array([((D <= r) & fin).sum(1).mean() for r in rs])
    sel = (counts > 5) & (counts < 0.5*n)
    if sel.sum() < 4: return np.nan, np.nan
    bd = float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])
    # heterogeneity: CV of per-node mass at the mid-window radius
    rmid = rs[sel][len(rs[sel])//2]
    Ni = ((D <= rmid) & fin).sum(1)
    cv = float(Ni.std()/Ni.mean())
    return bd, cv

def calib_ball(b):
    m = np.array([0.91, 1.70, 2.20]); t = np.array([1., 2., 3.])
    if not np.isfinite(b): return np.nan
    if b > m[-1]: return float(t[-1] + (b-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2]))
    if b < m[0]:  return float(t[0] + (b-m[0])*(t[1]-t[0])/(m[1]-m[0]))
    return float(np.interp(b, m, t))

def run(seed, pb, pc, lag, saturating):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    n = 2; H[0,1] = H[1,0] = 1.0
    w = 0; traj = [0, 1]
    rho = solve_rho(H[:n,:n], LAM)
    for ep in range(EPOCHS):
        C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
        Cs = 0.5*(C + C.T)
        m0 = Cs.shape[0]
        deg0 = (Cs > 1e-6).sum(1)
        sat0 = np.where(deg0 > 0, Cs.sum(1)/np.maximum(deg0,1), 0.0)
        for _ in range(EV):
            u = rng.random()
            pb_eff = pb
            if u < pb_eff and n < NMAX:
                H[w, n] += 1.0; H[n, w] += 1.0
                w = n; n += 1
            elif u < pb_eff + pc and len(traj) > lag + 1:
                tgt = int(traj[-lag])
                if tgt != w:
                    c = Cs[w, tgt] if (w < Cs.shape[0] and tgt < Cs.shape[0]) else 0.0
                    dH = (1.0 - c) if saturating else 1.0
                    H[w, tgt] += dH; H[tgt, w] += dH
            else:
                m_ = Cs.shape[0]
                p = np.zeros(n)
                if w < m_: p[:m_] = Cs[w, :m_]
                p += 1e-9 * (H[w,:n] + H[:n,w])
                if saturating and m_ > 0:
                    # diffusion flux: flow prefers targets with free capacity
                    p[:m0] *= (1.0 - np.clip(sat0, 0, 1)) + 0.05
                p[w] = 0.0
                ss = p.sum()
                if ss < 1e-12:
                    nb = np.where(H[w,:n]+H[:n,w] > 0)[0]; nb = nb[nb != w]
                    nxt = int(rng.choice(nb)) if len(nb) else w
                else:
                    nxt = int(rng.choice(n, p=p/ss))
                c = Cs[w, nxt] if (w < Cs.shape[0] and nxt < Cs.shape[0]) else 0.0
                dH = (1.0 - c) if saturating else 1.0
                H[w, nxt] += dH
                w = nxt
            traj.append(w)
            if len(traj) > 4*LWIN: traj = traj[-2*LWIN:]
        H[:n,:n] *= (1.0-GAMMA)
        rho = solve_rho(H[:n,:n], LAM)
    C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
    D = geodesic(0.5*(C+C.T))
    bd, cv = ball_metrics(D)
    return calib_ball(bd), cv, D.shape[0], n

print("mode        cond              seeds: d_cal (CV)            mean d_cal, mean CV")
for saturating in (False, True):
    tag = "SATURATING" if saturating else "control   "
    for pb, pc, lag in ((0.3, 0.0, 12), (0.3, 0.1, 6)):
        ds, cvs = [], []
        parts = []
        for seed in (5, 6, 7):
            d, cv, gc, n = run(seed, pb, pc, lag, saturating)
            ds.append(d); cvs.append(cv)
            parts.append(f"{d:5.2f}({cv:4.2f})")
        ds = np.array([x for x in ds if np.isfinite(x)])
        cvs = np.array([x for x in cvs if np.isfinite(x)])
        print(f"{tag} pb={pb} pc={pc} lag={lag}: " + " ".join(parts) +
              f"   -> d={ds.mean():5.2f}+-{ds.std():4.2f}  CV={cvs.mean():4.2f}")
