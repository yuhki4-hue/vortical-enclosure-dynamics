"""v7: ball-growth instrument applied to the v6 growth model.
Calibration (kNN sparse, section 5.11): ball_d 0.91/1.70/2.20 <-> true 1/2/3.
Main: pure tree + LAG sweep, multi-seed, final-epoch measurement."""
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
    ncomp, lab = connected_components((W > 0), directed=False)
    if ncomp > 1:
        big = np.bincount(lab).argmax()
        W = W[np.ix_(lab == big, lab == big)]
    return shortest_path(W, method='D', directed=False)

def ball_dimension(D):
    n = D.shape[0]
    fin = np.isfinite(D)
    nn = []
    for i in range(n):
        v = D[i][fin[i] & (D[i] > 0)]
        if v.size: nn.append(v.min())
    if not nn: return np.nan
    unit = np.median(nn)
    rs = unit * np.arange(1, 40)
    counts = np.array([((D <= r) & fin).sum(1).mean() for r in rs])
    sel = (counts > 5) & (counts < 0.5 * n)
    if sel.sum() < 4: return np.nan
    return float(np.polyfit(np.log(rs[sel]), np.log(counts[sel]), 1)[0])

def calib_ball(b):
    m = np.array([0.91, 1.70, 2.20]); t = np.array([1., 2., 3.])
    if not np.isfinite(b): return np.nan
    if b > m[-1]:
        return float(t[-1] + (b - m[-1]) * (t[-1]-t[-2]) / (m[-1]-m[-2]))
    if b < m[0]:
        return float(t[0] + (b - m[0]) * (t[1]-t[0]) / (m[1]-m[0]))
    return float(np.interp(b, m, t))

def run(seed, pb, pc, lag):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    n = 2; H[0,1] = H[1,0] = 1.0
    w = 0; traj = [0, 1]
    rho = solve_rho(H[:n,:n], LAM)
    for ep in range(EPOCHS):
        C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
        Cs = 0.5*(C + C.T)
        for _ in range(EV):
            u = rng.random()
            if u < pb and n < NMAX:
                H[w, n] += 1.0; H[n, w] += 1.0
                w = n; n += 1
            elif u < pb + pc and len(traj) > lag + 1:
                tgt = int(traj[-lag])
                if tgt != w:
                    H[w, tgt] += 1.0; H[tgt, w] += 1.0
            else:
                m_ = Cs.shape[0]
                p = np.zeros(n)
                if w < m_: p[:m_] = Cs[w, :m_]
                p += 1e-9 * (H[w,:n] + H[:n,w])
                p[w] = 0.0
                ss = p.sum()
                if ss < 1e-12:
                    nb = np.where(H[w,:n]+H[:n,w] > 0)[0]; nb = nb[nb != w]
                    nxt = int(rng.choice(nb)) if len(nb) else w
                else:
                    nxt = int(rng.choice(n, p=p/ss))
                H[w, nxt] += 1.0
                w = nxt
            traj.append(w)
            if len(traj) > 4*LWIN: traj = traj[-2*LWIN:]
        H[:n,:n] *= (1.0-GAMMA)
        rho = solve_rho(H[:n,:n], LAM)
    C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
    D = geodesic(0.5*(C+C.T))
    return ball_dimension(D), D.shape[0]

print("condition                | ball_d per seed -> d_cal (giant comp)")
print("pure tree pb=0.3 pc=0:")
vals = []
for seed in (5, 6, 7, 8):
    b, gc = run(seed, 0.3, 0.0, 12)
    vals.append(calib_ball(b))
    print(f"  seed {seed}: ball={b:.3f} -> d_cal={calib_ball(b):.2f} (gc={gc})")
v = np.array(vals)
print(f"  => tree: d_cal = {v.mean():.2f} +- {v.std():.2f}")

for lag in (4, 6, 9, 12, 18):
    vals = []
    for seed in (5, 6, 7):
        b, gc = run(seed, 0.3, 0.1, lag)
        vals.append(calib_ball(b))
    v = np.array([x for x in vals if np.isfinite(x)])
    fv = ", ".join(f"{x:.2f}" for x in vals)
    print(f"LAG={lag:2d} pc=0.1: d_cal seeds [{fv}]  mean {v.mean():.2f} +- {v.std():.2f}")
