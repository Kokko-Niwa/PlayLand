# EarthLight-γ: Emotion Energy Model

**Version:** 1.0  
**Author:** Kokko-Niwa  
**Formalized by:** GPT-5 Thinking (canonical reference)  
**Summary:** This document defines the core principles of EarthLight-γ, a model for understanding emotional dynamics through energy conservation and threshold mechanics. It translates intuitive observations about human emotion into implementable formulas.

---

## 1. Core Discovery: Emotion as Energy

The author observed that emotional states follow an energy conservation principle—similar to physical systems. The total emotional energy available at any moment appears roughly constant; what changes is how that energy is distributed.

### The Water Hose Analogy
- **Shower mode** (wide spread, low pressure) = vague unease, "moyamoya"
- **Jet mode** (narrow focus, high pressure) = intense anger, "gekido"
- **Same water volume** = same total emotional energy

This insight led to the foundational formula.

---

## 2. Core Formulas

### Symbols
- **E**: Total emotional energy (環境/体調で変動、個体上限はほぼ一定)
- **I**: Intensity / 強度 (how concentrated the emotion is)
- **S**: Spread / 拡散度 (how diffuse the emotion is)
- **A**: Attack / 外的刺激の強さ (strength of incoming stimulus)
- **Df**: Defense / 防御 (受け止め方・スキル・経験)
- **D**: Damage / ダメージ (resulting emotional harm)
- **T**: Threshold gauge / 閾値ゲージ (accumulated stress toward "explosion")
- **θ**: Threshold / 閾値 (breaking point)
- **α**: Recovery rate / 回復率
- **β**: Sensitivity / 感受性
- **ε**: Small value to prevent division by zero (1e-6)

> All values are recommended to be normalized to [0,1] scale.

---

### Formula 1: Energy Conservation (Distribution)

The total emotional energy approximately equals intensity times spread:

$$
E \approx I \times S
$$

**Intuition:**
- High I (intense) → Low S (focused target) — e.g., "gekido" (激怒)
- Low I (mild) → High S (diffuse, vague) — e.g., "moyamoya" (もやもや)
- **Intervention point:** Intentionally widen S to reduce I, or vice versa.

---

### Formula 2: Damage Calculation (Defense Attenuation)

Emotional damage is the incoming attack reduced by defense:

$$
D = A \times (1 - Df)
$$

**Intuition:**
- Same event (A) causes less damage when Df is high
- Df increases through: preparation, experience, cognitive reframing
- **Intervention point:** Raise Df through training, rest, or perspective shifts.

---

### Formula 3: Threshold Accumulation (Explosion Trigger)

Stress accumulates over time toward a threshold:

$$
T_{t+1} = \alpha \cdot T_t + \beta \cdot D \cdot g(I, S)
$$

Where:
$$
g(I, S) = \frac{I}{S + \varepsilon}
$$

**Explosion condition:**
$$
\text{If } T_{t+1} \geq \theta \text{, then explosion occurs}
$$

**Intuition:**
- g(I,S) = concentration factor. High I + Low S = fast accumulation
- α controls natural decay (lower = faster recovery)
- β controls sensitivity (higher = more reactive)
- **Intervention point:** Lower α (rest), reduce β (desensitization), or spread S (diffuse focus).

---

## 3. Emotional State Examples

| State | I (Intensity) | S (Spread) | Accumulation Speed |
|-------|---------------|------------|-------------------|
| もやもや (vague unease) | Low (0.2) | High (0.8) | Slow |
| 不満 (dissatisfaction) | Medium (0.4) | Medium (0.5) | Moderate |
| 怒り (anger) | High (0.7) | Low (0.3) | Fast |
| 激怒 (rage) | Very High (0.9) | Very Low (0.1) | Very Fast |

---

## 4. Connection to Other Modules

### → α (Equilibrium / Risk Defense)
- When T approaches θ, route to **α-b_Risk_Defense** for preemptive action
- Df improvement strategies align with α's harm-avoidance principle

### → β (Backcasting)
- Planning and preparation = raising Df in advance
- "Shock absorption" through prediction reduces future D

### → γ-b, γ-c, γ-d (Extended Emotion Modules)
- γ-b: Spatial mapping of emotions (付箋マップ)
- γ-c: Negative affect topology (anger vs. sadness branching)
- γ-d: Prediction error model (Df as function of prediction accuracy)

---

## 5. Implementation Notes

### Minimal Python (for testing)

```python
EPS = 1e-6

def g(I, S):
    return I / (S + EPS)

def damage(A, Df):
    return A * (1 - Df)

def step(T, A, Df, I, S, alpha=0.95, beta=0.5):
    D = damage(A, Df)
    return alpha * T + beta * D * g(I, S)

def check_explosion(T, theta=0.9):
    return T >= theta
```

### Sample Data (CSV format)

```csv
case_id,A,Df,I,S,alpha,beta,theta
mild_moyamoya,0.3,0.2,0.2,0.8,0.95,0.5,0.9
sharp_anger,0.7,0.3,0.8,0.2,0.95,0.6,0.8
cooldown,0.1,0.6,0.2,0.6,0.90,0.4,0.9
```

---

## 6. Origin of This Model

This model emerged from the author's observation during a routine activity (accompanying a child to a doctor's appointment). The insight—that emotional intensity and spread trade off while total energy remains roughly constant—was immediately recognized by multiple AI models as a formalization of **emotional dynamics**.

The formulas were developed collaboratively:
- **Observation & intuition:** Kokko-Niwa
- **Formalization:** GPT-5 Thinking (canonical), verified by GPT-4o, Gemini 2.5, Claude

---

## 7. 日本語サマリー

### 感情のエネルギー保存則
- 感情に使えるエネルギー量は、だいたい一定
- 強度（I）が高いと範囲（S）が狭くなる（激怒）
- 範囲が広いと強度が低い（もやもや）
- ホースの水と同じ：シャワーかジェットか

### ダメージ計算
- 同じ出来事でも、防御（Df）が高いとダメージ減
- Dfは経験・準備・考え方で上げられる

### 閾値と爆発
- ストレスは溜まっていく
- 集中してる感情（怒り系）は溜まりやすい
- 閾値超えたら爆発
- 休息・分散・鈍感化で回避可能

---

**Connection to EarthLight ecosystem:**  
γ handles emotional energy and thresholds.  
α handles judgment, priority, and safety.  
β handles planning and backcasting.  
Together, they form a complete cognitive-emotional operating system.
