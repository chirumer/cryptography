# Equation Mapping for PPT Slides

This document maps each LaTeX equation to the relevant slide(s) in your presentation.

---

## 📊 Equation-to-Slide Mapping

### Introductory Concepts Section

#### **Slide: Differential Privacy**
- **Equation:** `01_differential_privacy_definition.tex`
- **Content:**
  ```
  Pr[M(x) ∈ S] ≤ e^ε Pr[M(y) ∈ S] + δ
  ```
- **Purpose:** Mathematical definition of (ε,δ)-differential privacy
- **When to use:** Use this when introducing the concept of differential privacy and explaining the privacy guarantees

---

#### **Slide: Local Differential Privacy**
- **Equation:** `02_local_differential_privacy_definition.tex`
- **Content:**
  ```
  ∀y ∈ Range(M): Pr[M(v₁) = y] ≤ e^ε Pr[M(v₂) = y]
  ```
- **Purpose:** Definition of ε-local differential privacy (LDP)
- **When to use:** Use this when explaining how LDP differs from centralized DP - emphasizing that privacy is guaranteed at the user level

---

#### **Slide: Pure Local Differential Privacy**
- **Equation:** `03_pure_ldp_protocol_properties.tex`
- **Content:**
  ```
  Pr[PE(v₁) ∈ {y | v₁ ∈ Support(y)}] = p*
  ∀v₂≠v₁ Pr[PE(v₂) ∈ {y | v₁ ∈ Support(y)}] = q*
  ```
- **Purpose:** Defines the mathematical properties of pure LDP protocols
- **When to use:** When explaining the probabilistic guarantees of pure LDP (constraint: p* > q*)

---

#### **Slide: Frequency Estimation Problem**
- **Equation:** `06_aggregation_formula.tex`
- **Content:**
  ```
  f̃ᵥ = (Σⱼ 𝕀_{Support(yʲ)}(v) - nq*) / (p* - q*)
  ```
- **Purpose:** General aggregation formula for frequency estimation in pure LDP protocols
- **When to use:** When explaining how the server aggregates perturbed values to estimate frequencies

---

#### **Slide: Attack – Problem Formulation**
- **Equation:** `04_attacker_optimization_objective.tex`
- **Content:**
  ```
  max_Y G(Y)
  ```
- **Purpose:** The optimization problem for the Maximal Gain Attack (MGA)
- **When to use:** When introducing the adversary's objective - maximizing gain by injecting fake users

---

### Frequency Estimation Techniques Section

#### **Slide: K Randomized Response**
- **Equation:** `05_krr_perturbation_probabilities.tex`
- **Content:**
  ```
  Pr[PE(v) = i] = {
    p = e^ε/(e^ε + d - 1),  if i=v
    q = (1-p)/(d-1),        otherwise
  }
  ```
- **Purpose:** Defines the perturbation probabilities for kRR protocol
- **When to use:** When explaining how kRR works - the true value is reported with probability p, false values with probability q

---

#### **Slide: Optimized Unary Encoding**
- **Equation:** `07_oue_perturbation_probabilities.tex`
- **Content:**
  ```
  Pr[PE(v) = i] = {
    p = 1/2,               if i=v
    q = 1/(e^ε + 1),      otherwise
  }
  ```
- **Purpose:** Defines the perturbation probabilities for OUE protocol
- **When to use:** When explaining OUE - highlight that variance is independent of domain size d (advantage over kRR)

---

#### **Slide: Optimized Local Hashing**
- **Equation:** `08_olh_perturbation_probabilities.tex`
- **Content:**
  ```
  ∀i∈[d] Pr[y = ⟨H,x⟩] = {
    p = e^ε/(e^ε + d - 1),  if x=i
    q = 1/(e^ε + d - 1),    otherwise
  }
  ```
- **Purpose:** Defines the perturbation probabilities for OLH protocol
- **When to use:** When explaining OLH - combines OUE's variance properties with reduced communication costs

---

### Evaluation Section

#### **Slide: Gain from Attacks** OR **Impacts of Parameters on Attacks**
- **Equation:** `09_security_privacy_tradeoff.tex`
- **Content:**
  ```
  G_MGA ∝ 1/(e^ε - 1)
  ```
- **Purpose:** Demonstrates the security-privacy tradeoff
- **When to use:** When showing the paradox that stronger privacy (lower ε) makes the system MORE vulnerable to poisoning attacks

---

## 📝 Usage Notes

### Essential Equations (Must Include):
1. **01** - Differential Privacy definition (foundational concept)
2. **02** - Local Differential Privacy definition (key distinction from DP)
3. **05** - kRR perturbation (first protocol)
4. **07** - OUE perturbation (improved protocol)
5. **08** - OLH perturbation (optimal protocol)
6. **09** - Security-privacy tradeoff (key finding)

### Optional Equations (Depending on Time):
- **03** - Pure LDP properties (if you have time to explain the general framework)
- **04** - Attack optimization (if explaining attack methodology in detail)
- **06** - Aggregation formula (if showing how estimation actually works)

---

## 🎯 Recommended Presentation Flow

1. **Introduction slides:** Use equations 01, 02 to define DP and LDP
2. **Frequency Estimation:** Use equation 06 if explaining the estimation process in detail
3. **Protocol slides:** Use equations 05, 07, 08 for kRR, OUE, and OLH respectively
4. **Attack slides:** Use equation 04 if explaining the attack formulation
5. **Evaluation slides:** Use equation 09 to show the security-privacy paradox

---

## 🚀 Quick Start

To convert selected equations to SVG images:

```bash
# Copy desired equations to the equations folder
cp potential_equations/01_differential_privacy_definition.tex equations/
cp potential_equations/02_local_differential_privacy_definition.tex equations/
# ... etc

# Convert to SVG
python latex_to_svg.py
```

Or convert all equations at once:
```bash
cp potential_equations/*.tex equations/
python latex_to_svg.py
```

The SVG images will be generated in the `images/` folder.

---

## 🔍 Additional Equations Analysis

After careful analysis of all source files, I identified **12 additional equations** that could significantly enhance your presentation. These equations are organized by category and mapped to specific slides below.

### 📊 Recommended Additional Equations (Organized by Slide)

---

#### **Slide: Comparison between Estimators** (NEW)

**ESSENTIAL - Variance Formulas (3 equations):**

These equations are **critical** for explaining why OUE/OLH dominate kRR:

**10. kRR Variance Formula**
- **LaTeX:** `n\cdot\frac{d-2+e^\epsilon}{(e^\epsilon-1)^2}`
- **Displays as:** Var(kRR) = n · (d-2+e^ε)/(e^ε-1)²
- **Purpose:** Shows kRR variance scales **linearly with domain size d** - catastrophic for large domains
- **Why include:** Demonstrates fundamental limitation of kRR

**11. OUE Variance Formula**
- **LaTeX:** `n \cdot \frac{4e^\epsilon}{(e^\epsilon-1)^2}`
- **Displays as:** Var(OUE) = n · 4e^ε/(e^ε-1)²
- **Purpose:** Proves variance is **independent of domain size d**
- **Why include:** Shows key breakthrough - OUE decouples from domain size

**12. OLH Variance Formula**
- **LaTeX:** `n \cdot \frac{4e^\epsilon}{(e^\epsilon-1)^2}`
- **Displays as:** Var(OLH) = n · 4e^ε/(e^ε-1)²
- **Purpose:** Same optimal variance as OUE with reduced communication
- **Why include:** Proves OLH achieves theoretical optimality

---

#### **Slides: Attacking kRR, Attacking OUE, Attacking OLH**

**ESSENTIAL - Attack Gain Formulas (3 equations):**

These show **exactly how much damage** each attack causes:

**13. kRR MGA Gain Formula**
- **LaTeX:** `\beta(1-f_T) + \frac{\beta(d-r)}{e^\epsilon-1}`
- **Displays as:** G(kRR) = β(1-f_T) + β(d-r)/(e^ε-1)
- **Purpose:** Attack gain with explicit **domain-scaling term** β(d-r)
- **Why include:** Mathematically proves kRR is catastrophically vulnerable for large d
- **Use on:** "Attacking kRR" slide

**14. OUE MGA Gain Formula**
- **LaTeX:** `\beta(2r-f_T) + \frac{2\beta r}{e^\epsilon-1}`
- **Displays as:** G(OUE) = β(2r-f_T) + 2βr/(e^ε-1)
- **Purpose:** Attack gain **independent of d**, only scales with number of targets r
- **Why include:** Shows improved security vs kRR
- **Use on:** "Attacking OUE" slide

**15. OLH MGA Gain Formula**
- **LaTeX:** `\beta(2r-f_T) + \frac{2\beta r}{e^\epsilon-1}`
- **Displays as:** G(OLH) = β(2r-f_T) + 2βr/(e^ε-1)
- **Purpose:** Same attack resistance as OUE
- **Why include:** Proves OLH maintains OUE's security properties
- **Use on:** "Attacking OLH" slide

---

#### **Slide: Comparison between Estimators** (Communication Costs)

**ESSENTIAL - Communication Complexity (2 equations):**

**16. OUE Communication Cost** ⚠️
- **LaTeX:** `O(d)`
- **Displays as:** O(d)
- **Purpose:** Shows **prohibitive linear communication** cost in domain size
- **Why include:** Explains why OUE is impractical despite optimal variance
- **Impact:** Critical limitation

**17. OLH Communication Cost** ✅
- **LaTeX:** `O(\log n)`
- **Displays as:** O(log n)
- **Purpose:** **Exponentially better** than OUE's O(d)
- **Why include:** This is why OLH is the winner - optimal variance + practical communication
- **Impact:** THE key result

**OPTIONAL:**
**18. kRR Communication Cost**
- **LaTeX:** `O(\log d)`
- **Displays as:** O(log d)
- **Purpose:** Lowest communication overhead
- **Why include:** Completeness (but less critical)

---

#### **Slide: Attack – Problem Formulation** (OPTIONAL)

**Definition Equations (helpful for clarity):**

**19. Fake User Fraction**
- **LaTeX:** `\beta = \frac{m}{n+m}`
- **Displays as:** β = m/(n+m)
- **Purpose:** Defines attacker strength (m fake users out of n+m total)
- **Why include:** Clarifies the threat model parameter

**20. Target Set Frequency**
- **LaTeX:** `f_T = \sum_{t \in T} f_t`
- **Displays as:** f_T = Σ_{t∈T} f_t
- **Purpose:** Sum of true frequencies for all target items
- **Why include:** Defines notation used in attack gain formulas

---

### 📋 Summary: What to Add

#### **MUST ADD (8 equations) - Tell the Complete Story:**

| Priority | Equations | Slide Location | Why Critical |
|----------|-----------|----------------|--------------|
| 🔴 HIGH | 10-12 (Variance) | Comparison between Estimators | Proves OUE/OLH superiority in utility |
| 🔴 HIGH | 13-15 (Attack Gain) | Attacking kRR/OUE/OLH | Proves OUE/OLH superiority in security |
| 🔴 HIGH | 16-17 (Communication) | Comparison between Estimators | Proves OLH is practical (OUE is not) |

#### **OPTIONAL (4 equations) - Nice to Have:**

| Priority | Equations | Slide Location | Purpose |
|----------|-----------|----------------|---------|
| 🟡 MEDIUM | 18 (kRR Comm) | Comparison | Completeness |
| 🟡 MEDIUM | 19-20 (Definitions) | Attack Formulation | Clarity |

---

### 🎯 Recommended Extended Presentation Flow

**Updated flow incorporating new equations:**

1. **Introduction slides:** Use equations 01, 02 (DP, LDP definitions)
2. **Pure LDP slide:** Use equation 03 (p*, q* properties)
3. **Protocol slides:** Use equations 05, 07, 08 (kRR, OUE, OLH perturbation)
4. **Attack formulation:** Use equation 04 (optimization), optionally 19-20 (definitions)
5. **Attacking protocol slides:** Use equations 13, 14, 15 (specific attack gains)
6. **Comparison slide:** Use equations 10-12 (variance), 16-17 (communication) - **THIS IS KEY**
7. **Evaluation slides:** Use equation 09 (security-privacy paradox)

---

### 💡 Key Insight

The **12 additional equations** complete the narrative:

**The Full Story:**
- **Equations 10-12** show OUE/OLH have domain-independent variance (utility win)
- **Equations 13-15** show OUE/OLH resist domain-scaling attacks (security win)
- **Equations 16-17** show OLH has practical communication while OUE doesn't (practicality win)
- **Together:** OLH dominates across all three dimensions: utility, security, and practicality

This is the complete mathematical proof that **OLH is the optimal protocol**.
