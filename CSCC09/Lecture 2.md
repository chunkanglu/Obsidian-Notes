# Javascript
- first class functions
- Use ES2020 in the class (ES6)
- Optional chaining `if(thing?.attr)` instead of `if (thing && thing.attr)`
- String to int `+ '5'`
- Nullish coalescing
- `===` casts type, usually don't use `==`
# JS in the Browser
- No access to other programs
- cannot execute arbitrary OS commands
- cannot access other tabs
- Can mount & access local filesystem (experimental thing)
- Including JS for C09 Vanilla JS
	- Include as separate file at the end of HTML body
	- `<script src="main.js"/>`
# Document Object Model
- Tree representation of HTML document accessible with JS
- Add, change, remove HTML elements and attributes
- Change CSS styles
- Event listeners
```js
document.querySelector()
document.querySelectorAll()
```
```js
.innerHTML
.attributes
.style // Don't use
.append()
.prepend()
.appendChild() // Last child of the element
.removeChild()
document.createElement()
```
```js
// <button id="b">Thing</button>
document.querySelector("b").addEventListener()
```
- Global variables
	- window
	- history
	- localStorage / sessionStorage
	- document
- `setTimeout`: run after some time
- `setInterval`: run in schedule
# Writing Better Browser JS
- interpreted by browsers in consistent way 
- `"use strict";` at the start of the file
	- force browser to validate JS against standard
	- dynamically raises errors in console for non-compliant things
- All JS files share same execution environment
	- 2 files with the same function name will be a problem
- Closures
	- encapsulate and export namespace
	- each file should we wrapped in a closure
```js
const $ = (function() {
	"use strict";
	let module = {};
	module.get = function() {
		... // some function body
	}
	return module;
})();

(function() {
	"use strict";
	let module = {};
	module.get = function() {
		... // some function body
	}
	return module;
})();
```
- DOM takes time to load
	- HTML, CSS loaded earlier than DOM logic
	- Event listeners may not attach fast enough
	- Triggers once when DOM initialized
```js
// This overrides
window.onload = function() {
	... // Adding event listeners
}

// This appends / adds new event listener
window.addEventListener('DOMContentLoaded', (event) => {})
```
- using `debugger;` in code for debugging & being able to access variables at that time in DevTools console
- Remember don't be able to submit for empty form usually
# Structuring JS Code in Frontend
## Model-VIew-Viewmodel (MVVM)
- View - HTML
- ViewModel - DOM bindings, presentation logic, event listeners
	- query model changes and update view
- Model - business logic & data

- In vanilla JS
	- Model: `api-service.js` frontend API service
	- ViewModel: `index.js` Frontend Controller
	- View: `index.html`
- 
