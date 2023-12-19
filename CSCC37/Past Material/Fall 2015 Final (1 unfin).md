# Q4
![[Pasted image 20231218041017.png]]
## a
$g_1$ is the first form of $f$ so it can be used
$g_4$ is a second form of $f$ with $h(x) = \frac{1}{x^2}$
## b Which variation of g should be used, and why?
**IDK**
## c Derive an even better variation of g for use in this problem, and explain why it is better.
By the Rate of Convergence Theorem and taking the derivatives of the above variations of g, we get that they converge linearly. Consider the variation of g from using Newton's Method:
$$
g(x) = x - \frac{x^2 - 2}{2x}
$$
We know that Newton's Method converges quadratically which is better than linearly.
# Q5
![[Pasted image 20231218054116.png]]
## a
| $x$ | $y[x_i]$ | $y[x_{i+1}, x_i]$ | $y[x_{i+2}, x_{i+1}, x_i]$ | $y[x_{i+3}, x_{i+2}, x_{i+1}, x_i]$ |
|-|-|-|-|-|
|-1|4||||
|||$\frac{6-4}{0-(-1)}=2$|||
|0|6||$\frac{6-2}{1-(-1)}=2$||
|||$\frac{12-6}{1-0}=6$|||
|1|12||||
$p(x) = 4 + 2(x+1) + 2(x+1)(x)$
## b Derive the Lagrange form
$p(x) = \sum_{i=0}^{n} \ell_i(x) y_i$
$\ell_i(x) = \prod_{j=0, j\ne i}^{n} \frac{x - x_j}{x_i - x_j}$
$\ell_0(x) = \frac{x - x_1}{x_0 - x_1} \frac{x - x_2}{x_0 - x_2} = \frac{x - 0}{-1-0} \frac{x - 1}{-1 - 1} = \frac{x(x-1)}{2}$
$\ell_1(x) = \frac{x + 1}{1} \frac{x - 1}{-1} = -(x^2-1)$
$\ell_2(x) = \frac{x + 1}{1 + 1} \frac{x}{1} = \frac{x(x+1)}{2}$
$p(x) = 2x(x-1) - 6(x^2 - 1) + 6x(x+1)$
## c Verify both polynomials are the same by converting to monomial basis
From a: $p(x) = 4 + 2x + 2 + 2x^2 + 2x = 6 + 4x + 2x^2$
From b: $p(x) = 2x^2 - 2x - 6x^2 + 6 + 6x^2 + 6x = 6 + 4x + 2x^2$
Which is the same
## d
![[Pasted image 20231218061219.png]]

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
## e
![[Pasted image 20231218061843.png]]
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