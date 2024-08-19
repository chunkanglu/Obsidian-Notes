- await makes promise synchronous instead of async, which makes sense for backend as you can hang until you have a good value
- whereas frontend you never want to hang and instead want a callback
# MVC
Model each has DB table
View to serve HTML
Controller to link model and view with backend by accepting HTTPS requests and send commands to Model

# ORM - Sequelize
Active record pattern

# N+1 problem
Querying all rows, then for each row we are hitting the DB again
- Also happens for API calls
## Solution 1 - Joins
Join to get all info, then return at once for just 1 DB call
## Solution 2 - Batching Queries
- useful for DBs without joins
- **DEFINITELY IN FINAL**
- get items from first model, then do a single call for the other info

# API Pagination
- Can separate into pages and then with a limit
	- return object with more info like next page url, and total count
- If very little data or need to generate aggregate info, no pagination good
## Offset-limit Pagination
- pages and limit
- `ORDER BY created_at OFFSET 10 LIMIT 10`
- offset is not optimized as above actually limit 20 then ignores first 10
- may not work if new data comes in
## In-memory Backend pagination
- retrieve collection in backend memory but serve pagination to frontend
- big memory usage in server
## Cursor based pagination
- treats DB as doubly linked-list
- returns pointer to previous / next record not on current page
- requires a sequential column like `id` for consistent ordering
	- could be timestamp
# Uploading and serving files
`Content-Type: multipart/form-data`
- Don't base64 encode file content and send as json
- store user-uploaded file content separately from static content
- limit / validate files in frontend and backend
	- maybe also through security scan on prod
## MIME type
- browsers use MIME type to determine filetype
- `multer` library
## Returning images
return correct content type header
- set content type to mimetype