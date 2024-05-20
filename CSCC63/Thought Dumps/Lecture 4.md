# Decidable Languages
- If a language can be solved by a TM, it is *decidable*, otherwise *undecidable*
- Good to describe languages using set notation instead: $\{ \text{instance} | \text{some decidable statement} \}$
- Two useful languages that are decidable
$$
ACC: \left\{ \langle M, w, k \rangle | \text{M accepts w in at most k steps} \right\}
$$
$$
H: \left\{ \langle M, w, k \rangle | \text{M halts on w  in at most k steps} \right\}
$$
- Two undecidable languages
$$
A_{TM}: \left\{ \langle M, w \rangle | \text{M accepts w} \right\}
$$
$$
HALT: \left\{ \langle M, w \rangle | \text{M halts on w} \right\}
$$
- Cannot use Universal TM and Run M on w since it may loop forever
	- Since no time limit, we effectively need to try for $k = 1, 2, \ldots$ to infinity

- There isn't a way to look at a code and figure out what it would do and if it would work

- Using *Liar's Paradox* to assume a language is decidable and encode the paradox in logic to get a contradiction and show that it is undecidable
	- Key point is the **self-reference**
- Proof by contradiction
	- Assume $A_{TM}$ is decidable. Thus by Church-Turing Thesis, there exists algorithm $M_A$ that (takes in TM $M$ and string $w$) solves it.
	- Use program to encode Liar's paradox
		- program $D$ (diagonalization) will take input $w$, figure out what some TM would do on $w$, and do the opposite
		- We will ultimately feed $D$ into itself
		```
		D = "On input <M>"
			1. Does M accept <M>? Run MA on <M, M>
			2. If yes, reject
			3. Else, accept
		```
		-  We are able to feed $M$ as $w$ since the TM representation of $M$ is ultimately a string 
		- Run $D$ on $\langle D \rangle$
			- If it accepts, then $M_A$ rejects $\langle D, D \rangle>$ so $D$ rejects in line 2 (**NOT POSSIBLE since we just saw it accepts**)
			- Else, $M_A$ rejects $\langle D, D \rangle$, so $D$ accepts on line 3 (**AGAIN INCONSISTENT ANSWER**)
		- If $M_A$ was actually decidable, then this inconsistency would not occur
	- Check our encoding is not consistent and get a contradiction
	- Use contradiction to argue that original assumption was wrong
- $D$ fails to work because there's an endless loop of $D$ trying to reference itself 1 level deeper each time

- If we allow looping programs, we can solve $A_{TM}$
```
MA = "On input <M, w>":
	1. Run M on w
	2. If accepts, accept
	3. Reject
```
- This accepts all yes-instances, and never accepts any no-instances (but can loop on no-instances)
	- This is a *recognizable* language, where $M_A$ is a *recognizer*
	- **TODO: fill in missing notes here**

- Decidable iff recorgnizable and co-recognizable
$$
\begin{align}
&L \text{ is recognizable means } \exists M_1, \forall x \in \Sigma^* \\
&~~x \in L \implies M_1 \text{ accepts } \land \\
&~~x \notin L \implies M_1 \text{ rejects }
\end{align}
$$
- Similar for co-recognizable
- $L$ co-recognizable $\iff \overline{L}$ recognizable

# Dovetailing
Suppose some TM $M_1$ recognizes $L$ and another TM $M_2$ recognizes $\overline{L}$. Then following TM decides $L$:
```
M = "On input w":
	1. For k = 0, 1, 2, ...:
		1. Run M_1 on w for k steps
		2. If accepts, accept
		3. Run M_2 on w for k steps
		4. If accepts, reject
```