---
tags:
  - CSCC37
---
Given $F : \mathbb{R} \rightarrow \mathbb{R}$ that is non-linear. Solve $F(x) = 0$.
- In general, no closed form analytic solution.
- Need numerical techniques with iterative algorithms for approximate solutions $\hat{x}_k, k = 0, 1, 2, \ldots$ that fill hopefully converge to the true solution (root) $k \rightarrow \infty \implies \hat{x}_k \rightarrow \tilde{x}$.
# Big Questions
- Are there roots?
- How many roots?
	- Sometimes we know such as for polynomials, the Fundamental Theorem of Algebra states $n$-polynomial has $n$ roots
	- But usually we don't know
# Fixed Point Methods
$F(\tilde{x}) = 0 \iff \tilde{x} = g(\tilde{x})$ where $\tilde{x}$ is a fixed point of $g(x)$.
- Can always use ***first form***: $g(x) = x - F(x)$ (or $g(x) = x + F(x)$)
	- $F(\tilde{x}) = 0 \iff \tilde{x} = g(\tilde{x})$
- Alternatively ***second form*** $g(x) = x - h(x)F(x)$ for any auxiliary function $h(x)$
	- $h(x) = -1$ to get $g(x) = x + F(x)$
	- Usually $h(x)$ is complicated to make $g(x)$ able to be solved quickly
	- Now **we also have to worry about when** $h(\tilde{x}) = 0$ and this gives a **false positive solution**
		- We need to plug in $F(\tilde{x}) \ne 0$ to confirm if it is a valid root
			- Trade off for using second form for better speed (of ability) of convergence outweighs the cost of this operation
		-  $F(\tilde{x}) = 0 \implies \tilde{x} = g(\tilde{x})$
		-  $\tilde{x} = g(\tilde{x}) \centernot\implies  F(\tilde{x}) = 0$
# Fixed Point Iteration (FPI)
Start with guess $\hat{x}_0$, then iterate with $\hat{x}_{k+1} = g(\hat{x}_k), k = 0, 1, 2, \ldots$ until convergence (or failure).
- Testing for convergence
	- **X-test** - convergence can be when $||\hat{x}_{k+1} - \hat{x}_k|| < \epsilon$ for some small epsilon like $10^{-16}$
	- **F-test** - measure $||F(\hat{x}_{k})|| < \epsilon$
- Depending on initial guess $\hat{x}_0$, the Fixed Point Iteration $(*)$ may or may not work
## Fixed Point Theorem (FPT)
If there is a closed interval $\left[a, b\right]$ such that:
$$
\begin{align}
&g(x) \in \left[a, b\right], \forall x \in [a, b] \tag{1} \\
&|g'(x)| \le L < 1, \forall x \in [a, b] \tag{2}
\end{align}
$$
1. $g(x)$ gets stuck
2. First derivative is fractional
Then $g(x)$ has a unique fixed point in $[a, b]$.
### Existence of Fixed Point in $[a, b]$
If $a \le x \le b$ and $a \le g(x) \le b$ then $x = g(x)$ has at least 1 solution in $[a, b]$.
#### Proof of Existence
Consider $f(x) = x - g(x)$ where $a \le x \le b$.
$f(a) = a - g(a) \le 0$ since $g(a) \ge a$
$f(b) = b - g(b) \ge 0$ since $g(b) \le b$
Thus there must be some point $a \le c \le b$ such that $f(c) = 0$ which is a solution.
### Proof of FPT
#### General Useful Result for Proof
For any two points $p, q \in [a, b]$,
$g(p) - g(q) = g'(c)(p-q)$ for some point $p \le c \le q$ by Mean Value Theorem
$|g(p) - g(q)| \le L|p - q|$
#### Actual Proof
Start with any $x_0 \in [a, b]$ and iterate $x_{k+1} = g(x_k), k = 0, 1, 2, \ldots$
then all $x_k \in [a, b]$ by (1)
Moreover,
$$
\begin{align}
x_{k+1} - x_{k} &= g(x_k) - g(x_{k-1})  \\
&= g'(\eta_k)(x_k - x_{k-1}) \text{ for some } \eta_k \in [x_{k-1}, x_k] \subset [a, b] \text{ by Mean Value Theorem}
\end{align}
$$
$$
\begin{align}
|x_{k+1} - x_{k}| &\le L (x_k - x_{k-1}) & \text{ by (2)} \\
&\le \cdots & \text{ iteratively repeat} \\
&\le L^k |x_1 - x_0|
\end{align}
$$
Since $L < 1$, $k \rightarrow \infty \implies |x_{k+1} - x_k| \rightarrow 0 \implies x_k$ converges to *some* point $\tilde{x} \in [a, b]$
Must show that:
1. $\tilde{x} = g(\tilde{x})$
	Consider $g(\tilde{x}) - g(x_k) = g'(\xi_k)(\tilde{x} - x_k)$
$$
\begin{align}
|g(\tilde{x}) - \tilde{x}| &= |g'(\xi_k)(\tilde{x} - x_k) + g(x_k) - \tilde{x}| \\
&= |g'(\xi_k)(\tilde{x} - x_k) + x_{k+1} - \tilde{x}| & \text{by def of g(x)} \\
&\le |g'(\xi_k)(\tilde{x} - x_k)| + |x_{k+1} - \tilde{x}| & \text{Triangle Inequality} \\
&= |g'(\xi_k)|~|\tilde{x} - x_k| + |x_{k+1} - \tilde{x}| & \text{Separate constant} \\
&= 0 & \text{since $x_k, x_{k+1}$ converge to $\tilde{x}$}
\end{align}
$$
2. $\tilde{x}$ is unique in $[a, b]$ (only one fixed point in $[a, b]$)
	Suppose for contradiction there were two points distinct $\tilde{x}_1, \tilde{x}_2$.
$$
\begin{align}
\tilde{x}_1 - \tilde{x}_2 &= g(\tilde{x}_1) - g(\tilde{x}_2) \\
&= g'(c)(\tilde{x}_1 - \tilde{x}_2)
\end{align}
$$
$$
\begin{cases}
|\tilde{x}_1 - \tilde{x}_2| \le L|\tilde{x}_1 - \tilde{x}_2| & \text{from above} \\
L|\tilde{x}_1 - \tilde{x}_2| \le |\tilde{x}_1 - \tilde{x}_2| & \text{since $L$ is fractional}
\end{cases}
\implies |\tilde{x}_1 - \tilde{x}_2| = 0 \implies \tilde{x}_1 = \tilde{x}_2
$$
## Rate of Convergence
If the following holds, we have the $p^{th}$ order convergence to the fixed point $\tilde{x}$:
$$
\lim_{x_k \rightarrow \tilde{x}} \frac{|\tilde{x} - x_{k+1}|}{|\tilde{x}-x_k|^p} = c \ne 0
$$
- Ratio of current iteration to power of previous iteration
- $c$ must be a fraction for convergence
- Higher $p$ values give much faster decrease of absolute error
- Second form allows us manipulate the equation to get a larger $p$ value
# Work Through Example 1
$$
F(x) = x^2 + 2x -3 = 0
$$
> [!warning]- We know the true solutions are
> $x = -1, 3$

Consider the following Fixed Point Iteration using second form:
$$
x_{k+1} = x_k + \frac{x_{k}^2 + 2x_k - 3}{x_{k}^2 - 5} \tag{*}
$$
$$
h(x) = \frac{-1}{x^2 - 5}
$$
Although this $h(x)$ was arbitrarily chosen (<mark style="background: #FFB8EBA6;">wtf</mark>), it conveniently can never be $h(x) = 0$ so we can avoid the possibility of not finding a root of $F(x)$

Start algorithm $(*)$ with:
- $\hat{x}_0 = -5$, $\hat{x}_k$ converges to $-3$
- $\hat{x}_0 = 5$, $\hat{x}_k$ does not converge
- $\hat{x}_0 = 0$, $\hat{x}_k$ converges to $1$
- $\hat{x}_0 = 1.5$, $\hat{x}_k$ converges to $1$
# Work Through Example 2
$$
F(x) = x - e^{-x} = 0
$$
![[non-linear-eq-example-plot.png]]
We can preliminarily think about the graphs of the two equations to get an idea of how many roots and possibly roughly where the root is.
We can transform this to fixed point as so using first form:
$$
x - e^{-x} = 0 \iff x = e^{-x}
$$
We want to find a guaranteed interval of convergence.
$$
x_{k+1} = e^{-x_k}
$$
#### Using FPT
Let's pull an educated guess interval out of our ass $[a, b] = [0.1, 1]$.
> Note: this is real handwavy and needs better explanation
To show this satisfies condition 1 of FPT, check end points 0.1 and 1, and note that $g(x)$ is monotonically decreasing in the interval.
Then for condition 2, $|g'(x)| = e^{-x}$ is fractional everywhere in $[0.1, 1]$
#### Rate of Convergence
How fast does it converge

| $k$ | $x_k$ |
| -------- | -------- |
| 0 | 0.936 |
| 1 | 0.392 |
| 2 | 0.67 |
| 3 | 0.51 |
| $\vdots$ | $\vdots$ |
| 34 | 0.5671433 |
And it converges at iteration 34

Table of absolute error $|\tilde{x} - \hat{x}_k|$:

| $k$ | $p=1, c=\frac{1}{2}$ | $p=2, c=\frac{1}{2}$ |
|---|-----------|-----------|
| $0$ | $10^{-1}$       | $10^{-1}$ |
| $1$ | $5 \times 10^{-2}$    | $10^{-2}$ |
| $2$ | $2.5 \times 10^{-2}$   | $10^{-4}$ |
| $3$ | $1.25 \times 10^{-2}$  | $10^{-8}$ |
| $4$ | $6.25 \times 10^{-3}$  | $10^{-16}$ |
| $5$ | $3.125 \times 10^{-3}$ | $10^{-32}$ |
Each time cut in half vs. square root
- Second order method is much faster
