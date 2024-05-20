- TM that takes in other TMs and emulates those TMs
	- Universal TM $U$ takes inputs $<M, w>$
- TM $M = (Q, \sum, \Gamma, \delta, s, q_A, q_R)$
- Since the parameter $M$ can have various tape alphabets $\Gamma$ and $U$ can only have its own, we need to assume that $\Gamma$ has been encoded in some way that $U$ can understand and use

- Suppose $w = 01011$
- $U$ uses 3 tapes
	1. stores transition functions and the string $w$
		1. $\delta \# 01011$
	2. stores the tape of $M$
		1. $\underset{\uparrow}01011$
		2. can use the tape head here for the tape head in $M$
	3. holds the current state of $M$
		1. $q_0$

## Running $U$
- If $<M, w>$ is not the right format, reject
- Copy $<\delta, w>$ to first tape, $w$ to second, $s$ to third
- While $M$ not halted
	- Check if in accept for reject state
	- Simulate step of $M$
		- get current state from tape 3
		- Compare with encoded transitions in $\delta$ and update the state and tape of $M$ to match
		- If no transition matches, reject

## Usage
Allows us to use these:
On Input <M, w, k>:
	1.
	2.
	...
	i. Run M on w for k steps.