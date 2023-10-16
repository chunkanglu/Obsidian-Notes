## What are Optimization Problems
- Given input, find output that:
	- satisfies constraints
	- optimizes the objective function (for optimal solution)

## How Greedy works
- Greedily (myopically only looking one step ahead) extends partial solution at incrementally, irrevocably (does not go back/backtrack)

## Applications
- Scheduling
- Graph (MST, Dijkstra)
- Approximation

## Interval Scheduling (KT 4.1)
Input: Set of $n$ intervals (jobs)
Interval $i$: start time $s(i)$, finish time $f(i) > s(i)$

Intervals $i, j$ overlap if their intervals contain more than 1 point in common
**Feasible**: set of intervals where no two overlap

> **Max Cardinality Set** is a set that cannot be extended
> But a set cannot be extended is not max cardinality

Output: Max carnality feasible subset of input (biggest set of jobs that can be done with the machine that do not overlap
#### Algorithm
1. Sort intervals in *some order*
2. Start with trivial empty solution A
3. For each job i in sorted order
	1. if i overlaps no interval in A, then add to A
4. Return A

##### Defining some order
###### Try 1: Increasing start time (DNW)
- Fails if the longest interval is longer than the allotted time
###### Try 2: Increasing length (DNW)
- One bad short interval can rule out 2 longer ones (conflicting with more than 1 interval)
###### Try 3: Increasing number of overlaps (DNW)
###### Try 4: Increasing finish time
- Keep track of finish time F of last job in A
- Check if $s(i) \ge F$
- Time Complexity: $O(nlogn)$
	- Sort intervals $O(nlogn)$
	- Loop $n$ times, with each check $O(1)$
### Proof: Promising set approach
Claim 1: for every iteration t, there exists optimal set A*, such that $A_t$ is included in some optimal set $A_t \subset A_t^*$

Induction on t:
Basis: t = 0 trivially true
IS: Suppose t is true, an optimal set includes $A_t$. Show this holds for $A_{t+1}$
- Case 1: $A_{t+1} = A_t$, same optimal set is used, no change
- Case 2: $A_{t+1} = A_t union \{i\}$ 
	- If $j$ is in optimal, then no change
	- If $i not A_t^*$, Special case
Thus A at the end of the algorithm is optimal
###### Special Case 
$j$ was added in iter $i$, $j \notin A_i^*$.
$J$ must overalap with at least 1 interval in $A_i^*$ for it to not be in the optimal set.
$j$ cannot overlap 2 intervals $j', j''$ in $A_i^*$ or else it would be in this configuration $s(j') < s(j) < f(j') < s(j'') < f(j) < f(j'')$ but in this case $j'$ finishes first and should be the one considered instead of $j$ by the greedy algorithm in this iteration.
Thus $j$ only overlaps with some interval $j* \in A_i^*$ and we can construct $A_{I+1}^* = A_i^* - \{j*\} + \{j\}$.

By claim, we know $A_n \subseteq A^*$ . Suppose $A_n \subset A^*$. This means there exists some $j \in A^* - A$ that does not overlap with any interval in $A^*$ due to feasibility. It also cannot overlap with any interval in $A_n$ since it is a perfect subset of $A^*$. Thus the algorithms must have considered it and be added to $A_n$, contradicting that $j \notin A$ and $A_n = A%*$.


i must overlap at least 1 job in optimal set (since it would already be in optimal)
i cannot overlap 2 jobs in optimal (since we sort in increasing finish times)
Thus, i overlaps exactly one job i* (that is right before j) in optimal
- Construct new optimal by removing i* and adding i
- $A_{t+1}^* = A_t^* - i^* + i$

###### Proof
Finish set is a subset of optimal, and optimal set cannot contain more jobs

### Greedy stays ahead
Claim 2: A is always feasible

Let i_1, i_2, ..., i_k be jobs in A in left-to-right order (in the order the jobs were added to set A)
Let i_1*, ..., i_m* be jobs in some optimal A* in left-to-right order
Claim 3: $\forall t \in [1..k], finish(i_t) \le f(i_t*)$
Proof: Induction on t
Basis: t = 1 trivially true, always choose first one
IS: Assume $f(i_t) \le f(i_t*)$ from 1 up to t, show it holds for $t+1$
Assume for contradiction, not true at t+1


## Max Weight Interval Scheduling
Instead of all jobs same weight and having the most, we want the optimal with largest sum of weights.
No greedy algo for this, but dynamic programming can.


## Smallest Number of Machines to schedule all jobs

