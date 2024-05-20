- Course is full stack dev
	- frontend, backend, operations (deployment)
	- 25% final req
- Why web
	- easy to maitain, develop
- Outcomes
	- teaches fundamental concepts
- 3 projects
	- microblog guided labs (twitter ish thing)
	- webgallery without guidance for 3 assignments (incremental, 2 weeks each)
	- 9 weeks to build your own web app as team of 3
- Labs
	- if experience in html/css/js skip lab 2, lab 3
	- express: lab 4
- Sample concepts
	- devtools
	- n+1 problem
	- cache stampeding
	- Oauth2
	- TLS termination
	- server driver UI
	- Hacking the web: SQL injection...
	- ...
# Core Principles
- grade working code only
- no rubrics in advance, only high level guidelines
- consistency
	- there will be a CSCC09 style guide
	- linter WIP
# Dev Environment
- Chrome only for marking
- Unix-type system (docker will be used)
- Github pro account
- Encourages Github Copilot
- Editing HTML/css/js
- Node 18+
# Mobile-first HTML/CSS
## Goals
Create page based on design mockup
Follow best practices in structuring HTML/CSS
Make a mobile-first website
Using Chrome Devtools to speed up development
## What is HTML
- content of page
- metadata in `<head>`
- content in `<body>`
## What is CSS
- describes presentation of elements in the HTML
- cascading as more specific CSS rules override less specific ones
### Using \<div\> s
- Flexbox CSS
- Grid CSS
- 12-column layout
	- divide webpage to 12 columns with `display: flex` and `flex-wrap: wrap`
	- you can further divide 12 columns inside an elements
```
.col-2 {
	flex-basis: calc(2 / 12 * 100%)
}
```

- Utility-first CSS frameworks
	- one class per CSS rule essentially
	- try not to have cascading effect

- Mobile first layouts
	- start with CSS media queries
```css
@media (min-width: 320px) {
	.col-sm-1 {
		flex-basis: calc(1/12 * 100%)
	}
}
@media (min-width: 768px) {
	.col-md-1 {
		flex-basis: calc(1/12 * 100%)
	}
}
```