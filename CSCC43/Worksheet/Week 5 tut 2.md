# Part 1 Joins
## Q1
a legal
b not legal which distinct to select is ambiguous
c legal
## Q2
duplicate surname with different campus
## Q3
```sql
SELECT sid, COUNT(DISTINCT dept)
FROM Took, Offering
WHERE Took.oid = Offering.oid
GROUP BY sid
```
## Q4
a
```sql
SELECT *
FROM One RIGHT JOIN Two On One.b = Two.b
```
b
```sql
SELECT *
FROM One LEFT JOIN Two On One.b = Two.b
```
# Part 2 Subqueries
## Q1
Return student's course grade for courses taught by horton
## Q2
Return students whose cgpa is grater than that of the student with sid 99999
## Q3
REturn students who got a grade of at least 80 in courses student with the surname Lakemeyer have taken
## Q4
a
Returns a values for rows in R whose b value is in the b column in S
b
Nope, theres no way to filter the b in this way without introducing duplicates in a
## Q5
Return instructor who have only taught once
## Q6
Return courses that students who have taken a CSC course have taken
## Q7
a
```sql
CREATE VIEW Counts AS
SELECT dept || cNum AS course, instructor, count(*) AS nOfferings
FROM Offering
GROUP BY course, instructor
```
b
```sql
SELECT Counts.course, Counts.instructor, Counts.nOfferings
FROM (
	SELECT course, MAX(nOfferings) AS ma
	FROM Counts
	GROUP BY course
) mOffer, Counts
WHERE mOffer.course = Counts.course
AND mOffer.ma = Counts.nOfferings
```
## Q8
```sql
SELECT surname, email
FROM Student
WHERE NOT EXISTS (
	SELECT *
	FROM Took, Offering
	WHERE Student.sid = Took.sid
	AND Took.oid = Offering.oid
	AND Offering.dept = 'CSC'
)
```
## Q9
```sql
SELECT DISTINCT Offering.instructor
From Offering
WHERE EXISTS (
	SELECT *
	FROM Took
	WHERE Offering.oid = Took.oid
	AND Took.grade = 100
)
```
## Q10
```sql
(
 SELECT 'junior' AS level, AVG(grade)
 FROM Took, Offering
 WHERE Took.oid = Offering.oid
 AND Offering.cNum >= 100
 AND Offering.cNum <= 299
)
UNION
(
 SELECT 'senior' AS level, AVG(grade)
 FROM Took, Offering
 WHERE Took.oid = Offering.oid
 AND Offering.cNum >= 300
 AND Offering.cNum <= 499
)
```