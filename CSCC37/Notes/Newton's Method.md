---
tags:
  - CSCC37
---
# What is Newton's Method
For $f(x) = 0, f: \mathbb{R} \rightarrow \mathbb{R}$
$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}, k = 0, 1, 2, \ldots
$$
$f(x) = 0 \iff x = g(x)$ with $g(x) = x - \frac{f(x)}{f'(x)}$ which is second-form with $h(x) = \frac{1}{f'(x)}$.
Note that $h(x) \ne 0, \forall x$.
# Speed
Suppose $f(\tilde{x}) = 0$ but $f'(\tilde{x}) \ne 0$ (note the method can't work if the derivative is 0).
Applying Rate of Convergence Theorem,
$$
\begin{align}
g(x) &= x - \frac{f(x)}{f'(x)} \\
g'(x) &= 1 - \left( \frac{f'(x) f'(x) - f(x) f''(x)}{(f'(x))^2} \right) = \frac{f(x) f''(x)}{(f'(x))^2} \\
&\implies g'(\tilde{x}) = \frac{f(\tilde{x}) f''(\tilde{x})}{(f'(\tilde{x}))^2} = 0
\end{align}
$$
Thus Newton's method is ***at least*** quadratically convergent (it is exactly quadratically but we won't do the second derivative since pain).
# Geometric Interpretation
Want to solve $f(x) = 0$.
Consider that for a small interval, the $f(x)$ is essentially linear if you look at the small interval.
At the iterate $x_k$, approximate (or model) f(x) by a linear polynomial $p(x)$ that satisfies $p(x_k) = f(x_k)$ and $p'(x_k) = f'(x_k)$, which is the tangent of $f$ at $x_k$.
$$
\implies p_k(x) = f(x_k) + (x-x_k)f'(x_k)
$$
Then $x_{k+1}$ is the root of $p_k(x), ~p_k(x_{k+1}) = 0$.
$$
\begin{align}
&\implies f(x_k) + (x_{k+1} - x_k) f'(x_k) = 0 \\
&\implies x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
\end{align}
$$
![[Pasted image 20231110112259.png]]
Newton's method may not converge in some cases. Such as if we get to a position where $f'(x_k) = 0$. Or we start on the "wrong" side of a downward concave that never crosses the x-axis.
![[Pasted image 20231110113757.png]]
# Example $f(x) = x - e^{-x}$
$$
\begin{align}
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)} &= x_k - \frac{x_k - e^{-x_k}}{1+e^{-x_k}} \\
&= \frac{(1+x_k)e^{-x_k}}{1+e^{-x_k}}
\end{align}
$$
Starting from $\hat{x}_0 = 0.936$ it would take around 4 steps to converge (7 digits correct).