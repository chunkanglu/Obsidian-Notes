## Data, Database, DBMS
Database management system creates, manipulate, and retrieve large amounts of data efficiently in a database over long periods of time.
- Data retention policy of 7 to 10 years usually
- Temporal databases are used to archive historical data

## Data Models
- Used to represent structure of data in database
- 2 main types:
	- Entity relationship model (Diagrammatic representation)
	- Relational Model (collection of tables)
- Other models:
	- Semi structured
	- Unstructured
	- Graph data model

> Terminology:
> - Table/Relation
> - Row/Record
> - Column/Field

## DBMS
- Provides
	- Ability to specify structure of data (schema) and enforce it
	- Ability to query or modify data
	- High performance for big data and complex queries
	- Durability of data (stability from corruption)
	- Concurrent access between multiple users
	- Security
	- Versioning
#### Architecture of Relational DBMS
- Client-server model between data and users or applications
- Parsing queries
- Fundamental operation

## Relational Model
> **Domain:** all unique values of an attribute/field/column
> Cardinality of a relation: 

![[img_table_vocab.png]]
#### Domain
- Set (or range) of allowed values of an attribute/column
- NULL is in every domain implicitly to show DNE or not applicable
	- Eg. For storing first, middle, last names, most will have NULL for middle name

#### Schema
- Structure of table
- **Relation instances:** values in the table over the schema

#### Changes in a Database
- Instances/data constantly change
	- Store current version of data
- Schema (should) rarely change
#### Constraints
- Domain Constraint
	- attribute can only take values in domain
	- each data point must be atomic and have flat-file structure (singular values instead of composite attributes or structures)
		- You can't store something like a list or another table
- Key Constraint
	- No 2 tuples/rows should have the same value for all attributes (ie. no duplicates)
- Domain Integrity Constraint
- Referential Integrity Constraint
	- domain of reference key is subset of domain of primary key

## [[Database Key Types]]





