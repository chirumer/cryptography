#!/usr/bin/env python3
"""
Generate LaTeX description files with EXACT term definitions matching each equation.
Each term in the equation must be defined, and only terms in that equation.
"""

from pathlib import Path

# Verified equations and their EXACT term definitions
EQUATIONS = {
    # image1: Pr[M(x) ∈ S] ≤ e^ε Pr[M(y) ∈ S] + ε
    "image1": {
        "name": "Differential Privacy Definition",
        "terms": [
            (r"\Pr", "Probability"),
            (r"\mathcal{M}", "Randomized mechanism"),
            (r"x, y", "Neighboring datasets"),
            (r"S", "Set of possible outputs"),
            (r"e^\varepsilon", "Privacy loss bound"),
            (r"\varepsilon", "Privacy parameter"),
        ]
    },
    # image2: Pr[A(v1) = y] ≤ e^ε Pr[A(v2) = y]
    "image2": {
        "name": "Local Differential Privacy (LDP)",
        "terms": [
            (r"\Pr", "Probability"),
            (r"\mathcal{A}", "LDP algorithm"),
            (r"v_1, v_2", "Any two input values"),
            (r"y", "Output value"),
            (r"e^\varepsilon", "Privacy loss bound"),
            (r"\varepsilon", "Privacy parameter"),
        ]
    },
    # image3: Pr(PE(v1) = y) ≤ e^ε Pr(PE(v2) = y)
    "image3": {
        "name": "LDP for Perturb-Encode",
        "terms": [
            (r"\Pr", "Probability"),
            (r"\text{PE}", "Perturb-Encode function"),
            (r"v_1, v_2", "Any two input values"),
            (r"y", "Perturbed output"),
            (r"e^\varepsilon", "Privacy loss bound"),
        ]
    },
    # image4: Pr[PE(v1) ∈ {y | v1 ∈ Support(y)}] = p
    "image4": {
        "name": "Support Probability (True Positive)",
        "terms": [
            (r"\Pr", "Probability"),
            (r"\text{PE}", "Perturb-Encode function"),
            (r"v_1", "User's true value"),
            (r"y", "Perturbed output"),
            (r"\text{Support}(y)", "Set of values y supports"),
            (r"p", "True positive probability"),
        ]
    },
    # image5: Pr(PE(v1) ∈ {y | v1 ∈ S(y)}) = p
    "image5": {
        "name": "Support Set Probability p",
        "terms": [
            (r"\Pr", "Probability"),
            (r"\text{PE}", "Perturb-Encode function"),
            (r"v_1", "User's true value"),
            (r"y", "Perturbed output"),
            (r"S(y)", "Support set of y"),
            (r"p", "True positive probability"),
        ]
    },
    # image6: Pr(PE(v2) ∈ {y | v1 ∈ S(y)}) = q
    "image6": {
        "name": "Support Set Probability q",
        "terms": [
            (r"\Pr", "Probability"),
            (r"\text{PE}", "Perturb-Encode function"),
            (r"v_1, v_2", "Different input values"),
            (r"y", "Perturbed output"),
            (r"S(y)", "Support set of y"),
            (r"q", "False positive probability"),
        ]
    },
    # image7: f̃_v = (1/n) Σ (1_{S(y_i)}(v) - q) / (p - q)
    "image7": {
        "name": "Frequency Estimation Formula",
        "terms": [
            (r"\tilde{f}_v", "Estimated frequency of item v"),
            (r"n", "Total number of users"),
            (r"\mathbf{1}_{S(y_i)}(v)", "Indicator: 1 if v in S(y_i)"),
            (r"y_i", "Perturbed value from user i"),
            (r"p", "True positive probability"),
            (r"q", "False positive probability"),
        ]
    },
    # image8: Σ E[1_{S(y_i)}(v)] = n(f_v(p-q) + q)
    "image8": {
        "name": "Expected Support Count",
        "terms": [
            (r"\sum_{i=1}^{n}", "Sum over all n users"),
            (r"\mathbb{E}", "Expected value"),
            (r"\mathbf{1}_{S(y_i)}(v)", "Indicator function"),
            (r"f_v", "True frequency of item v"),
            (r"p", "True positive probability"),
            (r"q", "False positive probability"),
        ]
    },
    # image9: Pr(S_i=1) = {q if B0[i]=1, p if B0[i]=0}
    "image9": {
        "name": "RAPPOR Bit Perturbation",
        "terms": [
            (r"\Pr", "Probability"),
            (r"S_i", "Perturbed bit at position i"),
            (r"B_0[i]", "Original bit at position i"),
            (r"p", "Probability bit 0 flips to 1"),
            (r"q", "Probability bit 1 stays 1"),
        ]
    },
    # image10: Pr(y_i=1) = {p=1/2 if i=v, q=1/(e^ε+1) otherwise}
    "image10": {
        "name": "OUE Perturbation Probabilities",
        "terms": [
            (r"\Pr", "Probability"),
            (r"y_i", "Perturbed bit at position i"),
            (r"i", "Bit position index"),
            (r"v", "User's true value"),
            (r"p = \frac{1}{2}", "True bit probability"),
            (r"q = \frac{1}{e^\varepsilon+1}", "False bit probability"),
        ]
    },
    # image11: Pr(y=(H,a)) = {p if a=H(v), q otherwise}
    "image11": {
        "name": "OLH Perturbation Probabilities",
        "terms": [
            (r"\Pr", "Probability"),
            (r"y = (H, a)", "Perturbed output tuple"),
            (r"H", "Hash function"),
            (r"a", "Hash output value"),
            (r"v", "User's true value"),
            (r"d'", "Hash domain size"),
            (r"p, q", "Perturbation probabilities"),
        ]
    },
    # image12: Pr(y=a) = {p if a=v, q otherwise}
    "image12": {
        "name": "k-RR Randomized Response",
        "terms": [
            (r"\Pr", "Probability"),
            (r"y", "Reported value"),
            (r"a", "Possible output value"),
            (r"v", "User's true value"),
            (r"d", "Domain size"),
            (r"p", "Probability of true report"),
            (r"q", "Probability of false report"),
        ]
    },
    # image13: Var[f̃_v] = q(1-q)/(n(p-q)^2) + f_v(1-f_v)/n
    "image13": {
        "name": "Variance of Frequency Estimator",
        "terms": [
            (r"\text{Var}", "Variance operator"),
            (r"\tilde{f}_v", "Estimated frequency"),
            (r"f_v", "True frequency of item v"),
            (r"n", "Number of users"),
            (r"p", "True positive probability"),
            (r"q", "False positive probability"),
        ]
    },
    # image14: Gain_MGA = m/(n+m) · (p-q)/c
    "image14": {
        "name": "Maximal Gain Attack (MGA)",
        "terms": [
            (r"\text{Gain}_{\text{MGA}}", "Attack gain for MGA"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p", "True positive probability"),
            (r"q", "False positive probability"),
            (r"c", "Normalization constant"),
        ]
    },
    # image15: f̃'_t = f̃_t + Gain_MGA
    "image15": {
        "name": "Boosted Frequency (Target)",
        "terms": [
            (r"\tilde{f}'_t", "Target frequency after attack"),
            (r"\tilde{f}_t", "Original target frequency"),
            (r"\text{Gain}_{\text{MGA}}", "MGA attack gain"),
            (r"t", "Target item index"),
        ]
    },
    # image16: f̃'_i = f̃_i - mq/((n+m)(p-q)) for all i≠t
    "image16": {
        "name": "Reduced Frequency (Non-target)",
        "terms": [
            (r"\tilde{f}'_i", "Item frequency after attack"),
            (r"\tilde{f}_i", "Original item frequency"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p, q", "Support probabilities"),
            (r"i \neq t", "Non-target items"),
        ]
    },
    # image17: G_RIA = mp/((n+m)(p-q))
    "image17": {
        "name": "Random Input Attack Gain",
        "terms": [
            (r"G_{\text{RIA}}", "Random Input Attack gain"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p", "True positive probability"),
            (r"q", "False positive probability"),
        ]
    },
    # image18: f = 1/(e^(ε/2) + 1)
    "image18": {
        "name": "RAPPOR Permanent Parameter",
        "terms": [
            (r"f", "Permanent randomization parameter"),
            (r"e^{\varepsilon/2}", "Exponential of half epsilon"),
            (r"\varepsilon", "Privacy parameter"),
        ]
    },
    # image19: c̃(i) = (Σ_j 1_{B_j[i]=1} - fn/2) / (1-f)
    "image19": {
        "name": "RAPPOR Frequency Estimation",
        "terms": [
            (r"\tilde{c}(i)", "Estimated count for item i"),
            (r"\sum_j", "Sum over all users j"),
            (r"\mathbf{1}", "Indicator function"),
            (r"B_j[i]", "Bit i of user j's report"),
            (r"f", "Permanent randomization parameter"),
            (r"n", "Number of users"),
        ]
    },
    # image21: G_kRR-MGA = m/((n+m)(p-q)) · c
    "image21": {
        "name": "kRR MGA Gain",
        "terms": [
            (r"G_{\text{kRR-MGA}}", "kRR MGA attack gain"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p", "True positive probability"),
            (r"q", "False positive probability"),
            (r"c", "Protocol constant"),
        ]
    },
    # image22: G_kRR-RIA = (p+(r-1)q)m/((n+m)(p-q)) - c
    "image22": {
        "name": "kRR RIA Gain",
        "terms": [
            (r"G_{\text{kRR-RIA}}", "kRR RIA attack gain"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p, q", "Support probabilities"),
            (r"r", "Number of attack values"),
            (r"c", "Protocol constant"),
        ]
    },
    # image23: G_kRR-RPA = rmd/((n+m)(p-q)) - c
    "image23": {
        "name": "kRR RPA Gain",
        "terms": [
            (r"G_{\text{kRR-RPA}}", "kRR RPA attack gain"),
            (r"r", "Number of attack values"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"d", "Domain size"),
            (r"p, q", "Support probabilities"),
            (r"c", "Protocol constant"),
        ]
    },
    # image24: G_OUE-MGA = rm/((n+m)(p-q)) - c
    "image24": {
        "name": "OUE MGA Gain",
        "terms": [
            (r"G_{\text{OUE-MGA}}", "OUE MGA attack gain"),
            (r"r", "Number of attack values"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p, q", "Support probabilities"),
            (r"c", "Protocol constant"),
        ]
    },
    # image25: G_OUE-RIA = (p+(r-1)q)m/((n+m)(p-q)) - c
    "image25": {
        "name": "OUE RIA Gain",
        "terms": [
            (r"G_{\text{OUE-RIA}}", "OUE RIA attack gain"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p, q", "Support probabilities"),
            (r"r", "Number of attack values"),
            (r"c", "Protocol constant"),
        ]
    },
    # image26: G_OUE-RPA = rm·2/((n+m)(p-q)) - c
    "image26": {
        "name": "OUE RPA Gain",
        "terms": [
            (r"G_{\text{OUE-RPA}}", "OUE RPA attack gain"),
            (r"r", "Number of attack values"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p, q", "Support probabilities"),
            (r"c", "Protocol constant"),
        ]
    },
    # image27: G_OLH-MGA = rm/((n+m)(p-q)) - c
    "image27": {
        "name": "OLH MGA Gain",
        "terms": [
            (r"G_{\text{OLH-MGA}}", "OLH MGA attack gain"),
            (r"r", "Number of attack values"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p, q", "Support probabilities"),
            (r"c", "Protocol constant"),
        ]
    },
    # image28: G_OLH-RIA = (p+(r-1)q)m/((n+m)(p-q)) - c
    "image28": {
        "name": "OLH RIA Gain",
        "terms": [
            (r"G_{\text{OLH-RIA}}", "OLH RIA attack gain"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"p, q", "Support probabilities"),
            (r"r", "Number of attack values"),
            (r"c", "Protocol constant"),
        ]
    },
    # image29: G_OLH-RPA = rmd'/((n+m)(p-q)) - c
    "image29": {
        "name": "OLH RPA Gain",
        "terms": [
            (r"G_{\text{OLH-RPA}}", "OLH RPA attack gain"),
            (r"r", "Number of attack values"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"d'", "Hash output domain size"),
            (r"p, q", "Support probabilities"),
            (r"c", "Protocol constant"),
        ]
    },
    # image31: c = m/(n+m)
    "image31": {
        "name": "Attack Constant",
        "terms": [
            (r"c", "Fraction of malicious users"),
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
        ]
    },
    # image32: FrequencyGain = 1/(e^ε - 1)
    "image32": {
        "name": "Frequency Gain Bound",
        "terms": [
            (r"\text{FrequencyGain}", "Maximum achievable gain"),
            (r"e^\varepsilon", "Exponential of epsilon"),
            (r"\varepsilon", "Privacy parameter"),
        ]
    },
}


def generate_latex_descriptions():
    """Generate clean LaTeX for term descriptions."""
    desc_dir = Path("descriptions_latex")
    desc_dir.mkdir(exist_ok=True)
    
    for img_name, eq_data in EQUATIONS.items():
        if not eq_data.get("terms"):
            continue
        
        filepath = desc_dir / f"{img_name}_terms.tex"
        
        # Build simple inline LaTeX
        term_strs = []
        for term, definition in eq_data["terms"]:
            term_strs.append(f"{term} : \\text{{{definition}}}")
        
        content = r" \\  ".join(term_strs)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"✓ Created {filepath}")


if __name__ == "__main__":
    generate_latex_descriptions()
    print(f"\n✓ Generated {len(EQUATIONS)} term definition files")
