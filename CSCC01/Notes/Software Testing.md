# What
- Running software to detect defects
	- Cannot prove absolute absence of defects
- Can be automated
- Objective evaluation of quality
- Detects complex runtime interaction defects
- **Alternatives:** statis analysis, code reviews
# Testing Levels
- Unit testing
- Integration Testing (between modules)
- System testing (by testers in dev environment)
- Acceptance Testing (done by recruited users in prod-like environment)
# Unit Testing
- Testing individual functions in isolation within a module
# Integration Testing
- Units are tested together
- 2 approaches
	- *Bottom Up* - test in order of topological sort, start with units without dependencies and move upwards
	- *Top down* - Go from most high level down, using stubs for untested units
# Testing Strategies
## Structural Coverage Strategies (White Box Testing)
- Includes
	- Statement Coverage
	- Branch Coverage
	- Def-use Coverage
	- Logic Coverage
- Can quantify the thoroughness of testing (ie. % coverage of code by tests in terms of statements or branches)
- Complex coverage types are more effective at detecting defeats but are more costly to create
	- Achieving full coverage may not be practical/feasible
### Def-use Coverage
$(\text{variable}, \text{definition line}, \text{usage line})$
- Given a test case, testing criteria may include
	- use of every def
	- execute every use
### Logic Coverage 
- *Predicate Coverage* - test set should make each predicate evaluate to true and false
- *Clause Coverage*- test set should make each clause evaluate to true and false
- *Active Clause Coverage* - extra requirement that each clause should determine the predicate (if you flip the clause, then the predicate should flip)
## Function Coverage Strategies (Black Box Testing)
### Use Cases as Tests
- Does it work as expected, not caring about the actual underlying code
	- basic flow
	- alternate flow
	- test postconditions
	- break preconditions
- Good
	- functional acceptance testing
	- manual tests
	- can find many types of defects
		- system errors (eg. memory leaks)
		- performance problems
- Limitations
	- use cases may be ambiguous or out of data
	- inconsistencies between use cases
### Testing with good/bad data
- Bad data
	- Too little/much
	- Wrong type
- Good data
	- normal, expected values
- Using various input values to trigger/test specific conditions
## Stress Testing
### Quick Testing
- quick, cheap tests to try and break the system
	- use inputs to force all error messages
	- overflow buffers
	- force data structure with too many values
	- violate data constraints
	- force large/tiny computation (ie. to introduce round-off or overflow/underflow)
	- weird filesystem conditions
### Interference Testing
- While task running, interfere with it
	- have interrupts (eg. from process signal)
	- change context (eg. changing a setting when an action is performing)
	- cancel a related & needed task
	- overload cpu (or throttle it)
	- put machine to sleep
# When to Stop
## Estimation (eg. Zero-Failure Testing)
![[Pasted image 20240311205545.png]]
## Fault Seeding
- Artificially introduce $N$ faults
- start testing to see how many get found
- Estimate that ratio of seeded faults found is same as non-seeded faults