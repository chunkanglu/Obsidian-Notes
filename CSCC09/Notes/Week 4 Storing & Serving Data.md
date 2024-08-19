# Backend
- Part of MVC
- Persistent storage with a database
- SQL abstraction with ORMs
- Getting from DB is async (can block if use await)
# N+1 Problem Fixes
- When query once, then query again for each result of first query
- Time complexity scales with number of results returned
- Also an issue for API calls but resolving these is dependent on if API infra supports it
- Solution 1: joins to get all data needed at once
- Solution 2: Batching queries
	- When joins not possible (or not feasible)
	- Query multiple at once as a group `WHERE id IN (1, 2, 3)` instead of single elements `WHERE id = 1`
# Pagination
- Splitting into multiple pages instead of getting all at once 
- No pagination
	- fast as everything is in memory, but consumes large amounts of memory
	- no pagination if we know amount of data is limited (or bounded by small number) or **need aggregate data** (mean, median, ...)
- Backend in-memory pagination
	- Retrieve all in backend but serve paginated version in frontend
	- Good if no easily available pagination method
	- lots of memory used in backend
## Offset Limit
- page & limit
- offset $=$ page $\times$ limit
- Good when data does not change
- Bad when data frequently changes & `OFFSET` in SQL is not optimized
	- Each page has 3 elements, load first page. 3 new elements added. Going to page 2 shows the same 3 elements.
## Cursor-based
- Have a previous and next pointer returned with data
- Requires some form of sequential ordering with ids or timestamp
- More overhead, but can correctly deal with changing data
# Files & Uploads
- `Content-Type: multipart/formdata` for non-strings in request body
- Needs `<input type="file" />` form input to upload from client
- Backend gets:
	- File content
	- Metadata: filename, content type, size, path
- Sending files from backend, browsers use MIME type to determine file type through response header `Content-Type`
- Security
	- Uploaded files should be stored separately
	- Files should not be trusted
		- restrict file upload type
		- restrict browser file select type
		- Run through security scan