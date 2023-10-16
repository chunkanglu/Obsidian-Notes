Relation defined in terms of stored tables and other views
- Breaks down large queries
- Reduces repeated subqueries
### Types
- Virtual - temporary snapshot of a query output, without creating a new schema
- Materialized - actually constructed and stored
### Example
```sql
CREATE VIEW topresults AS

SELECT firstname, surname, cnum
FROM Student, Took, Offering
WHERE
	Student.sid = Took.sid AND
	Took.oid = Offering oid AND
	grade >= 80 AND
	dept = 'CSC'
```