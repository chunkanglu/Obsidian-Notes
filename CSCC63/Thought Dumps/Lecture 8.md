- Quantifiers in the order of there exists, then for all likely is not recognizable

# Rice's theorem
Suppose that $P$ is a language of TM descriptions such that:
- $P$ is neither empty nor the set of all TM descriptions
- If $M_1$ and $M_2$ are TMs such that $L(M_1) = L(M_2)$, then $\langle M_1 \rangle \in P \iff \langle M_2 \rangle \in P$
Then $P$ is undecidable.

Any TM of this sort is not decidable:
$\{ \langle M \rangle | L(M) = \Sigma^* \}$
$\{ \langle M \rangle | M \text{ accepts "1"} \}$
$\{ \langle M \rangle | L(M) = \emptyset \}$
But theorem does not say anything about languages like below that have some info about how the TM is run:
$\{ \langle M \rangle | M \text{ accpets "1" within 500 steps}  \}$

# Oracles
- What is we could solve HALT? And how would things change
- Oracle is essentially a black box that we can feed it instances of a language (eg. an oracle for HALT) and instantly get a yes-no answer
	- Something "plugged-into" a TM to give it more power
	- This is only for theory

- Can make some languages decidable, but not all
- An oracle machine can't solve its own halting problem (ie. you can't use it on another checking halt TM)

# Arithmetical Hierarchy
*Separate undecidable languages into levels*

$\Sigma_1$: Recognizable languages
$\Pi_1$: Co-recognizable languages
$\Delta_1$: Decidable
$\Delta_2$: Decidable with HALT oracle
$\Sigma_2$: Recognizable languages (given HALT oracle)
$\Pi_2$: Co-recognizable languages (given HALT oracle)
$\Delta_3$: Decidable with HALT$^{\text{HALT}}$ oracle
... and so on...

The number tells us how many quantifiers
- $\Sigma$s have form $\exists \forall \exists \ldots$
- $\Pi$s have form $\forall \exists \forall \ldots$
But not all languages can be expressed with the quantifier way
