---
tags:
  - CSCC37
---
Always finds a root, but is slow.
# Algorithm (its just binary search)
Find bracket $a \le b$ such that $f(a)  \le 0 \le f(b)$ or $f(b) \le 0 \le f(a)$. Crosses axis. $\implies$ at least 1 root of $f(x)$ in $[a, b]$
WLOG $f(a)  \le 0 \le f(b)$
1. Loop until $b-a$ small enough
	1. $m = (a + b) / 2$
	2. If $f(m) \le 0$ then $a := m$
	3. Else $b := m$

Interval contracts by $\frac{1}{2}$ at each step and will always have at least one root in $[a, b]$.
# Speed
Linear convergence