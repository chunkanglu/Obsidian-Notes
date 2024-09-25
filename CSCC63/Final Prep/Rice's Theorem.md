**Just about any statement about a TM's language is undecidable**

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