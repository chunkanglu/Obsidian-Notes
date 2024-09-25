Conjectures:
- $P \ne NP \cap co-NP$
- $NP \ne co-NP$
- $P \ne NP$

- Conjecture: worst-case run time $O(n^2 2^n)$
- Complexity is how efficiently we can decide a decidable language
- Class $TIME(t(n))$ is set of languages with worst case $O(t(n))$ time by deterministic TM
- Time complexity between different TM formalisms (multi) can only (from simulated) have a blowup of a constant power
- $P$ is set of languages decided in polytime by deterministic TM
- Integer inputs have exponential growth when adding another digit
- Runtime of non-deterministic TM is max steps taken on any branch 
- Class $NTIME(t(n))$ is set of languages with worst case $O(t(n))$ time by non-deterministic TM
- $NP$ is set of languages deceded in polytime by non-deterministic TM
- $NP$ also set of languages that can be verified (given a certificate) in polytime by a deterministic TM

Show in $NP$:
1. Is language a decision problem
2. Give a certificate
3. Show certificate is polynomial in size to input
4. Give a verifier
5. Show verifier is polytime with respect to input

- co-$NP$ is complement of $NP$, same operations on complement of language

- $A$ polytime reducible to $B$ iff exists polytime function that converts instance of $A$ to instance of $B$

- Language is **hard** for a class, if every language in class reduces to it
- Language is **complete** for a class, if it is hard and the language is in the class too
- 3SAT is NP-complete by Cook-Levin Theorem
- If any NP-complete language is in $P$, then $P = NP$

- Show language is in $P$ by giving a polytime algo that solves it

- NP-intermediate are problems in $NP$ that are neither $NP$-complete, nor in $P$
- Integer factorization in NP-intermediate