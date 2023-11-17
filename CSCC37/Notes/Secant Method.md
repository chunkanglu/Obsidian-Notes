---
tags:
  - CSCC37
---
For when you can't get $f'(x)$ easily (hard to solve or expensive) for [[Newton's Method]].
Approximate $f'(x_k)$ by its secant:
$$
f'(x_k) \approx \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}
$$
$$
\implies x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}
$$
# Geometric Interpretation
![[Pasted image 20231110120737.png]]
$$
p_k(x) = f(x_k) + (x - x_k) \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}
$$
Let $x_{k+1}$ be the root of $p_k(x)$, $p_k(x_{k+1}) = 0$.
$$
\implies f(x_k) + (x - x_k) \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}} = 0
$$
$$
\implies x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}
$$
# Important Note
This is not a fixed point iteration anymore in the form $x_{k+1} = g(x_k)$.
Cannot directly use Fixed Point Theorem or Rate of Convergence Theorem to analyse the Secant Method.
# Speed
~~(With some adjustments, can prove that the rate of convergence is $p = \frac{1 + \sqrt 5}{2} \approx 1.62$ since it related to Fibonacci numbers)~~
It is *Super Linear* convergence since $p > 1, p < 2$ so not (theoretically) as fast as Newton's Method (in terms of number of iterations).
**However,** you don't need to evaluate 2 function calls like in Newton's $f(x_k), f'(x_k)$
Actually only 1 which is $f(x_k)$ since $f(x_{k-1})$ has already been calculated in a previous iteration and can be stored.
So 2 steps of Secant Method costs roughly the same as 1 step of Newton's Method (assuming both functions cost the same amount to call).
The **effective** rate of convergence (ie. real time) takes into account cost per iteration as well as number of iterations.
So the Secant method is effectively faster than Newton's Method.

