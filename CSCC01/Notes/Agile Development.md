# What
- Feedback-driven
- divided into iterations usually 1-2 weeks
- output of each iteration (story points completed) is measured and continuously adjusted to accurately estimate and assess work performance
- features are implemented by business value and ensuring quality
# Manifesto
1. **Individuals and interactions** over processes and tools
	1. More important to have competent people working together than to have the greatest tools
2. **Working software** over comprehensive documentation
	1. Prioritize the now in shipping working (but optionally good) code
	2. highest priority is to satisfy the customer with quick and continuous delivery of software
	3. Main point of development is the software
3. **Customer collaboration** over contract negotiation
	1. contract is no substitute for working closely with customers
4. **Responding to change** over following a plan
	1. plans must not be too rigid to accommodate changes in tech, environment, stakeholders
# Circle of Life
- Practice of Extreme programming that Agile has evolved from
## Business Practices
### User Stories
- description of a feature
- these may start out vague and be iteratively be more detailed as things get know, split, merged, or discarded
- assigned a *story point value* to indicate complexity and time needed to complete
	- point value is usually determined with activities that involve the whole team like planning poker
	- story points should be roughly linear
	- a **golden user story** should be used as reference so others can be assigned in relation to this
- INVEST guideline
	- Independent - each story should be separate (except for sub-tasks)
	- Negotiable - should be high-level for stakeholders
	- Valuable - actually have business impact
	- Estimable - be detailed enough to estimate complexity
	- Small - be do-able by 1-2 devs within 1 sprint 
	- Testable - customers should be able to validate correctness
- Automated testing used to determine if story is complete
### Iterations
- Starts with *initial planning meeting* that gathers whole team to discuss overall trajectory of what stories to be completed
- *Velocity* is the number of story points programmers think they can complete
- Stories are prioritized based on Return-on-investment of time
- Mid-point check to assess overall pace and adjust plan
	- should be roughly equal $\frac{velocity}{2}$, if not then adjust accordingly
- QA should begin writing acceptance tests once IPM and communicate with devs
- Iteration ends with a demo of completed stories and ensuring that all tests pass
- *Velocity charts* and *Burn-down charts* are updated for stories that have passed acceptance tests
	- burn-down shows **total story points remaining** and predicts date for next milestone
	- velocity indicates the performance of the team
	- burn-down **does not** correlate with velocity as there can always be adjustments to story point values (eg. modifications, adding/removal of stories)
- Releases should be done often and the whole team should be working together
## Team Practices
### Metaphor
- Team should decide on consistent aspects and create concepts to refer to them uniformly
- *Data Dictionary*
### Sustainable Pace
- A performant dev is a healthy dev
- Should not be overworked or do overtime to maximize consistent performance
### Collective Ownership
- Everybody is responsible for the code
- Should not be the case that one person/team knows everything about one chunk and others have no idea
- Reduces liability and dependence on particular people/teams
- Everybody makes decisions together
### Continuous Integration
- Version control
- Automated test, build and deployment
## Technical Practices
### Test-Driven Development
1. Write tests before the code that is needed to pass the test
2. Tests should be minimal and specific to what is needed to pass
3. Code should be minimal and only sufficient to pass the failing test
### Refactoring
- Improving structure of code without altering behaviour
- Connected with TDD in *Red-Green-Refactor*
	- Create test that fails
	- Make test pass by writing code
	- Refactor code
	- Repeat
### Simple Design
- Writing only the code that is required and is the smallest but most expressive
- DRY - Don't repeat yourself
- Remove duplication and decrease the number of elements (classes, variables)
### Pairing
- 2 people working together on the same problem
	- 3 or more is *mob programming*
- Promotes knowledge sharing and is more code review
- Not scheduled but spontaneous depending on the situation at hand