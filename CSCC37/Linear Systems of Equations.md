> Solve $A\vec{x} = \vec{b}$ where $A$ is a square matrix.

We have system of equations:
$$
\begin{align}
a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n &= b_2 \\
\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \ldots + a_{nn}x_n &= b_n
\end{align}
$$
## 1. Reduce system to triangular form
1. Assume $a_{11} \ne 0$. 
	1. Multiply eq.1 by $\frac{a_{21}}{a_{11}}$ and subtract from eq.2
	2. Multiply eq.1 by $\frac{a_{31}}{a_{11}}$ and subtract from eq.3
	3. ...
	4. Multiply eq.1 by $\frac{a_{n1}}{a_{11}}$ and subtract from eq.n
$$
\begin{align*}
a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n &= b_1 \\
0 + \hat{a_{22}}x_2 + \ldots + \hat{a_{2n}}x_n &= \hat{b_2} \\
\vdots \\
0 + \hat{a_{n2}}x_2 + \ldots + \hat{a_{nn}}x_n &= \hat{b_n}
\end{align*}
$$
2. Repeat for submatrix $a_{22}$ to $a_{nn}$, assuming $a_{22} \ne 0$
	1. Multiply eq.2 by $\frac{\hat{a_{32}}}{\hat{a_{22}}}$ and subtract from eq.3
	3. ...
	4. Multiply eq.2 by $\frac{\hat{a_{n2}}}{\hat{a_{22}}}$ and subtract from eq.n
3. ...
4. Continue to $\tilde{a}_{n-1, n-1} \ne 0$
	1. Multiply eq.$n-1$ by $\frac{\tilde{a}_{n, n-1}}{\tilde{a}_{n-1, n-1}}$ and subtract from eq.$\tilde{n}$

Final triangular equations
$$
\begin{align*}
a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n &= b_1 \\
\hat{a_{22}}x_2 + \ldots + \hat{a_{2n}}x_n &= \hat{b_2} \\
\vdots \\
\tilde{\tilde{a}}_{nn}x_n &= \tilde{\tilde{b_n}}
\end{align*}
$$
## 2. Solve bottom-up with back-substitution


# Alternative view of process in matrix form
> Gauss Transform

### Eliminate first column of $A$ below $a_{11}$
$A\vec{x} = \vec{b} \implies (L_1 A)\vec{x} = L_1 \vec{b}$ where $L_1$ is identity but with first column with previous multipliers
$$
L_1 = 
\begin{bmatrix}
1 & 0 & 0 & \ldots &0 \\
-\frac{a_{21}}{a_{11}} & 1 & 0 & \ldots & 0 \\
-\frac{a_{31}}{a_{11}} & 0 & 1 & \ldots & 0 \\
\vdots &&& \ddots\\
-\frac{a_{n1}}{a_{11}} & 0 & 0 & \ldots & 1
\end{bmatrix}
$$
### Eliminate second column of $(L_1A)$ below $\hat{a}_{11}$
$(L_1 A)\vec{x} = L_1 \vec{b} \implies L_2(L_1 A)\vec{x} = L_2(L_1 \vec{b})$
$$
L_2(L_1 A) = 
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & \ldots & a_{1n} \\
0 & \hat{a}_{22} & \hat{a}_{23} & \ldots & \hat{a}_{2n} \\
0 & 0 & \hat{a}_{33} & \ldots & \hat{a}_{3n} \\
\vdots &&& \ddots\\
0 & 0 & 0 & \ldots & \hat{a}_{nn}
\end{bmatrix}
$$
$$
L_1 = 
\begin{bmatrix}
1 & 0 & 0 & \ldots &0 \\
0 & 1 & 0 & \ldots & 0 \\
0 & -\frac{\hat{a}_{32}}{\hat{a}_{22}} & 0 & \ldots & 0 \\
\vdots &&& \ddots\\
0 & -\frac{\hat{a}_{n2}}{\hat{a}_{22}} & 0 & \ldots & 1
\end{bmatrix}
$$

### Continue to get $\underbrace{L_{n-1}(L_{n-2}(...L_2 (L_1 A)...)}_{U} \vec{x} = \underbrace{L_{n-1}(L_{n-2}(...L_2 (L_1 \vec{b})...)}_{\tilde{\tilde{b}}}$
- Define as $U\vec{x} = \tilde{\tilde{b}}$
- Reduced equivalent system to solve with back-substitution 

# LU Factorization
We have $L_{n-1}L_{n-2} \ldots L_2 L_1 A = U$
$$
A = \underbrace{(L_1^{-1} L_2^{-1} \ldots L_{n-1}^{-1})}_{L} U
$$
> *Lemma 1:*  If $L_i$ is a Gauss Transform, then $L_i^{-1}$ exists and also is a Gauss Transform. Furthermore, computing $L_i^{-1}$ essentially is **free** in constant time.
> *Proof:* <mark style="background: #FFB86CA6;">Assignment 2 and in TB</mark>

> *Lemma 2:* If $L_i$ and $L_j$ are Gauss Transforms, and $i < j$ (multiply right to left), then $L_i L_j = L_i + L_j - I$ ($I$ is the identity). Note that the $i$th column and $j$th column don't overlap so technically nothing is added. Essentially **free**, in constant time.
> *Proof:* <mark style="background: #FFB86CA6;">Assignment 2 and in TB</mark>

#### Why LU Factorization instead of just processing both sides
$L_{n-1} L_{n-2} \ldots L_2 L_1 A \vec{x} = L_{n-1} L_{n-2} \ldots L_2 L_1 \vec{b}$
For repeated operation with same $A$ but different $\vec{b}$, by using LU Factorization we remove the need for repeated triangularizing of $A$ since you get the same $U$ every time.

- Reduction to triangularized form is the most expensive step
- Forward and backward substitution are much cheaper
- Thus if we have several linear systems where $A$ does not change, we can save on costs this way by only factoring once.

