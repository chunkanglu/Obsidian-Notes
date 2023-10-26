---
tags:
  - CSCC37
---
We will count *multiplication & addition* pairs ($mx + b$) a **_flop_** (floating point operation).
- Multiplication usually paired with addition
- The flop is the most expensive step (much more than all other operations used in the process like comparison or row swaps)
	- **See below, factorization is $\frac{n}{3}$ times as much compared to the solves**
- Assuming that all multiplications cost the same amount
# Computing the LU factorization
#### Stage 1
$$
\begin{bmatrix}
\square & - & - & \ldots & - \\
0 & * & *  & \ldots & * \\
0 & * & *  & \ldots & * \\
\vdots \\
0 & * & *  & \ldots & * \\
0 & * & *  & \ldots & * \\
\end{bmatrix}
$$
There are $n-1 \times n-1$ asterisks and each asterisk is a flop.
Adding a multiple of row $1$ to rows $, \ldots, n$ costs $(n-1)^2$ flops.
#### Stage 2
$(n-2)^2$ flops
#### Stage n-1
$(n- (n-1))^2 = 1$ flop
#### Total Complexity
$$
\begin{align}
(n-1)^2 + (n-2)^2 + \cdots + 1 &= \sum_{i = 1}^{n-1} (n-i)^2 \\
&= \frac{n(n-1)(2n-1)}{6} \\
&= \frac{n^3}{3} + O(n^2)
\end{align}
$$
# Computing forward solve $Ld = b$
$$
\begin{bmatrix}
1 & 0 & 0 & \ldots & 0 \\
L_{21} & 1 & 0 & \ldots & 0 \\
L_{31} & L_{32} & 1 & \ldots & 0 \\
\vdots & \vdots & \vdots & \ddots \\
L_{n1} & L_{n2} & L_{n3} & \ldots & 1
\end{bmatrix}
\begin{bmatrix}
d_1 \\
d_2 \\
d_3 \\
\vdots \\
d_n
\end{bmatrix}
=
\begin{bmatrix}
b_1 \\
b_2 \\
b_3 \\
\vdots \\
b_n
\end{bmatrix}
$$
$$
\begin{align}
d_1 &= b_1 & \text{0 flops} \\
d_2 &= b_2 - L_{21}d_1 & \text{1 flop} \\
d_3 &= b_3 - L_{31}d_1 - L_{32}d_2 & \text{2 flops} \\
\vdots \\
d_n &= b_n - L_{n1}d_1 - \ldots - L_{n, n-1}d_{n-1} & \text{n-1 flops}
\end{align}
$$
#### Total Complexity
$$
\frac{n(n-1)}{2} = \frac{n^2}{2} + O(n) \text{ flops}
$$
# Computing backwards substitution $Ux = d$
Same as forward.
#### Total Complexity
$$
\frac{n(n-1)}{2} = \frac{n^2}{2} + O(n) \text{ flops}
$$
# Combining both solves together
#### Total Complexity
$$
n^2 + O(n) \text{ flops}
$$
# Important Note
If you have several system to solve with the same coefficient matrix $A$ but with different right hand sides, it is much ($\frac{n}{3}$ times) cheaper to factor $A$ only only and then use the factorization for each right hand side. 
$$
\begin{align}
Ax &= b \\
Ax &= c \\
\vdots \\
Ax &= z
\end{align}
$$