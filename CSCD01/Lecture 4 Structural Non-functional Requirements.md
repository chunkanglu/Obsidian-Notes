- Code quality of the system, instead of performance ([[CSCD01/Lecture 3|Lecture 3]])
- non-functional requirements have the same weight as functional requirements and may be more in terms of cost and time
- non-functional requirements change per project
# Server Update & Maintenance
## Upgradability
How easy is it to upgrade the system from one version to a more updated one?
- Change DB schema, migration
- Upgrade other things
## Preparing a next release
- Current state: modify the code and roll new version
- Problems
	1. Hard to keep track of versions
	2. Dependents of your code (eg. frontend when backend changes) need to also update (ie. when your API response schema changes)
		- Should try to make upgrades *backward compatible*, so users can continue to use old version after update
### Semantic Versioning
X.Y.Z
- X is Major release, not backwards compatible & resets Y and Z after increment
- Y is Minor release, backwards compatible with substantial new functionality & resets Z to 0 after increment
- Z is Patch release, backwards compatible bug fixes
### Codebase backward compatibility
- Even without API changes, updating the same thing that connects to the same database can still cause issues
	- eg. if different versions are expecting different schemas like deleting column (need proper migration to not have issues)
	- eg. requires database rows that v1 did not have
#### Database Migrations (eg. Alembic, ActiveRecord, ...)
- Migrations take time and script to change schemas and move data around
- New Column
- Data Model Refactor (eg. Normalizing)
- Availability issue due to downtime when transferring data
## Deployment Strategies
- Can swap deployment strategies depending on situation
### Recreate Deployment strategy
1. Package new version of app
2. Shut down old versions
3. Spin up new versions
- Do while offline:
	- Serve maintenance page
	- Data migrations
	- Schema changes
- Pros:
	- This is fast, easy, little overhead but sacrifices availability
- Cons:
	- Hard to rollback
### Ramped deployment strategy
1. Package new version of app
2. Shut down one old replica
3. Spin up one new replica
4. Repeat until all versions rolled out & replicas replaced
- No downtime
- All automatically done
- Serves new and old versions concurrently until all versions rolled out
- Requires additional work to manage backwards compatibility
	- Stuff like adding a new column and old version having issues like null issues
- Pros:
- Cons:
	- Requires backwards compatible changes
	- Harder to rollback
### Canary Deployment strategy
1. Package new version of app
2. Shut down one old replica
3. **MANUALLY** spin up one new replica
4. Repeat until all versions rolled out & replicas replaced
- Canarying releases
- Observe before rolling out more to check for issues
- Pros:
	- Good for experimental changes to see how userbase reacts
	- Fast rollback
- Cons:
	- Requires backwards compatible changes
### Blue-green (red-black) deployment strategy
1. Package new version of app
2. Spin up all new replicas
3. Load balancer redirect traffic to new version
4. Shutdown all old replicas
- Pros:
	- Instantaneous version switch
	- Easy rollback
- Cons:
	- Requires backwards compatible changes
	- Costly in infra due to needing to double replicas (old & new)
# Configurability & Customizability
- Adapting codebase to multiple clients
## Customizability
- How easy can software behavior be changed through modifying application code?
- By who?
	- Developers
	- DevOps
	- Support
- Modifying code is fast to start, but needs to go through lengthy deployment process
- Customizability through If-else statements
	- But this can lead to many if-else statements for many different implementations of code paths
- When we add customizations in a fast timeline, we sacrifice on maintainability of code
- Keeping up with many changes can get overwhelming when trying to adapt to different clients
## Configurability
- Software behavior can be changed without modifying application code
- Configurable by who:
	- Developers
	- DevOps
	- Support
	- Implementer
	- End-user
	- Each level has increasing difficult of implementing
- Skip lengthy deployment processes
### Configurable widgets through FSM
- Remove code-driven behavior and create our own JSON-based langauge that (renders HTML) modelled finite state machines to determine how the widget works
	- ie. changing states for different implementations
- Need to onboard Support
	- requires education sessions
	- requires validation (to make sure JSON works)
	- tools
- Support can provide it to end-user
	- requires different solution (eg. text boxes and more user friendly options)
	- WYSIWYG - what you see is what you get
	- requires maintained feature documentation, tool dev support
## Configuration vs. Customization
- Both try to change code behaviour based on choices
- The configurable a system is, the less you can customize
	- eg. not adding button to UI, but adding a component which then indirectly adds to UI
	- Higher effort in adding features
	- Regression on all possible configurations
	- Should customizable to configurable instead?
- The more customizable a system is, the less configurable it can become
	- Hardcoded specific options, need to refactor lots to make it configurable
	- Need to make sure all existing clients have the configuration setting (because it was previously auto-done in code)
	- Each path will need to map to a configuration
	- Need a heavy refactor to remove "hardcoded" attributes without functionality changes (seems like work for nothing)
# Security
- Implicit requirement of top priority
- Follow OWASP Top Ten and best practices (eg. when dealing with passwords)
- Should be considered explicitly
	- Drwiven by some other Non-functional requirement
	- Risk evaluation of architecture (eg. app allows for arbitrary code execution)
# Legality
- Regulation govern what you can or cannot do
- eg. for health info PHIPA - Personal Health Information Protection Act
	- auditability of accesses to patient record
	- data residency (where is data located)
	- patient authorization of information sharing (what patient want to share and when)
- eg. financial industry
	- 
- eg. GDPR, privacy regulations, ...
- regular Database audits
- Do not allow unauthorized access
## Time to Market
### Agility - how fast can this be done
- Meeting deadlines
- Want agility for all
- Opinionated web frameworks allows for usually one best way to write code
- Trainability
### Deployability
- Need to be able to create feature and deploy it (eg. backwards compatible)
### Testability
- Has there been enough resources put into test infra
# Maintainability: Tech Choices & Best Practices
- How easy it is for a developer to change behavior of an app
- Maintainability is inversely proportional to lines of code
- Opinionated web frameworks allows for a specific best practice
- Ability to read large code bases
	- Using common terms like factory, strategy, builder, ... so developers should not need to look deeper to understand
	- Enforcing SOLID design in best practices