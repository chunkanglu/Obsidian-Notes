# Operational Non-functional Requirements
- performance of the system
- more non-functional requirements we consider, the higher cost and time
- most important non-functional requirements are unique to each organization based on goal
	- based on data access patterns, user input, business requirements
	- some have more or less considerations
- Requires business input
- Don't make assumptions
## Handling many requests
- Can the server handle $x$ number of requests per second
- Throw more money (everything costs money) but do it in different ways to be cost-effective
### Vertical Scaling
- getting better hardware (cpu, ram, ...)
- straightforward, easier setup
- single point of failure if just one server
### Horizontal Scaling
- getting more server instances
- needs additional component of load balancer to serve as single entrypoint and manage multiple servers
	- also costs overhead (like another server with resources)
	- *Kubernetes*
	- Also hidden overheads
		- maintenance
		- network requests
			- data transfers between servers adds more latency
- Better availability through redundancy
### Load Estimation
- Need to know how many requests we should expect, and when
- Different systems have different load patterns
	- some grow more linearly over time
		- Requires *scalability* - ability for application to respond well to (somewhat consistent) heavy load
	- others can have spikes sometimes and then drop to a more constant load
		- Requires *Elasticity* - ability to scale up with sudden demand
### Tradeoffs
- Infrastructure costs
- Have to consider **making decisions on tradeoffs** 
	- We can have many servers on all the time to guarantee high RPS (requests per second), but this is wasting unused capacity most of the time
## Database Bottleneck
- Servers now can handle many more requests but the single database cannot
	- requests get dropped
	- or requests are queued until server can process
## CAP Theorem
- *Consistency* - every read returns the most recent write or an error
	- every node in a distributed cluster will have the same replicated copies of the data
- *Availability* - every request to a non-failing node must result in a response
	- you will always get a response (even when failing nodes exist), but it may not be the latest data
- *Partition Tolerance* - system continues to operate even if some nodes fail or network issues that prevent communication between parts of the system
- You can only guarantee 2 of 3 in any distributed data system (under non-perfect circumstances like with network issues)
### Tradeoffs
1. Consistency & Partition Tolerance
	1. guarantees always correct data even when some nodes fail, but not all requests may go though
	2. used for information sensitive data like ticket booking, stock trading, ... as we can't afford double booking or incorrect transactions
	3. MongoDB, Redis
2. Availability & Partition Tolerance
	1. system is always available but may serve outdated data
	2. Often in social media or content sites like YouTube as lack of availability causes user to shift away from the platform
	3. Cassandra, DynamoDB
3. Consistency & Availability
	1. prioritizes consistent data even if it becomes unavailable
	2. will send either old data or no data at all on network failure
	3. impossible to achieve on distributed system since connections between nodes not guaranteed to result in up-to-date data and uninterrupted service
	4. Monolithic architecture of traditional singular SQL database that blocks so only singular concurrent read/write so everyone sees the same data
	5. MySQL, PostgreSQL
- Consistency & Availability
	- 1 single database
	- trivially gives most recent write as it is the only one writing
	- always give response if non failing
	- If database goes down, the system cannot operate so no partition tolerance
- Source-replica (master-slave) replication for partition tolerance
	- main source database writes to multiple replica databases, so more reading bandwidth
	- If we assume it works perfectly and insertions are almost instant, then we technically can have all 3
		- However if an insert takes like 30 second then we don't have availability
	- Inserting synchronously vs. async change can change if read mid-change can cause issues
		- Waiting until all updates finish (blocking all requests), **gives consistency** but block and can timeout, **not availability**
		- Don't wait until all updates finish, **gives availability**, but **not consistency** (latest read may not be the latest write)
- Sacrificing consistency mean read doesn't always return latest write
	- when you want to guarantee data is not overidden
	- but this could actually make sense (when you will get the right data but may not be immediately)
		- Rendering multiplayer games, like between different frames 
		- UDP, packets can get lost, but if interpretable at the end its fine

# Availability
- When do users need to access app
	- hopefully whenever the user needs it
- Happy path, server is always available
	- But server version updates/maintenance or server failures can always compromise availability
- Server updates inevitable
	- security updates (eg. vulnerable packages, end-of-life programs)
	- infrastructure version updates (eg. in Kubernetes)
	- bugs in application
- *When is a suitable time to take down an application?*
	- Differs between the client perspective and the service perspective
	- Can log usage and do it when its lowest
	- Cost of downtime vs. Cost of upgradability
- *What is path to recovery on server failure?*
	- <mark style="background: #FF5582A6;">IN THE QUIZ</mark>
	- **Site Reliability Engineering by Google**
		- Handling Overload
			- individual tasks should be protected against overload
			- handle degradation seriously to avoid piling up of errors and possibly cascading failure
			- degraded responses
				- responses that are not as accurate or contain less data than normal, but are easier to compute
					- ie. searching over a smaller section, or using local cached copies of data instead of retrieving from full
			- extreme load cases, try to load balance and limit and show errors as last resort
			- enforce per customer limits so only misbehaving customers receive errors
			- backend tasks that check user is out of quota must be fast and lightweight, but isn't always the case for using less resources
				- client-side throttling fixes this by capping outgoing client side requests if a large amount of recent ones are rejected with out of quota errors
				- one form is adaptive throttling
			- requests can also be made associated with one of four possible criticality values and only say reject requests of a certain criticality or below
			- handling actual overload errors
				- large subset of backend tasks are overloaded
					- shouldn't happen if load balancing system is working perfectly
					- requests should not be retried and errors should go to caller
				- small subset of tasks are overloaded
					- usually from imperfections in load balancing
					- retry request immediately possibly with different server that has more spare resources
					- treating retries identical to new tasks allows for organic load balancing as it allows for the task to be tried on a new node
			- deciding to retry or not
				- per-request retry budget (3 attempts then fail to caller)
				- per-client retry budget, client keeps track of requests to retries ratio and only retry if ration is under threshold (10%)
					- little need to retry if only a small subset of tasks overloaded
				- including a counter of number of retries a request has done in metadata
				- forms a tree structure as systems have dependencies and requests should only be retried at the layer immediately above rejection, and then propagate upwards to handle on error
		- Addressing cascading failures
			- failure that grows over time as a result of positive feedback, when portion of system fails, increasing the probability that other portions also fail
				- ie. single replica for a service can fail due to overload, and spreads its load to other replicas which then subsequently also fail
			- Causes
				- Server Overload
					- Most common cause either directly or due to extensions or variations
				- Resource Exhaustion
					- can result in hight latency, more errors, or lower quality results, rendering server less efficient or cause server to crash
					- Can include
						- CPU
						- Memory
						- Threads
						- File descriptors
					- resource dependencies lead to a chain of causes
				- Service Unavailability
					- Snowball effect
					- can fail health checks without crashing which also leads to same results as load balancer will not work as expected
			- Preventing
				- Load test server's capabilities to know limit beforehand and perform capacity planning
				- Serve degraded results
				- Reject requests when overloaded, fail early and cheaply (load shedding and graceful degradation)
					- load shedding drops some proportion of traffic as server approaches overload
						- per-task throttling based on CPU, memory, queue length
						- changing queuing method from FIFO to LIFO or using controlled delay algorithm to reduce load by removing requests that are unlikely to be worh processing
							- eg. if web search is taking 10 seconds, it is likely the user will refresh and issue new request so old one should be ignored
					- graceful degradation takes load shedding further by reducing amount of work performed by decreasing quality of responses (see *degraded responses*)
					- Need to determine which and when to kick in and at what layers in the stack (eg. is it needed in all layers or just at some choke point)
				- Have higher level systems reject requests
					- at reverse proxies (ie. by some criteria like IP address to mitigate DOS attacks)
					- at load balancers to either be indiscriminate for all users or selective
					- at individual tasks to prevent random fluctuations in load balancing from overwhelming server
			- Retries
				- always use randomized exponential backoff
				- limit retries per request
				- maybe have server-wide retry budget (eg. 60 retries per minute), and just fail if over
				- avoid retries at multiple levels as a single request at top layer may produce number of attempts as large as the product of the number of attempts in each layer to the lowest
					- If the database can’t service requests because it’s overloaded, and the backend, frontend, and JavaScript layers all issue 3 retries (4 attempts), then a single user action may create 64 attempts (4^3) on the database. This behavior is undesirable when the database is returning those errors because it’s overloaded.
			- Deadlines
				- define how long a request can wait before frontend give up, limiting time backend consumes frontend resources
				- pick deadline not too long to avoid consuming resources after failure
				- pick deadline not too short can cause more expensive requests to always fail
				- Deadline propagation, set deadline high in stack and each process in the task will have deadline of remaining time after previous task
			- Triggering conditions for cascading failures
				- process death
				- process updates
				- new rollouts
				- organic growth
				- planned changes, drains, outages
				- request profile changes
				- resource limits
			- Testing for Cascading failures
				- Test until failure and beyond to know behaviour when overloaded and if it recovers itself
				- test popular (large) clients, and see how internal and external client (services) react
				- Test noncritical backends
					- make sure their unavailability does not interfere with critical components
			- Immediate fixes
				- increase resources, can work if service has not entered a death spiral
				- Stop health check failures/deaths, to not restart unhealthy tasks for more cluster scheduling systems like Borg
				- Restart servers
				- Drop traffic, as final means to address triggering condition, reduce load until crashing stops, and gradually recover load if healthy again
				- enter degraed modes serving degraded results or dropping unimportant traffic
				- eliminate batch load, turning off some less important services
				- eliminate bad traffic, like blocking some heavy load queries
	
- Measuring availability
	- health checks (schedule ping site)
	- response within some time (expecting immediate answer like Google search result)
	- Time Based Availability
		- $availbility = \frac{\text{uptime}}{\text{total time}}$
		- periodic pings
		- Health Check endpoint (if server is healthy)
			- server is responsive to requests
			- dependent API connections work
			- database connection fine with suitable latency
			- cache is warmed
		- Service-Level Agreement (SLA)
			- Monthly downtime allowed: 99% (7h), 99.9% (43m), 99.99% (4m), 99.999% (26s)
			- Each level requires significantly more effort than previous level (much more automation and infra needed)
				- Converting human intervention to automatic recovery
				- Converting user reporting to automated alerting
	- Aggregate Availability
		- $availability = \frac{success}{total}$
		- uptime is request success rate vs. failure rat
		- Even if service is up all the time, there can still be users unable to be served
		- *But where should we calculate this value from in a distributed system?*
			- Done at Load balancer level
			- Not at a server level, if server fails, it still accepts requests
## Increasing Performance
- response time of the request
- Improve
	- data retrieval
		- from where like RAM, hard disk, over network
		- size of input, output
	- compute performance
		- Big-O complexity
- Focus on data retrieval after having (optimal) data structures and code itself at a lower level
### Caching
- Common method to increase data retrieval performance
	- Retrieve from memory instead of disk
	- Perform computation in advance instead of on request
#### Read-through caching
- Data is loaded into cache on demand
- Pros:
	- Only cache what you need
- Cons:
	- Will often have cache misses
	- **Cache stampeding** - too many cache misses at the same time, leading to redundant calculations
```
result = cache[x];
if (!result) {
	result = query something
	cache[x] = result;
}
```
#### Write-through caching
- Add to cache when writing to DB
- ensures cache always up-to-date
- Can write to:
1. Cache then DB
	1. When performance is critical, adding to DB may instead be periodic or less frequent with main place to fetch being cache
2. DB then Cache
	1. This ensures if it fails after the first write, you still have the data
- Pros:
	- Theoretically 0% cache miss (unless cache is full, in which use ways to know what to keep)
- Cons:
	- Could be wasting space in the cache (for things not used often)
```
on_write:
	write to DB
	result = cache[x];
	
```
#### Read-through AND Write-through?
- Possible thing?
- write-through essentially overrides the read-through part, **maybe** unless if write-through part fails somehow (like its full and no proper way to handle well after some sort of clearing)
#### How
- memcached or redis popular stored in RAM instead of hard disk so it is fast
- CAP Theorem still applies (eg. consider if cache goes down)
#### Tradeoffs
- Increase in performance with caching
- Sacrifice
	- code simplicity
	- need extra overhead & cost
	- not all things able to easily map as key-value (for redis like cache systems)
### Size of Input / Output
- smaller size leads to faster transfer message/data
- Compression of web data with gzip, Kafka data with Apache Avro
	- lossy vs. lossless compression
- But decompression takes resources
	- Is it faster than just transferring the raw data?

# Takeaways
1. Don't try to consider everything
	1. Since its usually not possible
	2. Only do if necessary
	3. **Users will want everything, but what do they actually need?**
2. Evaluating tradeoffs
	1. Cost, performance, availability
	2. Don't make assumptions
	3. Make tradeoffs backed by outside data (like clients, statistics) and not intuition/past experience