---
tags:
  - CSCC37
---
Can we improve $\hat{x}$ (at a reasonable cost) after getting some perturbed solution from trying to solve $Ax = b$, but actually getting $(A+E)\hat{x} = b$. See [[Round off Error Analysis of Gaussian Elimination]].
$$
\begin{align}
\begin{cases}
Ax &= b \\
A\hat{x} &= b - r \\
\end{cases}
\implies A(x - \hat{x}) &= r & \text{ let $z = x - \hat{x}$}
\end{align}
$$
So we now solve $Az = r$ (pretty quickly if we already did an LU factorization on A).
$$
z = x - \hat{x} \iff x = \hat{x} + z
$$
We try to use $z$ as a **correction vector** with the original computed solution to get the true solution.
Problem is we get $\hat{z}$ instead of $z$ when we compute $Az = r$ for the same reason our $\hat{x}$ is inaccurate.
- **High level:** If we get say at least 2 leading digits correct in $\hat{x}$, we will get 2 digits correct in $\hat{z}$ and then have 4 leading digits correct in $\hat{x} + \hat{z}$. Keep repeating, to iteratively get more correct.
> [!warning] If the matrix is very poorly conditioned, then this will not work.
## Algorithm
Compute $\hat{x}^{(0)}$ by solving $Ax = b$
For $i = 0, 1, 2, \ldots$ until solution is *good enough* (or convergence failure):
	Compute $r^{(i)} = b - A\hat{x}^{(i)}$
	Solve $Az^{(i)} = r^{(i)}$ for $\hat{z}$
	Update $\hat{x}^{i+1} = \hat{x}^{i} + \hat{z}^{i}$
	