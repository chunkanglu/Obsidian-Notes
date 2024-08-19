# Authentication
- Who is trying to access info
- Fail to authenticate, return 401 status
- Account signup/login system for users
- Include username, password, and any other info as needed
## Passwords
- Passwords should not be stored in plain text, or only just hashed
	- rainbow table attack where most common passwords are pre-hashed by some algo and can brute force 
- Salt & Hash
	- `newHash = salt + '$" + hash(salt + password)`
	- rainbow table prevented as hash is different every time for same password string
- Should not be sent to API as query param or in request body as these can be easily read (even with HTTPS)
## HTTP Basic Auth
 - Add to header of each request `Authorization: Basic base64(username + ":" + password)`
 - isBasicAuthenticated Express middlewase available
 - Backend decode and compare with DB data
 - Simple, but still similarly exposed as request body
 - Requires password sent every time (more chances of exposure) and needs to compare with hash every time (not efmmuficient)
## Cookie Based Auth
- Populated through HTTP responses `Set-Cookie: key=value`
- Auto sent for every request to site
- Return encrypted *session cookie* after successful login `SetCookie: session-id=encryptedSessionId`
- On request, backend decrypts and compares with its own list of existing sessions
- `express-session` uses symmetric encryption
	- secret used to encrypt the session cookies should not be leaked, otherwise hackers can decrypt and be able to spoof other users
	- loaded as env variable
## Access Token Auth
- Return access token after logging in 
- Client requests must manually include this in the request header like `Authorization: Bearer authToken`
# Authorization
- Limiting user access
- Fail to authorize, return 403
- Backend endpoints referring to authenticated user `/users/me`
- Basic authorization can just be an if statement
## OAuth2
- Authorize application to access 3rd party provider's resources on user's behalf
- Technically not used for authentication, but if we are allowed to access their info, then the user must have provided the right details so we can **assume** they are why they are.
- Dev of app must register app with provider
	- `redirect_url` for Authorization Code Grant Type
	- `scopes` what info app can request/access
- Provider gives app
	- `client_id` to identify app for provider, public
	- `client_secret`, only for app backend
### Password Grant Type
1. After login, post /token backend with `Authorization: Basic base64 of (client_id: clien_secret)`
2. Backend post /oauth/token provider to get access token for user on provider
3. Backend can get provider info on user request
- Should only be used for trusted internal applications as we give username and password to provider on the app as login
 - Need to pass client_id and client_secret so provider can identify it is our app that is performing the action
### Authorization Code Grant Type
1. Backend post to /authorize provider with client_id
	1. Need client_id to identify what app is requesting permission
2. Redirected and user logs into provider, giving consent to app using info
3. Provider accepts and redirects to app `redirect_url` with *Authorization Code* as query param
4. Backend post to /oauth/token provider with client_secret (and included auth code) to get access token
	1. Need client_secret to validate identity of app requesting token

- Users get to input password directly to provider through something the provider provides
	- any 3rd party backend should use this
- App using this grant type must have backend to store `client_secret`
### Refresh Token Grant Type
- Access tokens short-lived, but also provide long-lived `refresh_token`
- Post with same Authorization header and body of `{ "refresh_token": token, "grant_type": "refresh_token" }`
### Scopes
- Restrict what app can do using the granted access token