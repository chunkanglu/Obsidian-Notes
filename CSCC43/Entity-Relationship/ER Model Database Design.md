---
tags:
  - CSCC37
---
Logical representation of tables
- Not actual table and values

# Goals
## Phases
1. Get data needs of project and users
2. Choosing a data model (SQL, noSQL)
3. Moving from abstract data model to actual database implementation
	- Logical Design - schema
	- Physical Design - layout of database
- Avoid
	- Redundancy
	- Incompleteness - bad design can make certain aspect impossible to model
## Design Approaches
### Entity Relationship Model
- Models a collection of entities and relationships between entities
- Each entity is distinguishable from other objects and are described by a set of attributes (rectangular box)
- Relationship represented diagrammatically with diagrams (diamond between entities)
#### Entity Sets
- Set of entities of the same type that share the same properties
- Entities represented by set of attributes common in all members of entity set
- Subset of attributes form primary key of entity set
#### Classification of Attributes
##### Simple attribute vs. Composite attribute
- Cannot be divided further (eg. age)
- Can be split into smaller attributes (eg. name can be split into first, middle, last)
- Usually like to be simple
##### Single valued attributes vs. Multi-valued attribute
- Multi - eg. phone number (can have business number, personal number)
- Usually like to be single valued
##### Stored attribute vs. Derived attribute
- Stored - directly stored in database and usually cannot be derived using logic (eg. name of someone)
- Derived - eg. age can be derived with date of birth
##### Complex Attribute
- Both composite and multi-valued
- Addresses (not distinguishing business, home)
- Subjective if this is actually needed
## Relationships
#### Recursive Relationships
- Employee is colleague of another employee
#### Descriptive attributes
- Attributes used on relationships that may not be able to be expressed in entities
- Not stored, but just description of overall logical flow
#### Ternary Relationships
- Most relationships are binary but some can have three
### Constraints
#### Mapping Cardinality
- One-to-One
- One-to-many (eg. one instructor advises many students)
- Many-to-one
- Many-to-many
- The "one" edge in the diagram has an arrow
##### Complex Cardinalities <mark style="background: #FF5582A6;">**ON FINAL**</mark>
- Minimum and maximum cardinality of relation
- One side corresponds to at least and at most some number of instances of the other side (based on assumptions)
- Can be just like (M, N), (0, N), (1, N) to not need to specify a concrete number
## Total vs. Partial participation
- Total - every entity in E must participate in at least one relationship in R (denoted by double line)
- Partial - some entities do not
## Subclasses in ER
- Specialization of parent class - Subclasses form tree, no multiple inheritance
- **Isa** triangle to indicate subclass
## Keys and Weak Entity Sets
- minimal sets of attributes which uniquely identify instances of an entity set
- internal keys - formed by one or more attributes of entity itself
- Strong entity - can be identified  directly by an attribute (ie. by some id value)
- Weak entity - other entities involved in identification (foreign keys)
- Only root of parent class needs key, subclasses inherit it
### Normalization Theory
- Formalize what designs are bad, and test for them
- How to remove bad decisions
[[Normalization Theory]]

