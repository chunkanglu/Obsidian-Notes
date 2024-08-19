# JS Event Loop
- JS single threaded
- long running tasks on frontend will block
- Parts
	- Stack - executing code
	- Task queue, for setTimeout, setInterval, etc
	- Microtask Queue, for evaluating promises
	- IO Loop, for network requests
	- Heap, used to store objects
- Event Loop
	- Evaluate script (synchronous stuff)
	- Process all microtasks
	- Processes next task
	- Process all microtasks
	- Repeat
# Web Workers
- enables multi-threading with background threads
```
worker.postMessage(payload)
worker.onMessage
```
- No access to DOM and document variable
- must be served in the same domain for security
- limited browser APIs available, but has special ones Push API, Servic e Worker, WebGPU
- Same communication method as in iFrame communication and Chrome extension message passing
# Progressive Web Apps (PWA)
- Make web apps look native, work offline, working notifications
- Powered by Service Workers
	- Can intercept network requests (cache information locally)
	- Background fetching (download media)
	- Push API to send info from server to client, like notifications
## Push API
1. Obtain permission from end user
2. End user give authorization through token/endpoint/ VAPID key
3. Can use key and push info to send notifications to end user
- Sent through push endpoint to Browser Vendor Push Server (dependent on browser)
# Testing
- 3 Levels
	- Integration testing
	- e2e
	- system
- Using automated tests enforced in CI pipelines like Github Actions to auto-run after push to PR
## Integration Testing
- modules tested as a group
- Manually: Postman, with logging on frontend and backend
- Automated: Testing framework (mocha) with assertion library (chai)
- Create new DB for testing
## e2e Testing
- Simulate how real users use app
- Manually: Click same sequence of buttons until it works
- Automated: Cypress, Selenium
## System Testing
- Going onto deployed instance and monkey testing
- Should set up QA/dev environment which is replica of prod
