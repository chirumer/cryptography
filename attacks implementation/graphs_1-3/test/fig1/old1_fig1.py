"""
Recreate Figure 1 from "Data Poisoning Attacks to Local Differential Privacy Protocols"
Impact of different parameters on the overall gains (first row) and normalized overall gains 
(second row) of the three attacks for kRR.

From Table 1 in the paper:
- RPA: G = β(r/d - f_T)
- RIA: G = β(1 - f_T)
- MGA: G = β(1 - f_T) + β(d-r)/(e^ε - 1)

Default parameters from Table 2:
- β = 0.05
- r = 1
- f_T = 0.01
- ε = 1
- k = 20 (not used for frequency estimation)
- g = 10 (not used for frequency estimation)
- d = 1024 (from Section 5.1: "By default, we synthesize a dataset with 1,024 items")
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter
import matplotlib

# Use a clean style matching the original
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['xtick.major.width'] = 0.8
plt.rcParams['ytick.major.width'] = 0.8

# Default parameters
DEFAULT_BETA = 0.05
DEFAULT_R = 1
DEFAULT_FT = 0.01
DEFAULT_EPSILON = 1
DEFAULT_D = 1024  # From Section 5.1: Zipf dataset has 1,024 items by default

def compute_gains_kRR(beta, r, f_T, epsilon, d):
    """
    Compute overall gains for the three attacks on kRR.
    
    From Table 1:
    - RPA: β(r/d - f_T)
    - RIA: β(1 - f_T)
    - MGA: β(1 - f_T) + β(d-r)/(e^ε - 1)
    """
    e_eps = np.exp(epsilon)
    
    G_RPA = beta * (r / d - f_T)
    G_RIA = beta * (1 - f_T)
    G_MGA = beta * (1 - f_T) + beta * (d - r) / (e_eps - 1)
    
    return G_RPA, G_RIA, G_MGA

def compute_normalized_gains(G_RPA, G_RIA, G_MGA, f_T):
    """
    Normalized overall gain = (G + f_T) / f_T
    """
    norm_RPA = (G_RPA + f_T) / f_T
    norm_RIA = (G_RIA + f_T) / f_T
    norm_MGA = (G_MGA + f_T) / f_T
    return norm_RPA, norm_RIA, norm_MGA

# Parameter ranges based on Figure 1
beta_range = np.logspace(-3, -1, 20)  # 10^-3 to 10^-1
r_range = np.array([1, 5, 10, 15, 20])  # Match the discrete points in figure
fT_range = np.logspace(-3, -1, 20)  # 10^-3 to 10^-1
epsilon_range = np.linspace(0.5, 3.0, 20)  # 0.5 to 3.0
d_range = 2**np.arange(4, 13)  # 2^4 to 2^12

# Compute gains for each parameter variation

# 1. Varying β
G_RPA_beta, G_RIA_beta, G_MGA_beta = [], [], []
for beta in beta_range:
    rpa, ria, mga = compute_gains_kRR(beta, DEFAULT_R, DEFAULT_FT, DEFAULT_EPSILON, DEFAULT_D)
    G_RPA_beta.append(rpa)
    G_RIA_beta.append(ria)
    G_MGA_beta.append(mga)
G_RPA_beta = np.array(G_RPA_beta)
G_RIA_beta = np.array(G_RIA_beta)
G_MGA_beta = np.array(G_MGA_beta)
norm_RPA_beta, norm_RIA_beta, norm_MGA_beta = compute_normalized_gains(G_RPA_beta, G_RIA_beta, G_MGA_beta, DEFAULT_FT)

# 2. Varying r - f_T scales with r (f_T = r * 0.01)
G_RPA_r, G_RIA_r, G_MGA_r = [], [], []
fT_for_r = []
for r in r_range:
    f_T = r * 0.01  # f_T scales with number of target items
    fT_for_r.append(f_T)
    rpa, ria, mga = compute_gains_kRR(DEFAULT_BETA, r, f_T, DEFAULT_EPSILON, DEFAULT_D)
    G_RPA_r.append(rpa)
    G_RIA_r.append(ria)
    G_MGA_r.append(mga)
G_RPA_r = np.array(G_RPA_r)
G_RIA_r = np.array(G_RIA_r)
G_MGA_r = np.array(G_MGA_r)
fT_for_r = np.array(fT_for_r)
norm_RPA_r, norm_RIA_r, norm_MGA_r = compute_normalized_gains(G_RPA_r, G_RIA_r, G_MGA_r, fT_for_r)

# 3. Varying f_T
G_RPA_fT, G_RIA_fT, G_MGA_fT = [], [], []
for fT in fT_range:
    rpa, ria, mga = compute_gains_kRR(DEFAULT_BETA, DEFAULT_R, fT, DEFAULT_EPSILON, DEFAULT_D)
    G_RPA_fT.append(rpa)
    G_RIA_fT.append(ria)
    G_MGA_fT.append(mga)
G_RPA_fT = np.array(G_RPA_fT)
G_RIA_fT = np.array(G_RIA_fT)
G_MGA_fT = np.array(G_MGA_fT)
norm_RPA_fT, norm_RIA_fT, norm_MGA_fT = compute_normalized_gains(G_RPA_fT, G_RIA_fT, G_MGA_fT, fT_range)

# 4. Varying ε
G_RPA_eps, G_RIA_eps, G_MGA_eps = [], [], []
for eps in epsilon_range:
    rpa, ria, mga = compute_gains_kRR(DEFAULT_BETA, DEFAULT_R, DEFAULT_FT, eps, DEFAULT_D)
    G_RPA_eps.append(rpa)
    G_RIA_eps.append(ria)
    G_MGA_eps.append(mga)
G_RPA_eps = np.array(G_RPA_eps)
G_RIA_eps = np.array(G_RIA_eps)
G_MGA_eps = np.array(G_MGA_eps)
norm_RPA_eps, norm_RIA_eps, norm_MGA_eps = compute_normalized_gains(G_RPA_eps, G_RIA_eps, G_MGA_eps, DEFAULT_FT)

# 5. Varying d
G_RPA_d, G_RIA_d, G_MGA_d = [], [], []
for d in d_range:
    rpa, ria, mga = compute_gains_kRR(DEFAULT_BETA, DEFAULT_R, DEFAULT_FT, DEFAULT_EPSILON, d)
    G_RPA_d.append(rpa)
    G_RIA_d.append(ria)
    G_MGA_d.append(mga)
G_RPA_d = np.array(G_RPA_d)
G_RIA_d = np.array(G_RIA_d)
G_MGA_d = np.array(G_MGA_d)
norm_RPA_d, norm_RIA_d, norm_MGA_d = compute_normalized_gains(G_RPA_d, G_RIA_d, G_MGA_d, DEFAULT_FT)

# Create figure - match original dimensions
fig, axes = plt.subplots(2, 5, figsize=(17, 6.5))

# Colors matching the original figure exactly
color_RPA = '#1f77b4'  # Standard matplotlib blue
color_RIA = '#d97b0d'  # Orange/tan color matching original
color_MGA = '#2ca02c'  # Standard matplotlib green

marker_RPA = 'o'
marker_RIA = 'x'
marker_MGA = 's'

linestyle_RPA = '-'
linestyle_RIA = '--'
linestyle_MGA = ':'

markersize_default = 6
linewidth_default = 1.5

def plot_row(ax, x_data, y_rpa, y_ria, y_mga, xlabel, xscale='linear', 
             use_xticks=None, is_normalized=False, markevery=1):
    """Plot gains with appropriate scale"""
    
    ax.plot(x_data, y_rpa, color=color_RPA, marker=marker_RPA, linestyle=linestyle_RPA,
            label='RPA', markersize=markersize_default, linewidth=linewidth_default, 
            markerfacecolor=color_RPA, markevery=markevery)
    ax.plot(x_data, y_ria, color=color_RIA, marker=marker_RIA, linestyle=linestyle_RIA,
            label='RIA', markersize=markersize_default+1, linewidth=linewidth_default, 
            markeredgewidth=1.5, markevery=markevery)
    ax.plot(x_data, y_mga, color=color_MGA, marker=marker_MGA, linestyle=linestyle_MGA,
            label='MGA', markersize=markersize_default, linewidth=linewidth_default, 
            markerfacecolor=color_MGA, markevery=markevery)
    
    ax.set_xscale(xscale)
    ax.set_xlabel(xlabel, fontsize=12, fontstyle='italic')
    
    if is_normalized:
        ax.set_yscale('log')
        ax.set_ylim([10**0, 10**5])
        ax.set_yticks([10**0, 10**1, 10**2, 10**3, 10**4, 10**5])
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
            lambda x, p: f'$10^{{{int(np.log10(x))}}}$' if x >= 1 else f'{x:.0f}'))
    else:
        # Use symlog for non-normalized to show values crossing zero
        ax.set_yscale('symlog', linthresh=1e-2)
        ax.set_ylim([-10**-2, 10**2])
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        # Set y-axis ticks to match original
        ax.set_yticks([10**2, 10**1, 10**0, 10**-1, 10**-2, 0, -10**-2])
        # Custom formatter for symlog scale
        def symlog_formatter(x, p):
            if x == 0:
                return '0'
            elif x > 0:
                if x >= 1:
                    return f'$10^{{{int(np.log10(x))}}}$'
                else:
                    return f'$10^{{{int(np.log10(x))}}}$'
            else:
                return f'$-10^{{{int(np.log10(-x))}}}$'
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(symlog_formatter))
    
    if use_xticks is not None:
        ax.set_xticks(use_xticks)
        ax.set_xticklabels([f'$2^{{{int(np.log2(t))}}}$' for t in use_xticks])
    
    ax.legend(loc='best', fontsize=8, framealpha=0.95, edgecolor='none')
    ax.grid(True, alpha=0.3, which='major', linestyle='-', linewidth=0.5)

# Row 1: Overall Gains (G)
# β plot
ax = axes[0, 0]
plot_row(ax, beta_range, G_RPA_beta, G_RIA_beta, G_MGA_beta, r'$\beta$', xscale='log', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# r plot
ax = axes[0, 1]
plot_row(ax, r_range, G_RPA_r, G_RIA_r, G_MGA_r, r'$r$', xscale='linear')
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_xlim([0, 21])

# f_T plot
ax = axes[0, 2]
plot_row(ax, fT_range, G_RPA_fT, G_RIA_fT, G_MGA_fT, r'$f_T$', xscale='log', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# ε plot
ax = axes[0, 3]
plot_row(ax, epsilon_range, G_RPA_eps, G_RIA_eps, G_MGA_eps, r'$\varepsilon$', xscale='linear', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')
ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax.set_xlim([0.4, 3.1])

# d plot
ax = axes[0, 4]
plot_row(ax, d_range, G_RPA_d, G_RIA_d, G_MGA_d, r'$d$', xscale='log', use_xticks=d_range)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# Row 2: Normalized Overall Gains
# β plot
ax = axes[1, 0]
plot_row(ax, beta_range, norm_RPA_beta, norm_RIA_beta, norm_MGA_beta, r'$\beta$', 
         xscale='log', is_normalized=True, markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)

# r plot  
ax = axes[1, 1]
plot_row(ax, r_range, norm_RPA_r, norm_RIA_r, norm_MGA_r, r'$r$', 
         xscale='linear', is_normalized=True)
ax.set_ylabel('Normalized G', fontsize=11)
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_xlim([0, 21])

# f_T plot
ax = axes[1, 2]
plot_row(ax, fT_range, norm_RPA_fT, norm_RIA_fT, norm_MGA_fT, r'$f_T$', 
         xscale='log', is_normalized=True, markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)

# ε plot
ax = axes[1, 3]
plot_row(ax, epsilon_range, norm_RPA_eps, norm_RIA_eps, norm_MGA_eps, r'$\varepsilon$', 
         xscale='linear', is_normalized=True, markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)
ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax.set_xlim([0.4, 3.1])

# d plot
ax = axes[1, 4]
plot_row(ax, d_range, norm_RPA_d, norm_RIA_d, norm_MGA_d, r'$d$', 
         xscale='log', use_xticks=d_range, is_normalized=True)
ax.set_ylabel('Normalized G', fontsize=11)

plt.tight_layout(rect=[0, 0.05, 1, 1])

# Add caption below figure
fig.text(0.5, 0.01, 'Figure 1: Impact of different parameters on the overall gains (first row) and normalized overall gains (second row) of\nthe three attacks for kRR.', 
         ha='center', fontsize=11, fontweight='bold')

plt.savefig('fig1_recreated_final.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('fig1_recreated.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Figure saved!")

# Print verification values
print("\nVerification - computed gains with default parameters:")
print(f"Default: β={DEFAULT_BETA}, r={DEFAULT_R}, f_T={DEFAULT_FT}, ε={DEFAULT_EPSILON}, d={DEFAULT_D}")
rpa, ria, mga = compute_gains_kRR(DEFAULT_BETA, DEFAULT_R, DEFAULT_FT, DEFAULT_EPSILON, DEFAULT_D)
print(f"RPA: G = {rpa:.6f}")
print(f"RIA: G = {ria:.6f}")
print(f"MGA: G = {mga:.6f}")
print("\nNormalized gains:")
n_rpa, n_ria, n_mga = compute_normalized_gains(rpa, ria, mga, DEFAULT_FT)
print(f"RPA: Normalized G = {n_rpa:.2f}")
print(f"RIA: Normalized G = {n_ria:.2f}")
print(f"MGA: Normalized G = {n_mga:.2f}")