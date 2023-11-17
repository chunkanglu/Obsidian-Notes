---
tags:
  - CSCC37
---
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
This can be proved but is very technical and outside the scope of the course.
## Is $\frac{||\hat{x} - x||}{||x||}$, Relative Error Small?
There is a difference between residual being small and error being small.
> [!error] Problem is, we don't know the true solution $x$
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
From this, it looks like $r_\beta$ is the better solution *(when it is not)* since $\frac{||r_\beta||}{||b||}$ is much smaller.
However the relative error is much smaller for $\hat{x}_\alpha$.
## Relationship between relative error and relative residual
When does a small relative residual (which is guaranteed if we use row partial pivoting) guarantee a small relative error?
How do we check if we have an actual solution (solution accuracy)?

We currently have:
$$
\begin{cases}
A\hat{x} &= b - r \\
Ax &= b
\end{cases}
$$
$$
\implies A(x - \hat{x}) = r \iff (x-\hat{x}) = A^{-1}r
$$
$$
\begin{align}
||x - \hat{x}|| = ||A^{-1}r|| &\le ||A^{-1}||~||r|| & \text{ Equation 1} \\
b = Ax \iff ||b|| = ||Ax|| \le ||A||~||x|| \iff \frac{1}{||b||} &\ge \frac{1}{||A||~||x||} & \text{ Equation 2}
\end{align}
$$
Combining Equations 1 and 2:
$$
\frac{||x - \hat{x}||}{||A|| ~ ||x||} \le \frac{||A^{-1}|| ~ ||r||}{||b||}
$$
$$
\frac{||x - \hat{x}||}{||x||} \le \frac{||A|| ~ ||A^{-1}|| ~ ||r||}{||b||} = cond(A) \frac{||r||}{||b||}
$$
$cond(A) = ||A||||A^{-1}||$ is the **condition number** of a matrix with respect to some norm.
- It amplifies the relative error upper bound, so even if residual is small, if condition number is large the relative error will become large.
- Conversely is $cond(A)$ is not too large, then the problem is well conditioned and a small relative residual is a reliable indicator of a small relative error.
- Conditioning is a continuous spectrum, how large is *"very large"* depends on context.
> **Note:** $1 = ||I|| = ||A A^{-1}|| \le ||A|| ||A^{-1}|| = cond(A)$ So condition number is always $\ge 1$.
#### Using Previous Example
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
$$
A = 
\begin{bmatrix}
0.780 & 0.563 \\
0.913 & 0.659
\end{bmatrix}
, ~
A^{-1} = 
\frac{1}{10^6}
\begin{bmatrix}
0.659 & -0.563 \\
-0.913 & 0.780
\end{bmatrix}
\text{ using}
\left(
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}^{-1} = 
\frac{1}{det(A)}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
\right)
$$
$$
\begin{align}
&||A||_{\infty} = 1.572 \\
&||A^{-1}||_{\infty} = 1.693 \times 10^6 \\
\end{align}
$$
$$
\begin{align}
\implies cond_{\infty}(A) &= ||A||_{\infty}||A^{-1}||_{\infty} \\
&= 2.66 \times 10^6
\end{align}
$$
$$
\frac{||x - \hat{x}|}{||x||} \le 2.66 \times 10^6 \frac{||r||}{||b||}
$$
The relative error in $x$ could be as much as $2.66 \times 10^6$ times the relative residual. This is a poorly conditioned problem so relative residual is **not** a reliable indicator of relative error.
##### Geometric Interpretation of $cond(A)$
Geometrically, we can represent this as $0.780x_1 + 0.563x_2 = 0.217$ and $0.913x_1 + 0.659x_2 = 0.254$.
These two lines are nearly parallel, so any small change would cause a large shift in the intersection point.
> $cond(A)$ is essentially the degree of how parallel the lines (or planes in $\mathbb{R}^3$ or hyperplanes in higher dimension) are. Conversely, smaller $cond(A)$ is the orthogonality of the lines.
#### Different Example
$$
A =
\begin{bmatrix}
c & s \\
-s & c
\end{bmatrix}
\text{ where } c^2 + s^2 = 1 \text{ (eg. $c = \cos \theta, s = \sin \theta$ for any $\theta$)}
$$
$$
A^{-1} =
\frac{1}{c^2 + s^2}
\begin{bmatrix}
c & -s \\
s & c
\end{bmatrix}
=
\begin{bmatrix}
c & -s \\
s & c
\end{bmatrix}
= A^{T}
$$
$A$ is an orthogonal matrix. Let us use the 2-norm. 
$$
\begin{align}
||A||_2  &\stackrel{\text{def}}{=} \sqrt{e(A^{T}A)} \text{ where $e$ is the spectral radius} \\
&= \sqrt{e(I)} \\
&= 1 \\
\end{align}
$$
$$
\begin{align}
||A^{-1}||_2  &= \sqrt{e((A^{-1})^{T}A^{-1})} \\
&= \sqrt{e(AA^{-1})} \\
&= \sqrt{e(I)} \\
&= 1 \\
\end{align}
$$
$$
cond_2(A) = ||A|_2|||A^{-1}||_2 = 1
$$
So it is perfectly well conditioned.
$$
\frac{||x|| - \hat{x}||_2}{||x||_2} \le \frac{||r||_2}{||b||_2}
$$
> Relative residual **is** the upper bound for relative error for these ***perfectly well conditioned*** systems.

##### Geometric Interpretation
![[geometric_cond]]
# Making Error Better
[[Iterative Refinement of Linear System Solution]]