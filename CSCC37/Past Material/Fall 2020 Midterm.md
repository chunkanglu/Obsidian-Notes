![[cscC37-F20-termtest.pdf]]
1. floating point representation
2. floating point representation
3. subtractive cancellation & function condition number
4. LU factorization
5. Condition of linear system
6. condition of matrix
7. iterative refinement

# Q1
> Design a computer that is able to store $(0.1)_{10}$ exactly. A floating point number on your computer must be represented internally in a base less than 10, and must have a mantissa with a finite number of digits. (Hint: Is this possible?)

After trying base 2, 3, 5, 7 and seeing that that all cycle, we also know that 4, 6, 8, 9 will cycle as they are multiples of the previous set. As none of the bases less than 10 work, this is not possible.
# Q2
> What numbers are representable with a finite expression in the binary system but are not finitely representable in the decimal system? Justify your answer.

None, as you can always convert a finite number in binary to a finite number in decimal since 10 is a multiple of 2.
# Q3
> We wish to evaluate f (x) = β − √β2 − x2 where β  0 and |x| < β. a. Identify the range of x where f (x) suffers from potential subtractive cancellation. An approximate range will suffice
> Evaluate limx→α cond(f (x)), where α is the smallest number, in absolute value, within the range you identified in (a). Does the condition number reflect the potential for subtractive cancellation? Explain.
> Derive an alternate form of f (x), stable for evaluation in the range you identified in (a).

# Q4
> ![[Pasted image 20231104114342.png]]
> Use the factorization computed in (a) to solve the system.
> Why is Gaussian Elimination usually implemented as in this question (i.e., P A = LU is computed separately, and then the factorization is used to solve Ax = b)?
## 4a
$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
A =
\begin{bmatrix}
2 & 6 & 6 \\
3 & 5 & 12 \\
6 & 6 & 12
\end{bmatrix}
, ~
$$
$$
P_1 =
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{bmatrix}
, ~
P_1 A =
\begin{bmatrix}
6 & 6 & 12 \\
3 & 5 & 12 \\
2 & 6 & 6
\end{bmatrix}
, ~
L_1 =
\begin{bmatrix}
1 & 0 & 0 \\
-\frac{1}{2} & 1 & 0 \\
-\frac{1}{3} & 0 & 1
\end{bmatrix}
,~
L_1 P_1 A =
\begin{bmatrix}
6 & 6 & 12 \\
0 & 2 & 6 \\
0 & 4 & 2
\end{bmatrix}
$$
$$
P_2 =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix}
, ~
P_2 L_2 P_1 A =
\begin{bmatrix}
6 & 6 & 12 \\
0 & 4 & 2 \\
0 & 2 & 6
\end{bmatrix}
, ~
L_2 =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -\frac{1}{2} & 1
\end{bmatrix}
,~
L_2 P_2 L_1 P_1 A =
\begin{bmatrix}
6 & 6 & 12 \\
0 & 4 & 2 \\
0 & 0 & 5
\end{bmatrix}
$$
$$
U =
\begin{bmatrix}
6 & 6 & 12 \\
0 & 4 & 4 \\
0 & 0 & 5
\end{bmatrix}
$$
$$
\begin{align}
L_2 \tilde{L}_1 P_2 P_1 A = U \\

\end{align}
$$
$$
P =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{bmatrix}
=
\begin{bmatrix}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
$$
$$
\tilde{L}_1 = P_2 L_1 P_2 =
\begin{bmatrix}
1 & 0 & 0 \\
-\frac{1}{3} & 1 & 0 \\
-\frac{1}{2} & 0 & 1
\end{bmatrix}
,~
L = L_2^{-1} \tilde{L}_1^{-1} =
\begin{bmatrix}
1 & 0 & 0 \\
\frac{1}{3} & 1 & 0 \\
\frac{1}{2} & \frac{1}{2} & 1
\end{bmatrix}
$$
## 4b
$PA = LU \implies LUx = Pb$
$Ld = Pb$
$$
\begin{bmatrix}
1 & 0 & 0 \\
\frac{1}{3} & 1 & 0 \\
\frac{1}{2} & \frac{1}{2} & 1
\end{bmatrix}
\begin{bmatrix}
d_1 \\
d_2 \\
d_3
\end{bmatrix}
=
\begin{bmatrix}
30 \\
20 \\
25
\end{bmatrix}
$$
$$
\begin{align}
d_1 = 30 \\
d_2 = 20 - \frac{1}{3} \times 30 = 10 \\
d_3 = 25 - 15 - 5 = 5
\end{align}
$$
$Ux = d$
$$
\begin{bmatrix}
6 & 6 & 12 \\
0 & 4 & 4 \\
0 & 0 & 5
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
=
\begin{bmatrix}
30 \\
10 \\
5
\end{bmatrix}
$$
$$
\begin{align}
x_3 &= 1 \\
4x_2 = 6 \implies x_2 &= \frac{3}{2} \\
6x_1 + 9 + 12 = 30 \implies 6x_1 = 9 \implies x_1 &= \frac{3}{2}
\end{align}
$$
## 4c
If we have to solve similar equations using the same $A$ matrix but different $b$ it is much more efficient to calculate using forward and back substitution with the $LU$ factorization than doing individual solves each time.
# Q5
## 5a
Poorly conditioned, lines are nearly parallel
Perfectly conditioned, lines are orthogonal
## 5b
IDK
## 5c
3 planes all orthogonal to each other
# Q6
## 6a
$$
A =
\begin{bmatrix}
2 & 4 \\
1 & 2+\epsilon
\end{bmatrix}
, ~
A^{-1} = 
\frac{1}{det(A)}
\begin{bmatrix}
2+\epsilon & -4 \\
-1 & 2
\end{bmatrix}
= \begin{bmatrix}
\frac{2+\epsilon}{2\epsilon} & -\frac{2}{\epsilon} \\
-\frac{1}{2\epsilon} & \frac{1}{\epsilon}
\end{bmatrix}
$$
$$
\begin{align}
||A||_1 &= 6 + \epsilon \\
||A^{-1}||_1 &= \max \left( \frac{3+\epsilon}{2\epsilon}, \frac{3}{\epsilon} \right) = \frac{3}{\epsilon} \\
||A||_1 ||A^{-1}||_1 &= \frac{18 + 3\epsilon}{\epsilon} \\
\lim_{\epsilon \rightarrow 0} ||A||_1 ||A^{-1}||_1 &= \infty
\end{align}
$$
## 6b
similar to 5a?
$$
\begin{cases}
y = \frac{1}{2} x - \frac{1}{4}b_1 \\
y = \frac{1}{2+\epsilon} x + \frac{1}{2 + \epsilon} b_2
\end{cases}
$$
As $\epsilon \rightarrow 0$ lines get more parallel and are subject perturbations.
When $\epsilon = 0$ then they are exactly parallel, which explains the infinity condition number of $A$.
# Q7
$$
\begin{cases}
Az_i = r_i \\
(A+E)\hat{z}_i = r_i
\end{cases}
$$
$$
\begin{align}
||\hat{x}_{i+1} - x|| = ||\hat{x}_i + \hat{z}_i - x|| &\le ||\hat{x}_i - x|| + ||\hat{z}_i|| \\
&= ||\hat{x}_i - x|| + ||(A+E)^{-1}r_i|| \\

&= ||\hat{x}_i - x|| + ||A^{-1}r_i||  \\
&\le ||\hat{x}_i - x|| + ||A^{-1}||~||r_i|| \\
&= ||\hat{x}_i - x|| + ||A^{-1}||~||Az_i|| \\
&= ||\hat{x}_i - x|| + ||A^{-1}||~||A||~||x
\end{align}
$$

$$
||\hat{x}_{i+1} - x|| \le 
$$