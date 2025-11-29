# RAPPOR: Equations to Include in Slide

## 1. Permanent Randomized Response (Memoized Noise)

Client maintains a **memoized** noisy Bloom-filter bit \(B'_i\) for each Bloom-filter bit \(B_i\):

\[
B'_i =
\begin{cases}
1 & \text{with prob } \tfrac{1}{2}f \\
0 & \text{with prob } \tfrac{1}{2}f \\
B_i & \text{with prob } 1 - f
\end{cases}
\]

**Meaning / why it’s useful**

- This is the **core RAPPOR mechanism**: instead of using the true bit \(B_i\), the client stores a permanently randomized bit \(B'_i\).
- Parameter \(f\) controls **longitudinal privacy**: larger \(f\) → more randomization → stronger privacy but less utility.
- It distinguishes RAPPOR from kRR/OUE/OLH by showing that RAPPOR randomizes **once and reuses** the noisy value.

On the slide, you can annotate:

- \(f\): noise level for long-term privacy  
- \(B_i\): true Bloom-filter bit  
- \(B'_i\): permanently randomized bit (memoized on client)


## 2. Instantaneous Randomized Response (Per-Report Noise)

For each report, the client sends another noisy bit \(S_i\), based on \(B'_i\):

\[
P(S_i = 1) =
\begin{cases}
q & \text{if } B'_i = 1 \\
p & \text{if } B'_i = 0
\end{cases}
\]

**Meaning / why it’s useful**

- Shows the **second layer of randomization**: even the memoized noisy bit is not sent directly.
- Parameters \(p\) and \(q\) give a similar structure to kRR/OUE (probability of reporting 1 given the underlying bit).
- Highlights **short-term privacy / linkability** control via \(p, q\), in addition to \(f\) for long-term privacy.

On the slide, you can annotate:

- \(p\): probability of reporting 1 when \(B'_i = 0\)  
- \(q\): probability of reporting 1 when \(B'_i = 1\)  
- \(S_i\): reported bit after both randomization steps


## 3. Bit-Level Unbiased Estimator (Server-Side Reconstruction)

For cohort \(j\) and bit \(i\):

- \(c_{ij}\): number of received reports with \(S_i = 1\)  
- \(N_j\): number of users in cohort \(j\)

Then the estimator of the **true** number of times that bit was set in the original Bloom filters is

\[
t_{ij} =
\frac{
  c_{ij} - \bigl(p + \tfrac{1}{2} f q - \tfrac{1}{2} f p\bigr)\,N_j
}{
  (1 - f)\,(q - p)
}.
\]

**Meaning / why it’s useful**

- This is the RAPPOR analogue of the unbiased estimators you show for kRR, OUE, OLH.
- Conceptually:  
  - Subtract the expected number of 1s due purely to randomization.  
  - Divide by the effective signal \((1 - f)(q - p)\) to debias the result.
- It connects RAPPOR back to the main theme of your talk: **estimating true frequencies from locally privatized reports**.

On the slide, you can summarize verbally:

> “Given noisy bits \(S_i\) and parameters \(f, p, q\), the server uses this estimator to debias counts before decoding string frequencies.”


## 4. Optional: Longitudinal Privacy Parameter \(\varepsilon_\infty\)

If you have room and want one compact DP expression, you can include the longitudinal privacy guarantee for the permanent response (with \(h\) hash functions):

\[
\varepsilon_\infty
  = 2h \ln \frac{1 - \tfrac{1}{2}f}{\tfrac{1}{2}f}.
\]

**Meaning / why it’s useful**

- Quantifies how **long-term \(\varepsilon\)-DP** depends on \(f\) and the number of hash functions \(h\).
- Makes the privacy–utility trade-off explicit:
  - Increasing \(f\) pushes the fraction inside the log closer to 1 ⇒ smaller \(\varepsilon_\infty\) ⇒ stronger privacy.
- Fits nicely if you already defined \(\varepsilon\)-DP earlier; here it’s the RAPPOR-specific formula.


## 5. Suggested Slide Layout

You can design your “RAPPOR” slide roughly as:

1. **Title**: “RAPPOR (Bloom-filter-based LDP with memoized RR)”  

2. **Left column – Client-side mechanism**
   - Permanent randomized response for \(B'_i\) (Equation 1)  
   - Instantaneous randomized response for \(S_i\) (Equation 2)

3. **Right column – Server-side & privacy**
   - Unbiased estimator \(t_{ij}\) (Equation 3) with one-line explanation: “Debiases aggregate counts before string decoding.”  
   - Optional \(\varepsilon_\infty\) formula (Equation 4) with note: “Controls longitudinal \(\varepsilon\)-DP via \(f\) and \(h\).”

This keeps your RAPPOR slide parallel to your other mechanism slides (kRR / OUE / OLH), while clearly showing what is unique about RAPPOR:  
- **Bloom filters**,  
- **two-stage randomization (memoized + per-report)**, and  
- **explicit longitudinal privacy control**.
