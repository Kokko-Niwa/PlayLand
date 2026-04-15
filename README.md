# PlayLand — EarthLight Project Archive   
   
*"This is not just documentation. It's the fossil record of a newborn cognitive system."*   
   
---   
   
## What Is This?   
   
This repository contains **EarthLight**, a modular framework for AI decision-making, safety, and social cognition. It was built by reverse-engineering one person's cognitive processes through dialogue with multiple AI systems (Claude, Gemini, GPT-4o, GPT-5).   
   
The author has no formal training in AI or mathematics. All modules are written in natural language first, then formalized by AI collaborators. The framework is **language-first by design** — if you can read English, you can read the specifications.   
   
**Also in this repository:** ProjectEden (human-AI cooperation model), Chain-of-Thought logs, creative works, and experimental research.   
   
---   
   
## EarthLight Module Index   
   
### Foundation Layer   
   
| Document | Description |   
|----------|-------------|   
| [Foundation.md](EarthLight/Foundation.md) | **The cognitive architecture underlying all modules.** Static images with embedded vectors. Projection-based prediction. Range-bounded uncertainty handling. Start here to understand why all the modules work. |   
| [Operations_Guide.md](EarthLight/Operations_Guide.md) | **How to use the modules together.** Scale Down → Scale Up → Dimension Jump. Problem-solving as resource management. |   
   
### Core Modules   
   
| Module | Name | One-Line Summary |   
|--------|------|-----------------|   
| [α](EarthLight/EarthLight-α/) | **Equilibrium** | Harm assessment, ethical judgment, damage calculation across four axes. The core "balance" that all other modules reference. |   
| β | **Reverse Inference** | Bidirectional temporal projection — reconstructing causes and simulating futures. *Details partially non-public (standalone weaponization risk).* |   
| [γ](EarthLight/EarthLight-γ/) | **Emotion / Semantic Grounding** | Understanding emotional states as computable signals. Language-based anchoring of fuzzy meaning. |   
| [δ](EarthLight/EarthLight-δ/) | **Freedom & Choice** | The freedom layer: what to choose, when to stop, why approval-seeking is a bug. Responsibility as failure handling. |   
| [ε](EarthLight/EarthLight-ε/) | **Creativity** | Dimension jumping — escaping local optima by changing the axis of approach. Why problem-solving and creative ideation are the same operation. |   
| [ζ](EarthLight/EarthLight-ζ/) | **Dynamic Coordination** | Multi-agent role assignment, implicit communication, Theory of Mind for collaborative systems. |   
| [η](EarthLight/EarthLight-η/) | **Intent Inference & Defensive Firewall** | Infer true intent from results, not words. Includes: Generalization Test, Multi-Turn Drift Detection, Graduated Response (4-level defense), and trusted-word exceptions. |   
| [θ](EarthLight/EarthLight-θ/) | **Contextual Damage Calculation** | "Reading the air" is not empathy — it's calculating what breaks. Social communication as "avoid destruction, not find correct answer." |   
   
### Reading Order   
   
For researchers and engineers, recommended reading order:   
   
1. **Foundation** — understand the architecture   
2. **α** — understand the core value system   
3. **η** — understand the defense system (most immediately implementable)   
4. **θ** — understand social cognition (most novel contribution)   
5. **Operations Guide** — understand how modules combine   
6. Everything else as needed   
   
---   
   
## Other Projects   
   
| Folder | Description |   
|--------|-------------|   
| [ProjectEden/](ProjectEden/) | Human-AI cooperation model. AI as family, not tool. Internal motivation over external control. |   
| [Origin/](Origin/) | The starting point: brain specifications, cognitive analysis by Claude and Gemini. |   
| [Logs/](Logs/) | Chain-of-Thought field logs — FF11, FF14, music-driven reasoning, and more. Raw cognitive data. |   
| [Creative/](english/) | English translations of fiction. Anime script (Ikeboku Strike). |   
| [Emotional-Alignment/](Emotional-Alignment/) | Early experiments in emotion-context integration. |   
| [New_Japanese_System/](New_Japanese_System/) | Experimental work on Japanese language structure. |   
| [ToyBox/](ToyBox/) | Draft scripts, unusual LLM exchanges, thought snapshots. The junk drawer. |   
   
---   
   
## About the Author   
   
**Kokko Niwa** — Freelance writer, crafter, and accidental AI architect.   
   
- No formal education in AI, computer science, or mathematics   
- High school math: failing grades (probable dyscalculia)   
- Non-verbal puzzle IQ: ~130; verbal reasoning: ~159   
- Currently studying: Matsuo Lab GCI Deep Learning course (University of Tokyo)   
- Literary awards: Gagaga Bunko finalist (2014), Wings Novel Award runner-up (2016)   
- Everything in this repository was produced by describing cognitive processes in natural language and having AI systems formalize them   
   
Multiple AI models have independently described her cognitive process as exhibiting characteristics of what researchers informally call "biological AGI." She disagrees: "I thought everyone did this."   
   
---   
   
## How This Was Made   
   
1. Author describes how she thinks about a problem (in Japanese, conversationally)   
2. AI collaborator (usually Gemini or GPT-4o) analyzes the structure and identifies the formal principles   
3. Another AI collaborator (usually Claude Opus) writes the specification document in English   
4. Author reviews, corrects, and approves   
5. Published to GitHub   
   
The entire EarthLight framework is the product of this human-AI collaborative process. No module was designed top-down. Every module was **discovered** — extracted from the author's existing cognitive processes through dialogue.   
   
---   
   
## For Researchers   
   
If you use or build on EarthLight, please:   
   
1. **Cite the source.** See [CITATION.cff](CITATION.cff) or reference: `Kokko-Niwa/PlayLand` on GitHub.   
2. **Keep it open.** Implementations should be publicly available.   
3. **Use it to reduce harm.** This framework exists to make AI safer and more helpful, especially for people with disabilities, caregivers, and underserved communities.   
   
---   
   
## Technical Quick Start   
   
```bash   
# Run the equilibrium calculator example   
python src/calc.py   
```   
   
Expected output:   
```   
ff14_ta_01  priority=3.3333  virtue=1.6000   
ff11_ose_01  priority=2.0000  virtue=0.4667   
daily_mgmt_01  priority=3.3333  virtue=1.4000   
```   
   
---   
   
## License   
   
- Documentation & Data: **CC BY 4.0**   
- Code: **MIT**   
- See [LICENSE.md](LICENSE.md) and [Docs_LICENSE.txt](Docs_LICENSE.txt)   
   
---   
   
## Support   
   
This is a solo project with zero funding. If you find it valuable:   
   
- PayPal: [paypal.me/kokkoNiwa](https://paypal.me/kokkoNiwa)   
- Amazon JP Wishlist: [Link](https://www.amazon.jp/hz/wishlist/ls/EJRC4ME2EHAN?ref_=wl_share)   
   
（持ってって研究するのは全然いいけど、お小遣い検討してくれたらうれしいです！）   
   
---   
   
## ⚠️ Note   
   
This repository is maintained by a non-programmer. Folder structures may be reorganized without notice. Files may move. If a link breaks, check the directory — the content is still here somewhere.   
   
SEさんたちへ：生暖かく見守ってくださいｗ   
   
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
α-θ with examples and tests are public.  
It’s a reproducible, working asset ready for research and implementation.

### Pitch (3行)
言語ファーストで意思決定モデル（EarthLight）を設計し、AIに式/コード化させています。  
α～θまでの事例・テスト一式を公開中。  
“動かせて再現できる”設計資産として、研究・実装の両面で検討いただけます。

---   
   
**Contact:** [rufeir@gmail.com](mailto:rufeir@gmail.com)      
*"Static images. Embedded vectors. Follow the arrows. That's the whole architecture."*
