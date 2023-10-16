Given some 2D plane with points, we want to find the pair with the shortest Euclidean distance. That is some $(p, p') st. p, p' \in P \text{ and } \forall q, q' \in P, \sqrt{(x_q-x'_q)^2 + (y_q-y'_q)^2} \ge \sqrt{(x_p-x'_p)^2 + (y_p-p'_q)^2}$

# Idea
The idea is to split the input space into 2 halves vertically with the middle being between the middle two elements in $P$ when sorted horizontally. We either have the closest pair have both points in either half, or one is in the left and one is in the right. 
For ones in each half, we recursively solve as a subproblem. 
To check the pair which cross the border, we do the following:

Let $\delta$ be the smallest distance for the pairs found in both halves. For pairs crossing the border, we only need to consider the elements that are at most $\delta$ away from the border, as we want to find a pair with a distance less than $\delta$. Also consider that for each point in this $2\delta$ wide strip, we only need to look at points that are at most $\delta$ away from it vertically. If we look at these points from bottom to top, we only need to consider a $2 \delta \times \delta$ size rectangle for each point for candidates that have a smaller distance.

For each point, we only need to check at most 7 points. If we divide the rectangle into squares of $\frac{\delta}{2} \times \frac{\delta}{2}$, notice that there are 8 squares, and each of them can only contain at most 1 point. This is because we already know that the minimum distance between these points is at least $\delta$ by construction. As the point we are checking for pairs occupies one of these squares, there are only 7 other candidates to check for.
> Technically there can be less since we are repeating some calculation for points on the same side with the one we are considering, but differentiating the logic for the current point being left/right of the middle takes a lot more needless effort without improving the asymptotic complexity of the algorithm.

Repeat for all points in the strip, and we return the pair with the smallest distance

# Algorithm
```
CLOSESTPAIR(P):
P_x := list of points in P sorted by x-coordinate
P_y := list of points in P sorted by y-coordinate
return RCP(P_x, P_y)

RCP(P_x, P_y):
if len(P_x) <= 3:
	calculate all pairwise distances and return smallest
else:
	L_x := P_x[:n/2]
	R_x := P_x[n/2:]
	m := (max_x_coord(L_x) + min_x_coord(R_x)) / 2
	L_y := sublist of P_y with points in L_x
	R_y := sublist of P_y with points in R_x
	(p_l, q_l) := RCP(L_x, L_y)
	(p_r, q_r) := RCP(R_x, R_y)
	delta := min(dist(p_l, q_l), dist(p_r, q_r))
	(p*, q*) := corresponting pair with min dist
	B := sublist of P_y with points at most delta away from m
	for each of p in B in order (bottom-top):
		for each of (up to) next 7 points q after p in B:
			if dist(p, q) < dist(p*, q*): update (p*, q*)
	return (p*, q*)
```
# Runtime
##### RCP
Everything (excluding the recursive parts) up to the `for` loops can each be done in $O(n)$ time.
The `for` loops are $O(7n) = O(n)$.
We solve 2 subproblems each of size $\frac{n}{2}$.
$$
T(n) = 2T(\frac{n}{2}) + cn = \Theta(n \log{n})
$$
##### CLOSESTPAIR
Each sort is $O(n \log{n})$.
RCP is also $O(n \log{n})$ from above.

>**Thus total complexity is** $O(n \log{n})$.