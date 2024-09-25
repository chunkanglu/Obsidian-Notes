How difficult programs are to solve

- Usually we aren't interested in a single program/implementation but rather whether a problem itself has a lower bound for how efficient an algo to solve this may be
$$
TIME(t(n)) = \left\{ L | L \text{is a language decided by some TM with worst-case time } O(t(n)) \right\}
$$
- Set of all languages that can be solved worst case $O(t(n))$
- The formalism / type of TM matters, but only up to a constant power
	- eg. if multi-tape has worst-case $O(t(n))$, we can simulate with single-tape with worst-case $O(t^2(n))$

# Input Sizes
- Time complexity of algorithms are usually based on the whole input size $|I|$
- For most cases like input arrays this won't change whether the resulting algorithm is in $P$ or not
- However, problem when input is a number
	- We think of numbers as encoded bit (or some other base) strings which then act similar to an array
	- Adding a new digit grows it by a whole factor, if binary, it doubles the number
	- Thus things grow *exponentially*
	- See Pseudo-polynomial
# Class P
$$
P = \bigcup_{k \in \mathbb{N}} TIME(n^k)
$$
- Set of languages that can be decided in polytime on a *deterministic* single tape TM
- P is like decidability in Computability
- These are problems that a **easy to solve**, in comparison to $NP$ problems below
# Class NP
$$
NTIME(t(n)) = \left\{ L | L \text{is a language decided by some nondeterministic TM with worst-case time } O(t(n)) \right\}
$$
- Runtime $t(n)$ of a non-deter TM is the maximum number of steps taken on *any* branch of the computation tree for any input of size $n$
$$
NP = \bigcup_{k \in \mathbb{N}} NTIME(n^k)
$$
**Alternative Description:**
$L \in NP$ if there is a *deterministic polytime* verifier TM V st. $x \in L$ iff $\exists C_x$ a certificate polynomial to the length of $x$ where $V(x, C_x)$ accepts.
**To show a language $L$ is in $NP$**
1. Show $L$ is a decision yes/no problem
2. Give certificate
3. Show certificate is polynomial to size of input
4. Give verifier
5. Show verifier is polynomial to size of input

- NP is like recognizability in Computability
- They are problems that are **easy to check**, but hard to solve
# P and NP
- Big open question of relationship between $P$ and $NP$
- $P \subseteq NP$ since every deter TM is a non-deter TM
- Every non-deter TM can be simulated by a deter TM with exponential slowdown
- Conjecture that $P \ne NP$
- 