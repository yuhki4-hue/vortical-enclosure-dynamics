"""VED stochastic quantization, Phase 3: emergent light cone.

2+1d: a 2d lattice chi(x, y) evolves in tau. The stationary state is a 2d
Euclidean QFT; Osterwalder-Schrader reconstruction takes y as emergent time.
Energy = decay rate of stationary correlations along y (transfer-matrix pole):

    4 D_y sinh^2(E/2) = D_x khat_x^2 + m^2
    small k:  E^2 = c^2 k^2 + m_t^2,   c^2 = D_x/D_y,   m_t^2 = m^2/D_y

Tests (two runs: isotropic D=(1,1), anisotropic D=(1.44,1)):
  1. light-cone speed        c^2 = D_x/D_y
  2. IR metric anisotropy    (A-B)/(A+B) from small-k quadratic form of 1/S
  3. mass                    m^2 at bare value (Liouville protection, 2d interacting)
  4. Lorentz violation       deviation from E^2 = c^2 k^2 + m_t^2 is O((ka)^2)

Run: python3 simulate_phase3.py     (numpy, matplotlib; ~4 min)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

QUICK = bool(int(os.environ.get("QUICK", "0")))   # QUICK=1: fast smoke test

# ---------------------------------------------------------------- parameters
N, dx = 64, 1.0
Gamma, aDelta = 0.04, 0.04            # m^2 = 0.08, xi ~ 3.5
hbar, dt = 0.05, 0.05
R = 8                                  # simultaneous replicas
BURN, STEPS, EVERY = (600, 6_000, 50) if QUICK else (6_000, 64_000, 50)
m2 = Gamma + aDelta
RUNS = (("iso", 1.0, 1.0, 21), ("aniso", 1.44, 1.0, 22))


def run(Dx, Dy, seed):
    rng = np.random.default_rng(seed)
    chi = np.full((R, N, N), np.log(2.0))          # axes: (replica, y, x)
    amp = np.sqrt(2 * hbar * dt / dx**2)

    def step(c):
        lap = Dx * (np.roll(c, 1, 2) + np.roll(c, -1, 2) - 2 * c) \
            + Dy * (np.roll(c, 1, 1) + np.roll(c, -1, 1) - 2 * c)
        return c + dt * (lap - Gamma * (np.exp(c) - 1.0) + aDelta) \
                 + amp * rng.standard_normal(c.shape)

    for _ in range(BURN):
        chi = step(chi)
    Ssum, n = np.zeros((N, N)), 0
    for i in range(STEPS):
        chi = step(chi)
        if i % EVERY == 0:
            d = chi - chi.mean(axis=(1, 2), keepdims=True)
            Ssum += (np.abs(np.fft.fft2(d, axes=(1, 2)))**2).mean(axis=0) / N**2
            n += 1
    return Ssum / n                                # S[k_y, k_x]


def pole_fit(S, kmax_idx=16):
    """Per k_x: fit hbar/S = a + b(1-cos k_y) over all k_y (Euler-corrected).
       a = D_x khat_x^2 + m^2,  b = 2 D_y."""
    ky = 2 * np.pi * np.fft.fftfreq(N)
    onemc = 1 - np.cos(ky)
    rows = []
    for ik in range(1, kmax_idx + 1):
        lam = np.zeros(N)
        for _ in range(3):                          # iterate O(dt) correction
            s_corr = S[:, ik] * (1 - lam * dt / 2)
            w = s_corr**2
            A = np.vstack([np.ones(N), onemc]).T
            (a, b), *_ = np.linalg.lstsq(w[:, None] * A, w * (hbar / s_corr),
                                         rcond=None)
            lam = a + b * onemc
        rows.append((2 - 2 * np.cos(2 * np.pi * ik / N), a, b))
    return np.array(rows)


def quadform_smallk(S, kcut=0.7):
    """Fit hbar/S = A kx^2 + B ky^2 + C kx ky + M on the small-k disc."""
    k1 = 2 * np.pi * np.fft.fftfreq(N)
    KX, KY = np.meshgrid(k1, k1)
    m = (KX**2 + KY**2 < kcut**2) & (KX**2 + KY**2 > 0)
    x, y, s = KX[m], KY[m], S[m]
    lam = hbar / s
    for _ in range(3):
        lamc = hbar / (s * (1 - lam * dt / 2))
        A = np.vstack([x**2, y**2, x * y, np.ones(len(x))]).T
        coef, *_ = np.linalg.lstsq(A, lamc, rcond=None)
        lam = A @ coef
    Ax, By, Cxy, M = coef
    return (Ax - By) / (Ax + By), Cxy


# ------------------------------------------------------------------- runs
res = {}
for tag, Dx, Dy, seed in RUNS:
    S = run(Dx, Dy, seed)
    pf = pole_fit(S)
    khat2, a, b = pf[:, 0], pf[:, 1], pf[:, 2]
    Dx_m, m2_m = np.polyfit(khat2, a, 1)
    Dy_m = b.mean() / 2
    aniso, cross = quadform_smallk(S)
    res[tag] = dict(S=S, khat2=khat2, E=2 * np.arcsinh(np.sqrt(a / (2 * b))),
                    Dx_m=Dx_m, Dy_m=Dy_m, m2_m=m2_m, c2=Dx_m / Dy_m)
    print(f"{tag}: D=({Dx},{Dy})   c^2={Dx_m/Dy_m:.4f} (pred {Dx/Dy:.4f})   "
          f"m^2={m2_m:.4f} (pred {m2})   anisotropy={aniso:+.4f} "
          f"(pred {(Dx-Dy)/(Dx+Dy):+.4f})   cross={cross:+.4f} (pred 0)")

# ------------------------------------------------------------------- figure
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14.5, 4.2))
cols = {"iso": "#7D3C98", "aniso": "#E67E22"}
kk = np.linspace(0.01, 1.5, 300)
for tag, Dx, Dy, _ in RUNS:
    r = res[tag]
    k = np.arccos(1 - r["khat2"] / 2)
    E_lat = 2 * np.arcsinh(np.sqrt((r["Dx_m"] * (2 - 2 * np.cos(kk)) + r["m2_m"])
                                   / (4 * r["Dy_m"])))
    ks = kk[kk < 0.35]
    El = 2 * np.arcsinh(np.sqrt((r["Dx_m"] * (2 - 2 * np.cos(ks)) + r["m2_m"])
                                / (4 * r["Dy_m"])))
    al, be = np.polyfit(ks**2, El**2, 1)
    ax1.plot(k**2, r["E"]**2, "o", ms=5, color=cols[tag],
             label=f"{tag}: $c^2$={r['c2']:.3f} (pred {Dx/Dy:g})")
    ax1.plot(kk**2, E_lat**2, "-", color=cols[tag], lw=1)
    ax1.plot(kk**2, al * kk**2 + be, "--", color=cols[tag], lw=0.8, alpha=0.7)
    ax2.loglog(kk, np.abs(E_lat**2 - (al * kk**2 + be)) / E_lat**2, "-",
               color=cols[tag], lw=1)
    ax2.loglog(k, np.abs(r["E"]**2 - (al * k**2 + be)) / r["E"]**2, "o", ms=4,
               color=cols[tag])
    # panel 3: angular isotropy on a ring
    k1 = 2 * np.pi * np.fft.fftfreq(N)
    KX, KY = np.meshgrid(k1, k1)
    KR = np.sqrt(KX**2 + KY**2)
    ring = (KR > 0.42) & (KR < 0.58)
    lam = hbar / res[tag]["S"][ring]
    lam = lam / (1 - lam * dt / 2)
    th = np.arctan2(KY[ring], KX[ring])
    o = np.argsort(th)
    ax3.plot(th[o], ((lam - m2) / KR[ring]**2)[o], ".", ms=3, color=cols[tag],
             alpha=0.5)
    tt = np.linspace(-np.pi, np.pi, 200)
    ax3.plot(tt, Dx * np.cos(tt)**2 + Dy * np.sin(tt)**2, "-", color=cols[tag],
             lw=1.2, label=rf"{tag}: $D_x\cos^2\theta+D_y\sin^2\theta$")
ax2.loglog(kk, 0.08 * kk**2, "k:", lw=1, label=r"$\propto k^2$ guide")
ax1.set_xlabel(r"$k^2$"); ax1.set_ylabel(r"$E^2(k)$")
ax1.set_title("Emergent light cones: $E^2=c^2k^2+m_t^2$,  $c^2=D_x/D_y$")
ax2.set_xlabel(r"$k$"); ax2.set_ylabel(r"$|E^2-(c^2k^2+m_t^2)|/E^2$")
ax2.set_title(r"Lorentz violation is $O((ka)^2)$-suppressed")
ax3.set_xlabel(r"$\theta$"); ax3.set_ylabel(r"$D(\theta)$")
ax3.set_title(r"IR metric isotropy on ring $|k|\approx 0.5$")
for ax in (ax1, ax2, ax3):
    ax.legend(fontsize=8, frameon=False)
plt.tight_layout()
plt.savefig("figures/fig2_emergent_lightcone.png", dpi=160)
print("wrote figures/fig2_emergent_lightcone.png")
