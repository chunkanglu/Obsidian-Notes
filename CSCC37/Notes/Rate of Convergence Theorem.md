---
tags:
  - CSCC37
---
# Theorem
For the Floating Point Iteration $x_{k+1} = g(x_{k})$, if $g'(\tilde{x}) = g''(\tilde{x}) = \cdots = g^{p-1}(\tilde{x}) = 0$, but $g^{p}(\tilde{x}) \ne 0$, then we have exactly $p^{th}$ order convergence.
Note if $g^{p}(\tilde{x}) = 0$, then just increase $p$ by $1$ and we have $(p+1)^{th}$ convergence.
## Examples
If only $g'(\tilde{x}) = 0$, then quadratically convergent.
If $g'(\tilde{x}) = g''(\tilde{x}) = 0$, then cubically convergent.
## Proof
$$
\begin{align}
x_{k+1} = g(x_{k}) &= g(\tilde{x} + (x_{k}-\tilde{x}))  \\
&= g(\tilde{x}) + (x_{k}-\tilde{x})g'(\tilde{x}) + \frac{(x_k - \tilde{x})^2}{2!}g''(\tilde{x}) + \ldots + \frac{(x_k - \tilde{x})^{p-1}}{(p-1)!}g^{(p-1)}(\tilde{x}) + \frac{(x_k - \tilde{x})^{p}}{(p)!}g^{(p)}(\eta_k) & \text{where $\eta_k \in [\tilde{x}, x_k]$}
\end{align}
$$
<mark style="background: #FF5582A6;">wtf is the above "taylor expansion" thats not how it works</mark>
Suppose $g'(\tilde{x}) = g''(\tilde{x}) = \cdots = g^{p-1}(\tilde{x}) = 0$, then the above Taylor Expansion becomes:
$$
x_{k+1} = g(\tilde{x}) + \frac{(x_k - \tilde{x})^{p}}{(p)!}g^{(p)}(\eta_k) \iff \frac{x_{k+1} - \tilde{x}}{(x_k - \tilde{x})^p} = \frac{1}{p!}g^{p}(\eta_k)
$$
As $k \rightarrow \infty, x_k \rightarrow \tilde{x}$ and $\eta_k \in [\tilde{x}, x_k]$, the interval is shrinking so $\eta_k \rightarrow \tilde{x}$.
Taking the limit as $k \rightarrow \infty$ and since $g^{p}(\tilde{x}) \ne 0$, we have:
$$
\lim_{x_k \rightarrow \tilde{x}} \frac{|x_{k+1} - \tilde{x}|}{|(x_k - \tilde{x})^p|} =
\lim_{\eta_k \rightarrow \tilde{x}} \frac{1}{p!} |g^{p}(\eta_k)| \ne 0
$$
Which is exactly the definition of Rate of Convergence.