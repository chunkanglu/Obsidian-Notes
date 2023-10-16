## Representation of Non-Negative Integers (in Computing)
For a base $b$ system, $b \in \mathbb{N}, b > 0$.
For some $x$ in base $b$, $x \ge 0, x \in \mathbb{N}, 0 \le d_i < b$ for $i = 0, 1, ... n$, $x = (d_n, d_{n-1}, ..., d_1, d_0)_b = d_n \cdot b^n + ... + d_0 \cdot b^0$ is the binary to decimal conversion
- Computers work in base 2 (binary), we usually work with base 10 (decimal)
#### Convert Decimal to Binary
Example: $(350)_{10}$ to base 2
	Keep dividing by 2 until quotient is 0, keeping track of quotient and remainder, then read Remainder bottom up.

| Numerator | Denominator | Quotient | Remainder |
|-----------|-------------|----------|-----------|
| 350       | 2           | 175      | 0         |
| 175       | 2           | 87       | 1         |
| 87        | 2           |          |           |

- Conversion is **safe** (for natural numbers) and does not lose information, as long as it fits in memory (overflow)
# Representation of Real numbers
For $x \in \mathbb{R}$, $x = \pm (x_I . x_F)_b = \pm (d_n d_{n-1} \ldots d_1 d_0 . d_{-1} d_{-2} \ldots)_b$, separation of $x_I$ the integral, $x_F$ the fractional part, the sign can be stored in one bit.
- $x_I$ can be converted using above
- $x_F$ can cause problems due to infinite digits

For base $b$ system, $x_f = (. d_{-1} d_{-2} \ldots)_b = (\sum_{i=1}^{\infty} d_{-i} b^{-i})_{10}$
- A terminating **binary** fraction with $n$ digits has a terminating **decimal** fraction representation
- A terminating **decimal** fraction may **<mark style="background: #FF5582A6;">**NOT**</mark>** have a terminating **binary** fraction representation (See below Example 2)
#### Converting Decimal to Base $b$
Example 1: Convert $(.625)_{10}$ to binary.
Keep multiplying by the base until the fraction is 0. 

| Multiplier | Base | Product | Integral | Fraction |
|------------|------|---------|----------|----------|
| .625       | 2    | 1.25    | 1        | .25      |
| .25        | 2    | 0.5     | 0        | .5       |
| .5         | 2    | 1.0     | 1        | 0        |
Read top down. $(.625)_{10} = (.101)_2$

Example 2: Convert $(.1)_{10}$ to binary.

| Multiplier | Base | Product | Integral | Fraction |
|------------|------|---------|----------|----------|
| .1         | 2    | 0.2     | 0        | .2       |
| .2         | 2    | 0.4     | 0        | .4       |
| .4         | 2    | 0.8     | 0        | .8       |
| .8         | 2    | 1.6     | 1        | .6       |
| .6         | 2    | 1.2     | 1        | .2       |
| .2         | 2    | 0.4     | 0        | .4       |
Problem is that it is repeating. $(.1)_{10} = (.0\overline{0011})_2$

## Machine Representation of Reals
Reals represented on a computer as Floating Point Number (FP#s).
An floating point number in base $b$ has the form $x = (F)_b . b^{(e)_b}$
Where:
- $b$ is the **base** of the computing device
- $F = \pm (. d_1 d_2 \ldots d_t)_b$ is the **mantissa**
	- By our convention, $0 \le$ |mantissa| $< 1$, it is fractional
- $e = \pm (c_s c_{s-1} \ldots c_2 c_1)_b$ is the **exponent**
	- Exponent is limited (due to $s$ digits), $-M \le e \le M$ where $M = (a_1a_2\ldots a_n)_b$ where  each $a_i = b-1$ the largest digit, essentially $M$ is the largest possible representable number
A floating point number is **normalized** if $d_1$ is non-zero unless all digits are 0. Since $0.1 = 0.01 \times 10 = 0.001 \times 100 \ldots$ there is an infinite number of representations.

**Significant digits** (of a non-zero floating point number) are the digits following and including the first non-zero digit (of the mantissa).
- All digits of the mantissa of a normalized floating point number are significant

## Domain of Floating Point Numbers
Largest possible Floating point number in absolute value is:
- $(\underbrace{aa\ldots a}_\text{t})b \cdot b^{(\underbrace{aa \ldots a}_s)_b}$ where first set of $a$ is $t$ times, second set of $a$ is $s$ times
Smallest possible Floating point number in absolute value (non-zero), ie. closest value to 0 is:
- $(\underbrace{.100 \ldots 0}_t)_b \cdot b^{-(\underbrace{aa \ldots a}_s)_b}$ normalized, where $a = b-1$
- $(\underbrace{.00 \ldots 1}_t)_b \cdot b^{-(\underbrace{aa \ldots a}_s)_b}$ non-normalized

$\mathbb{R}_b(t, s)$ is the set of all floating point number of base $b$ with absolute value inside these ranges.
- **Note:** that this set is **finite** unlike real numbers since we are limited by digits after decimal point (in there is an infinite number of real number between any 2 real numbers, but this is not the case here)
	- Precisely, $\mathbb{R}$ is **compact** whereas $\mathbb{R}_b(t, s)$ is not
	- There are no floating point number between two consecutive floating point numbers (actually there isn't even *consecutive* real numbers in the first place)

**Overflow** or **Underflow** occur when a non-zero floating point number is outside the ranges tries to be stored, ie. too large or too small.

## Converting real number $x \in \mathbb{R}$ as $Fl(x) \in \mathbb{R}_b(t, s)$
1. Normalize mantissa
2. Truncate or round (depending if the last digit is $\ge \frac{b}{2}$ or $< \frac{b}{2}$) mantissa
	- Alternatively add $\frac{b}{2}$ to the number then truncate (equivalent to rounding and saves an if-statement cost)
Example:
- In $\mathbb{R}_b(2, 4)$
	- $$
	  \begin{equation}
		Fl(\frac{2}{3}) =
		\begin{cases}
			0.66 & \text{truncate} \\
			0.67 & \text{round}
		\end{cases}
	  \end{equation}
	  $$
## Round Off Error
The difference between $x \in \mathbb{R}$ and $Fl(x) \in \mathbb{R}_b(t, s)$ usually measured relative to $x$
$$\delta = \frac{x - Fl(x)}{x}, Fl(x) = x(1-\delta)$$
$\delta$ is the Relative Round off
- can be bound independently of $x$
	- $\delta < b^{1-t}$ for truncated normalized floating point numbers
	- $|\delta| < \frac{1}{2}b^{1-t}$

## Machine Arithmetic
Let $x, y \in \mathbb{R}$ and $Fl(x), Fl(y) \in \mathbb{R}_b(t,s)$
Consider $\circ \in \{+, -, \cdot, /\}$, does computer give:
- $x \circ y$? **NO**
- $Fl(x) \circ Fl(y)$? **NO**
> Computer actually gives $Fl(Fl(x) \circ Fl(y))$

Example:
- In $\mathbb{R}_{10}(2, 4)$
	- $x = 2, y = 0.0000058, x + y = 2.0000058$
	- $Fl(x) = (+0.20 \cdot 10^1)_{10}$
	- $Fl(y) = (+ 0.58 \cdot 10^{-5})_{10}$ 
	- $Fl(x) + Fl(y) = 0.20000058 \cdot 10^1$ (temp) not actually able to be stored in computer
	- $Fl(Fl(x) + Fl(y)) = 0.20 \cdot 10^1$
## Machine Precision (Machine Epsilon)
> The smallest non-normalized floating point number $eps$ such that $1+eps > 1$ 

$$
\begin{equation}
	eps =
	\begin{cases}
		b^{1-t} & \text{chopping} \\
		\frac{1}{2}b^{1-t} & \text{rounding}
	\end{cases}
\end{equation}
$$
Machine Precision, by above definition is the bound for Relative Round Off
$$\delta = \frac{x - Fl(x)}{x} \implies
\begin{equation}
	\begin{cases}
		0 \le \delta \le eps & \text{chopping} \\
		-eps \le \delta \le eps & \text{rounding}
	\end{cases}
\end{equation}
$$
## How is error propagated
How exactly is error propagated in each of $\overline{\circ} \in \{+, - \cdot, /\}$, where $\overline{\circ}$ is machine implementation of $\circ$.

Let $x, y \in \mathbb{R}$. $Fl(x) = x(1-\delta_x), Fl(y) = y(1 - \delta_y)$
- $x \cdot y$
	- Computer gives following,
$$
\begin{align*}
  Fl(Fl(x) \cdot Fl(y)) &= [x(1-\delta_x) \cdot y(1-\delta_y)](1-\delta_{temp}) \\
  &= x \cdot y (1-\delta_x)(1-\delta_y)(1-\delta_{temp}) \\
  &= x \cdot y (1-\delta_x - \delta_y + \delta_x \delta_y)(1-\delta_{temp}) \\
  &= x \cdot y (1-\delta_x - \delta_y + \delta_x \delta_y - \delta_{temp} + \delta_x \delta_{temp} + \delta_y \delta_{temp} - \delta_x\delta_y\delta_{temp}) \\
  &\approx x \cdot y(1 - \delta_x - \delta_y - \delta_{temp}) \text{ since each } \delta < eps\text{, meaning } |\delta^3| << \delta^2 << \delta \\
  &= x \cdot y(1-\delta) \text{ where } |\delta| \le 3eps
\end{align*}
$$
	- Thus final error is pretty small
- $x / y$ <mark style="background: #FFB86CA6;">In A1 or Term test</mark>
	- Similar to multiplication
- $x + y$
$$
\begin{align*}
  Fl(Fl(x) + Fl(y)) &= [x(1-\delta_x) + y(1-\delta_y)](1-\delta_{temp}) \\
  &\approx x(1-\delta_x-\delta_{temp}) + y(1-\delta_y-\delta_{temp}) \text{ same reason as above} \\
  &= (x + y)\Big[1 - \frac{x}{x+y}(\delta_x+\delta_{temp}) - \frac{y}{x+y}(\delta_y+\delta_{temp})\Big] \\
  &= (x + y) [1- \delta] \text{ where } |\delta| \le |\frac{x}{x+y}|2eps + |\frac{y}{x+y}|2eps = \frac{|x|+|y|}{|x+y|}2eps
\end{align*}
$$
$$
\begin{equation}
	|\delta| \le
	\begin{cases}
		2eps & xy > 0, \text{ie. if x, y same signs} \\
		2eps \frac{x-y}{x+y} & xy < 0,  \text{ie. if x, y opposite signs}
	\end{cases}
\end{equation}
$$
		When $x \approx -y$, the error bound for addition could get very large, very fast.
		This is **Subtractive Cancellation**

Example:
- Subtractive Cancellation
	- In $\mathbb{R}_{10}(3, 1)$  with rounding
		- Compute $a^2-2ab + b^2$, with $a = 15.6$, $b = 15.7$
			- $(a-b)^2 \ge 0$
		- $Fl(a) = 0.156 \cdot 10^2, Fl(b) = 0.157 \cdot 10^3$
		- No initial Round off
		- $Fl(a^2) = Fl(243.36) = 0.243 \cdot 10^3$
		- $Fl(2ab) = Fl(489.84) = 0.490 \cdot 10^3$
		- $Fl(b^2) = Fl(246.49) = 0.246 \cdot 10^3$
		- $Fl(Fl(a^2) - Fl(2ab) + Fl(b^2)) = Fl(243 - 490 + 246) = Fl(-1) = -0.100 \cdot 10^1$
		- Round off occurred after calculation and remapping
		- We now have incorrect sign