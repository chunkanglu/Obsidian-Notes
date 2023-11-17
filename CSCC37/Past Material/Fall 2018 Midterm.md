1. floating point error bound
2. LU factorization
3. LU factorization
4. LU factorization extension
5. Roundoff error LU factorization

# Q4
$$
\begin{align}
PAQ = LU
\end{align}
$$
Notice that $Q^{-1} = Q^T$
$$
PAx = LUQ^Tx = Pb
$$
# Q5
Row pivoting allows our multipliers in our Gauss Transforms to remain fractional and not be extremely large in orders of magnitude larger than the other elements.
Consider the following:
$$
A =
\begin{bmatrix}
10^{-16} & 4 \\
2 & 1
\end{bmatrix}
$$
Without pivoting, we would have the following Gauss Transform:
$$
L = 
\begin{bmatrix}
1 & 0 \\
-2 \times 10^{16} & 1
\end{bmatrix}
, ~
L A =
\begin{bmatrix}
10^{-16} & 4 \\
0 & 1- 8 \times 10^{16}
\end{bmatrix}
$$