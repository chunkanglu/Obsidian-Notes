- Multitape
	- walk right until blank char
	- a new character is in the tape alphabet for every state in the old multi-tape machine
	- There are |Q\ states
	- For each time we branch off when we see the state for one chunk of the tape, we create a new state in the new machine
		- at most $|\Gamma|$ states
		- Since this repeats for each branching, there are $O(n|Q||\Gamma|^n)$ total states needed to remember all this
			- **TODO: draw out concrete example**

- |Q| copies, one for each old state
- For each of the states, it moves until tape head reaches new section and this is recorded as a new state
- $|\Gamma|$ possible branches

- **Could there ever be an issue of needing to run the transitions for the k tapes in a specific order?**
	- I guess we can just add more states to add more movement

- if each of the original tapes takes $O(n^2)$ time, when emulated, we takes each of those steps
	- doing each of the forward & backward passes is linear to the size of the entire string
	- In worst case, we write a char at each step and add length each time so update would take $O(n^2)$
	- Thus total time is $O(n^4)$

If og multi-tape machine takes $O(f(n))$ then the new one would become $O([f(n)]^2)$ time
___
- For non-deter TM, we use BFS cuz DFS may end up getting stuck looping if there are multiple ways to get to the same config (unless if extra logic added for checking if seen using third tape)
- Time taken $\approx$ size of tree $\approx 2^{O(\text{tree height})}$
	- exponential slowdown
	- There is no known faster way to do the reduction
___
- Most programming languages have some function that takes in a piece of code and runs it
- Universal TM takes a TM $M$ and a string $w$ as input
- $M = (Q, \sum, \Gamma, \delta, q_0, q_A, q_R)$
- Suppose $w = 01011$
- $U$ uses 3 tapes
	1. stores transition functions and the string $w$
		1. $\delta \# 01011$
	2. stores the tape of $M$
		1. $\underset{\uparrow}01011$
		2. can use the tape head here for the tape head in $M$
	3. holds the current state of $M$
		1. $q_0$
- small issue if tape alphabets between $M$ and $U$ differ
	- This is because $M$ is an input and not fixed, so we cannot hardcode the tape alphabet
	- Can encode the whole tape alphabet $\Gamma$ of $M$ as something like binary (ie. a prefix code) or another format that our own tape alphabet uses
		- **Do we need to physically store the encoding somewhere**
	- This is why the second tape of $U$ is used
- can use  a new TM to compare 2 characters in the same position, to find the right transition function that corresponds to the encoded character from the new tape alphabet
Allows for:
```
On Input <M, w>:
	1.
	2.
	...
	i. Run M on w for k steps.
```


Which yes-no decision problems can halt on all inputs and solve the decision problem