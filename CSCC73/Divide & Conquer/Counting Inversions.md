# Problem
![[counting_inversion_problem.png]]
Give a divide and conquer algorithm that solves this problem in $O(n \log n)$. Hint: Sort the array in increasing order as you count the number of inversions.
# Idea
```python
countInversions(A, a, b):
	if a == b:
		return (A, 0)
	if b - a + 1 == 2:
		if A[a] > A[b]:
			return ([A[b], A[a]], 1)
		else:
			return (A, 0)

	m = (a+b) / 2
	AL, CL = countInversions(A, a, m)
	AR, CR = countInversions(A, m+1, b)
	# Find inversions across sections
	# Since we make each section sorted increasing, we do merge-like operation below
	A' = []
	CA = 0
	l = 0
	r = 0
	while l < len(AL) and r < len(AR):
		if AR[r] < AL[l]: # When there is inversion
			A'.append(AR[r])
			# Since AL is sorted, if AR[r] is less than AL[l], it is also less than all elements after l in AL
			CA += len(AL) - l # Num elements left in AL
			r += 1
		else:
			A'.append(AL[l])
			l += 1
	return (A', CL + CR + CA)
		
```