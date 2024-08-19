# Too many users
- Cannot handle enough concurrent requests
- Add more backend replicas with load balancing
- Data must be shared in place common to all replicas (not in memory)
# Not enough memory
- Vertical scaling, but limited by resources of a single VM
- Horizontal Scaling with orchestration like Kubernetes
# Too many DB hits
- Application caching results and only hit DB for cache miss or refresh
- In-memory caching bad
	- uses more memory
	- limited to single instance
- Use Redis (in-memory data structure store, used as distributed, in-memory key-value DB or cache)
	- Atomic operations of SET, GET, INCR
# Long computation
- Example: Same resource not in cache yet, 100 ppl request so all miss and do long computation, then store in cache (lots of wasted computation)
- Cache stampede, under high load and cache miss, all processes try to do expensive computation, leading to cascading failure
- Locking
- Periodic recomputation (cronjob)
## Locks
- Type 1: wait/blocking lock
	- blocks until lock obtained
	- bad since slow and no concurrency
- Type 2: Reject
	- reject if not cannot be obtained
	- lots of failures
- Issues:
	- deadlocks
	- increased code complexity
	- scalability issues like latency and contention for locks
- Deadlocks when 1 request stuck cuz it cannot get lock and other process never unlocks resource
	- eg. 2 processes A, B. A works on x then y, B works on y then x, but stuck in deadlock waiting for each other to finish
- Need to choose right params for locks
	- Time-to-live, before auto unlocking
	- What elements to lock
## Periodic recomputation (cache warming)
- scheduled recompute cache independent from incoming requests
- Issues
	- outdated/stale data
	- does not respond to new data immediately
	- inefficient if data does not change much
## Updating cache
- update both cache (fast retrieval) and persistent storage (main storage) independently on new data
- Issues
	- increased computation if high update frequency
	- cache thrashing, constantly being updated, little time to serve data to cliients
	- cache consistency between processes
# Critical Section
- code that must be executed by 1 thread/process at a time to prevent corruption, race conditions. etc
- includes database transactions, cache updating, concurrent web requests
## Frontend retry requests
- Linear backoff, waits constant time and tries again. 100 users will respectively wait 1, 2, 3, ..., 100 seconds each if 1 sec backoff
- Exponential backoff, spreading it out, but still large clusters of requests
- Exponential backoff with jitter, spread with exponential backoff and randomization to minimize overlap
# 4 Golden Signals of Monitoring
- Good to set alerts for each type
## Errors
- Rate of requests that fail
	- how many users were affected by errors in code
	- why did requests not work as intended
- Inspecting server logs bad
	- separate logs on replicas
	- not parsable if many users
	- logs disappear on server restart
- Catch errors and log stacktrace to error monitoring tool like Sentry
- Alert when high percentage of errors like over 50% over 10 minutes
## Traffic - Requests per second
- Demand put on the system
	- is application reaching breaking point
	- is there enough resources provisionsed to serve all users properly
- Number of requests coming from users vs. how many server can handle
- Stress test server to find breaking point
- Infer number of requests from processing logs with Elastic stack, cloudflare reverse proxy logs, nginx reverse proxy logs
	- rarely use application logs directly as hard to understand individually
$$
\text{Num replicas} = \frac{\text{Find breaking point (for single replica)}}{\text{find peak load of users}} + 2
$$
- 2 extra, 1 for being able to update servers, 1 in-case something goes down
- Alert when sudden increase of traffic or when replica fails
## Latency
- Time needed to serve a request
	- is it serving users in the right amount of time
	- why are requests taking longer/shorter than expected
- latency costs sales and traffic by lowering user experience
- Mean & 95th percentile (worst) both important metrics
- Latency monitoring with Elastic APM, can see what calls take how much time
- Alert when latency abnormally high
## Saturation
- how "full" the system is, emphasizing resources most constrained
	- how many more users can web app take
	- how many hours until disk space is full
- Monitoring with tools like Grafana to observe trends like
	- memory leaks
	- CPU usage
	- Disk trending to full
- Alert when abnormally high usage or when close to saturated