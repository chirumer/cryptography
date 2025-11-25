import numpy as np
import matplotlib.pyplot as plt

# New color scheme - different from original paper
color_RPA = '#9467bd'  # Purple
color_RIA = '#e74c3c'  # Red
color_MGA = '#17becf'  # Cyan/Teal

# Marker styles
marker_RPA = 'o'
marker_RIA = 'x'
marker_MGA = 's'

# Line styles
line_RPA = '-'
line_RIA = '--'
line_MGA = ':'

# Default parameters (Table 2)
beta_default = 0.05
r_default = 1
fT_default = 0.01
epsilon_default = 1
d_default = 1024

# OUE formulas from Table 1
def G_RPA_OUE(beta, r, fT, epsilon, d):
    """RPA overall gain for OUE: β(r - f_T)"""
    return beta * (r - fT)

def G_RIA_OUE(beta, r, fT, epsilon, d):
    """RIA overall gain for OUE: β(1 - f_T)"""
    return beta * (1 - fT)

def G_MGA_OUE(beta, r, fT, epsilon, d):
    """MGA overall gain for OUE: β(2r - f_T) + 2βr/(e^ε - 1)"""
    return beta * (2*r - fT) + (2 * beta * r) / (np.exp(epsilon) - 1)

def normalized_gain(G, fT):
    """Normalized overall gain: (G + f_T) / f_T"""
    return (G + fT) / fT

# Parameter ranges
beta_range = np.logspace(-3, -1, 20)
r_range = np.array([1, 5, 10, 15, 20])
fT_range = np.logspace(-3, -1, 20)
epsilon_range = np.linspace(0.5, 3.0, 20)
d_range = np.array([2**i for i in range(4, 13)])  # 2^4 to 2^12

def plot_top_row(ax, x_values, G_RPA, G_RIA, G_MGA, xlabel, xscale='log', show_legend=False):
    """Plot overall gains (top row)"""
    ax.plot(x_values, G_RPA, color=color_RPA, marker=marker_RPA, linestyle=line_RPA, 
            markersize=5, label='RPA', linewidth=1.5)
    ax.plot(x_values, G_RIA, color=color_RIA, marker=marker_RIA, linestyle=line_RIA, 
            markersize=7, markeredgewidth=2, label='RIA', linewidth=1.5)
    ax.plot(x_values, G_MGA, color=color_MGA, marker=marker_MGA, linestyle=line_MGA, 
            markersize=5, label='MGA', linewidth=1.5)
    
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('G', fontsize=12)
    ax.set_xscale(xscale)
    ax.set_yscale('log')
    ax.set_ylim(1e-3, 1e0)
    ax.grid(True, alpha=0.3)
    if show_legend:
        ax.legend(loc='best', fontsize=8)

def plot_bottom_row(ax, x_values, norm_RPA, norm_RIA, norm_MGA, xlabel, xscale='log', show_legend=False):
    """Plot normalized overall gains (bottom row)"""
    ax.plot(x_values, norm_RPA, color=color_RPA, marker=marker_RPA, linestyle=line_RPA, 
            markersize=5, label='RPA', linewidth=1.5)
    ax.plot(x_values, norm_RIA, color=color_RIA, marker=marker_RIA, linestyle=line_RIA, 
            markersize=7, markeredgewidth=2, label='RIA', linewidth=1.5)
    ax.plot(x_values, norm_MGA, color=color_MGA, marker=marker_MGA, linestyle=line_MGA, 
            markersize=5, label='MGA', linewidth=1.5)
    
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('Normalized G', fontsize=12)
    ax.set_xscale(xscale)
    ax.set_yscale('log')
    ax.set_ylim(1e0, 1e3)
    ax.grid(True, alpha=0.3)
    if show_legend:
        ax.legend(loc='best', fontsize=8)

# Create figure
fig, axes = plt.subplots(2, 5, figsize=(17, 6.5))

# Graph 1: Varying beta
G_RPA_beta = [G_RPA_OUE(b, r_default, fT_default, epsilon_default, d_default) for b in beta_range]
G_RIA_beta = [G_RIA_OUE(b, r_default, fT_default, epsilon_default, d_default) for b in beta_range]
G_MGA_beta = [G_MGA_OUE(b, r_default, fT_default, epsilon_default, d_default) for b in beta_range]

norm_RPA_beta = [normalized_gain(g, fT_default) for g in G_RPA_beta]
norm_RIA_beta = [normalized_gain(g, fT_default) for g in G_RIA_beta]
norm_MGA_beta = [normalized_gain(g, fT_default) for g in G_MGA_beta]

plot_top_row(axes[0, 0], beta_range, G_RPA_beta, G_RIA_beta, G_MGA_beta, r'$\beta$', show_legend=True)
plot_bottom_row(axes[1, 0], beta_range, norm_RPA_beta, norm_RIA_beta, norm_MGA_beta, r'$\beta$', show_legend=True)

# Graph 2: Varying r
# When varying r, use constant fT = 0.01 for BOTH G calculation AND normalization
G_RPA_r = [G_RPA_OUE(beta_default, r, fT_default, epsilon_default, d_default) for r in r_range]
G_RIA_r = [G_RIA_OUE(beta_default, r, fT_default, epsilon_default, d_default) for r in r_range]
G_MGA_r = [G_MGA_OUE(beta_default, r, fT_default, epsilon_default, d_default) for r in r_range]

norm_RPA_r = [normalized_gain(g, fT_default) for g in G_RPA_r]
norm_RIA_r = [normalized_gain(g, fT_default) for g in G_RIA_r]
norm_MGA_r = [normalized_gain(g, fT_default) for g in G_MGA_r]

plot_top_row(axes[0, 1], r_range, G_RPA_r, G_RIA_r, G_MGA_r, r'$r$', xscale='linear', show_legend=True)
plot_bottom_row(axes[1, 1], r_range, norm_RPA_r, norm_RIA_r, norm_MGA_r, r'$r$', xscale='linear', show_legend=True)

# Graph 3: Varying fT
G_RPA_fT = [G_RPA_OUE(beta_default, r_default, ft, epsilon_default, d_default) for ft in fT_range]
G_RIA_fT = [G_RIA_OUE(beta_default, r_default, ft, epsilon_default, d_default) for ft in fT_range]
G_MGA_fT = [G_MGA_OUE(beta_default, r_default, ft, epsilon_default, d_default) for ft in fT_range]

norm_RPA_fT = [normalized_gain(g, ft) for g, ft in zip(G_RPA_fT, fT_range)]
norm_RIA_fT = [normalized_gain(g, ft) for g, ft in zip(G_RIA_fT, fT_range)]
norm_MGA_fT = [normalized_gain(g, ft) for g, ft in zip(G_MGA_fT, fT_range)]

plot_top_row(axes[0, 2], fT_range, G_RPA_fT, G_RIA_fT, G_MGA_fT, r'$f_T$', show_legend=True)
plot_bottom_row(axes[1, 2], fT_range, norm_RPA_fT, norm_RIA_fT, norm_MGA_fT, r'$f_T$', show_legend=True)

# Graph 4: Varying epsilon
G_RPA_eps = [G_RPA_OUE(beta_default, r_default, fT_default, eps, d_default) for eps in epsilon_range]
G_RIA_eps = [G_RIA_OUE(beta_default, r_default, fT_default, eps, d_default) for eps in epsilon_range]
G_MGA_eps = [G_MGA_OUE(beta_default, r_default, fT_default, eps, d_default) for eps in epsilon_range]

norm_RPA_eps = [normalized_gain(g, fT_default) for g in G_RPA_eps]
norm_RIA_eps = [normalized_gain(g, fT_default) for g in G_RIA_eps]
norm_MGA_eps = [normalized_gain(g, fT_default) for g in G_MGA_eps]

plot_top_row(axes[0, 3], epsilon_range, G_RPA_eps, G_RIA_eps, G_MGA_eps, r'$\varepsilon$', xscale='linear', show_legend=True)
plot_bottom_row(axes[1, 3], epsilon_range, norm_RPA_eps, norm_RIA_eps, norm_MGA_eps, r'$\varepsilon$', xscale='linear', show_legend=True)

# Graph 5: Varying d
G_RPA_d = [G_RPA_OUE(beta_default, r_default, fT_default, epsilon_default, d) for d in d_range]
G_RIA_d = [G_RIA_OUE(beta_default, r_default, fT_default, epsilon_default, d) for d in d_range]
G_MGA_d = [G_MGA_OUE(beta_default, r_default, fT_default, epsilon_default, d) for d in d_range]

norm_RPA_d = [normalized_gain(g, fT_default) for g in G_RPA_d]
norm_RIA_d = [normalized_gain(g, fT_default) for g in G_RIA_d]
norm_MGA_d = [normalized_gain(g, fT_default) for g in G_MGA_d]

# Custom x-axis for d (powers of 2)
plot_top_row(axes[0, 4], d_range, G_RPA_d, G_RIA_d, G_MGA_d, r'$d$', xscale='log', show_legend=True)
axes[0, 4].set_xticks(d_range)
axes[0, 4].set_xticklabels([f'$2^{{{int(np.log2(d))}}}$' for d in d_range], fontsize=8)

plot_bottom_row(axes[1, 4], d_range, norm_RPA_d, norm_RIA_d, norm_MGA_d, r'$d$', xscale='log', show_legend=True)
axes[1, 4].set_xticks(d_range)
axes[1, 4].set_xticklabels([f'$2^{{{int(np.log2(d))}}}$' for d in d_range], fontsize=8)

plt.tight_layout()
plt.suptitle('Figure 2: Impact of different parameters on the overall gains (first row) and normalized overall gains (second row) of\nthe three attacks for OUE.', 
             fontsize=12, y=-0.02)
plt.subplots_adjust(bottom=0.15)

plt.savefig('fig2_recreated_oue.png', dpi=150, bbox_inches='tight')
plt.savefig('fig2_recreated.png', dpi=150, bbox_inches='tight')
print("Figure saved!")

# Verification
print("\n=== Verification for OUE with default parameters ===")
print(f"Default: β={beta_default}, r={r_default}, f_T={fT_default}, ε={epsilon_default}, d={d_default}")
print(f"\nRPA: G = β(r - f_T) = {beta_default} × ({r_default} - {fT_default}) = {G_RPA_OUE(beta_default, r_default, fT_default, epsilon_default, d_default):.6f}")
print(f"RIA: G = β(1 - f_T) = {beta_default} × (1 - {fT_default}) = {G_RIA_OUE(beta_default, r_default, fT_default, epsilon_default, d_default):.6f}")
print(f"MGA: G = β(2r - f_T) + 2βr/(e^ε - 1) = {G_MGA_OUE(beta_default, r_default, fT_default, epsilon_default, d_default):.6f}")

print("\n=== Verification for graph 2 (varying r) ===")
for r in r_range:
    g_rpa = G_RPA_OUE(beta_default, r, fT_default, epsilon_default, d_default)
    g_ria = G_RIA_OUE(beta_default, r, fT_default, epsilon_default, d_default)
    g_mga = G_MGA_OUE(beta_default, r, fT_default, epsilon_default, d_default)
    print(f"  r={r}: RPA={g_rpa:.4f}, RIA={g_ria:.4f}, MGA={g_mga:.4f}")
