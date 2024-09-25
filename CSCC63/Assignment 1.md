# 1
## a
Turns out only $q_0, q_1, q_2$ are used if empty string is inputted.

\item $q_0\textvisiblespace$
\item $0q_1\textvisiblespace$
\item $01q_2\textvisiblespace$
\item $0q_211$
\item $q_2001$
\item $1q_101$
\item $11q_01\textvisiblespace$
\item $110q_1\textvisiblespace\textvisiblespace$
\item $1101q_2\textvisiblespace$
\item $110q_211$
\item $11q_2001$
\item $111q_101$
\item $1111q_01\textvisiblespace$
\item $11110q_1\textvisiblespace\textvisiblespace$
\item $111101q_2\textvisiblespace$
```latex
\begin{enumerate}
	\item $q_0\textvisiblespace$
	\item $0q_1\textvisiblespace$
	\item $01q_2\textvisiblespace$
	\item $0q_211$
	\item $q_2001$
	\item $1q_101$
	\item $11q_01\textvisiblespace$
	\item $110q_1\textvisiblespace\textvisiblespace$
	\item $1101q_2\textvisiblespace$
	\item $110q_211$
	\item $11q_2001$
	\item $111q_101$
	\item $1111q_01\textvisiblespace$
	\item $11110q_1\textvisiblespace\textvisiblespace$
	\item $111101q_2\textvisiblespace$
\end{enumerate}
```
# b
Note its not only for the empty string input.
**Answer is probably 3**

If we don't write anything, then we will have a difference of at most 2 as the character to move to and head will have swapped places:
Example: Assume X is anything and we take $0 \to R$ arrow from $q_x$ to $q_y$
$\ldots 0q_x0\ldots$
becomes
$\ldots 00q_y\ldots$
diff 2

If we have arrow $0 \to L$ it becomes
$\ldots q_y00\ldots$
diff 2

If we have arrow $0 \to 1, L$ it becomes
$\ldots q_y01\ldots$
diff 3

**Lemma: At most 3 characters can change between two neighbouring configurations in any TM**
By moving right, no write: change 2
By moving right, write: change 2
By moving left, no write: change 2
By moving left, write: change 3 (2 from moving swap, 1 from the character written to the right of the swapped characters)
Edge case at the start of string, moving left, no write: 0 change
Edge case at the start of string, moving left, write: 1 change

Most difference from moving left and writing.
We can see this is possible in $M_2$ by observing $C_9$ and $C_10$ shown in part a.
# 2
We generally aren't able to prove something isn't in a language
Show that $\overline{L_2}$ is not co-recognizable
$$
\overline{L_2} = \{ \langle M \rangle ~ | ~ \forall n \in \mathbb{N}, 0^n1^n \in L(M) \}
$$
We want all $0^n1^n \in L(M_0)$ ($M_0$ accepts every $0^n1^n$) iff M halts on w
Just have $M_0$ accept everything?
Proof that $\text{HALT} \leqslant_m \overline{L_2}$:
HALT not co-recognizable so neither should be $\overline{L_2}$.

Consider the TM $P$ "On input $\langle M, w \rangle:$
1. Construct the TM $M_0$ as follows:
	$M_0$ = "On input $x$:
		1. Pass.
		2. Run $M$ on $w$.
		3. Accept."
2. Return $\langle M_0 \rangle$. "

Proof that $\langle M_0 \rangle \in \overline{L_2}$ iff $\langle M, w \rangle \in$ HALT
- ($\impliedby$) Suppose that $\langle M, w \rangle \in$ HALT.
	- Then for every input $x$, $M_0$ reaches line 2.
	- When it does, $M$ will halt and $M_0$ will reach line 3 in which it accepts.
	- So $M_0$ will accept every input.
	- $\implies$ $M_0$ accepts all $0^n1^n, \forall n \in \mathbb{N}$
	- $\implies \langle M_0 \rangle \in \overline{L_2}$
- ($\implies$) Suppose that $\langle M, w \rangle \notin$ HALT
	- Then for every input $x$, $M_0$ reaches line 2.
	- When it does, $M$ will halt and $M_0$ will never reach line 3 and accept
	- So $M_0$ will not accept any input.
	- $\implies$ $M_0$ does not accept any $0^n1^n, \forall n \in \mathbb{N}$
	- $\implies \langle M_0 \rangle \in L_2$
As we know HALT is not co-recognizable, it must be that $L_2$ is not co-recognizable.
# 3
**Basically the same as 2?**
Consider the TM $P$ "On input $\langle M, w \rangle:$
1. Construct the TM $M_0$ as follows:
	$M_0$ = "On input $x$:
		1. Pass.
		2. Run $M$ on $w$.
		3. Accept."
2. Return $\langle M_0 \rangle$. "

Proof that $\langle M_0 \rangle \in L_3$ iff $\langle M, w \rangle \in$ HALT
- ($\impliedby$) Suppose that $\langle M, w \rangle \in$ HALT.
	- Then for every input $x$, $M_0$ reaches line 2.
	- When it does, $M$ will halt and $M_0$ will reach line 3 in which it accepts.
	- So $M_0$ will accept every input.
	- $\implies$ $M_0$ accepts some $0^n1^n$ for some $n \in \mathbb{N}$
	- $\implies \langle M_0 \rangle \in L_3$
- ($\implies$) Suppose that $\langle M, w \rangle \notin$ HALT
	- Then for every input $x$, $M_0$ reaches line 2.
	- When it does, $M$ will halt and $M_0$ will never reach line 3 and accept
	- So $M_0$ will not accept any input.
	- $\implies$ $M_0$ does not accept any $0^n1^n, \forall n \in \mathbb{N}$
	- $\implies \langle M_0 \rangle \notin L_3$
As we know HALT is not co-recognizable, it must be that $L_3$ is not co-recognizable.

# 4
Language contains instances of tuples $\langle M, k \rangle$ such that there exists some string $w$ where $M$ accepts $w$ within $k$ steps.
- Probably *recognizable*, since we can concretely say if accepts given a specific $w$
- Probably *not co-recognizable*, since what requires proving no string is accepted which is generally not do-able (as there are infinitely many strings)
# 5
$$
L_5 = \{ \langle M \rangle | \forall w \in \Sigma^*, w \in L(M) \lor \exists n \in \mathbb{N} \text{ such that } w = 0^n 1^n \}
$$

# 6
**are be describing M itself or are we using M?**

start 0,0 cell and all other empty
reads final char in all strings in the 3 by 3 grid centered at i, j and current state for transition
write to end or erase final character in string (**can we edit final char?**)
	this is somewhat like either writing the final character or using the previous character but with some difference
change state and move to *any* of the cells in the 3by3 grid it read from
	**is the state not tied to the location of the cell?**

$> 9$ tapes? one for each of the 3 by 3 grid to store location
	could just be one tape with like (middle-xy, top-left-xy, top-mid-xy, ...) if we want less tapes, but this is effectively what emulating multitape with single tape does
one for current state
one to store the next positions for the 3x3 (like $XX\#XX\#\ldots$) so that next turn they get copied over respectively, then these get emptied
	These could also just be separate tapes to make things more readable

*still need a way to store the strings inside each cell so that they can be retrieved using the locations*
	maybe something like ($\text{x-coord}|\text{y-coord}|\text{string}$), but we still need a good way to order things for it to be able to sweep through the tape and find the right 
		actually we don't need to order it, it doesn't need to be efficient

add char at end becomes (starting from empty to the right of existing) write char then move right
delete char at end becomes write nothing, move left, write empty, don't move (somehow)

1. Store (i, j) location
2. Store (i-1, j) location
3. Store (i+1, j) location
4. Store (i, j-1) location
5. Store (i, j+1) location
6. Store (i-1, j-1) location
7. Store (i-1, j+1) location
8. Store (i+1, j-1) location
9. Store (i+1, j+1) location
10. Store current state
11. Store strings at each location
	1. This can be in a format like $\text{x-coord}|\text{y-coord}|\text{string}$ for each location, split by delimiters such as $\#$
	2. Writing a character at the end in $P$ would be done in $M$ by finding the corresponding location section in this tape, shifting all characters after it to the right by 1, then writing the new character with the space created
	3. Deleting a character at the end in $P$ would be done in $M$ similarly to writing a new character by finding corresponding location, then shifting all characters after the last character left by 1 to remove the last character from the section

```
probably not needed, we can just directly override when needed
11. Store next (i, j) location
12. Store next (i-1, j) location
13. Store next (i+1, j) location
14. Store next (i, j-1) location
15. Store next (i, j+1) location
16. Store next (i-1, j-1) location
17. Store next (i-1, j+1) location
18. Store next (i+1, j-1) location
19. Store next (i+1, j+1) location
```
 Questions
 - I believe we assume that transitions in $P$ are able to be transformed into a format $M$ can use, according to our specification?
 - Is the pseudocode essentially writing the individual steps that the TM $M$ would take to replicate $P$? So lines somewhat like: "Read from tape 1, then do ...". I couldn't really find anything similar in the notes.
 - If we need to use operations like shift everything after a character left/right or scanning through a tape to match some character(s), do we need to explicitly specify how or can we assume we already know how to do these? We've seen these operations being used in lecture for explaining multi-tape to single tape, and it looks like we assumed we have that functionality.
# 7
# 8 (Bonus)
