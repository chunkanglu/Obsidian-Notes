## SubQuery in FROM clause
- Subqueries must be in brackets
- Subqueries should be named
### Example
$Took \times \rho_{Hoffering}{(subquery)}$
```sql
SELECT sid, dept||cnum as course, grade %% where || is string concatenation %%
FROM Took, (
	SELECT *
	FROM Offering
	WHERE instructor='XYZ') Hoffering
WHERE Took.oid = Hoffering.oid;
```

## SubQuery in WHERE clause
- Used when subquery is guaranteed to produce **exactly 1 tuple** and can be used as a value
- Easiest is when it only has 1 component/column (ie. it gives a direct value)
- We cannot do this directly in Relational Algebra
	- RA cannot handle NULL values
	- We would use a different format
### Example
```sql
SELECT sid, surname
FROM Student
WHERE cgpa >
	(SELECT cgpa
	FROM Student
	WHERE sid = 99999);
```
- If subquery returns NULL, then our overall output may be NULL
- If subquery returns more than one row, we get `ERROR: more than one row returned by a subquery used as an expression`.
### Quantifying over multiple results
$\forall$ ALL, $\exists$ SOME/ANY
```sql
SELECT sID, surname, cgpa
FROM Student
WHERE cgpa >= ALL %% or SOME %%
	(SELECT cgpa
	FROM Student
	WHERE campus='UTSC')
```
## IN operator
- Iff value(s) are in the set of rows generate by the subquery
```sql
SELECT sID, dept||cnum AS course, grade
FROM Took JOIN Offering On Took.oID = Offering.oID
WHERE Took.oID IN %% or NOT IN %%
	(
		SELECT oID
		FROM Offering
		WHERE instructor='Atwood'
	);
```
## EXISTS Operator
- Iff subquery result has at least one tuple
- Kind of like an if-statement for each outer query output row
### Example
Correlated subquery
- Student is the inner query references the Student in outer query
```sql
SELECT surname, cgpa
FROM Student
WHERE EXISTS (
	SELECT *
	FROM Took
	WHERE Student.sid = Took.sid and grade > 85; 
)
```
**TODO:** FIND A BETTER EXAMPLE
## Scoping
- Evaluated inside out
- If you need to use result from inner query in outer one, use naming
- If it refers to any name defined outside of itself, it must be evaluated once for each tuple
in the outer query. These are called correlated subqueries