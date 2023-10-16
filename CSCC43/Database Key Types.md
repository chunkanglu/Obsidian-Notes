#### Superkey
- A set of attributes that allow us to uniquely identify a particular row
- Any adding additional attributes to a superkey gives a superkey
- Attributes can contain NULL
#### Key (Minimal Superkey / Candidate Key)
- A minimal set of attributes to uniquely identify a particular row
- Subset of Superkeys
- Removing all attributes from a Superkey that are not necessary for unique identification
- Cannot contain NULL
- Every table must have at least 1 Candidate key
#### Primary Key
- 1 of the Candidate keys designated as main key used for operations
#### Alternate Key
- Keys that are Candidate keys but are not the Primary Key
#### Foreign Key
- When an attribute can only take on values specified in some other attribute
- Usually a Primary key in one table and acts as a secondary key in another
	- Used to link/cross-reference data between tables

![[img_key_hierarchy.png]]

Alternate explanations: [[Key - Definition from SO]]