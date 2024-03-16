# Template
- Define outline of algorithm, deferring some steps to subclasses
- Algorithm has a main *template* method that runs the other methods that should not be touched and stay the same (as a generic runner)
- Allows subclasses to redefine specific steps with changing overall structure
- Used when there are several classes that contain mostly identical algorithms with minor differences
- Template based on **inheritance** (extension through subclasses), whereas Strategy is based on **composition** (extension by supplying different classes to the main class)
	- Template is static
	- Strategy allows changes at runtime

```java
abstract class Thing {
	abstract type smallerMethod1();
	abstract type smallerMethod2(); 
	...
	public void templateMethod() {
		smallerMethod1();
		...
		smallerMethod2();
	}
}

class ConcreteThing1 extends Thing {
	public ConcreteThing1() {}
	public type smallerMethod1() {
		...
	}
	public type smallerMethod2() {
		...
	}
}
class ConcreteThing2 extends Thing {
	public ConcreteThing2() {}
	public type smallerMethod1() {
		...
	}
	public type smallerMethod2() {
		...
	}
}

public class Main {
	public static void main(String[] args) {
		t = new ConcreteThing1();
		t.templateMethod();
	}
}
```
# Decorator
- Extend functionality by wrapping around existing functionality
- Used when you may want to dynamically add different functionality and creating all combinations if infeasible
```java
abstract class Thing {
	...
	public abstract void doSomething();
}
public class ConcreteThing extends Thing {
	public ConcreteThing(...) {}
	public void doSomething() {
		...
	}
}

abstract class ThingDecorator extends Thing {
	Thing thing;
}
public class ConcreteThingDecorator extends ThingDecorator {
	public ConcreteThingDecorator(Thing thing) {
		this.thing = thing;
	}
	@Override
	public void doSomthing() {
		// Add additional behaviour
		... this.thing.doSomething(); ...
	}
}

public class Main {
	public static void main(String[] args) {
		Thing thing = new ConcreteThing(...);
		thing = new ConcreteThingDeccorator(thing);
	}
}
```
# State
- Allow alteration of behaviour by setting the internal state attribute and then using encapsulation to generically use the same call
- **Appear as if object changed class after a state change**
	- Think finite state machine and how behaviours change depending on the state
- Extract all state-specific behaviour into its own object, then have the main *context* class have an attribute & function to set & store the current state to use
	- The main function that uses these states should be generic and offload implementation to the states
- **States may/are aware of other states and can thus initiate changes to other states**
	- The main class can then initiate these transitions using generic functions (yet again implemented by each state)
```java
abstract class State {
	abstract void changeState();
	abstract void doSomething();
}

class ConcreteState1 {
	private Thing thing;
	public ConcreteState1(Thing thing) {
		this.thing = thing
	}
	public void changeState() {
		this.thing.setState(new ConcreteState2(this.thing));
	}
	public void doSomething() {
		...
	}
}
class ConcreteState2 {
	private Thing thing;
	public ConcreteState2(Thing thing) {
		this.thing = thing
	}
	public void changeState() {
		this.thing.setState(new ConcreteState1(this.thing));
	}
	public void doSomething() {
		...
	}
}

class Thing {
	private State state;
	public Thing() {
		...
	}
	public void setState(State state) {
		this.state = state;
	}
	public void changeState() {
		this.state.changeState();
	}
	public void doSomething() {
		this.state.doSomething();
	}
}

class Main {
	public static void main(String[] args) {
		Thing t = new Thing();
		t.setState(new ConcreteState1(t));
		t.doSomething();
		t.changeState();
		t.doSomething();
	}
}
```
# Composite
- Be able to combine multiple instances of the class together to form as one entity
- Literally like compositing shapes on a page to form a picture
- Compose objects into tree structure and treat these structures as a single object
	- **This pattern only works if you can recursively form objects by combining other objects together**
- **Literally a tree data structure**
```java
abstract class Node {
	abstract void doSomething();
}
class Leaf extends Node {
	public Leaf() {
		...
	}
	public void doSomething()
}
class Composition extends Node {
	private ArrayList<Node> instances;
	public Composition() {
		this.instances = new ArrayList<Node>();
	}
	public void add(Node node) {
		this.instances.add(node);
	}
	public void doSomthting() {
		for (Node i in this.instances) {
			i.doSomething();
		}
	}
}
```
# Command
- Encapsulate actions as an individual object, allowing a class to set which object to use and call the same way
```java
class Reciever {
	public Reciever(...) {
		...
	}
	public void doSomething() {
		...
	}
	public void doOtherSomething() {
		...
	}
}

abstract class Command {
	public abstract void execute();
}
class DoSomethingCommand extends Command {
	Reciever reciever;
	public DoSomethingCommand(Reciever reciever) {
		this.reciever = reciever;
	}
	public void execute() {
		this.reciever.doSomething();
	}
}
class DoOtherSomethingCommand extends Command {
	Reciever reciever;
	public DoOtherSomethingCommand(Reciever reciever) {
		this.reciever = reciever;
	}
	public void execute() {
		this.reciever.doOtherSomething();
	}
}

class Controller {
	Command command;
	public Controller() {}
	public void setCommand(Command command) {
		this.command = command;
	}
	public void go() {
		this.command.execute();
	}
}

class Main {
	public static void main(String[] args) {
		Reciever r = new Reciever(...);
		Controller c = new Controller();
		c.setCommand(new DoSomethingCommand(r));
		c.go();
		c.setCommand(new DoOtherSomethingCommand(r));
		c.go();
	}
}
```
# Iterator
- Provide a way to wrap around an aggregate object for sequential reads without exposing underlying representation
	- eg. you have one thing represented as a linked list, another that is an in-order traversal of a binary tree, but you want a generic interface to iterate over the elements
- Usually implements `next(), hasNext(), done()` of some sort
```java
class Node {
	...
}

abstract class Iterator {
	abstract boolean hasNext();
	abstract Node next();
}
class ListIterator extends Iterator {
	ArrayList<Node> list;
	Node i;
	public ListIterator(ArrayList<Node> list) {
		this.list = list;
	}
	public boolean hasNext() {
		return i.getNext() != null;
	}
	public Node next() {
		if (!hasNext()) {
			throw new Exception();
		}
		i = i.getNext();
		return i;
	}
}
class BSTIterator extends Iterator {
	Stack<Node> stack;
	Tree tree;
	public BSTIterator(Tree tree) {
		this.tree = tree
		this.stack.push(tree.getNode());
	}
	public boolean hasNext() {
		return !stack.isEmpty();
	}
	public Node next() {
		if (!hasNext()) {
			throw new Exception();
		}
		Node i = this.stack.pop()
		for (Node n: i.getChildren()) {
			this.stack.push(n);
		}
		return i;
	}
}

public class Main {
	public static void main(String[] args) {
		BSTIterator b = new BSTIterator(...);
		while (b.hasNext()) {
			... (b.next());
		}
	}
}
```