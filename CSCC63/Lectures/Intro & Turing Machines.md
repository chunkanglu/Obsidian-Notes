This course investigates 2 main topics of:
1. *Computability* - What questions can logic ever solve given some indefinite but finite amount of time and memory?
2. *Complexity* - What questions can logic solve efficiently?
# Terminology
*Decision Problem* - Some problem with a yes / no boolean answer
- These can have the form "Given A, is B" or "Given A, does there exist B"
- You can alternatively describe these problems with set notation to show the set of *instances* (see right below) that evaluate to yes
*Instance* - "Inputs" are what go into a program, and we differentiate it with what goes into the problem
- Do note that we need to be able to encode the objects we ask questions about into a format that can be used by a computer (ie. things like real numbers, not floating-point approximations would not work as they require infinite memory)
*Encoded format* - Things like a graph must be transformed for a computer to interpret it. For graph $G$, the *encoded format* for the input is $\langle G \rangle$
*Algorithm* - A logical sequence of steps which will, for any problem instance, terminate in a finite amount of time and give the solution for that instance.
- Some programs such as operating systems are not algorithms, as they technically don't halt themselves (the processes running do)
- We cannot be certain on the result of computation on non-halting algorithm, but there still can be uses **IN ASSIGNMENT 1**
# Algorithms as Objects
There needed to be a generic way to describe an algorithm instead of concrete implementations. Mathematicians thus made various formalisms to describe algorithms like Lambda Calculus and Turing Machines.
It turns out that these are the maximum limit of computational power, and these formalisms allow for the same level of representation. Additionally, these describe what a human could do with pen and paper as well as on a computer.
# Turing Machines
A much more powerful and expressive variant of automata compared to DFSAs and PDAs / CFGs.
- Arbitrarily large computing times
	- The head (position of the character in question) can move left or right when reading
- Unrestricted access to memory
	- It is allowed to write / modify characters
	- There is an implicit unlimited number of blank $\textvisiblespace$ characters to the right of the string
## Running a string through
1. Have the head at the first (leftmost) character of the string
2. Read the character
3. If there is an arrow coming out of the current state with this character, continue, else stop and determine if it stopped on an accepting state
4. See if there is anything to write to the current position
5. Move the head in the specified direction
	1. If we are already at the very left of the tape and try to move left, just stay in place
6. Repeat until halt
## Formal Definition
A Turing Machine is a tuple:
$$
M = (Q, \Sigma, \Gamma, \delta, s, q_A, q_R)
$$
where:
- $Q$ is a set of states - nodes in the diagram
- $\Sigma$ is the input alphabet - finite set of input characters, but also other scratch characters (does not include the blanks $\textvisiblespace$ at the end). In prev example. $\Sigma = \{0, 1, \#\}$
- $\Gamma$ is the tape alphabet - set of available input characters, and any other characters we might see in computation. In prev example, $\Gamma = \left\{ 0, 1, \#, x, \textvisiblespace \right\}$
	- $\Sigma \subseteq \Gamma$ and $\textvisiblespace \in \Gamma$
- $\delta$ is the transition function - the arrows
	- $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{ L, R \}$
- $s$ is the start state
- $q_A$ is the accept state, if we ever enter this state we halt and accept
- $q_R$ is the reject state