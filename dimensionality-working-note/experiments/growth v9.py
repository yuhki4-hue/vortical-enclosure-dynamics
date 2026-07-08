"""v9: generative geometry + PARALLEL registration (partial order).

Every node hosts a flow (walker count = node count; a new node is born
carrying its own flow). Per tick, ALL flows act simultaneously under the
epoch-frozen C. Within a tick, H updates are additive hence commutative:
registration order inside a tick has no physical content -- a genuine
partial order replaces the global serial clock of v1-v8.
Rules per flow per tick: branch (pb) / close onto OWN log at fixed lag (pc)
/ move along C and register (else). Same primitives as v6, de-serialized.
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path, connected_components

LAM = 0.1; GAMMA = 0.5
NMAX = 900; LAG = 6
TOTAL_EVENTS = 54_000        # matched to v6 (18 x 3000)
EVENTS_PER_EPOCH = 3_000     # decay + rho cadence, matched to v6

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
    rmid = rs[sel][len(rs[sel])//2]
    Ni = ((D <= rmid) & fin).sum(1)
    return bd, float(Ni.std()/Ni.mean())

def calib_ball(b):
    m = np.array([0.91, 1.70, 2.20]); t = np.array([1., 2., 3.])
    if not np.isfinite(b): return np.nan
    if b > m[-1]: return float(t[-1] + (b-m[-1])*(t[-1]-t[-2])/(m[-1]-m[-2]))
    if b < m[0]:  return float(t[0] + (b-m[0])*(t[1]-t[0])/(m[1]-m[0]))
    return float(np.interp(b, m, t))

def run(seed, pb, pc, lag):
    rng = np.random.default_rng(seed)
    H = np.zeros((NMAX, NMAX))
    n = 2; H[0,1] = H[1,0] = 1.0
    pos = [0, 1]                       # walker b sits at pos[b]; b indexes nodes
    logs = [[0], [1]]                  # each flow's own trajectory log
    rho = solve_rho(H[:n,:n], LAM)
    ev_count = 0; ev_epoch = 0
    C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
    while ev_count < TOTAL_EVENTS:
        order = rng.permutation(n)     # tick: all flows act; order physically void
        for b in order:
            if ev_count >= TOTAL_EVENTS: break
            u = rng.random()
            w = pos[b]
            if u < pb and n < NMAX:
                H[w, n] += 1.0; H[n, w] += 1.0
                pos[b] = n
                pos.append(n); logs.append([n])   # new node carries a new flow
                logs[b].append(n)
                n += 1
            elif u < pb + pc and len(logs[b]) > lag + 1:
                tgt = int(logs[b][-lag])
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
                pos[b] = nxt
                logs[b].append(nxt)
                if len(logs[b]) > 200: logs[b] = logs[b][-100:]
            ev_count += 1; ev_epoch += 1
            if ev_epoch >= EVENTS_PER_EPOCH:
                H[:n,:n] *= (1.0-GAMMA)
                rho = solve_rho(H[:n,:n], LAM)
                C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n]); Cs = 0.5*(C+C.T)
                ev_epoch = 0
    rho = solve_rho(H[:n,:n], LAM)
    C = 1 - np.exp(-LAM*rho[:,None]*H[:n,:n])
    D = geodesic(0.5*(C+C.T))
    bd, cv = ball_metrics(D)
    return calib_ball(bd), cv, D.shape[0], n

print("v9 parallel registration (flow per node, tick-synchronous, frozen C)")
print("serial v6/v7 baseline: tree d=0.71+-0.08 CV=0.68 | lag6 d=0.67+-0.50 CV=0.89")
for pb, pc, lag in ((0.02, 0.0, 6), (0.02, 0.02, 6), (0.02, 0.05, 6)):
    ds, cvs, parts = [], [], []
    for seed in (5, 6, 7):
        d, cv, gc, n = run(seed, pb, pc, lag)
        ds.append(d); cvs.append(cv)
        parts.append(f"{d:5.2f}({cv:4.2f},gc={gc})")
    dsf = np.array([x for x in ds if np.isfinite(x)])
    cvf = np.array([x for x in cvs if np.isfinite(x)])
    print(f"pb={pb} pc={pc}: " + " ".join(parts) +
          (f"  -> d={dsf.mean():5.2f}+-{dsf.std():4.2f} CV={cvf.mean():4.2f}" if dsf.size else "  -> all nan"))
