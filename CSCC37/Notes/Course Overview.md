---
tags:
  - CSCC37
---
# What is Numerical Analysis
Used for examining Physical Systems as Mathematical models (for simulation) since analyzing the physical system directly is usually hard and costly
- Weather/Climate Change prediction
- Automotive Design
- Some models
	- Linear Equations
	- Non-linear Equations
	- Differential Equations
	- Integral Equations
- In rare cases, the models have other analytic (closed-form) solution
- In the other cases, we need a Numerical solution
	- may even choose numerical solution over analytical solution due to speed/cost
## Floating point Arithmetic
- Representing (storing/arithmetic on) real numbers on a computer
- Can numbers be represented exactly?
	- $\pi$ No
	- $\sqrt{2}$ No
	- $\frac{1}{10}$ No, floating point error from base conversion to binary (which becomes an infinite string)
	- Many cannot since it theoretically requires unlimited memory to store the digits (no pattern or cycles)
	- **Initial Rounding Error**
- **Error Propagation** (after rounding error)
	- *Notation:* **Mantissa** - section of float number after the decimal point
	- **Subtractive/Catastrophic Cancellation** - occurs whenever the result of addition or subtraction is much smaller in magnitude than the operands
		- Example: For 4 digit mantissa computer with rounding
			- True solution for:
				$0.1234367 - 0.1234216 = 0.151 \times 10^{-4}$
			- But in this computer, both values are first rounded to 4 digits, then computed:
				$0.1234 - 0.1234 = 0$
- Condition/Stability of algorithms
	- Numerical measure of how small changes to the input in a function/algorithm are propagated to the output of function/algorithm
		- Greater value means more sensitive to things like round-off error
	- Conditioning refers to functions
		- `cond(F)` returns the condition of the function
	- Stability refers to algorithms
## [[Linear Systems of Equations]]
- Solve $A\vec{x} = \vec{b}, A \in \mathbb{R}^{n \times n}, \vec{b} \in \mathbb{R}^{n}$ to find $\vec{x}$
	- $A$ **must be square**
- Utilize different techniques in context of computing and determine its sensitivity
	- *Direct Methods*
		- Gaussian Elimination
			- Factor $A = LU$ where $L$ is *unit lower triangular matrix* (diagonal is all $1$), $U$ is *upper triangular matrix* (**LU Factorization**)
			- $A\vec{x} = \vec{b} \iff LU\vec{x} = \vec{b}$, let $\vec{d} = U\vec{x}$
			- Solve $L\vec{d} = \vec{b}$, for $\vec{d}$ . This becomes easy due to the structure of $L$. (**Forward Elimination**)
			- Solve $U\vec{x} = \vec{d}$, for $\vec{x}$. Similar method to previous step. (**Backward Substitution**)
			- Error can propagate through all the subtractions and multiplications performed
			- Time complexity: $O(n^3)$
	- *Iterative Methods
		- Alternative to direct methods that may be faster or more stable in certain scenarios
		- *Some algorithm we don't have name for*
			- Split $A = L + D + U$, where $L$ is *strict lower triangle matrix* (diagonal is also 0), $D$ is a *diagonal matrix*, $U$ is a *strict upper triangle matrix*
			  $$
			 \begin{aligned}
			 A\vec{x} = b
			 &\iff L\vec{x} + D\vec{x} + U\vec{x} = \vec{b} \\
			 &\iff D\vec{x} = -(L+U)\vec{x} + \vec{b}
			 \end{aligned}
			 $$
			- Solve $D\vec{x} = -(L+U)\vec{x} + \vec{b}$ for $\vec{x}$ iteratively
				- $D\vec{x_{k+1}} = -(L+U)\vec{x_{k}} + \vec{b}$ for $k = 0, 1, 2, \ldots$ until convergence ^iterative-algo
					- Iterative Refinement (to possibly improve the final solution $\hat{x}$)
					- **X-test** - convergence can be when $||\vec{x_{k+1}} - \vec{x_k}|| < \epsilon$ for some small epsilon like $10^{-16}$
					- **F-test** - measure $||\vec{b} - A\vec{x_{k}}|| < \epsilon$
					- Often use both tests
				- Start with initial guess of $\vec{x_{0}} = 0$
				- Time complexity hinges on how long until convergence
					- if less than $n^2$ then faster than Gaussian Elimination else slower
## Single non-Linear Equations
- Given $F: \mathbb{R} \rightarrow \mathbb{R}$, Solve $F(x) = 0$ for $x \in \mathbb{R}$
	- Is there solution? If so, how many?
- Usually no simple, closed form formula
- Algorithms for these are based on the *Fixed Point Problem*
	  $$
	 F(x) = 0 \iff x = g(x)
	 $$
	- Can always use $g(x) = x - F(x)$ or $g(x) = x - h(x)F(x)$ where h(x) is some other auxiliary function (but must also check if we get $h(x) = 0$ instead of $F(x) = 0$)
	- Right side has an iterative algorithm (**Fixed Point Iteration**)
		- Same idea as previous section [[#^iterative-algo]]
## Approximation & Interpolation
## Data Fitting 
- Regression
	- Find line $a_0 + a_1t = y$ that goes through $\{(t_0, y_0), (t_1, y_1\}$
		- $\begin{bmatrix} 1 & t_0 \\ 1 & t_1\end{bmatrix} \begin{bmatrix} a_0 \\ a_1 \end{bmatrix} = \begin{bmatrix} y_0 \\ y_1 \end{bmatrix}$
	- Find line through 3 points of a line, 3 points 2 variables (3 row 2 column matrix)
		- Issue as matrix not square, cannot use [[#System of Linear Equations|Linear System Techniques]]
		- Overdetermined (more rows than columns) **<mark style="background: #FFB8EBA6;">(In D37)</mark>**
			- No unique solution
			- Instead, try to find *best possible* fit
				- Find $a_0, a_1$ such that $||A\vec{x}-b||_2$ is minimize
		- Underdetermined (more columns than rows) **<mark style="background: #FFB8EBA6;">(In D37)</mark>
			- Infinitely many solutions
			- Look for *family of solutions*
	- Piecewise interpolation
			- For 3 points, find 2 lines that connect $p_1$ to $p_2$, then another to connect $p_2$ to $p_3$
				- problem is this interpolation is not smooth due to cusps
					- Not $C_1$ continuous (first derivative as not present at all points)
					- not for graphics
## Numerical Integration / Quadrature
- Estimate $\int_{a}^{b}F(x)dx$
	- Can be piecewise interpolated exactly such that each section has a simple equation
		- This breaks up the area under the curve to be a sum of the area of many trapezoids (this is using degree 1)
		- Using degree 0 is rectangles and it becomes a Riemann Sum