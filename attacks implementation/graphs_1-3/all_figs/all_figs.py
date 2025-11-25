# ===== From /mnt/data/fig1.py =====
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

KEY INSIGHT: When varying any parameter, f_T stays constant at 0.01 for both
G calculation and normalization. This keeps RIA and MGA constant when varying r.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter, ScalarFormatter
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

# 1. Varying β (f_T = 0.01 constant)
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

# 2. Varying r 
# Use f_T = 0.01 (constant) for BOTH G calculation AND normalization
# This keeps RIA and MGA normalized gains constant
G_RPA_r, G_RIA_r, G_MGA_r = [], [], []
for r in r_range:
    rpa, ria, mga = compute_gains_kRR(DEFAULT_BETA, r, DEFAULT_FT, DEFAULT_EPSILON, DEFAULT_D)
    G_RPA_r.append(rpa)
    G_RIA_r.append(ria)
    G_MGA_r.append(mga)

G_RPA_r = np.array(G_RPA_r)
G_RIA_r = np.array(G_RIA_r)
G_MGA_r = np.array(G_MGA_r)
# Use constant f_T = 0.01 for normalization (keeps RIA and MGA constant)
norm_RPA_r, norm_RIA_r, norm_MGA_r = compute_normalized_gains(G_RPA_r, G_RIA_r, G_MGA_r, DEFAULT_FT)

# 3. Varying f_T (r = 1, constant)
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

# 4. Varying ε (f_T = 0.01 constant)
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

# 5. Varying d (f_T = 0.01 constant)
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

# New color scheme - different from original paper
color_RPA = '#9467bd'  # Purple
color_RIA = '#e74c3c'  # Red
color_MGA = '#17becf'  # Cyan/Teal

marker_RPA = 'o'  # circle
marker_RIA = 'x'  # x
marker_MGA = 's'  # square

# Try different markers - using filled circle, x with thicker lines, filled square with edge
markersize_RPA = 5
markersize_RIA = 7
markersize_MGA = 5

linestyle_RPA = '-'
linestyle_RIA = '--'
linestyle_MGA = ':'

linewidth_default = 1.5

def plot_top_row(ax, x_data, y_rpa, y_ria, y_mga, xlabel, xscale='linear', 
                 use_xticks=None, markevery=1):
    """Plot gains for top row with symlog scale"""
    
    ax.plot(x_data, y_rpa, color=color_RPA, marker=marker_RPA, linestyle=linestyle_RPA,
            label='RPA', markersize=markersize_RPA, linewidth=linewidth_default, 
            markerfacecolor=color_RPA, markevery=markevery)
    ax.plot(x_data, y_ria, color=color_RIA, marker=marker_RIA, linestyle=linestyle_RIA,
            label='RIA', markersize=markersize_RIA, linewidth=linewidth_default, 
            markeredgewidth=2, markevery=markevery)
    ax.plot(x_data, y_mga, color=color_MGA, marker=marker_MGA, linestyle=linestyle_MGA,
            label='MGA', markersize=markersize_MGA, linewidth=linewidth_default, 
            markerfacecolor=color_MGA, markevery=markevery)
    
    ax.set_xscale(xscale)
    ax.set_xlabel(xlabel, fontsize=12, fontstyle='italic')
    
    # Use symlog scale for top row
    ax.set_yscale('symlog', linthresh=1e-2)
    ax.set_ylim([-10**-2, 10**2])
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.set_yticks([10**2, 10**1, 10**0, 10**-1, 10**-2, 0, -10**-2])
    
    if use_xticks is not None:
        ax.set_xticks(use_xticks)
        ax.set_xticklabels([f'$2^{{{int(np.log2(t))}}}$' for t in use_xticks])
    
    ax.legend(loc='best', fontsize=8, framealpha=0.95, edgecolor='none')
    ax.grid(True, alpha=0.3, which='major', linestyle='-', linewidth=0.5)

def plot_bottom_row(ax, x_data, y_rpa, y_ria, y_mga, xlabel, xscale='linear', 
                    use_xticks=None, markevery=1):
    """Plot normalized gains for bottom row - includes 0 on y-axis"""
    
    ax.plot(x_data, y_rpa, color=color_RPA, marker=marker_RPA, linestyle=linestyle_RPA,
            label='RPA', markersize=markersize_RPA, linewidth=linewidth_default, 
            markerfacecolor=color_RPA, markevery=markevery)
    ax.plot(x_data, y_ria, color=color_RIA, marker=marker_RIA, linestyle=linestyle_RIA,
            label='RIA', markersize=markersize_RIA, linewidth=linewidth_default, 
            markeredgewidth=2, markevery=markevery)
    ax.plot(x_data, y_mga, color=color_MGA, marker=marker_MGA, linestyle=linestyle_MGA,
            label='MGA', markersize=markersize_MGA, linewidth=linewidth_default, 
            markerfacecolor=color_MGA, markevery=markevery)
    
    ax.set_xscale(xscale)
    ax.set_xlabel(xlabel, fontsize=12, fontstyle='italic')
    
    # Use symlog scale starting from 0 for bottom row
    ax.set_yscale('symlog', linthresh=1)
    ax.set_ylim([0, 10**5])
    ax.set_yticks([0, 10**0, 10**1, 10**2, 10**3, 10**4, 10**5])
    
    if use_xticks is not None:
        ax.set_xticks(use_xticks)
        ax.set_xticklabels([f'$2^{{{int(np.log2(t))}}}$' for t in use_xticks])
    
    ax.legend(loc='best', fontsize=8, framealpha=0.95, edgecolor='none')
    ax.grid(True, alpha=0.3, which='major', linestyle='-', linewidth=0.5)

# Row 1: Overall Gains (G)
# β plot
ax = axes[0, 0]
plot_top_row(ax, beta_range, G_RPA_beta, G_RIA_beta, G_MGA_beta, r'$\beta$', xscale='log', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# r plot
ax = axes[0, 1]
plot_top_row(ax, r_range, G_RPA_r, G_RIA_r, G_MGA_r, r'$r$', xscale='linear')
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_xlim([0, 21])

# f_T plot
ax = axes[0, 2]
plot_top_row(ax, fT_range, G_RPA_fT, G_RIA_fT, G_MGA_fT, r'$f_T$', xscale='log', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# ε plot
ax = axes[0, 3]
plot_top_row(ax, epsilon_range, G_RPA_eps, G_RIA_eps, G_MGA_eps, r'$\varepsilon$', xscale='linear', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')
ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax.set_xlim([0.4, 3.1])

# d plot
ax = axes[0, 4]
plot_top_row(ax, d_range, G_RPA_d, G_RIA_d, G_MGA_d, r'$d$', xscale='log', use_xticks=d_range)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# Row 2: Normalized Overall Gains
# β plot
ax = axes[1, 0]
plot_bottom_row(ax, beta_range, norm_RPA_beta, norm_RIA_beta, norm_MGA_beta, r'$\beta$', 
                xscale='log', markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)

# r plot  
ax = axes[1, 1]
plot_bottom_row(ax, r_range, norm_RPA_r, norm_RIA_r, norm_MGA_r, r'$r$', xscale='linear')
ax.set_ylabel('Normalized G', fontsize=11)
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_xlim([0, 21])

# f_T plot
ax = axes[1, 2]
plot_bottom_row(ax, fT_range, norm_RPA_fT, norm_RIA_fT, norm_MGA_fT, r'$f_T$', 
                xscale='log', markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)

# ε plot
ax = axes[1, 3]
plot_bottom_row(ax, epsilon_range, norm_RPA_eps, norm_RIA_eps, norm_MGA_eps, r'$\varepsilon$', 
                xscale='linear', markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)
ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax.set_xlim([0.4, 3.1])

# d plot
ax = axes[1, 4]
plot_bottom_row(ax, d_range, norm_RPA_d, norm_RIA_d, norm_MGA_d, r'$d$', 
                xscale='log', use_xticks=d_range)
ax.set_ylabel('Normalized G', fontsize=11)

plt.tight_layout(rect=[0, 0.05, 1, 1])

# Add caption below figure
fig.text(0.5, 0.01, 'Figure 1: Impact of different parameters on the overall gains (first row) and normalized overall gains (second row) of\nthe three attacks for kRR.', 
         ha='center', fontsize=11, fontweight='bold')

plt.savefig('fig1_recreated.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Figure saved!")

# ===== From /mnt/data/fig2.py =====
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
    ax.set_ylim(1e-3, 1e1)
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

plt.savefig('fig2_recreated.png', dpi=150, bbox_inches='tight')
print("Figure saved!")

# ===== From /mnt/data/fig3.py =====
"""
Recreate Figure 3 from "Data Poisoning Attacks to Local Differential Privacy Protocols"
Impact of different parameters on the overall gains (first row) and normalized overall gains 
(second row) of the three attacks for OLH.

From Table 1 in the paper:
- RPA: G = -β*f_T
- RIA: G = β(1 - f_T)
- MGA: G = β(2r - f_T) + 2βr/(e^ε - 1)

Default parameters from Table 2:
- β = 0.05
- r = 1
- f_T = 0.01
- ε = 1
- k = 20 (not used for frequency estimation)
- g = 10 (not used for frequency estimation)
- d = 1024 (from Section 5.1: "By default, we synthesize a dataset with 1,024 items")

KEY INSIGHT: When varying any parameter, f_T stays constant at 0.01 for both
G calculation and normalization. This keeps RIA and MGA constant when varying r.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter, ScalarFormatter
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

def compute_gains_OLH(beta, r, f_T, epsilon, d):
    """
    Compute overall gains for the three attacks on OLH.
    
    From Table 1:
    - RPA: -β*f_T
    - RIA: β(1 - f_T)
    - MGA: β(2r - f_T) + 2βr/(e^ε - 1)
    """
    e_eps = np.exp(epsilon)
    
    G_RPA = -beta * f_T
    G_RIA = beta * (1 - f_T)
    G_MGA = beta * (2*r - f_T) + (2 * beta * r) / (e_eps - 1)
    
    return G_RPA, G_RIA, G_MGA

def compute_normalized_gains(G_RPA, G_RIA, G_MGA, f_T):
    """
    Normalized overall gain = (G + f_T) / f_T
    """
    norm_RPA = (G_RPA + f_T) / f_T
    norm_RIA = (G_RIA + f_T) / f_T
    norm_MGA = (G_MGA + f_T) / f_T
    return norm_RPA, norm_RIA, norm_MGA

# Parameter ranges based on Figure 3
beta_range = np.logspace(-3, -1, 20)  # 10^-3 to 10^-1
r_range = np.array([1, 5, 10, 15, 20])  # Match the discrete points in figure
fT_range = np.logspace(-3, -1, 20)  # 10^-3 to 10^-1
epsilon_range = np.linspace(0.5, 3.0, 20)  # 0.5 to 3.0
d_range = 2**np.arange(4, 13)  # 2^4 to 2^12

# Compute gains for each parameter variation

# 1. Varying β (f_T = 0.01 constant)
G_RPA_beta, G_RIA_beta, G_MGA_beta = [], [], []
for beta in beta_range:
    rpa, ria, mga = compute_gains_OLH(beta, DEFAULT_R, DEFAULT_FT, DEFAULT_EPSILON, DEFAULT_D)
    G_RPA_beta.append(rpa)
    G_RIA_beta.append(ria)
    G_MGA_beta.append(mga)
G_RPA_beta = np.array(G_RPA_beta)
G_RIA_beta = np.array(G_RIA_beta)
G_MGA_beta = np.array(G_MGA_beta)
norm_RPA_beta, norm_RIA_beta, norm_MGA_beta = compute_normalized_gains(G_RPA_beta, G_RIA_beta, G_MGA_beta, DEFAULT_FT)

# 2. Varying r 
# Use f_T = 0.01 (constant) for BOTH G calculation AND normalization
# This keeps RIA normalized gains constant
G_RPA_r, G_RIA_r, G_MGA_r = [], [], []
for r in r_range:
    rpa, ria, mga = compute_gains_OLH(DEFAULT_BETA, r, DEFAULT_FT, DEFAULT_EPSILON, DEFAULT_D)
    G_RPA_r.append(rpa)
    G_RIA_r.append(ria)
    G_MGA_r.append(mga)

G_RPA_r = np.array(G_RPA_r)
G_RIA_r = np.array(G_RIA_r)
G_MGA_r = np.array(G_MGA_r)
# Use constant f_T = 0.01 for normalization (keeps RIA constant)
norm_RPA_r, norm_RIA_r, norm_MGA_r = compute_normalized_gains(G_RPA_r, G_RIA_r, G_MGA_r, DEFAULT_FT)

# 3. Varying f_T (r = 1, constant)
G_RPA_fT, G_RIA_fT, G_MGA_fT = [], [], []
for fT in fT_range:
    rpa, ria, mga = compute_gains_OLH(DEFAULT_BETA, DEFAULT_R, fT, DEFAULT_EPSILON, DEFAULT_D)
    G_RPA_fT.append(rpa)
    G_RIA_fT.append(ria)
    G_MGA_fT.append(mga)
G_RPA_fT = np.array(G_RPA_fT)
G_RIA_fT = np.array(G_RIA_fT)
G_MGA_fT = np.array(G_MGA_fT)
norm_RPA_fT, norm_RIA_fT, norm_MGA_fT = compute_normalized_gains(G_RPA_fT, G_RIA_fT, G_MGA_fT, fT_range)

# 4. Varying ε (f_T = 0.01 constant)
G_RPA_eps, G_RIA_eps, G_MGA_eps = [], [], []
for eps in epsilon_range:
    rpa, ria, mga = compute_gains_OLH(DEFAULT_BETA, DEFAULT_R, DEFAULT_FT, eps, DEFAULT_D)
    G_RPA_eps.append(rpa)
    G_RIA_eps.append(ria)
    G_MGA_eps.append(mga)
G_RPA_eps = np.array(G_RPA_eps)
G_RIA_eps = np.array(G_RIA_eps)
G_MGA_eps = np.array(G_MGA_eps)
norm_RPA_eps, norm_RIA_eps, norm_MGA_eps = compute_normalized_gains(G_RPA_eps, G_RIA_eps, G_MGA_eps, DEFAULT_FT)

# 5. Varying d (f_T = 0.01 constant)
G_RPA_d, G_RIA_d, G_MGA_d = [], [], []
for d in d_range:
    rpa, ria, mga = compute_gains_OLH(DEFAULT_BETA, DEFAULT_R, DEFAULT_FT, DEFAULT_EPSILON, d)
    G_RPA_d.append(rpa)
    G_RIA_d.append(ria)
    G_MGA_d.append(mga)
G_RPA_d = np.array(G_RPA_d)
G_RIA_d = np.array(G_RIA_d)
G_MGA_d = np.array(G_MGA_d)
norm_RPA_d, norm_RIA_d, norm_MGA_d = compute_normalized_gains(G_RPA_d, G_RIA_d, G_MGA_d, DEFAULT_FT)

# Create figure - match original dimensions
fig, axes = plt.subplots(2, 5, figsize=(17, 6.5))

# New color scheme - different from original paper
color_RPA = '#9467bd'  # Purple
color_RIA = '#e74c3c'  # Red
color_MGA = '#17becf'  # Cyan/Teal

marker_RPA = 'o'  # circle
marker_RIA = 'x'  # x
marker_MGA = 's'  # square

# Try different markers - using filled circle, x with thicker lines, filled square with edge
markersize_RPA = 5
markersize_RIA = 7
markersize_MGA = 5

linestyle_RPA = '-'
linestyle_RIA = '--'
linestyle_MGA = ':'

linewidth_default = 1.5

def plot_top_row(ax, x_data, y_rpa, y_ria, y_mga, xlabel, xscale='linear', 
                 use_xticks=None, markevery=1):
    """Plot gains for top row with symlog scale"""
    
    ax.plot(x_data, y_rpa, color=color_RPA, marker=marker_RPA, linestyle=linestyle_RPA,
            label='RPA', markersize=markersize_RPA, linewidth=linewidth_default, 
            markerfacecolor=color_RPA, markevery=markevery)
    ax.plot(x_data, y_ria, color=color_RIA, marker=marker_RIA, linestyle=linestyle_RIA,
            label='RIA', markersize=markersize_RIA, linewidth=linewidth_default, 
            markeredgewidth=2, markevery=markevery)
    ax.plot(x_data, y_mga, color=color_MGA, marker=marker_MGA, linestyle=linestyle_MGA,
            label='MGA', markersize=markersize_MGA, linewidth=linewidth_default, 
            markerfacecolor=color_MGA, markevery=markevery)
    
    ax.set_xscale(xscale)
    ax.set_xlabel(xlabel, fontsize=12, fontstyle='italic')
    
    # Use symlog scale for top row
    ax.set_yscale('symlog', linthresh=1e-2)
    ax.set_ylim([-10**-2, 10**2])
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.set_yticks([10**2, 10**1, 10**0, 10**-1, 10**-2, 0, -10**-2])
    
    if use_xticks is not None:
        ax.set_xticks(use_xticks)
        ax.set_xticklabels([f'$2^{{{int(np.log2(t))}}}$' for t in use_xticks])
    
    ax.legend(loc='best', fontsize=8, framealpha=0.95, edgecolor='none')
    ax.grid(True, alpha=0.3, which='major', linestyle='-', linewidth=0.5)

def plot_bottom_row(ax, x_data, y_rpa, y_ria, y_mga, xlabel, xscale='linear', 
                    use_xticks=None, markevery=1):
    """Plot normalized gains for bottom row - includes 0 on y-axis"""
    
    ax.plot(x_data, y_rpa, color=color_RPA, marker=marker_RPA, linestyle=linestyle_RPA,
            label='RPA', markersize=markersize_RPA, linewidth=linewidth_default, 
            markerfacecolor=color_RPA, markevery=markevery)
    ax.plot(x_data, y_ria, color=color_RIA, marker=marker_RIA, linestyle=linestyle_RIA,
            label='RIA', markersize=markersize_RIA, linewidth=linewidth_default, 
            markeredgewidth=2, markevery=markevery)
    ax.plot(x_data, y_mga, color=color_MGA, marker=marker_MGA, linestyle=linestyle_MGA,
            label='MGA', markersize=markersize_MGA, linewidth=linewidth_default, 
            markerfacecolor=color_MGA, markevery=markevery)
    
    ax.set_xscale(xscale)
    ax.set_xlabel(xlabel, fontsize=12, fontstyle='italic')
    
    # Use symlog scale starting from 0 for bottom row
    ax.set_yscale('symlog', linthresh=1)
    ax.set_ylim([0, 10**5])
    ax.set_yticks([0, 10**0, 10**1, 10**2, 10**3, 10**4, 10**5])
    
    if use_xticks is not None:
        ax.set_xticks(use_xticks)
        ax.set_xticklabels([f'$2^{{{int(np.log2(t))}}}$' for t in use_xticks])
    
    ax.legend(loc='best', fontsize=8, framealpha=0.95, edgecolor='none')
    ax.grid(True, alpha=0.3, which='major', linestyle='-', linewidth=0.5)

# Row 1: Overall Gains (G)
# β plot
ax = axes[0, 0]
plot_top_row(ax, beta_range, G_RPA_beta, G_RIA_beta, G_MGA_beta, r'$\beta$', xscale='log', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# r plot
ax = axes[0, 1]
plot_top_row(ax, r_range, G_RPA_r, G_RIA_r, G_MGA_r, r'$r$', xscale='linear')
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_xlim([0, 21])

# f_T plot
ax = axes[0, 2]
plot_top_row(ax, fT_range, G_RPA_fT, G_RIA_fT, G_MGA_fT, r'$f_T$', xscale='log', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# ε plot
ax = axes[0, 3]
plot_top_row(ax, epsilon_range, G_RPA_eps, G_RIA_eps, G_MGA_eps, r'$\varepsilon$', xscale='linear', markevery=2)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')
ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax.set_xlim([0.4, 3.1])

# d plot
ax = axes[0, 4]
plot_top_row(ax, d_range, G_RPA_d, G_RIA_d, G_MGA_d, r'$d$', xscale='log', use_xticks=d_range)
ax.set_ylabel(r'$G$', fontsize=12, fontstyle='italic')

# Row 2: Normalized Overall Gains
# β plot
ax = axes[1, 0]
plot_bottom_row(ax, beta_range, norm_RPA_beta, norm_RIA_beta, norm_MGA_beta, r'$\beta$', 
                xscale='log', markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)

# r plot  
ax = axes[1, 1]
plot_bottom_row(ax, r_range, norm_RPA_r, norm_RIA_r, norm_MGA_r, r'$r$', xscale='linear')
ax.set_ylabel('Normalized G', fontsize=11)
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_xlim([0, 21])

# f_T plot
ax = axes[1, 2]
plot_bottom_row(ax, fT_range, norm_RPA_fT, norm_RIA_fT, norm_MGA_fT, r'$f_T$', 
                xscale='log', markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)

# ε plot
ax = axes[1, 3]
plot_bottom_row(ax, epsilon_range, norm_RPA_eps, norm_RIA_eps, norm_MGA_eps, r'$\varepsilon$', 
                xscale='linear', markevery=2)
ax.set_ylabel('Normalized G', fontsize=11)
ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax.set_xlim([0.4, 3.1])

# d plot
ax = axes[1, 4]
plot_bottom_row(ax, d_range, norm_RPA_d, norm_RIA_d, norm_MGA_d, r'$d$', 
                xscale='log', use_xticks=d_range)
ax.set_ylabel('Normalized G', fontsize=11)

plt.tight_layout(rect=[0, 0.05, 1, 1])

# Add caption below figure
fig.text(0.5, 0.01, 'Figure 3: Impact of different parameters on the overall gains (first row) and normalized overall gains (second row) of\nthe three attacks for OLH.', 
         ha='center', fontsize=11, fontweight='bold')

plt.savefig('fig3_recreated.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Figure 3 saved as fig3_recreated.png!")


