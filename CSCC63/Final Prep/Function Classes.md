- Functional analogues to language classes $P, NP, PS$
- $FP$ functions that can be computed in polytime
- $FP$ contains all polytime reductions and questions on finding solution to $P$  problems
- $FNP$ are questions "given an input, fond one of its certificates if it exists"
- $FP \subseteq FNP$ and $P = NP$ iff $FP = FNP$

- Self-reducible: If language is NP-complete we can always use a solver (oracle) for the language to solve functional analogue
	- If $L$ is NP-complete, there is polytime reduction $L \leqslant_p 3SAT$
	- Also has verifier $V$
	- Make NTM
	  ![[Pasted image 20240814153112.png]]
	- Use logic in Cook-Levin Reduction, finding certificate for $L$ is finding a certificate for $\phi$ which can be done with 3SAT oracle
	- If only $L$ oracle, since it NP-complete, there is polytime reduction to 3SAT so we can use this reduction and $L$ oracle to effectively have a 3SAT oracle
	- **Overall** to find certificate for $L$
		- Run above NTM through Cook-Levin reduction to get $\phi$
		- Run FIND-SATISFYING-ASSIGNMENT solver (shown in class) on $\phi$, using 3SAT to $L$ reduction and $L$ oracle to simulate 3SAT oracle
		- Use direct correspondence to translate back to $L$

- FNP stronger than NP as we can identify both yes and no instances, so it also solves co-NP-complete version of problems alongside NP-complete version (ie. can return null)