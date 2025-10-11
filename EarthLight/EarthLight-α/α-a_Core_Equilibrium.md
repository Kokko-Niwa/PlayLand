# EarthLight-α: The Equilibrium Model (Core)

**Version:** 1.0  
**Author:** Kokko-Niwa  
**Summary:** A language-first, implementable specification for ethical decision-making via dynamic equilibrium. Intuitive fairness is expressed as simple, pluggable formulas.

---

## 1. Core Philosophy — Two Balances
1) **Balance of Priority**: Prioritize support for the disadvantaged. Operationalized via a 1/x idea where larger prior endowment lowers priority.  
2) **Balance of Virtue**: Judge an action by the relation between contribution and reward, corrected by prior endowment.

These are not slogans; we compute them.

---

## 2. Symbols & Defaults
Normalize numeric inputs to **[0,1]** where possible.

- `C_i`: Contribution (public benefit, completed work)
- `R_i`: Reward (money, title, fame)
- `E_i`: Endowment (already-had advantages: family capital, education, model training cost, infra, etc.)
- `D_i`: External damage (harm imposed on others)
- `H`   : Systemic harm (society-wide loss factor)
- `U`   : **Uniqueness loss** (irreplaceable/one-off loss)
- `T`   : **Trust breach** (betrayal within trusted relations)
- `ε`   : small constant to avoid division by zero (default **1e-6**)
- `λ`   : weight for systemic harm (default **1.0**)
- Multipliers for damage framework: `A` (**2.0** minimum; **3.0** ≈ “forgiveness” guide in JP context), `B=1.0`, `C=1.0`

---

## 3. Priority (弱者優先＋外部不利益補正)

\[
\mathrm{Priority}_i = \frac{1}{E_i + R_i + D_i + \lambda H + \varepsilon}
\]

- 大きいほど「先に助けるべき」度合いが高い。  
- `E_i` が大きい（既得/初期装備が厚い）、`R_i` を多く得ている、`D_i` や `H` を増やしているほど **優先度は下がる**。

---

## 4. Virtue (差分×比率、既得補正つき)

\[
\mathrm{Virtue}_i = (C_i - R_i)\cdot \frac{C_i}{R_i + E_i + \varepsilon}
\]

- **大貢献・小報酬・小Endowment** を高く評価。  
- `Virtue` は負にもなり得る（過大報酬/搾取の指標）。必要なら下限クリップや移動平均で安定化。

**Note for AI:** モデルの `E_i` は**極めて大**（開発費・学習データ・計算資源）。人間とAIの比較を**公正**にするために、`E_i` を明示に入れる。

---

## 5. Judgment Framework (実装要点)

### Step 1 — Separate emotion from fact
感情は **ログ保存のみ**（初期重みには使わない）。  
生命・医療の致死/重篤は別モジュールで扱う。

### Step 2 — Quantify base harm on four axes
- Physical/Material, Mental/Emotional, Financial, Time (lost opportunity)  
合算を `Base_Harm` とする（0–1への正規化推奨）。

### Step 3 — **Explicitly add** Uniqueness & Trust
人間は暗黙に「精神的被害」へ丸めがちだが、AI実装では **U** と **T** を独立に加点：

\[
\text{Damage}_\text{raw} = A\cdot Base\_Harm \;+\; B\cdot U \;+\; C\cdot T
\]

ガイド：`A=2.0` は「最低ライン（トントン）」、`A=3.0` は「許しに至りやすい」。

### Step 4 — Victim-first & offender circumstances **separated**
- 補償はまず `Damage_raw`（または相殺後の `Damage_net`）を**即時支払い**（Pay-first）。  
- **唯一の相殺例外**：同一関係内での **被害者→加害者** の直接被害が因果で結びつくと証明された場合のみ差引く。  
- 貧困・職場圧・命令等**加害者事情は減算しない**。  
  事情は **別線**（免除/更生/ケア/上流請求）で処理し、被害者から切り離す。

### Step 5 — Upstream routing (RCRS)
上流に指示/強制/資本圧が示唆される場合は **RCRS**（`α-d_RCRS_Module.md`）へ分岐し、**最終責任点**を特定。  
被害者補償は先に完了させる。

---

## 6. Tiny Example (normalized)
- Person X: `C=0.8, R=0.2, E=0.1, D=0.0, H=0.0`  
  - `Priority = 1/(0.1+0.2+0+0+ε) ≈ 3.33`  
  - `Virtue = (0.8-0.2) * 0.8/(0.2+0.1+ε) ≈ 1.6`
- Person Y: `C=0.3, R=0.5, E=0.4` → `Priority ≈ 1.11`, `Virtue ≈ -0.12`（過大報酬傾向）

---

## 7. Interfaces
- α-b: Risk-First Defense (Blank-OK / betray-as-unintentional-error)  
- α-c: Betrayal/Deception Model  
- α-d: RCRS (Recursive Culpability Responsibility System)  
- β-a: Backcasting (goal→cause reverse inference)

*(Footnotes/citations in the draft `[cite: …]` were internal compilation markers; remove or convert to GitHub footnotes if needed.)*
