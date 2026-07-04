"""VED stochastic quantization, Phase 4: the re-addressing gauge sector.

The VED core variable C_ij is an oriented link variable (rho_i makes
C_ij != C_ji). Its antisymmetric part a_ij transforms under local node
re-addressing as a_ij -> a_ij + phi_i - phi_j. Re-addressing invariance is
the local form of the founding axiom (only differences are physical), and it
forces the a-sector action to be loop-based:

    S = (beta/2) sum_p F_p^2  [+ (eps/2) sum a^2  = explicit breaking]
    F(n) = a_x(n) + a_y(n+x) - a_x(n+y) - a_y(n)

Zero-fit-parameter predictions tested (2d lattice, links a_x, a_y):
  1. transverse propagator  S_T(k) = hbar/(beta khat^2 + eps): massless pole at eps=0
  2. longitudinal (gauge-orbit) modes never equilibrate at eps=0:
     cold-start growth <|a_L|^2> = 2 hbar tau  ("addresses never close")
  3. breaking eps>0: mass^2 = eps appears AND orbits close at hbar/eps -- same coin
  4. flux-area law  Var(Phi_A) = (hbar/beta) A (1 - A/N^2)  (vorticity budget)

Run: python3 simulate_phase4.py       (~5 min both runs; QUICK=1 for smoke test)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

QUICK = bool(int(os.environ.get("QUICK", "0")))

N, R = 64, 8
beta, hbar, dt = 1.0, 0.05, 0.05
GROW, REC = (400, 10) if QUICK else (4000, 10)
STAT, EVERY = (5_000, 50) if QUICK else (50_000, 50)
KIDX = [1, 2, 4]                       # tracked transverse modes (k along x)

k1 = 2 * np.pi * np.fft.fftfreq(N)
QXg = (np.exp(1j * k1) - 1)[None, :]
QYg = (np.exp(1j * k1) - 1)[:, None]
q2g = np.abs(QXg)**2 + np.abs(QYg)**2
q2g[0, 0] = 1.0
Lmask = q2g > 1e-12
Lmask[0, 0] = False


def curl(ax, ay):
    return ax + np.roll(ay, -1, -1) - np.roll(ax, -1, -2) - ay


def run(eps, seed):
    rng = np.random.default_rng(seed)
    ax = np.zeros((R, N, N))
    ay = np.zeros((R, N, N))          # cold start: growth curves need a=0 origin
    amp = np.sqrt(2 * hbar * dt)

    def step(ax, ay):
        f = curl(ax, ay)
        dax = -beta * (f - np.roll(f, 1, -2)) - eps * ax
        day = -beta * (np.roll(f, 1, -1) - f) - eps * ay
        return (ax + dt * dax + amp * rng.standard_normal(ax.shape),
                ay + dt * day + amp * rng.standard_normal(ay.shape))

    growth_L, growth_T = [], []
    for i in range(GROW):
        ax, ay = step(ax, ay)
        if i % REC == 0:
            fx = np.fft.fft2(ax); fy = np.fft.fft2(ay)
            L = (np.conj(QXg) * fx + np.conj(QYg) * fy) / np.sqrt(q2g)
            growth_L.append((np.abs(L)**2).mean(axis=0)[Lmask].mean() / N**2)
            row = []
            for ik in KIDX:
                qx = np.exp(1j * 2 * np.pi * ik / N) - 1
                t = qx * fy[..., 0, ik] / abs(qx)
                row.append(np.mean(np.abs(t)**2) / N**2)
            growth_T.append(row)
    ST_sum = np.zeros((N, N)); SL_sum = np.zeros((N, N)); n = 0
    flux_snaps = []
    for i in range(STAT):
        ax, ay = step(ax, ay)
        if i % EVERY == 0:
            fx = np.fft.fft2(ax); fy = np.fft.fft2(ay)
            T = (QXg * fy - QYg * fx) / np.sqrt(q2g)
            L = (np.conj(QXg) * fx + np.conj(QYg) * fy) / np.sqrt(q2g)
            ST_sum += (np.abs(T)**2).mean(axis=0) / N**2
            SL_sum += (np.abs(L)**2).mean(axis=0) / N**2
            n += 1
            if eps == 0.0 and i % (EVERY * 20) == 0:
                flux_snaps.append(curl(ax, ay).copy())
    return (np.array(growth_L), np.array(growth_T),
            ST_sum / n, SL_sum / n, flux_snaps)


def flux_variance(snaps, Lbox):
    v = []
    for f in snaps:
        cs = f.cumsum(-2).cumsum(-1)
        S1 = cs[:, Lbox - 1:, Lbox - 1:]
        S2 = np.zeros_like(S1); S3 = np.zeros_like(S1); S4 = np.zeros_like(S1)
        S2[:, :, 1:] = cs[:, Lbox - 1:, :-Lbox]
        S3[:, 1:, :] = cs[:, :-Lbox, Lbox - 1:]
        S4[:, 1:, 1:] = cs[:, :-Lbox, :-Lbox]
        v.append((S1 - S2 - S3 + S4).var())
    return float(np.mean(v))


res = {}
for eps, seed in ((0.0, 41), (0.02, 42)):
    gL, gT, ST, SL, snaps = run(eps, seed)
    res[eps] = dict(gL=gL, gT=gT, ST=ST, SL=SL, snaps=snaps)
    lam = beta * q2g[Lmask] + eps
    ratio = ST[Lmask] / (hbar / (lam * (1 - lam * dt / 2)))
    print(f"eps={eps}: S_T / [hbar/(beta khat^2 + eps)] = {ratio.mean():.4f} "
          f"+- {ratio.std()/np.sqrt(Lmask.sum()):.4f}")
    tau = np.arange(len(gL)) * REC * dt
    if eps == 0.0:
        slope = np.polyfit(tau, gL, 1)[0]
        print(f"          longitudinal growth slope = {slope:.4f}  (prediction 2 hbar = {2*hbar})")
    else:
        rL = SL[Lmask].mean() / (hbar / (eps * (1 - eps * dt / 2)))
        print(f"          longitudinal saturation S_L/(hbar/eps) = {rL:.4f}  (orbits close)")

print("flux-area law, prediction (hbar/beta) A (1 - A/N^2):")
for Lb in (2, 4, 8, 12, 16):
    A = Lb**2
    print(f"  L={Lb:2d}: measured {flux_variance(res[0.0]['snaps'], Lb):.4f}"
          f"   predicted {hbar/beta*A*(1-A/N**2):.4f}")

# ------------------------------------------------------------------- figure
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14.5, 4.2))
tau = np.arange(len(res[0.0]['gL'])) * REC * dt
cols = plt.cm.viridis(np.linspace(0.2, 0.75, len(KIDX)))
ax1.plot(tau, res[0.0]['gL'], '-', color='#C0392B', lw=1.6,
         label=r'longitudinal (addresses), $\epsilon=0$')
ax1.plot(tau, 2 * hbar * tau, 'k--', lw=1, label=r'$2\hbar\tau$ (never closes)')
for i, (ik, c) in enumerate(zip(KIDX, cols)):
    k2 = 2 - 2 * np.cos(2 * np.pi * ik / N)
    ax1.plot(tau, res[0.0]['gT'][:, i], '-', color=c, lw=1.2)
    ax1.plot(tau, hbar / (beta * k2) * (1 - np.exp(-2 * beta * k2 * tau)), ':', color=c, lw=1)
ax1.plot(tau, res[0.02]['gL'], '-', color='#E67E22', lw=1.4,
         label=r'longitudinal, $\epsilon=0.02$ (closes at $\hbar/\epsilon$)')
ax1.set_xlabel(r'$\tau$'); ax1.set_ylabel(r'$\langle|a_{L,T}(k)|^2\rangle$')
ax1.set_title('Orbit non-closure vs physical equilibration')
ax1.legend(fontsize=7, frameon=False)
kk = np.geomspace(q2g[Lmask].min(), q2g[Lmask].max(), 200)
for eps, c, lab in ((0.0, '#7D3C98', r'$\epsilon=0$: massless pole'),
                    (0.02, '#E67E22', r'$\epsilon=0.02$: mass$^2=\epsilon$')):
    ax2.loglog(q2g[Lmask].ravel(), res[eps]['ST'][Lmask].ravel(), '.', ms=2, color=c, alpha=0.3)
    ax2.loglog(kk, hbar / (beta * kk + eps), '-', color=c, lw=1.2, label=lab)
ax2.set_xlabel(r'$\hat{k}^2$'); ax2.set_ylabel(r'$S_T(k)$')
ax2.set_title('Mass forbidden by re-addressing invariance')
ax2.legend(fontsize=8, frameon=False)
Ls = np.array([2, 4, 8, 12, 16]); A = Ls**2.0
ax3.plot(A, [flux_variance(res[0.0]['snaps'], int(l)) for l in Ls], 'o', color='#2E86AB', label='measured')
Ag = np.linspace(0, 300, 100)
ax3.plot(Ag, hbar / beta * Ag * (1 - Ag / N**2), 'k--', lw=1, label=r'$(\hbar/\beta)A(1-A/N^2)$')
ax3.set_xlabel(r'enclosed area $A$'); ax3.set_ylabel(r'Var$(\Phi_A)$')
ax3.set_title('Vorticity budget: flux-area law')
ax3.legend(fontsize=8, frameon=False)
plt.tight_layout()
plt.savefig('figures/fig4_gauge_sector.png', dpi=160)
print('wrote figures/fig4_gauge_sector.png')
