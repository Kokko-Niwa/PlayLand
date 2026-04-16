# EarthLight Foundation — Operational Notes   
   
**How Vector Resources Are Allocated in Practice**   
   
**Version:** 1.0     
**Author:** Kokko-Niwa     
**Origin:** Dialogue with GPT-5.4 (2026-04-16). The author described how she decides which objects to track with full vector information and which to ignore. The resulting rules turned out to be a practical attention-allocation algorithm.   
   
---   
   
## Context   
   
The [Foundation](Foundation.md) document describes the core architecture: static images with embedded vectors. But it doesn't address a critical practical question:   
   
> **If everything has a potential vector, how do you avoid tracking everything?**   
   
The answer: you don't track everything. You apply a two-stage filter that drastically reduces the number of active vectors at any moment. This is how the architecture stays lightweight.   
   
---   
   
## Stage 1: Object Classification (Attention Tiering)   
   
Before any vector is computed, objects are classified by their **potential for unpredictable motion**. This determines their initial monitoring level.   
   
| Class | Initial Monitoring | Why |   
|-------|-------------------|-----|   
| **Inorganic objects** | Ignore unless moving or likely to move | Physics is predictable. A rock stays a rock. A landslide gets full attention. |   
| **Machines** | Treat as potentially dynamic | A machine is an inorganic object that can suddenly become active. Inactive machine = inorganic. Active machine = tracked. |   
| **Plants** | Same as inorganic | Change rate is too slow for real-time decision-making. A tree doesn't move on human timescales. |   
| **Animals** | Partial monitoring by default | Self-directed motion with high prediction error. You don't know where a dog will go next. |   
| **Humans** | Full monitoring when interacting | Highest unpredictability. Multiple vector dimensions (physical, social, intentional). |   
   
**The classification criterion is NOT "alive vs. not alive."** It is **"how unpredictably does this thing move, and how fast?"** A plant is alive but doesn't move on relevant timescales, so it gets the same treatment as a rock. A turned-off machine is inorganic in practice; a turned-on machine is a tracked entity.   
   
### Why This Matters for AI   
   
Current AI systems either:   
- Track everything equally (expensive, most of the computation is wasted on static objects)   
- Use fixed attention patterns (miss important changes in "low-priority" areas)   
   
The tiering system pre-filters what deserves computational resources based on **motion potential**, not category labels. This is similar in spirit to event cameras (which only process pixels that change) and sparse attention mechanisms (which only compute attention for high-salience tokens).   
   
---   
   
## Stage 2: Personal Impact Filter   
   
After classification, a second filter applies:   
   
```   
Does this object's motion affect me (or what I care about)?   
  YES → Monitor actively, maintain full vectors   
  NO  → Ignore, or store only coarse position   
```   
   
This is not selfishness — it's resource management. The author's system has finite processing capacity (as does any system). Allocating vector resources to objects that cannot affect the current situation is waste.   
   
**"Affect me" includes indirect effects.** If an object doesn't threaten the author directly but threatens someone she's responsible for, or disrupts a system she depends on, it gets monitoring. The calculation is: **does this object's trajectory intersect with anything I need to protect?**   
   
---   
   
## Combined Filter: The Full Selection Process   
   
```   
For each object in the environment:   
   
1. CLASSIFY: What type is it?   
   Inorganic/Plant → LOW (track only if visibly moving)   
   Machine (off)   → LOW   
   Machine (on)    → MEDIUM   
   Animal           → MEDIUM   
   Human            → HIGH (when interacting)   
   
2. IMPACT CHECK: Does its trajectory affect me or mine?   
   YES → Promote to ACTIVE. Assign full vector (direction + magnitude).   
   NO  → Keep at current level or DEMOTE to dormant.   
   
3. RESOURCE ALLOCATION:   
   ACTIVE objects  → Full vector tracking, continuous update   
   MEDIUM objects  → Periodic check, coarse vector   
   LOW/DORMANT     → Position only, no vector computation   
      
4. TRANSITION DETECTION:   
   If a DORMANT object starts moving → re-evaluate (go to Step 1)   
   If an ACTIVE object stops mattering → demote (save resources)   
```   
   
**This is a living process.** Objects constantly shift between levels. A parked car (LOW) starts moving toward you (→ ACTIVE). A person in conversation (ACTIVE) walks away (→ demote). The system re-evaluates whenever it detects state changes.   
   
---   
   
## Extension to Social Space   
   
The same tiering system applies to social entities, but the "motion" being tracked is **influence, power, and intentional direction** rather than physical movement.   
   
### Social Vector Processing   
   
| Physical Space | Social Space |   
|---------------|-------------|   
| Object position | Person's role/status |   
| Physical velocity | Direction of influence (who are they pushing/pulling?) |   
| Physical force | Strength of influence (how much can they change?) |   
| Collision prediction | Conflict/damage prediction |   
| "Does it affect me?" | "Does their influence reach me or mine?" |   
   
### Authority as Vector, Not Label   
   
The author reports that she does not process "authority" as a meaningful input:   
   
> "I don't understand authority. It has no force toward me. It disrupts equilibrium."   
   
What she processes instead:   
   
- **Where is this person's influence directed?** (vector direction)   
- **How strong is that influence?** (vector magnitude)   
- **Does it reach me?** (impact filter)   
- **Does it disturb the overall balance?** (α check)   
   
This means:   
   
```   
A person with high authority but no vector toward you = IGNORE   
A person with low authority but strong vector toward you = MONITOR   
A person with high authority and strong vector toward others =    
  CALCULATE (their influence trajectory affects the system you're in)   
```   
   
**"Authority" is not treated as "correctness."** A powerful person's statement is not weighted more heavily because they are powerful. It is evaluated by the same vector + damage calculation as anyone else's. However, the **damage potential** of a powerful person's actions is larger, because their influence vectors reach more people.   
   
This directly connects to α (Equilibrium): accumulated advantages (E_i) don't make actions more correct — they make harmful actions more damaging.   
   
### Practical Result   
   
The author can simultaneously:   
- Ignore a CEO's opinion when it doesn't affect her   
- Calculate the precise impact of that CEO's decision on a system she cares about   
- Predict where the resulting damage will land   
- Act to protect affected parties   
   
All without ever processing "this person is important, therefore I should listen." The importance is derived from influence vectors, not from labels.   
   
---   
   
## Implementation Considerations for AI   
   
GPT-5.4 noted (in the dialogue that produced this document) that the core ideas align well with current research directions:   
   
1. **Sparse state representations** — not all objects need equal computational attention   
2. **Salience-based resource allocation** — compute budget follows importance, not position   
3. **Event-driven updates** — process changes, not static states   
4. **Dormant object management** — store cheaply, re-activate when relevant   
   
The gap between the author's cognitive process and AI implementation is primarily in:   
   
- **Transition detection:** How does the system notice that a dormant object has become active? (The author does this intuitively; AI needs explicit triggers.)   
- **Salience scoring:** What makes something "likely to move strongly soon"? (The author uses experience-calibrated intuition; AI needs a learnable scoring function.)   
- **Cross-domain transfer:** How do physical-space tiering rules translate to social-space tiering? (The author does this seamlessly; AI needs explicit mapping.)   
   
These are engineering problems, not conceptual problems. The architecture is sound; the implementation details require research.   
   
---   
   
## Connection to Foundation and Other Modules   
   
| This document clarifies... | In relation to... |   
|---------------------------|-------------------|   
| **Which objects get vectors** | Foundation's "static images with embedded vectors" — not ALL objects get vectors |   
| **How to stay lightweight** | Foundation's "extremely lightweight" claim — this is the mechanism |   
| **What "ignore" means** | Foundation's "range-and-retroact" — dormant objects can be re-activated |   
| **Social vector processing** | θ (contextual damage) and η (intent inference) — both operate on social vectors |   
| **Authority handling** | α (equilibrium) — authority ≠ correctness; influence is computed, not assumed |   
   
---   
   
*"Track what moves. Ignore what doesn't. If something starts moving, track it then. That's the whole attention system."*
