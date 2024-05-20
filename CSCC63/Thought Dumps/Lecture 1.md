- Be sure to repeat and understand hard tutorial questions as 1 question will be pulled for each of midterm and final (no solutions for this, ask in OH and Piazza)
- limits of computation, what can we theoretically do with **any** computer
	- these are the limits of logic and not dependent on the actual performance of a computer
	- what can no computer ever solve even if we let it run indefinitely without memory constraints
	- *Halting problem* cannot be solved by computers
- Complexity - what can we solve efficiently
- Decisions problems are boolean problems
	- Given A, is B?
	- Given A, is there / does there exist B?
- A lot of these questions have a definite yes/no answer, but not all (given graph, give shortest path)
- Doing a shortest path on computer requires a stream of bits and we can reduce long functions to "what's the first bit?... second?"
- For problems
	- want to talk about problem input, but we call these "instances"
	- we say inputs as what we physically put in a program rather than a decision problem

- Encoding inputs
- we need to encode inputs in a way so that computer can understand what to work with
	- a computer cannot "read" a picture of a graph
- For graph $G$, the *encoded format* for the input is $\langle G \rangle$
	- $G$ is the object itself, $\langle G \rangle$ is the string representation of the object
	- these can the adjacency matrix / list

- Given a string and a language you can ask problems like is the string in the language
- decision problems and languages both embody similar ideas and revolve around sets of strings

- Algorithm is intuitively a sequence of logical steps we can use a computer to solve a problem
	- algos should halt on aall possible inputs in a finite amount of time / steps

> An algorithm to solve a problem is a logical sequence of steps which will, for any problem instance, terminate in a finite amount of time and give the solution for that instance.
- If every algo can be encoded in a certain type of object, and that object can't do something, then algorithms can't do that thing either

- Encoding algos can use Alonzo Church's Lambda Calculus, Emil Posts's computing machines, Alan Turing's Turing Machines
	- All these have the "same power", same level of representation
- DFSAs are a good start but not powerful enough to recognize things like $0^n 1^n$
- CFGs/PDAs (Push down Automatas) are a step above, but we still cannot recognise things like $\{w\#w | w \in \{ 0, 1 \}^* \}$
	- CFGs still cannot check if $w$ is the same before and after the $\#$
	- difference between DFSAs and CFGs is in memory
	- what if we had unrestricted finite memory? does this change things
	- These are still not enough for us to use

Turing machines
- similar to DFSAs but with some differences
- use an input table instead of input string
	- positions / cells on the sting represent memory cells
	- the string is written on the left, with unlimited number of blank characters as memory to the right for us to use
- Can move the head (pointer for which character we are looking at) to the left or right
	- direction of movement is determined by the arrow in the machine
	- *if we are already at the very left of the tape and we try to move left, we just don't move*
- Blank spaces on the right side of the tape are implicit, but if it's been written or modified, it should be written
- TM can write to the tape, which an arrow to show what to write
	- **Write come before movement**
	- In this model it has to move to the left or right, a machine with the same still movement has the same level of expression as it can be replicated by left-right machine
- ![[Pasted image 20240507131459.png]]
- starting with string $010\#011\_~\_~\_\ldots$
	- *NOTE:* $q_i$ should be under the char to its right
	- it follows starting at $q_1$: $q_1010\#011\textvisiblespace$
	- Go to $q_2$, pointing right, write an $x$, move right: $xq_210\#011\textvisiblespace$
	- Loop back to $q_2$, still pointing right, move right: $x1q_20\#011\textvisiblespace$
	- Again:  $x10q_2\#011\textvisiblespace$
	- Go go $q_4$, pointing right, move right: $x10\#q_4011\textvisiblespace$
	- Go to $q_6$, pointing left, write an $x$, move left:  $x10q_6\#x11\textvisiblespace$
	- $\cdots$
	- **TODO: finish this**
	- $xx0\#q_6xx1\textvisiblespace$
	- End: $xxx\#xxq_41\textvisiblespace$, No 1-arrow cannot continue, reject as not in accept state
- Treating TM like Assembly language, for the context of this course, we care less on the efficiency
- TM are easier to do math on due to little syntactic sugar to worry about
- For later *Post correspondence problem*

TM is a tuple:
$$
M = (Q, \Sigma, \Gamma, \delta, s, q_A, q_R)
$$
where:
- $Q$ is a set of states - nodes in the diagram
- $\Sigma$ is the input alphabet - finite set of input characters, but also other scratch characters (does not include the blanks $\textvisiblespace$ at the end). In prev example. $\Sigma = \{0, 1, \#\}$
- $\Gamma$ is the tape alphabet
- $\delta$ is the transition function - the arrows
	- $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{ L, R \}$
- $s$ is the start state
- $q_A$ is the accept state, if we ever enter this state we halt and accept
- $q_R$ is the reject state

- It is possible to have non-determinism in a Turing Machine
	- apparently this doesn't change *Computability* (what we can calculate), but does affect *Complexity*

- Why TMs
	- basically program them the way we do regular computers
	- their configurations are fairly well-behaved, we can do math, so we can relate TMs (and computability results from TMs) to non-TMs