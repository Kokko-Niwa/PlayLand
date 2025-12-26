# EarthLight-γ-c: Negative Affect Topology

**Version:** 1.0  
**Author:** Kokko-Niwa  
**Formalized by:** GPT-5 Thinking (canonical reference)  
**Summary:** This document maps the branching structure of negative emotions—how "unpleasant" splits into anger-route vs. sadness-route, and how misdirected anger (誤射) occurs.

---

## 1. Core Observation: Two Directions of Negative Emotion

The author observed that negative emotions branch into fundamentally different paths:

### The Fork
```
Positive (快) ──→ Generally safe, no intervention needed
                  (instant release, no accumulation problem)

Negative (不快) ─┬→ Dissatisfaction (不満) → Anger (怒り)
                │   "Something/someone broke what I had or expected"
                │   → Has a TARGET
                │
                └→ Grief (悲しみ)
                    "Loss of what existed"
                    → No target (or self as target)
```

### Key Insight
> 「悲しみと称されるのはほぼ、『あった状態からの喪失』。それ以上でもそれ以下でもなさそう」

Grief is purely about **loss**. Anger is about **something/someone causing the loss**.

---

## 2. Variables for Branching

| Symbol | Meaning | Range |
|--------|---------|-------|
| valence | Positive or negative | +1 / -1 |
| target_clarity | How clear is the target/cause | [0, 1] |
| loss_indicator | How much is this about losing something | [0, 1] |
| locus_control | Sense of personal control/agency | [0, 1] |
| E_total | Total accumulated emotional energy | [0, 1] |
| θ_energy | Energy threshold for "release phase" | ~0.6 |
| τ_target | Target clarity threshold | ~0.7 |

---

## 3. The Energy-First Gate (Critical Correction)

The author's key correction to the initial model:

> 「まずエネルギー総量での閾値があって、それを超えると対象で振り分け」

**Wrong model:** Target clarity → Anger  
**Correct model:** Energy threshold FIRST → THEN target clarity decides direction

### Why This Matters
- Low energy + clear target = mild annoyance, no explosion
- High energy + clear target = directed anger
- High energy + unclear target = **misdirected anger (誤射)**

---

## 4. Branching Logic

### Phase 1: Valence Check
```
if valence == '+':
    route = 'log_only'  # Positive emotions: just record, no intervention
    return route
```

### Phase 2: Self-Directed Risk Check
```
if loss_indicator >= θ_loss AND locus_control <= θ_ctrl_low:
    route = 'care_self_directed'  # 自責化リスク → 即ケア
    return route
```

### Phase 3: Energy Threshold Check
```
E_total = w1 * S + w2 * I  # Accumulated stress + current intensity

if E_total < θ_energy:
    route = 'monitor_only'  # Not enough energy to explode
    return route
```

### Phase 4: Target-Based Routing
```
if target_clarity >= τ_target:
    route = 'alpha_risk_defense'  # Clear target → anger route
else:
    route = 'misattribution_guard'  # Unclear target → 誤射リスク
```

---

## 5. Complete Routing Code

```python
def route_negative_emotion(
    valence, 
    loss_indicator, 
    locus_control,
    S,  # stacked stress
    I,  # current intensity
    target_clarity,
    theta_loss=0.7,
    theta_ctrl_low=0.3,
    theta_energy=0.6,
    tau_target=0.7,
    w1=0.5,
    w2=0.5
):
    # Phase 1: Positive emotion
    if valence == '+':
        return 'log_only'
    
    # Phase 2: Self-directed risk
    if loss_indicator >= theta_loss and locus_control <= theta_ctrl_low:
        return 'care_self_directed'
    
    # Phase 3: Energy check
    E_total = w1 * S + w2 * I
    if E_total < theta_energy:
        return 'monitor_only'
    
    # Phase 4: Target-based routing
    if target_clarity >= tau_target:
        return 'alpha_risk_defense'  # Proper anger route
    else:
        return 'misattribution_guard'  # Misdirection risk
```

---

## 6. The Misattribution Problem (誤射)

When energy exceeds threshold but target is unclear:

> 「対象が今一つはっきりしない＞偶然そこに居合わせただけの人へ向かったりする」

### Misattribution Guard Protocol

1. **Delay:** Don't act immediately (24-hour rule, sleep on it)
2. **Low-risk discharge:** Walk, exercise, write it out
3. **Verification:** 
   - Timeline: What actually happened when?
   - Evidence: What do I actually know vs. assume?
   - Intent: What was the other person's actual intent?
4. **Third-party check:** Tell someone neutral, get their read
5. **Re-route:** After cooling, re-evaluate target_clarity

```python
def misattribution_guard(E_total, target_clarity):
    actions = []
    actions.append("DELAY: Do not act for 24 hours")
    actions.append("DISCHARGE: Walk 10min / Write 3 lines / Exercise")
    actions.append("VERIFY: Timeline, Evidence, Intent")
    actions.append("CHECK: Tell neutral party, get feedback")
    actions.append("RE-ROUTE: Re-evaluate target_clarity after cooldown")
    return actions
```

---

## 7. Anger ↔ Sadness Oscillation

The author observed that anger and sadness can **alternate** for the same event:

> 「怒りと悲しみが交互（人間完全同時はさすがに難しい）とかもある」

### Why This Happens
- Same event has both: a **loss** (→ sadness) AND a **cause** (→ anger)
- Human attention can only focus on one at a time
- So we oscillate between mourning the loss and being angry at the cause

### Handling in Code
```python
# Track oscillation
emotion_history = ['anger', 'sadness', 'anger', 'sadness']

if oscillation_detected(emotion_history):
    # Both need addressing
    actions = [
        "ACKNOWLEDGE: Both loss and cause are real",
        "SEPARATE: Process grief and anger in different sessions",
        "GRIEF FIRST: Often reduces anger intensity"
    ]
```

---

## 8. Self-Directed Anger (自責化)

When grief is overwhelming and there's no external target, anger turns inward:

> 「不可抗力による悲しみが大きすぎると、はけ口を求めて自分に対する怒りに走る」

### Detection
- High loss_indicator (≥ 0.7)
- Low locus_control (≤ 0.3)
- No clear external target

### Response
**Immediate care route.** Do not process through normal anger pathways.

```python
if self_directed_risk(loss_indicator, locus_control, target_clarity):
    return {
        'route': 'immediate_care',
        'actions': [
            "STOP: Do not analyze further",
            "SUPPORT: Connect with safe person",
            "RESOURCE: Professional help if persistent",
            "REFRAME: External factors exist, not just self"
        ]
    }
```

---

## 9. Connection to Other Modules

### → γ-a (Energy Model)
- E_total calculation uses I and S from γ-a
- Threshold mechanics are consistent

### → γ-b (Emotion Space Mapping)
- Anger and sadness occupy different regions in the space
- Oscillation = movement between regions

### → γ-d (Prediction Error)
- Grief often involves massive prediction error (didn't expect the loss)
- This explains why sudden loss hurts more than anticipated loss

### → α-b (Risk Defense)
- Anger route hands off to α-b for preemptive action
- "Blank-OK" principle: stop first, verify later

### → α-d (RCRS)
- If the "cause" is an upstream actor (company, system), route to RCRS
- Victim care first, responsibility tracing second

---

## 10. Sample Data

```csv
case_id,valence,target_clarity,loss_indicator,locus_control,S,I,route,notes
clear_anger,-,0.9,0.2,0.6,0.6,0.7,alpha_risk_defense,"明確な対象→怒りルート"
pure_grief,-,0.1,0.9,0.4,0.5,0.6,care_grief,"喪失のみ→ケア優先"
self_blame,-,0.2,0.9,0.1,0.7,0.8,care_self_directed,"自責化リスク→即ケア"
misdirection_risk,-,0.3,0.3,0.5,0.8,0.7,misattribution_guard,"対象不明瞭→誤射警戒"
oscillating,-,0.6,0.7,0.5,0.6,0.6,monitor_both,"怒りと悲しみ交互"
low_energy,-,0.8,0.3,0.6,0.2,0.3,monitor_only,"エネルギー不足→監視のみ"
```

---

## 11. 日本語サマリー

### ネガティブ感情の分岐
- **不満→怒り**：「誰か/何かに壊された」→対象がある
- **悲しみ**：「あったものの喪失」→対象がない

### エネルギーが先、対象が後
- まず「エネルギー総量」が閾値を超えるかどうか
- 超えてから「対象がはっきりしてるか」で振り分け
- はっきりしてない＝**誤射リスク**（関係ない人に当たる）

### 怒りと悲しみの交互
- 同じ出来事で両方感じることがある
- 人間は同時処理できないから交互になる
- 両方あることを認めて、別々に処理する

### 自責化の危険
- 喪失が大きい＋自分でどうしようもない＝自分を責め始める
- これは即ケアルート。分析モードに入らない。

### 誤射を防ぐ
- 24時間待つ
- 歩く/書く/運動で放電
- 事実確認（時系列・証拠・意図）
- 第三者に話す
- 冷えてから再判定

---

**This topology maps the "which way does the emotion go?" decision tree—critical for AI systems that need to respond appropriately to human emotional states.**
