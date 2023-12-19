---
tags:
  - CSCC43
---
# Data Types
- define type of each attribute (type declarations)
- types can vary between different dbms
- Common types
	- CHAR(n) - fixed lengh n chars, (right/back) padded with blanks if not long enough
	- VARCHAR(n) - variable length up to n chars
	- TEXT - unlimited (not standard but is in Postgresql)
	- INT
	- SMALLINT, BIGINT
	- FLOAT
	- BOOLEAN
	- DATE, TIME, TIMESTAMP
- Types can be more precise
	- eg. Decimal(18, 2)
- Type constraint checked every times a value is assigned the attribute
- Defaults when no value specified
- Single Relation constraints
	- nut null
	- primary key (cannot be null)
	- unique (can be null)
	- check(predicate) generic condition validation
	- Assertions
## User defined types
- Technically subtypes
- These are based on an existing type, but with additional rules
```sql
CREATE domain Grade as INT
	DEFAULT NULL
	CHECK (value >= 0 AND value <= 100)

CREATE domain Campus as VARCHAR(4)
	DEFAULT 'StG'
	CHECK (value in ('StG', 'UTM', 'UTSC'))
```
# Primary Key
## Primary Key Constraints
- is a key (unique)
- not null
- Performance dependent on Primary key and indices
- Every table should have 1 primary key
	- can have 0 but likely cause errors
```sql
CREATE TABLE Thing (
	ID INT PRIMARY KEY,
	name VARCHAR(25)
);

CREATE TABLE Thing (
	ID INT,
	name VARCHAR(25),
	PRIMARY KEY (ID)
);
```
# Unique
## Uniqueness Constraint
- can have more than 1 attribute unique
- can be null
```sql
CREATE TABLE Thing (
	ID INT UNIQUE,
	name VARCHAR(25)
);

CREATE TABLE Thing (
	ID INT,
	name VARCHAR(25),
	UNIQUE (ID)
);
```
## Unique on multiple columns
This
```sql
CREATE TABLE Thing (
	ID INT,
	name VARCHAR(25),
	UNIQUE (ID, name)
);
```
is different from
```sql
CREATE TABLE Thing (
	ID INT,
	name VARCHAR(25),
	UNIQUE (ID),
	UNIQUE(name)
);
```
## NULL in Unique
- Two nulls are **not equal**
```sql
CREATE TABLE test (
	first VARCHAR(25),
	last VARCHAR(25),
	UNIQUE(first, last)
);
```
- Allows two insertions of `(NULL, 'thing')`
# Foreign Key
## Foreign Key Constraint
- Must reference a primary key or *unique* value in another table
```sql
CREATE TABLE Thing (
	email TEXT PRIMARY KEY
	num text REFERENCES OtherTable(Key)
);
```
## Enforcing Constraint
- Reaction policy (constraint violations)
- you get to define what the DBMS does
- Deletion can also cause violation (when trying to reference something that is deleted)
- Inserting new key that does not reference anything in other table violates constraints
# Check Constraints
```sql
CREATE domain Grade as SMALLINT
	DEFAULT NULL
	CHECK (value >= 0 AND VALUE <= 100)
```
- Not used much in real word since it is hard to remember what is defined how, and it is inflexible if requirements change over time
- Checked when new tuple is inserted into relation or updated
	- if change somewhere else violates constraint, DBMS will not notice 
## Attribute-based (Column) Check Constraint
- Constraints for a *single* column
- Condition inside `CHECK` can be anything that could go in a `WHERE` clause (even subqueries)
- Only checked when new tuple is inserted or value for that attribute is updated
	- Can silently fail, in below example, if `P` removes some program that is used in Student, check is not run and no error
```sql
CREATE TABLE Student (
	SID INT,
	program VARCHAR(5) CHECK(
		program in (SELECT post FROM P)	
	),
	firstName VARCHAR(15) NOT NULL,
	...
)
```
## Tuple-based (Row) Check Constraint
- Constraints over *multiple* columns
```sql
CREATE TABLE Student(
	sID INT,
	age INT,
	year INT,
	check(year = age - 18)
);
```
- can break if age < 18
- Also only checked when insert or update
## How NULL affects Check Constraint
- NULL *passes* check constraints
![[null_check_constraint.png]]
# Not NULL Constraints
```sql
CREATE TABLE Course (
	cNum INT,
	name VARCHAR(40) NOT NULL,
	dept DEPARTMENT,
	PRIMARY KEY (cNum, dept)
);
```
- many attributes should not be null in practice
- A type of attribute-based constraint
# Naming Constraints
```sql
CREATE domain Grade as SMALLINT
	DEFAULT NULL
	CONSTRAINT gradeInRange
		CHECK (value >= 0 and value <= 100)
```
# Assertions
- Check constraints cannot express constraints across tables
- Schema elements at the top level, can express cross-table constraints
- Probably never used
	- Very costly since it must be *checked every database update*
	- Testing and maintenance difficult
```sql
CREATE ASSERTION <name> CHECK <condition>;
```
# Triggers
- Compromise between Check constraints less power and Assertions
- Cross-table constraints
- Control cost by having control over when they are applied
	- Event - after some database action like delete or before update
	- Condition - boolean expression
	- Action - any SQL statements
- Used for Foreign key constraints
```sql
CREATE TRIGGER some_trigger AFTER INSERT ON some_table
```
# Policies
- `ON DELETE RESTRICT` - rejects the modification, raises error
	- Same as `NO ACTION`, in most DBMS
- `ON DELETE CASCADE` - deletes row in current table and all referencing rows in other tables
- `ON DELETE SET NULL` - referencing rows will still exist but original reference changed to NULL
- `ON UPDATE CASCADE` - also updates when the primary key that is referenced is updated
	- **NOTE: primary key shouldn't be updated (*usually*) in the first place**
```sql
CREATE TABLE Took (
	FOREIGN KEY (sID) references Student
		ON DELETE CASCADE
		ON UPDATE CASCADE,
)
```
# Deleting
- If deleting a tuple violates a foreign key constraint, you will usually get an error
- Usually use some sort of [[#Policies|policy]] to account for this
```sql
DELETE FROM Course
WHERE dept = 'CSC'
```
# Updating Schema
## Alter
```sql
ALTER TABLE Course
	ADD column numSections INT;
```
## Drop
- Remove table and schema whole thing
```sql
DROP TABLE Course
```