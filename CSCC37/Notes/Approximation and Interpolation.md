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
> Relevant: [[#Norm of a Continuous function]]
> ie. You can always approximate any function with a polynomial.
### Numerical Methods for Polynomial Interpolation
#### Vandermonde (Method of Undetermined Coefficients)
> **Theorem:**
> For any sets $\{ x_i : i = 0, 1, \cdots, n \}, \{ y_i : i = 0, 1, \cdots, n  \}$ where $x_i$ are distinct, $y_i$ not necessarily distinct (it is an injection), $\exists$ a unique polynomial $p(x) \in \mathcal{P}_n$ such that $p(x_i) = y_i$
> ie. A unique degree $n$ (or less) polynomial can be made to fit $n + 1$ points.
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
1 & x_0^1 & x_0^2 & \cdots & x_0^n \\
1 & x_1^1 & x_1^2 & \cdots & x_1^n \\
\vdots \\
1 & x_n^1 & x_n^2 & \cdots & x_n^n
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
The matrix is a Vandermonde matrix.
Question: Is this matrix $V$ nonsingular/invertible?
- Yes since columns are independent
- Alt Common proof
	- $V$ singular $\iff \exists a \ne 0 \text{ st. } Va = 0$ 
	- Going back to polynomials, this is equivalent to $p(x_i) = 0, i = 0, 1, \cdots, n \implies$ $p$ has $n + 1$ roots, but $p(x) \in \mathcal{P}_n \implies p(x) = 0, \forall x$ by Fundamental Theorem of Algebra
		- By FTOA: $n$ degree polynomial must have $n$ roots, if there is more, then it must be the $0$ polynomial
	- Thus $a = 0$ and V is non-singular
- Another proof
	- $det(V) = (-1)^{n+1} \prod_{i = 1}^{n} \prod_{j = 0}^{i - 1} (x_i - x_j)$, ~~trust me bro~~
	- Since $x_i$ distinct, determinant is non-zero so invertible

**This proves existence but does not lead to the best algorithm**
- $x_i^n$ can be massive, especially as we consider from top left corner of $V$ to bottom right
	- condition of $V$ can be very bad
- cost of $LU$ factorization $\frac{n^3}{3} + O(n^2) + n^2 + O(n)$
#### Lagrange Basis
For the simple interpolation problem $p(x_i) = y_i; i = 0, 1, \cdots, n$, consider the following basis:
$$
l_i(x) = \prod_{j = 0, j \ne i}^{n} \frac{x-x_j}{x_i-x_j}
$$
Note:
- $l_i(x) \in \mathcal{P}_n, \forall i$
- For $x_j$ is a data (interpolation) point
$$
l_i(x_j) =
\begin{cases}
1 & j = i \\
0 & j \ne i
\end{cases}
$$
This results in: $p(x) = \displaystyle \sum_{i = 0}^{n} l_i(x) y_i$
- $p(x) \in \mathcal{P}_n$ polynomial of degree $n$
- $p(x_i) = y_i; i = 0, 1, \cdots, n$
- Lagrange polynomial is *free* to construct
**But** while it is easy to calculate at the interpolation points, since we aren't looking for the values at the data points (the point of interpolation), it will be painfully expensive to solve the product of each basis function and actually interpolate using this method.
#### Newton (Divided Difference) Basis
For the simple interpolation problem $p(x_i) = y_i; i = 0, 1, \cdots, n$, consider the following basis:
$$
p(x) = a_0 + a_1(x - x_0) + a_2(x-x_0)(x-x_1) + \cdots + a_n(x-x_0)(x-x_1)\cdots(x-x_{n-1})
$$
<mark style="background: #FFB86CA6;">See A4</mark>
Note that this is not as expensive to evaluate due to Nested Evaluation, can factor out each $(x - x_i)$ in successive terms.
$$
\begin{cases}
p(x_0) = y_0 \\
\vdots \\
p(x_n) = y_n
\end{cases}
\iff
\begin{bmatrix}
1 & 0 & 0 & \cdots & 0 \\
1 & (x_1 - x_0) & 0 & \cdots & 0 \\
1 & (x_2 - x_0) & (x_2 - x_0)(x_2 - x_1) & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & (x_n - x_0) & (x_n - x_0)(x_n - x_1) & \cdots & (x_n - x_0)(x_n - x_1)\cdots(x_n - x_{n-1})
\end{bmatrix}
\begin{bmatrix}
a_0 \\
a_1 \\
\vdots \\
a_n
\end{bmatrix}
=
\begin{bmatrix}
y_0 \\
y_1 \\
\vdots \\
y_n
\end{bmatrix}
$$
- No factorization needed
- No conditioning issues
- Can be evaluated efficiently
**Do we need to set up and forward solve this lower triangular system?**
- No
$$
\begin{align}
a_0 &= y_0 \\
a_1 &= \frac{y_1 - y_0}{x_1 - x_0} = y[x_1]\\
a_2 &= \frac{\frac{y_2 - y_1}{x_2 - x_1} - \frac{y_1 - y_0}{x_1 - x_0}}{x_2 - x_0} = y[x_2, x_1, x_0] \\
\vdots \\
a_n
\end{align}
$$
##### Pattern of divided differences
$$
\begin{align}
y[x_i] &= y(x_i) = y_i \\
y[x_{i+k}, \cdots, x_i] &= \frac{y[x_{i+k}, \cdots, x_{i+1}] - y[x_{i+k-1, \cdots, x_i}]}{x_{i+k} - x_i}
\end{align}
$$
Example:
$y[x_2, x_1, x_0] = \frac{y[x_2, x_1] - y[x_1, x_0]}{x_2 - x_0}$
##### Newton Polynomial Theorem
The coefficients of the Newton Polynomial follow the divided differences pattern
$$
\begin{align}
p(x) = y[x_0] &+ (x - x_0)y[x_1, x_0] \\
&+ (x - x_0)(x - x_1)y[x_2, x_1, x_0] \\
&+ \cdots  \\
&+ (x - x_0)\cdots(x - x_{n-2})y[x_{n-1}, \cdots, x_0] \\
&+ (x - x_0)\cdots(x - x_{n-1})y[x_n, \cdots, x_0]
\end{align}
$$
$p(x) \in \mathcal{P_n}$ and $p(x_i) = y_i, \forall i = 0, 1, \cdots, n$
###### Proof
By induction on $n$. Let $p(x) \equiv p_n(x)$..
**Base cases:**
- $n = 0$, $p_0(x) = y[x_0]$
	- $p_0(x_0) = y_0$
- $n = 1$, $p_1(x) = y[x_0] + (x - x_0)y[x_1, x_0]$
	- $p_1(x_0) = y[x_0] = y_0$
	- $p_1(x_1) = y[x_0] + (x_1 - x_0)\frac{y_1 - y_0}{x_1 - x_0} = y_1$
**Induction Hypothesis:**
- IH 1: Assume $p_{n-1}(x) \in \mathcal{P_{n-1}}$ is the unique polynomial of degree $\le n - 1$ that satisfies: $p_{n-1}(x_i) = y_i, i = 0, 1, \cdots, n-1$, the **first** $n$ interpolation conditions (ie. it interpolates the first $n$ data points $x_0, x_1, \cdots, x_{n-1}$).
$$
\begin{align}
p_{n-1}(x) = y[x_0] &+ (x - x_0)y[x_1, x_0] \\
&+ (x - x_0)(x - x_1)y[x_2, x_1, x_0] \\
&+ \cdots  \\
&+ (x - x_0)\cdots(x - x_{n-2})y[x_{n-1}, \cdots, x_0]
%% &+ (x - x_0)\cdots(x - x_{n-1})y[x_n, \cdots, x_0] %%
\end{align}
$$
- IH 2: Assume $q(x) \in \mathcal{P_{n-1}}$ is the unique polynomial of degree $\le n-1$ that satisfies $q(x_i) = y_i, i = 1, 2, \cdots n$, the **last** $n$ interpolation conditions
	- **<mark style="background: #FF5582A6;">Note</mark>**: $q(x)$ is just $p_{n-1}(x)$ with the data shifted $x_i \to x_{i+1}$ (since we only fit the last $n$, we essentially just ignore $x_0$ and start $p(x)$ form from $x_1$ to $x_n$)
		- 
$$
\begin{align}
q(x) = y[x_1] &+ (x - x_1)y[x_2, x_1] \\
&+ (x - x_1)(x - x_2)y[x_3, x_2, x_1] \\
&+ \cdots  \\
&+ (x - x_1)\cdots(x - x_n)y[x_n, \cdots, x_1]
%% &+ (x - x_0)\cdots(x - x_{n-1})y[x_n, \cdots, x_0] %%
\end{align}
$$
- **NOTE:** this is NOT strong induction, we just have 2 induction hypotheses (deriving from 1)
**Induction Step:**
- Consider $p_n(x) = p_{n-1}(x) + (x - x_0)\cdots(x - x_{n-1}) a_n$
- Clearly by IH 1, $p_n(x_i) = y_i, \forall i = 0, 1, \cdots, n-1$ since last term disappears
- Need to choose $a_n$ such that $p_n(x_n) = y_n$
- Consider $r(x) = \frac{(x - x_0)q(x) - (x - x_n)p_{n-1}(x)}{x_n - x_0}$
	- Note that
		- $r(x_0) = p_{n - 1}(x_0) = y_0$ by IH 1
		- $r(x_n) = q(x_n) = y_n$ by IH 2
		- and for $i = 1, 2, \cdots, n-1$, $r(x_i) = \frac{(x_i - x_0)y_i - (x_i - x_n) y_i}{x_n - x_0}$ since $p_{n-1}(x_i) = y_i$ and $q(x_i) = y_i$
$r(x) \in \mathcal{P_n}$, is the **unique** (by [[#Vandermonde (Method of Undetermined Coefficients)|Theorem here]]) polynomial of degree $\le$ $n$ that goes through $n + 1$ points $r(x_i) = y_i, \forall i = 0, 1, \cdots, n$.
If $p_n(x) = p_{n-1}(x) + (x - x_0)\cdots(x - x_{n-1}) a_n$ also satisfies $p_n(x_i) = y_i, \forall i = 0, 1, \cdots, n$, then by the uniqueness:
$$
p_n(x) \equiv r(x)
$$

Coefficient of $x^n$ in $p_n(x)$ is $a_n$.
Coefficient of $x^n$ in $r(x)$ is last coefficient in $q(x)$ - last coefficient in $p_{n-1}(x)$ over $x_n - x_0$:
$$
\frac{y[x_n, \cdots, x_1] - y[x_{n-1}, \cdots, x_0]}{x_n - x_0}
$$
Which is exactly $y[x_n, \cdots, x_0]$, and thus $a_n \equiv y[x_n, \cdots, x_0]$ as wanted. $\square$
##### Example
Find $p \in \mathcal{p_3}$ such that $p(0) = 1, p(1) = 3, p(2) = 9, p(3) = 25$

Using a divided difference table.
Imagine arrows pointing 2-to-1 to the right

| $x$ | $y[x_i]$ | $y[x_{i+1}, x_i]$ | $y[x_{i+2}, x_{i+1}, x_i]$ | $y[x_{i+3}, x_{i+2}, x_{i+1}, x_i]$ |
|-|-|-|-|-|
|0|1||||
|||$\frac{3-1}{1-0}=2$|||
|1|3||$\frac{6-2}{2-0}=2$||
|||$\frac{9-3}{2-1}=6$||$\frac{5-2}{3-0}=1$|
|2|9||$\frac{16-6}{3-1}=5$||
|||$\frac{25-9}{3-2}=16$|||
|3|25||||
$$
\begin{align}
p(x) = y[x_0] &+ (x - x_0)y[x_1, x_0] \\
&+ (x - x_0)(x - x_1)y[x_2, x_1, x_0] \\
&+ (x - x_0)(x-x_1)(x - x_2)(x - x_{n-2})y[x_3, x_2, x_1, x_0] \\
\end{align}
$$
$p(x) = 1 + 2x + 2x(x-1) + 1x(x-1)(x-2)$
##### How are divided differences and derivative related?
$\displaystyle y[x_1, x_0] = \frac{y(x_1) - y(x_0)}{x_1 - x_0}$
- What happens if $x_1 \to x_0$?
- $\displaystyle \lim_{x_1 \to x_0} y[x_1, x_0] = \lim_{x_1 \to x_0} \frac{y(x_1)-y(x_0)}{x_1 - x_0} = y'(x_0)$ if $y'(x_0)$ exists
- Which is the first derivative of $y$ by first-principles.
$\displaystyle y[x_2, x_1, x_0] = \frac{y[x_2, x_1] - y[x_1, x_0]}{x_2 - x_0}$
- $\displaystyle \lim_{\substack{x_2 \to x_0 \\ x_1 \to x_0}} y[x_2, x_1, x_0] = \frac{y''(x_0)}{2!}$
**Can show that in general:**
$$
\lim_{\substack{x_k \to x_0 \\ x_{k-1} \to x_0 \\ \vdots \\ x_1 \to x_0}} y[x_{k}, x_{k-1}, \cdots, x_0] = \frac{y^{(k)(x_0)}}{k!}
$$
We have been working with simple interpolation.
![[Pasted image 20231220122022.png]]
##### How does [[#How are divided differences and derivative related?|this]] help with Osculatory (general) Interpolation? (ie. interpolation with derivative data)
Example:
Find $p \in \mathcal{P}_4$ such that $p(0) = 0, p(1) = 1, p(2) = 6, p'(1) = 1, p''(1) = 2$

|$x_i$|$y[x_i]$|$y[x_{i+1}, x_i]$|$y[x_{i+2}, x_{i+1}, x_i]$|$y[x_{i+3}, x_{i+2}, x_{i+1}, x_i]$|$y[x_{i+4}, x_{i+3}, x_{i+2}, x_{i+1}, x_i]$|
|---|---|---|---|---|---|
|0|0|||||
|||$\frac{1-0}{1-0}=1$||||
|1|1||$\frac{5-1}{2-1}=0$|||
|||$\frac{y'(1)}{1!}=1$||$\frac{1-0}{1-0}=1$||
|1|1||$\frac{y''(1)}{2!}=1$||$\frac{3-1}{2-0} = 1$|
|||$\frac{y'(1)}{1!}=1$||$\frac{4-1}{2-1}=3$||
|1|1||$\frac{5-1}{2-1}=4$|||
|||$\frac{6-1}{2-1}=5$||||
|2|6|||||
We write the derivatives into the table but when coalescing the values, use the derivative form instead of the divided-difference.
Reading top row for coefficients
$p(x) = y[0] + xy[1, 0] + x(x-1)y[1, 1, 0] + x(x-1)^2y[1, 1, 1, 0] + x(x-1)^3y[2,1,1,1,0]$
$= x + x(x-1)^2 + x(x-1)^3$
### Error in  Polynomial Interpolation
$E(x) = y(x) - p(x)$
Note that $y(x)$ is the "correct" underlying function that generates the data points $[x_i, y_i]$.

For simple interpolation $p(x_i) = y_i, \forall i = 0, 1, \cdots, n$.
Can show that:
$$
E(x) = \frac{y^{(n+1)}(\eta)}{(n+1)!} \prod_{i=0}^{n} (x - x_i) \text{ where } \eta \in \text{span}\{ x_0, x_1, \cdots, x_n, x \} = \text{closed interval } [\min \{ x_0, x_1, \cdots, x_n, x \}, \max \{ x_0, x_1, \cdots, x_n, x \}]
$$

It looks like the remainder of the Taylor expansion, since the polynomial interpolation is like a [[#Truncated Taylor Series|truncated Taylor expansion]].
For first part, the more data points the closer $p$ is to $y$ since $n \to \infty$.
#### Runge Phenomenon
$$
y(x) = \frac{1}{1 + 25x^2}
$$
![[runge_phenomenon.png]]
The more interpolation points for this function the higher degree polynomial $\implies$ the worse it gets.
Problem is the higher derivatives of the function $y^{(n+1)}(\eta)$ grow faster than $(n+1)!$, thus the higher polynomial, the worse error gets.
This is where piecewise (spline) interpolation important
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
