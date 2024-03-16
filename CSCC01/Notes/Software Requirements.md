# Separating Problem and Solution
- Problem statement can be what's discussed about with stakeholders as well as used to guide design choices and test cases
- *Verification* - solution solves stated problem
- *Validation* - problem statement corresponds to needs of stakeholders
# Stakeholders
- not limited to customers
	- users
	- designers
	- project manager
	- marketing
# Identifying Goals
- Why is the system needed
- express as set of specific goals
- iteratively refine goals to arrive at specific requirements
- explicit declaration provides source of truth for conflict resolution
	- can be too rigid in times of change
## Goal Elaboration & Analysis
![[Pasted image 20240309114648.png]]
- Splitting goal into sub-tasks that need to be completed
  ![[Pasted image 20240309114943.png]]
![[Pasted image 20240309115921.png]]
- + goal helps achieve other
- - goal hurts achievement
- ++ makes goal
- -- breaks goal
## Soft Goals
- Qualitative aspects that are non-functional
- These can influence which goals are prioritized
![[Pasted image 20240309115328.png]]
# Requirements to Design
1. What is the problem
	1. Identify the big goal and vision
2. Scope the problem
	1. How much new functionality is needed to complete
3. Idenify solution scenarios
	1. How will users interact with the software 
4. Architecture
	1. How will the functionality be designed/created
# Types of Requirements
- *Functional* - what is directly needed form the system to accomplish the goal
- *Non-functional* - anything else that does not directly affect the correctness of the system (eg. performance, quality of life stuff)
# Actors
## Primary Actors
- Need direct support form the system to do their daily tasks
- Direct interest in the results from the system
## Secondary Actors
- Those that maintain the system
# Personas
- Fictional character representing a user of the system with specific characteristics
	- enhances user centered design
	- gives team a frame of reference for a target audience
# Use Case
- Functional requirement of system between the users and the system
- set of scenarios tied together by common user goal
	- eg. Buy a product: find product, add to cart, checkout, fill payment, system authorizes purchase, system confirms sale
# Use Case Diagram
![[Pasted image 20240309120648.png]]
- Diagram showing interactions between the system, actors (need not be human), and use cases
See more in [[UML#Use Case Diagrams|Use Case Diagrams]]

