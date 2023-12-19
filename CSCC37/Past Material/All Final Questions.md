![[Pasted image 20231219094530.png]]
$g_1$ is the first form of $f$ so it can be used
$g_4$ is a second form of $f$ with $h(x) = \frac{1}{x^2}$
![[Pasted image 20231219094545.png]]
IDK
![[Pasted image 20231219094553.png]]
By the Rate of Convergence Theorem and taking the derivatives of the above variations of g, we get that they converge linearly. Consider the variation of g from using Newton's Method:
$$
g(x) = x - \frac{x^2 - 2}{2x}
$$
We know that Newton's Method converges quadratically which is better than linearly.

![[Pasted image 20231219094606.png]]

| $x$ | $y[x_i]$ | $y[x_{i+1}, x_i]$ | $y[x_{i+2}, x_{i+1}, x_i]$ | $y[x_{i+3}, x_{i+2}, x_{i+1}, x_i]$ |
|-|-|-|-|-|
|-1|4||||
|||$\frac{6-4}{0-(-1)}=2$|||
|0|6||$\frac{6-2}{1-(-1)}=2$||
|||$\frac{12-6}{1-0}=6$|||
|1|12||||
$p(x) = 4 + 2(x+1) + 2(x+1)(x)$
![[Pasted image 20231219094619.png]]
$p(x) = \sum_{i=0}^{n} \ell_i(x) y_i$
$\ell_i(x) = \prod_{j=0, j\ne i}^{n} \frac{x - x_j}{x_i - x_j}$
$\ell_0(x) = \frac{x - x_1}{x_0 - x_1} \frac{x - x_2}{x_0 - x_2} = \frac{x - 0}{-1-0} \frac{x - 1}{-1 - 1} = \frac{x(x-1)}{2}$
$\ell_1(x) = \frac{x + 1}{1} \frac{x - 1}{-1} = -(x^2-1)$
$\ell_2(x) = \frac{x + 1}{1 + 1} \frac{x}{1} = \frac{x(x+1)}{2}$
$p(x) = 2x(x-1) - 6(x^2 - 1) + 6x(x+1)$
![[Pasted image 20231219094629.png]]
From a: $p(x) = 4 + 2x + 2 + 2x^2 + 2x = 6 + 4x + 2x^2$
From b: $p(x) = 2x^2 - 2x - 6x^2 + 6 + 6x^2 + 6x = 6 + 4x + 2x^2$
Which is the same
![[Pasted image 20231219094639.png]]

| $x$ | $y[x_i]$ | $y[x_{i+1}, x_i]$ | $y[x_{i+2}, x_{i+1}, x_i]$ | $y[x_{i+3}, x_{i+2}, x_{i+1}, x_i]$ |
|-|-|-|-|-|
|-1|4||||
|||$\frac{6-4}{0-(-1)}=2$|||
|0|6||$\frac{6-2}{1-(-1)}=2$||
|||$\frac{12-6}{1-0}=6$||$\frac{-2 - 2}{2 - (-1)} = -\frac{4}{3}$|
|1|12||$\frac{2 - 6}{2 - 0} = -2$||
|||$\frac{16-12}{2-1}=2$|||
|2|16||||
$p(x) = 4 + 2(x+1) + 2(x+1)(x) - \frac{4}{3} (x+1)(x)(x-1)$
![[Pasted image 20231219094647.png]]
$x_0$ to $x_1$: $2x + 6$
$x_1$ to $x_2$: $6x+6$
$x_2$ to $x_3$: $4x + 8$
$$
p(x) =
\begin{cases}
2x + 6 & \text{if } -1 \le x < 0 \\
6x + 6 & \text{if } 0 \le x < 1 \\
4x + 8 & \text{if } 1 \le x \le 2
\end{cases}
$$

![[Pasted image 20231219094741.png]]
Base 3: $(0.100)^{-1}$
Base 10: $3^{-2}$
![[Pasted image 20231219094750.png]]
Base 3: $(0.222)^{1}$
Base 10: $2 \cdot 3 + 2 \cdot 3^{-1} + 2 \cdot 3^{-2}$
![[Pasted image 20231219094758.png]]
$\frac{1}{2}b^{-2}$
![[Pasted image 20231219094806.png]]
Cannot be represented as it is outside of the representable domain of this system.
![[Pasted image 20231219094813.png]]
$0.120$
![[Pasted image 20231219094821.png]]
$0.100, 0.101, 0.102, 0.110, 0.111, 0.112, 0.120, 0.121, 0.122, 0.200, 0.201, 0.202, 0.210, 0.211, 0.212, 0.220, 0.221, 0.222$
There are 18 possible mantissas. Since only 3 possible exponents, in total there are 54 possible representable numbers.

![[Pasted image 20231219094830.png]]
$d_kb^k + d_{k-1}b^{k-1} + \cdots + d_1b^1 + d_0b^0$
$(((d_k)b + d_{k-1})b + \cdots + d_1)b + d_0$
Clearly this can be done in $k$ flops

![[Pasted image 20231219094842.png]]![[Pasted image 20231219094854.png]]
![[Pasted image 20231219094904.png]]
No as we would be performing the current 2 step process of factorizing then solving into 1 with all the same operations. As we are solving one system only this makes no change, but will be more expensive if solving for multiple systems.

![[Pasted image 20231219094915.png]]
F-test: $f(x_k) < \epsilon$ 
X-test: $|x_{k+1} - x_k| < \epsilon$ for some small defined epsilon (eg. machine epsilon)
![[Pasted image 20231219094928.png]]

![[Pasted image 20231219094939.png]]
$g(x) = x - \frac{x^3 - \alpha}{3x^2}$
It will not converge if we start at $x_0 = 0$ since $\lim_{x \to 0} \frac{x^3-\alpha}{3x^2} = \infty$
If we do not directly start at $0$ as it is obvious it will not converge, starting at any point such that a later iteration of $x_k = 0$ will also cause it not to converge.

Want $x - \frac{x^3 - \alpha}{3x^2} = 0$.
$\implies \frac{-2x^3-\alpha}{3x^2} = 0$
$\implies 2x^3 + \alpha = 0$
$\implies x = \sqrt[3]{-\frac{\alpha}{2}} = -\sqrt[3]{\frac{\alpha}{2}}$
Thus starting at $x_0 = -\sqrt[3]{\frac{\alpha}{2}}$ will not converge.

![[Pasted image 20231219094950.png]]
For it to be a fixed point we need:
$a^{\frac{1}{3}} = g(a^{\frac{1}{3}}) = pa^{\frac{1}{3}} + \frac{q a}{a^{\frac{2}{3}}} + \frac{ra^2}{a^{\frac{5}{3}}}$
$\implies a^{\frac{1}{3}} = pa^{\frac{1}{3}} + qa^{\frac{1}{3}} + ra^{\frac{1}{3}}$
$\implies p + q + r = 1$
For the highest order, we want to get the derivatives of the iteration $g(x)$ to vanish. Since we have 3 variables we can solve for, we still have 2 more equations we can create (aside from the above fixed point one) to create an iteration that is at least cubicly-convergent.
$g'(x) = p - \frac{2qa}{x^3}  -\frac{5ra^2}{x^6}$
$g'(a^{\frac{1}{3}}) = 0 \implies p - 2q - 5r = 0$

$g''(x) = \frac{6qa}{x^4} + \frac{30ra^2}{x^7}$
$g''(a^{\frac{1}{3}}) = 0 \implies q + 5r = 0$

Thus we have equations:
$$
\begin{cases}
p + q + r = 1 \\
p - 2q - 5r = 0 \\
q + 5r = 0
\end{cases}
$$
Solution is $p = \frac{5}{9}, q = \frac{5}{9}, r = \frac{1}{9}$
We can see that with this solution: $g'''(a^{\frac{1}{3}}) \ne 0$, thus is exactly cubic convergence.
<mark style="background: #FF5582A6;">For how error dependent, idk rate of convergence definition Solution does not make sense</mark>
![[Pasted image 20231219072621.png]]

![[Pasted image 20231219095001.png]]
Split into first fraction and the $W(x)$ term.
As said in lecture for the Runge function, the $n+1$ derivative would grow faster than the factorial denominator and dramatically increase the upper bound in error.
![[Pasted image 20231219095012.png]]
idk
The growth can be controlled slightly through the selection of interpolation points to form the $W(x)$ term as the first term is not really dependent on the actual points.
![[Pasted image 20231219095020.png]]
![[Pasted image 20231219095030.png]]
No, as the Runge function is not a polynomial, which is a nessecary condition for Weierstrass's theorem.

![[Pasted image 20231219095041.png]]
$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 \\
1 & 2 & 4 & 8 \\
1 & 3 & 9 & 27
\end{bmatrix}
\begin{bmatrix}
a_0 \\
a_1 \\
a_2 \\
a_3
\end{bmatrix}
=
\begin{bmatrix}
3 \\
7 \\
37 \\
141
\end{bmatrix}
$$
![[Pasted image 20231219095050.png]]
$p(x) = 3 + 4x + 13x(x-1) + 8x(x-1)(x-2)$
![[Pasted image 20231219095059.png]]
$p(x) = -6(x-1)(x-2)(x-3)y_0 + 2x(x-2)(x-3)y_1 -2x(x-1)(x-3)y_2 + 6x(x-1)(x-2)y_3$
![[Pasted image 20231219095107.png]]
If we have each $\ell_i(x)$ in the Lagrange form precomputed and saved, then both Divided differenace and Lagrange would take $O(n)$ flops to compute the new equation. However the constant would be smaller for Divided difference, and would thus be the best method.
![[Pasted image 20231219095116.png]]

![[Pasted image 20231219095142.png]]
reverse loop from n to 1

![[Pasted image 20231219095154.png]]
$Ax = b \implies PAx = Pb \implies PAQx = PQb \implies LUx = PQb$

![[Pasted image 20231219095210.png]]
First form: $g(x) = x - f(x)$, $g(x) = e^{-x}$
Second Form: $g(x) = x - h(x)f(x)$, $g(x) = x - \frac{x - e^{-x}}{1 + xe^{-x}}$
![[Pasted image 20231219095220.png]]
Root finding cannot to easily solved directly with generalizable method, conversion to fixed-point allows for use of general iterative formula.

![[Pasted image 20231219095511.png]]
![[Pasted image 20231219095519.png]]
![[Pasted image 20231219095526.png]]
![[Pasted image 20231219095534.png]]
From Vandermonde proof,
**Theorem:**
> For any sets $\{ x_i : i = 0, 1, \cdots, n \}, \{ y_i : i = 0, 1, \cdots, n  \}$ where $x_i$ are distinct, $y_i$ not necessarily distinct (it is an injection), $\exists$ a unique polynomial $p(x) \in \mathcal{P}_n$ such that $p(x_i) = y_i$
> ie. A unique degree $n$ (or less) polynomial can be made to fit $n + 1$ points.

Confirm that each data point is satisfied by plugging them in.
![[Pasted image 20231219095545.png]]
Newton's since you add another row to the table and perform $n$ computations for the new coefficient, and finally just add the term to the original. Lagrange is technically also linear but has more steps and converting to monomial has more steps.
![[Pasted image 20231219095747.png]]

![[Pasted image 20231219095756.png]]
![[Pasted image 20231219095811.png]]

![[Pasted image 20231219095917.png]]
![[Pasted image 20231219095925.png]]
![[Pasted image 20231219095931.png]]

![[Pasted image 20231219100102.png]]
#### Sol
![[Pasted image 20231219100901.png]]
#### Cont
![[Pasted image 20231219100129.png]]

![[Pasted image 20231219100203.png]]
![[Pasted image 20231219100222.png]]

![[Pasted image 20231219100233.png]]
#### Sol
![[Pasted image 20231219101211.png]]
#### Cont
![[Pasted image 20231219100335.png]]

![[Pasted image 20231219100343.png]]

![[Pasted image 20231219100406.png]]

![[Pasted image 20231219100450.png]]

![[Pasted image 20231219100529.png]]

![[Pasted image 20231219100545.png]]
![[Pasted image 20231219100619.png]]

![[Pasted image 20231219100733.png]]

![[Pasted image 20231219101308.png]]
![[Pasted image 20231219101318.png]]
#### Sol
![[Pasted image 20231219101331.png]]
#### Cont
![[Pasted image 20231219101404.png]]

![[Pasted image 20231219101440.png]]
![[Pasted image 20231219101447.png]]

![[Pasted image 20231219101456.png]]

![[Pasted image 20231219101522.png]]