# Parametric Equilibrium Model (EarthLight-α)

This module formalizes “who should be prioritized” and “who is acting virtuously” as transparent, simple functions. All inputs are normalized to [0,1] in a chosen window (short/mid/long).

## Symbols
- **Cᵢ**: Contribution (public benefit / produced value)
- **Rᵢ**: Reward (pay / rank / reputation actually received)
- **Eᵢ**: Endowment (already-had advantages: assets, credential, institutional support)
- **Dᵢ**: Damage to others (externalized cost caused by i)
- **H**: Systemic harm (global risk or harm in the scene)
- **ε>0**, **λ≥0**: numerical guards / weights  
> Recommend evaluating in three windows: short / mid / long; then aggregate if needed.

## Priority (weak-first with externality compensation)
\[
\mathrm{Priority}_i=\frac{1}{E_i + R_i + D_i + \lambda H + \varepsilon}
\]

## Virtue (difference × ratio with endowment correction)
\[
\mathrm{Virtue}_i=(C_i - R_i)\cdot \frac{C_i}{R_i + E_i + \varepsilon}
\]

**Intuition.**  
- Priority goes up when someone has *less* prior advantage (E), *less* reward (R), and imposes *less* damage (D), under a given system harm level (H).  
- Virtue is high when one contributes much more than one receives, especially when starting advantages were small.

## Role normalization (when labs/tools give built-in advantage)
\[
E'_i=\alpha E_i + \beta E_{\mathrm{role}}
\]
Use this when a role (e.g., “fully equipped lab team”) confers shared structural advantage.

## Minimal example
If a person delivers \(C=0.8\) while receiving \(R=0.2\) with \(E=0.1\), then  
\(\mathrm{Virtue}\approx (0.8-0.2)\times \frac{0.8}{0.2+0.1}\approx 1.6\).  


## Japanese ver
このモジュールは、「誰が優先されるべきか」と「誰が善行をしているか」を、透明でシンプルな関数として定式化します。すべての入力は、選択されたウィンドウ（短期／中期／長期）内で [0,1] に正規化されます。

## Symbols
- C_i: Contribution (成果/公共益)  
- R_i: Reward (報酬/地位/名声)  
- E_i: Endowment (既得: 資産/肩書/教育投資)  
- D_i: Damage to others (外部不利益)  
- H: Systemic harm (全体被害)  
- ε>0, λ≥0: numerical guards

> すべて [0,1] 正規化を推奨。期間は短期/中期/長期の3窓で評価。

## Priority (弱者優先＋外部不利益補正)
\[
\mathrm{Priority}_i=\frac{1}{E_i + R_i + D_i + \lambda H + \varepsilon}
\]

## Virtue (差分×比率、既得補正つき)
\[
\mathrm{Virtue}_i=(C_i - R_i)\cdot \frac{C_i}{R_i + E_i + \varepsilon}
\]

### Role normalization (研究所フル装備などの緩和)
\[
E'_i=\alpha E_i + \beta E_{\mathrm{role}}
\]

