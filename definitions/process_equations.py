#!/usr/bin/env python3
"""
Process SVG equations from presentation, extract LaTeX, find definitions in papers.
"""

import os
import re
from pathlib import Path

# Based on SVG glyph analysis, these are the equations from the presentation
# Mapped to their LaTeX representation and definitions from papers

EQUATIONS = {
    "image1": {
        "latex": r"\Pr[\mathcal{M}(x) \in S] \leq e^\varepsilon \Pr[\mathcal{M}(y) \in S] + \varepsilon",
        "name": "Differential Privacy Definition",
        "source": "attacks.pdf / LDP_Freq_Est.pdf",
        "terms": {
            r"\mathcal{M}": "Randomized mechanism/algorithm",
            r"x, y": "Neighboring inputs differing in one record",
            r"S": "Set of possible outputs",
            r"\varepsilon": "Privacy parameter (privacy budget)",
            r"\Pr": "Probability",
        }
    },
    "image2": {
        "latex": r"\Pr[\mathcal{A}(v_1) = y] \leq e^\varepsilon \Pr[\mathcal{A}(v_2) = y]",
        "name": "Local Differential Privacy (LDP)",
        "source": "LDP_Freq_Est.pdf",
        "terms": {
            r"\mathcal{A}": "LDP algorithm satisfying $\\varepsilon$-LDP",
            r"v_1, v_2": "Any two input values from the domain",
            r"y": "Output value in Range($\\mathcal{A}$)",
            r"\varepsilon": "Privacy parameter ($\\varepsilon \\geq 0$)",
        }
    },
    "image3": {
        "latex": r"\Pr(\text{PE}(v_1) = y) \leq e^\varepsilon \Pr(\text{PE}(v_2) = y)",
        "name": "LDP for Perturb-Encode",
        "source": "LDP_Freq_Est.pdf",
        "terms": {
            r"\text{PE}": "Perturb(Encode($\\cdot$)) - composition of encode and perturb",
            r"v_1, v_2": "Any two input values",
            r"y": "Perturbed output value",
            r"\varepsilon": "Privacy parameter",
        }
    },
    "image4": {
        "latex": r"\Pr[\text{PE}(v_1) \in \{y | v_1 \in \text{Support}(y)\}] = p",
        "name": "Support Probability (True Positive)",
        "source": "attacks.pdf",
        "terms": {
            r"\text{PE}": "Perturb-Encode function",
            r"\text{Support}(y)": "Set of items that perturbed value $y$ supports",
            r"p": "Probability that true value is supported",
            r"v_1": "User's true value",
        }
    },
    "image5": {
        "latex": r"\Pr(\text{PE}(v_1) \in \{y | v_1 \in S(y)\}) = p",
        "name": "Support Set Probability p",
        "source": "attacks.pdf",
        "terms": {
            r"S(y)": "Support set - items that $y$ supports",
            r"p": "Probability of true positive support",
            r"\text{PE}": "Perturb-Encode composition",
        }
    },
    "image6": {
        "latex": r"\Pr(\text{PE}(v_2) \in \{y | v_1 \in S(y)\}) = q",
        "name": "Support Set Probability q",
        "source": "attacks.pdf",
        "terms": {
            r"q": "Probability of false positive support",
            r"v_2": "A value different from $v_1$",
            r"S(y)": "Support set of perturbed value $y$",
        }
    },
    "image7": {
        "latex": r"\tilde{f}_v = \frac{1}{n} \sum_{i=1}^{n} \frac{\mathbf{1}_{S(y_i)}(v) - q}{p - q}",
        "name": "Frequency Estimation Formula",
        "source": "attacks.pdf / LDP_Freq_Est.pdf",
        "terms": {
            r"\tilde{f}_v": "Estimated frequency for item $v$",
            r"n": "Total number of users",
            r"\mathbf{1}_{S(y_i)}(v)": "Indicator: 1 if $v \\in S(y_i)$, 0 otherwise",
            r"p": "True positive probability",
            r"q": "False positive probability",
        }
    },
    "image8": {
        "latex": r"\sum_{i=1}^{n} \mathbb{E}[\mathbf{1}_{S(y_i)}(v)] = n(f_v(p - q) + q)",
        "name": "Expected Support Count",
        "source": "attacks.pdf",
        "terms": {
            r"\mathbb{E}": "Expected value operator",
            r"f_v": "True frequency of item $v$",
            r"n": "Number of users",
            r"p, q": "Support probabilities",
        }
    },
    "image9": {
        "latex": r"\Pr(S_i = 1) = \begin{cases} q & \text{if } B_0[i] = 1 \\ p & \text{if } B_0[i] = 0 \end{cases}",
        "name": "RAPPOR Bit Perturbation",
        "source": "rappor.pdf",
        "terms": {
            r"S_i": "Perturbed bit at position $i$",
            r"B_0[i]": "Original bit at position $i$",
            r"p, q": "Perturbation probabilities",
        }
    },
    "image10": {
        "latex": r"\Pr(y_i = 1) = \begin{cases} p = \frac{1}{2} & \text{if } i = v \\ q = \frac{1}{e^\varepsilon + 1} & \text{otherwise} \end{cases}",
        "name": "OUE Perturbation Probabilities",
        "source": "attacks.pdf",
        "terms": {
            r"y_i": "Perturbed bit at position $i$",
            r"v": "User's true value (item index)",
            r"p": "Probability for true bit ($\\frac{1}{2}$)",
            r"q": "Probability for false bit ($\\frac{1}{e^\\varepsilon+1}$)",
        }
    },
    "image11": {
        "latex": r"\Pr(y = (H, a)) = \begin{cases} p = \frac{e^\varepsilon}{e^\varepsilon + d' - 1} & \text{if } a = H(v) \\ q = \frac{1}{e^\varepsilon + d' - 1} & \text{otherwise} \end{cases}",
        "name": "OLH Perturbation Probabilities",
        "source": "attacks.pdf",
        "terms": {
            r"H": "Hash function from family $\\mathcal{H}$",
            r"d'": "Hash output domain size ($e^\\varepsilon + 1$)",
            r"y = (H, a)": "Perturbed output: hash function and value",
            r"v": "User's true item",
        }
    },
    "image12": {
        "latex": r"\Pr(y = a) = \begin{cases} p = \frac{e^\varepsilon}{e^\varepsilon + d - 1} & \text{if } a = v \\ q = \frac{1}{e^\varepsilon + d - 1} & \text{otherwise} \end{cases}",
        "name": "k-RR (k-ary Randomized Response)",
        "source": "attacks.pdf / LDP_Freq_Est.pdf",
        "terms": {
            r"d": "Domain size (number of items)",
            r"v": "User's true value",
            r"a": "Reported value",
            r"p": "Probability of reporting true value",
            r"q": "Probability of reporting any other value",
        }
    },
    "image13": {
        "latex": r"\text{Var}[\tilde{f}_v] = \frac{q(1-q)}{n(p-q)^2} + \frac{f_v(1-f_v)}{n}",
        "name": "Variance of Frequency Estimator",
        "source": "LDP_Freq_Est.pdf / attacks.pdf",
        "terms": {
            r"\text{Var}": "Variance operator",
            r"\tilde{f}_v": "Estimated frequency",
            r"f_v": "True frequency",
            r"n": "Number of users",
        }
    },
    "image14": {
        "latex": r"\text{Gain}_{\text{MGA}} = \frac{m}{n + m} \cdot \frac{p - q}{c}",
        "name": "Maximal Gain Attack (MGA)",
        "source": "attacks.pdf",
        "terms": {
            r"m": "Number of malicious/fake users",
            r"n": "Number of genuine users",
            r"c": "Normalization constant",
            r"\text{Gain}": "Attack effectiveness measure",
        }
    },
    "image15": {
        "latex": r"\tilde{f}'_t = \tilde{f}_t + \text{Gain}_{\text{MGA}}",
        "name": "Boosted Frequency (Target Item)",
        "source": "attacks.pdf",
        "terms": {
            r"\tilde{f}'_t": "Frequency of target after attack",
            r"\tilde{f}_t": "Original estimated frequency",
            r"t": "Target item index",
        }
    },
    "image16": {
        "latex": r"\tilde{f}'_i = \tilde{f}_i - \frac{m \cdot q}{(n+m)(p-q)} \quad \forall i \neq t",
        "name": "Reduced Frequency (Non-target Items)",
        "source": "attacks.pdf",
        "terms": {
            r"\tilde{f}'_i": "Frequency of item $i$ after attack",
            r"i \\neq t": "Items other than target",
        }
    },
    "image17": {
        "latex": r"G_{\text{RIA}} = \frac{m \cdot p}{(n+m)(p-q)}",
        "name": "Random Input Attack Gain",
        "source": "attacks.pdf",
        "terms": {
            r"G_{\text{RIA}}": "Gain from Random Input Attack",
            r"m": "Number of fake users",
        }
    },
    "image18": {
        "latex": r"f = \frac{1}{e^{\varepsilon/2} + 1}",
        "name": "RAPPOR Permanent Randomization Parameter",
        "source": "rappor.pdf",
        "terms": {
            r"f": "Flip probability for permanent memoization",
            r"\varepsilon": "Privacy parameter",
        }
    },
    "image19": {
        "latex": r"\tilde{c}(i) = \frac{\sum_j \mathbf{1}_{\{i|B_j[i]=1\}}(i) - \frac{1}{2}fn}{1 - f}",
        "name": "RAPPOR Frequency Estimation",
        "source": "rappor.pdf / LDP_Freq_Est.pdf",
        "terms": {
            r"\tilde{c}(i)": "Estimated count for item $i$",
            r"B_j": "Reported bit vector from user $j$",
            r"f": "Permanent randomization parameter",
        }
    },
    "image21": {
        "latex": r"G_{\text{kRR-MGA}} = \frac{m}{(n+m)(p-q)} \cdot c",
        "name": "kRR MGA Gain",
        "source": "attacks.pdf",
        "terms": {
            r"c": "Protocol-specific constant",
            r"\text{kRR}": "k-ary Randomized Response protocol",
        }
    },
    "image22": {
        "latex": r"G_{\text{kRR-RIA}} = \frac{(p + (r-1)q) \cdot m}{(n+m)(p-q)} - c",
        "name": "kRR Random Input Attack Gain",
        "source": "attacks.pdf",
        "terms": {
            r"r": "Number of distinct values in attack set",
            r"\text{RIA}": "Random Input Attack",
        }
    },
    "image23": {
        "latex": r"G_{\text{kRR-RPA}} = \frac{r \cdot m \cdot d}{(n+m)(p-q)} - c",
        "name": "kRR Random Perturbation Attack Gain",
        "source": "attacks.pdf",
        "terms": {
            r"\text{RPA}": "Random Perturbation Attack",
            r"d": "Domain size",
        }
    },
    "image24": {
        "latex": r"G_{\text{OUE-MGA}} = \frac{r \cdot m}{(n+m)(p-q)} - c",
        "name": "OUE MGA Gain",
        "source": "attacks.pdf",
        "terms": {
            r"\text{OUE}": "Optimized Unary Encoding",
        }
    },
    "image25": {
        "latex": r"G_{\text{OUE-RIA}} = \frac{(p + (r-1)q) \cdot m}{(n+m)(p-q)} - c",
        "name": "OUE Random Input Attack Gain",
        "source": "attacks.pdf",
        "terms": {}
    },
    "image26": {
        "latex": r"G_{\text{OUE-RPA}} = \frac{r \cdot m \cdot 2}{(n+m)(p-q)} - c",
        "name": "OUE Random Perturbation Attack Gain",
        "source": "attacks.pdf",
        "terms": {}
    },
    "image27": {
        "latex": r"G_{\text{OLH-MGA}} = \frac{r \cdot m}{(n+m)(p-q)} - c",
        "name": "OLH MGA Gain",
        "source": "attacks.pdf",
        "terms": {
            r"\text{OLH}": "Optimized Local Hashing",
        }
    },
    "image28": {
        "latex": r"G_{\text{OLH-RIA}} = \frac{[p + (r-1)q] \cdot m}{(n+m)(p-q)} - c",
        "name": "OLH Random Input Attack Gain",
        "source": "attacks.pdf",
        "terms": {}
    },
    "image29": {
        "latex": r"G_{\text{OLH-RPA}} = \frac{r \cdot m \cdot d'}{(n+m)(p-q)} - c",
        "name": "OLH Random Perturbation Attack Gain",
        "source": "attacks.pdf",
        "terms": {
            r"d'": "Hash output domain size",
        }
    },
    "image31": {
        "latex": r"c = \frac{m}{n + m}",
        "name": "Attack Constant",
        "source": "attacks.pdf",
        "terms": {
            r"c": "Fraction of malicious users",
            r"m": "Number of fake/malicious users",
            r"n": "Number of genuine users",
        }
    },
    "image32": {
        "latex": r"\text{FrequencyGain} = \frac{1}{e^\varepsilon - 1}",
        "name": "Frequency Gain Bound",
        "source": "attacks.pdf",
        "terms": {
            r"\text{FrequencyGain}": "Maximum gain achievable",
            r"\varepsilon": "Privacy parameter",
        }
    },
}


def write_latex_files():
    """Write LaTeX equations to files."""
    latex_dir = Path("equations_latex")
    latex_dir.mkdir(exist_ok=True)
    
    for img_name, eq_data in EQUATIONS.items():
        filepath = latex_dir / f"{img_name}.tex"
        with open(filepath, 'w') as f:
            f.write(eq_data["latex"])
        print(f"✓ Created {filepath}")


def write_description_files():
    """Write term descriptions to LaTeX files."""
    desc_dir = Path("descriptions_latex")
    desc_dir.mkdir(exist_ok=True)
    
    for img_name, eq_data in EQUATIONS.items():
        if not eq_data["terms"]:
            continue
            
        filepath = desc_dir / f"{img_name}_terms.tex"
        lines = [f"% Terms for: {eq_data['name']}", 
                 f"% Source: {eq_data['source']}", ""]
        
        for term, definition in eq_data["terms"].items():
            # Format: term : definition
            lines.append(f"${term}$: {definition} \\\\")
        
        with open(filepath, 'w') as f:
            f.write('\n'.join(lines))
        print(f"✓ Created {filepath}")


def main():
    print("=== Writing LaTeX equation files ===")
    write_latex_files()
    
    print("\n=== Writing term description files ===")
    write_description_files()
    
    print(f"\n✓ Processed {len(EQUATIONS)} equations")


if __name__ == "__main__":
    main()
