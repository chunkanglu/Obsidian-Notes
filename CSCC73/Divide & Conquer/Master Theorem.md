We can model divide and conquer steps of an algorithm using the following recurrence.
$$
\begin{equation}
	T(n) = 
	\begin{cases}
		aT(\frac{n}{b}) + c n^d & \text{non-base case} \\
		x & \text{base case}
	\end{cases}
\end{equation}
$$
We split the original problem into $a$ subproblems to be recursively solved, each of size $\frac{n}{b}$. Each time we recursively solve, the input is reduced to a fraction of the original, hence the $log$ complexity. Then the results are combined in some polynomial fashion.

The Master Theorem is as follows for a divide an conquer algorithm with recurrence $T(n)$:
$$
\begin{equation}
	T(n) = 
	\begin{cases}
		\Theta(n^d) & a < b^d \text{ (dominated by merge step)} \\
		\Theta(n^d \log{n}) & a = b^d \text{ (bit of both)}\\
		\Theta(n^{\log_{b}{a}}) & a > b^d \text{ (dominated by recursive calls)}
	\end{cases}
\end{equation}
$$
