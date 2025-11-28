# Equation SVGs

This README embeds each generated equation image and includes all metadata from `equations_for_slides.md`,
plus a Unicode/plain-text representation of the LaTeX.

> Note: Only LaTeX sections under `**LaTeX:**` in `equations_for_slides.md` are considered here.

## Equation 1 – Differential Privacy Definition

![Equation 1](images/eq01.svg)

- **Image file**: `images/eq01.svg`
- **Slide:** Differential Privacy
- **LaTeX:**

```latex
\forall t \in \text{Range}(A) : \Pr[A(D) = t] \leq e^\varepsilon \Pr[A(D') = t]
```


- **Readable Version:** For all outputs t in the range of algorithm A: The probability that A(D) equals t is at most e^ε times the probability that A(D') equals t, where D and D' are datasets differing in one element.
- **Source:** LDP_Freq_Est.pdf, Section 2 (Definition 1), Page 730
- **Why it belongs:** This is the foundational definition of Differential Privacy that the presentation introduces as a core concept.
- **Unicode equation:** `\forall t \in \textRange(A) : \Pr[A(D) = t] \leq e^\varepsilon \Pr[A(D') = t]`

## Equation 2 – Local Differential Privacy Definition

![Equation 2](images/eq02.svg)

- **Image file**: `images/eq02.svg`
- **Slide:** Local Differential Privacy
- **LaTeX:**

```latex
\forall y \in \text{Range}(A) : \Pr[A(v_1) = y] \leq e^\varepsilon \Pr[A(v_2) = y]
```


- **Readable Version:** For all possible outputs y: The probability that algorithm A outputs y given input v₁ is at most e^ε times the probability that A outputs y given input v₂.
- **Source:** LDP_Freq_Est.pdf, Section 2.1 (Definition 2), Page 730
- **Why it belongs:** This defines Local Differential Privacy, which is the key privacy model discussed in the presentation.
- **Unicode equation:** `\forall y \in \textRange(A) : \Pr[A(v_1) = y] \leq e^\varepsilon \Pr[A(v_2) = y]`

## Equation 3 – LDP Definition (Alternative Form from Attacks Paper)

![Equation 3](images/eq03.svg)

- **Image file**: `images/eq03.svg`
- **Slide:** Local Differential Privacy
- **LaTeX:**

```latex
\Pr(PE(v_1) = y) \leq e^\varepsilon \Pr(PE(v_2) = y)
```


- **Readable Version:** The probability that the perturbed encoded value of v₁ equals y is at most e^ε times the probability that the perturbed encoded value of v₂ equals y.
- **Source:** attacks.pdf, Section 2.1 (Definition 1), Page 3
- **Why it belongs:** This provides the mathematical foundation for understanding how LDP protocols work.
- **Unicode equation:** `\Pr(PE(v_1) = y) \leq e^\varepsilon \Pr(PE(v_2) = y)`

## Equation 4 – Frequency Estimation Formula (Pure LDP)

![Equation 4](images/eq04.svg)

- **Image file**: `images/eq04.svg`
- **Slide:** Frequency Estimation Problem
- **LaTeX:**

```latex
\tilde{f}_v = \frac{\frac{1}{n} \sum_{i=1}^{n} \mathbf{1}_{S(y_i)}(v) - q}{p - q}
```


- **Readable Version:** The estimated frequency for item v equals: (the average count of perturbed values supporting v, minus q) divided by (p - q), where p and q are the perturbation probabilities.
- **Source:** attacks.pdf, Section 2.1, Equation (3), Page 3
- **Why it belongs:** This is the core aggregation formula used for frequency estimation in Pure LDP protocols.
- **Unicode equation:** `\tildef_v = \frac\frac1n \sum_i=1^n \mathbf1_S(y_i)(v) - qp - q`

## Equation 5 – Unbiased Estimator Property

![Equation 5](images/eq05.svg)

- **Image file**: `images/eq05.svg`
- **Slide:** Frequency Estimation Problem
- **LaTeX:**

```latex
\sum_{i=1}^{n} E[\mathbf{1}_{S(y_i)}(v)] = n(f_v(p-q) + q)
```


- **Readable Version:** The sum of expected characteristic functions equals n times (true frequency times (p-q) plus q).
- **Source:** attacks.pdf, Section 2.1, Equation (4), Page 3
- **Why it belongs:** This shows that Pure LDP protocols are unbiased estimators.
- **Unicode equation:** `\sum_i=1^n E[\mathbf1_S(y_i)(v)] = n(f_v(p-q) + q)`

## Equation 6 – Pure LDP Definition - Probability p

![Equation 6](images/eq06.svg)

- **Image file**: `images/eq06.svg`
- **Slide:** Pure Local Differential Privacy
- **LaTeX:**

```latex
\Pr(PE(v_1) \in \{y | v_1 \in S(y)\}) = p
```


- **Readable Version:** The probability that an item v₁ is perturbed to a value in its own support set equals p.
- **Source:** attacks.pdf, Section 2.1 (Definition 2), Equation (1), Page 3
- **Why it belongs:** This defines the first condition for a Pure LDP protocol.
- **Unicode equation:** `\Pr(PE(v_1) \in \y | v_1 \in S(y)\) = p`

## Equation 7 – Pure LDP Definition - Probability q

![Equation 7](images/eq07.svg)

- **Image file**: `images/eq07.svg`
- **Slide:** Pure Local Differential Privacy
- **LaTeX:**

```latex
\Pr(PE(v_2) \in \{y | v_1 \in S(y)\}) = q
```


- **Readable Version:** The probability that an item v₂ (≠ v₁) is perturbed to a value in v₁'s support set equals q.
- **Source:** attacks.pdf, Section 2.1 (Definition 2), Equation (2), Page 3
- **Why it belongs:** This defines the second condition for a Pure LDP protocol.
- **Unicode equation:** `\Pr(PE(v_2) \in \y | v_1 \in S(y)\) = q`

## Equation 8 – Pure Protocol Definition (Framework Paper)

![Equation 8](images/eq08.svg)

- **Image file**: `images/eq08.svg`
- **Slide:** Pure Local Differential Privacy
- **LaTeX:**

```latex
\Pr[PE(v_1) \in \{y | v_1 \in \text{Support}(y)\}] = p^*
```
```latex
\forall v_2 \neq v_1 : \Pr[PE(v_2) \in \{y | v_1 \in \text{Support}(y)\}] = q^*
```


- **Readable Version:** For a pure protocol, the probability that any value v₁ maps to its own support set is p*, and the probability that any other value v₂ maps to v₁'s support set is q*.
- **Source:** LDP_Freq_Est.pdf, Section 3 (Definition 3), Page 732
- **Why it belongs:** This provides the formal framework definition of Pure LDP protocols.
- **Unicode equation:** `\Pr[PE(v_1) \in \y | v_1 \in \textSupport(y)\] = p^*`

## Equation 9 – kRR Perturbation Probabilities

![Equation 9](images/eq09.svg)

- **Image file**: `images/eq09.svg`
- **Slide:** K Randomized Response
- **LaTeX:**

```latex
\Pr(y = a) = \begin{cases} \frac{e^\varepsilon}{d-1+e^\varepsilon} = p, & \text{if } a = v \\ \frac{1}{d-1+e^\varepsilon} = q, & \text{otherwise} \end{cases}
```


- **Readable Version:** For kRR: The probability of outputting the true value is e^ε/(d-1+e^ε), and the probability of outputting any other value is 1/(d-1+e^ε).
- **Source:** attacks.pdf, Section 2.1.1, Equation (5), Page 3
- **Why it belongs:** This defines the perturbation mechanism for the kRR protocol.
- **Unicode equation:** `\Pr(y = a) = \begincases \frace^\varepsilond-1+e^\varepsilon = p, & \textif a = v \frac1d-1+e^\varepsilon = q, & \textotherwise \endcases`

## Equation 10 – Direct Encoding Perturbation (Equivalent to kRR)

![Equation 10](images/eq10.svg)

- **Image file**: `images/eq10.svg`
- **Slide:** K Randomized Response
- **LaTeX:**

```latex
\Pr[\text{Perturb}_{DE}(x) = i] = \begin{cases} p = \frac{e^\varepsilon}{e^\varepsilon + d - 1}, & \text{if } i = x \\ q = \frac{1}{e^\varepsilon + d - 1}, & \text{if } i \neq x \end{cases}
```


- **Readable Version:** The probability of outputting the true value i=x is e^ε/(e^ε+d-1), otherwise it's 1/(e^ε+d-1).
- **Source:** LDP_Freq_Est.pdf, Section 4.1, Page 734
- **Why it belongs:** This is the same as kRR, showing the Direct Encoding method.
- **Unicode equation:** `\Pr[\textPerturb_DE(x) = i] = \begincases p = \frace^\varepsilone^\varepsilon + d - 1, & \textif i = x q = \frac1e^\varepsilon + d - 1, & \textif i \neq x \endcases`

## Equation 11 – Variance of Direct Encoding / kRR

![Equation 11](images/eq11.svg)

- **Image file**: `images/eq11.svg`
- **Slide:** K Randomized Response
- **LaTeX:**

```latex
\text{Var}^*[\tilde{c}_{DE}(i)] = n \cdot \frac{d - 2 + e^\varepsilon}{(e^\varepsilon - 1)^2}
```


- **Readable Version:** The variance of the frequency estimate for Direct Encoding equals n times (d-2+e^ε) divided by (e^ε-1)².
- **Source:** LDP_Freq_Est.pdf, Section 4.1, Page 734
- **Why it belongs:** This shows how the estimation error scales with domain size d for kRR.
- **Unicode equation:** `\textVar^*[\tildec_DE(i)] = n \cdot \fracd - 2 + e^\varepsilon(e^\varepsilon - 1)^2`

## Equation 12 – OUE Perturbation Probabilities

![Equation 12](images/eq12.svg)

- **Image file**: `images/eq12.svg`
- **Slide:** Optimized Unary Encoding
- **LaTeX:**

```latex
\Pr(y_i = 1) = \begin{cases} \frac{1}{2} = p, & \text{if } i = v \\ \frac{1}{e^\varepsilon + 1} = q, & \text{otherwise} \end{cases}
```


- **Readable Version:** For OUE: A bit at position v (the true value) stays 1 with probability 1/2, while other bits become 1 with probability 1/(e^ε+1).
- **Source:** attacks.pdf, Section 2.1.2, Equation (6), Page 3
- **Why it belongs:** This defines the perturbation mechanism for OUE.
- **Unicode equation:** `\Pr(y_i = 1) = \begincases \frac12 = p, & \textif i = v \frac1e^\varepsilon + 1 = q, & \textotherwise \endcases`

## Equation 13 – OUE Variance

![Equation 13](images/eq13.svg)

- **Image file**: `images/eq13.svg`
- **Slide:** Optimized Unary Encoding
- **LaTeX:**

```latex
\text{Var}^*[\tilde{c}_{OUE}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```


- **Readable Version:** The variance of OUE's frequency estimate equals n times 4e^ε divided by (e^ε-1)².
- **Source:** LDP_Freq_Est.pdf, Section 4.3, Equation (9), Page 735
- **Why it belongs:** This shows the optimal variance achieved by OUE.
- **Unicode equation:** `\textVar^*[\tildec_OUE(i)] = n \cdot \frac4e^\varepsilon(e^\varepsilon - 1)^2`

## Equation 14 – Privacy of Unary Encoding

![Equation 14](images/eq14.svg)

- **Image file**: `images/eq14.svg`
- **Slide:** Optimized Unary Encoding
- **LaTeX:**

```latex
\varepsilon = \ln\left(\frac{p(1-q)}{(1-p)q}\right)
```


- **Readable Version:** The privacy budget ε equals the natural log of (p times (1-q)) divided by ((1-p) times q).
- **Source:** LDP_Freq_Est.pdf, Section 4.3, Equation (5), Page 735
- **Why it belongs:** This shows how ε relates to the perturbation probabilities p and q.
- **Unicode equation:** `\varepsilon = \ln\left(\fracp(1-q)(1-p)q\right)`

## Equation 15 – OLH Perturbation Probabilities

![Equation 15](images/eq15.svg)

- **Image file**: `images/eq15.svg`
- **Slide:** Optimized Local Hashing
- **LaTeX:**

```latex
\Pr(y = (H, a)) = \begin{cases} \frac{e^\varepsilon}{e^\varepsilon + d' - 1} = p', & \text{if } a = H(v) \\ \frac{1}{e^\varepsilon + d' - 1} = q', & \text{otherwise} \end{cases}
```


- **Readable Version:** For OLH: The probability of reporting the correct hash value is e^ε/(e^ε+d'-1), where d' = e^ε+1 is the hash range.
- **Source:** attacks.pdf, Section 2.1.3, Equation (7), Page 3-4
- **Why it belongs:** This defines the perturbation mechanism for OLH.
- **Unicode equation:** `\Pr(y = (H, a)) = \begincases \frace^\varepsilone^\varepsilon + d' - 1 = p', & \textif a = H(v) \frac1e^\varepsilon + d' - 1 = q', & \textotherwise \endcases`

## Equation 16 – OLH Overall Probability Parameters

![Equation 16](images/eq16.svg)

- **Image file**: `images/eq16.svg`
- **Slide:** Optimized Local Hashing
- **LaTeX:**

```latex
p = p' = \frac{e^\varepsilon}{e^\varepsilon + d' - 1}, \quad q = \frac{1}{d'} \cdot p' + (1 - \frac{1}{d'}) \cdot q' = \frac{1}{d'}
```


- **Readable Version:** For OLH: p equals e^ε/(e^ε+d'-1) and q equals 1/d'.
- **Source:** attacks.pdf, Section 2.1.3, Page 4
- **Why it belongs:** This shows how OLH's probabilities simplify when using the optimal hash range.
- **Unicode equation:** `p = p' = \frace^\varepsilone^\varepsilon + d' - 1, \quad q = \frac1d' \cdot p' + (1 - \frac1d') \cdot q' = \frac1d'`

## Equation 17 – Optimal Hash Range for OLH

![Equation 17](images/eq17.svg)

- **Image file**: `images/eq17.svg`
- **Slide:** Optimized Local Hashing
- **LaTeX:**

```latex
g = e^\varepsilon + 1
```


- **Readable Version:** The optimal number of hash buckets g equals e^ε + 1.
- **Source:** LDP_Freq_Est.pdf, Section 4.4, Page 736
- **Why it belongs:** This shows the key optimization that makes OLH achieve optimal variance.
- **Unicode equation:** `g = e^\varepsilon + 1`

## Equation 18 – OLH Variance

![Equation 18](images/eq18.svg)

- **Image file**: `images/eq18.svg`
- **Slide:** Optimized Local Hashing
- **LaTeX:**

```latex
\text{Var}^*[\tilde{c}_{OLH}(i)] = n \cdot \frac{4e^\varepsilon}{(e^\varepsilon - 1)^2}
```


- **Readable Version:** The variance of OLH equals n times 4e^ε divided by (e^ε-1)², which is the same as OUE.
- **Source:** LDP_Freq_Est.pdf, Section 4.4, Equation (11), Page 736
- **Why it belongs:** This shows that OLH achieves the same optimal variance as OUE.
- **Unicode equation:** `\textVar^*[\tildec_OLH(i)] = n \cdot \frac4e^\varepsilon(e^\varepsilon - 1)^2`

## Equation 19 – Attack Objective - Overall Gain

![Equation 19](images/eq19.svg)

- **Image file**: `images/eq19.svg`
- **Slide:** Attack – Problem Formulation
- **LaTeX:**

```latex
G(Y) = \sum_{t \in T} E[\Delta \tilde{f}_t]
```


- **Readable Version:** The overall gain G is the sum of expected frequency gains for all target items in set T.
- **Source:** attacks.pdf, Section 3.1, Page 5
- **Why it belongs:** This defines the attacker's objective function.
- **Unicode equation:** `G(Y) = \sum_t \in T E[\Delta \tildef_t]`

## Equation 20 – Attack Optimization Problem

![Equation 20](images/eq20.svg)

- **Image file**: `images/eq20.svg`
- **Slide:** Attack – Problem Formulation
- **LaTeX:**

```latex
\max_{Y} G(Y)
```


- **Readable Version:** The attacker aims to maximize the overall gain G by choosing the optimal set of perturbed values Y for fake users.
- **Source:** attacks.pdf, Section 3.1, Equation (8), Page 5
- **Why it belongs:** This formalizes the attack as an optimization problem.
- **Unicode equation:** `\max_Y G(Y)`

## Equation 21 – Frequency Gain Definition

![Equation 21](images/eq21.svg)

- **Image file**: `images/eq21.svg`
- **Slide:** Attack – Problem Formulation
- **LaTeX:**

```latex
\Delta \tilde{f}_t = \tilde{f}_{t,a} - \tilde{f}_{t,b}
```


- **Readable Version:** The frequency gain for target item t is the estimated frequency after attack minus the estimated frequency before attack.
- **Source:** attacks.pdf, Section 3.1, Page 5
- **Why it belongs:** This defines how attack success is measured.
- **Unicode equation:** `\Delta \tildef_t = \tildef_t,a - \tildef_t,b`

## Equation 22 – Overall Gain Formula

![Equation 22](images/eq22.svg)

- **Image file**: `images/eq22.svg`
- **Slide:** Attack Types
- **LaTeX:**

```latex
G = \frac{\sum_{i=n+1}^{n+m} \sum_{t \in T} E[\mathbf{1}_{S(y_i)}(t)]}{(n+m)(p-q)} - c
```


- **Readable Version:** The overall gain equals the sum of expected supports for target items from fake users, divided by ((n+m)(p-q)), minus a constant c.
- **Source:** attacks.pdf, Section 3.2, Equation (13), Page 5
- **Why it belongs:** This is the key formula used to analyze all three attack types.
- **Unicode equation:** `G = \frac\sum_i=n+1^n+m \sum_t \in T E[\mathbf1_S(y_i)(t)](n+m)(p-q) - c`

## Equation 23 – kRR - RPA Overall Gain

![Equation 23](images/eq23.svg)

- **Image file**: `images/eq23.svg`
- **Slide:** Attacking kRR
- **LaTeX:**

```latex
G = \frac{rm}{d(n+m)(p-q)} - c
```


- **Readable Version:** For Random Perturbed-value Attack on kRR: The gain equals (r×m)/(d×(n+m)×(p-q)) minus c, where r is the number of target items.
- **Source:** attacks.pdf, Section 3.3, Page 6
- **Why it belongs:** This shows the gain formula for the baseline attack on kRR.
- **Unicode equation:** `G = \fracrmd(n+m)(p-q) - c`

## Equation 24 – kRR - RIA Expected Characteristic Function

![Equation 24](images/eq24.svg)

- **Image file**: `images/eq24.svg`
- **Slide:** Attacking kRR
- **LaTeX:**

```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```


- **Readable Version:** The expected characteristic function equals (1/r)×p + (1-1/r)×q.
- **Source:** attacks.pdf, Section 3.3, Equation (21), Page 6
- **Why it belongs:** This shows how RIA calculates expected support.
- **Unicode equation:** `E[\mathbf1_S(y_i)(t)] = \frac1r \cdot p + (1 - \frac1r) \cdot q`

## Equation 25 – kRR - MGA Overall Gain

![Equation 25](images/eq25.svg)

- **Image file**: `images/eq25.svg`
- **Slide:** Attacking kRR
- **LaTeX:**

```latex
G = \frac{m}{(n+m)(p-q)} - c
```


- **Readable Version:** For Maximal Gain Attack on kRR: The gain equals m/((n+m)(p-q)) minus c.
- **Source:** attacks.pdf, Section 3.3, Page 6
- **Why it belongs:** This shows the optimal gain achievable on kRR.
- **Unicode equation:** `G = \fracm(n+m)(p-q) - c`

## Equation 26 – OUE - RPA Expected Support

![Equation 26](images/eq26.svg)

- **Image file**: `images/eq26.svg`
- **Slide:** Attacking OUE
- **LaTeX:**

```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \Pr(y_{i,t} = 1) = \frac{1}{2}
```


- **Readable Version:** For RPA on OUE: The expected support equals 1/2 (since each bit is randomly set).
- **Source:** attacks.pdf, Section 3.4, Equation (22), Page 6
- **Why it belongs:** This analyzes the baseline attack on OUE.
- **Unicode equation:** `E[\mathbf1_S(\mathbfy_i)(t)] = \Pr(y_i,t = 1) = \frac12`

## Equation 27 – OUE - RIA Expected Support

![Equation 27](images/eq27.svg)

- **Image file**: `images/eq27.svg`
- **Slide:** Attacking OUE
- **LaTeX:**

```latex
E[\mathbf{1}_{S(\mathbf{y}_i)}(t)] = \frac{1}{r} \cdot p + (1 - \frac{1}{r}) \cdot q
```


- **Readable Version:** For RIA on OUE: The expected support equals (1/r)×p + (1-1/r)×q.
- **Source:** attacks.pdf, Section 3.4, Equation (24), Page 6
- **Why it belongs:** This shows how RIA works on OUE.
- **Unicode equation:** `E[\mathbf1_S(\mathbfy_i)(t)] = \frac1r \cdot p + (1 - \frac1r) \cdot q`

## Equation 28 – OUE - MGA Overall Gain

![Equation 28](images/eq28.svg)

- **Image file**: `images/eq28.svg`
- **Slide:** Attacking OUE
- **LaTeX:**

```latex
G = \frac{rm}{(n+m)(p-q)} - c
```


- **Readable Version:** For MGA on OUE: The gain equals (r×m)/((n+m)(p-q)) minus c.
- **Source:** attacks.pdf, Section 3.4, Page 6
- **Why it belongs:** This shows the optimal gain achievable on OUE.
- **Unicode equation:** `G = \fracrm(n+m)(p-q) - c`

## Equation 29 – OLH - RIA Expected Support

![Equation 29](images/eq29.svg)

- **Image file**: `images/eq29.svg`
- **Slide:** Attacking OLH
- **LaTeX:**

```latex
E[\mathbf{1}_{S(y_i)}(t)] = \frac{1}{r} \cdot p' + (1 - \frac{1}{r}) \cdot q'
```


- **Readable Version:** For RIA on OLH: The expected support equals (1/r)×p' + (1-1/r)×q'.
- **Source:** attacks.pdf, Section 3.5, Equation (27), Page 7
- **Why it belongs:** This analyzes RIA on OLH.
- **Unicode equation:** `E[\mathbf1_S(y_i)(t)] = \frac1r \cdot p' + (1 - \frac1r) \cdot q'`

## Equation 30 – OLH - MGA Overall Gain

![Equation 30](images/eq30.svg)

- **Image file**: `images/eq30.svg`
- **Slide:** Attacking OLH
- **LaTeX:**

```latex
G = \frac{rm}{(n+m)(p-q)} - c
```


- **Readable Version:** For MGA on OLH: The gain equals (r×m)/((n+m)(p-q)) minus c (same as OUE).
- **Source:** attacks.pdf, Section 3.5, Page 7
- **Why it belongs:** This shows OLH has similar vulnerability to OUE.
- **Unicode equation:** `G = \fracrm(n+m)(p-q) - c`

## Equation 31 – Variance Comparison Table

> **Note:** No SVG image was generated for this equation.
- **Slide:** Comparison between Estimators
- **LaTeX:**

| Protocol | Variance |
|----------|----------|
| DE/kRR | $n \cdot \frac{d-2+e^\varepsilon}{(e^\varepsilon-1)^2}$ |
| OUE | $n \cdot \frac{4e^\varepsilon}{(e^\varepsilon-1)^2}$ |
| OLH | $n \cdot \frac{4e^\varepsilon}{(e^\varepsilon-1)^2}$ |


- **Readable Version:** - kRR variance depends on domain size d - OUE and OLH have the same variance, independent of d
- **Source:** LDP_Freq_Est.pdf, Table 1, Page 737
- **Why it belongs:** This provides the key comparison between estimator accuracies.
- **Unicode equation:** `| Protocol | Variance | |----------|----------| | DE/kRR | $n \cdot \fracd-2+e^\varepsilon(e^\varepsilon-1)^2$ | | OUE | $n \cdot \frac4e^\varepsilon(e^\varepsilon-1)^2$ | | OLH | $n \cdot \frac4e^\varepsilon(e^\varepsilon-1)^2$ |`

## Equation 32 – When to Use Each Protocol

![Equation 32](images/eq32.svg)

- **Image file**: `images/eq32.svg`
- **Slide:** Comparison between Estimators
- **LaTeX:**

```latex
d < 3e^\varepsilon + 2 \Rightarrow \text{Use DE/kRR}
```
```latex
d > 3e^\varepsilon + 2 \Rightarrow \text{Use OUE or OLH}
```


- **Readable Version:** Use kRR when domain size d < 3e^ε + 2; otherwise use OUE or OLH.
- **Source:** LDP_Freq_Est.pdf, Section 5, Page 737
- **Why it belongs:** This provides practical guidance on protocol selection.
- **Unicode equation:** `d < 3e^\varepsilon + 2 \Rightarrow \textUse DE/kRR`

## Equation 33 – Overall Gain Summary Table

> **Note:** No SVG image was generated for this equation.
- **Slide:** Gain from Attacks
- **LaTeX:**

| Attack | kRR | OUE | OLH |
|--------|-----|-----|-----|
| RPA | $\beta(\frac{r}{d} - f_T)$ | $\beta(r - f_T)$ | $-\beta f_T$ |
| RIA | $\beta(1 - f_T)$ | $\beta(1 - f_T)$ | $\beta(1 - f_T)$ |
| MGA | $\beta(1-f_T) + \frac{\beta(d-r)}{e^\varepsilon-1}$ | $\beta(2r-f_T) + \frac{2\beta r}{e^\varepsilon-1}$ | $\beta(2r-f_T) + \frac{2\beta r}{e^\varepsilon-1}$ |

where $\beta = \frac{m}{n+m}$


- **Readable Version:** MGA achieves the largest gain; β represents the fraction of fake users among all users.
- **Source:** attacks.pdf, Table 1, Page 7
- **Why it belongs:** This summarizes the attack effectiveness for all protocol-attack combinations.
- **Unicode equation:** `| Attack | kRR | OUE | OLH | |--------|-----|-----|-----| | RPA | $\beta(\fracrd - f_T)$ | $\beta(r - f_T)$ | $-\beta f_T$ | | RIA | $\beta(1 - f_T)$ | $\beta(1 - f_T)$ | $\beta(1 - f_T)$ | | MGA | $\beta(1-f_T) + \frac\beta(d-r)e^\varepsilon-1$ | $\beta(2r-f_T) + \frac2\beta re^\varepsilon-1$ | $\beta(2r-f_T) + \frac2\beta re^\varepsilon-1$ | where $\beta = \fracmn+m$`

## Equation 34 – Security-Privacy Tradeoff

![Equation 34](images/eq34.svg)

- **Image file**: `images/eq34.svg`
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

```latex
\text{Frequency Gain} \propto \frac{1}{e^\varepsilon - 1}
```


- **Readable Version:** As ε decreases (stronger privacy), the frequency gain from attacks increases (weaker security).
- **Source:** attacks.pdf, Section 3.6, Page 7
- **Why it belongs:** This demonstrates the fundamental security-privacy tradeoff.
- **Unicode equation:** `\textFrequency Gain \propto \frac1e^\varepsilon - 1`

## Equation 35 – Standard Deviation of Estimation

> **Note:** No SVG image was generated for this equation.
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

| Protocol | Standard Deviation |
|----------|-------------------|
| kRR | $\frac{r\sqrt{d-2+e^\varepsilon}}{(e^\varepsilon-1)\sqrt{n}}$ |
| OUE | $\frac{2re^{\varepsilon/2}}{(e^\varepsilon-1)\sqrt{n}}$ |
| OLH | $\frac{2re^{\varepsilon/2}}{(e^\varepsilon-1)\sqrt{n}}$ |


- **Readable Version:** The standard deviation of estimation decreases with √n, showing attacks are significant compared to natural noise.
- **Source:** attacks.pdf, Table 1, Page 7
- **Why it belongs:** This shows that attack gains are much larger than estimation noise.
- **Unicode equation:** `| Protocol | Standard Deviation | |----------|-------------------| | kRR | $\fracr\sqrtd-2+e^\varepsilon(e^\varepsilon-1)\sqrtn$ | | OUE | $\frac2re^\varepsilon/2(e^\varepsilon-1)\sqrtn$ | | OLH | $\frac2re^\varepsilon/2(e^\varepsilon-1)\sqrtn$ |`

## Equation 36 – RAPPOR Permanent Randomized Response

![Equation 36](images/eq36.svg)

- **Image file**: `images/eq36.svg`
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

```latex
B_i' = \begin{cases} 1, & \text{with probability } \frac{1}{2}f \\ 0, & \text{with probability } \frac{1}{2}f \\ B_i, & \text{with probability } 1-f \end{cases}
```


- **Readable Version:** Each bit is set to 1 with probability f/2, to 0 with probability f/2, or kept unchanged with probability 1-f.
- **Source:** rapor.pdf, Section 2, Step 2, Page 4
- **Why it belongs:** This is the memoization step that provides longitudinal privacy in RAPPOR.
- **Unicode equation:** `B_i' = \begincases 1, & \textwith probability \frac12f 0, & \textwith probability \frac12f B_i, & \textwith probability 1-f \endcases`

## Equation 37 – RAPPOR Differential Privacy Guarantee

![Equation 37](images/eq37.svg)

- **Image file**: `images/eq37.svg`
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

```latex
\varepsilon_\infty = 2h \ln\left(\frac{1 - \frac{1}{2}f}{\frac{1}{2}f}\right)
```


- **Readable Version:** The infinite-collection privacy guarantee equals 2h times ln((1-f/2)/(f/2)), where h is the number of hash functions.
- **Source:** rapor.pdf, Section 3.1, Theorem 1, Page 5
- **Why it belongs:** This shows RAPPOR's privacy guarantee for longitudinal data collection.
- **Unicode equation:** `\varepsilon_\infty = 2h \ln\left(\frac1 - \frac12f\frac12f\right)`

## Equation 38 – RAPPOR Instantaneous Response Probabilities

![Equation 38](images/eq38.svg)

- **Image file**: `images/eq38.svg`
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

```latex
q^* = P(S_i = 1 | b_i = 1) = \frac{1}{2}f(p+q) + (1-f)q
```
```latex
p^* = P(S_i = 1 | b_i = 0) = \frac{1}{2}f(p+q) + (1-f)p
```


- **Readable Version:** The probability of observing 1 depends on both the permanent response and instantaneous randomization parameters.
- **Source:** rapor.pdf, Section 3.2, Lemma 1, Page 6
- **Why it belongs:** This defines the combined effect of RAPPOR's two-stage randomization.
- **Unicode equation:** `q^* = P(S_i = 1 | b_i = 1) = \frac12f(p+q) + (1-f)q`

## Equation 39 – RAPPOR Frequency Estimation

![Equation 39](images/eq39.svg)

- **Image file**: `images/eq39.svg`
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

```latex
t_{ij} = \frac{c_{ij} - (p + \frac{1}{2}fq - \frac{1}{2}fp)N_j}{(1-f)(q-p)}
```


- **Readable Version:** The estimated count for bit i in cohort j is calculated by adjusting the observed count for randomization effects.
- **Source:** rapor.pdf, Section 4, Page 6
- **Why it belongs:** This shows how RAPPOR aggregates and decodes noisy reports.
- **Unicode equation:** `t_ij = \fracc_ij - (p + \frac12fq - \frac12fp)N_j(1-f)(q-p)`

## Equation 40 – Framework Variance Formula

![Equation 40](images/eq40.svg)

- **Image file**: `images/eq40.svg`
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

```latex
\text{Var}[\tilde{c}(i)] = \frac{nq^*(1-q^*)}{(p^*-q^*)^2} + \frac{nf_i(1-p^*-q^*)}{p^*-q^*}
```


- **Readable Version:** The variance has two terms: one depending on q* and one depending on the true frequency f_i.
- **Source:** LDP_Freq_Est.pdf, Section 3, Equation (2), Page 733
- **Why it belongs:** This is the general variance formula for pure LDP protocols.
- **Unicode equation:** `\textVar[\tildec(i)] = \fracnq^*(1-q^*)(p^*-q^*)^2 + \fracnf_i(1-p^*-q^*)p^*-q^*`

## Equation 41 – Approximate Variance (for infrequent values)

![Equation 41](images/eq41.svg)

- **Image file**: `images/eq41.svg`
- **Slide:** Impacts of Parameters on Attacks
- **LaTeX:**

```latex
\text{Var}^*[\tilde{c}(i)] = \frac{nq^*(1-q^*)}{(p^*-q^*)^2}
```


- **Readable Version:** When f_i is small, the variance is dominated by the first term only.
- **Source:** LDP_Freq_Est.pdf, Section 3, Equation (4), Page 733
- **Why it belongs:** This simplification is key for comparing protocol accuracies.
- **Unicode equation:** `\textVar^*[\tildec(i)] = \fracnq^*(1-q^*)(p^*-q^*)^2`

