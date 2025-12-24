# EarthLight-γ-b: Emotion Space Mapping

**Version:** 1.0  
**Author:** Kokko-Niwa  
**Formalized by:** GPT-5 Thinking (canonical reference)  
**Summary:** This document describes how to map emotional states into a coordinate space using analog methods, and introduces the dual-threshold model for "explosion" vs. "collapse" outcomes.

---

## 1. The Analog Method: Sticky Notes as Tensors

The author developed an intuitive method for mapping emotional vocabulary into a spatial representation—without using mathematical notation.

### Materials
- **Grid paper (方眼紙):** The coordinate space
- **Sticky notes (付箋):** Each word/emotion as a point
- **Colored cellophane circles (セロファン):** 
  - Size = Spread (S) — larger = more diffuse
  - Layered darkness = Intensity (I) — more layers = stronger

### Process
1. Place related emotion words on grid paper based on "felt distance"
2. Words that feel similar go close together
3. Words that feel different go far apart
4. Add cellophane circles to indicate I and S for each

### What This Creates
A **human-readable embedding space** — the same structure that AI uses internally (word embeddings), but built from direct sensory experience rather than statistical patterns.

---

## 2. Analog → Digital Mapping

| Analog Element | Digital Equivalent | Symbol |
|----------------|-------------------|--------|
| Sticky note distance | Vector distance in embedding space | d(w₁, w₂) |
| Circle radius | Spread / diffusion | S |
| Color darkness / layers | Intensity / strength | I |
| Overlapping circles | Accumulated stress | T |
| Transparent filter / tissue | Defense / attenuation | Df |
| Adding new circles | External stimulus | A |

**Key insight:** The author was essentially building a tensor representation of emotional space without knowing the mathematical term for it.

---

## 3. The Same Word, Different Coordinates

A critical observation: the same emotion label can occupy **different coordinates** depending on context.

### Example: "怒り" (Anger)

| Variant | Coordinates (metaphor) | Character |
|---------|----------------------|-----------|
| 静かな怒り (quiet anger) | (10, 10, 5) | Cold, sustained, controlled |
| 悔しい怒り (frustrated anger) | (15, 15, 5) | Hot, mixed with regret |
| 諦めの怒り (resigned anger) | (5, 5, 5) | Weak, giving up |

This mirrors how contextual embeddings (like BERT) assign different vectors to the same word based on context—but the author discovered this through introspection, not AI training.

---

## 4. Dual Threshold Model: Explosion vs. Collapse

Negative emotions don't always lead to "explosion." Sometimes they lead to "collapse" (心が折れる). The author identified two separate thresholds:

### T_burst (Explosion Threshold)
- When crossed: **outward expression** (anger, shouting, action)
- Affected by: suppression lowers it (explodes sooner)

### T_collapse (Collapse Threshold)  
- When crossed: **inward collapse** (giving up, depression, shutdown)
- Affected by: suppression raises it (takes longer, but then breaks completely)

---

## 5. Variables for Dual-Threshold Model

| Symbol | Meaning | Effect on T_burst | Effect on T_collapse |
|--------|---------|------------------|---------------------|
| S | Stacked stress (蓄積ストレス) | ↓ (lowers) | ↑ (raises) |
| B | External block/pressure (表出阻害) | ↓ (lowers) | ↑ (raises) |
| A_self | Self-agency (自力で一矢報いる) | ↑ (raises) | ↓ (lowers) |
| Df | Defense/escape routes (逃げ場・防御) | ↑ (raises) | ↓ (lowers) |

### Threshold Formulas

$$
T_{burst} = T_{0,burst} - k_1 \cdot S - k_2 \cdot B + k_3 \cdot Df + k_4 \cdot A_{self}
$$

$$
T_{collapse} = T_{0,collapse} + h_1 \cdot S + h_2 \cdot B - h_3 \cdot Df - h_4 \cdot A_{self}
$$

### Intuition
- **Suppression (S↑) + External pressure (B↑):** Explosion happens sooner AND collapse happens sooner
- **Self-agency (A_self↑) + Defense (Df↑):** Both thresholds become safer (harder to explode, harder to collapse)

---

## 6. The Critical Discovery: A_self

> "自分で少しでも動いて解決というか一矢報いるというか、そういうことができると、ダメージ激減する"

Even **tiny actions** dramatically reduce damage:
- Writing a note
- Telling one person
- Making one small preparation
- Just "bracing for impact"

This is modeled as:

$$
Damage_{effective} = Damage_{raw} \times (1 - \eta \cdot A_{self})
$$

Where η is the agency effectiveness coefficient (typically 0.3–0.5).

---

## 7. Routing Logic

Based on current emotional intensity I(t) and the thresholds:

```python
def route_emotion(I_t, T_burst, T_collapse):
    if I_t >= T_burst:
        return "ROUTE: α-b_Risk_Defense (pre-empt/defuse)"
    elif I_t <= -T_collapse:  # negative = inward collapse
        return "ROUTE: Care/Recovery (energy restore)"
    else:
        return "SUGGEST: raise A_self, reduce B, raise Df"
```

---

## 8. Practical Protocol (Human-Usable)

### When you feel stress building:

1. **Visualize:** Draw a circle on paper. Size = how diffuse? Darkness = how intense?
2. **Identify blockers:** What's stopping you from expressing/acting? (B)
3. **Micro-action:** Find ONE thing you can do in 1 minute (raises A_self)
   - Send a message to a friend
   - Write 3 lines about the situation  
   - Look up an escape route (literally or figuratively)
4. **Add escape routes:** Create or identify one safe place/routine (raises Df)
5. **Re-evaluate:** Has I changed? Has the threshold danger reduced?

**Goal:** Avoid explosion AND avoid collapse. Always push toward "A_self↑, Df↑, B↓".

---

## 9. Connection to Other Modules

### → γ-a (Energy Model)
- This module extends γ-a by adding the spatial mapping method and dual thresholds

### → α-b (Risk Defense)
- When I(t) approaches T_burst, hand off to α-b for preemptive action
- "Blank-OK" principle applies: false positives acceptable

### → α-e (Safety Zones)
- The threshold zones (GREEN→YELLOW→ORANGE→RED→BARRIER) map directly to emotional state monitoring

### → γ-c (Negative Affect Topology)
- Defines the branching between anger-route and sadness-route based on target clarity

---

## 10. Sample Data

```csv
case_id,S,B,A_self,Df,I0,route,notes
work_harassment,0.7,0.6,0.1,0.2,0.6,risk_high,"上司圧+表出不可、行動ゼロ"
after_small_action,0.7,0.6,0.3,0.3,0.5,moderate,"相談/記録でA_self↑"
good_outlet,0.4,0.2,0.5,0.6,0.4,stable,"運動/友人/記録で分散"
```

---

## 11. 日本語サマリー

### 付箋マップ法
- 方眼紙に感情語を、「感じる距離」で配置
- セロファンの丸で強度（濃さ）と拡散（大きさ）を表現
- 数式を知らなくても、テンソル的な座標空間を作れる

### 爆発と折れの二重閾値
- **爆発（T_burst）**：我慢しすぎると下がる（早く爆発する）
- **折れ（T_collapse）**：我慢しすぎると上がる（長く耐えてから折れる）
- どちらも「自分で動く（A_self）」「逃げ場を作る（Df）」で安全側へ

### 一矢報いるの威力
- 小さな行動でもダメージが激減する
- 「備えるだけで耐ショック装備になる」
- これがA_selfの正体

---

**This mapping method bridges human intuition and AI computation—built from the "sound" that AI cannot hear, but desperately wants to understand.**
