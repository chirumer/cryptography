# Attack Gain Equations

This folder contains LaTeX equations for attack gains on Local Differential Privacy (LDP) protocols, extracted from sections 3.3, 3.4, and 3.5 of the attacks paper.

## Variables

- **n**: number of genuine users
- **m**: number of fake users (injected by attacker)
- **d**: domain size (number of items)
- **d'**: hash range for OLH (typically d' = e^ε + 1)
- **r**: number of target items
- **p, q**: perturbation probabilities (protocol-specific)
- **c**: constant term = m(fT(p-q)+rq)/((n+m)(p-q))
- **fT**: sum of true frequencies of target items

## Attack Types

- **RPA** (Random Perturbed-value Attack): Randomly selects perturbed values
- **RIA** (Random Item Attack): Randomly selects target items and perturbs them
- **MGA** (Maximal Gain Attack): Optimal attack that maximizes gain

---

## kRR (k-Randomized Response)

### RPA - Random Perturbed-value Attack
![kRR RPA Gain](../attack_gain_images/krr_rpa_gain.svg)

### RIA - Random Item Attack
![kRR RIA Gain](../attack_gain_images/krr_ria_gain.svg)

### MGA - Maximal Gain Attack
![kRR MGA Gain](../attack_gain_images/krr_mga_gain.svg)

---

## OUE (Optimized Unary Encoding)

### RPA - Random Perturbed-value Attack
![OUE RPA Gain](../attack_gain_images/oue_rpa_gain.svg)

### RIA - Random Item Attack
![OUE RIA Gain](../attack_gain_images/oue_ria_gain.svg)

### MGA - Maximal Gain Attack
![OUE MGA Gain](../attack_gain_images/oue_mga_gain.svg)

---

## OLH (Optimized Local Hashing)

### RPA - Random Perturbed-value Attack
![OLH RPA Gain](../attack_gain_images/olh_rpa_gain.svg)

### RIA - Random Item Attack
![OLH RIA Gain](../attack_gain_images/olh_ria_gain.svg)

### MGA - Maximal Gain Attack
![OLH MGA Gain](../attack_gain_images/olh_mga_gain.svg)

---

## Key Observations

1. **MGA achieves the largest gain** among all three attacks for each protocol
2. **RIA outperforms RPA** for kRR and OLH
3. **RPA outperforms RIA** for OUE
4. **Gain increases as privacy budget ε decreases** (security-privacy tradeoff)
5. **OUE RPA gain depends on r** (number of targets), not domain size d

## Source

Equations extracted from:
- **Paper**: Data Poisoning Attacks to Local Differential Privacy Protocols
- **Sections**: 3.3 (kRR), 3.4 (OUE), 3.5 (OLH)
