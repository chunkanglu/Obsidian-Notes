We have $n$ jobs, each with a duration $t(i)$ and deadline $d(i)$. All jobs must start at or after release time $r$. We want to minimize the maximum lateness over all jobs (ie. $\sum_{\forall i} \max{(start(i)+t(i)-d(i), 0)}$). 

```
MINLATENESS(t[1..n], d[1..n], r):
S := []
Sort jobs in t, d in increasing deadline
next_start := r
for each job:
	S.append(next_start)
	next_start := next_start + t[job]
Return S
```
Intuition is to do jobs one after another in the order of deadline.

All optimal schedules have no gaps (jobs are one after another). 
- You can always decrease total lateness by shifting jobs to the left to remove the gaps

We define an inversion between two schedules $S_1, S_2$ if there exists a pair of elements $i, j$ that are in opposite order in the two schedules.
Let $S$ be the output of the algorithm.  Let $S*$ be an optimal schedule that has the fewest number of inversions relative to $S$. We will show by exchange argument that we can get no worse total lateness by modifying $S*$ reducing the number of inversions in $S*$.
If $S*$ has zero inversions, then $S* = S$ and $S$ is optimal.
Suppose for contradiction $S*$ has at least 1 inversion. We will show that this case is not possible. Let $i', j'$ be the elements in $S*$ causing an inversion. 
