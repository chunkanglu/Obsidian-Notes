---
tags:
  - CSCC43
---
![[Week 10, Translate ER into DB Schema.pdf]]
# Restructuring an ER model
- Analysis of redundancies
- choosing entity set vs attribute
- limiting use of weak entity sets
- settling on keys
- creating entity sets to replace attributes with
- cardinality greater than one
## Analysis of Redundancies
- Redundances can happen when attributes can be delegated to a superclass (to not repeat same information many times when it could just reference to one item)
## Entity Set vs. Attributes
- Entity set should have at least
	- more than the name of something (> 1 non-key attribute)
	- is the many in many-to-one or many-to-many relationship
- Entity - Thing on its own
- Attribute - Detail about a thing
## Limiting Weak Entities
- Use weak entity when no stronger attribute as a unique ID
- Try to create an ID
## Settling on Keys
- Make sure every entity set has a key
- Attributes with NULL cannot be primary
- Internal keys preferable to external
- Integer keys preferable
- As few attributes as possible
### Avoid Multi Attribute and String Keys
- Wasteful
- Break Encapsulation
- Brittle when more multiple instances
## Attributes with Cardinality > 1
- Relational model doesn't allow multi-values attributes, convert to entity sets
# Translating into Logical Schema from ER
- Good translation should:
	- Not allow redundancy
	- Not allow unnecessary NULL values
## General Idea
- Entity set becomes relation
	- Attributes are attributes of entity set
- Relationship becomes relation
	- Attributes of relationship
	- Keys of connecting entity sets
## Converting Many-to-Many Binary Relationships
![[Pasted image 20231109194703.png]]
```sql
Employee(_Number_, salary, surname)
Project(_code_, Budget, Name)
Participation(_Number, Code_, StartDate)
```
$Participation(Number) \subseteq Employee(Number)$
$Participation(Code) \subseteq Project(Code)$

If we had say another **Number** in another entity that is connected, we would then want to rename to something like **eNumber, projectCode**.
Also note that the key for Participation is *both* Number and Code since you need both to identify an instance.
# Many-to-Many Recursive Relationships
![[Pasted image 20231109195321.png]]
$$
\begin{align}
&Product(\underline{Code}, Name, Cost) \\
&Composition(\underline{Part, Subpart}, Quantity)
\end{align}
$$
# Many-to-Many Ternary Relationship
![[Pasted image 20231109195624.png]]
$$
\begin{align}
&Supplier(\underline{SupplierID}, SupplierName) \\
&Product(\underline{Code}, Type) \\
&Department(\underline{Name}, Telephone) \\
&Supply(\underline{SupplierID, Code, Name}, Quantity) \\
&Supply(SupplierID) \subseteq Supplier(SupplierID) \\
\cdots
\end{align}
$$
# One-to-Many Relationships (Mandatory Participation One Side)
![[Pasted image 20231109195957.png]]
$$
\begin{align}
&Player(\underline{DateOfBirth, Surname}, Position) \\
&Team(\underline{Name}, Town, TeamColours) \\
&Contract(\underline{Surname, DateOfBirth}, Team, Salary)
\end{align}
$$
Don't need Team in Key as always at least 1 team
We can actually put Team name and/or Salary directly into Player.
$$
\begin{align}
&Player(\underline{Surname, DateOfBirth}, Position, TeamName, Salary) \\
&Team(\underline{TeamName}, Town, TeamColours) \\
&Player(TeamName) \subseteq Team(TeamName)
\end{align}
$$
# One-to-One Relationship (Mandatory participation both sides)
![[Pasted image 20231109200745.png]]
$$
\begin{align}

\end{align}
$$
We don't *need* a Management relation, and can move StartDate to Head or Department.
- Theoretically you can combine since it is mandatory from both, but if you cannot guarantee this, then you likely cannot
# One-to-One Relationship (Optional participation for one)
![[Pasted image 20231109201252.png]]
$$
\begin{align}

\end{align}
$$
Can move StartDate to mandatory Department and remove Management.
Since 0 or 1 Employee per Department, we can have Employee number in Department
## Max 1 Constraint


# From Real world to ER Example
We wish to create a database for a company that runs training courses. For this, we must store data about **trainees** and **instructors**. For each course participant (about 5,000 in all), identified by a code, we want to store her social security number, surname, age, sex, place of birth, employer’s name, address and telephone number, previous employers (and periods employed), the courses attended (there are about 200 courses) and the final assessment for each course. We need also to represent the seminars that each participant is attending at present and, for each day, the places and times the classes are held.
Each course has a code and a title and any course can be given any number of times. Each time a particular course is given, we will call it an ‘edition’ of the course. For each edition, we represent the start date, the end date, and the number of participants. If a trainee is self-employed, we need to know her area of expertise, and, if appropriate, her title. For somebody who works for a company, we store the level and position held. For each instructor (about 300), we will show the surname, age, place of birth, the edition of the course taught, those taught in the past and the courses that the tutor is qualified to teach. All the instructors’ telephone numbers are also stored. An instructor can be permanently employed by the training company or freelance

$$
\begin{align}
&Participant(ParticipantCode, SIN, Surname, Age, Sex, PlaceOfBirth, SelfEmployed, EmployerID) \\
&Employer(EmployerID, EmployerName, EmployerAddress, EmployerAddress, EmployerPhone)
&Instructor(InstructorID, Surname, Age, PlaceOfBirth, EditionID) \\
&QualifiedToTeach() \\
&CoursesAttended() \\
&PreviousEmployers(EmployerID, Start, End) \\
&Seminars(SeminarID, ParticipantCode) \\
&Courses(CourseCode, CourseTitle) \\
&Editions(EditionID, CourseCode, eStart, eEnd, numParticipants)
\end{align}
$$