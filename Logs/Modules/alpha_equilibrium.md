# α: Core Equilibrium (優先度/徳スコア)

**Spec**: ../..//EarthLight-α/α-a_Core_Equilibrium.md  
**Purpose**: 弱者優先と徳スコア（C,R,E,D,H,λ,ε）で配分と評価を数式化。

### Key signals (what to log)
- `priority = 1/(E+R+D+λH+ε)` を使った優先度判断
- `virtue = (C-R) * C/(R+E+ε)` を使った行動評価
- どの入力変数をどう正規化したか（0〜1）

### Minimal example
- Case: `ff14_ta_01` → priority=3.33, virtue=1.6  
- Rationale: E小・C大・R控えめのため高スコア。

