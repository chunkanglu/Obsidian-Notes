# 1
Force same starting and ending tile? 
Similar to previous one?

$\frac{\$_{s=a}}{\$}$
$\frac{\$_{s=b}}{\$}$
$\frac{\$_{s=b}}{\$}$
multiple starting tiles

# 2
- Lexicographically
- a, b, c, aa, ab, ac, ba, bb, bc, ca, cb, cc, aaa, ...
- 10th string is ca (if we don't count empty string, otherwise it's bc)
- 3 strings for single character, 9 for 2-char, 27 for 3-char, 81 for 4-char, 243 for 5-char, then we need to see how many from aaa to bbc
	- aaa to baa is 9
	- baa to bba is 3
	- bba to bbc is 2
- Would take 377 iterations to get to aaabbc
# 3
$$
L = \left\{ \langle M, w \rangle |~ \text{Running } w \text{ on } M \text{ tries to move head off of the left side of tape} \right\}
$$
# 4
