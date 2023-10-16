Let $X$ and $Y$ be 2 binary numbers represented as $n$-bit arrays.
We can split these into two chunks of (roughly) size $\frac{n}{2}$.
$X = X_1 \cdot 2^{\frac{n}{2}} + X_0$  
$Y = Y_1 \cdot 2^{\frac{n}{2}} + Y_0$

$$
\begin{align*}
X \cdot Y &= X_1 Y_1 \cdot 2^{n} + (X_1 Y_0 + X_0 Y_1) \cdot 2^{\frac{n}{2}} + X_0 Y_0 \\
&= X_1 Y_1 \cdot 2^{n} + ((X_1 + X_0)(Y_1 + Y_0) - X_1 Y_1 - X_0 Y_0) \cdot 2^{\frac{n}{2}} + X_0 Y_0 \\
& \text{Let } a = X_1 Y_1, b = (X_1 + X_0)(Y_1 + Y_0), c = X_0 Y_0 \\
&= a \cdot 2^{n} + (b - a - c) \cdot 2^{\frac{n}{2}} + c
\end{align*}
$$
Notice this only uses 3 multiplications rather than the 4 using the traditional method. Additionally, each of the multiplications $a, b, c$ can be recursively calculated using the same method. Thus we get the following recurrence:
$$
T(n) = 3T(\frac{n}{2}) + cn = \Theta(n^{log_{2}{3}}) \approx \Theta(n^{1.585})
$$

This same idea can be extended to splitting into more than 2 chunks.

**Small Note:**
Let $U = X_1 + X_0, V = Y_1 + Y_0$.
Both of these addition may end up with a carry-out bit leading to $\frac{n}{2}+1$ bits each.
Let us decompose as follows:
$U = U_1 \cdot 2^{\frac{n}{2}} + U_0$ where $U_1$ is the carry out bit.
$V = V_1 \cdot 2^{\frac{n}{2}} + V_0$ where $V_1$ is the carry out bit.
$$
U \cdot V = U_1 V_1 \cdot 2^{n} + (U_1 V_0 + U_0 V_1) \cdot 2^{\frac{n}{2}} + U_0 V_0
$$
Notice that $U_1 V_1$ is 1-bit multiplication which is constant.

