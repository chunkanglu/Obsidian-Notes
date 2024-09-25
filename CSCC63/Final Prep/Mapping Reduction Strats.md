# Specific Input Values
If you need to prove there exists a certain (form of) input that gets accepted, then you can make it so that one specific input does something else compared to other inputs
```
# From HALT
Let P = "On Input <M, w>":
	Let M0 = "On input <x>:
		If x != 01, accept.
		Run M on w.
		Accept.
	Return <M0>"
```
Can also place the condition after:
```
# From HALT
Let P = "On Input <M, w>":
	Let M0 = "On input <x>:
		Run M on w.
		If x == 1, accept, else, reject.
	Return <M0>"
```
# Running For Limited Steps
When we need to differentiate between halted and not
# Using Length of Input
Useful for `for all` type language reductions where you need to reduce from HALT (or complement) and do something **when it does not halt**.
This works because you can "spread" the number of steps run over an arbitrary large amount.
```
# From HALT-comp
Let P = "On Input <M, w>":
	Let M0 = "On input <x>:
		Let k = |x|.
		Run M on w for k steps.
		If it halts, loop, else, accept.
	Return <M0>"
```
# Multiple TMs in Language
Try to make one more elaborate and the others simpler and match the elaborate one.