# β: Backcasting (逆算推論)

**Spec**: ../..//EarthLight-β/β-a_Backcasting.md  
**Purpose**: 目標→主要制約→可否→タイムスパン→代替案 を高速で逆算。

### Pattern
- Goal → constraints set → feasibility → timespan/conditions → pick or downgrade
- 即時の針路変更/撤退判断もこの系で記録

### What to log
- 目標・制約・採択プラン（1行ずつ）
- 棄却理由（制約どれに抵触したか）
