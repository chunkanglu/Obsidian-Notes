In a TM, $0, 1 \to R$ for $q_2 to q_4$ is effectively$q_2, 0 \to q_2, 0, R$ and $q_2, 1 \to q_2, 1, R$
- We shouldn't write the blank char as we treat it like a delimiter

TM to recognize $L = \left\{ 1^{2^n} | n \in \mathbb{N} \right\} = \{ 1, 11, 1111, 11111111, \ldots \}$
- Base case, do I have a single 1
- Then take half of the string and check if it is a power of 2
- We do this by crossing off every other 1
- After reaching the end of the string we go back to the beginning and repeat the process
![[Drawing 2024-05-09 14.23.21.excalidraw]]

- All programs can be compiled down into a TM
- But is there more powerful automata
	- multiple tapes
	- non-determinism
	- Use RAM instead of linear tape

# Multi-tape Turing Machines
- Read a character from each tape once a turn
- Each tape can move a different direction and write a different character if needed
- For 3 tapes it could look something like this
![[Drawing 2024-05-09 14.40.24.excalidraw]]
- **Fun thing is that multi-tape machines can be replicated with a single tape machine**
> Given tapes:
> $\$10X01$
> $\$X1110X0$
> $\$1010$ 
> Can become: $\$10q_1X01\#\$X11q_110X0\#\$q_11010$
> By combining to together with $\#$  and also with multiple tape heads written on to the tape so we can move the real tape head around without forgetting where we are in each individual string. 
> ![[Drawing 2024-05-09 14.56.00.excalidraw]]
> The idea is to branch off when we get to the next string's state, and then keep moving right until the next section's head.
> Once we reach the end, we can always keep moving left to find the heads of each tape.
> 
> One pass left to right give each character of the tape.
> Transition functions walking right to left can then update the characters in each tape.
> 
> Actual implementation can be tricky since if we want to write to end of tape 1 but before tape 2, you need to shift everything after it
- Original machines may take $n^3$ steps, and emulating can have $n^3$ cost
	- You have to branch off like 3 times for each next state which creates the cubed complexity
