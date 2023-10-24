# Problem
We are given a list of $n > 0$ objects, say $X = (x_{1} , x_{2} , . . . , x_{n} )$. The only operation we can do on these objects is equality testing (therefore we can not sort it). We must find all objects which occur in $X$ strictly more than $\frac{n}{3}$ times. (We define $|X|$ to be this $n$.)
# Idea
If an item occurs more than $\frac{n}{3}$ times, then it must occur more than $\frac{n}{3}$ times in at least one of the halves.

```python
freqThird(X, a, b):
	if a == b:
		return (X[a], (1))
	# Else b > a
	m = floor((b+a-1) / 2)
	DL, CL = freqThird(X, a, m)
	DR, CR = freqThird(X, m+1, b)
	
	# Combine candidates for > n/3
	# DL, DR will be naturally sorted
	# Essentially the merge operation but if its the same value as the one last added, we only increment count and not add duplicate to D
	D = []
	C = []
	l = 0
	r = 0
	while l < len(DL) and r < len(DR):
		if D != [] and DL[l] == D[-1]:
			C[-1] += CL[l]
			l += 1
		elif D != [] and DR[r] == D[-1]:
			C[-1] += CR[r]
			r += 1
		elif DL[l] >= DR[r]:
			D.append(DL[l])
			C.append(CL[l])
			l += 1
		else:
			D.append(DR[r])
			C.append(CR[r])
			r += 1
	if l < len(DL):
		D += DL
		C += CL
	else:
		D += DR
		C += CR
		
	# Remove candidates that < n/3
	DF = []
	CF = []
	for i in range(D):
		if C[i] > n/3:
			DF.append(D[i])
			CF.append[C[i]]

	return (DF, CF)


D, _ = freqThird(X, 1, n)
```
# Runtime
a = 2
b = 2
d = 1
Total Complexity: $O(n \log n)$