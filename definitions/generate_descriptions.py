#!/usr/bin/env python3
"""
Generate LaTeX description files that can be rendered by latex_to_svg.py
"""

from pathlib import Path

# Same equations dictionary from before
EQUATIONS = {
    "image1": {
        "name": "Differential Privacy Definition",
        "terms": [
            (r"\mathcal{M}", "Randomized mechanism/algorithm"),
            (r"x, y", "Neighboring inputs differing in one record"),
            (r"S", "Set of possible outputs"),
            (r"\varepsilon", "Privacy parameter (privacy budget)"),
        ]
    },
    "image2": {
        "name": "Local Differential Privacy (LDP)",
        "terms": [
            (r"\mathcal{A}", r"LDP algorithm satisfying epsilon-LDP"),
            (r"v_1, v_2", "Any two input values from the domain"),
            (r"y", r"Output value in Range(A)"),
            (r"\varepsilon", r"Privacy parameter (epsilon >= 0)"),
        ]
    },
    "image3": {
        "name": "LDP for Perturb-Encode",
        "terms": [
            (r"PE", r"Perturb(Encode(.))"),
            (r"v_1, v_2", "Any two input values"),
            (r"y", "Perturbed output value"),
        ]
    },
    "image4": {
        "name": "Support Probability (True Positive)",
        "terms": [
            (r"\text{PE}", "Perturb-Encode function"),
            (r"\text{Support}(y)", r"Set of items y supports"),
            (r"p", "Probability true value is supported"),
        ]
    },
    "image5": {
        "name": "Support Set Probability p",
        "terms": [
            (r"S(y)", r"Support set of y"),
            (r"p", "True positive probability"),
        ]
    },
    "image6": {
        "name": "Support Set Probability q",
        "terms": [
            (r"q", "False positive probability"),
            (r"v_2", r"Value different from v_1"),
        ]
    },
    "image7": {
        "name": "Frequency Estimation Formula",
        "terms": [
            (r"\tilde{f}_v", r"Estimated frequency for item v"),
            (r"n", "Total number of users"),
            (r"\mathbf{1}_{S(y_i)}(v)", r"Indicator: 1 if v in S(y_i)"),
            (r"p - q", "Difference in support probabilities"),
        ]
    },
    "image8": {
        "name": "Expected Support Count",
        "terms": [
            (r"\mathbb{E}", "Expected value operator"),
            (r"f_v", r"True frequency of item v"),
            (r"n", "Number of users"),
        ]
    },
    "image9": {
        "name": "RAPPOR Bit Perturbation",
        "terms": [
            (r"S_i", r"Perturbed bit at position i"),
            (r"B_0[i]", r"Original bit at position i"),
            (r"p, q", "Perturbation probabilities"),
        ]
    },
    "image10": {
        "name": "OUE Perturbation Probabilities",
        "terms": [
            (r"y_i", r"Perturbed bit at position i"),
            (r"v", "User's true value"),
            (r"p = \frac{1}{2}", "True bit probability"),
            (r"q = \frac{1}{e^\varepsilon + 1}", "False bit probability"),
        ]
    },
    "image11": {
        "name": "OLH Perturbation Probabilities",
        "terms": [
            (r"H", r"Hash function from family H"),
            (r"d' = e^\varepsilon + 1", "Hash output domain size"),
            (r"(H, a)", "Perturbed output tuple"),
        ]
    },
    "image12": {
        "name": "k-RR Randomized Response",
        "terms": [
            (r"d", "Domain size (number of items)"),
            (r"v", "User's true value"),
            (r"p", "Probability of reporting true value"),
            (r"q", "Probability of any other value"),
        ]
    },
    "image13": {
        "name": "Variance of Frequency Estimator",
        "terms": [
            (r"\text{Var}", "Variance operator"),
            (r"\tilde{f}_v", "Estimated frequency"),
            (r"f_v", "True frequency"),
        ]
    },
    "image14": {
        "name": "Maximal Gain Attack (MGA)",
        "terms": [
            (r"m", "Number of malicious users"),
            (r"n", "Number of genuine users"),
            (r"c", "Normalization constant"),
        ]
    },
    "image15": {
        "name": "Boosted Frequency (Target)",
        "terms": [
            (r"\tilde{f}'_t", "Frequency after attack"),
            (r"t", "Target item index"),
        ]
    },
    "image16": {
        "name": "Reduced Frequency (Non-target)",
        "terms": [
            (r"\tilde{f}'_i", r"Frequency of item i after attack"),
            (r"i \neq t", "Items other than target"),
        ]
    },
    "image17": {
        "name": "Random Input Attack Gain",
        "terms": [
            (r"G_{\text{RIA}}", "Gain from Random Input Attack"),
            (r"m", "Number of fake users"),
        ]
    },
    "image18": {
        "name": "RAPPOR Permanent Parameter",
        "terms": [
            (r"f", "Flip probability for memoization"),
            (r"\varepsilon", "Privacy parameter"),
        ]
    },
    "image19": {
        "name": "RAPPOR Frequency Estimation",
        "terms": [
            (r"\tilde{c}(i)", r"Estimated count for item i"),
            (r"B_j", r"Reported bit vector from user j"),
            (r"f", "Permanent randomization parameter"),
        ]
    },
    "image21": {
        "name": "kRR MGA Gain",
        "terms": [
            (r"c", "Protocol-specific constant"),
        ]
    },
    "image22": {
        "name": "kRR RIA Gain",
        "terms": [
            (r"r", "Distinct values in attack set"),
        ]
    },
    "image23": {
        "name": "kRR RPA Gain",
        "terms": [
            (r"d", "Domain size"),
        ]
    },
    "image24": {
        "name": "OUE MGA Gain",
        "terms": [
            (r"\text{OUE}", "Optimized Unary Encoding"),
        ]
    },
    "image27": {
        "name": "OLH MGA Gain",
        "terms": [
            (r"\text{OLH}", "Optimized Local Hashing"),
        ]
    },
    "image29": {
        "name": "OLH RPA Gain",
        "terms": [
            (r"d'", "Hash output domain size"),
        ]
    },
    "image31": {
        "name": "Attack Constant",
        "terms": [
            (r"c", "Fraction of malicious users"),
            (r"m", "Fake users"),
            (r"n", "Genuine users"),
        ]
    },
    "image32": {
        "name": "Frequency Gain Bound",
        "terms": [
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
        
        # Build simple inline LaTeX - each term on separate line using \atop
        # Since the script wraps in $...$, use simple math formatting
        term_strs = []
        for term, definition in eq_data["terms"]:
            term_strs.append(f"{term} : \\text{{{definition}}}")
        
        # Join with line breaks using \\atop  
        content = r" \\  ".join(term_strs)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"✓ Created {filepath}")


if __name__ == "__main__":
    generate_latex_descriptions()
