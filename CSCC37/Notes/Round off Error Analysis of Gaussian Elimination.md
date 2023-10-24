## Factorization $PA = LU$
Because of rounding errors (both initial and propagated), we actually get $\hat{L}, \hat{U}, \hat{P}$ such that:
$$
\hat{P}(A + E) = \hat{L}\hat{U}
$$
$E$ is the error from factorization.
The elements are perturbed due to the operations and round off error. We are hoping that these perturbations are small (near machine epsilon or multiples of it). Example:
$$
U = 
\begin{bmatrix}
0 & 1 \\
1 & 2
\end{bmatrix}, ~
\hat{U} = 
\begin{bmatrix}
0 & 1-\epsilon \\
1 & 2+\epsilon
\end{bmatrix}
$$
$P$ is only a permutation matrix, however due to round off error, it may cause incorrect permutations.
> We are hoping **that $||E||$ is small compared to $||A||$** (if we pivot during the factorization).

## Solve forward and backward
Can introduce more roundoff error, but this can be represented as: $$(A+\tilde{E})\hat{x} = b$$$\tilde{E}$ is the error from forward and back solve, where $\tilde{E}$ is slightly different than $E$.
Usually we drop distinction and consider them the same.
$$
(A+E)\hat{x} = b
$$
$\hat{x}$ is a computed solution, but not necessarily that of the original problem (unless $E$ is 0 which it probably isn't).
___
**Equivalently**, let $E\hat{x} = r$ $$
\begin{align}
(A+E)\hat{x} = b \iff r = b - A\hat{x}
\end{align}
$$Where $r$ is the difference between the true and computed solution, the **residual**.
## Is $||E||$ small compared to $||A||$?
If we use row partial pivoting during the factorization, we can show that (outside of scope) $$
||E|| \lessapprox k \epsilon ||A||
$$where $k$ is:
- not too large
- grows with size of $A$
- depends on pivoting strategy
- does not dominate $\epsilon$

Similarly, for the residual $$
||r|| \lessapprox k \epsilon ||b|| \iff \frac{||r||}{||b||} \lessapprox k \epsilon
$$
where $\frac{||r||}{||b||}$ is called the relative residual. We can see that the residual is also close to machine epsilon.
## Is $\frac{||\hat{x} - x||}{||x||}$, Relative Error Small?
There is a difference between residual being small and error being small.
**Note:** We don't know the true solution $x$
#### Example showing difference
$$
\begin{bmatrix}
0.780 & 0.563 \\
0.913 & 0.659
\end{bmatrix}
x = 
\begin{bmatrix}
0.217 \\
0.254
\end{bmatrix}
$$
> [!warning]- We know the true solution is
> $x =\begin{bmatrix}1 \\-1\end{bmatrix}$.

Consider the computed solutions (using some black box algorithms):
$$
\hat{x}_\alpha =
\begin{bmatrix}
0.999 \\
-1.001
\end{bmatrix},
\hat{x}_\beta =
\begin{bmatrix}
0.341 \\
-0.087
\end{bmatrix}
$$
We calculate residuals
$$
\begin{align}
r_\alpha = b - A\hat{x}_\alpha =
\begin{bmatrix}
-0.001243 \\
-0.001572
\end{bmatrix} \\
r_\beta = b - A\hat{x}_\beta =
\begin{bmatrix}
-0.000001 \\
0
\end{bmatrix}
\end{align}
$$
From this, it looks like $r_\beta$ is the better solution (when it is not).
However the relative error is much smaller for $\hat{x}_\alpha$.
## Relationship between relative error and relative residual
When does a small relative residual (which is guaranteed if we use row partial pivoting) guarantee a small relative error?
How do we check if we have an actual solution (solution accuracy)?