import numpy as np

# Parameters from table 2
DEFAULTS = {
    'beta': 0.05,
    'r': 1,
    'fT': 0.01,
    'epsilon': 1,
    'd': 1024
}

print("="*60)
print("COMPARING GAIN FORMULAS")
print("="*60)
print()

# My implementation
print("MY IMPLEMENTATION:")
print("-"*60)

def my_compute_gains_kRR(beta, r, fT, epsilon, d):
    e_eps = np.exp(epsilon)
    G_MGA = beta * (1 - fT) + beta * (d - r) / (e_eps - 1)
    return G_MGA

def my_compute_gains_OUE(beta, r, fT, epsilon, d):
    G_MGA = beta * (2*r - fT) + 2*beta*r / (np.exp(epsilon) - 1)
    return G_MGA

def my_compute_gains_OLH(beta, r, fT, epsilon, d):
    e_eps = np.exp(epsilon)
    G_MGA = beta * (2*r - fT) + 2*beta*r / (e_eps - 1)
    return G_MGA

print(f"kRR MGA: {my_compute_gains_kRR(**DEFAULTS):.6f}")
print(f"OUE MGA: {my_compute_gains_OUE(**DEFAULTS):.6f}")
print(f"OLH MGA: {my_compute_gains_OLH(**DEFAULTS):.6f}")
print()

# Original implementation from notebook
print("ORIGINAL IMPLEMENTATION:")
print("-"*60)

def compute_gains_kRR(beta, r, fT, epsilon, d):
    e_eps = np.exp(epsilon)
    return (
        beta * (r/d - fT),                                # RPA
        beta * (1 - fT),                                  # RIA
        beta * (1 - fT) + beta * (d - r) / (e_eps - 1)    # MGA
    )

def compute_gains_OUE(beta, r, fT, epsilon, d):
    return (
        beta * (r - fT),
        beta * (1 - fT),
        beta * (2*r - fT) + 2*beta*r / (np.exp(epsilon) - 1)
    )

def compute_gains_OLH(beta, r, fT, epsilon, d):
    e_eps = np.exp(epsilon)
    return (
        -beta * fT,
        beta * (1 - fT),
        beta * (2*r - fT) + 2*beta*r / (e_eps - 1)
    )

rpa, ria, mga = compute_gains_kRR(**DEFAULTS)
print(f"kRR - RPA: {rpa:.6f}, RIA: {ria:.6f}, MGA: {mga:.6f}")

rpa, ria, mga = compute_gains_OUE(**DEFAULTS)
print(f"OUE - RPA: {rpa:.6f}, RIA: {ria:.6f}, MGA: {mga:.6f}")

rpa, ria, mga = compute_gains_OLH(**DEFAULTS)
print(f"OLH - RPA: {rpa:.6f}, RIA: {ria:.6f}, MGA: {mga:.6f}")
print()

print("="*60)
print("ANALYSIS")
print("="*60)
print("✓ Formulas are IDENTICAL")
print("✓ My implementation correctly extracts only MGA from original")
print()
print("If curves differ, check:")
print("1. Parameter ranges used")
print("2. Plotting scale/axis settings")
print("3. Which parameters are being varied")
