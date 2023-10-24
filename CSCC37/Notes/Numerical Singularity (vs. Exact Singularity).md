---
tags:
  - CSCC37
---
During numerical factorization in a Floating Point system, usually we cannot expect exact zeros, but "near singular" if all elements below (and including) the diagonal in column $k$ at the $k^{th}$ stage are of magnitude:
$$
\lessapprox \epsilon \cdot \max_{1 \le j < k}{|u_{jj}|}
$$
This is numerical singularity and the above is a common heuristic.