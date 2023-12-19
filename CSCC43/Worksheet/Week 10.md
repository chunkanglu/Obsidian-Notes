# Part 1
## Q1
a. Department
b. Name and City from Branch
c. No, has exactly 1 manager
d. Either 0 or 1
e. 1-to-1: Mangement; 1-to-many: Composition; many-to-many: Participation
f. Ternary: None; Recursive: None
## Q2
$Project(\underline{Name}, Budget, ReleaseDate$
$Employee(\underline{Code}, Surname, Salary, Age)$
$Department(\underline{Name, City}, Phone)$
$Branch(\underline{City}, Number, Street, PostCode)$
$Participation(\underline{Name, Code}, StartDate)$
$Membership(\underline{Code, Name, City}, StartDate)$
$Management(\underline{Code, Name, City})$
$Composition(\underline{Name, City})$

$Department(City) \subseteq Branch(City)$
$Participation(Name) \subseteq Project(Name)$
$Participation(Code) \subseteq Employee(Code)$
$Membership(Code) \subseteq Employee(Code)$
$Membership(Name) \subseteq Department(Name)$
$Membership(City) \subseteq Department(City)$
$Management(Code) \subseteq Employee(Code)$
$Management(Name) \subseteq Department(Name)$
$Management(City) \subseteq Department(City)$
$Composition(Name) \subseteq Department(Name)$
$Composition(City) \subseteq Department(City)$
$Composition(City) \subseteq Branch(City)$

Min-1 Cardinality Constraint:
$Department(Name, City) \subseteq Management(Name, City)$
$Department(Name, City) \subseteq Composition(Name, City)$
$Department(Name, City) \subseteq Membership(Name, City)$
$Branch(City) \subseteq Composition(City)$
$Project(Name) \subseteq Participation(Name)$
## Q3
