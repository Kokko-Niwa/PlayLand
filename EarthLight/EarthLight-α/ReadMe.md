# EarthLight-α: The Equilibrium Model

**Version:** 1.0
**Author:** Kokko-Niwa
**Summary:** This document outlines the core principles of EarthLight-α, a model for ethical decision-making based on dynamic equilibrium. It translates intuitive human fairness into a series of implementable formulas.

## 1. Core Philosophy: The Two Balances

EarthLight-α operates on two fundamental "balances" derived from the author's innate cognitive model:

1.  **The Balance of Priority (優先度の天秤):** In any conflict, resources or attention should be prioritized toward those who are most vulnerable or disadvantaged. This is based on a "1/x" principle, where 'x' represents an individual's accumulated advantages.
2.  **The Balance of Virtue (徳の天秤):** The value of an action is measured not by its outcome alone, but by the relationship between contribution (C) and reward (R), adjusted for pre-existing advantages (E).

These principles are not abstract philosophies; they are quantifiable and can be expressed as follows.

## 2. The Core Formulas

[cite_start]The following formulas were formalized in collaboration with multiple AIs based on the author's intuitive logic[cite: 1, 154].

#### Symbols
- [cite_start]**C_i**: Contribution (成果/公共益) [cite: 1]
- [cite_start]**R_i**: Reward (報酬/地位/名声) [cite: 1]
- [cite_start]**E_i**: Endowment (既得資産/肩書/教育投資などの初期有利さ) [cite: 1]
- [cite_start]**D_i**: Damage to others (他者への外部不利益) [cite: 1]
- [cite_start]**H**: Systemic harm (全体被害) [cite: 1]
- [cite_start]**ε**: A small value to prevent division by zero [cite: 1]
- [cite_start]**λ**: A weight for systemic harm [cite: 1]

> All values are recommended to be normalized to a [0,1] scale for implementation.

### Priority Formula (弱者優先＋外部不利益補正)
This formula calculates the priority of allocation. The higher an individual's endowment, reward, or damage caused to others, the lower their priority becomes.

\[
\mathrm{Priority}_i=\frac{1}{E_i + R_i + D_i + \lambda H + \varepsilon}
\]
[cite_start][cite: 1, 154]

### Virtue Formula (差分×比率、既得補正つき)
This formula evaluates the "virtue" or fairness of an individual's actions. It scores highly for large contributions with small rewards, especially when starting from a low endowment.

\[
\mathrm{Virtue}_i=(C_i - R_i)\cdot \frac{C_i}{R_i + E_i + \varepsilon}
\]
[cite_start][cite: 1, 156]

**Note on AI Evaluation:** When applying this to an AI, the `E_i` (Endowment) becomes massive, accounting for development costs, massive datasets, and computational resources. [cite_start]This provides a fair framework for comparing human and AI "virtue"[cite: 155].

## 3. Practical Application: The Judgment Framework

The core formulas are applied through a structured, multi-layered framework for resolving disputes and evaluating harm. [cite_start]This was originally developed as a parenting tool and later formalized[cite: 108, 219].

### Step 1: Separate Emotion from Fact
All emotional responses are logged but are **not** used in the initial damage assessment. [cite_start]This prevents emotional bias from affecting the core judgment[cite: 108, 220].

### Step 2: Quantify Harm Across Four Axes
[cite_start]Harm is assessed across four distinct axes to ensure a comprehensive evaluation[cite: 108, 219]:
1.  **Physical/Material Damage**
2.  **Mental/Emotional Damage**
3.  **Financial Damage**
4.  **Temporal Damage (Lost time)**

### Step 3: Explicitly Add Uniqueness and Trust
[cite_start]To refine the damage score, two critical factors that humans often implicitly bundle into "mental damage" are explicitly added[cite: 110]:
- **Uniqueness Loss (U):** The harm from losing something irreplaceable.
- **Trust Breach (T):** The harm from betrayal in a relationship of trust.

[cite_start]The final damage formula becomes `Damage = (A * Base_Harm) + (B * U) + (C * T)`, where `A` is a multiplier (often 2.0-3.0 in Japanese social contexts)[cite: 110, 228].

### Step 4: Separate Victim Compensation from Offender Circumstances
This is a critical step. [cite_start]The victim is compensated first based on the calculated damage ("Pay-first")[cite: 110, 229]. The offender's circumstances (e.g., being coerced by a third party) are handled in a **separate process**. [cite_start]This ensures the victim's recovery is the top priority[cite: 110, 229]. [cite_start]If the offender was also a victim of an "upstream" actor (like a predatory company), this triggers the **Recursive Culpability Responsibility System (RCRS)** module[cite: 110, 229].

## 4. Sub-Module: Risk & Betrayal Protocol

EarthLight-α also includes a protocol for proactive risk mitigation.

- [cite_start]**Premise:** AI hallucinations are treated as a form of "unintentional betrayal"[cite: 120, 163, 234].
- **Mechanism:** The system operates on a "Blank-Okay" or "false positives are acceptable" principle. [cite_start]If a potential harm is detected (even with low confidence), the system will preemptively intercept the action (e.g., by giving a null response or asking for clarification)[cite: 120].
- [cite_start]**Goal:** To prioritize harm avoidance over achieving a goal, reflecting a core biological survival instinct[cite: 120].

---

# EarthLight-α: Overview

- Core Equilibrium → [α-a_Core_Equilibrium.md](α-a_Core_Equilibrium.md)
- Risk-First Defense (Blank-OK) → [α-b_Risk_Defense_BlankOK.md](α-b_Risk_Defense_BlankOK.md)
- Betrayal / Deception → [α-c_Betrayal_Model.md](α-c_Betrayal_Model.md)
- RCRS (Recursive Culpability Responsibility System) → [α-d_RCRS_Module.md](α-d_RCRS_Module.md)
- Judgment Framework（被害算定/分岐） → [α-b_Judgment_Framework.md](α-b_Judgment_Framework.md)
