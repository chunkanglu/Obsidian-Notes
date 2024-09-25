# 1
Clearly if we can check if $w \in CFG$ if there is a PCP instance that creates the string $w$, and we repeat the same for $w'$ then by combining those pieces one after the other, we get $ww'$

Or we can use pseudocode type (refence past C63) and prove either not recognizable or not co-recognizable
# 2

# 3

# 4
By definition an algorithm is polytime if it runs in polynomial time with respect to the size of the input. However, notice that the input to `FIND-FACT` are integers and the main loop in the algorithm from line 3 to 5 can run at most $O(b)$ times. As we consider integers as bit strings, this would actually lead to an exponential time. Therefore, the algorithm is not polytime (but actually pseudo-polytime).

