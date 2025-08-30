# Backcasting (β) — Skeleton

Reasoning from the **desired goal** back to the present, scoring plans by reachability and value under constraints.

- **Goal**: \(G\)  **Current**: \(S\)  **Constraints**: \(\Theta\)  **Cost**: \(K\)  
- **Reachability**: \(F(S\!\to\!G \mid \Theta)\)  **Value**: \(V(G)\)

\[
\mathrm{BackcastScore}= \frac{F \cdot V}{K + \varepsilon}
\]

**Operational integration.**  
1) Rank candidate plans by **BackcastScore**.  
2) For the shortlisted options, apply **α (Priority/Virtue)** to decide *who* should do *what* and *when*.

## Mini example
Target \(G\): “ship a 5-min pilot episode in 2 weeks”;  
Constraints \(\Theta\): single animator, volunteer VA, simple facial rigs;  
Then raise \(F\) for paths that reuse templates and keep \(K\) (time/coordination) small; finally route tasks by α.


# 逆算推論 — Skeleton

- Goal: G, Current: S, Constraints: Θ, Cost: K
- Reachability F(S→G|Θ), Value V(G)

\[
\mathrm{BackcastScore}= \frac{F \cdot V}{K + \varepsilon}
\]

実運用: まず BackcastScore で候補を絞り、残りに Priority/Virtue を適用。

