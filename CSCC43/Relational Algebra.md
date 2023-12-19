# Unary Operators
#### Select
Select rows from Table
$\sigma_{rows}(Table)$ 
#### Project
Select columns from Table, duplicate rows are removed
$\pi_{columns}(Table)$
#### Rename
Rename a column from old to new in a given Table
$\rho_{old \rightarrow new}(Table)$
# Binary Operators
#### Cartesian Product
All possible combination of values in the two columns
- Can introduce tuples that don't make sense
$A \times B$
#### Natural Join
Essentially Inner join that implicitly matches on common columns.
$A \bowtie B$
#### Union
Combine rows together, duplicates get combined into one row
$A \cup B$
#### Intersection
Row that are present in both sets. Both sets should have same columns
$A \cap B$
#### Difference
Rows in $A$ but not in $B$
$A - B$
#### Division
If problem has *every* or *all* then likely use division
$A / B = \pi_{x}(A) - \pi_{x}((\pi_{x}(A) \times B) - A)$
- Suppose $A / B = T$. $T$ is essentially: "what values of the other columns can we Cartesian product with $B$ such that all rows are in $A$".
	- $\pi_x(A) \times B$ Theoretical all combinations if *all* of B had combination with column $x$ of $A$
	- $\pi_{x}((\pi_x(A) \times B) - A)$ Get combinations that do not exist and find corresponding $x$ column values (which are the ones that do not have all)
	- Subtract from all possible $x$ column values the violations for those that have all
- Columns of $S$ must be a subset of columns in $R$
#### Theta Join
Basically natural join but instead of condition being equal on same columns, it is join when satisfying condition $theta$
$A \bowtie_{\theta} B = \sigma_{\theta}(A \times B)$
#### Equi Join
Special case of Theta Join.
Natural join but you can specify what columns you want equal
$A \bowtie_{A_i=B_j, A_m=B_n} B$
#### Outer Joins
- Full outer join A ⟗ B
- Left join $A ⟕ B$
- Right join $A ⟖ B$
## Operator Precedence
1. $\sigma, \pi, \rho$
2. $\bowtie, \bowtie_{\theta}, \times$
3. $\cap$
4. $\cup, -$

# Grouping
$\Gamma_{groupKeys, f(aggregateAttri)}(Table)$
# Sorting
$\tau_{sortAttri}(Table)$ sort ascending
$\tau_{-sortAttri}(Table)$ sort decending
# General Tips
## Max
Pair tuples with itself and get those that are not max (have another tuple that is larger than it), then subtract this from all tuples to get the max(es)
## Min
Same idea as [[#Max]]
## k or more
Create combinations with k cartesian products to form combinations such that they satisfy the condition wanted
## Exactly k
Set of k or more - Set of k+1 or more
## Every/All
Either use division directly or perform the broken up steps of division separately (if there is the need to)