---
tags:
  - CSCC37
---
# Types of Approximation
## Polynomial Interpolation
Find polynomial $p(x)$ such that $p(x_i) = f(x_i); i = 0, 1, \ldots, n$ where $f$ is the *underlying function* of the data

Consider $\mathcal{P}_n = \{ \text{polynomials of degree} \le n \}$
$\mathcal{P}_n$ is a function space of dimension $n+1$
One possible basis is $\{ x^i : i = 0, 1, \cdots, n \}$, monomial basis.
Clearly, $\{ x^i : i = 0, 1, \cdots, n \}$ **spans** $\mathcal{P}_n$ and $\{ x^i : i = 0, 1, \cdots, n \}$ are **independent**
$$
\sum_{i = 0}^{n} a_i x_i = 0, \forall x \implies a_i = 0,  \forall i
$$
Note: can shift the monomial basis $\{ (x-c)^i : i = 0, 1, \cdots, n \}$
### Do approximating or interpolating polynomials exist?
> **Weierstrass Theorem:**
> If $f \in C[a, b]$ is $C_0$ continuous in $[a, b]$, then $\forall \epsilon > 0,  \exists p_\epsilon \text{ st. } ||f - p_\epsilon||_\infty < \epsilon$
> ie. You can always approximate any function with a polynomial.
### Numerical Methods for Polynomial Interpolation
#### Vandermonde (Method of Undetermined Coefficients)
> **Theorem:**
> For any sets $\{ x_i : i = 0, 1, \cdots, n \}, \{ y_i : i = 0, 1, \cdots, n  \}$ where $x_i$ are distinct, $y_i$ not necessarily distinct (it is an injection), $\exists$ a unique polynomial $p(x) \in \mathcal{P}_n$ such that $p(x_i) = y_i$
> ie. A unique degree $n$ polynomial can be made to fit $n + 1$ points.
> *Algorithm & Proof:*
> If $p(x)$ exists, it must be possible to write it as $p(x) = \sum_{i = 0}^{n} a_i x_i$ with $n+1$ unknowns being the coefficients $a_i$.
> Need $n+1$ equations to find the $a_i$.
> Convert to a matrix/vector problem
$$
\begin{cases}
p(x_0) = y_0 \\
\vdots \\
p(x_n) = y_n
\end{cases}
\implies
\begin{bmatrix}

\end{bmatrix}
\begin{bmatrix}
a_0 \\
a_1  \\
\vdots \\
a_n
\end{bmatrix}
= 
\begin{bmatrix}
y_0 \\
y_1  \\
\vdots \\
y_n
\end{bmatrix}
$$
## Data Fitting
Least squares approximation
Find $p(x)$ that minimizes the distance to the $f$ which is $||f - p||_2$ (2-norm euclidean distance)
#### Norm of a Continuous function
$$
\begin{align}
&||f - p||_2 = \sqrt{\int_{a}^{b} \left( f(x) - p(x) \right)^2 dx} & \text{least squares approx} \\
&||f - p||_\infty = \max_{a \le x \le b} \left| f(x) - p(x) \right| & \text{min max problem} \\
&||f - p||_1 = \int_{a}^{b} \left| f(x) - p(x) \right| dx
\end{align}
$$
## Truncated Taylor Series
- Leaves off remainder term
$$
\begin{align}
f(x) &= f(a + x-a) \\
p(x) &= f(a) + f'(a)(x-a) + \ldots + \frac{f^{(n)}(a)}{n!} (x-a)^n & \text{truncated taylor} \\
e(x) &= f(x) - p(x) = \frac{f^{(n+1)}(\eta)}{(n+1)!} (x-a)^{n+1} & \text{error term}
\end{align}
$$
