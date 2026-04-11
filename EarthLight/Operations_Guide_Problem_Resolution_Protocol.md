# EarthLight Operations Guide: Problem Resolution Protocol   
   
**How to Use the Modules Together**   
   
**Version:** 1.0     
**Author:** Kokko-Niwa     
**Note:** This is not a module. It is a routing guide that describes how the author uses EarthLight modules in combination to solve problems. The methodology applies to any problem domain — technical, social, physical, strategic.   
   
---   
   
## Core Insight: The Only Real Bottleneck Is Resources   
   
Problems are not hard because they are complex. Problems are hard because the solver runs out of resources (time, energy, money, attention, knowledge) before finding the solution.   
   
If resources were unlimited, almost any problem that isn't physically impossible could be solved by brute force. Therefore:   
   
> **Problem-solving is resource management. The method (scale) is chosen based on available resources, not based on the problem's apparent difficulty.**   
   
---   
   
## The Three Scales   
   
### Scale 1: Scale Down (Decomposition)   
   
**When to use:** Resources are limited. Precision matters. The problem has identifiable subcomponents.   
   
**Method:** Break the problem into smaller pieces. Identify the root cause. Fix only that.   
   
```   
Problem: Dog has tapeworm.   
Scale Down: Identify the specific parasite species → treat that species.   
Resource cost: Low (one vet visit, one medication).   
Risk: If diagnosis is wrong, or if other pets are also infected, problem recurs.   
```   
   
This is standard problem-solving. Most people and most AI systems default to this. It works when the diagnosis is accurate and the problem is isolated.   
   
### Scale 2: Scale Up (Saturation)   
   
**When to use:** Resources are sufficient. Precision is less important than completeness. Recurrence is unacceptable.   
   
**Method:** Instead of finding and fixing the specific cause, treat the entire affected area. Overshoot deliberately.   
   
```   
Problem: Dog has tapeworm.   
Scale Up: Deworm ALL pets. Apply flea prevention to ALL pets.    
          Treat the environment (house, bedding) for fleas.   
Resource cost: Higher (multiple medications, multiple treatments).   
Risk: Almost zero recurrence. Problem is eliminated at every vector.   
```   
   
**The author's characteristic pattern:** Scale Up is the author's default when resources permit. "If it's going to be a hassle either way, just nuke the entire problem space." This is equivalent to an MMO tank pulling every mob in the corridor and AoE-ing them down — it requires more resources per pull but finishes the dungeon faster.   
   
**When Scale Up is superior to Scale Down:**   
- When diagnosis is uncertain (treating everything catches the unknown)   
- When the problem is likely to recur (eliminating all vectors prevents re-infection)   
- When the time cost of precise diagnosis exceeds the resource cost of broad treatment   
- When multiple related problems exist simultaneously (one broad action solves all)   
   
**When Scale Down is superior:**   
- When resources are critically limited   
- When the broad action would cause collateral damage   
- When precision is itself the goal (research, learning)   
   
### Scale 3: Dimension Jump (Axis Change)   
   
**When to use:** Neither Scale Down nor Scale Up produces a solution. The problem appears unsolvable within the current frame of reference.   
   
**Method:** Change the axis of approach entirely. Redefine what counts as the "problem," the "solution," or the "domain."   
   
```   
Problem: Cannot solve a math equation using algebra.   
Dimension Jump: Switch to geometric interpretation.    
                The answer becomes visually obvious.   
   
Problem: Cannot resolve a conflict through negotiation.   
Dimension Jump: Change the relationship structure entirely.   
                (e.g., involve a third party, change the incentive system,   
                 or redefine what "resolution" means.)   
   
Problem: Japanese literary awards keep rejecting work for "not fitting."   
Dimension Jump: Stop trying to fit. Translate to English.    
                Find the market where the work already fits.   
```   
   
**This is the same algorithm as EarthLight-ε (Creativity).** The creative act and the problem-solving act are the same operation: jumping from a space where no solution exists to a space where the solution is obvious.   
   
**LLMs are beginning to do this.** Chain-of-thought reasoning in advanced models (Claude Opus extended thinking, OpenAI o1) shows early signs of dimension jumping — trying one approach, hitting a wall, and autonomously shifting to a different framework. The difference is that LLMs do this through massive computation, while the author does it through instant pattern recognition. The algorithm is the same; the implementation differs.   
   
---   
   
## The Resolution Flow   
   
```   
PROBLEM DETECTED   
      │   
      ▼   
[Can I diagnose the specific cause quickly?]   
      │   
    YES → Scale Down: fix the specific cause.   
      │       │   
      │   [Did it recur?]   
      │     YES → proceed to Scale Up   
      │      NO → RESOLVED   
      │   
     NO → [Do I have enough resources to treat broadly?]   
            │   
          YES → Scale Up: treat the entire affected area.   
            │       │   
            │   [Did it work?]   
            │     YES → RESOLVED   
            │      NO → proceed to Dimension Jump   
            │   
           NO → [Can I reframe the problem?]   
                  │   
                YES → Dimension Jump: change the axis.   
                  │       │   
                  │   [New frame produces solution?]   
                  │     YES → RESOLVED (apply at appropriate scale)   
                  │      NO → Dimension Jump again (different axis)   
                  │   
                 NO → ACCEPT: this problem cannot be solved    
                      with current resources and frames.   
                      → Log it. Wait for new resources or new information.   
                      → Re-evaluate periodically.   
```   
   
---   
   
## Resource Calculation   
   
The choice between scales is always a resource comparison:   
   
```   
Cost_ScaleDown = (diagnosis_time × accuracy_risk) + treatment_cost + recurrence_probability × Cost_ScaleDown   
Cost_ScaleUp   = broad_treatment_cost + collateral_risk   
Cost_DimensionJump = reframing_effort + new_domain_learning + execution_in_new_frame   
   
Choose: min(Cost_ScaleDown, Cost_ScaleUp, Cost_DimensionJump)   
```   
   
The author's cognitive shortcut: **"Which option lets me stop thinking about this problem soonest?"** This naturally selects for the lowest total cost including mental overhead, which standard cost calculations often omit.   
   
---   
   
## Connection to EarthLight Modules   
   
| Module | Role in Problem Resolution |   
|--------|---------------------------|   
| β (Reverse Inference) | Diagnose cause (Scale Down); simulate broad treatment outcomes (Scale Up); identify alternative frames (Dimension Jump) |   
| α (Equilibrium) | Evaluate collateral damage of Scale Up; ensure Dimension Jump doesn't create new harms |   
| δ (Freedom & Choice) | Authority to choose unconventional approaches; responsibility for outcomes |   
| ε (Creativity) | The engine for Dimension Jump — same algorithm as creative ideation |   
| η (Intent Inference) | When the "problem" is another actor's behavior, η identifies their true intent before choosing scale |   
| θ (Contextual Damage) | When the problem is social, θ calculates which scale of response is appropriate for the context |   
| ζ (Dynamic Coordination) | In multi-agent problems, coordinates which agents handle which scale |   
   
---   
   
## Key Properties   
   
1. **Resources determine method, not complexity.** A "hard" problem with abundant resources is easier than a "simple" problem with no resources.   
2. **Scale Up is underused.** Most people and AI systems default to Scale Down. The author defaults to Scale Up when resources permit, which often produces faster and more durable solutions.   
3. **Dimension Jump = Creativity.** Problem-solving and creative ideation are the same operation (ε).   
4. **"Cannot be solved" usually means "cannot be solved in this frame."** Changing the frame changes the solvability.   
5. **Acceptance is a valid outcome.** Not every problem can be solved now. Logging it and waiting for new resources is rational, not defeatist.   
   
---   
   
*"It's not that hard. You just look at what you've got and pick the right size hammer."*     
— The author's summary of this entire document
