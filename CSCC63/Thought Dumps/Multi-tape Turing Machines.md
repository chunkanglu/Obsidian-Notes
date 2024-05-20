- Can emulate multi-tape behaviour with a single tape
	- **Thus multitape does not have more power than single tape**
- Need a character not in the tape input alphabet $\#$ to separate tapes
- Need a state head for each section
- Init head of multitape to left side of tape
- While not halting (accept / reject), emulate a single step
	> The TM would essentially have a tree-ish shape, since it would create a "branch" for each transitions in tape1, then for each of tape1 transitions would have a branch for each transition in tape2, and so on.
	
	- Scan through left to right, advancing to see which combination of transitions across all tapes to perform, stopping once we find the end
	- Go right to left, actually performing each action, then advancing until the "previous" tape by moving left until a state is found