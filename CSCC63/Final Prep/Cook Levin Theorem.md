SHows that 3SAT is NP-Complete

$$
A_{B-NTM} = \left\{ \langle M, w, \#^r \rangle \Bigg|
\begin{align*}
& M \text{ is a verifier that accepts some certificate } c \\
& \text{ of length at most } |w|^k \text{ for } w \text{ within } r \text{steps}
\end{align*}
 \right\}
$$

This is NP-hard and the argument works for any language in NP.
> To see why this has to be N P-hard, consider the example:  
• HAM-PATH ∈ N P, so we can build an verifier M that decides whether a path P  
for 〈G, s, t〉 is a certificate for HAM-PATH using O(nk′  
) steps for some k′ ∈ N.  
• We can set w = 〈G, s, t〉 and r to be the worst-case time M can take for an input of  
size |w| (00for any certificate).  
• If we do so, then 〈M, w, #r〉 ∈ AB-NTM iff 〈G, s, t〉 ∈ HAM-PATH.

Then just need $A_{B-NTM} \leqslant_p 3SAT$ by building a boolean formula $\phi$ that encodes the operation of a TM.

We consider a (deteministic but actually non-deterministic holds with some modifications) $M$ that halts in polynomial time (**dunno where this is from**) so there is some $k$ such that $M$ cannot take more than $n^k$ steps ($r = n^k$)
Also $M$ cannot move its head more than $n^k$ spaces as a result.
Create $n^k \times (n^k + 2)$ table to encode all operations of $M$ on $w$, each row being a configuration.
![[Pasted image 20240812191017.png]]

Need to build a $\phi$ that encodes this $M$ by satisfying 4 properties:
1. Every cell contains exactly 1 character
2. Characters on the first row match $C_0$ ($q_0$ and input)
3. There is a $q_{accept}$ character somewhere on the table
4. Every row in the table follows from the one above given the operation of $M$

Each is encoded by an individual $\phi_{condition}$ and joined with ANDs.

Entire reduction is $O(n^{2k})$ so it is polynomial time
