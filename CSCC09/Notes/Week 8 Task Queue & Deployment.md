# Long Running Tasks
- Comuptationally heavy or needing to make many API calls for single outupt (eg. needing to get data from multiple pages)
- HTTP doesn't allow aborting request once sent from client
- If synchronous and user terminates, backend will keep running task and block for other uses
- If async, request can be immediately acknowledged with 202 status, then server sent events (like result) or store in DB
- Task queue is async worker that performs the tasks
# Deployment
- Need
	- Domain name
	- VM
	- TLS certificate for HTTPS
## Domain name
- Managed by ICANN (Internet Corporation for Assigned Names and Numbers)
- Domain Name Registrars to register domain name
- DNS - Domain Name System
	- points domain names to IP addresses
	- **A record** - point to IP
	- **CNAME record** - point to another domain (that eventually does to A record)
## Virtual Machine
- Many Providers
- Selecting VM specs (RAM, disk, CPU, GPU, bandwidth) dependent on system
## HTTPS
- HTTP default port 80, HTTPS 443
- HTTP lacks
	- confidentiality - easily monitorable
	- authenticity - easily impersonatable
	- integrity - easily modifiable
- HTTPS helps with:
	- confidentiality - uses asymmetric encryption using TLS certificate to establish connection that hides request data
	- authenticity - TLS certificate must be signed by trusted authority (letsEntrypt, Google, Amazon) stored in browser or OS
		- ensure not compromised certificate
	- integrity - compare hashed certificate contents encrypted with private key then decrypted with public key and just hashed contents
		- ensure certificate not tampered
## Deployment Setup
- Reverse proxy (NGINX) to split HTTP requests to web application and API
	- also for TLS termination, decrypts request, fowards to API, receive response, and sends encrypted version
- Need to allow CORS on server so client can access it `Access-Control-Allow-Origin: client-domain`
	- Otherwise CORS protection disallow Javascript from reading response
	- But request does go through to server
## Docker
- Containerize and isolate applications to be run on different environments
- docker compose lets you run multiple containers together with links