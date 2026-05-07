"""
============================================================
  Análisis Experimental - Ley de Hooke
  Curso de Física III · Universidad de Investigación y Desarrollo
  Prof. Dr. José Hernández-Jiménez
============================================================
  Gráficas generadas:
    1. F vs Δx  →  Regresión lineal + constante k
    2. Ue vs Δx →  Energía potencial elástica (parábola)
    3. Residuos  →  Análisis de error del modelo
============================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats

# ──────────────────────────────────────────────
#  DATOS EXPERIMENTALES
# ──────────────────────────────────────────────

masas = np.array([0.05, 0.08, 0.14, 0.18, 0.24])   # kg

# Fuerza = m * g  (g = 9.8 m/s²)
g = 9.8
fuerza = masas * g   # N  →  [0.49, 0.784, 1.372, 1.764, 2.352]

# Elongaciones medidas en laboratorio (metros)
x1 = np.array([0.002, 0.004, 0.006, 0.008, 0.012])   # Resorte 1
x2 = np.array([0.013, 0.020, 0.036, 0.045, 0.060])   # Resorte 2

# ──────────────────────────────────────────────
#  REGRESIÓN LINEAL  F = k · Δx
# ──────────────────────────────────────────────

# Resorte 1
slope1, intercept1, r1, p1, se1 = stats.linregress(x1, fuerza)
k1 = slope1   # N/m

# Resorte 2
slope2, intercept2, r2, p2, se2 = stats.linregress(x2, fuerza)
k2 = slope2   # N/m

# Valores predichos por el modelo
F_pred1 = slope1 * x1 + intercept1
F_pred2 = slope2 * x2 + intercept2

# Residuos
res1 = fuerza - F_pred1
res2 = fuerza - F_pred2

# Energía potencial elástica  Ue = ½ k Δx²
Ue1 = 0.5 * k1 * x1**2
Ue2 = 0.5 * k2 * x2**2

# Curva suave para la parábola
x1_smooth = np.linspace(0, x1.max() * 1.1, 200)
x2_smooth = np.linspace(0, x2.max() * 1.1, 200)
Ue1_smooth = 0.5 * k1 * x1_smooth**2
Ue2_smooth = 0.5 * k2 * x2_smooth**2

# ──────────────────────────────────────────────
#  ESTILO VISUAL
# ──────────────────────────────────────────────

plt.rcParams.update({
    "figure.facecolor":  "#0D1117",
    "axes.facecolor":    "#161B22",
    "axes.edgecolor":    "#30363D",
    "axes.labelcolor":   "#E6EDF3",
    "axes.titlecolor":   "#E6EDF3",
    "axes.grid":         True,
    "grid.color":        "#21262D",
    "grid.linewidth":    0.8,
    "xtick.color":       "#8B949E",
    "ytick.color":       "#8B949E",
    "text.color":        "#E6EDF3",
    "legend.facecolor":  "#161B22",
    "legend.edgecolor":  "#30363D",
    "legend.labelcolor": "#E6EDF3",
    "font.family":       "DejaVu Sans",
    "font.size":         10,
})

COLOR_R1   = "#58A6FF"   # azul  – Resorte 1
COLOR_R2   = "#3FB950"   # verde – Resorte 2
COLOR_LINE = "#F78166"   # coral – línea de tendencia
ALPHA_FILL = 0.12

# ──────────────────────────────────────────────
#  FIGURA PRINCIPAL  (3 filas × 2 columnas)
# ──────────────────────────────────────────────

fig = plt.figure(figsize=(14, 16), facecolor="#0D1117")
fig.suptitle(
    "Análisis Experimental — Ley de Hooke\n"
    "Física III · Universidad de Investigación y Desarrollo",
    fontsize=15, fontweight="bold", color="#E6EDF3",
    y=0.98
)

gs = gridspec.GridSpec(3, 2, figure=fig,
                       hspace=0.55, wspace=0.35,
                       top=0.93, bottom=0.05,
                       left=0.08, right=0.97)

# ════════════════════════════════════════════
#  GRÁFICA 1a  –  F vs Δx  (Resorte 1)
# ════════════════════════════════════════════
ax1a = fig.add_subplot(gs[0, 0])

x_line1 = np.linspace(0, x1.max() * 1.15, 200)
ax1a.fill_between(x_line1, slope1 * x_line1 + intercept1,
                  alpha=ALPHA_FILL, color=COLOR_R1)
ax1a.plot(x_line1, slope1 * x_line1 + intercept1,
          color=COLOR_LINE, lw=2, ls="--",
          label=f"Ajuste lineal\n$k_1 = {k1:.1f}$ N/m\n$R^2 = {r1**2:.4f}$")
ax1a.scatter(x1, fuerza, color=COLOR_R1, s=70, zorder=5,
             edgecolors="white", lw=0.8, label="Datos experimentales")

ax1a.set_title("F vs Δx — Resorte 1", fontweight="bold", pad=8)
ax1a.set_xlabel("Elongación Δx  (m)")
ax1a.set_ylabel("Fuerza F  (N)")
ax1a.legend(fontsize=8.5, loc="upper left")
ax1a.set_xlim(left=0)
ax1a.set_ylim(bottom=0)

# ════════════════════════════════════════════
#  GRÁFICA 1b  –  F vs Δx  (Resorte 2)
# ════════════════════════════════════════════
ax1b = fig.add_subplot(gs[0, 1])

x_line2 = np.linspace(0, x2.max() * 1.15, 200)
ax1b.fill_between(x_line2, slope2 * x_line2 + intercept2,
                  alpha=ALPHA_FILL, color=COLOR_R2)
ax1b.plot(x_line2, slope2 * x_line2 + intercept2,
          color=COLOR_LINE, lw=2, ls="--",
          label=f"Ajuste lineal\n$k_2 = {k2:.1f}$ N/m\n$R^2 = {r2**2:.4f}$")
ax1b.scatter(x2, fuerza, color=COLOR_R2, s=70, zorder=5,
             edgecolors="white", lw=0.8, label="Datos experimentales")

ax1b.set_title("F vs Δx — Resorte 2", fontweight="bold", pad=8)
ax1b.set_xlabel("Elongación Δx  (m)")
ax1b.set_ylabel("Fuerza F  (N)")
ax1b.legend(fontsize=8.5, loc="upper left")
ax1b.set_xlim(left=0)
ax1b.set_ylim(bottom=0)

# ════════════════════════════════════════════
#  GRÁFICA 2a  –  Ue vs Δx  (Resorte 1)
# ════════════════════════════════════════════
ax2a = fig.add_subplot(gs[1, 0])

ax2a.fill_between(x1_smooth, Ue1_smooth,
                  alpha=ALPHA_FILL, color=COLOR_R1)
ax2a.plot(x1_smooth, Ue1_smooth,
          color=COLOR_R1, lw=2,
          label=f"$U_e = \\frac{{1}}{{2}} k_1 \\Delta x^2$\n$k_1 = {k1:.1f}$ N/m")
ax2a.scatter(x1, Ue1, color=COLOR_R1, s=70, zorder=5,
             edgecolors="white", lw=0.8, label="Puntos experimentales")

# Anotación en el último punto
ax2a.annotate(f"$U_e$ = {Ue1[-1]*1000:.2f} mJ",
              xy=(x1[-1], Ue1[-1]),
              xytext=(x1[-1]*0.6, Ue1[-1]*0.75),
              color="#8B949E", fontsize=8,
              arrowprops=dict(arrowstyle="->", color="#8B949E", lw=0.8))

ax2a.set_title("Energía Potencial Elástica vs Δx — Resorte 1",
               fontweight="bold", pad=8)
ax2a.set_xlabel("Elongación Δx  (m)")
ax2a.set_ylabel("Energía $U_e$  (J)")
ax2a.legend(fontsize=8.5)
ax2a.set_xlim(left=0)
ax2a.set_ylim(bottom=0)

# ════════════════════════════════════════════
#  GRÁFICA 2b  –  Ue vs Δx  (Resorte 2)
# ════════════════════════════════════════════
ax2b = fig.add_subplot(gs[1, 1])

ax2b.fill_between(x2_smooth, Ue2_smooth,
                  alpha=ALPHA_FILL, color=COLOR_R2)
ax2b.plot(x2_smooth, Ue2_smooth,
          color=COLOR_R2, lw=2,
          label=f"$U_e = \\frac{{1}}{{2}} k_2 \\Delta x^2$\n$k_2 = {k2:.1f}$ N/m")
ax2b.scatter(x2, Ue2, color=COLOR_R2, s=70, zorder=5,
             edgecolors="white", lw=0.8, label="Puntos experimentales")

ax2b.annotate(f"$U_e$ = {Ue2[-1]*1000:.2f} mJ",
              xy=(x2[-1], Ue2[-1]),
              xytext=(x2[-1]*0.55, Ue2[-1]*0.75),
              color="#8B949E", fontsize=8,
              arrowprops=dict(arrowstyle="->", color="#8B949E", lw=0.8))

ax2b.set_title("Energía Potencial Elástica vs Δx — Resorte 2",
               fontweight="bold", pad=8)
ax2b.set_xlabel("Elongación Δx  (m)")
ax2b.set_ylabel("Energía $U_e$  (J)")
ax2b.legend(fontsize=8.5)
ax2b.set_xlim(left=0)
ax2b.set_ylim(bottom=0)

# ════════════════════════════════════════════
#  GRÁFICA 3a  –  Residuos  (Resorte 1)
# ════════════════════════════════════════════
ax3a = fig.add_subplot(gs[2, 0])

ax3a.axhline(0, color="#F78166", lw=1.5, ls="--", alpha=0.7,
             label="Residuo = 0 (modelo perfecto)")
ax3a.fill_between(x1, res1, alpha=0.15, color=COLOR_R1)
ax3a.scatter(x1, res1, color=COLOR_R1, s=70, zorder=5,
             edgecolors="white", lw=0.8, label="Residuos")
ax3a.vlines(x1, 0, res1, color=COLOR_R1, lw=1.2, alpha=0.5)

# Etiqueta en cada residuo
for xi, ri in zip(x1, res1):
    ax3a.annotate(f"{ri*1000:.2f} mN",
                  xy=(xi, ri), xytext=(xi + 0.0002, ri + 0.001 * np.sign(ri)),
                  color="#8B949E", fontsize=7)

ax3a.set_title("Análisis de Residuos — Resorte 1", fontweight="bold", pad=8)
ax3a.set_xlabel("Elongación Δx  (m)")
ax3a.set_ylabel("$F_{medida} - F_{modelo}$  (N)")
ax3a.legend(fontsize=8.5)

# ════════════════════════════════════════════
#  GRÁFICA 3b  –  Residuos  (Resorte 2)
# ════════════════════════════════════════════
ax3b = fig.add_subplot(gs[2, 1])

ax3b.axhline(0, color="#F78166", lw=1.5, ls="--", alpha=0.7,
             label="Residuo = 0 (modelo perfecto)")
ax3b.fill_between(x2, res2, alpha=0.15, color=COLOR_R2)
ax3b.scatter(x2, res2, color=COLOR_R2, s=70, zorder=5,
             edgecolors="white", lw=0.8, label="Residuos")
ax3b.vlines(x2, 0, res2, color=COLOR_R2, lw=1.2, alpha=0.5)

for xi, ri in zip(x2, res2):
    ax3b.annotate(f"{ri*1000:.2f} mN",
                  xy=(xi, ri), xytext=(xi + 0.001, ri + 0.002 * np.sign(ri)),
                  color="#8B949E", fontsize=7)

ax3b.set_title("Análisis de Residuos — Resorte 2", fontweight="bold", pad=8)
ax3b.set_xlabel("Elongación Δx  (m)")
ax3b.set_ylabel("$F_{medida} - F_{modelo}$  (N)")
ax3b.legend(fontsize=8.5)

# ──────────────────────────────────────────────
#  CAJA DE RESULTADOS EN LA FIGURA
# ──────────────────────────────────────────────

resumen = (
    f"  RESUMEN DE RESULTADOS  \n"
    f"  ─────────────────────────────────────────  \n"
    f"  Resorte 1 │ k₁ = {k1:.2f} N/m │ R² = {r1**2:.4f}  \n"
    f"  Resorte 2 │ k₂ = {k2:.2f} N/m │ R² = {r2**2:.4f}  \n"
    f"  Resorte 1 es ≈ {k1/k2:.1f}× más rígido que el Resorte 2"
)
fig.text(0.5, 0.005, resumen, ha="center", va="bottom",
         fontsize=9, color="#8B949E",
         fontfamily="monospace",
         bbox=dict(boxstyle="round,pad=0.4",
                   facecolor="#161B22", edgecolor="#30363D"))

# ──────────────────────────────────────────────
#  GUARDAR
# ──────────────────────────────────────────────

output_path = "/mnt/user-data/outputs/ley_de_hooke_graficas.png"
plt.savefig(output_path, dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print(f"✓ Figura guardada en: {output_path}")

# ──────────────────────────────────────────────
#  RESUMEN EN CONSOLA
# ──────────────────────────────────────────────

print("\n" + "═"*50)
print("  RESULTADOS — LEY DE HOOKE")
print("═"*50)
print(f"  Resorte 1 → k₁ = {k1:.2f} N/m  |  R² = {r1**2:.4f}")
print(f"  Resorte 2 → k₂ = {k2:.2f} N/m  |  R² = {r2**2:.4f}")
print(f"\n  Resorte 1 es {k1/k2:.1f}× más rígido que el Resorte 2")
print("\n  Residuos Resorte 1 (N):", [f"{r:.4f}" for r in res1])
print("  Residuos Resorte 2 (N):", [f"{r:.4f}" for r in res2])
print("═"*50)
