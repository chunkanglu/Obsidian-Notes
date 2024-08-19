# SQL Injection
- Exploits raw, unsanitized SQL by prematurely exiting check condition
- Backend: `SELECT * FROM users WHERE USERNAME = '${username}' AND PASSWORD = '${password}' LIMIT 1`
- Exploit: `SELECT * FROM users WHERE USERNAME = 'Paco' OR 1=1 --' AND PASSWORD = 'something' LIMIT 1`
- Preventing
	- Escape user input
	- Input validation (ie. type checking)
	- Use ORMs, don't use string interpolation for queries
# NoSQL Injection
- Same idea
- Backend: `db.find({ id: productId });`
- Exploit: `db.find({ id: {“$ne”: -1} });`
	- condition always passes
# Improper Input Validation
- Dumb inputs can break things
- Requests can be manipulated, do not assume
- Preventing
	- Validate inputs in backend
	- Sensitive operations must be handled in backend to prevent tampering
# Broken Access Control
- Unauthorized user access, modify, delete data they shouldn't have access to
- Preventing
	- Always check user authorization in backend for resource, and return 403 if not allowed
# Race Conditions
- Overloading backend with many requests
```
If already upvoted, return 403
Else, upvote, return 200
```
- If a second upvote check passes before first one updates, then 2 upvotes go through
- Preventing
	- Using a lock so only 1 request a time, can use redis to implement lock across multiple processes/workers
# Incomplete If Statement
- Using unexpected input and backend does not have right handling
# Cross Site Request Forgery (CSRF)
- Malicious site exploits existing logged-in session cookie to carry out actions
- Requires Cookie-based session handling & predictable request params to happen
- **Restrictive CORS headers on HTTP responses do not help as CORS only prevents reading data, not writing.** Request still goes through (given hijacked authentication)
- Preventing
	- CSRF Token - unpredictable request param stored in `<meta>` tag under `<head>` in HTTP request header different every time page is served which server validates
	- Partial solution with `SameSite=Strict` cookie flag
		- Prevents auto-sending cookie over cross-origin requests
		- But clicking link from external site (eg. email) to open your site does not send cookies (ie. not auto-logged in)
# Cross Site Scripting (XSS)
- Injecting malicious JS into web app
- Enters through untrusted source web request and included in content user sees without validation
- Preventing
	- Sanitize user input (ensure cannot be interpreted as code)
	- `HttpOnly` cookie flag - document.cookie no longer accessible through Javascript (but this only prevents cookie hijacking)
## Reflected XSS Attack
- Injected script reflected off server in error message, search result, or any response including some or all of input sent to server
- Usually from tricking user into clicking malicious link that runs script in some way
- Browser executes the script as it came from "trusted" server
- Not persistent
`www.thing.com/search?q=<script>bad things here</script>`
## Stored XSS Attack
- Malicious data sent to be stored in DB and later sent in frontend to be inserted into DOM
Using as input `<iframe src=\"javascript:alert(document.cookie)\">`
# Client Code Analysis
- Frontend javascript is visible (albeit usually minified) so important logic should not be here