# Q1
![[Pasted image 20231218062445.png]]
## a
Base 3: $(0.100)^{-1}$
Base 10: $3^{-2}$
## b
Base 3: $(0.222)^{1}$
Base 10: $2 \cdot 3 + 2 \cdot 3^{-1} + 2 \cdot 3^{-2}$
## c
$\frac{1}{2}b^{-2}$
## d
Cannot be represented as it is outside of the representable domain of this system.
## e
$(0.120)$
## f
$0.100, 0.101, 0.102, 0.110, 0.111, 0.112, 0.120, 0.121, 0.122, 0.200, 0.201, 0.202, 0.210, 0.211, 0.212, 0.220, 0.221, 0.222$
There are 18 possible mantissas. Since only 3 possible exponents, in total there are 54 possible representable positive numbers. Then double for negatives 108.
# Q2
![[Pasted image 20231219055136.png]]
$d_kb^k + d_{k-1}b^{k-1} + \cdots + d_1b^1 + d_0b^0$
$(((d_k)b + d_{k-1})b + \cdots + d_1)b + d_0$
Clearly this can be done in $k$ flops
# Q3
![[Pasted image 20231219055619.png]]
## c
No as we would be performing the current 2 step process of factorizing then solving into 1 with all the same operations. As we are solving one system only this makes no change, but will be more expensive if solving for multiple systems.
# Q4
![[Pasted image 20231219061603.png]]
## a
F-test: $f(x_k) < \epsilon$ 
X-test: $|x_{k+1} - x_k| < \epsilon$ for some small defined epsilon (eg. machine epsilon)
## c
$g(x) = x - \frac{x^3 - \alpha}{3x^2}$
It will not converge if we start at $x_0 = 0$ since $\lim_{x \to 0} \frac{x^3-\alpha}{3x^2} = \infty$
If we do not directly start at $0$ as it is obvious it will not converge, starting at any point such that a later iteration of $x_k = 0$ will also cause it not to converge.

Want $x - \frac{x^3 - \alpha}{3x^2} = 0$.
$\implies \frac{-2x^3-\alpha}{3x^2} = 0$
$\implies 2x^3 + \alpha = 0$
$\implies x = \sqrt[3]{-\frac{\alpha}{2}} = -\sqrt[3]{\frac{\alpha}{2}}$
Thus starting at $x_0 = -\sqrt[3]{\frac{\alpha}{2}}$ will not converge.
# Q5
![[Pasted image 20231219065332.png]]
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
$\frac{|x_{k+1} - a^{\frac{1}{3}}|}{|x_k - a^{\frac{1}{3}}|}$
# Q6
![[Pasted image 20231219072713.png]]
# a
Split into first fraction and the $W(x)$ term.
As said in lecture for the Runge function, the $n+1$ derivative would grow faster than the factorial denominator and dramatically increase the upper bound in error.
## b
idk
The growth can be controlled slightly through the selection of interpolation points to form the $W(x)$ term as the first term is not really dependent on the actual points.
## c
 draw the bell with bad interp
## d
No, as the Runge function is not a polynomial, which is a nessecary condition for Weierstrass's theorem.
# Q7
![[Pasted image 20231219081000.png]]
## a
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
## b Newton form
$p(x) = 3 + 4x + 13x(x-1) + 8x(x-1)(x-2)$
## c Lagrange form
$p(x) = -6(x-1)(x-2)(x-3)y_0 + 2x(x-2)(x-3)y_1 -2x(x-1)(x-3)y_2 + 6x(x-1)(x-2)y_3$
Then expand to confirm
## d Which method best if adding new interp points
If we have each $\ell_i(x)$ in the Lagrange form precomputed and saved, then both Divided differenace and Lagrange would take $O(n)$ flops to compute the new equation. However the constant would be smaller for Divided difference, and would thus be the best method.
## e create spline that interp
do thing