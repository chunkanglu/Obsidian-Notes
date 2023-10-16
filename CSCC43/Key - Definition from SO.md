https://stackoverflow.com/questions/6951052/differences-between-key-superkey-minimal-superkey-candidate-key-and-primary-k

**Key** A key is a single or combination of multiple fields. Its purpose is to access or retrieve data rows from table according to the requirement. The keys are defined in tables to access or sequence the stored data quickly and smoothly. They are also used to create links between different tables.

**Types of Keys**

**Primary Key** The attribute or combination of attributes that uniquely identifies a row or record in a relation is known as primary key.

**Secondary key** A field or combination of fields that is basis for retrieval is known as secondary key. Secondary key is a non-unique field. One secondary key value may refer to many records.

**Candidate Key or Alternate key** A relation can have only one primary key. It may contain many fields or combination of fields that can be used as primary key. One field or combination of fields is used as primary key. The fields or combination of fields that are not used as primary key are known as candidate key or alternate key.

**Composite key or concatenate key** A primary key that consists of two or more attributes is known as composite key.

**Sort Or control key** A field or combination of fields that is used to physically sequence the stored data called sort key. It is also known s control key.

A **superkey** is a combination of attributes that can be uniquely used to identify a database record. A table might have many superkeys. Candidate keys are a special subset of superkeys that do not have any extraneous information in them.

**Example for super key**: Imagine a table with the fields `<Name>`, `<Age>`, `<SSN>` and `<Phone Extension>`. This table has many possible superkeys. Three of these are `<SSN>`, `<Phone Extension, Name>` and `<SSN, Name>`. Of those listed, only `<SSN>` is a candidate key, as the others contain information not necessary to uniquely identify records.

**Foreign Key** A foreign key is an attribute or combination of attribute in a relation whose value match a primary key in another relation. The table in which foreign key is created is called as dependent table. The table to which foreign key is refers is known as parent table.