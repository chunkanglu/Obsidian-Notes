## Q1
1. m + n
2. min(m, n)
3. n?

## Q2
```sql
(SELECT term
FROM Offering
WHERE instructor="Jepson")
INTERSECT
(SELECT term
FROM Offering
WHERE instructor="Suzuki")
```
## Q3
```sql
(SELECT sID
FROM Took
WHERE grade >= 85)
UNION
(SELECT sID
FROM Took, Offering
WHERE Took.oID = Offering.oID
AND Offering.instructor = "Atwood"
AND Took.grade > 50)
```
## Q4
```sql
(SELECT DISTINCT term
FROM Offering)
EXCEPT
(SELECT DISTINCT term
FROM Offering
WHERE dept = "CSC" AND cNum = "369")
```
## Q5
```sql
(SELECT oID, 'high' as results
FROM Took
GROUP BY oID
HAVING AVG(grade) >= 80)
UNION
(SELECT oID, 'low' as results
FROM Took
GROUP BY oID
HAVING AVG(grade) < 60)
ORDER BY oID %% ? %%
```
## Q6
Union all keeps duplicates