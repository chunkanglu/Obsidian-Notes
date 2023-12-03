# Main Problem
Approximate $I(f) = \int_{a}^{b} f(x) dx$
- $f(x)$ may not have closed-form anti-derivative
- anti-derivative may be very expensive to calculate
# Riemann Sums
$$
R(f) = \sum_{i = 0}^{N - 1} f(\eta_i) (x_{i+1} - x_i)
$$
where $a \equiv x_0 \le \eta_0 \le x_1 \le \eta_1 \le x_2 \le \cdots \le x_N \equiv b$
- commonly chosen $\eta_i$ is left endpoint $x_i$, right endpoint $x_{i+1}$, or midpoint $\frac{x_{i+1} + x_i}{2}$
![[Pasted image 20231201104017.png]]
- Riemann Sum is a **Composite Rule**
	- Apply a simple formula like above to many short sub-intervals and then sum all results 
# Basic Formulas (Interpolatory Quadrature)
- Based on interpolating polynomial
Approximate $f(x)$ by $p(x)$ on $[a, b]$ (or $x_i, x_{i+1}$)
Then $I(f) \approx Q(f) = I(p) = \int_{a}^{b} p(x) dx$
## Lagrange Form
$$
p(x) = \sum_{i = 0}^{n} f(x_i)\ell_i(x), ~ p(x) \in $\mathcal{P}_n$
$$
Standard Form of a Quadrature Rule $Q(f) = \sum_{i = 0}^{n} A_i f(x_i)$
$$
\begin{align}
Q(f) = I(p)
&= \int_{a}^{b} p(x) dx \\
&= \int_{a}^{b} \sum_{i = 0}^{n} f(x_i)\ell_i(x) dx \\
&= \sum_{i = 0}^{n} f(x_i) \int_{a}^{b} \ell_i(x) dx \\
&= \sum_{i = 0}^{n} A_i f(x_i) & \text{where } A_i = \int_{a}^{b} \ell_i(x) dx
\end{align}
$$
- $A_i$ - weights
- $x_i$ - nodes
- However for $A_i$, $\ell_i(x)$ is **pain** to actually integrate, and will not compute the weights this way
- **Note:** $Q(f)$ is a *linear operator*
	- $Q(\alpha F + g) = \alpha Q(f) + Q(g)$
	- For functions $f$ and $g$, $\alpha \in \mathbb{R}$

If $Q(f)$ integrates $1, x, x^2, \cdots, x^n$ exactly and $Q(f)$ is a linear operator, then $Q(f)$ *integrates all polynomials exactly*.
## Theorem: Existence of Interpolatory Quadrature Rules
1. Given any set of $n+1$ *distinct* nodes, can choose the weights $A_i$ such that the quadrature rule is *exact for all polynomials of degree* $\le n$.
2. Weights $A_i$ are *unique* (only one such quadrature rule)
#### Proof
Since $Q(f)$ is a linear operator, we only need to show $Q$ is exact for $1, x, x^2, \cdots, x^n$.
For the $x^k$:
$$
Q(x^k) = \sum_{i = 0}^{n} A_i x_i^k = \int_a^b x^k dx = \frac{1}{k+1} \left( b^{k+1} - a^{k+1} \right)
$$
Have $n + 1$ equations (for each monomial) with $n + 1$ unknowns $A_i$.
Solve the following system for the weights $A_i$:
$$
\begin{align}
k = 0 \\
k = 1 \\
k = 2 \\
\vdots \\
k = n
\end{align}

\quad

\begin{bmatrix}
1 & 1 & \cdots & 1 \\
x_0 & x_1 & \cdots & x_n \\
x_0^2 & x_1^2 & \cdots & x_n^2 \\
\vdots & \vdots & \vdots & \vdots \\
x_0^n & x_1^n & \cdots & x_n^n
\end{bmatrix}
\begin{bmatrix}
A_0 \\
A_1 \\
A_2 \\
\vdots \\
A_n
\end{bmatrix}
=
\begin{bmatrix}
b - a \\
\frac{b^2 - a^2}{2} \\
\frac{b^3 - a^3}{3} \\
\vdots \\
\frac{b^{n+1} - a^{n+1}}{n+1}
\end{bmatrix}
$$
**Note:** This is the transpose of the Vandermonde matrix
Prove that this is invertible (so that this is solvable):
- Using the same argument [[Approximation and Interpolation#Vandermonde (Method of Undetermined Coefficients)|as before]] by proving rows are linearly independent. 

Thus we can get the weights $A_i$ without explicit integration of Lagrange basis.
## Precision
If $m$ is the largest natural such that $Q$ integrates all polynomials of degree $\le m$ exactly, then *the precision of* $Q$ *is* $m$.
- $m$ may be greater than $n$ (ie. $Q$ may work well for polynomials that it may not be explicitly defined for)
## Simple Rules
For $I(f) = \int_a^b f(x) dx$.
### Midpoint Rule $n = 0$
![[Pasted image 20231201114910.png|400]]
$I(f) \approx M(f) = I(p_0) = (b - a) f(\frac{a+b}{2})$
where weight $A_0 = b - a$ and node $x_0 = \frac{a + b}{2}$
Derived geometrically.
**Note:** $n = 0$ (degree of the interpolating polynomial). Lets consider the precision:
- $M(x^0) = M(1) = b - a = I(1)$. This is as defined.
- $M(x^1) = M(x) = (b - a) \left( \frac{a + b}{2} \right) = \frac{b^2 - a^2}{2} = I(x)$. So it integrates a line exactly.
- $M(x_2) = (b - a) \left( \frac{a + b}{2} \right)^2 \ne \frac{b^3 - a^3}{3} = I(x^2)$
- Thus precision $m = 1$
*Why is the midpoint rule precision $m = 1$?*
![[Pasted image 20231201120403.png|400]]
### Trapezoidal Rule $n = 1$
![[Pasted image 20231201120646.png|400]]
$I(f) \approx T(f) = I(p_1) = (b - a) \left( \frac{f(a) + f(b)}{2} \right) = \frac{b - a}{2} \left( f(a) + f(b)\right)$
- Derived geometrically (without transpose Vandermonde)
- Weights $A_0 = \frac{b - a}{2}, A_1 = \frac{b - a}{2}$
- Nodes $x_0 = a, x_1 = b$
*Precision of Trapezoidal Rule*
- $T(x^0) = (b - a) (\frac{1 + 1}{2}) = b - a =  I(1)$
- $T(x^1) = (b - a) \left( \frac{a + b}{2} \right) = \frac{b^2 - a^2}{2} = I(x)$
- $T(x^2) = (b - a) \left( \frac{a^2 + b^2}{2} \right) \ne \frac{b^3 - a^3}{3} = I(x^2)$
- Thus precision is $m = 1$
### Simpson's Rule $n = 2$
Choose outer 2 points $a, b$ as well as midpoint.
![[Pasted image 20231201121803.png|400]]
$I(f) \approx S(f) = I(p_2) = \frac{b - a}{6} \left( f(a) + 4f\left(\frac{a + b}{2}\right)  + f(b) \right)$
- $A_0 = \frac{b - a}{6}, A_1 = \frac{2}{3}(b-a), a_2 = \frac{b-a}{6}$
- $x_0 = a, x_1 = \frac{a+b}{2}, x_2 = b$
*Precision of Simpson's Rule*
- $S(x^0), S(x^1), S(x^2)$ must work as it is defined for it
- $S(x^3) =$ <mark style="background: #FF5582A6;">TODO</mark>
## Error in Interpolatory Quadrature
$$
\begin{align}
e_n &= I(f) - Q_n(f) \\
&= \int_a^b \left(f(x) - p_n(x)\right) dx \\
&= \int_a^b \frac{f^{(n+1)}(\eta)}{(n+1)!} \prod_{i=0}^{n} (x - x_i) dx & \text{See (*)}
\end{align}
$$

where $Q_n$ is quadrature rule based off of $n$ nodes.
(\*) - from [[Approximation and Interpolation#Error in Polynomial Interpolation|Error in Polynomial Interpolation]]

## Will interpolatory quadrature rules converge to $I(f)$ as $n$ increases to infinity?
**Theorem:** Let $f \in C[a, b]$ and $Q_n(f) = \sum_{i = 0}^{n} A_i^{(n)} f\left(x_i^{(n)}\right)$
Then $\lim_{n \to \infty} Q_n(f) = I(f) \iff \exists$ constant $k$ st. $\sum_{i = 0}^{n} \left|A_i^{(n)}\right| \le k, \forall n$
<mark style="background: #FFB86CA6;">What about the Runge Phenomenon? do the oscillations cancel out?</mark>
oscillations symmetric about x-axis
interpolant becomes so dense it does things
