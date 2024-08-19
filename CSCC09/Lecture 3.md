- Chrome Devtools related questions from Lecture 2 **ON FINAL**
- CRUD
	- put - replace
	- patch - update
- HTTP
	- Request body
		- only allows strings, use JSON to represent complex data structures
		- Should be formatted according to `Content-Type` header
	- Header
		- type of info in request body
		- agent executing request
		- cookies
	- Response Status Code
		- Use the specific one for clients (4XX)
		- Use just 500 for server errors to not expose things

- Get request
	- no request body, but use query params
	- use **plural** for endpoint names
- patch / put
	- usually patch
	- since most of the time you aren't changing everything

- API for UI tools
	- Hoppscotch
	- Thunder Client (VSCode)

JS HTTP API calls
- use `fetch`