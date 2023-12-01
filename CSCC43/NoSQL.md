- Databases hightly structured
	- know data format in schema
- Plain text unstructured
	- no predefined format
	- self-describing, little external knowledge needed but need to infer what the data means
## Motivation: Avoid RDBMS/SQL Limitation
- Harder to scale
- Joints across multiple nodes hard
- RDBMS handle data growth hard
- Rigid schema design not manageable
- Need for DBA expensive, outdated
## Scaling
- Vertical scaling
	- upgrade to more powerful hardware
	- issues
		- additional investment
		- single point of failure
- Horizontal scaling
	- extra identical boxes
		- network communication
		- workload balancing
		- additional investment
## Network Partition
- distributed structure 
## CAP Theorem
- impossible for distributed data store to simultaneously provide more than two of the three gurantees
	- consistency: every read receives the most recent write or an error
	- availability: every request receives a non-error response - without guarantee that it contains the most recent write
	- partition tolerance: the system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes
- consistency and availability is not a "binary" decision
## ACID vs. BASE
Relational databses
- atomicity: all or none principle
- consistency: databse must be consistenbefore and after transaction
- isolation: each transaction is independent
- durability
NoSQL
- basically available
- soft state
- Eventual consistency
## Pros and Cons
- Cheap, easy to implement
- datae replecated to multiple nodes
- give up on
	- joins
	- ACID transations
	- SQL
	- easy integration with other SQL-based applications