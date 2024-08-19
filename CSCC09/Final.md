# Frontend
- 12 column layout
	- display flex + utility classes for num cols to fill
- How css selecctor works
- What chrome devtools does
- Javascript global scoping + using closures
- window.onload, load js after page is loaded
- vulnerabilities
	- CSRF
		- malicious site hijacks requests from user and sends requests to targeted site
		- happens because of session cookies automatically sent by browser
		- protections: using token based auth, same-site=strict flag, **csrf token**
		- cors governs if js can read response of http api request
			- strict cors policy does not stop csrf as it does not prevent making the request in the first place even if you can't read it
	- DOM & stored XSS attacks
		- little bobby tables
	- client code analysis
		- frontend code is visible to users to be reverse engineered
		- don't put secrets

Event loop question:
- if there are multiple setTimeouts, and there is a long running task first, it will block and not decrement the timer
```js
setTimeout(function a () {}, 1000)
setTimeout(function b () {}, 500)
setTimeout(function c () {}, 0)
function d () {
	for (let i = 0; i < 1000000000; i++) {}
}

d()
```
- **NOT**:This will run d, and not enqueue a, b, c to task queue until after it is finished
- Timer keeps ticking but get blocked by single thread
# Backend
- pagination
	- for retrieving multiple items at once without getting all
	- offset-limit
	- cursor-based
		- take 1 more element after/before all the elements you want to actually use as cursors
- express session secret should not be in the source code, should be in environment variable
	- with secret, they can decrypt/encrypt someone's cookie and get their session id to spoof requests
- vulnerabiliities
	- sql/nosql injection
	- imporoper input validation
	- broken access control
	- race condition attack
	- incomplete if statement
	- **bonus question: the in-class bonus to get account for juice shop with client side analysis**
		- https://www.youtube.com/watch?v=pmBJ1ZAlpF8
- cors
- n+1 problem
	- eg. making 1 call to fetch n images and n calls to get comments for images
	- use joins
	- 
- oauth
	- why is it so complicated
	- why can't i directly return access token
		- need to verify it is made by the application
		- need to give client secret
- webhooks
	- schema of webhook is determined by the other party
	- developing webhooks locally by tunneling: ngrok, cloudflare tunnels
# Deployment
- reverse proxy
	- tls termination
	- decrypts https request from user, forwards unencrypted request to api, encrypt http response to user
	- internal use http for convenience
- large scale web apps
	- error monitoring
		- sentry
	- availability monitoring
		- uptime of site
		- locust for traffic stress testing
		- monitor reverse proxy logs
		- elastic stack, datadog, other tech
	- sync, async, task queues
