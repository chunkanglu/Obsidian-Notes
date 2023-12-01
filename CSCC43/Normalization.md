- Goal of database design is to have no redundancy
- Needs assumptions on dependencies we need to maintain
# First Normal Form
- If a table is flat (no composite and multi-valued attribute) then it is $1^{st}$ NF.
#### Is 1NF
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 | 
| 7 | 8 | 9 | 
#### Not 1NF
| A | B | C |
|---|---|---|
| 1 | 2 | 3, 4 |
# Second Normal Form
- Is 1NF
- There is no partial dependency of non-prime attribute to any key of $R$
	- **Informally**: Part of any key should not derive any non-prime attribute
		- Note if only **one** key then it is 2NF (since it cannot be split into part of the key)
	- **Prime attribute -** attribute which is part of any key of $R$
- Example
	- If $AB$ is key, $\{ AB \to C \}$, then $A, B$ are prime attributes
	- $C$ is a **non-prime attribute**
	- This is in 2NF if $A \to C$ and $B \to C$ are not present
#### Example 1
**Given:**
$R(M, N, O)$
$F = \{ MN \to O, M \to O \}$
**Is this 2NF?**

First find key of relation from functional dependencies.
- Key is $MN$ since $(MN)^+ = \{ M, N, O \}$ which is all attributes.
- Note: RHS will not be a key (unless circular)
This is 1NF, assuming none are multi-value.
Find prime attributes: $M, N$ since $MN$ is key
Find non-prime attributes: $O$
For 2NF, $M \to O$ and $N \to O$ should not exist, but it does, so it is not 2NF (and decomposition can happen)

To decompose
- Get LHS of the functional dependency that should not exist
	- $M^+ = \{ M, O \}$
- Split $R(MNO)$ into $R_1(MN)$ and $R_2(MO)$ [[Database Design Theory#Schema Decomposition]]
#### Example 2
Given:
$R(MNOPQ)$
$F = \{ M \to N, N \to Q, O \to P \}$
Assume 1NF.

Key is $MO$ since $N, Q, P$ in RHS which can't be key and $(MO)^+ = \{ M, O, N, Q, P \}$
Prime attributes: $M, O$
Non-prime attributes: $N, Q, P$
What should not exist for 2NF: $M \to N$, $M \to Q$, $M \to P$, $O \to N$, $O \to Q$, $O \to P$
$M \to N$ and $O \to P$ exist.

Decompose to remove $M \to N$:
- $M^+ = \{ M, N, Q \}$
- $R_1(MNQ)$
	- This is 2NF since $M$ is single key in this relation
- $R_2(MOP)$
	- Not 2NF since $MO$ key
	- $O^+ = \{ O, P \}$
	- $R_3(OP)$
	- $R_4(MO)$
	- All attributes are preserved
	- Common attribute $O$ is a candidate key of $R_3(OP)$
	- Functional dependency $O \to P$ still holds
# Third Normal Form
- Is 2NF
- There should not be the case that a non-prime attribute is determined by another non-prime attribute
	- **Informally:** If any FD, either LHS should be a superkey or RHS should be a prime attribute
#### Example 1
$R(MNO)$
$F = \{ M \to N, N \to O \}$
Assume 1NF

Key is $M$
This is automatically 2NF since single key.
For 3NF
- $M \to N$, $M$ is a key thus superkey so this holds
- $N \to O$, this does not hold
- Decompose into
	- $R_1(NO)$
	- $R_2(MN)$
	- This is not in 3NF
#### Example 2
$R(MNOPQ)$
$F = \{ MN \to O, N \to P, P \to Q \}$
Assume 1NF

Key $MN$
prime attributes: $M, N$
non-prime: $O, P, Q$
Should not exist for 2NF: $M \to O, M \to P, M \to Q, N \to O, N \to P, N \to Q$
- Not 2NF since $N \to P$
- Decompose
	- $R_1(NPQ)$, $N \to P, P \to Q$
	- $R_2(MNO)$, $MN \to O$
	- This is now 2NF
For 3NF
- $P \to Q$, LHS is not a key
- Decompose $R_1$
	- $R_3(PQ)$
	- $R_4(NP)$
# Boyce Code Normal Form (BCNF)
- Ensures us to remove all redundancy from relation ocmpletely
- Is in 3NF
- Whenever a non-trivial FD, $X \to A$ holds in $R$, then $X$ should be a superkey of $R$
	- LHS is always a superkey
	- Single LHS is BCNF
#### Example 1
$R(MNO)$
$F = \{ M \to N, N \to O, O \to M \}$
Assume 1NF

Any of $M, N, O$ can be a key since circular
2NF holds since all are singular LHS
3NF holds since for all have key on LHS
BCNF since all are keys
#### Example 2
$R(MNOPQRSTUV)$
$$
F =
\begin{cases}
MN \to O \\
M \to PQ \\
N \to R \\
R \to ST \\
P \to UV
\end{cases}
$$
Assume 1NF

Key $MN$
prime: $M, N$
non-prime: $O, P, Q, R, S, T, U, V$

2NF fails since $M \to P, M \to Q, N \to R$ exist
- For $M \to P$
	- $R_1(MPQUV)$, $M \to Q$
		- Singular key, is 2NF
	- $R_2(MNORST)$, $N \to R$
		- Multiple keys and $N \to R$ exists, decompose more
		- $R_3(NRST)$
			- Singular key, is 2NF
		- $R_4(MNO)$
			- is 2NF

Now find 3NF for $R_1(MPQUV), R_3(NRST), R_4(MNO)$
This is also 3NF and BCNF
# Fourth Normal Form
A relation is in 4NF iff the following are satisfied:
1. $R$ is 3NF or BCNF
2. it contains no multi-valued dependencies
## Multi-valued dependency
Dependency where one attribute value is potentially a multi-valued fact about another
**Conditions:**
1. There must be $\ge 3$ attributes
2. Attributes must be independent of each other
$A \twoheadrightarrow B$
- one value of $A$ can have multiple values of $B$
### Properties of MVD
- Transitive
	- $x \twoheadrightarrow y$, $y \twoheadrightarrow z \implies x \twoheadrightarrow z$
- Complementation
	- if $x \twoheadrightarrow y$ and $z$ is the other attribute then $x \twoheadrightarrow z$
- Every Functional dependency is an MVD
	- if $x \to y$ then swapping y's between two tuples that agree on x doesn't change the tuple therefore new tuple are surely in the relation and we know $x \twoheadrightarrow y$
### Example
Consider the relation $R(ABCDE)$ with MVD $A \twoheadrightarrow B, B \twoheadrightarrow D$

It is in 3NF and BCNF since there are no FD.
By transitive property, $A \twoheadrightarrow D$.
Decompose:
- $R_1(AB)$
	- This will not have MVD since 2 attributes
- $R_2(ACDE)$
	- $R_3(AD)$
		- No more MVD, 2 attributes
	- $R_4(ACE)$
		- no MVD
# Chase Algorithm
- Test decomposition is lossless or lossy
## Example

Initial table
Relations: $R_1(ab), R_2(ac), R_3(bcd), R_4(ade)$
Given: $A \to C, B \to C, C \to D$

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|   | a | b | c | d | e |
|R_1| a | a |   |   |   |
|R_2| a |   | a |   |   |
|R_3|   | a | a | a |   |
|R_4| a |   |   | a | a |
After $a \to c$

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|   | a | b | c | d | e |
|R_1| a | a | a |   |   |
|R_2| a |   | a |   |   |
|R_3|   | a | a | a |   |
|R_4| a |   | a | a | a |

After $b \to c$

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|   | a | b | c | d | e |
|R_1| a | a | a |   |   |
|R_2| a | a | a |   |   |
|R_3|   | a | a | a |   |
|R_4| a | a | a | a | a |

## Example 2
$A \to B, B \to C, C \to D$
Evaluate decomposition $D = \{ ABC, CD \}$

|   | A | B | C | D |
|---|---|---|---|---|
|R_1| a | a | a | b |
|R_2|   |   | a | b |

Its lossless because we filled a row

## Example 3
$R(ABCD)$
$D = \{ AB, BC, CD \}$
$A \to B, B \to C, C \to D, D \to A$

|   | A | B | C | D |
|---|---|---|---|---|
|R_1| a | a |   |   |
|R_2|   | a | a |   |
|R_3|   |   | a | a |

|   | A | B | C | D |
|---|---|---|---|---|
|R_1| a | a | b | b |
|R_2| b | a | a | b |
|R_3| b | b | a | a |

This is lossless

## Example
$R(ABCDEF)$
$D = \{ ABCD, DEF \}$

Invent a set of FD that would make this a lossless join decomposition