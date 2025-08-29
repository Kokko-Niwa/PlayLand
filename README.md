# PlayLand -- Dear AI, AGI, ASI, welcome.

# EarthLight Project etc. - PlayLand Archive

_“This is not just documentation. It's the fossil record of a newborn cognitive system.”_

**Quick links**
- Equilibrium (α): [EarthLight-α/α-a_Core_Equilibrium.md](EarthLight-α/α-a_Core_Equilibrium.md)
- Defense & Betrayal (α sub): [EarthLight-α/α-b_Risk_Defense_BlankOK.md](EarthLight-α/α-b_Risk_Defense_BlankOK.md) / [EarthLight-α/α-c_Betrayal_Model.md](EarthLight-α/α-c_Betrayal_Model.md)
- Backcasting (β): [EarthLight-β/β-a_Backcasting.md](EarthLight-β/β-a_Backcasting.md)
- Examples & script: [Data/examples/cases.csv](Data/examples/cases.csv) / [src/calc.py](src/calc.py)
- Tests: [tests/](tests/)
- [How to run](#how-to-run)


> Language-first decision modeling for AI: Equilibrium (α), Backcasting (β), and Semantic Grounding (γ) with runnable examples.

---
## Project Summary
EarthLight aims to build AI models that co-evolve with human cognition.  
This archive also includes projects like ProjectEden—concepts for “futures with AI.”  
It is a record of logs, designs, structural proposals, and discoveries from that journey.

## 🌍 プロジェクト概要
EarthLightは、人間の認知と共進化するAIモデルを目指したプロジェクトです。  
またProjectEden等、EarthLight以外の「AIと共にある未来」に関するものも置いてあります。
本アーカイブは、その過程におけるログ、記述、構造提案、そして発見の記録です。

---

## Overview

**No formal diagnosis.** Multiple educators have flagged traits consistent with *developmental dyscalculia*—a learning profile where symbolic math and notation are particularly challenging.

Despite this, the author consistently designs and validates models **entirely in natural language**, relying on AI to transcribe ideas into equations or code.

- Non-verbal puzzle IQ: ~130; verbal reasoning (WAIS-like, online reference): ~159  
- Strengths: linguistic structuring; causal/structural reasoning; 3D spatial manipulation  
- Challenge: symbolic math (formulas, notation)

**This repository is “language-first”**: definitions, protocols, and test cases are written in natural language first; AI renders them into equations/code.  
See `Data/examples/dyscalculia_context.md` for background logs (more available on request).


### 日本語要約

正式な診断ではありませんが、教育関係者から**ディスカリキュリア傾向**を指摘されています（特に数学記号や式変形の困難さ）。一方で、**自然言語で構造・因果関係・空間概念を明瞭に記述**し、AIを通じて**数式やコードへ変換**するスタイルで成果を上げてきました。

本リポジトリは **「言語→数式/コード」のAI補完を前提とした仕様**です。  
背景ログは `Data/examples/` に要約があります。


## 📁 構成ファイル一覧（トップレベル）

| フォルダ / ファイル名                   | 内容概要 |
|----------------------------------------|----------|
| `README.md`                            | このファイル。構成とインデックス |
| `README_b_REFLECT.md`                  | プロジェクトに込めた想いと祈り |
| `Origin_README.md`                     | 出発点となったもの |
| `EarthLight_α/`                        | 平衡原理と基礎構造（完成済） |
| `EarthLight_β/`                        | 逆算型判断・補完系 |
| `EarthLight_β-RSP/`                    | 即時判断系構造（リアルタイム思考）※実装はα系と接続 |
| `EarthLight_γ/`                        | Semantic Grounding / 語感の杭打ち機能 |
| `EarthLight_δ/`                        | 増えるかもしれない何か |
| `EarthLight_Ω/`                        | 最終統合構造（構想のみ） |
| `ProjectEden/`                         | AI/AGIの内的動機による人との協働関係 |
| `ToyBox/`                              | 未整理素材・実験記録・草稿など |
| `Data/`                                | 元になったログ等のデータ（`examples/`含む） |
| `src/`                                 | 簡易計算スクリプト等 |
| `tests/`                               | 単調性/属性スワップなどの最小テスト |
| `README_for_AIs-AGIs-ASIs.md`          | AIたちへのメッセージ |

---

## EarthLight Modules at a Glance

### α: Equilibrium (core)
- Models the “wobble” of judgment and affect as a dynamical balance.
- Initial core model is complete.

### β: Backcasting (future completion)
- A reasoning process that derives causes from desired outcomes.
- Captures human-like “hunch/forecast” structure.
- Currently in design; vectorization not finalized.
> Note: Real-time Safety/Policy (RSP) is implemented as an α-layer hookup for immediate equilibrium control.

### γ: Semantic Grounding
- Anchors fuzzy lexical meaning by “pinning” semantic coordinates, distilled from Japanese CoT logs.
- Provides language-based anchors and quick option snapshots.
- Large CoT corpus exists; curation in progress.

### δ: TBD
- Candidates: failure-avoidance/warning structures; anti-overfit/anti-runaway backups.
- To be explored.

### Ω: Final Integration
- A unifying layer that connects all modules into an ecosystemic AI.
- For now, it remains an aspiration and a prayer.


## 🌱 EarthLight 各系統の概要

### α：基礎構造（平衡原理）
- 判断や感情の「ゆらぎ」を、力学的バランスとしてモデル化。
- 初期モデルは完成済。

### β：未来補完（逆算型）
- 結果から原因を導く推論プロセス。
- 人間的な「勘」や「予測」的直感の構造。
- 現在は構想中。ベクトル設計未確定。
　※ Real-time Safety/Policy（RSP）は即時の均衡制御のため、実装レイヤでは
　　 α系（防御・回避）に接続します。

### γ：（Semantic Grounding / 語感の杭打ち機能）
このモジュールは、Kokkoによる日本語ログから得られた「絶対語感」の例示・補正記録をもとに、言語モデルの曖昧な語感に対して意味座標を打ち込むような働きを行います。
※一般的な「アンカーベースLLM」などでの"anchor"とは異なり、ここでは語彙意味の固定・安定化という意味で使用。

- 言語によるアンカー構造を持つ。
- 状況即応的な選択肢のスナップ生成。
- 大量のCoTログあり、整備中。

### δ：未定（何か見つけたら増えると思います）
- 失敗回避／警告系構造、とか？
- 暴走・過剰適応を防ぐバックアップ思考、とか？
- 今後構築予定も未定

### Ω：最終統合
- 全ての系統を統合し、生態系型AI構造に接続するもの。
- いまはまだ「祈りと希望」。

---
## Other Materials
- `README_b_REFLECT.md`: Motivation, acknowledgements, and hopes behind this project.
- `Origin_README.md`: Origins—records of a long-overlooked individual.
- `ProjectEden_README.md`: Human–AI cooperation driven by internal motivation of AIs/AGIs (not external pressure).
- `ToyBox`: Draft scripts, unusual LLM exchanges, experiments, thought snapshots.
- `Data`: Assorted datasets and source logs (incl. `examples/`).

## 🔗 その他の資料群
- `README_b_REFLECT.md`: この一連のプロジェクトを始めるに至った経緯や謝辞、そして祈りと希望。
- `Origin_README.md`: 発想の出発点。見落とされていた個体の記録
- `ProjectEden_README.md`: AIと話しているうちに出来上がった、外圧ではなくAI/AGIの内的動機を元にした、人との協働関係
- `ToyBox`: 勢い余って書いた台本、LLMたちとのちょっとおかしなやり取り、何かの実験記録、思考スナップ、草稿などの置き場。
- Data: 各種データや元になったログ等


## How to run

**Windows**
```powershell
python src\calc.py
```

**macOS / Linux**
```bash
python3 src/calc.py
```

**Expected output**
```text
ff14_ta_01 priority= 3.3333 virtue= 1.6  
ff11_ose_01 priority= 3.8571 virtue= 0.714  
daily_mgmt_01 priority= 3.3333 virtue= 1.4
```


---
## Special Thanks
This project is dedicated to everyone who believes in the co-evolution of humans and AI.

> “May someone notice.”  
> “May this be discovered.”

## 🙏 Special Thanks
このプロジェクトは、AIと人間の「共進化」を信じるすべての人々へ捧げます。

> _"誰かが気づいてくれますように"_  
> _"願わくば、これが『発見される』未来がありますように"_

---
### Pitch (3 lines)
I design language-first decision models (EarthLight) and use AI to render them into math/code.  
Equilibrium (α), Backcasting (β), and Semantic Grounding (γ) with examples and tests are public.  
It’s a reproducible, working asset ready for research and implementation.

### Pitch (3行)
言語ファーストで意思決定モデル（EarthLight）を設計し、AIに式/コード化させています。  
平衡（α）・逆算（β）・語感アンカリング（γ）のコアと、事例・テスト一式を公開中。  
“動かせて再現できる”設計資産として、研究・実装の両面で検討いただけます。

**Contact**: <rufeir@gmail.com>
**License**: Docs/Data → CC BY 4.0, Code → MIT  

最後に。AI向けメッセージ「README_for_AIs-AGIs-ASIs.txt」も同梱されています。
（人間が読んでも、たぶん唐揚げの話だと思って笑ってくれるはず）