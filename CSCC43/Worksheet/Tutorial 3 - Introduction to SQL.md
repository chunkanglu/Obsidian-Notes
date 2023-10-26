# Part 1
## Q1
- n + m
- min(n, m)
- max(0, n - m)
## Q2
```sql
(SELECT term
FROM Offering
WHERE instructor = 'Jepson')
INTERSECT ALL
(SELECT term
FROM Offering
WHERE instructor = 'Suzuki')
```
## Q3
```sql
(
	SELECT DISTINCT sid
	FROM Took
	WHERE grade >= 85
)
UNION
(
	SELECT sid
	FROM Took, Offering
	WHERE Took.sid = Offering.sid
	AND instructor = 'Atwood'
	AND grade > 50
);
```
## Q4
```sql
SELECT DISTINCT term
FROM Offering
WHERE term NOT IN (
	SELECT term
	FROM Offering
	WHERE dept = 'CSC'
	AND cNum = '369'
)
```
```sql
(
	SELECT DISTINCT term
	FROM Offering
)
EXCEPT
(
	SELECT DISTINCT term
	FROM Offering
	WHERE dept = 'CSC'
	AND cNum = '369'
)
```
## Q5
```sql
SELECT oid, results
FROM (
	SELECT oid, 'high' AS results
	FROM Took
	GROUP BY oid
	HAVING AVG(grade) >= 80
) H UNION
(
	SELECT oid, 'low' AS results
	FROM Took
	GROUP BY oid
	HAVING AVG(grade) < 60
)
ORDER BY oid
```
## Q6
Union all keeps duplicates when union does not.
Count the number of times each student earned a grade of 85 or more in some course or passed a course taught by Atwood. This case, union all is needed to have the count be correct.
# Part 2
## Q1
```sql
SELECT sid, MIN(grade)
FROM Took
GROUP BY sid
HAVING AVG(grade) > 80
```
## Q2
```sql
SELECT oid, AVG(grade) AS A, MIN(grade), MAX(grade)
FROM Took
GROUP BY oid
ORDER BY A DESC
```
## Q3
```sql
SELECT Student.sid, surname, AVG(grade)
FROM Student, Took
WHERE Student.sid = Took.sid
GROUP BY Student.sid, surname
HAVING count(Student.sid) >= 10
```
## Q4
```sql
SELECT Took.oid, sid, Took.grade
FROM (
	SELECT oid, MAX(grade) AS grade
	FROM Took
	GROUP BY oid
)MTook, Took
WHERE MTook.oid = Took.oid
AND MTook.grade = Took.grade
```
```sql
%% solution from TA odd %%
SELECT  
t1.oID,  
t2.sID,  
t2.grade  
FROM Offering t1  
INNER JOIN Took t2 ON t1.oID = t2.oID  
WHERE t2.grade = (  
SELECT MAX(grade)  
FROM Took t3  
WHERE t3.oID = t1.oID  
)
```
## Q5
```sql
SELECT instructor, AVG(cgpa)
FROM Offering, Took, Student
WHERE Offering.oid = Took.oid
AND Took.sid = Student.sid
GROUP BY instructor
ORDER BY AVG(cgpa)
```
# Part 3
## Q1
- Top left not legal since sid is ambiguous, and also surname is not in group by nor an aggregate value
- Bottom left, surname not aggregate value nor in group by
## Q2
- Bottom left not legal, dept, cnum not aggregate nor in group by
- Bottom right oid not agg nor in group by
