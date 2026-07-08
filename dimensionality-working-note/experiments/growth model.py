"""Growth model: H accumulated as discrete registration events (K1 implementation).

Rule (main, history-dependent):
  a walker sits at node i; moves to j with prob ~ C_ij + eta (eta = tiny
  exploration floor so the process can bootstrap); each traversal REGISTERS
  one event: H_ij += 1. This is Vol.1's "structure generates its own
  selectivity" taken literally: existing C guides where new H lands.

Control (history-independent):
  the same total number of events placed on uniformly random directed pairs.
  Per section 5.6 this should stay d = infinity. Any difference between the
  two runs isolates history-dependence itself as the cause.

Measurement: after each epoch, solve the rho fixed point, build C, S~,
  D = -log S~, kernel exp(-D/med), calibrated power-law estimator.
NO coordinates, NO locality, NO dimension anywhere in the rule.
"""
import numpy as np

N = 300
LAM = 0.05
ETA = 1e-3          # exploration floor (uniform, geometry-free)
EPOCHS = 24
EVENTS_PER_EPOCH = 20_000


def solve_rho(H, lam, iters=800):
    rho = np.ones(H.shape[0])
    for _ in range(iters):
        rho_new = (1 - np.exp(-lam * rho[:, None] * H)).sum(1)
        if np.allclose(rho_new, rho, atol=1e-12):
            break
        rho = 0.5 * rho + 0.5 * rho_new
    return rho


def spectrum_dim(H, lam):
    rho = solve_rho(H, lam)
    if rho.max() < 1e-8:
        return np.nan, 0.0
    C = 1 - np.exp(-lam * rho[:, None] * H)
    Ssym = 0.5 * (C + C.T)
    Sc = np.clip(Ssym, 1e-12, 1 - 1e-12)
    D = -np.log(Sc)
    np.fill_diagonal(D, 0.0)
    med = np.median(D[D > 0])
    if not np.isfinite(med) or med <= 0:
        return np.nan, 0.0
    S = np.exp(-D / med)
    ev = np.linalg.eigvalsh(S)[::-1]
    ev = ev[ev > 1e-12 * ev[0]]
    k = np.arange(1, len(ev) + 1)
    kmax = max(11, len(ev) // 4)
    sel = (k >= 5) & (k <= kmax)
    s = np.polyfit(np.log(k[sel]), np.log(ev[sel]), 1)[0]
    d_hat = 1.0 / (abs(s) - 1.0) if abs(s) > 1.0 else np.inf
    return d_hat, s


def calibrate(d_hat):
    """Invert the calibration curve from section 5.6.1 (linear interp)."""
    meas = np.array([0.95, 1.99, 3.50, 5.82])
    true = np.array([1.0, 2.0, 3.0, 4.0])
    if not np.isfinite(d_hat):
        return np.inf
    return float(np.interp(d_hat, meas, true))


def run_growth(seed, mode):
    rng = np.random.default_rng(seed)
    H = np.zeros((N, N))
    # bootstrap: a single seed event so rho > 0 is reachable
    i0, j0 = rng.integers(N, size=2)
    H[i0, j0] += 1
    walker = int(i0)
    history = []
    rho = solve_rho(H, LAM)
    for ep in range(EPOCHS):
        if mode == "walker":
            C = 1 - np.exp(-LAM * rho[:, None] * H)
            for _ in range(EVENTS_PER_EPOCH):
                p = C[walker] + ETA
                p[walker] = 0.0
                p = p / p.sum()
                nxt = rng.choice(N, p=p)
                H[walker, nxt] += 1
                walker = nxt
            # C updated once per epoch (adiabatic selectivity); within an
            # epoch the walker sees frozen C -- registration is discrete,
            # selectivity update is the slow variable.
        else:  # control: same event count, uniform random placement
            ii = rng.integers(N, size=EVENTS_PER_EPOCH)
            jj = rng.integers(N, size=EVENTS_PER_EPOCH)
            np.add.at(H, (ii, jj), 1)
        rho = solve_rho(H, LAM)
        d_hat, slope = spectrum_dim(H, LAM)
        history.append((ep, (ep + 1) * EVENTS_PER_EPOCH, d_hat, calibrate(d_hat), slope))
    return history


for mode in ("walker", "control"):
    print("=" * 76)
    print(f"mode = {mode}   (N={N}, lam={LAM}, eta={ETA}, "
          f"{EVENTS_PER_EPOCH} events/epoch)")
    print("=" * 76)
    for seed in (3, 4):
        print(f" seed {seed}:")
        hist = run_growth(seed, mode)
        for ep, ev, dh, dc, sl in hist:
            if ep % 3 == 2 or ep == 0:
                dh_s = f"{dh:6.2f}" if np.isfinite(dh) else "   inf"
                dc_s = f"{dc:6.2f}" if np.isfinite(dc) else "   inf"
                print(f"   epoch {ep:2d}  events {ev:7d}   d_raw={dh_s}"
                      f"   d_cal={dc_s}   slope={sl:6.2f}")
