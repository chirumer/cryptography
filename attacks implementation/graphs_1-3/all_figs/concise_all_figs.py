"""
Recreate Figures 1, 2, and 3 from "Data Poisoning Attacks to Local Differential Privacy Protocols"
Concise version with consolidated code for all three protocols: kRR, OUE, and OLH
"""

import numpy as np
import matplotlib.pyplot as plt

# Styling
plt.rcParams.update({'font.family': 'sans-serif', 'font.size': 10, 'axes.linewidth': 0.8,
                     'xtick.major.width': 0.8, 'ytick.major.width': 0.8})

# Colors and markers
COLORS = {'RPA': '#9467bd', 'RIA': '#e74c3c', 'MGA': '#17becf'}
MARKERS = {'RPA': 'o', 'RIA': 'x', 'MGA': 's'}
LINES = {'RPA': '-', 'RIA': '--', 'MGA': ':'}
SIZES = {'RPA': 5, 'RIA': 7, 'MGA': 5}

# Default parameters (Table 2)
DEFAULTS = {'beta': 0.05, 'r': 1, 'fT': 0.01, 'epsilon': 1, 'd': 1024}

# Parameter ranges
RANGES = {
    'beta': np.logspace(-3, -1, 20),
    'r': np.array([1, 5, 10, 15, 20]),
    'fT': np.logspace(-3, -1, 20),
    'epsilon': np.linspace(0.5, 3.0, 20),
    'd': 2**np.arange(4, 13)
}

# Gain formulas from Table 1
def compute_gains_kRR(beta, r, fT, epsilon, d):
    """kRR: RPA=β(r/d-fT), RIA=β(1-fT), MGA=β(1-fT)+β(d-r)/(e^ε-1)"""
    e_eps = np.exp(epsilon)
    return (beta * (r/d - fT), beta * (1 - fT), beta * (1 - fT) + beta * (d - r) / (e_eps - 1))

def compute_gains_OUE(beta, r, fT, epsilon, d):
    """OUE: RPA=β(r-fT), RIA=β(1-fT), MGA=β(2r-fT)+2βr/(e^ε-1)"""
    return (beta * (r - fT), beta * (1 - fT), beta * (2*r - fT) + 2*beta*r / (np.exp(epsilon) - 1))

def compute_gains_OLH(beta, r, fT, epsilon, d):
    """OLH: RPA=-β*fT, RIA=β(1-fT), MGA=β(2r-fT)+2βr/(e^ε-1)"""
    e_eps = np.exp(epsilon)
    return (-beta * fT, beta * (1 - fT), beta * (2*r - fT) + 2*beta*r / (e_eps - 1))

def normalized_gain(G, fT):
    """Normalized overall gain: (G + fT) / fT"""
    return (G + fT) / fT

def compute_all_gains(protocol_func, param_name, param_range, use_varying_fT=False):
    """Compute gains across a parameter range"""
    gains = {'RPA': [], 'RIA': [], 'MGA': []}
    
    for i, param_val in enumerate(param_range):
        params = DEFAULTS.copy()
        params[param_name] = param_val
        
        G_RPA, G_RIA, G_MGA = protocol_func(**params)
        gains['RPA'].append(G_RPA)
        gains['RIA'].append(G_RIA)
        gains['MGA'].append(G_MGA)
    
    # Convert to arrays
    for key in gains:
        gains[key] = np.array(gains[key])
    
    # Compute normalized gains
    fT_for_norm = param_range if use_varying_fT else DEFAULTS['fT']
    norm_gains = {key: normalized_gain(gains[key], fT_for_norm) for key in gains}
    
    return gains, norm_gains

def plot_row(ax, x_data, gains, xlabel, xscale, row_type, use_xticks=None, markevery=1):
    """Plot a single subplot"""
    for attack in ['RPA', 'RIA', 'MGA']:
        ax.plot(x_data, gains[attack], color=COLORS[attack], marker=MARKERS[attack],
                linestyle=LINES[attack], label=attack, markersize=SIZES[attack],
                linewidth=1.5, markerfacecolor=COLORS[attack] if attack != 'RIA' else None,
                markeredgewidth=2 if attack == 'RIA' else 1, markevery=markevery)
    
    ax.set_xscale(xscale)
    ax.set_xlabel(xlabel, fontsize=12, fontstyle='italic')
    ax.legend(loc='best', fontsize=8, framealpha=0.95, edgecolor='none')
    ax.grid(True, alpha=0.3, which='major', linestyle='-', linewidth=0.5)
    
    if row_type == 'top':
        ax.set_yscale('symlog', linthresh=1e-2)
        ax.set_ylim([-1e-2, 1e2])
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax.set_yticks([1e2, 1e1, 1e0, 1e-1, 1e-2, 0, -1e-2])
    else:  # bottom row
        ax.set_yscale('symlog', linthresh=1)
        ax.set_ylim([0, 1e5])
        ax.set_yticks([0, 1e0, 1e1, 1e2, 1e3, 1e4, 1e5])
    
    if use_xticks is not None:
        ax.set_xticks(use_xticks)
        ax.set_xticklabels([f'$2^{{{int(np.log2(t))}}}$' for t in use_xticks])

def plot_figure_OUE(ax, x_data, gains, xlabel, xscale, row_type, use_xticks=None, markevery=1):
    """Plot OUE (Figure 2) with log scale"""
    for attack in ['RPA', 'RIA', 'MGA']:
        ax.plot(x_data, gains[attack], color=COLORS[attack], marker=MARKERS[attack],
                linestyle=LINES[attack], label=attack, markersize=SIZES[attack],
                linewidth=1.5, markerfacecolor=COLORS[attack] if attack != 'RIA' else None,
                markeredgewidth=2 if attack == 'RIA' else 1)
    
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_xscale(xscale)
    ax.set_yscale('log')
    ax.set_ylim(1e-3, 1e1) if row_type == 'top' else ax.set_ylim(1e0, 1e3)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=8)
    
    if use_xticks is not None:
        ax.set_xticks(use_xticks)
        ax.set_xticklabels([f'$2^{{{int(np.log2(d))}}}$' for d in use_xticks], fontsize=8)

def create_figure(protocol_func, protocol_name, use_log_for_oue=False):
    """Generate a complete figure for a protocol"""
    fig, axes = plt.subplots(2, 5, figsize=(17, 6.5))
    
    param_configs = [
        ('beta', r'$\beta$', 'log', None, 2),
        ('r', r'$r$', 'linear', [1, 5, 10, 15, 20], 1),
        ('fT', r'$f_T$', 'log', None, 2),
        ('epsilon', r'$\varepsilon$', 'linear', [0.5, 1.0, 1.5, 2.0, 2.5, 3.0], 2),
        ('d', r'$d$', 'log', RANGES['d'], 1)
    ]
    
    for col, (param_name, xlabel, xscale, xticks, markevery) in enumerate(param_configs):
        use_varying_fT = (param_name == 'fT')
        gains, norm_gains = compute_all_gains(protocol_func, param_name, RANGES[param_name], use_varying_fT)
        
        # Top row: Overall gains
        if use_log_for_oue:
            plot_figure_OUE(axes[0, col], RANGES[param_name], gains, xlabel, xscale, 'top', xticks, markevery)
            axes[0, col].set_ylabel('G', fontsize=12)
        else:
            plot_row(axes[0, col], RANGES[param_name], gains, xlabel, xscale, 'top', xticks, markevery)
            axes[0, col].set_ylabel(r'$G$', fontsize=12, fontstyle='italic')
        
        # Bottom row: Normalized gains
        if use_log_for_oue:
            plot_figure_OUE(axes[1, col], RANGES[param_name], norm_gains, xlabel, xscale, 'bottom', xticks, markevery)
            axes[1, col].set_ylabel('Normalized G', fontsize=11)
        else:
            plot_row(axes[1, col], RANGES[param_name], norm_gains, xlabel, xscale, 'bottom', xticks, markevery)
            axes[1, col].set_ylabel('Normalized G', fontsize=11)
        
        # Set x-axis limits for r and epsilon
        if param_name == 'r':
            axes[0, col].set_xlim([0, 21])
            axes[1, col].set_xlim([0, 21])
        elif param_name == 'epsilon':
            axes[0, col].set_xlim([0.4, 3.1])
            axes[1, col].set_xlim([0.4, 3.1])
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    fig.text(0.5, 0.01, 
             f'Figure: Impact of different parameters on the overall gains (first row) and normalized overall gains (second row) of\\nthe three attacks for {protocol_name}.',
             ha='center', fontsize=11, fontweight='bold')
    
    return fig

# Generate all three figures
print("Generating Figure 1 (kRR)...")
fig1 = create_figure(compute_gains_kRR, 'kRR', use_log_for_oue=False)
fig1.savefig('fig1_recreated.png', dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Figure 1 saved!")

print("Generating Figure 2 (OUE)...")
fig2 = create_figure(compute_gains_OUE, 'OUE', use_log_for_oue=True)
fig2.savefig('fig2_recreated.png', dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Figure 2 saved!")

print("Generating Figure 3 (OLH)...")
fig3 = create_figure(compute_gains_OLH, 'OLH', use_log_for_oue=False)
fig3.savefig('fig3_recreated.png', dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Figure 3 saved!")

plt.close('all')
print("\n✅ All figures generated successfully!")
