- Run M on w acts as a filter
- If we want something to happen if M does not halt on w
	- then we are effectively doing
		- $\langle M, w, 1 \rangle \notin$ HALT
		- $\langle M, w, 2 \rangle \notin$ HALT
		- $\langle M, w, 3 \rangle \notin$ HALT
		- ...
	- Run M on w for k steps (where k is input to $M_0$), if it halts then loop, otherwise accept
	- Since k is arbitrary, if something doesn't halt on k, then M does not halt on w generally


- If you reduce from some language that is both not recognizable nor co-recognizable to the target language, then we also know **both** for the target in just 1 reduction

- $EQ_{TM}$ is 

$DEC = \{ \langle M \rangle | L(M) \text{ id decidable } \} = \{ \langle M \rangle | \exists \langle N \rangle, N \text{ halts on all inputs and } L(M) = L(N) \}$
