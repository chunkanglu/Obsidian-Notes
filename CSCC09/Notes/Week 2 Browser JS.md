# Javascript
- dynamic, weak typed, first class functions
- can be included inline, embedded, or separate file (at end of `<body>`)
	- `<script src="js/main.js"/>`
# DOM
- Document Object Model
- Tree representation of HTML doc accessible via javascript
- Access nodes with `document.querySelector(".thing");` and `document.querySelectorAll(".thing");`
	- Note `document.querySelector(".dropdown .dropdown-item");` fails as there may be more than 1 instance that it matches with
- Other functions
	- `x.append(ele); x.prepend(ele);`
	- `x.appendChild(ele);`
	- `document.createElement('div');`
- Event Listeners
```js
document.querySelector("#thing").addEventListener("click", () => { console.log("thing") });
```
- `setTimeout()`, `setInterval()`
# Better JS
- `use strict;` to force browser to validate JS against standards
- Avoid scoping issues (from no namespaces) with closures
```js
// module.js
const module = (function() {
	"use strict";
	let module = {};
	function privateThing() { ... }
	module.thing = function() { ... }
	return module
}());

// index.js
(function() {
	"use strict";
	module.thing()
}());
```
- Only attach event listeners after DOM loaded
```js
window.onload = function() {
// Overrides existing window.onload
}

window.addEventListener('DOMContentLoaded', (event) => {
// Adds stuff to run when DOM loaded without override
})
```
- State management modules & using localStorage to write to & load from localStorage
# Debugging Javascript
- Using Devtools console
- Using `debugger;` in code
# Frontend Structure MVVM
- Model-View-ViewModel
	- Model: API service 
	- ViewModel: Main controller file (`index.js)
	- View: HTML file
	- View should not know nor interact with Model, that is ViewModel's job
# JSON
- Used for storing JS stuff as plain text for placing in stuff like localStorage
- `JSON.stringify(obj)` and `JSON.parse(string)`