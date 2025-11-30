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
**LaTeX Source:** `equations/eq01.tex` → **Image:** `equations_svg/eq01.svg`
```latex
\forall t \in \text{Range}(A) : \Pr[A(D) = t] \leq e^\varepsilon \Pr[A(D') = t]
```
![Equation 1](equations_svg/eq01.svg)

**Terms:** `descriptions_latex/desc_eq01.tex` → `descriptions_svg/desc_eq01.svg`
![Description 1](descriptions_svg/desc_eq01.svg)

---

### Equation 2: ε-Local Differential Privacy Definition
**LaTeX Source:** `equations/eq02.tex` → **Image:** `equations_svg/eq02.svg`
```latex
\forall y \in \text{Range}(A) : \Pr[A(v_1) = y] \leq e^\varepsilon \Pr[A(v_2) = y]
```
![Equation 2](equations_svg/eq02.svg)

**Terms:** `descriptions_latex/desc_eq02.tex` → `descriptions_svg/desc_eq02.svg`
![Description 2](descriptions_svg/desc_eq02.svg)

---

### Equation 3: Perturbation Mechanism ε-LDP
**LaTeX Source:** `equations/eq03.tex` → **Image:** `equations_svg/eq03.svg`
```latex
\Pr(PE(v_1) = y) \leq e^\varepsilon \Pr(PE(v_2) = y)
```
![Equation 3](equations_svg/eq03.svg)

**Terms:** `descriptions_latex/desc_eq03.tex` → `descriptions_svg/desc_eq03.svg`
![Description 3](descriptions_svg/desc_eq03.svg)

---

### Equation 4: Frequency Estimator Formula
**LaTeX Source:** `equations/eq04.tex` → **Image:** `equations_svg/eq04.svg`
```latex
\tilde{f}_v = \frac{\frac{1}{n} \sum_{i=1}^{n} \mathbf{1}_{S(y_i)}(v) - q}{p - q}
```
![Equation 4](equations_svg/eq04.svg)

**Terms:** `descriptions_latex/desc_eq04.tex` → `descriptions_svg/desc_eq04.svg`
![Description 4](descriptions_svg/desc_eq04.svg)

---

### Equation 5: Expected Value of Support Indicator
**LaTeX Source:** `equations/eq05.tex` → **Image:** `equations_svg/eq05.svg`
```latex
\sum_{i=1}^{n} E[\mathbf{1}_{S(y_i)}(v)] = n(f_v(p-q) + q)
```
![Equation 5](equations_svg/eq05.svg)

**Terms:** `descriptions_latex/desc_eq05.tex` → `descriptions_svg/desc_eq05.svg`
![Description 5](descriptions_svg/desc_eq05.svg)

---

### Equation 6: True Perturbation Probability p
**LaTeX Source:** `equations/eq06.tex` → **Image:** `equations_svg/eq06.svg`
```latex
\Pr(PE(v_1) \in \{y | v_1 \in S(y)\}) = p
```
![Equation 6](equations_svg/eq06.svg)

**Terms:** `descriptions_latex/desc_eq06.tex` → `descriptions_svg/desc_eq06.svg`
![Description 6](descriptions_svg/desc_eq06.svg)

---

### Equation 7: False Perturbation Probability q
**LaTeX Source:** `equations/eq07.tex` → **Image:** `equations_svg/eq07.svg`
```latex
\Pr(PE(v_2) \in \{y | v_1 \in S(y)\}) = q
```
![Equation 7](equations_svg/eq07.svg)

**Terms:** `descriptions_latex/desc_eq07.tex` → `descriptions_svg/desc_eq07.svg`
![Description 7](descriptions_svg/desc_eq07.svg)

---

### Equation 8: Generalized True Positive Probability p*
**LaTeX Source:** `equations/eq08.tex` → **Image:** `equations_svg/eq08.svg`
```latex
\Pr[PE(v_1) \in \{y | v_1 \in \text{Support}(y)\}] = p^*
```
![Equation 8](equations_svg/eq08.svg)

**Terms:** `descriptions_latex/desc_eq08.tex` → `descriptions_svg/desc_eq08.svg`
![Description 8](descriptions_svg/desc_eq08.svg)

---

## Part 2: LDP Protocol Definitions
*Source: LDP_Freq_Est.pdf*

### Equation 9: k-Randomized Response (kRR) Probabilities
**LaTeX Source:** `equations/eq09.tex` → **Image:** `equations_svg/eq09.svg`
```latex
\Pr(y = a) = \begin{cases} \frac{e^\varepsilon}{d-1+e^\varepsilon} = p, & \text{if } a = v \\ \frac{1}{d-1+e^\varepsilon} = q, & \text{otherwise} \end{cases}
```
![Equation 9](equations_svg/eq09.svg)

**Terms:** `descriptions_latex/desc_eq09.tex` → `descriptions_svg/desc_eq09.svg`
![Description 9](descriptions_svg/desc_eq09.svg)

---

### Equation 10: Direct Encoding (DE) Perturbation
**LaTeX Source:** `equations/eq10.tex` → **Image:** `equations_svg/eq10.svg`
```latex
\Pr[\text{Perturb}_{DE}(x) = i] = \begin{cases} p = \frac{e^\varepsilon}{e^\varepsilon + d - 1}, & \text{if } i = x \\ q = \frac{1}{e^\varepsilon + d - 1}, & \text{if } i \neq x \end{cases}
```
![Equation 10](equations_svg/eq10.svg)

**Terms:** `descriptions_latex/desc_eq10.tex` → `descriptions_svg/desc_eq10.svg`
![Description 10](descriptions_svg/desc_eq10.svg)

---

### Equation 11: Direct Encoding Variance
**LaTeX Source:** `equations/eq11.tex` → **Image:** `equations_svg/eq11.svg`
```latex
\text{Var}^*[\tilde{c}_{DE}(i)] = n \cdot \frac{d - 2 + e^\varepsilon}{(e^\varepsilon - 1)^2}
```
![Equation 11](equations_svg/eq11.svg)

**Terms:** `descriptions_latex/desc_eq11.tex` → `descriptions_svg/desc_eq11.svg`
![Description 11](descriptions_svg/desc_eq11.svg)

---

### Equation 12: Optimized Unary Encoding (OUE) Probabilities
**LaTeX Source:** `equations/eq12.tex` → **Image:** `equations_svg/eq12.svg`
```latex
\Pr(y_i = 1) = \begin{cases} \frac{1}{2} = p, & \text{if } i = v \\ \frac{1}{e^\varepsilon + 1} = q, & \text{otherwise} \end{cases}
```
![Equation 12](equations_svg/eq12.svg)

**Terms:** `descriptions_latex/desc_eq12.tex` → `descriptions_svg/desc_eq12.svg`
![Description 12](descriptions_svg/desc_eq12.svg)

---

### Equation 13: OUE Variance
**LaTeX Source:** `equations/eq13.tex` → **Image:** `equations_svg/eq13.svg`
```latex
\text{Var}^*[\tilde{c}_{OUE}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```
![Equation 13](equations_svg/eq13.svg)

**Terms:** `descriptions_latex/desc_eq13.tex` → `descriptions_svg/desc_eq13.svg`
![Description 13](descriptions_svg/desc_eq13.svg)

---

### Equation 14: Privacy Budget from Probabilities
**LaTeX Source:** `equations/eq14.tex` → **Image:** `equations_svg/eq14.svg`
```latex
\varepsilon = \ln\left(\frac{p(1-q)}{(1-p)q}\right)
```
![Equation 14](equations_svg/eq14.svg)

**Terms:** `descriptions_latex/desc_eq14.tex` → `descriptions_svg/desc_eq14.svg`
![Description 14](descriptions_svg/desc_eq14.svg)

---

### Equation 15: Optimized Local Hashing (OLH) Perturbation
**LaTeX Source:** `equations/eq15.tex` → **Image:** `equations_svg/eq15.svg`
```latex
\Pr(y = (H, a)) = \begin{cases} \frac{e^\varepsilon}{e^\varepsilon + d' - 1} = p', & \text{if } a = H(v) \\ \frac{1}{e^\varepsilon + d' - 1} = q', & \text{otherwise} \end{cases}
```
![Equation 15](equations_svg/eq15.svg)

**Terms:** `descriptions_latex/desc_eq15.tex` → `descriptions_svg/desc_eq15.svg`
![Description 15](descriptions_svg/desc_eq15.svg)

---

### Equation 16: OLH Effective Probabilities
**LaTeX Source:** `equations/eq16.tex` → **Image:** `equations_svg/eq16.svg`
```latex
p = p' = \frac{e^\varepsilon}{e^\varepsilon + d' - 1}, \quad q = \frac{1}{d'} \cdot p' + (1 - \frac{1}{d'}) \cdot q' = \frac{1}{d'}
```
![Equation 16](equations_svg/eq16.svg)

**Terms:** `descriptions_latex/desc_eq16.tex` → `descriptions_svg/desc_eq16.svg`
![Description 16](descriptions_svg/desc_eq16.svg)

---

### Equation 17: Optimal Hash Domain Size
**LaTeX Source:** `equations/eq17.tex` → **Image:** `equations_svg/eq17.svg`
```latex
g = e^\varepsilon + 1
```
![Equation 17](equations_svg/eq17.svg)

**Terms:** `descriptions_latex/desc_eq17.tex` → `descriptions_svg/desc_eq17.svg`
![Description 17](descriptions_svg/desc_eq17.svg)

---

### Equation 18: OLH Variance
**LaTeX Source:** `equations/eq18.tex` → **Image:** `equations_svg/eq18.svg`
```latex
\text{Var}^*[\tilde{c}_{OLH}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```
![Equation 18](equations_svg/eq18.svg)

**Terms:** `descriptions_latex/desc_eq18.tex` → `descriptions_svg/desc_eq18.svg`
![Description 18](descriptions_svg/desc_eq18.svg)

---

## Part 3: Attack Gain Formulas
*Source: attacks.pdf*

### Equation 19: Total Attack Gain Function
**LaTeX Source:** `equations/eq19.tex` → **Image:** `equations_svg/eq19.svg`
```latex
G(Y) = \sum_{t \in T} E[\Delta \tilde{f}_t]
```
![Equation 19](equations_svg/eq19.svg)

**Terms:** `descriptions_latex/desc_eq19.tex` → `descriptions_svg/desc_eq19.svg`
![Description 19](descriptions_svg/desc_eq19.svg)

---

### Equation 20: Attack Optimization Objective
**LaTeX Source:** `equations/eq20.tex` → **Image:** `equations_svg/eq20.svg`
```latex
\max_{Y} G(Y)
```
![Equation 20](equations_svg/eq20.svg)

---

### Equation 21: Frequency Gain Definition
**LaTeX Source:** `equations/eq21.tex` → **Image:** `equations_svg/eq21.svg`
```latex
\Delta \tilde{f}_t = \tilde{f}_{t,a} - \tilde{f}_{t,b}
```
![Equation 21](equations_svg/eq21.svg)

**Terms:** `descriptions_latex/desc_eq21.tex` → `descriptions_svg/desc_eq21.svg`
![Description 21](descriptions_svg/desc_eq21.svg)

---

### Equation 22: General Attack Gain Formula
**LaTeX Source:** `equations/eq22.tex` → **Image:** `equations_svg/eq22.svg`
```latex
G = \frac{\sum_{i=n+1}^{n+m} \sum_{t \in T} E[\mathbf{1}_{S(y_i)}(t)]}{(n+m)(p-q)} - c
```
![Equation 22](equations_svg/eq22.svg)

**Terms:** `descriptions_latex/desc_eq22.tex` → `descriptions_svg/desc_eq22.svg`
![Description 22](descriptions_svg/desc_eq22.svg)

---

### Equation 23: kRR RPA Attack Gain
**LaTeX Source:** `equations/eq23.tex` → **Image:** `equations_svg/eq23.svg`
```latex
G = \frac{rm}{d(n+m)(p-q)} - c
```
![Equation 23](equations_svg/eq23.svg)

**Terms:** `descriptions_latex/desc_eq23.tex` → `descriptions_svg/desc_eq23.svg`
![Description 23](descriptions_svg/desc_eq23.svg)

---

### Equation 24: Expected Support Indicator (kRR)
**LaTeX Source:** `equations/eq24.tex` → **Image:** `equations_svg/eq24.svg`
```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```
![Equation 24](equations_svg/eq24.svg)

**Terms:** `descriptions_latex/desc_eq24.tex` → `descriptions_svg/desc_eq24.svg`
![Description 24](descriptions_svg/desc_eq24.svg)

---

### Equation 25: kRR MGA Attack Gain
**LaTeX Source:** `equations/eq25.tex` → **Image:** `equations_svg/eq25.svg`
```latex
G = \frac{m}{(n+m)(p-q)} - c
```
![Equation 25](equations_svg/eq25.svg)

**Terms:** `descriptions_latex/desc_eq25.tex` → `descriptions_svg/desc_eq25.svg`
![Description 25](descriptions_svg/desc_eq25.svg)

---

### Equation 26: Expected Support Indicator (OUE MGA)
**LaTeX Source:** `equations/eq26.tex` → **Image:** `equations_svg/eq26.svg`
```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \Pr(y_{i,t} = 1) = \frac{1}{2}
```
![Equation 26](equations_svg/eq26.svg)

**Terms:** `descriptions_latex/desc_eq26.tex` → `descriptions_svg/desc_eq26.svg`
![Description 26](descriptions_svg/desc_eq26.svg)

---

### Equation 27: Expected Support Indicator (OUE RIA)
**LaTeX Source:** `equations/eq27.tex` → **Image:** `equations_svg/eq27.svg`
```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```
![Equation 27](equations_svg/eq27.svg)

**Terms:** `descriptions_latex/desc_eq27.tex` → `descriptions_svg/desc_eq27.svg`
![Description 27](descriptions_svg/desc_eq27.svg)

---

### Equation 28: OUE MGA Attack Gain
**LaTeX Source:** `equations/eq28.tex` → **Image:** `equations_svg/eq28.svg`
```latex
G = \frac{rm}{(n+m)(p-q)} - c
```
![Equation 28](equations_svg/eq28.svg)

**Terms:** `descriptions_latex/desc_eq28.tex` → `descriptions_svg/desc_eq28.svg`
![Description 28](descriptions_svg/desc_eq28.svg)

---

### Equation 29: Expected Support Indicator (OLH)
**LaTeX Source:** `equations/eq29.tex` → **Image:** `equations_svg/eq29.svg`
```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p' + (1 - \frac{1}{r}) \cdot q'
```
![Equation 29](equations_svg/eq29.svg)

**Terms:** `descriptions_latex/desc_eq29.tex` → `descriptions_svg/desc_eq29.svg`
![Description 29](descriptions_svg/desc_eq29.svg)

---

### Equation 30: OLH Attack Gain
**LaTeX Source:** `equations/eq30.tex` → **Image:** `equations_svg/eq30.svg`
```latex
G = \frac{rm}{(n+m)(p-q)} - c
```
![Equation 30](equations_svg/eq30.svg)

---

### Equation 32: Protocol Selection Threshold
**LaTeX Source:** `equations/eq32.tex` → **Image:** `equations_svg/eq32.svg`
```latex
d < 3e^\varepsilon + 2 \Rightarrow \text{Use DE/kRR}
```
![Equation 32](equations_svg/eq32.svg)

**Terms:** `descriptions_latex/desc_eq32.tex` → `descriptions_svg/desc_eq32.svg`
![Description 32](descriptions_svg/desc_eq32.svg)

---

### Equation 34: Frequency Gain Proportionality
**LaTeX Source:** `equations/eq34.tex` → **Image:** `equations_svg/eq34.svg`
```latex
\text{Frequency Gain} \propto \frac{1}{e^\varepsilon - 1}
```
![Equation 34](equations_svg/eq34.svg)

---

## Part 4: RAPPOR Equations
*Source: rappor.pdf*

### Equation 36: Permanent Randomized Response (B')
**LaTeX Source:** `equations/eq36.tex` → **Image:** `equations_svg/eq36.svg`
```latex
B_i' = \begin{cases} 1, & \text{with probability } \frac{1}{2}f \\ 0, & \text{with probability } \frac{1}{2}f \\ B_i, & \text{with probability } 1-f \end{cases}
```
![Equation 36](equations_svg/eq36.svg)

---

### Equation 37: Longitudinal Privacy
**LaTeX Source:** `equations/eq37.tex` → **Image:** `equations_svg/eq37.svg`
```latex
\varepsilon_\infty = 2h \ln\left(\frac{1 - \frac{1}{2}f}{\frac{1}{2}f}\right)
```
![Equation 37](equations_svg/eq37.svg)

---

### Equation 38: Conditional Probability q*
**LaTeX Source:** `equations/eq38.tex` → **Image:** `equations_svg/eq38.svg`
```latex
q^* = P(S_i = 1 | b_i = 1) = \frac{1}{2}f(p+q) + (1-f)q
```
![Equation 38](equations_svg/eq38.svg)

---

### Equation 39: RAPPOR Unbiased Estimator
**LaTeX Source:** `equations/eq39.tex` → **Image:** `equations_svg/eq39.svg`
```latex
t_{ij} = \frac{c_{ij} - (p + \frac{1}{2}fq - \frac{1}{2}fp)N_j}{(1-f)(q-p)}
```
![Equation 39](equations_svg/eq39.svg)

---

### Equation 40: RAPPOR Variance
**LaTeX Source:** `equations/eq40.tex` → **Image:** `equations_svg/eq40.svg`
```latex
\text{Var}[\tilde{c}(i)] = \frac{nq^*(1-q^*)}{(p^*-q^*)^2} + \frac{nf_i(1-p^*-q^*)}{p^*-q^*}
```
![Equation 40](equations_svg/eq40.svg)

---

### Equation 41: RAPPOR Worst-Case Variance
**LaTeX Source:** `equations/eq41.tex` → **Image:** `equations_svg/eq41.svg`
```latex
\text{Var}^*[\tilde{c}(i)] = \frac{nq^*(1-q^*)}{(p^*-q^*)^2}
```
![Equation 41](equations_svg/eq41.svg)

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

## RAPPOR Slide Equations
*Source: rapor_slide_eqns/*

### Permanent Randomized Response
**Source:** `rapor_slide_eqns/eq1_permanent_randomized_response.tex`
```latex
B'_i = \begin{cases} 1 & \text{with probability } \frac{1}{2}f \\ 0 & \text{with probability } \frac{1}{2}f \\ B_i & \text{with probability } 1 - f \end{cases}
```

### Instantaneous Randomized Response
**Source:** `rapor_slide_eqns/eq2_instantaneous_randomized_response.tex`
```latex
P(S_i = 1) = \begin{cases} q & \text{if } B'_i = 1 \\ p & \text{if } B'_i = 0 \end{cases}
```

### Unbiased Estimator
**Source:** `rapor_slide_eqns/eq3_unbiased_estimator.tex`
```latex
t_{ij} = \frac{c_{ij} - \left(p + \frac{1}{2} f q - \frac{1}{2} f p\right) N_j}{(1 - f)(q - p)}
```

### Longitudinal Privacy
**Source:** `rapor_slide_eqns/eq4_longitudinal_privacy.tex`
```latex
\varepsilon_\infty = 2h \ln \frac{1 - \frac{1}{2}f}{\frac{1}{2}f}
```

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
| $h$ | Number of hash functions in RAPPOR |
