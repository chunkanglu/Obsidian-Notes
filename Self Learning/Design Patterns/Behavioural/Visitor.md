- Separate algorithms from objects they operate on, being able to add new functionality without modifying the existing classes
- 2 parts
	- Element - objects that have some sort of `accept` method that takes a visitor as argument and allows visitor to perform actions on object (eg. run a method inside the visitor for this type of element)
	- Visitor - has a bunch of methods which correspond to the operations on different types of elements
- Can technically achieve the same result with wrapper type patterns like [[Decorator]], but this allows for all methods under a single class