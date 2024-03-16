# Why Model
- To communicate abstract ideas in a more effective visual manner
- To understand a codebase and its connections
- To improve design and identify problems
# What is UML
- Modelling language
- Provide abstraction for OO design
	- forward design (diagram before code)
	- backward design (diagram after code)
# Types of UML Diagrams
- *Structural*
	- Static view of the system
	- Class diagrams
- *Behavioral*
	- Dynamic view of the system
	- Use Case Diagram, State Diagram
# Class Diagram
- Classes in an OO system & relationships between classes
- 2 types of relationships:
	- *Association*
	- *Generalization*
- Represented by rectangle with class name, attributes, methods with visibility (public +, private -, protected #, package ~)
![[Pasted image 20240309170544.png]]
![[Pasted image 20240309171744.png]]
- An order associated with 1 customer, 1 customer associated with 0 or more orders
## Association Relationship
- *Aggregation*
	- "has" relationship
	- White diamond (A has B in above image)
	- eg. A student is part of a course. If the course disappears, the student does not disappear
- *Composition*
	- strong aggregation ("owns" relationship)
	- Black diamond (A owns B in above image)
	- eg. A tutorial is part of a course. If the course disappears, the tutorial disappears
- *Dependency*
	- "uses" relationship, no explicit connection (this is very general)
	- changing one element **might** lead to changing another
	- Dashed open arrow
### Generalization Relationship
- *Inheritance*
	- "is a"
	- closed arrow
- *Realization / Implementation*
	- "implements ..."
	- Used for *interfaces*
	- dashed closed arrow
# Use Case Diagrams
![[Pasted image 20240309173837.png]]
![[Pasted image 20240309174653.png]]
![[Pasted image 20240309174817.png]]
- UML diagram that mainly consists of use cases and actors (need not be human)
- Models relationships:
	- *Include* - when some behaviour is similar across $\ge 1$ use case
		- In doing $A$, we also do $B$ (A - - $\text{<<include>>}$ - - > B) but $B$ is reused in other parts of the system and never done alone
		- Dashed open arrow with \<\<include\>\> written
	- *Generalization* - when use case is similar to another one, but does more
		- Special type of parent but can add more in any way (pretty much same as inheritance)
		- Closed arrow
	- *Extentd - Generalization with constraints at specific **extension points** in the parent use case
		- Dashed open arrow with \<\<extend\>\> written
# Interaction Diagram
- Captures behaviour of single use case
## Sequence Diagram
- Interactions that happen at runtime
- Creation of object is box
- Dashed lines from each object to show *lifeline*
- Solid boxes (activation box) when object is active
![[Pasted image 20240309181102.png]]
