---
tags:
  - CSCC43
---
- Express constraints on data
- Decompose relations
- Normalization
# Normalized Schema
- Minimal redundancy
- Splitting into smaller relations
# Functional Dependency
$A \rightarrow B$ ($A$ implies $B$) means for every value of $A$ your are able to uniquely identify $B$
- Also referred as: $B$ is **functionally dependent** on $A$
- Can be not only one column on each side: $A \rightarrow BC$
- Conditions:
	- Left side does not have duplicates/ is distinct/ is unique
## Types of Functional Dependencies
### Trivial FD
$x \rightarrow y$ is a trivial functional dependency $\iff y \subseteq x$ where $x, y$ are sets of attributes
**Example:**
$x = \left\{A, B \right\}, y = \left\{ A \right\}$
$A \rightarrow A$
### Non-Trivial FD
$x \rightarrow y$ is a non-trivial functional dependency $\iff x \cap y = \emptyset$ where $x, y$ are sets of attributes
**Examples:**
$A \rightarrow B$
$AB \rightarrow C$
### Semi-Trivial FD
$x \rightarrow y$ is a semi-trivial functional dependency $\iff x \cap y \ne \emptyset$ but *not* $y \subseteq x$
**Examples:**
$BC \rightarrow BCD$

### Properties
If $A \rightarrow BC$, then $A \rightarrow B$ and $A \rightarrow C$
If $A \to B$ and $A \to C$, then $A \to BC$
$$
A \to BC \equiv A \to B \text{ and } A \to C
$$
#### Armstrong's Axioms
- **Reflexivity**: If $Y \subseteq X$, then $X \to Y$
- **Augmentation**: If _X_ → _Y_, then _XZ_ → _YZ_
- **Transitivity**: If _X_ → _Y_ and _Y_ → _Z_, then _X_ → _Z_

#### Closure set of an attribute
Set of attributes which can be uniquely identified by A, denoted by $A^+$
> Used for finding candidate keys of a relation without looking at the values of each attribute

**Given:**
$A \to B$
$B \to D$
$C \to DE$
$CD \to AB$
**Closures:**
$A^+ = \{ A, B, D \}$ using $A \to B$ and $B \to D$
$B^+ = \{ B, D \}$ using $B \to D$
$C^+ = \{ C, D, E, A, B  \}$ using $C \to DE$ and $CD \to AB$
$D^+ = \{ D \}$
$E^+ = \{ E \}$

**Given:**
$AB \to CD$
$AF \to D$
$DE \to F$
$C \to G$
$F \to E$
$G \to A$
**Closures:**
$(CF)^+ = \{ C, F, G, A, D, E \}$
$BG^+ = \{ B, G, A, C, D \}$
$AF^+ = \{ A, F, D, E \}$
### Decomposition
$F^+$ is set of all functional dependencies which hold on $F$
$F = \{ A \to B, B \to C \}$
$A \to C$
$A \to A$
$B \to B$
$AB \to A$
$F^+ = \{ A^+ = \ldots, B^+ = \ldots, C^+ = \ldots, AB^+ = \ldots, AC^+ = \ldots, BC^+ = \ldots, ABC^+ = \ldots \}$
## Schema Decomposition
- Decomposing and combining it back should result in the original (Lossless decomposition)
- Lossy Decomposition
	- Does it result in the same information as before
	- Can cause spurious tuples
		- creates data that was not originally there
### Principles for Lossless decomposition
- Both tables should have a common attribute
- Common attributes should be candidate key of at least one relation
**Example:** $ABC$ split into $AB, AC$ should be valid if $A$ is a candidate key of either $AB$, $AC$, or both

### Good Decomposition Principles
- Lossless
- Attribute preserving
	- Decomposition must include all attributes
- Functional Dependency Preservation
	- $F \subseteq (F_1 \cup F_2)^+$ where $F$ is original functional dependency and $F_1, F_2$ are the new ones after decomposing
### Example Question
$R(ABC)$
$FD = \{ A \to B, B \to C, C \to A \}$
Let $R_1(AB)$ and $R_2(BC)$ be decomposition of $R(ABC)$, check whether it is a lossless decomposition or not.
**Solution:**
Find closure of $B$ to determine if it is a candidate key.
$B^+ = \{ B, C, A \}$
It is a candidate key for both, so this is a lossless decomposition.
# Minimal Basis/Cover of a Functional Dependency set
- Functional dependency that can't be further broken down
- Denoted as $F'$
### Example 1
Given relation $R(A, B, C, D)$
$$
F = \{A \to AC, B \to ABC, D \to ABC\}
$$
Step 1: Split everything
$$
\begin{align}
A \to A \\
A \to C \\
B \to A \\
B \to B \\
B \to C \\
D \to A \\
D \to B \\
D \to C
\end{align}
$$
Step 2: Remove redundancies, check each dependency and see if it is needed (ie. can we get the same dependency using other info, is it already in the closure set without using it)
$$
\begin{align}
A \to C \\
B \to A \\
D \to B \\
\end{align}
$$
### Example 2
Given $\{ A \to B, C \to B, D \to ABC, AC \to D \}$
$$
\begin{align}
A \to B \\
C \to B \\
D \to A \\
D \to B \\
D \to C \\
AC \to D
\end{align}
$$
Remove redundancies:
$$
\begin{align}
A \to B \\
C \to B \\
D \to A \\
D \to C \\
AC \to D
\end{align}
$$
Try to reduce all LHS to singleton value.
Here we cannot do anything since $A \notin C^+$ and $C \notin A^+$.