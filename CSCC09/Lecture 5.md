# Authentication
- Rainbow table attack, brute force common hashed passwords
- **Salt and Hash**
	- Salt: random string prepended with password and hashed together
		- salt is in plain text, followed by delimiter, then hashed salt+password
- Don't send login info in path or stuff (like query param) that can be logged in backend
	- Putting passwords in thing like HTTPS body is fine, as long as you don't log it
## Auth Scemes
### HTTP Basic Auth
- Add to headers with `Authorization: Basic base64(username + ":" password)`
- `isBasicAuthenticated` Express Middleware
- Easy
- Sends password for every request, and need to compare salt+hash to password
- 401 if not authenticated
#### Cookies
- Populated exclusively throught HTTP responses
	- `Set-Cookie: cookie-key=cookie-value`
- The cookie request header is then auto added to each subsequent request
- backend has decrypted session id which can then be used to identify user
- use `express-session` to encrypt session-id for cookies
	- secret should be in env variable
### Bearer/Access Token
- Cookies are browser specific
- Access tokens are common
- attach access token to HTTPS request headers
	- store in frontend
# Authorization
- What are you accessing? Do you have access?
- 403 if not authorized
## OAuth 2
- authorization via 3rd-parties
- **User** authorizes **Application** to access **Provider's resources** from **provider** on their behalf
- How to
	- Need to register application with provider
		- define `redirect_url` used in Authorization Code Grant Type
		- `scopes` what can this app access
		- Provider returns
			- `app_id`: public
			- `app_secret`: only known to backend to prove identify to 3rd party
- Password Grant Type
	- `Authorization: Basic base64 of (app_id: app_secret)`
	- Should only be used for trusted internal applications as we give the application a password for another provider
- Authorization Code Grant Type
	- user directly input the password to provider
	- **Any 3rd party with a backend should use this**
	- HTTP redirect status code needed when redirecting from 3rd party to `redirect_url`, body includes url
	- Notes: <mark style="background: #FFF3A3A6;">ONE OF THESE IN FINAL</mark>
		- /authorize need app_id to claim what app is wanting access
		- /token needs app_secret to verify it is actually the correct app identity
		- Can only use if you can keep `app_secret` actually a secret in the backend (Does not work if no backend)
- Refresh Token Grant Type
	- access tokens short-lived, usually these grant types give you a (long-lived) refresh token
- Using OAuth for Authentication
	- Assume if user has access to some 3rd party thing, you can assume they are the right person they claim to be