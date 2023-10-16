# Solutions
![[Week5Sol.pdf]]
# Part 1
## Q1
a not legal since count needs a grouby
b, c legal

## Q2
When there are duplicate surNames with the same campus

## Q3
```sql
SELECT sid, count(distinct dept)
FROM Offering, Took
WHERE Offering.oID = Took.oID
GROUP BY Took.sID
```

## Q4
a
```sql
SELECT *
FROM One RIGHT JOIN Two ON One.b = Two.b
```
b
```sql
SELECT *
FROM One LEFT JOIN Two ON One.b = Two.b
```
# Part 2

## Q1
For all students that took a course with Horton, return their sid, course name, and grade.
## Q2
Return all students' sid and surname that have a cgpa higher than the cgpa of the student with sid 99999.
# Q3
Return the sid, course name, and grade for students that have taken a course with students with surname Lakemeyer and got a grade of at least 80.
## Q4
a
Filter R such that only rows whose b value is in S's b column, then return the a column of the filtered relation.
b **DOES NOT WORK, HAS DUPLICATES WHEN SHOULDN"T HAVE try on part 1 q4**
```sql
SELECT a
FROM R, S
WHERE R.b = S.b
```
## Q5
Return instructors that have only taught once
## Q6
Return  unique oid in ascending order for offerings of CSC courses where students took the same course more than once.
## Q7
a
```sql
CREATE VIEW Counts AS

SELECT dept || cNum AS course, intructor, count(*) AS nOffering
FROM Offering
GROUP BY course, intructor
```