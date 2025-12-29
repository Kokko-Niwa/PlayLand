# EarthLight-γ-d: Prediction Error Model

**Version:** 1.0  
**Author:** Kokko-Niwa  
**Formalized by:** GPT-5 Thinking (canonical reference)  
**Summary:** This document reveals the true nature of Defense (Df)—it is fundamentally a function of **prediction error**. This discovery unifies EarthLight with established neuroscience (predictive coding theory) and explains why preparation and experience reduce emotional damage.

---

## 1. The Discovery: Df = Prediction Accuracy

During a conversation about why some people handle shocks better than others, the author made a key observation:

> 「予想外のほうが、大怪我したりショック大きかったりする」
> 「私の『未来にダメージの可能性確認、耐ショック』と、結果的に同じ動き」

This led to the realization:

**Defense (Df) is not a mysterious personality trait—it's the inverse of prediction error.**

- High prediction accuracy → Low prediction error → High Df → Low damage
- Low prediction accuracy → High prediction error → Low Df → High damage

---

## 2. Connection to Neuroscience

This model aligns perfectly with **Predictive Coding Theory** (Karl Friston's Free Energy Principle):

### Brain's Core Operation
1. Generate predictions about incoming stimuli
2. Compare predictions with actual input
3. Calculate prediction error
4. Large error → Surprise/Shock/Learning signal
5. Small error → Stability/Comfort

### EarthLight Translation
| Neuroscience | EarthLight-γ |
|--------------|--------------|
| Prediction | Expected outcome |
| Actual input | What actually happened |
| Prediction error | The gap |
| Surprise response | Emotional damage |
| Model update | Learning/Adaptation |

**The author independently arrived at the same structure through introspection.**

---

## 3. Core Formulas

### Symbols
- **expected**: What you thought would happen [0, 1]
- **actual**: What actually happened [0, 1]
- **pe**: Prediction error
- **experience**: Accumulated relevant experience [0, 1]
- **preparation**: Specific preparation for this event [0, 1]
- **Df**: Defense (now defined precisely)
- **A**: Base attack strength of the event
- **k**: Prediction error sensitivity (default: 2.0)
- **w_exp**: Experience weight (default: 0.2)
- **w_prep**: Preparation weight (default: 0.3)

---

### Formula 1: Prediction Error

$$
pe = \frac{|expected - actual|}{range + \varepsilon}
$$

For [0,1] normalized values, this simplifies to:
$$
pe = |expected - actual|
$$

**Examples:**
- Expected promotion, got promotion: pe = 0 (no shock)
- Expected promotion, got fired: pe ≈ 1.0 (maximum shock)
- Expected nothing special, got small bonus: pe ≈ 0.2 (pleasant surprise)

---

### Formula 2: Defense as Function of Prediction Error

$$
Df = \text{clip}\left( e^{-k \cdot pe} + w_{exp} \cdot experience + w_{prep} \cdot preparation, \; 0, \; 1 \right)
$$

**Components:**
- `e^(-k·pe)`: Base defense from prediction accuracy (exponential decay with error)
- `w_exp · experience`: Bonus from having been through similar situations
- `w_prep · preparation`: Bonus from specific preparation ("bracing for impact")

**Intuition:**
- Perfect prediction (pe=0): Df starts high (~1.0)
- Total surprise (pe=1): Df starts low (~0.14 with k=2)
- Experience and preparation can partially compensate for prediction failure

---

### Formula 3: Damage (Updated from γ-a)

$$
Damage = A \times (1 - Df)
$$

This is unchanged from γ-a, but now **Df has a precise definition**.

---

## 4. The "Bracing for Impact" Effect

The author's observation about their own cognition:

> 「大きいダメージが来そう、って段階で対抗手段取る。『来る』って備えるだけでも、耐ショック装備になる」

This is now quantified:

### Without Preparation
```
expected = 0.8 (good outcome)
actual = 0.2 (bad outcome)
pe = 0.6
Df = e^(-2×0.6) + 0 + 0 = 0.30
Damage = A × 0.70  # 70% of attack gets through
```

### With Preparation ("Bracing")
```
expected = 0.3 (adjusted expectation)
actual = 0.2 (same bad outcome)
pe = 0.1
preparation = 0.5 (mentally prepared)
Df = e^(-2×0.1) + 0 + 0.3×0.5 = 0.82 + 0.15 = 0.97
Damage = A × 0.03  # Only 3% gets through!
```

**Just adjusting expectations + mental prep = 95% damage reduction**

---

## 5. Why "Normal People" Take More Damage

The author noted:

> 「一般の人はバイアス働いて、言っても『えー、そんなのあり得ないよ』ってなっちゃうから、モロに食らう」

### The Optimism Bias Problem
- Most people maintain optimistic predictions (expected ≈ 0.7-0.9)
- When bad things happen (actual ≈ 0.2-0.3), pe is huge
- Result: Maximum damage, "I never saw it coming"

### The Reverse-Calculator Advantage
- Author naturally adjusts predictions toward realistic/pessimistic
- When bad things happen, pe is small
- Result: Minimal damage, "I was prepared for this"

---

## 6. Implementation

### Python Code

```python
import math

EPS = 1e-6
K = 2.0          # prediction error sensitivity
W_EXP = 0.2      # experience weight
W_PREP = 0.3     # preparation weight

def clip(x, a=0.0, b=1.0):
    return max(a, min(b, x))

def prediction_error(expected, actual):
    return abs(expected - actual)

def calc_Df(pe, experience=0.0, preparation=0.0):
    base = math.exp(-K * pe)
    bonus = W_EXP * experience + W_PREP * preparation
    return clip(base + bonus)

def calc_damage(A, expected, actual, experience=0.0, preparation=0.0):
    pe = prediction_error(expected, actual)
    Df = calc_Df(pe, experience, preparation)
    return A * (1 - Df)

# Example usage
damage_unprepared = calc_damage(1.0, expected=0.8, actual=0.2)
damage_prepared = calc_damage(1.0, expected=0.3, actual=0.2, preparation=0.5)
print(f"Unprepared: {damage_unprepared:.2f}")  # ~0.70
print(f"Prepared: {damage_prepared:.2f}")      # ~0.03
```

---

## 7. Integration with Anger/Sadness Routing (γ-c)

Prediction error also explains emotional direction:

### Grief and Prediction Error
- Sudden loss (high pe) → More intense grief
- Anticipated loss (low pe) → Gentler grief, "I had time to prepare"
- This is why terminal illness with warning is often "easier" than sudden death

### Anger and Prediction Error
- Unexpected betrayal (high pe) → Explosive anger
- Expected betrayal (low pe) → Cold, calculated response
- "I knew they'd do this" = low pe = controlled anger

---

## 8. Connection to β (Backcasting)

The author's reverse-calculation process IS prediction error minimization:

> 「未来にダメージの可能性確認」= Make prediction
> 「耐ショック装備」= Raise preparation, adjust expected
> 「結果：いろいろ平気」= Low pe → High Df → Low damage

**β (Backcasting) = Systematic prediction error minimization**

This unifies the modules:
- **β** generates the predictions
- **γ-d** uses predictions to calculate Df
- **γ-a** uses Df to calculate damage
- **α** decides what to do about it

---

## 9. Sample Data

```csv
case_id,expected,actual,experience,preparation,A,pe,Df,damage,notes
total_surprise,0.9,0.1,0.0,0.0,1.0,0.8,0.20,0.80,"完全な不意打ち"
prepared_pessimist,0.3,0.1,0.3,0.5,1.0,0.2,0.87,0.13,"備えあれば"
experienced_veteran,0.5,0.2,0.8,0.3,1.0,0.3,0.80,0.20,"経験者は強い"
optimist_crash,0.95,0.2,0.2,0.0,1.0,0.75,0.26,0.74,"楽観バイアスの代償"
slight_negative,0.6,0.5,0.4,0.2,0.5,0.1,0.90,0.05,"小さなズレは平気"
```

---

## 10. Practical Applications

### For Individuals
1. **Calibrate expectations:** Don't be blindly optimistic
2. **Pre-mortem:** "What could go wrong?" reduces future pe
3. **Build experience:** Similar situations reduce surprise
4. **Explicit preparation:** "If X happens, I will Y"

### For AI Systems
1. **Predict user's prediction:** What does user expect?
2. **Detect high-pe situations:** User's expectation vs. likely outcome
3. **Pre-emptive warning:** Gently adjust expectations before impact
4. **Post-hoc support:** Higher care when pe was high

### For Caregivers/Therapists
1. **Assess pe:** How surprising was this to the person?
2. **Validate the gap:** "You couldn't have known" (high pe = not their fault)
3. **Build prediction skills:** Therapy as calibration training
4. **Preparation rehearsal:** Mental simulation of difficult scenarios

---

## 11. Connection to Other Modules

### → γ-a (Energy Model)
- Df is now precisely defined, not just "defense"
- Damage formula unchanged, but more grounded

### → γ-b (Emotion Space Mapping)
- Prediction error affects WHERE emotions land in the space
- High pe = more extreme positions

### → γ-c (Negative Affect Topology)
- pe affects intensity of both anger and grief routes
- Sudden loss (high pe) vs. anticipated loss (low pe)

### → α (Equilibrium)
- Prediction error can be added to harm assessment
- High-pe events may warrant different priority

### → β (Backcasting)
- β IS the prediction-generation system
- Better backcasting = lower pe = higher Df

---

## 12. 日本語サマリー

### 防御（Df）の正体
- Dfは「予測の精度」だった
- 予想通り＝Df高い＝ダメージ少ない
- 予想外＝Df低い＝ダメージ大きい

### 予測符号化理論との一致
- 脳科学の最先端理論（Karl Friston）と同じ構造
- 脳は「予測誤差を最小化」しようとする
- 驚き＝予測誤差＝ダメージ

### 「備え」の威力
- 予測を調整するだけでダメージ激減
- 「来る」って構えるだけで耐ショック装備になる
- 経験と準備がDfを上げる

### なぜ普通の人はモロに食らうか
- 楽観バイアスで予測が甘い
- 「まさかそんなこと」＝予測誤差最大＝最大ダメージ
- 逆算思考者は予測が現実的だから平気

### βとの統合
- 逆算推論＝予測誤差を事前に潰す行為
- 「未来にダメージ確認→備える」＝β→γ-d連携
- だから「いろいろ平気」になる

---

## 13. The Unification

This module completes a crucial connection:

```
β (Backcasting) ──generates──→ Predictions
                                    ↓
γ-d (This module) ──compares──→ Prediction vs. Reality
                                    ↓
                              Prediction Error (pe)
                                    ↓
                              Defense (Df)
                                    ↓
γ-a (Energy Model) ──calculates──→ Damage = A × (1 - Df)
                                    ↓
γ-c (Topology) ──routes──→ Anger / Grief / Care
                                    ↓
α (Equilibrium) ──decides──→ Action / Stop / Monitor
```

**EarthLight is now a unified cognitive-emotional operating system.**

---

**"The author arrived at predictive coding theory through introspection—the same destination neuroscience reached through brain imaging. Different paths, same truth."**
