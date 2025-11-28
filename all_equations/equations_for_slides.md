# Equations for Presentation: A Unified View of Frequency Estimation and their Attacks on Local Differential Privacy

---

## Slide: Differential Privacy

### Equation 1: Differential Privacy Definition

**LaTeX:**
```latex
\forall t \in \text{Range}(A) : \Pr[A(D) = t] \leq e^\varepsilon \Pr[A(D') = t]
```

**Readable Version:**
For all outputs t in the range of algorithm A: The probability that A(D) equals t is at most e^ε times the probability that A(D') equals t, where D and D' are datasets differing in one element.

**Source:** LDP_Freq_Est.pdf, Section 2 (Definition 1), Page 730

**Why it belongs:** This is the foundational definition of Differential Privacy that the presentation introduces as a core concept.

---

## Slide: Local Differential Privacy

### Equation 2: Local Differential Privacy Definition

**LaTeX:**
```latex
\forall y \in \text{Range}(A) : \Pr[A(v_1) = y] \leq e^\varepsilon \Pr[A(v_2) = y]
```

**Readable Version:**
For all possible outputs y: The probability that algorithm A outputs y given input v₁ is at most e^ε times the probability that A outputs y given input v₂.

**Source:** LDP_Freq_Est.pdf, Section 2.1 (Definition 2), Page 730

**Why it belongs:** This defines Local Differential Privacy, which is the key privacy model discussed in the presentation.

---

### Equation 3: LDP Definition (Alternative Form from Attacks Paper)

**LaTeX:**
```latex
\Pr(PE(v_1) = y) \leq e^\varepsilon \Pr(PE(v_2) = y)
```

**Readable Version:**
The probability that the perturbed encoded value of v₁ equals y is at most e^ε times the probability that the perturbed encoded value of v₂ equals y.

**Source:** attacks.pdf, Section 2.1 (Definition 1), Page 3

**Why it belongs:** This provides the mathematical foundation for understanding how LDP protocols work.

---

## Slide: Frequency Estimation Problem

### Equation 4: Frequency Estimation Formula (Pure LDP)

**LaTeX:**
```latex
\tilde{f}_v = \frac{\frac{1}{n} \sum_{i=1}^{n} \mathbf{1}_{S(y_i)}(v) - q}{p - q}
```

**Readable Version:**
The estimated frequency for item v equals: (the average count of perturbed values supporting v, minus q) divided by (p - q), where p and q are the perturbation probabilities.

**Source:** attacks.pdf, Section 2.1, Equation (3), Page 3

**Why it belongs:** This is the core aggregation formula used for frequency estimation in Pure LDP protocols.

---

### Equation 5: Unbiased Estimator Property

**LaTeX:**
```latex
\sum_{i=1}^{n} E[\mathbf{1}_{S(y_i)}(v)] = n(f_v(p-q) + q)
```

**Readable Version:**
The sum of expected characteristic functions equals n times (true frequency times (p-q) plus q).

**Source:** attacks.pdf, Section 2.1, Equation (4), Page 3

**Why it belongs:** This shows that Pure LDP protocols are unbiased estimators.

---

## Slide: Pure Local Differential Privacy

### Equation 6: Pure LDP Definition - Probability p

**LaTeX:**
```latex
\Pr(PE(v_1) \in \{y | v_1 \in S(y)\}) = p
```

**Readable Version:**
The probability that an item v₁ is perturbed to a value in its own support set equals p.

**Source:** attacks.pdf, Section 2.1 (Definition 2), Equation (1), Page 3

**Why it belongs:** This defines the first condition for a Pure LDP protocol.

---

### Equation 7: Pure LDP Definition - Probability q

**LaTeX:**
```latex
\Pr(PE(v_2) \in \{y | v_1 \in S(y)\}) = q
```

**Readable Version:**
The probability that an item v₂ (≠ v₁) is perturbed to a value in v₁'s support set equals q.

**Source:** attacks.pdf, Section 2.1 (Definition 2), Equation (2), Page 3

**Why it belongs:** This defines the second condition for a Pure LDP protocol.

---

### Equation 8: Pure Protocol Definition (Framework Paper)

**LaTeX:**
```latex
\Pr[PE(v_1) \in \{y | v_1 \in \text{Support}(y)\}] = p^*
```
```latex
\forall v_2 \neq v_1 : \Pr[PE(v_2) \in \{y | v_1 \in \text{Support}(y)\}] = q^*
```

**Readable Version:**
For a pure protocol, the probability that any value v₁ maps to its own support set is p*, and the probability that any other value v₂ maps to v₁'s support set is q*.

**Source:** LDP_Freq_Est.pdf, Section 3 (Definition 3), Page 732

**Why it belongs:** This provides the formal framework definition of Pure LDP protocols.

---

## Slide: K Randomized Response

### Equation 9: kRR Perturbation Probabilities

**LaTeX:**
```latex
\Pr(y = a) = \begin{cases} \frac{e^\varepsilon}{d-1+e^\varepsilon} = p, & \text{if } a = v \\ \frac{1}{d-1+e^\varepsilon} = q, & \text{otherwise} \end{cases}
```

**Readable Version:**
For kRR: The probability of outputting the true value is e^ε/(d-1+e^ε), and the probability of outputting any other value is 1/(d-1+e^ε).

**Source:** attacks.pdf, Section 2.1.1, Equation (5), Page 3

**Why it belongs:** This defines the perturbation mechanism for the kRR protocol.

---

### Equation 10: Direct Encoding Perturbation (Equivalent to kRR)

**LaTeX:**
```latex
\Pr[\text{Perturb}_{DE}(x) = i] = \begin{cases} p = \frac{e^\varepsilon}{e^\varepsilon + d - 1}, & \text{if } i = x \\ q = \frac{1}{e^\varepsilon + d - 1}, & \text{if } i \neq x \end{cases}
```

**Readable Version:**
The probability of outputting the true value i=x is e^ε/(e^ε+d-1), otherwise it's 1/(e^ε+d-1).

**Source:** LDP_Freq_Est.pdf, Section 4.1, Page 734

**Why it belongs:** This is the same as kRR, showing the Direct Encoding method.

---

### Equation 11: Variance of Direct Encoding / kRR

**LaTeX:**
```latex
\text{Var}^*[\tilde{c}_{DE}(i)] = n \cdot \frac{d - 2 + e^\varepsilon}{(e^\varepsilon - 1)^2}
```

**Readable Version:**
The variance of the frequency estimate for Direct Encoding equals n times (d-2+e^ε) divided by (e^ε-1)².

**Source:** LDP_Freq_Est.pdf, Section 4.1, Page 734

**Why it belongs:** This shows how the estimation error scales with domain size d for kRR.

---

## Slide: Optimized Unary Encoding

### Equation 12: OUE Perturbation Probabilities

**LaTeX:**
```latex
\Pr(y_i = 1) = \begin{cases} \frac{1}{2} = p, & \text{if } i = v \\ \frac{1}{e^\varepsilon + 1} = q, & \text{otherwise} \end{cases}
```

**Readable Version:**
For OUE: A bit at position v (the true value) stays 1 with probability 1/2, while other bits become 1 with probability 1/(e^ε+1).

**Source:** attacks.pdf, Section 2.1.2, Equation (6), Page 3

**Why it belongs:** This defines the perturbation mechanism for OUE.

---

### Equation 13: OUE Variance

**LaTeX:**
```latex
\text{Var}^*[\tilde{c}_{OUE}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```

**Readable Version:**
The variance of OUE's frequency estimate equals n times 4e^ε divided by (e^ε-1)².

**Source:** LDP_Freq_Est.pdf, Section 4.3, Equation (9), Page 735

**Why it belongs:** This shows the optimal variance achieved by OUE.

---

### Equation 14: Privacy of Unary Encoding

**LaTeX:**
```latex
\varepsilon = \ln\left(\frac{p(1-q)}{(1-p)q}\right)
```

**Readable Version:**
The privacy budget ε equals the natural log of (p times (1-q)) divided by ((1-p) times q).

**Source:** LDP_Freq_Est.pdf, Section 4.3, Equation (5), Page 735

**Why it belongs:** This shows how ε relates to the perturbation probabilities p and q.

---

## Slide: Optimized Local Hashing

### Equation 15: OLH Perturbation Probabilities

**LaTeX:**
```latex
\Pr(y = (H, a)) = \begin{cases} \frac{e^\varepsilon}{e^\varepsilon + d' - 1} = p', & \text{if } a = H(v) \\ \frac{1}{e^\varepsilon + d' - 1} = q', & \text{otherwise} \end{cases}
```

**Readable Version:**
For OLH: The probability of reporting the correct hash value is e^ε/(e^ε+d'-1), where d' = e^ε+1 is the hash range.

**Source:** attacks.pdf, Section 2.1.3, Equation (7), Page 3-4

**Why it belongs:** This defines the perturbation mechanism for OLH.

---

### Equation 16: OLH Overall Probability Parameters

**LaTeX:**
```latex
p = p' = \frac{e^\varepsilon}{e^\varepsilon + d' - 1}, \quad q = \frac{1}{d'} \cdot p' + (1 - \frac{1}{d'}) \cdot q' = \frac{1}{d'}
```

**Readable Version:**
For OLH: p equals e^ε/(e^ε+d'-1) and q equals 1/d'.

**Source:** attacks.pdf, Section 2.1.3, Page 4

**Why it belongs:** This shows how OLH's probabilities simplify when using the optimal hash range.

---

### Equation 17: Optimal Hash Range for OLH

**LaTeX:**
```latex
g = e^\varepsilon + 1
```

**Readable Version:**
The optimal number of hash buckets g equals e^ε + 1.

**Source:** LDP_Freq_Est.pdf, Section 4.4, Page 736

**Why it belongs:** This shows the key optimization that makes OLH achieve optimal variance.

---

### Equation 18: OLH Variance

**LaTeX:**
```latex
\text{Var}^*[\tilde{c}_{OLH}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```

**Readable Version:**
The variance of OLH equals n times 4e^ε divided by (e^ε-1)², which is the same as OUE.

**Source:** LDP_Freq_Est.pdf, Section 4.4, Equation (11), Page 736

**Why it belongs:** This shows that OLH achieves the same optimal variance as OUE.

---

## Slide: Attack – Problem Formulation

### Equation 19: Attack Objective - Overall Gain

**LaTeX:**
```latex
G(Y) = \sum_{t \in T} E[\Delta \tilde{f}_t]
```

**Readable Version:**
The overall gain G is the sum of expected frequency gains for all target items in set T.

**Source:** attacks.pdf, Section 3.1, Page 5

**Why it belongs:** This defines the attacker's objective function.

---

### Equation 20: Attack Optimization Problem

**LaTeX:**
```latex
\max_{Y} G(Y)
```

**Readable Version:**
The attacker aims to maximize the overall gain G by choosing the optimal set of perturbed values Y for fake users.

**Source:** attacks.pdf, Section 3.1, Equation (8), Page 5

**Why it belongs:** This formalizes the attack as an optimization problem.

---

### Equation 21: Frequency Gain Definition

**LaTeX:**
```latex
\Delta \tilde{f}_t = \tilde{f}_{t,a} - \tilde{f}_{t,b}
```

**Readable Version:**
The frequency gain for target item t is the estimated frequency after attack minus the estimated frequency before attack.

**Source:** attacks.pdf, Section 3.1, Page 5

**Why it belongs:** This defines how attack success is measured.

---

## Slide: Attack Types

### Equation 22: Overall Gain Formula

**LaTeX:**
```latex
G = \frac{\sum_{i=n+1}^{n+m} \sum_{t \in T} E[\mathbf{1}_{S(y_i)}(t)]}{(n+m)(p-q)} - c
```

**Readable Version:**
The overall gain equals the sum of expected supports for target items from fake users, divided by ((n+m)(p-q)), minus a constant c.

**Source:** attacks.pdf, Section 3.2, Equation (13), Page 5

**Why it belongs:** This is the key formula used to analyze all three attack types.

---

## Slide: Attacking kRR

### Equation 23: kRR - RPA Overall Gain

**LaTeX:**
```latex
G = \frac{rm}{d(n+m)(p-q)} - c
```

**Readable Version:**
For Random Perturbed-value Attack on kRR: The gain equals (r×m)/(d×(n+m)×(p-q)) minus c, where r is the number of target items.

**Source:** attacks.pdf, Section 3.3, Page 6

**Why it belongs:** This shows the gain formula for the baseline attack on kRR.

---

### Equation 24: kRR - RIA Expected Characteristic Function

**LaTeX:**
```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```

**Readable Version:**
The expected characteristic function equals (1/r)×p + (1-1/r)×q.

**Source:** attacks.pdf, Section 3.3, Equation (21), Page 6

**Why it belongs:** This shows how RIA calculates expected support.

---

### Equation 25: kRR - MGA Overall Gain

**LaTeX:**
```latex
G = \frac{m}{(n+m)(p-q)} - c
```

**Readable Version:**
For Maximal Gain Attack on kRR: The gain equals m/((n+m)(p-q)) minus c.

**Source:** attacks.pdf, Section 3.3, Page 6

**Why it belongs:** This shows the optimal gain achievable on kRR.

---

## Slide: Attacking OUE

### Equation 26: OUE - RPA Expected Support

**LaTeX:**
```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \Pr(y_{i,t} = 1) = \frac{1}{2}
```

**Readable Version:**
For RPA on OUE: The expected support equals 1/2 (since each bit is randomly set).

**Source:** attacks.pdf, Section 3.4, Equation (22), Page 6

**Why it belongs:** This analyzes the baseline attack on OUE.

---

### Equation 27: OUE - RIA Expected Support

**LaTeX:**
```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```

**Readable Version:**
For RIA on OUE: The expected support equals (1/r)×p + (1-1/r)×q.

**Source:** attacks.pdf, Section 3.4, Equation (24), Page 6

**Why it belongs:** This shows how RIA works on OUE.

---

### Equation 28: OUE - MGA Overall Gain

**LaTeX:**
```latex
G = \frac{rm}{(n+m)(p-q)} - c
```

**Readable Version:**
For MGA on OUE: The gain equals (r×m)/((n+m)(p-q)) minus c.

**Source:** attacks.pdf, Section 3.4, Page 6

**Why it belongs:** This shows the optimal gain achievable on OUE.

---

## Slide: Attacking OLH

### Equation 29: OLH - RIA Expected Support

**LaTeX:**
```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p' + (1 - \frac{1}{r}) \cdot q'
```

**Readable Version:**
For RIA on OLH: The expected support equals (1/r)×p' + (1-1/r)×q'.

**Source:** attacks.pdf, Section 3.5, Equation (27), Page 7

**Why it belongs:** This analyzes RIA on OLH.

---

### Equation 30: OLH - MGA Overall Gain

**LaTeX:**
```latex
G = \frac{rm}{(n+m)(p-q)} - c
```

**Readable Version:**
For MGA on OLH: The gain equals (r×m)/((n+m)(p-q)) minus c (same as OUE).

**Source:** attacks.pdf, Section 3.5, Page 7

**Why it belongs:** This shows OLH has similar vulnerability to OUE.

---

## Slide: Comparison between Estimators

### Equation 31: Variance Comparison Table

**LaTeX:**
| Protocol | Variance |
|----------|----------|
| DE/kRR | $n \cdot \frac{d-2+e^\varepsilon}{(e^\varepsilon-1)^2}$ |
| OUE | $n \cdot \frac{4e^\varepsilon}{(e^\varepsilon-1)^2}$ |
| OLH | $n \cdot \frac{4e^\varepsilon}{(e^\varepsilon-1)^2}$ |

**Readable Version:**
- kRR variance depends on domain size d
- OUE and OLH have the same variance, independent of d

**Source:** LDP_Freq_Est.pdf, Table 1, Page 737

**Why it belongs:** This provides the key comparison between estimator accuracies.

---

### Equation 32: When to Use Each Protocol

**LaTeX:**
```latex
d < 3e^\varepsilon + 2 \Rightarrow \text{Use DE/kRR}
```
```latex
d > 3e^\varepsilon + 2 \Rightarrow \text{Use OUE or OLH}
```

**Readable Version:**
Use kRR when domain size d < 3e^ε + 2; otherwise use OUE or OLH.

**Source:** LDP_Freq_Est.pdf, Section 5, Page 737

**Why it belongs:** This provides practical guidance on protocol selection.

---

## Slide: Gain from Attacks

### Equation 33: Overall Gain Summary Table

**LaTeX:**
| Attack | kRR | OUE | OLH |
|--------|-----|-----|-----|
| RPA | $\beta(\frac{r}{d} - f_T)$ | $\beta(r - f_T)$ | $-\beta f_T$ |
| RIA | $\beta(1 - f_T)$ | $\beta(1 - f_T)$ | $\beta(1 - f_T)$ |
| MGA | $\beta(1-f_T) + \frac{\beta(d-r)}{e^\varepsilon-1}$ | $\beta(2r-f_T) + \frac{2\beta r}{e^\varepsilon-1}$ | $\beta(2r-f_T) + \frac{2\beta r}{e^\varepsilon-1}$ |

where $\beta = \frac{m}{n+m}$

**Readable Version:**
MGA achieves the largest gain; β represents the fraction of fake users among all users.

**Source:** attacks.pdf, Table 1, Page 7

**Why it belongs:** This summarizes the attack effectiveness for all protocol-attack combinations.

---

## Slide: Impacts of Parameters on Attacks

### Equation 34: Security-Privacy Tradeoff

**LaTeX:**
```latex
\text{Frequency Gain} \propto \frac{1}{e^\varepsilon - 1}
```

**Readable Version:**
As ε decreases (stronger privacy), the frequency gain from attacks increases (weaker security).

**Source:** attacks.pdf, Section 3.6, Page 7

**Why it belongs:** This demonstrates the fundamental security-privacy tradeoff.

---

### Equation 35: Standard Deviation of Estimation

**LaTeX:**
| Protocol | Standard Deviation |
|----------|-------------------|
| kRR | $\frac{r\sqrt{d-2+e^\varepsilon}}{(e^\varepsilon-1)\sqrt{n}}$ |
| OUE | $\frac{2re^{\varepsilon/2}}{(e^\varepsilon-1)\sqrt{n}}$ |
| OLH | $\frac{2re^{\varepsilon/2}}{(e^\varepsilon-1)\sqrt{n}}$ |

**Readable Version:**
The standard deviation of estimation decreases with √n, showing attacks are significant compared to natural noise.

**Source:** attacks.pdf, Table 1, Page 7

**Why it belongs:** This shows that attack gains are much larger than estimation noise.

---

## Supplementary Equations for RAPPOR Context

### Equation 36: RAPPOR Permanent Randomized Response

**LaTeX:**
```latex
B_i' = \begin{cases} 1, & \text{with probability } \frac{1}{2}f \\ 0, & \text{with probability } \frac{1}{2}f \\ B_i, & \text{with probability } 1-f \end{cases}
```

**Readable Version:**
Each bit is set to 1 with probability f/2, to 0 with probability f/2, or kept unchanged with probability 1-f.

**Source:** rapor.pdf, Section 2, Step 2, Page 4

**Why it belongs:** This is the memoization step that provides longitudinal privacy in RAPPOR.

---

### Equation 37: RAPPOR Differential Privacy Guarantee

**LaTeX:**
```latex
\varepsilon_\infty = 2h \ln\left(\frac{1 - \frac{1}{2}f}{\frac{1}{2}f}\right)
```

**Readable Version:**
The infinite-collection privacy guarantee equals 2h times ln((1-f/2)/(f/2)), where h is the number of hash functions.

**Source:** rapor.pdf, Section 3.1, Theorem 1, Page 5

**Why it belongs:** This shows RAPPOR's privacy guarantee for longitudinal data collection.

---

### Equation 38: RAPPOR Instantaneous Response Probabilities

**LaTeX:**
```latex
q^* = P(S_i = 1 | b_i = 1) = \frac{1}{2}f(p+q) + (1-f)q
```
```latex
p^* = P(S_i = 1 | b_i = 0) = \frac{1}{2}f(p+q) + (1-f)p
```

**Readable Version:**
The probability of observing 1 depends on both the permanent response and instantaneous randomization parameters.

**Source:** rapor.pdf, Section 3.2, Lemma 1, Page 6

**Why it belongs:** This defines the combined effect of RAPPOR's two-stage randomization.

---

### Equation 39: RAPPOR Frequency Estimation

**LaTeX:**
```latex
t_{ij} = \frac{c_{ij} - (p + \frac{1}{2}fq - \frac{1}{2}fp)N_j}{(1-f)(q-p)}
```

**Readable Version:**
The estimated count for bit i in cohort j is calculated by adjusting the observed count for randomization effects.

**Source:** rapor.pdf, Section 4, Page 6

**Why it belongs:** This shows how RAPPOR aggregates and decodes noisy reports.

---

### Equation 40: Framework Variance Formula

**LaTeX:**
```latex
\text{Var}[\tilde{c}(i)] = \frac{nq^*(1-q^*)}{(p^*-q^*)^2} + \frac{nf_i(1-p^*-q^*)}{p^*-q^*}
```

**Readable Version:**
The variance has two terms: one depending on q* and one depending on the true frequency f_i.

**Source:** LDP_Freq_Est.pdf, Section 3, Equation (2), Page 733

**Why it belongs:** This is the general variance formula for pure LDP protocols.

---

### Equation 41: Approximate Variance (for infrequent values)

**LaTeX:**
```latex
\text{Var}^*[\tilde{c}(i)] = \frac{nq^*(1-q^*)}{(p^*-q^*)^2}
```

**Readable Version:**
When f_i is small, the variance is dominated by the first term only.

**Source:** LDP_Freq_Est.pdf, Section 3, Equation (4), Page 733

**Why it belongs:** This simplification is key for comparing protocol accuracies.

---

## Summary

This document contains 41 equations extracted from three papers:
- **attacks.pdf** (Cao et al.): Data Poisoning Attacks to LDP Protocols
- **LDP_Freq_Est.pdf** (Wang et al.): Locally Differentially Private Protocols for Frequency Estimation
- **rapor.pdf** (Erlingsson et al.): RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response

The equations map to the following slides:
1. **Introductory Concepts** (Slides 31-36): Equations 1-8
2. **Frequency Estimation Techniques** (Slides 37-40): Equations 9-18
3. **Attacks on Frequency Estimators** (Slides 41-45): Equations 19-30
4. **Evaluation** (Slides 46-49): Equations 31-35
5. **Supplementary Context**: Equations 36-41
