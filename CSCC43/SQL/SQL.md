---
tags:
  - CSCC43
---
- Formal language for interacting with DBMS
- 2 parts
	- DDL - data Definition Language for defining schemas
		- Database administrators
	- DML - Data manipulation language for writing queries and modifying database
- SQL returns bags, not sets, so duplicates are kept
## Syntax
```sql
SELECT attributes
FROM tables
WHERE conditions for rows
GROUP BY aggregate cols
HAVING conditions for group
ORDER BY col to sort by
```
- Convention uppercase for keywords, but not actually case sensitive
- Identifiers like column names not case sensitive
- Literal strings are case sensitive, use single quotes
- Whitespace is ignored
### SELECT
- attributes from table
- expressions
```sql
SELECT sid, grade + 10 AS adjusted
FROM Took
```
- Constant expressions
```sql
SELECT dept, cNum, 'satisfies' AS breadthRequirement
FROM Course
WHERE breadth
```
### FROM
- identifies tables in query
- Optional - specify joins (but often just use WHERE)
- Optional - rename tables
	- nested queries
##### Examples
```sql
%% Select explicit table %%
FROM Student

%% Renaming %%
FROM Student AS S

%% Select multiple tables (cartisian product) %%
FROM Student, Course

%% Joining without condition (cartisian product) %%
FROM Student S JOIN Took T

%% Equi-join %%
FROM Student S JOIN Took T
ON S.ID = T.S_ID
```
#### Renaming
```sql
%% Rename table %%
SELECT e.name, e.id
FROM employee e

%% Rename attributes %%
SELECT e.name AS n
FROM employee e
```

#### Self Join
```sql
SELECT e1.name, e2.name
FROM employee e1, employee e2
WHERE e1.salary < e2.salary
```

### WHERE
- Filtering columns
```sql
SELECT name, sid, grade
FROM Course, Offereing, Took
WHERE Course.dept = Offering.dept AND
	Course.cnum = Offering.cnum AND
	Course.oid = Took.oid AND
	Course.dept = 'CSC'
```
- Boolean expressions
	- comparison >, <, ...
		- <> is not equals
	- combine boolean expressions with `AND, OR, NOT`



