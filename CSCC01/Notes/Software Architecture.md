# Architectural Structures
- set of elements held by a relation
- 3 categories
	- *Module* - partition system into units or modules (eg. database, UI, etc)
		- static view of how the code is organized
	- *Component-and-connector* - runtime components and communication between them
		- dynamic view of components are runtime
	- *Allocation* - relationship between system and non-software structures
		- how the system is allocated to different aspects (eg. team ownership, hardware allocation)
# Architectural Patterns
- Relationship between context, problem, solution
- Based on quality attributes:
	- *Modifiability* - can it be easily modified or extended without breaking other parts (ie. add feature, fixing bugs, optimize)
		- using suitable design patterns and following design principles like SOLID
	- *Availability* - can the service be always up and resilient to failure
		- have proper error handling covering edge cases, service duplication, database backups
	- *Interoperablity* - is it able to seamlessly work with other systems or components
		- have loose coupling and use conventional interfaces to make things easier
	- *Scalability* - is it able to to handle increased traffic
		- ensure sufficient hardware and service instances when deployed
	- *Reusability* - can components be easily reused
		- make components generic and self-contained as well as use standards and best practices to ensure compatibility
	- *Performance* - can it stay responsive (under scaling workload)
## Layered Pattern
- software divided into layers which contain cohesive set of services
- Used int operating systems & TCP/IP protocol
- 2 types:
	- *Closed architecture* - only next lower layer can be used by some layer
	- *Open architecture* - a layer can use any other service from a lower layer
- **Promotes reusability and modifiability**
	- clear separation of services
> [!warning] Challenges
> - Larger upfront cost & complexity
> - Performance penalty

![[Pasted image 20240309140131.png]]
## Model-View-Controller Pattern
- Goal of keeping UI functionality separate from application functionality whilst being responsive to user input
- Functionality separated into 3 components:
	- *Model* - manages application data (ie. core backend like interacting with DB)
	- *View* - produces representation of model (ie. frontend UI)
		- There can be multiple views for the same model (ie. can represent the same data in different ways)
	- *Controller* - translates user actions into changes to model or view
		- Multiple views may mean multiple controllers
> [!warning] Challenges
> - Increased codebase complexity
> - May not apply to all systems (eg. games or simple applications without much need for user input feedback)

![[Pasted image 20240309140531.png]]
## Pipe-and-Filter Pattern
- For system that transform streams of data from input to output (eg. ETL system)
- Divide filters as loosely coupled, reusable components with generic functionality (filters should work in isolation, without knowing what comes before or after it)
- Data undergoes a series of transformations performed by the filters and connected with pipes
> [!warning] Challenges
> - Not suitable for interactive systems (more for data processing)
> - Computational overhead

![[Pasted image 20240309141004.png]]
## Client-Server Pattern
- For when there are shared resources/services that many clients can use
- Clients request from the (centralized or distributed) server that responds to these requests
- Components may act as both client and server
> [!warning] Challenges
> - Server can be performance bottleneck
> - Single point of failure (if not properly managed with duplication, load balancing)

![[Pasted image 20240309141605.png]]
## Peer-to-Peer (P2P) Pattern
- Client-server but everyone (each a node) is both client and server, interacting with other components directly
- May have specialized *supernodes* that have indexing or routing capabilities
- Decentralized system
- Torrenting
- **Promotes reusability, interoperability, and scalability**
> [!warning] Challenges
> - Need to manage data security and data consistency since nodes can come and go (may be hard to enforce consistency which is why it is usually done for well-defined private groups)
> - No quality of service guarantee since nodes come and go, thus shortest path between nodes and latency may fluctuate

![[Pasted image 20240309142116.png]]
## Microservices
- Application decomposed into small, modular, independent services that are developed and deployed independently
- **Promotes modificability (small individualized services), reusability, interoperability (can use different languages/tools for each), and scalability (each service can be individually scaled)**
- Services communicate between each other using REST APIs with HTTP, gRPC (sync), or a message broker (async)
- *Gateway* between clients and internal services
- Services usually register themselves to a *service registry* to be discovered
	- eg. Kubernetes orchestrating everything as a cluster
> [!warning] Challenges
> - Upfront design and implementation cost
> - Harder to communicate between distributed services (may have more latency too)
> - Integration & End-to-end tests

![[Pasted image 20240309143025.png]]
### REpresentational State Transfer (REST)
- architectural style for designing networked applications
- *Stateless* - each request and response is self-contained (with all information needed for processing) and independent
- Resources (data/services) identified by unique Uniform resource Identifiers (URI) and represented in formats like JSON/XML
	- URL is combination of URI to machine & location of resource (eg. process name / port number) on the machine
### HTTP
- Defines the standard methods for interacting with resources
	- GET, POST, PUT, DELETE
- *Stateless*
- Status codes indicate outcome of request
	- 200 - OK
	- 404 - Not found
	- 500 - Internal server error
