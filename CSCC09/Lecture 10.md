# Event Loop

# Web Workers
- Web workers to separate things into separate threads to not freeze UI
	- but there is overhead to communicate with worker
	- no access to dom

# Progressive Web Applications
- powered by service workers
- allows for offline access for local interaction & usage
- allows for local notifications
## Service Workers
- intercept network requests and caching data locally
- background fetching in a separate thread
## Push API
- Browser Vendor Push Server is the one actually sending the notification, not something locally
- 