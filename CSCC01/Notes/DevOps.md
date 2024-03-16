# Why
- Low dev and operations communication leads to
	- Deployment failures
	- Increased downtime
	- Blaming
- Little automation leads to
	- needlessly wasted time
	- increased workload
	- increased error rate
# What
- Methodology that combines development and IT operations with the goals of
	- shortening software development life cycle
	- continuous delivery of high-quality software
- Automated CI/CD pipeline is an integral part
- Focus on tools and automation, whereas Agile is just a management process, not mutually exclusive and usually used in conjunction
# CI/CD Cycle
- Plan
- Code
- Build
- Test
- Release
- Deploy
- Operate
- Monitor
# Containerization
- lightweight virtualization system that packages a service and its dependencies into a self-contained, isolated environment
	- isolated in address space, disk usage, and processor usage
- Docker
# Orchestration
- Addresses complexities of deploying and management of large, distributed applications that are made of many containers
- Orchestration tasks
	- service discover
	- health monitoring
	- automated scaling
	- load balancing
- Kubernetes
	- containers in pods
	- namespaces
# DevOps Metrics
- Lead time for changes (time from merge to deployable state, show pipeline efficiency)
- Change failure rate
- Deployment frequency
- Mean time to recovery (time it takes team to fix partial/total failure in prod)
- Build failures
- Error rate
- Throughput
- Latency & Delays