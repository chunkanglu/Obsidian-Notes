# HTML
- HTML is content of page
- Metadata in `<head>`
- Content in Body
# CSS
- CSS describes how content looks
	- Cascading Style Sheets
		- Cascading as priority of CSS rules is relative to how specific the rule is
			- ie. id over class, `.btn.btn-blue` over `.btn`
	- Nested Components
		- Direct child: `.container > .container-text`
		- Some descendant: `.container .container.text` 
	- Common question is: **Where is the CSS located?**
	- Can be inline, embedded, or (most commonly) separate file with reference in header
		- `<link rel="stylesheet" type"text/css" href="style.css"/>`
# 12 Column Layout
```css
.row {
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
}

/* 12 grid bootstrap layout */
.col-1 {
  flex-basis: calc(1 / 12 * 100%);
}
.col-auto {
  flex: 1;
}

/* Responsive (desktop first) */
@media (max-width: 576px) {
  .col-sm-1 {
    flex-basis: calc(1 / 12 * 100%);
  }
}

/* Mobile-first */
@media (min-width: 576px) {
  .col-md-1 {
    flex-basis: calc(1 / 12 * 100%);
  }
}
```
sm: '320px',
md: '768px',
lg: '960px',
xl: '1200px',
'2xl': '1536px',