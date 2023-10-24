---
tags:
  - CSCC37
---
- What if at some stage of the elimination the pivot element is exactly zero?
	- In the algorithm above, we would have a divide by zero error
- Alternatively, a similar (but more common) problem if the pivot element element is very small in magnitude
	- **Solution:** Row partial pivoting
		- When eliminating the $k^{th}$ column, first look for row j, $j > k$, with largest element in magnitude in column $k$, and then swap rows $j$ and $k$
		- This causes all multipliers in the Gaussian Transforms to have magnitude $< 1$ (ie. is fractional)
- How to extract a factorization when row pivoting is used to control round off error propagation (stability)?
	- We now have $P$ matrices mixed in with the $L$ matrices, so the inverses is hard to find

#### Example 1
$$
A = 
\begin{bmatrix}
	1 & 2 & 1 \\
	1 & 2 & 4 \\
	1 & 3 & 3
\end{bmatrix}
,
L_1 =
\begin{bmatrix}
	1 & 0 & 0 \\
	-1 & 1 & 0 \\
	-1 & 0 & 1
\end{bmatrix}
,
L_1A = 
\begin{bmatrix}
	1 & 2 & 1 \\
	0 & 0 & 3 \\
	0 & 1 & 2
\end{bmatrix}
$$
- We cannot use row 2 in $L_1A$ to eliminate row 3
- Need to swap rows 2 and 3 using permutation matrix
$$
P_2 =
\begin{bmatrix}
	1 & 0 & 0 \\
	0 & 0 & 1 \\
	0 & 1 & 0
\end{bmatrix}
,
P_2(L_1 A) =
\begin{bmatrix}
	1 & 2 & 1 \\
	0 & 1 & 2 \\
	0 & 0 & 3
\end{bmatrix}
$$
#### Example 2
- Different $A, L_1$, but we don't care about it
- We can continue with elimination in this case
$$
L_1 A = 
\begin{bmatrix}
	1 & 2 & 1 \\
	0 & 10^{-16} & 3 \\
	0 & 1 & 2
\end{bmatrix}
,
L_2 =
\begin{bmatrix}
	1 & 0 & 0 \\
	0 & 1 & 0 \\
	0 & -10^{16} & 1
\end{bmatrix}
,
L_2 (L_1 A) =
\begin{bmatrix}
	1 & 2 & 1 \\
	0 & 10^{-16} & 3 \\
	0 & 0 & 2 - 3 \times 10^{16}
\end{bmatrix}
$$
Remaining elements in the lower right corner submatrix of $L_2 L_1 A$ are very large in magnitude unlike the other elements.
- Round off error can be shown to be directly proportional to the largest elements that occur during the factorization

Swap Rows 2 and 3
$$
P_{2} L_{1} A = 
\begin{bmatrix}
1 & 2 & 1 \\
0 & 1 & 2 \\
0 & 10^{16} & 3 
\end{bmatrix}
,
L_{2} = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 1 \\
0 & -10^{-16} & 1
\end{bmatrix}
,
L_{2} P_{2} L_{1} A =
\begin{bmatrix}
1 & 2 & 1 \\
0 & 1 & 2 \\
0 & 0 & 3 - 2 \times 10^{-16}
\end{bmatrix}
$$
- This is fine since $3 - 2 \times 10^{-16} \approx 3$

#### Example 3
$$
\begin{bmatrix}
2 & 6 & 6 \\
3 & 5 & 12 \\
6 & 6 & 12
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2}  \\
x_{3} 
\end{bmatrix}
=
\begin{bmatrix}
20 \\
25 \\
30
\end{bmatrix}
\iff Ax = b
$$
1. Pivot rows 1 and 3
$$
P_{1} A x = P_{1} b
$$
$$
P_{1} =
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{bmatrix}
\to
\begin{bmatrix}
6 & 6 & 12 \\
3 & 5 & 12 \\
2 & 6 & 6
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2}  \\
x_{3} 
\end{bmatrix}
=
\begin{bmatrix}
30 \\
25 \\
20
\end{bmatrix}
$$
2. Subtract $\frac{1}{2}$ row 1 from row 2 & $\frac{1}{3}$ row 1 from row 3
$$
L_{1} =
\begin{bmatrix}
1 & 0 & 0 \\
-\frac{1}{2} & 1 & 0 \\
-\frac{1}{3} & 0 & 1
\end{bmatrix}
,
L_{1} P_{1} A x = L_{1} P_{1}b
$$
$$
\begin{bmatrix}
6 & 6 & 12 \\
0 & 2 & 6 \\
0 & 4 & 2
\end{bmatrix}
x =
\begin{bmatrix}
30 \\
10 \\
10
\end{bmatrix}
$$
$$
P_{2} L_{1} P_{1} A x = P_{1} L_{1} P_{1} b
$$
$$
\begin{bmatrix}
6 & 6 & 12 \\
0 & 4 & 2 \\
0 & 2 & 6
\end{bmatrix}
x = 
\begin{bmatrix}
30 \\
10 \\
10
\end{bmatrix}
$$
$$
L_{2} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -\frac{1}{2} & 1
\end{bmatrix}
$$
$$
L_{2} P_{2} L_{1} P_{1} A x = L_{2} P_{2} L_{1} P_{1} b
$$
$$
\begin{align*}
U = L_{2} P_{2} L_{1} P_{1} \\
\hat{b} = L_{2} P_{2} L_{1} P_{1} b
\end{align*}
$$
$$
\begin{bmatrix}
6 & 6 & 12 \\
0 & 4 & 2 \\
0 & 0 & 5
\end{bmatrix}
x =
\begin{bmatrix}
30 \\
10 \\
5
\end{bmatrix}
$$
3. Extract factorization
$$
\begin{align}
L_{2} P_{2} L_{1} P_{1} A &\iff L_{2} P_{2} L_{1} P_{2} P_{2} P_{1} A & \text{since doing same permutation matrix twice is identity} \\
&\iff L_{2} \underbrace{(P_{2} L_{1} P_{2})}_{\tilde{L_{1}}} P_{2} P_{1} A \\
&\iff L_{2} \tilde{L_{1}} P_{2} P_{1} A \\
&= U
\end{align}
$$
$$
\begin{align} \\
P = P_{2} P_{1}, L = L_{2} \tilde{L_{1}}
&\iff P_{2} P_{1} A = \tilde{L_{1}^{-1} L_{2}^{-1}} U \\
&\iff PA = LU
\end{align}
$$
> Claim: $\tilde{L_{1}} = P_{2} L_{1} P_{2}$ is a Gauss Transform and is $L_{1}$ with two multipliers swapped. This generalizes to $n$ by $n$.
> **Proof:** <mark style="background: #FFB86CA6;">See A2</mark>
> **Example:**
$$
P_{2} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix}
,
L_{1} =
\begin{bmatrix}
1 & 0 & 0 \\
l_{21} & 1 & 0 \\
l_{31} & 0 & 1
\end{bmatrix}
$$
$$
\begin{align}
P_{2} L_{1} P_{2} &=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
l_{21} & 1 & 0 \\
l_{31} & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix} \\
&=
\begin{bmatrix}
1 & 0 & 0 \\
l_{31} & 0 & 1 \\
l_{21} & 1 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix} & \text{premultiply permutation matrix swaps rows} \\
&=
\begin{bmatrix}
1 & 0 & 0 \\
l_{31} & 1 & 0 \\
l_{21} & 0 & 1
\end{bmatrix} & \text{postmultiply permutation mtarix swaps columns}
\end{align}

$$

### Solving $Ax = b$ given $PA = LU$
$$
\begin{align}
Ax = b &\iff PAx = Pb \\
&\iff L U x = \tilde{b} & \text{where } \tilde{b} = Pb \\
\end{align}
$$
1. Solve $Ld = \tilde{b}$ for $d$
2. Solve $Ux = d$ for $x$

## Special Case
**What happens if at some stage $k$ of the elimination the diagonal and everything below it is exactly zero?**
<mark style="background: #FFB8EBA6;">𝓖𝓲𝓿𝓮 𝓾𝓹, 𝓼𝓽𝓸𝓹, 𝓰𝓮𝓽 𝓪 𝓵𝓲𝓯𝓮</mark>

Just skip the column.
However, $U_{kk} = 0 \implies U$ is singular, but we still have a factorization.

**Using the factorization to solve $Ax = b$?**
This is where problem in $Ux = d$ since $U$ is singular.
May have **infinitely many solutions** or **no solutions** depending on $d$.
**Example:**

$$
\begin{bmatrix}
2 & 5 & 4 \\
0 & 0 & 1 \\
0 & 0 & 2
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{bmatrix}
=
\begin{bmatrix}
d_{1} \\
d_{2} \\
d_{3}
\end{bmatrix}
$$
$$
\implies
\begin{equation}
\begin{cases}
2x_{3} = d_{3} \\
x_{3} = d_{2}
\end{cases}
\end{equation}
$$
If $d_{3} = 2d_{2}$, then infinite solutions since $x_{3}$ is a free parameter. Otherwise, no solution.