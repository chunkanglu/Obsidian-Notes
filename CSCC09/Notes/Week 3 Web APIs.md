# HTTP
- HTTP protocol
	- For sending and receiving data
- HTTP request
	- Consists of:
		- Request URL
		- Request Method
		- Request Header (metadata)
		- (For some request types) Request Body
	- URL
		- protocol: http / https
		- domain & port
		- url path & url params
		- query params
	- Request Body
		- Standard way to represent complex structured data with string representation
	- Request Header
		- Metadata like MIME type of data sent
		- Agent executing request
		- Cookies
- HTTP response
	- Status code
		- 401 Unauthenticated, 403 Unauthorized
		- Return more detailed info for client requests & just use 500 for server problems to not leak info
	- Response Header
		- metadata like `Content-Type: application/json`
	- Response Body
		- data in the type of `Content-Type`
# REST API
- Representation State Transfer
	- Stateless (each request is independent of each other)
	- Web API Standard
		- Good idea to make things cross compatible instead of each person having proprietary method
- Fullstack apps need basic CRUD actions
	- Create - `POST`
		- Usually no query params
		- Item to be created in body
	- Read - `GET`
		- No body, use url & query params for more info
			- eg. `include=author` to include related models to save API calls & DB hits (related to N+1 problem)
		- Should not have side effects (ie. modify DB)
		- Should return a JSON, instead of just the data so that more metadata can be sent
		- **URL should be PLURAL**
		- Getting a specific item should **only return infor about that item**
	- Update - `PUT` or `PATCH` (usually patch as put means replacing everything)
		- similar to POST
	- Delete  - `DELETE`
		- Similar to GET
		- sometimes include deletion reason via query param
# Frontend API Calls
- Use `fetch`
```js
fetch(someURL, {
	method: 'GET',
	headers: {
		...
	}
}).then((res) => {
	...
});
```
- Usually want loading, empty & error states to inform user