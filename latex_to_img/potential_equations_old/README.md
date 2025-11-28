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
cp 01_differential_privacy_definition.tex ../equations/
cp 02_local_differential_privacy_definition.tex ../equations/
# ... etc

# Convert to SVG
python ../latex_to_svg.py
```

Or convert all equations at once:
```bash
cp *.tex ../equations/
python ../latex_to_svg.py
```

The SVG images will be generated in the `images/` folder.
