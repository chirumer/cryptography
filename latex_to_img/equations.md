# Equations for Frequency Estimation with Local Differential Privacy and Attacks

This README suggests equations from your basis papers:

- `attacks.pdf`
- `LDP_Freq_Est.pdf`
- `rapor.pdf`

Each entry lists:
1. The LaTeX equation  
2. Which paper it is taken from  
3. Why it is relevant  
4. Which slide in `slides.pdf` it fits best

---

## 1. Global Differential Privacy

**Slide:** 4 – *Differential Privacy*  
**Paper:** LDP_Freq_Est.pdf

**Equation (central DP):**

\[
\forall t \in \mathrm{Range}(A):\quad 
\Pr[A(D) = t] \le e^{\varepsilon}\,\Pr[A(D') = t].
\]

**Why relevant:**  
Provides the standard (central) DP guarantee, which your LDP definitions and protocols generalize. Good to set the stage before moving to the local model.

---

## 2. Local Differential Privacy

**Slide:** 5 – *Local Differential Privacy*  
**Paper:** LDP_Freq_Est.pdf

**Equation (ε-LDP):**

\[
\forall y \in \mathrm{Range}(A):\quad
\Pr[A(v_1) = y] \le e^{\varepsilon}\,\Pr[A(v_2) = y].
\]

**Why relevant:**  
Formalizes the local model: the randomizer \(A\) runs on the client’s input \(v\). This is the core definition all your protocols (kRR, OUE, OLH, RAPPOR) must satisfy.

---

## 3. Pure Local Differential Privacy Protocol

**Slide:** 7 – *Pure Local Differential Privacy*  
**Paper:** LDP_Freq_Est.pdf

**Equations (pure protocol conditions):**

\[
\Pr\!\big[\mathrm{PE}(v_1) \in \{y \mid v_1 \in \mathrm{Support}(y)\}\big] = p^*,
\]

\[
\Pr\!\big[\mathrm{PE}(v_2) \in \{y \mid v_1 \in \mathrm{Support}(y)\}\big] = q^*,
\quad 0 < q^* < p^* < 1,
\]

LDP constraint:

\[
\frac{p^*}{q^*} \le e^{\varepsilon}.
\]

**Why relevant:**  
Defines “pure” LDP protocols via two parameters \(p^*, q^*\). This abstraction unifies kRR, OUE, and OLH and is later used to derive estimators and variances.

---

## 4. Generic Pure LDP Frequency Estimator

**Slide:** 6 – *Frequency Estimation Problem*  
**Paper:** LDP_Freq_Est.pdf

**Equation (unbiased estimator for count of item \(i\)):**

\[
\tilde{c}(i)
= \frac{
      \displaystyle \sum_j \mathbf{1}_{\mathrm{Support}(y_j)}(i) - n q^*
   }{
      p^* - q^*
   }.
\]

Often you then use \(\hat{f}_i = \tilde{c}(i)/n\) as the frequency estimator.

**Why relevant:**  
This is the unified estimator used for all pure LDP protocols. It clearly shows how the server decodes noisy reports using \(p^*, q^*\) and the support function.

---

## 5. Variance of Pure LDP Estimator

**Slide:** 19 – *Comparison between Estimators*  
**Paper:** LDP_Freq_Est.pdf

**Equation (variance and approximation for small \(f_i\)):**

Full variance:
\[
\mathrm{Var}[\tilde{c}(i)] 
= \frac{n q^*(1 - q^*)}{(p^* - q^*)^2}
  + \frac{n f_i \bigl(1 - p^* - q^*\bigr)}{p^* - q^*}.
\]

Approximation for rare items (\(f_i\) small):
\[
\mathrm{Var}^*[\tilde{c}(i)]
= \frac{n q^*(1 - q^*)}{(p^* - q^*)^2}.
\]

**Why relevant:**  
Describes accuracy of any pure LDP protocol in a compact form. By plugging in protocol-specific \(p^*, q^*\), you obtain the variances used to compare kRR, OUE, and OLH.

---

## 6. k-ary Randomized Response (kRR) Mechanism

**Slide:** 10 – *K Randomized Response*  
**Paper:** attacks.pdf

**Equation (perturbation rule):**

\[
\Pr(y = a) =
\begin{cases}
\displaystyle \frac{e^{\varepsilon}}{d - 1 + e^{\varepsilon}}, & a = v,\\[0.5em]
\displaystyle \frac{1}{d - 1 + e^{\varepsilon}}, & a \ne v.
\end{cases}
\]

**Why relevant:**  
The basic LDP mechanism used as a baseline. It shows how ε biases the output toward the true value vs. other domain elements, and serves as a reference for both accuracy and vulnerability.

---

## 7. Optimized Unary Encoding (OUE) Parameters and Variance

**Slide:** 11 – *Optimized Unary Encoding*  
**Paper:** LDP_Freq_Est.pdf

**Equations (optimized parameters):**

\[
q = \frac{1}{e^{\varepsilon} + 1},\qquad
p = \frac{1}{2}.
\]

Plugging these into the approximate variance formula yields:

\[
\mathrm{Var}^*[\tilde{c}_{\mathrm{OUE}}(i)]
= n \cdot \frac{4 e^{\varepsilon}}{(e^{\varepsilon} - 1)^2}.
\]

**Why relevant:**  
Shows how OUE is derived by choosing \(p,q\) that minimize variance. This variance is later compared to OLH and to other protocols.

---

## 8. Optimized Local Hashing (OLH): Parameters & Variance

**Slide:** 12 – *Optimized Local Hashing*  
**Paper:** LDP_Freq_Est.pdf

**Equations (LH perturbation, optimal g, and resulting parameters):**

Local Hashing:
\[
\Pr[y = i] =
\begin{cases}
\displaystyle p = \frac{e^{\varepsilon}}{e^{\varepsilon} + g - 1}, & x = i,\\[0.5em]
\displaystyle q = \frac{1}{e^{\varepsilon} + g - 1}, & x \ne i.
\end{cases}
\]

For OLH, optimal hash range size:
\[
g = e^{\varepsilon} + 1,
\]

which simplifies to:
\[
p^* = \frac{1}{2},\qquad
q^* = \frac{1}{e^{\varepsilon} + 1}.
\]

Approximate variance:
\[
\mathrm{Var}^*[\tilde{c}_{\mathrm{OLH}}(i)]
= n \cdot \frac{4 e^{\varepsilon}}{(e^{\varepsilon} - 1)^2}.
\]

**Why relevant:**  
Defines OLH and shows it has the same asymptotic variance as OUE. This is central to your “unified view” and to the comparison slide.

---

## 9. Expectation of Support Indicator in Pure LDP

**Slide:** 8 – *Attack – Problem Formulation*  
**Paper:** attacks.pdf

**Equation (expected support sum for item \(v\)):**

\[
\sum_{i=1}^{n} \mathbb{E}\big[\mathbf{1}_{S(y_i)}(v)\big]
= n \bigl(f_v (p - q) + q\bigr).
\]

**Why relevant:**  
Connects true frequency \(f_v\) to the expected number of outputs supporting \(v\). In attacks, you manipulate this expectation by injecting fake users.

---

## 10. Frequency Gain of an Attack on a Target Item

**Slides:** 8 – *Attack – Problem Formulation*; 20 – *Gain from Attacks*  
**Paper:** attacks.pdf

**Equation (frequency gain for target item \(t\)):**

\[
\Delta \tilde{f}_t
= 
\frac{1}{n+m}
\sum_{i=1}^{n+m}
\frac{\mathbf{1}_{S(y_i)}(t) - q}{p - q}
\;-\;
\frac{1}{n}
\sum_{i=1}^{n}
\frac{\mathbf{1}_{S(y_i)}(t) - q}{p - q}.
\]

**Why relevant:**  
Formalizes the attack’s objective: how much the estimated frequency of a target changes due to injected fake users. This directly corresponds to the “gain” curves in your evaluation.

---

## 11. Overall Gain for a Set of Targets

**Slide:** 20 – *Gain from Attacks*  
**Paper:** attacks.pdf

**Equation (overall expected gain for target set \(T\)):**

\[
G 
= \frac{
       \displaystyle \sum_{i=n+1}^{n+m} \sum_{t \in T} 
       \mathbb{E}\big[\mathbf{1}_{S(y_i)}(t)\big]
     }{
       (n + m)(p - q)
     }
     - c,
\]

where \(c\) is a constant depending on the original users and true frequencies (baseline term).

**Why relevant:**  
Aggregates the per-target gains into a single score, highlighting how protocol parameters affect susceptibility to poisoning.

---

## 12. Basic One-time RAPPOR Estimator

**Slides:** 6 – *Frequency Estimation Problem* or 9 – *Frequency Estimation Techniques*  
**Paper:** rapor.pdf

**Equations (expected count and estimator for bit \(i\)):**

\[
\mathbb{E}[C_i] = q T_i + p (N - T_i),
\]

\[
\hat{T}_i = \frac{C_i - pN}{q - p}.
\]

**Why relevant:**  
Canonical decoding for Basic One-time RAPPOR. It mirrors the generic pure-LDP estimator: subtract expected noise and rescale by \(p,q\).

---

## 13. Variance of Basic RAPPOR Estimator

**Slides:** 18 – *Evaluation* or 19 – *Comparison between Estimators*  
**Paper:** rapor.pdf

**Equation (variance when \(T_i = 0\)):**

\[
\mathrm{Var}(\hat{T}_i)
= \frac{p(1 - p)N}{(q - p)^2}.
\]

**Why relevant:**  
Gives a closed-form variance in terms of RAPPOR’s parameters. Useful for qualitatively comparing traditional RAPPOR to newer pure-LDP protocols.

---

## 14. Local Hashing (LH/OLH) Privacy Guarantee

**Slides:** 5 – *Local Differential Privacy* or 12 – *Optimized Local Hashing*  
**Paper:** LDP_Freq_Est.pdf

**Equation (privacy ratio bound):**

\[
\frac{\Pr[\langle H,y\rangle \mid v_1]}{\Pr[\langle H,y\rangle \mid v_2]}
= \frac{\Pr[\mathrm{Perturb}(H(v_1)) = y]}{\Pr[\mathrm{Perturb}(H(v_2)) = y]}
\le \frac{p}{q} = e^{\varepsilon}.
\]

**Why relevant:**  
Concrete example showing how a non-trivial encoding (hashing) still satisfies ε-LDP by bounding likelihood ratios.

---

# Additional Suggested Equations & New Slide Ideas

This section proposes extra equations not already covered above, plus possible slide titles.

---

## Extra 1 – RAPPOR Permanent Randomized Response Privacy

**Suggested slide title:** *Translating RAPPOR Parameters to ε*  
**Paper:** rapor.pdf

**Equation (long-term ε):**

\[
\varepsilon_{\infty}
= 2h \,\ln\!\left(
  \frac{1 - \tfrac{1}{2}f}{\tfrac{1}{2} f}
\right).
\]

**Why relevant:**  
Connects engineering parameters (number of hash functions \(h\) and flipping probability \(f\)) to a formal ε guarantee for long-term privacy.

---

## Extra 2 – RAPPOR Instantaneous Randomized Response Privacy

**Suggested slide title:** *Longitudinal vs One-time Privacy in RAPPOR*  
**Paper:** rapor.pdf

**Equations:**

\[
\varepsilon_{1}
= h \log\!\left(
    \frac{q^*(1 - p^*)}{p^*(1 - q^*)}
  \right),
\]

where
\[
q^* = \Pr(S_i = 1 \mid b_i = 1),
\quad
p^* = \Pr(S_i = 1 \mid b_i = 0).
\]

**Why relevant:**  
Separates instantaneous ε from longitudinal ε; useful if you want to highlight repeated reporting vs. one-time reports.

---

## Extra 3 – Security Threshold for kRR vs OUE/OLH

**Suggested slide title:** *When Are OUE and OLH More Secure than kRR?*  
**Paper:** attacks.pdf

**Equation (threshold on domain size \(d\)):**

\[
d > (2r - 1)\bigl(e^{\varepsilon} - 1\bigr) + 3r.
\]

**Why relevant:**  
Provides a simple analytic condition under which OUE and OLH are more robust to attacks than kRR, in terms of domain size \(d\), number of targets \(r\), and privacy budget \(\varepsilon\). Great for a theory-focused or backup slide.

---

*End of README.*
