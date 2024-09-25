- Two definitions of recognizatble languages equivalent
```
R = "On input <x>:
	For all certificate c:
		If P(x, c):
			Accept"
```
- But can we loop over, every certificate
	- Yes, with an effective enumeration
	- Every certificate must be a string
		- We try to loop for every possible string that could be a format of valid certificate
		- Done by every string length, then every possible character in the string
		- Remember to include the empty string $\epsilon$
- Direct correspondence between natural numbers (binary form) and the effective enumeration of $\{ 0, 1 \}^*$ strings
- Common ways to loop over strings
	- short lex order
- Usually just say the following as we know it is possible and we have seen it in class
	- Let $w_0, w_1, \ldots,$ be an effective enumeration of the strings
	- Let $\langle M_0 \rangle, \langle M_1 \rangle, \ldots$ be an effective enumeration of the TMs

- We can write every Turing Machine as a string (as seen previously as input the Universal TM), and we can also enumerate strings, asking each time "is this string in the format of a Turing Machine". Thus, we can enumerate over Turing Machines themselves.

- Language is recognizable iff we can write an **enumerator** for it
```
M = "Ignore input:
	For k = 0, 1, 2, ...:
		For i = 0, ..., k:
			For j = 0, ..., k:
				Run M_i on w_j for k steps.
				If it accepts, print <M_i, w_j> and continue to next i."
```
- Not we do not directly use infinity in the inner loops to avoid getting stuck on say $i = 0$ and $j$ going to infinity

Language is co-recognizable iff complement is recognizable
$$
\overline{L} = \{ \langle x \rangle |~ \forall c, Q(x, c) \} \text{ for decidable predicate } Q = \lnot P
$$
Decidable language is recognizable as every yes-instance is assessed correctly; it is also co-recognizable as every no-instance is assessed correctly.

Recognizable & Co-recognizable implies decidable by dovetailing:
Suppose $M_1$ recognizes $L$ and $M_2$ recognizes $\overline{L}$
```
M = "On input w:
	for k = 0, 1, 2, ,...
	Run M_1 on w for k steps
	If it accepts, accept
	Run M_2 on w for k steps
	If it accepts, reject"
```
___
# Reductions
Don't want to diagonalize every time.
If we know one undecidable language, we may be able to reduce/relate/transform one decision problem to another to show the other language is also undecidable.

Will show $HALT = \{ \langle M, w \rangle |~ M \text{halts on input } w \}$ knowing $A_{TM}$ is undecidable
- Given $A_{TM}, M, w$ instances, we construct a HALT instance
```
P = "On input <M, w>:
	Let M' = "On input x:
		Run M on x
		if is accepts, accept.
		Otherwise, loop."
	Output <M', w>."
```
- Clearly if $M$ accepts $w$, then so does $M'$ and it halts
- If $M$ dose not accept $w$, then $M'$ must loop
- Thus $M'$ halts on $w$ iff $M$ accepts $w$
	- $\langle M', w \rangle \in HALT \iff \langle M, w \rangle \in A_{TM}$

This is a **mapping reduction:**
- Given any two languages $A$ and $B$, we say $A \le_m B$ ($A$ mapping reduces to $B$) if we have some program $P$ such that:
	- $P$ halts on all inputs
	- If $x \in A$, then $P(x) \in B$
	- If $x \notin A$, then $P(x) \notin B$
- In above $A = A_{TM}, B = HALT$
- Thus if I can solve $B$, then I can use $P$ to solve $A$:
	- If $P(x) \in B$, then I know that $x \in A$
	- If $P(x) \notin B$, then I know that $x \notin A$
Theorems:
- If $A \le_m B$ and $B$ is decidable, then $A$ is decidable
- If $A \le_m B$ and $A$ is undecidable, then $B$ is undecidable
- If $A \le_m B$ and $B$ is recognizable, then $A$ is recognizable
- If $A \le_m B$ and $A$ is not recognizable, then neither is $B$
Also:
- If $A \le_m B$, then $\overline{A} \le_m \overline{B}$
	- Since $\exists P, (x \in A \iff P(x) \in B ) \implies (x \notin A \iff P(x) \notin B) \implies (x \in \overline{A} \iff P(x) \in \overline{B})$
- If $A \le_m B$ and $B$ is co-recognizable, then $A$ is co-recognizable
- If $A \le_m B$ and $A$ is not co-recognizable, then neither is $B$
___
# Mapping Reduction Examples
## $E_{TM} = \{ \langle M \rangle | L(M) = \emptyset \}$
- This accepts nothing
- Argue that $E_{TM}$ is co-recognizable
	- Must show a specific input $x$ and a time limit $k$ in which it accepts in: $\langle x, k \rangle$
- $E_{TM}$ is probably not recognizable
	- Need to prove it doesn't accept any input
## $L_1$
- Need to be given $N$ and time limits $k$s to accept $\langle N \rangle$ and $\epsilon$
	- Expect to be recognizable, not co-recognizable
## $L_2$
- This accepts 1 and not other string
- Can we prove that $M$ does not accept say 0?
	- It can theoretically take some large number that we won't get to, but we wouldn't know, so we can't prove this.
	- **In general, we can't prove that a TM doesn't accept something**
	- Not recognizable
- For co-recognizable
	- It either does not accept 
- Expect to be neither
## $ALL_{TM}$
- expect not co-recognizable
	- cannot prove it doesn't accept something
- expect not recognizable
	- cannot prove it accepts everything
- Neither
