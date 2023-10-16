- Insert tuple
- Delete tuple
- Update tuple

## Insert
```sql
INSERT INTO some_table VALUES list_of_rows

INSERT INTO some_table (subquery)
```

```sql
CREATE TABLE Ages(name TEXT, age INT);
INSERT INTO Ages VALUES ('Emma', 21), ('Zach', 25);
```
```sql
INSERT INTO Ages
(
	SELECT DISTINCT firstname, 19 AS age
	FROM Student
		JOIN Took USING(sID) %% same as Student.sID=Took.sID %%
		JOIN Offering USING oID
	WHERE cnum <= 199
)
```

```sql
CREATE TABLE Invite
(
	name TEXT,
	campus TEXT DEFAULT 'StG',
	email TEXT,
	age INT
)

INSERT INTO Invite(name, email)
(
	SELECT firstname, email
	FROM Student
	WHERE cgpa > 3.4
)
```
Here campus gets default value and age gets NULL.

## Delete
```sql
DELETE FROM some_table
WHERE condition;

%% Drop table %%
DELETE FROM some_table
```

Usually good idea to first SELECT the condition to check thing works.

```sql
DELETE FROM Course
WHERE NOT EXISTS
(
	SELECT *
	FROM Took JOIN Offering USING(oid)
	WHERE
		grade > 50 AND
		Offering.dept = Course.dept AND
		Offering.cnum = Course.cnum
)
```

## Update
```sql
UPDATE some_table
SET changed thing
WHERE condition
```

Usually good idea to first SELECT the condition to check thing works.

```sql
UPDATE Student
SET campus = ‘UTSC’
WHERE sid = 99999;

UPDATE Took
SET grade = 50
WHERE grade >= 47 and grade < 50
```