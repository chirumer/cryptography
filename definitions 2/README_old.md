# LDP Equation Reference

This document displays all equations from the `equations_svg` folder, mapped to their LaTeX source files and paper origins.

## Source Papers
- **LDP_Freq_Est.pdf** - Local Differential Privacy Frequency Estimation
- **attacks.pdf** - Data Poisoning Attacks to LDP Protocols  
- **rappor.pdf** - RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response

---

## Part 1: Differential Privacy Definitions
*Source: LDP_Freq_Est.pdf*

### Equation 1: ε-Differential Privacy (Database Level)
**Source:** `equations/eq01.tex`
```latex
\forall t \in \text{Range}(A) : \Pr[A(D) = t] \leq e^\varepsilon \Pr[A(D') = t]
```
![Equation 1](equations_svg/image1.svg)

**Terms:**
![Description 1](descriptions_svg/desc_eq01.svg)

---

### Equation 2: ε-Local Differential Privacy Definition
**Source:** `equations/eq02.tex`
```latex
\forall y \in \text{Range}(A) : \Pr[A(v_1) = y] \leq e^\varepsilon \Pr[A(v_2) = y]
```
![Equation 2](equations_svg/image2.svg)

**Terms:**
![Description 2](descriptions_svg/desc_eq02.svg)

---

### Equation 3: Perturbation Mechanism ε-LDP
**Source:** `equations/eq03.tex`
```latex
\Pr(PE(v_1) = y) \leq e^\varepsilon \Pr(PE(v_2) = y)
```
![Equation 3](equations_svg/image3.svg)

**Terms:**
![Description 3](descriptions_svg/desc_eq03.svg)

---

### Equation 4: Frequency Estimator Formula
**Source:** `equations/eq04.tex`
```latex
\tilde{f}_v = \frac{\frac{1}{n} \sum_{i=1}^{n} \mathbf{1}_{S(y_i)}(v) - q}{p - q}
```
![Equation 4](equations_svg/image4.svg)

**Terms:**
![Description 4](descriptions_svg/desc_eq04.svg)

---

### Equation 5: Expected Value of Support Indicator
**Source:** `equations/eq05.tex`
```latex
\sum_{i=1}^{n} E[\mathbf{1}_{S(y_i)}(v)] = n(f_v(p-q) + q)
```
![Equation 5](equations_svg/image5.svg)

**Terms:**
![Description 5](descriptions_svg/desc_eq05.svg)

---

### Equation 6: True Perturbation Probability p
**Source:** `equations/eq06.tex`
```latex
\Pr(PE(v_1) \in \{y | v_1 \in S(y)\}) = p
```
![Equation 6](equations_svg/image6.svg)

**Terms:**
![Description 6](descriptions_svg/desc_eq06.svg)

---

### Equation 7: False Perturbation Probability q
**Source:** `equations/eq07.tex`
```latex
\Pr(PE(v_2) \in \{y | v_1 \in S(y)\}) = q
```
![Equation 7](equations_svg/image7.svg)

**Terms:**
![Description 7](descriptions_svg/desc_eq07.svg)

---

### Equation 8: Generalized True Positive Probability p*
**Source:** `equations/eq08.tex`
```latex
\Pr[PE(v_1) \in \{y | v_1 \in \text{Support}(y)\}] = p^*
```
![Equation 8](equations_svg/image8.svg)

**Terms:**
![Description 8](descriptions_svg/desc_eq08.svg)

---

## Part 2: LDP Protocol Definitions
*Source: LDP_Freq_Est.pdf*

### Equation 9: k-Randomized Response (kRR) Probabilities
**Source:** `equations/eq09.tex`
```latex
\Pr(y = a) = \begin{cases} \frac{e^\varepsilon}{d-1+e^\varepsilon} = p, & \text{if } a = v \\ \frac{1}{d-1+e^\varepsilon} = q, & \text{otherwise} \end{cases}
```
![Equation 9](equations_svg/image9.svg)

**Terms:**
![Description 9](descriptions_svg/desc_eq09.svg)

---

### Equation 10: Direct Encoding (DE) Perturbation
**Source:** `equations/eq10.tex`
```latex
\Pr[\text{Perturb}_{DE}(x) = i] = \begin{cases} p = \frac{e^\varepsilon}{e^\varepsilon + d - 1}, & \text{if } i = x \\ q = \frac{1}{e^\varepsilon + d - 1}, & \text{if } i \neq x \end{cases}
```
![Equation 10](equations_svg/image10.svg)

**Terms:**
![Description 10](descriptions_svg/desc_eq10.svg)

---

### Equation 11: Direct Encoding Variance
**Source:** `equations/eq11.tex`
```latex
\text{Var}^*[\tilde{c}_{DE}(i)] = n \cdot \frac{d - 2 + e^\varepsilon}{(e^\varepsilon - 1)^2}
```
![Equation 11](equations_svg/image11.svg)

**Terms:**
![Description 11](descriptions_svg/desc_eq11.svg)

---

### Equation 12: Optimized Unary Encoding (OUE) Probabilities
**Source:** `equations/eq12.tex`
```latex
\Pr(y_i = 1) = \begin{cases} \frac{1}{2} = p, & \text{if } i = v \\ \frac{1}{e^\varepsilon + 1} = q, & \text{otherwise} \end{cases}
```
![Equation 12](equations_svg/image12.svg)

**Terms:**
![Description 12](descriptions_svg/desc_eq12.svg)

---

### Equation 13: OUE Variance
**Source:** `equations/eq13.tex`
```latex
\text{Var}^*[\tilde{c}_{OUE}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```
![Equation 13](equations_svg/image13.svg)

**Terms:**
![Description 13](descriptions_svg/desc_eq13.svg)

---

### Equation 14: Privacy Budget from Probabilities
**Source:** `equations/eq14.tex`
```latex
\varepsilon = \ln\left(\frac{p(1-q)}{(1-p)q}\right)
```
![Equation 14](equations_svg/image14.svg)

**Terms:**
![Description 14](descriptions_svg/desc_eq14.svg)

---

### Equation 15: Optimized Local Hashing (OLH) Perturbation
**Source:** `equations/eq15.tex`
```latex
\Pr(y = (H, a)) = \begin{cases} \frac{e^\varepsilon}{e^\varepsilon + d' - 1} = p', & \text{if } a = H(v) \\ \frac{1}{e^\varepsilon + d' - 1} = q', & \text{otherwise} \end{cases}
```
![Equation 15](equations_svg/image15.svg)

**Terms:**
![Description 15](descriptions_svg/desc_eq15.svg)

---

### Equation 16: OLH Effective Probabilities
**Source:** `equations/eq16.tex`
```latex
p = p' = \frac{e^\varepsilon}{e^\varepsilon + d' - 1}, \quad q = \frac{1}{d'} \cdot p' + (1 - \frac{1}{d'}) \cdot q' = \frac{1}{d'}
```
![Equation 16](equations_svg/image16.svg)

**Terms:**
![Description 16](descriptions_svg/desc_eq16.svg)

---

### Equation 17: Optimal Hash Domain Size
**Source:** `equations/eq17.tex`
```latex
g = e^\varepsilon + 1
```
![Equation 17](equations_svg/image17.svg)

**Terms:**
![Description 17](descriptions_svg/desc_eq17.svg)

---

### Equation 18: OLH Variance
**Source:** `equations/eq18.tex`
```latex
\text{Var}^*[\tilde{c}_{OLH}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```
![Equation 18](equations_svg/image18.svg)

**Terms:**
![Description 18](descriptions_svg/desc_eq18.svg)

---

## Part 3: Attack Gain Formulas
*Source: attacks.pdf*

### Equation 19: Total Attack Gain Function
**Source:** `equations/eq19.tex`
```latex
G(Y) = \sum_{t \in T} E[\Delta \tilde{f}_t]
```
![Equation 19](equations_svg/image19.svg)

**Terms:**
![Description 19](descriptions_svg/desc_eq19.svg)

---

### Equation 21: Frequency Gain Definition
**Source:** `equations/eq21.tex`
```latex
\Delta \tilde{f}_t = \tilde{f}_{t,a} - \tilde{f}_{t,b}
```
![Equation 21](equations_svg/image21.svg)

**Terms:**
![Description 21](descriptions_svg/desc_eq21.svg)

---

### Equation 22: General Attack Gain Formula
**Source:** `equations/eq22.tex`
```latex
G = \frac{\sum_{i=n+1}^{n+m} \sum_{t \in T} E[\mathbf{1}_{S(y_i)}(t)]}{(n+m)(p-q)} - c
```
![Equation 22](equations_svg/image22.svg)

**Terms:**
![Description 22](descriptions_svg/desc_eq22.svg)

---

### Equation 23: kRR RPA Attack Gain
**Source:** `equations/eq23.tex`
```latex
G = \frac{rm}{d(n+m)(p-q)} - c
```
![Equation 23](equations_svg/image23.svg)

**Terms:**
![Description 23](descriptions_svg/desc_eq23.svg)

---

### Equation 24: Expected Support Indicator (kRR)
**Source:** `equations/eq24.tex`
```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```
![Equation 24](equations_svg/image24.svg)

**Terms:**
![Description 24](descriptions_svg/desc_eq24.svg)

---

### Equation 25: kRR MGA Attack Gain
**Source:** `equations/eq25.tex`
```latex
G = \frac{m}{(n+m)(p-q)} - c
```
![Equation 25](equations_svg/image25.svg)

**Terms:**
![Description 25](descriptions_svg/desc_eq25.svg)

---

### Equation 26: Expected Support Indicator (OUE MGA)
**Source:** `equations/eq26.tex`
```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \Pr(y_{i,t} = 1) = \frac{1}{2}
```
![Equation 26](equations_svg/image26.svg)

**Terms:**
![Description 26](descriptions_svg/desc_eq26.svg)

---

### Equation 27: Expected Support Indicator (OUE RIA)
**Source:** `equations/eq27.tex`
```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```
![Equation 27](equations_svg/image27.svg)

**Terms:**
![Description 27](descriptions_svg/desc_eq27.svg)

---

### Equation 28: OUE MGA Attack Gain
**Source:** `equations/eq28.tex`
```latex
G = \frac{rm}{(n+m)(p-q)} - c
```
![Equation 28](equations_svg/image28.svg)

**Terms:**
![Description 28](descriptions_svg/desc_eq28.svg)

---

### Equation 29: Expected Support Indicator (OLH)
**Source:** `equations/eq29.tex`
```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p' + (1 - \frac{1}{r}) \cdot q'
```
![Equation 29](equations_svg/image29.svg)

**Terms:**
![Description 29](descriptions_svg/desc_eq29.svg)

---

### Equation 31: (Unknown Source)
**Source:** Unknown - no matching LaTeX file found

![Equation 31](equations_svg/image31.svg)

---

### Equation 32: Protocol Selection Threshold
**Source:** `equations/eq32.tex`
```latex
d < 3e^\varepsilon + 2 \Rightarrow \text{Use DE/kRR}
```
![Equation 32](equations_svg/image32.svg)

**Terms:**
![Description 32](descriptions_svg/desc_eq32.svg)

---

## Part 4: RAPPOR Equations
*Source: rappor.pdf*

### RAPPOR Equation 1: Permanent Randomized Response (B')
**Source:** `rapor_slide_eqns/eq1_permanent_randomized_response.tex`
```latex
B'_i = \begin{cases} 1 & \text{with probability } \frac{1}{2}f \\ 0 & \text{with probability } \frac{1}{2}f \\ B_i & \text{with probability } 1 - f \end{cases}
```

*Note: This equation is related to eq36 in the equations folder*

---

### RAPPOR Equation 2: Instantaneous Randomized Response (S)
**Source:** `rapor_slide_eqns/eq2_instantaneous_randomized_response.tex`
```latex
P(S_i = 1) = \begin{cases} q & \text{if } B'_i = 1 \\ p & \text{if } B'_i = 0 \end{cases}
```

---

### RAPPOR Equation 3: Unbiased Estimator
**Source:** `rapor_slide_eqns/eq3_unbiased_estimator.tex`
```latex
t_{ij} = \frac{c_{ij} - \left(p + \frac{1}{2} f q - \frac{1}{2} f p\right) N_j}{(1 - f)(q - p)}
```

*Note: This equation is related to eq39 in the equations folder*

---

### RAPPOR Equation 4: Longitudinal Privacy
**Source:** `rapor_slide_eqns/eq4_longitudinal_privacy.tex`
```latex
\varepsilon_\infty = 2h \ln \frac{1 - \frac{1}{2}f}{\frac{1}{2}f}
```

*Note: This equation is related to eq37 in the equations folder*

---

## Appendix: Attack Gain Equations Summary
*Source: attack_gain_equations/*

### kRR Attack Gains

| Attack Type | Formula | Source File |
|-------------|---------|-------------|
| MGA | $G_{\text{MGA}}^{\text{kRR}} = \frac{m}{(n+m)(p-q)} - c$ | `krr_mga_gain.tex` |
| RIA | $G_{\text{RIA}}^{\text{kRR}} = \frac{(p+(r-1)q)m}{(n+m)(p-q)} - c$ | `krr_ria_gain.tex` |
| RPA | $G_{\text{RPA}}^{\text{kRR}} = \frac{rm}{d(n+m)(p-q)} - c$ | `krr_rpa_gain.tex` |

### OUE Attack Gains

| Attack Type | Formula | Source File |
|-------------|---------|-------------|
| MGA | $G_{\text{MGA}}^{\text{OUE}} = \frac{rm}{(n+m)(p-q)} - c$ | `oue_mga_gain.tex` |
| RIA | $G_{\text{RIA}}^{\text{OUE}} = \frac{(p+(r-1)q)m}{(n+m)(p-q)} - c$ | `oue_ria_gain.tex` |
| RPA | $G_{\text{RPA}}^{\text{OUE}} = \frac{rm}{2(n+m)(p-q)} - c$ | `oue_rpa_gain.tex` |

### OLH Attack Gains

| Attack Type | Formula | Source File |
|-------------|---------|-------------|
| MGA | $G_{\text{MGA}}^{\text{OLH}} = \frac{rm}{(n+m)(p-q)} - c$ | `olh_mga_gain.tex` |
| RIA | $G_{\text{RIA}}^{\text{OLH}} = \frac{[p+(r-1)q]m}{(n+m)(p-q)} - c$ | `olh_ria_gain.tex` |
| RPA | $G_{\text{RPA}}^{\text{OLH}} = \frac{rm}{d'(n+m)(p-q)} - c$ | `olh_rpa_gain.tex` |

---

## Variable Reference

| Variable | Description |
|----------|-------------|
| $\varepsilon$ | Privacy budget parameter |
| $n$ | Number of genuine users |
| $m$ | Number of fake/malicious users |
| $d$ | Domain size (number of items) |
| $d'$ | Hash range for OLH (typically $e^\varepsilon + 1$) |
| $r$ | Number of target items |
| $p$ | True positive probability |
| $q$ | False positive probability |
| $c$ | Baseline constant |
| $f$ | RAPPOR flip probability |
| $f_v$ | True frequency of value $v$ |
| $\tilde{f}_v$ | Estimated frequency of value $v$ |
| $G$ | Attack gain |
| $T$ | Set of target items |
