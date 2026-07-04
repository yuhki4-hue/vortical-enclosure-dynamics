"""VED stochastic quantization, Collins two-field experiment: arms 0-1.

Two chi fields on the same lattice, coupled only through a shared closure
budget (barrier term), each with its own bare transport tensor D_a:

    d(chi_a)/dtau = D_a . lap(chi_a) - Gamma(e^{chi_a}-1) + aDelta
                    - dW/dchi_a + eta_a
    W = kB / (Cmax - C1 - C2),   C_a = 1 - exp(-chi_a)

This coupling is a potential term (gradient flow preserved): detailed balance
holds, OS reconstruction goes through, and the mass matrix / mixing mu^2 are
derived (not fit) from an expansion of W about the coupled stationary point.
Sharing noise/drift directly (rather than the barrier) breaks this -- see
README §0 audit table.

Arms:
  arm0 (kB=0):  uncoupled control, opposite bare anisotropies
                D1=(1.3,0.77), D2=(0.77,1.3)  ->  bare cones c1^2=1.69, c2^2=0.59
  arm1 (kB=0.02): shared-barrier coupling -> derived mu^2, tree-level band mixing

Measurement: 2x2 cross-spectrum matrix S_ab(k), inverted (with iterated Euler
matrix correction) to the effective action matrix Lambda(k) = hbar S^-1(k);
bands from the generalized eigenvalue problem det[A(kx) - 2sinh^2(E/2) B] = 0.

Run: python3 simulate_collins.py        (~4-5 min for both arms; QUICK=1 for smoke test)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

QUICK = bool(int(os.environ.get("QUICK", "0")))

N, dx = 64, 1.0
Gamma, aDelta, hbar, dt, R = 0.04, 0.04, 0.05, 0.05, 8
Cmax = 1.5
BURN, STEPS, EVERY = (600, 6_000, 50) if QUICK else (6_000, 60_000, 50)
D1, D2 = (1.3, 0.77), (0.77, 1.3)
ARMS = (("arm0", 0.0), ("arm1", 0.02))


def stationary_u(kB):
    us = np.linspace(0.26, 0.99, 200_000)
    s = Cmax - 2 + 2 * us
    g = Gamma * (1 / us - 1) - aDelta + (kB * us / s**2 if kB > 0 else 0 * us)
    return us[np.argmin(np.abs(g))]


def derived_mass_matrix(kB, u0):
    """Tree-level diagonal mass and bilinear mixing from expanding W = kB/s
    about the symmetric coupled stationary point. Not fit."""
    s0 = Cmax - 2 + 2 * u0
    Md = Gamma / u0 + kB * (-u0 / s0**2 + 2 * u0**2 / s0**3)
    mu2 = 2 * kB * u0**2 / s0**3
    return Md, mu2


def run(kB, seed):
    rng = np.random.default_rng(seed)
    u0 = stationary_u(kB)
    chi = np.full((2, R, N, N), -np.log(u0))
    amp = np.sqrt(2 * hbar * dt / dx**2)
    Dx = np.array([D1[0], D2[0]]).reshape(2, 1, 1, 1)
    Dy = np.array([D1[1], D2[1]]).reshape(2, 1, 1, 1)

    def step(c):
        lap = Dx * (np.roll(c, 1, 3) + np.roll(c, -1, 3) - 2 * c) \
            + Dy * (np.roll(c, 1, 2) + np.roll(c, -1, 2) - 2 * c)
        drift = -Gamma * (np.exp(c) - 1.0) + aDelta
        if kB > 0:
            u = np.exp(-c)
            s = Cmax - 2 + u[0] + u[1]
            drift = drift - kB * u / s**2          # -dW/dchi_a
        return c + dt * (lap + drift) + amp * rng.standard_normal(c.shape)

    for _ in range(BURN):
        chi = step(chi)
    S, n = np.zeros((N, N, 2, 2)), 0
    for i in range(STEPS):
        chi = step(chi)
        if i % EVERY == 0:
            d = chi - chi.mean(axis=(2, 3), keepdims=True)
            f = np.fft.fft2(d, axes=(2, 3))                        # (2,R,N,N)
            S += np.einsum("arxy,brxy->xyab", f, np.conj(f)).real / (R * N**2)
            n += 1
    return S / n, u0


def band_dispersion(S, kmax_idx=16):
    """Matrix pole fit per k_x on the k_y disc, generalized-eigenvalue bands."""
    ky = 2 * np.pi * np.fft.fftfreq(N)
    onemc = 1 - np.cos(ky)
    sel = onemc <= 1.2                    # keep the Euler correction small
    X = np.vstack([np.ones(sel.sum()), onemc[sel]]).T
    ks, Elo, Ehi, mats = [], [], [], []
    for ik in range(1, kmax_idx + 1):
        L0 = hbar * np.linalg.inv(S[:, ik, :, :])
        Lam = L0.copy()
        for _ in range(3):                                        # Lambda = hbar S^-1 + (dt/2) Lambda^2
            Lam = L0 + (dt / 2) * np.einsum("kab,kbc->kac", Lam, Lam)
        Lam = Lam[sel]
        A, B = np.zeros((2, 2)), np.zeros((2, 2))
        for a in range(2):
            for b in range(2):
                (A[a, b], B[a, b]), *_ = np.linalg.lstsq(X, Lam[:, a, b], rcond=None)
        A, B = (A + A.T) / 2, (B + B.T) / 2
        z = np.sort(np.real(np.linalg.eigvals(np.linalg.inv(B) @ A)))
        E = 2 * np.arcsinh(np.sqrt(np.maximum(z, 1e-12) / 2))
        ks.append(2 * np.pi * ik / N); Elo.append(E[0]); Ehi.append(E[1]); mats.append((A, B))
    return np.array(ks), np.array(Elo), np.array(Ehi), mats


def tree_bands(kk, Md, mu2):
    Elo, Ehi = [], []
    for k in kk:
        kh2 = 2 - 2 * np.cos(k)
        A = np.array([[Md + D1[0] * kh2, mu2], [mu2, Md + D2[0] * kh2]])
        B = np.diag([2 * D1[1], 2 * D2[1]])
        z = np.sort(np.real(np.linalg.eigvals(np.linalg.inv(B) @ A)))
        Elo.append(2 * np.arcsinh(np.sqrt(z[0] / 2)))
        Ehi.append(2 * np.arcsinh(np.sqrt(z[1] / 2)))
    return np.array(Elo), np.array(Ehi)


res = {}
for tag, kB in ARMS:
    S, u0 = run(kB, seed=31 if tag == "arm0" else 32)
    k, Elo, Ehi, mats = band_dispersion(S)
    kh2 = 2 - 2 * np.cos(k)
    Ast = np.array([a for a, _ in mats])
    M_meas = np.array([[np.polyfit(kh2, Ast[:, a, b], 1)[1] for b in range(2)] for a in range(2)])
    Md_th, mu2_th = derived_mass_matrix(kB, u0)
    res[tag] = dict(k=k, Elo=Elo, Ehi=Ehi, M_meas=M_meas, u0=u0, Md_th=Md_th, mu2_th=mu2_th)
    print(f"{tag} (kB={kB}): u0={u0:.4f}")
    print(f"  derived : M_diag={Md_th:.4f}  mu^2={mu2_th:.4f}")
    print(f"  measured: M = [[{M_meas[0,0]:.4f},{M_meas[0,1]:.4f}],"
          f"[{M_meas[1,0]:.4f},{M_meas[1,1]:.4f}]]")
    tlo, thi = tree_bands(k, Md_th, mu2_th)
    devlo = np.abs(Elo**2 - tlo**2) / tlo**2
    devhi = np.abs(Ehi**2 - thi**2) / thi**2
    print(f"  |E^2_meas - E^2_tree|/E^2, zero fit params: "
          f"lo mean={devlo.mean()*100:.2f}% hi mean={devhi.mean()*100:.2f}%")

# ------------------------------------------------------------------- figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))
c_lo, c_hi = "#2E86AB", "#C0392B"
kk = np.linspace(0.05, 1.6, 300)
for tag, mk, ls, lab in (("arm0", "o", "--", "uncoupled"), ("arm1", "s", "-", "shared barrier")):
    r = res[tag]
    tlo, thi = tree_bands(kk, r["Md_th"], r["mu2_th"])
    mfc_lo = "none" if tag == "arm0" else c_lo
    mfc_hi = "none" if tag == "arm0" else c_hi
    ax1.plot(r["k"]**2, r["Elo"]**2, mk, ms=4, color=c_lo, mfc=mfc_lo)
    ax1.plot(r["k"]**2, r["Ehi"]**2, mk, ms=4, color=c_hi, mfc=mfc_hi)
    ax1.plot(kk**2, tlo**2, ls, color=c_lo, lw=1)
    ax1.plot(kk**2, thi**2, ls, color=c_hi, lw=1, label=f"{lab} (tree, no fit params)")
    c2_meas_lo = np.gradient(r["Elo"]**2, r["k"]**2)
    c2_meas_hi = np.gradient(r["Ehi"]**2, r["k"]**2)
    c2_tree_lo = np.gradient(tlo**2, kk**2)
    c2_tree_hi = np.gradient(thi**2, kk**2)
    ax2.plot(r["k"], c2_meas_lo, mk, ms=4, color=c_lo, mfc=mfc_lo)
    ax2.plot(r["k"], c2_meas_hi, mk, ms=4, color=c_hi, mfc=mfc_hi)
    ax2.plot(kk, c2_tree_lo, ls, color=c_lo, lw=1)
    ax2.plot(kk, c2_tree_hi, ls, color=c_hi, lw=1)
for y, s in ((D1[0] / D1[1], "bare $c_1^2$"), (D2[0] / D2[1], "bare $c_2^2$"),
             ((D1[0] + D2[0]) / (D1[1] + D2[1]), r"$\bar D_x/\bar D_y$")):
    ax2.axhline(y, color="k", lw=0.5, alpha=0.5)
    ax2.text(1.45, y + 0.02, s, fontsize=7)
kstar = np.sqrt(res["arm1"]["mu2_th"] / ((D1[0] - D2[0]) / 2))
ax2.axvline(kstar, color="gray", lw=0.7, ls=":")
ax2.text(kstar + 0.02, 0.35, r"$k_*$", fontsize=8)
ax1.set_xlabel("$k^2$"); ax1.set_ylabel(r"$E_\pm^2(k)$")
ax1.set_title("Two-field bands: measured vs. derived tree curves")
ax1.legend(fontsize=8, frameon=False)
ax2.set_xlabel("$k$"); ax2.set_ylabel(r"running $c_\pm^2(k)=dE_\pm^2/dk^2$")
ax2.set_title("Cone convergence: partial (IR), as predicted")
plt.tight_layout()
plt.savefig("figures/fig3_collins_twofield.png", dpi=160)
print("wrote figures/fig3_collins_twofield.png")
