# Equations to Images Mapping

This document maps all equations from [equations.md](equations.md) to their corresponding SVG images in the [potential_images/](potential_images/) folder.

**Total Equations Extracted:** 26 equations from 17 sections
**Total Images Generated:** 26 SVG files

---

## 📋 Complete Equation-to-Image Mapping

### 1. Global Differential Privacy

**Section in equations.md:** Lines 17-30
**Slide:** 4 – *Differential Privacy*
**Paper:** LDP_Freq_Est.pdf

**Equation:**
```latex
\forall t \in \mathrm{Range}(A): \Pr[A(D) = t] \le e^{\varepsilon}\,\Pr[A(D') = t]
```

**Readable Form:**
```
∀t ∈ Range(A): Pr[A(D) = t] ≤ e^ε · Pr[A(D') = t]
```

**Image File:** [eq01_global_differential_privacy.svg](potential_images/eq01_global_differential_privacy.svg)

**Purpose:** Standard (central) DP guarantee

---

### 2. Local Differential Privacy

**Section in equations.md:** Lines 34-47
**Slide:** 5 – *Local Differential Privacy*
**Paper:** LDP_Freq_Est.pdf

**Equation:**
```latex
\forall y \in \mathrm{Range}(A): \Pr[A(v_1) = y] \le e^{\varepsilon}\,\Pr[A(v_2) = y]
```

**Readable Form:**
```
∀y ∈ Range(A): Pr[A(v₁) = y] ≤ e^ε · Pr[A(v₂) = y]
```

**Image File:** [eq02_local_differential_privacy.svg](potential_images/eq02_local_differential_privacy.svg)

**Purpose:** Formalizes the local model where randomizer runs on client's input

---

### 3. Pure Local Differential Privacy Protocol

**Section in equations.md:** Lines 51-75
**Slide:** 7 – *Pure Local Differential Privacy*
**Paper:** LDP_Freq_Est.pdf

**Equation 3a (p* definition):**
```latex
\Pr\!\big[\mathrm{PE}(v_1) \in \{y \mid v_1 \in \mathrm{Support}(y)\}\big] = p^*
```
**Readable Form:**
```
Pr[PE(v₁) ∈ {y | v₁ ∈ Support(y)}] = p*
```
**Image File:** [eq03a_pure_ldp_p_star.svg](potential_images/eq03a_pure_ldp_p_star.svg)

**Equation 3b (q* definition):**
```latex
\Pr\!\big[\mathrm{PE}(v_2) \in \{y \mid v_1 \in \mathrm{Support}(y)\}\big] = q^*, \quad 0 < q^* < p^* < 1
```
**Readable Form:**
```
Pr[PE(v₂) ∈ {y | v₁ ∈ Support(y)}] = q*,  where 0 < q* < p* < 1
```
**Image File:** [eq03b_pure_ldp_q_star.svg](potential_images/eq03b_pure_ldp_q_star.svg)

**Equation 3c (LDP constraint):**
```latex
\frac{p^*}{q^*} \le e^{\varepsilon}
```
**Readable Form:**
```
p*/q* ≤ e^ε
```
**Image File:** [eq03c_pure_ldp_constraint.svg](potential_images/eq03c_pure_ldp_constraint.svg)

**Purpose:** Defines "pure" LDP protocols via two parameters p*, q*

---

### 4. Generic Pure LDP Frequency Estimator

**Section in equations.md:** Lines 78-97
**Slide:** 6 – *Frequency Estimation Problem*
**Paper:** LDP_Freq_Est.pdf

**Equation:**
```latex
\tilde{c}(i) = \frac{\displaystyle \sum_j \mathbf{1}_{\mathrm{Support}(y_j)}(i) - n q^*}{p^* - q^*}
```

**Readable Form:**
```
c̃(i) = (Σⱼ 𝟙_{Support(yⱼ)}(i) - n·q*) / (p* - q*)
```

**Image File:** [eq04_pure_ldp_estimator.svg](potential_images/eq04_pure_ldp_estimator.svg)

**Purpose:** Unified estimator used for all pure LDP protocols

---

### 5. Variance of Pure LDP Estimator

**Section in equations.md:** Lines 101-123
**Slide:** 19 – *Comparison between Estimators*
**Paper:** LDP_Freq_Est.pdf

**Equation 5a (Full variance):**
```latex
\mathrm{Var}[\tilde{c}(i)] = \frac{n q^*(1 - q^*)}{(p^* - q^*)^2} + \frac{n f_i \bigl(1 - p^* - q^*\bigr)}{p^* - q^*}
```
**Readable Form:**
```
Var[c̃(i)] = [n·q*(1-q*)] / (p*-q*)² + [n·fᵢ·(1-p*-q*)] / (p*-q*)
```
**Image File:** [eq05a_variance_full.svg](potential_images/eq05a_variance_full.svg)

**Equation 5b (Approximation for rare items):**
```latex
\mathrm{Var}^*[\tilde{c}(i)] = \frac{n q^*(1 - q^*)}{(p^* - q^*)^2}
```
**Readable Form:**
```
Var*[c̃(i)] = [n·q*(1-q*)] / (p*-q*)²
```
**Image File:** [eq05b_variance_approx.svg](potential_images/eq05b_variance_approx.svg)

**Purpose:** Describes accuracy of any pure LDP protocol

---

### 6. k-ary Randomized Response (kRR) Mechanism

**Section in equations.md:** Lines 126-143
**Slide:** 10 – *K Randomized Response*
**Paper:** attacks.pdf

**Equation:**
```latex
\Pr(y = a) = \begin{cases}
\displaystyle \frac{e^{\varepsilon}}{d - 1 + e^{\varepsilon}}, & a = v \\
\displaystyle \frac{1}{d - 1 + e^{\varepsilon}}, & a \ne v
\end{cases}
```

**Readable Form:**
```
         ⎧ e^ε/(d-1+e^ε),     if a = v
Pr(y=a) = ⎨
         ⎩ 1/(d-1+e^ε),       if a ≠ v
```

**Image File:** [eq06_krr_mechanism.svg](potential_images/eq06_krr_mechanism.svg)

**Purpose:** Basic LDP mechanism used as baseline

---

### 7. Optimized Unary Encoding (OUE) Parameters and Variance

**Section in equations.md:** Lines 147-167
**Slide:** 11 – *Optimized Unary Encoding*
**Paper:** LDP_Freq_Est.pdf

**Equation 7a (Optimized parameters):**
```latex
q = \frac{1}{e^{\varepsilon} + 1}, \qquad p = \frac{1}{2}
```
**Readable Form:**
```
q = 1/(e^ε + 1),  p = 1/2
```
**Image File:** [eq07a_oue_parameters.svg](potential_images/eq07a_oue_parameters.svg)

**Equation 7b (Variance):**
```latex
\mathrm{Var}^*[\tilde{c}_{\mathrm{OUE}}(i)] = n \cdot \frac{4 e^{\varepsilon}}{(e^{\varepsilon} - 1)^2}
```
**Readable Form:**
```
Var*[c̃_OUE(i)] = n · 4e^ε / (e^ε - 1)²
```
**Image File:** [eq07b_oue_variance.svg](potential_images/eq07b_oue_variance.svg)

**Purpose:** Shows how OUE minimizes variance with optimal p,q choice

---

### 8. Optimized Local Hashing (OLH): Parameters & Variance

**Section in equations.md:** Lines 170-205
**Slide:** 12 – *Optimized Local Hashing*
**Paper:** LDP_Freq_Est.pdf

**Equation 8a (Local Hashing perturbation):**
```latex
\Pr[y = i] = \begin{cases}
\displaystyle p = \frac{e^{\varepsilon}}{e^{\varepsilon} + g - 1}, & x = i \\
\displaystyle q = \frac{1}{e^{\varepsilon} + g - 1}, & x \ne i
\end{cases}
```
**Readable Form:**
```
         ⎧ p = e^ε/(e^ε+g-1),     if x = i
Pr[y=i] = ⎨
         ⎩ q = 1/(e^ε+g-1),       if x ≠ i
```
**Image File:** [eq08a_olh_perturbation.svg](potential_images/eq08a_olh_perturbation.svg)

**Equation 8b (Optimal hash range size):**
```latex
g = e^{\varepsilon} + 1
```
**Readable Form:**
```
g = e^ε + 1
```
**Image File:** [eq08b_olh_optimal_g.svg](potential_images/eq08b_olh_optimal_g.svg)

**Equation 8c (Simplified parameters):**
```latex
p^* = \frac{1}{2}, \qquad q^* = \frac{1}{e^{\varepsilon} + 1}
```
**Readable Form:**
```
p* = 1/2,  q* = 1/(e^ε + 1)
```
**Image File:** [eq08c_olh_simplified_params.svg](potential_images/eq08c_olh_simplified_params.svg)

**Equation 8d (Approximate variance):**
```latex
\mathrm{Var}^*[\tilde{c}_{\mathrm{OLH}}(i)] = n \cdot \frac{4 e^{\varepsilon}}{(e^{\varepsilon} - 1)^2}
```
**Readable Form:**
```
Var*[c̃_OLH(i)] = n · 4e^ε / (e^ε - 1)²
```
**Image File:** [eq08d_olh_variance.svg](potential_images/eq08d_olh_variance.svg)

**Purpose:** Defines OLH and shows same asymptotic variance as OUE

---

### 9. Expectation of Support Indicator in Pure LDP

**Section in equations.md:** Lines 208-222
**Slide:** 8 – *Attack – Problem Formulation*
**Paper:** attacks.pdf

**Equation:**
```latex
\sum_{i=1}^{n} \mathbb{E}\big[\mathbf{1}_{S(y_i)}(v)\big] = n \bigl(f_v (p - q) + q\bigr)
```

**Readable Form:**
```
Σᵢ₌₁ⁿ E[𝟙_{S(yᵢ)}(v)] = n·(fᵥ·(p-q) + q)
```

**Image File:** [eq09_support_expectation.svg](potential_images/eq09_support_expectation.svg)

**Purpose:** Connects true frequency to expected number of outputs supporting v

---

### 10. Frequency Gain of an Attack on a Target Item

**Section in equations.md:** Lines 225-246
**Slides:** 8 – *Attack – Problem Formulation*; 20 – *Gain from Attacks*
**Paper:** attacks.pdf

**Equation:**
```latex
\Delta \tilde{f}_t = \frac{1}{n+m} \sum_{i=1}^{n+m} \frac{\mathbf{1}_{S(y_i)}(t) - q}{p - q} - \frac{1}{n} \sum_{i=1}^{n} \frac{\mathbf{1}_{S(y_i)}(t) - q}{p - q}
```

**Readable Form:**
```
Δf̃ₜ = [1/(n+m)]·Σᵢ₌₁ⁿ⁺ᵐ (𝟙_{S(yᵢ)}(t)-q)/(p-q) - (1/n)·Σᵢ₌₁ⁿ (𝟙_{S(yᵢ)}(t)-q)/(p-q)
```

**Image File:** [eq10_frequency_gain.svg](potential_images/eq10_frequency_gain.svg)

**Purpose:** Formalizes how estimated frequency changes due to fake users

---

### 11. Overall Gain for a Set of Targets

**Section in equations.md:** Lines 249-272
**Slide:** 20 – *Gain from Attacks*
**Paper:** attacks.pdf

**Equation:**
```latex
G = \frac{\displaystyle \sum_{i=n+1}^{n+m} \sum_{t \in T} \mathbb{E}\big[\mathbf{1}_{S(y_i)}(t)\big]}{(n + m)(p - q)} - c
```

**Readable Form:**
```
G = [Σᵢ₌ₙ₊₁ⁿ⁺ᵐ Σₜ∈T E[𝟙_{S(yᵢ)}(t)]] / [(n+m)·(p-q)] - c
```

**Image File:** [eq11_overall_gain.svg](potential_images/eq11_overall_gain.svg)

**Purpose:** Aggregates per-target gains into single score

---

### 12. Basic One-time RAPPOR Estimator

**Section in equations.md:** Lines 274-291
**Slides:** 6 – *Frequency Estimation Problem* or 9 – *Frequency Estimation Techniques*
**Paper:** rapor.pdf

**Equation 12a (Expected count):**
```latex
\mathbb{E}[C_i] = q T_i + p (N - T_i)
```
**Readable Form:**
```
E[Cᵢ] = q·Tᵢ + p·(N - Tᵢ)
```
**Image File:** [eq12a_rappor_expected_count.svg](potential_images/eq12a_rappor_expected_count.svg)

**Equation 12b (Estimator):**
```latex
\hat{T}_i = \frac{C_i - pN}{q - p}
```
**Readable Form:**
```
T̂ᵢ = (Cᵢ - p·N) / (q - p)
```
**Image File:** [eq12b_rappor_estimator.svg](potential_images/eq12b_rappor_estimator.svg)

**Purpose:** Canonical decoding for Basic One-time RAPPOR

---

### 13. Variance of Basic RAPPOR Estimator

**Section in equations.md:** Lines 293-308
**Slides:** 18 – *Evaluation* or 19 – *Comparison between Estimators*
**Paper:** rapor.pdf

**Equation:**
```latex
\mathrm{Var}(\hat{T}_i) = \frac{p(1 - p)N}{(q - p)^2}
```

**Readable Form:**
```
Var(T̂ᵢ) = [p·(1-p)·N] / (q-p)²
```

**Image File:** [eq13_rappor_variance.svg](potential_images/eq13_rappor_variance.svg)

**Purpose:** Closed-form variance in terms of RAPPOR's parameters

---

### 14. Local Hashing (LH/OLH) Privacy Guarantee

**Section in equations.md:** Lines 311-327
**Slides:** 5 – *Local Differential Privacy* or 12 – *Optimized Local Hashing*
**Paper:** LDP_Freq_Est.pdf

**Equation:**
```latex
\frac{\Pr[\langle H,y\rangle \mid v_1]}{\Pr[\langle H,y\rangle \mid v_2]} = \frac{\Pr[\mathrm{Perturb}(H(v_1)) = y]}{\Pr[\mathrm{Perturb}(H(v_2)) = y]} \le \frac{p}{q} = e^{\varepsilon}
```

**Readable Form:**
```
Pr[⟨H,y⟩|v₁] / Pr[⟨H,y⟩|v₂] = Pr[Perturb(H(v₁))=y] / Pr[Perturb(H(v₂))=y] ≤ p/q = e^ε
```

**Image File:** [eq14_olh_privacy_guarantee.svg](potential_images/eq14_olh_privacy_guarantee.svg)

**Purpose:** Shows how hashing still satisfies ε-LDP

---

### 15. RAPPOR Permanent Randomized Response Privacy

**Section in equations.md:** Lines 335-351
**Suggested slide:** *Translating RAPPOR Parameters to ε*
**Paper:** rapor.pdf

**Equation:**
```latex
\varepsilon_{\infty} = 2h \,\ln\!\left(\frac{1 - \tfrac{1}{2}f}{\tfrac{1}{2} f}\right)
```

**Readable Form:**
```
ε_∞ = 2h · ln[(1 - f/2) / (f/2)]
```

**Image File:** [eq15_rappor_longterm_epsilon.svg](potential_images/eq15_rappor_longterm_epsilon.svg)

**Purpose:** Connects engineering parameters to formal ε guarantee for long-term privacy

---

### 16. RAPPOR Instantaneous Randomized Response Privacy

**Section in equations.md:** Lines 354-377
**Suggested slide:** *Longitudinal vs One-time Privacy in RAPPOR*
**Paper:** rapor.pdf

**Equation 16a (Instantaneous ε):**
```latex
\varepsilon_{1} = h \log\!\left(\frac{q^*(1 - p^*)}{p^*(1 - q^*)}\right)
```
**Readable Form:**
```
ε₁ = h · log[q*(1-p*) / p*(1-q*)]
```
**Image File:** [eq16a_rappor_instantaneous_epsilon.svg](potential_images/eq16a_rappor_instantaneous_epsilon.svg)

**Equation 16b (Probability definitions):**
```latex
q^* = \Pr(S_i = 1 \mid b_i = 1), \quad p^* = \Pr(S_i = 1 \mid b_i = 0)
```
**Readable Form:**
```
q* = Pr(Sᵢ=1|bᵢ=1),  p* = Pr(Sᵢ=1|bᵢ=0)
```
**Image File:** [eq16b_rappor_probs.svg](potential_images/eq16b_rappor_probs.svg)

**Purpose:** Separates instantaneous ε from longitudinal ε

---

### 17. Security Threshold for kRR vs OUE/OLH

**Section in equations.md:** Lines 380-393
**Suggested slide:** *When Are OUE and OLH More Secure than kRR?*
**Paper:** attacks.pdf

**Equation:**
```latex
d > (2r - 1)\bigl(e^{\varepsilon} - 1\bigr) + 3r
```

**Readable Form:**
```
d > (2r - 1)·(e^ε - 1) + 3r
```

**Image File:** [eq17_security_threshold.svg](potential_images/eq17_security_threshold.svg)

**Purpose:** Analytic condition for when OUE/OLH are more robust to attacks than kRR

---

## 📊 Summary Statistics

| Category | Count | Files |
|----------|-------|-------|
| **Fundamental Definitions** | 5 | eq01, eq02, eq03a-c |
| **Estimators & Variance** | 6 | eq04, eq05a-b, eq07b, eq08d, eq13 |
| **Protocol Mechanisms** | 5 | eq06, eq07a, eq08a-c |
| **Attack Formulations** | 3 | eq09, eq10, eq11 |
| **RAPPOR Specific** | 5 | eq12a-b, eq15, eq16a-b |
| **Privacy Guarantees** | 2 | eq14, eq17 |
| **TOTAL** | **26** | **26 SVG images** |

---

## 🎯 Usage Guide

### Accessing Images

All SVG images are located in the [potential_images/](potential_images/) folder and can be directly inserted into your presentation.

### File Naming Convention

```
eq[NUMBER][LETTER]_[DESCRIPTIVE_NAME].svg
```

Where:
- `[NUMBER]` = Section number from equations.md (01-17)
- `[LETTER]` = Sub-equation identifier (a, b, c, d) when multiple equations exist in one section
- `[DESCRIPTIVE_NAME]` = Brief description of the equation

### Quick Reference by Slide

**Slide 4 (Differential Privacy):** eq01
**Slide 5 (Local DP):** eq02, eq14
**Slide 6 (Frequency Estimation):** eq04, eq12a-b
**Slide 7 (Pure LDP):** eq03a-c
**Slide 8 (Attack Formulation):** eq09, eq10
**Slide 10 (kRR):** eq06
**Slide 11 (OUE):** eq07a-b
**Slide 12 (OLH):** eq08a-d, eq14
**Slides 18-20 (Evaluation/Comparison):** eq05a-b, eq11, eq13, eq17

---

## 🚀 Converting Additional Equations

To add more equations:

1. Create a new `.tex` file in `potential_equations/`:
   ```bash
   echo "\\begin{equation*}\n[YOUR LATEX HERE]\n\\end{equation*}" > potential_equations/new_equation.tex
   ```

2. Run the converter:
   ```bash
   python latex_to_svg.py -e potential_equations -i potential_images
   ```

3. The SVG will be generated in `potential_images/`

---

**Last Updated:** November 27, 2025
**Generated from:** [equations.md](equations.md)
**Converter Script:** [latex_to_svg.py](latex_to_svg.py)
