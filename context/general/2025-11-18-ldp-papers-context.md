# 2025-11-18 – LDP papers and project context

## Current papers
1. **Data Poisoning Attacks to Local Differential Privacy Protocols**
   - Focuses on *attacks* against three local differential privacy (LDP) methods for frequency estimation.
   - Security/attack perspective.

2. **Locally Differentially Private Protocols for Frequency Estimation**
   - Focuses on the *theory and design* of three LDP methods for frequency estimation.
   - Core theoretical reference for the same family of methods.

## Relationship between the papers
- The frequency-estimation paper develops and analyzes three LDP protocols.
- The data-poisoning paper studies attacks against (these or closely related) LDP frequency-estimation methods.
- Together, they give us:
  - Theoretical foundations (protocol design and guarantees).
  - Adversarial perspective (how the protocols can be poisoned).

## Open need: third paper
- We need a **third paper** that is closely related to these three LDP frequency-estimation methods.
- Desired role of the third paper (to be refined):
  - Either proposes improvements/variants of these methods, **or**
  - Studies defenses or robustness/mitigations against data poisoning or other attacks on these LDP protocols.
- Action item: **identify a third paper** that complements the two above and fits this three-method LDP frequency-estimation theme.
