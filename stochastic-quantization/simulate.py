"""VED stochastic quantization, Phase 2 numerical confirmation.

chi-layer Langevin dynamics (C* = 1 quantum sector):

    d(chi)/dtau = D lap(chi) - V'(chi) + eta
    V'(chi)     = Gamma*(exp(chi) - 1) - aDelta        (barrier omitted)
    <eta eta>   = 2 hbar_eff delta_ij/dx delta(tau-tau')

Predictions tested:
  1. stationary propagator  S(k) = hbar/(D khat^2 + m^2),  m^2 = Gamma + aDelta
  2. FDT scaling            S proportional to hbar_eff
  3. spectral gap           zero-mode relaxation rate = m^2
  4. Liouville tadpole      <chi> = chi_bar - <dchi^2>/2   (V''' = m^2)
     + one-loop mass protection: gap independent of hbar (V'''' - V'''^2/V'' = 0)

Run: python3 simulate.py     (numpy, matplotlib; ~1 min; QUICK=1 for smoke test)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- parameters
QUICK = bool(int(os.environ.get("QUICK", "0")))
N, dx, D = 256, 1.0, 1.0
Gamma, aDelta = 0.25, 0.25          # -> chi_bar = ln 2, m^2 = 0.5
dt = 0.02
BURN, STEPS, EVERY = (1_000, 20_000, 50) if QUICK else (20_000, 500_000, 50)
HBARS = (0.05, 0.20)

m2 = Gamma + aDelta
chi_bar = np.log(1.0 + aDelta / Gamma)


def run(hbar, seed):
    rng = np.random.default_rng(seed)
    chi = np.full(N, chi_bar)
    amp = np.sqrt(2.0 * hbar * dt / dx)

    def step(c):
        lap = (np.roll(c, 1) - 2 * c + np.roll(c, -1)) / dx**2
        return c + dt * (D * lap - Gamma * (np.exp(c) - 1.0) + aDelta) \
                 + amp * rng.standard_normal(N)

    for _ in range(BURN):
        chi = step(chi)
    Ssum, nsamp, zmode = np.zeros(N), 0, []
    for i in range(STEPS):
        chi = step(chi)
        if i % EVERY == 0:
            d = chi - chi.mean()
            Ssum += np.abs(np.fft.fft(d))**2 * dx / N
            nsamp += 1
            zmode.append(chi.mean())
    k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    khat2 = (2 - 2 * np.cos(k * dx)) / dx**2
    return dict(hbar=hbar, k=k, khat2=khat2, S=Ssum / nsamp,
                S_th=hbar / (D * khat2 + m2),
                zmode=np.array(zmode), chi_mean=np.mean(zmode))


def gap(zmode, dt_samp, frac=2.0):
    z = zmode - zmode.mean()
    n = len(z)
    ac = np.correlate(z, z, "full")[n - 1:] / np.arange(n, 0, -1)
    ac /= ac[0]
    tmax = int(frac / m2 / dt_samp)
    t = np.arange(tmax) * dt_samp
    good = ac[:tmax] > 0.05
    return -np.polyfit(t[good], np.log(ac[:tmax][good]), 1)[0]


results = [run(h, seed=i + 1) for i, h in enumerate(HBARS)]

# ------------------------------------------------------------------- tests
print(f"m^2 = {m2:.3f}   chi_bar = {chi_bar:.4f}")
for r in results:
    mask = r["khat2"] > 1e-12
    lam = D * r["khat2"][mask] + m2
    raw = (r["S"][mask] / r["S_th"][mask]).mean()
    corr = (r["S"][mask] / (r["hbar"] / (lam * (1 - lam * dt / 2)))).mean()
    var = (r["hbar"] / N) * np.sum(1.0 / (r["khat2"] + m2))
    tad = chi_bar - var / 2
    g = gap(r["zmode"], dt * EVERY)
    print(f"hbar={r['hbar']:.2f}:  S/S_th={raw:.4f}  (dt-corrected {corr:.4f})   "
          f"gap={g:.4f} (pred {m2})   <chi>={r['chi_mean']:.4f} (tadpole {tad:.4f})")
fdt = (results[1]["S"][1:] / results[0]["S"][1:]).mean()
print(f"FDT: S(hbar={HBARS[1]})/S(hbar={HBARS[0]}) = {fdt:.3f}   "
      f"(prediction {HBARS[1]/HBARS[0]:.3f})")

# ------------------------------------------------------------------- figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
colors = ("#7D3C98", "#E67E22")
for r, c in zip(results, colors):
    o = np.argsort(r["k"]); k, S, T = r["k"][o], r["S"][o], r["S_th"][o]
    pos = k > 0
    lab = rf"$\hbar_{{\rm eff}}={r['hbar']}$"
    ax1.loglog(k[pos], S[pos], "o", ms=3, color=c, alpha=0.6, label=lab + " (sim)")
    ax1.loglog(k[pos], T[pos], "-", color=c, lw=1.2,
               label=lab + r"  $\hbar/(D\hat{k}^2+m^2)$")
    ax2.semilogx(k[pos], S[pos] / T[pos], ".", ms=3, color=c, alpha=0.5)
kg = np.geomspace(1e-2, np.pi, 200)
ax2.semilogx(kg, 1 + (2 - 2 * np.cos(kg) + m2) * dt / 2, "k--", lw=0.9,
             label=r"Euler $O(d\tau)$: $1+\lambda_k d\tau/2$")
ax2.axhline(1.0, color="k", lw=0.8)
ax1.set_xlabel(r"$k$"); ax1.set_ylabel(r"$S(k)=\langle|\chi_k|^2\rangle$")
ax1.set_title(rf"VED $\chi$-layer stationary propagator  ($m^2={m2}$)")
ax1.legend(fontsize=8, frameon=False)
ax2.set_xlabel(r"$k$"); ax2.set_ylabel(r"$S_{\rm sim}/S_{\rm theory}$")
ax2.set_ylim(0.9, 1.15); ax2.legend(fontsize=8, frameon=False)
ax2.set_title("deviation = time-discretization artifact")
plt.tight_layout()
plt.savefig("figures/fig1_stationary_propagator.png", dpi=160)
print("wrote figures/fig1_stationary_propagator.png")
