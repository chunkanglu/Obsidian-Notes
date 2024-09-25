- How many certificates does an instance of a language in NP have?
- $\#P$ is hard for NP, if we can count satisfiable we know if satisfiable
- If instance is unsatisfiable, also hard for co-NP
- $\#P$ is hard for FNP, since hard for NP
- $PS$ is hard for $\#P$, can solve problems in $\#P$ by looping over all possible certificates & counting number that accept

- $\#P$-complete if function $f \in \#P$ and any polytime solution to $f$ yields polytime solution for all problems in $\#P $
- Use parsimonious reduction to solve nay problem in $\#P$
	- Parsimonious reduction preserves number of certificates to problem
	- If not 1 to 1, but 1 to k, it is k-parsimonious

- $\#3SAT, \#CLIQUE, \#CYCLE$ are $\#P$-complete
- Parsimonious reduction from $\#3SAT$ use 1 thing for each truth assignment of a clause

- Toda's Theorem, access to $\#3SAT$ solver allows efficiently solve problems far beyond NP
- Probibilistic Polynomial Time PP iff language has polytime certificate/verifier pair such that more than half of certificates are accepted
$$
P \subseteq NP \subseteq PP \subseteq PS
$$
