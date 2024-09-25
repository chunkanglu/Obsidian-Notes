- how much memory needed to solve a problems (ie. number of tape cells used in TM)
- Conjecture, worst case time complexity not linked to space complexity (can differ greatly)
- Space needed for problem $\le$ time required
	- If TM takes at most $k$ steps, it uses at most $k$ cells
	- But a cell can be looked at more than once 

- Set $SPACE(f(n))$ are languages decided by $O(f(n))$ space TM
- Set $NSPACE(f(n))
- Class $PSPACE$ all languages solved in polyspace
- Class $NPSPACE$ all languages verified in polyspace

- Any TM that looks at whole input uses at least $O(n)$ space

- $NP \subseteq PS$
	- Can simulate an NTM by looping through all possible certificates and using a deterministic TM to verify
	- Certificates are polynomial in size
- $PS = NPS$
	- Satvich's Theorem: for any $f: N \rightarrow R^+. NSPACE(f(n)) \subseteq SPACE([f(n)]^2$
	- Proof for theorem shows time needed for search is still exponential, so no relation to P or NP

- PS-complete if language in PS and every language in PS **polytime reduces** to the language
	- if reductions were allowed to use polyspace instead of time, we could solve any problem in PS as part of the reduction, so all non--trivial languages in P are PS-complete
- True Quantified Boolean Formulas (TQBF) is PS-complete
- PS-complete problems look like adversarial 2-player games

- Logarithmic Space considers TMs with read-only input tape, log sized working tape, and write only output tape
- L is language decided by TM in $O(log n)$ space
- NL is L but with NTM
- Restriction when working with a machine that has limited memory but access to large DB


$$
L \subseteq NL \subseteq P \subseteq NP \subseteq PS = NPS \subseteq EXP
$$
- $P \ne PS$
- $P \ne EXP$
- $L \ne PS$
- $NL = co-NL$