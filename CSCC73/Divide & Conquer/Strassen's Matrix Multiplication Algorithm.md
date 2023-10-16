Similar idea to Karatsuba's Algorithm but applied to matrices.
It splits each matrix $A, B$ into 4 quadrants and then does a lot of weird merging to create 7 terms which results in the 4 quadrants of the output matrix.

$$
T(n) = 7T(\frac{n}{2}) + cn = \Theta(n^{log_{2}{7}}) \approx \Theta(n^{2.81})
$$
This is better than the $n^3$ standard way.