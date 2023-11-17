# Vector Norm Definition
$||v||$ is a vector norm if it satisfies the following:
1. $||v|| \ge 0, \forall v$
2. $||v|| = 0 \iff v = 0$
3. $||v + w|| \le ||v|| + ||w||$ Triangle Inequality
4. For scalar $a$, $||av|| = |a|\cdot||v||$
## Example Vector Norms
2-norm: $||v||_2 = \sqrt{v_1^2 + \cdots + v_n^2}$
$p$-norm: $||v||_p = \sqrt[p]{|v_1|^p + \cdots + |v_n|^p}$
Infinity-norm: $||v||_\infty = \max_{1 \le i \le n} (|v_i|)$

# Matrix Norm
A vector norm in a vector space where vectors are (square) matrices.
Alongside the regular conditions it should also satisfy:
- $||AB|| \le ||A||~||B||$ Sub-multiplicative
## Matrix induced $p$-norm
$||A||_p = \sup \frac{||Ax||_p}{||x||_p}$ for $x \ne 0$
1-norm: $||A||_1 =$ max absolute column sum
Infinity-norm: $||A||_\infty =$ max absolute row sum
