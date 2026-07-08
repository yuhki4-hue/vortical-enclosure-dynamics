"""Growth model v2: registration events + decay (the canonical -Gamma C term).

Change from v1: H decays each epoch, H <- H * (1 - gamma). Reinforcement
(walker registration) now competes with forgetting -- only self-consistently
revisited structure survives. Decay is NOT an import: it is the -Gamma C
term of the unified VED x IFGT equation, previously left out.
Sweep gamma to map regimes. Same control run (random placement + decay).
"""
import numpy as np

N = 300
LAM = 0.05
ETA = 1e-3
EPOCHS = 30
EV = 20_000

def solve_rho(H, lam, iters=800):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rn = (1 - np.exp(-lam * rho[:, None] * H)).sum(1)
        if np.allclose(rn, rho, atol=1e-12):
            break
        rho = 0.5 * rho + 0.5 * rn
    return rho

def spectrum_dim(H, lam):
    rho = solve_rho(H, lam)
    if rho.max() < 1e-8:
        return np.nan, 0.0, 0.0
    C = 1 - np.exp(-lam * rho[:, None] * H)
    S = 0.5 * (C + C.T)
    Sc = np.clip(S, 1e-12, 1 - 1e-12)
    D = -np.log(Sc); np.fill_diagonal(D, 0.0)
    med = np.median(D[D > 0])
    K = np.exp(-D / med)
    ev = np.linalg.eigvalsh(K)[::-1]
    ev = ev[ev > 1e-12 * ev[0]]
    k = np.arange(1, len(ev) + 1)
    sel = (k >= 5) & (k <= max(11, len(ev)//4))
    s = np.polyfit(np.log(k[sel]), np.log(ev[sel]), 1)[0]
    d = 1.0/(abs(s)-1.0) if abs(s) > 1.0 else np.inf
    return d, s, C.mean()

def calib(d):
    m = np.array([0.95,1.99,3.50,5.82]); t = np.array([1.,2.,3.,4.])
    return np.inf if not np.isfinite(d) else float(np.interp(d, m, t))

def run(seed, mode, gamma):
    rng = np.random.default_rng(seed)
    H = np.zeros((N, N))
    i0, j0 = rng.integers(N, size=2); H[i0, j0] = 1.0
    w = int(i0)
    rho = solve_rho(H, LAM)
    out = []
    for ep in range(EPOCHS):
        if mode == "walker":
            C = 1 - np.exp(-LAM * rho[:, None] * H)
            P = C + ETA
            np.fill_diagonal(P, 0.0)
            P = P / P.sum(1, keepdims=True)
            # vectorized-ish walk: sample in chunks with frozen P
            for _ in range(EV):
                w2 = rng.choice(N, p=P[w])
                H[w, w2] += 1.0
                w = w2
        else:
            ii = rng.integers(N, size=EV); jj = rng.integers(N, size=EV)
            np.add.at(H, (ii, jj), 1.0)
        H *= (1.0 - gamma)
        rho = solve_rho(H, LAM)
        d, s, cm = spectrum_dim(H, LAM)
        out.append((ep, d, calib(d), s, cm))
    return out

for gamma in (0.05, 0.2, 0.5):
    for mode in ("walker", "control"):
        hist = run(5, mode, gamma)
        ep, d, dc, s, cm = hist[-1]
        mid = hist[len(hist)//2]
        f = lambda x: f"{x:6.2f}" if np.isfinite(x) else "   inf"
        print(f"gamma={gamma:4.2f} {mode:7s} | mid: d_cal={f(mid[2])} slope={mid[3]:6.2f}"
              f" | final: d_cal={f(dc)} slope={s:6.2f} <C>={cm:.3f}")
