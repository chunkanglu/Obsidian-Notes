![[Week12_Tutorial.pdf]]
# Q1
## 1
$AB$
## 2
$R_1(BD)$ Key: $B$
$R_2(ABC)$ Key: $AB$
## 3
Already 3NF
# Q2
## 1
orderid
Non-prime attributes: date, customer, customeremail
## 2
Already 2NF, no parts of key
## 3
$R_1(customer, customeremail)$ Key: customer
$R_2(orderid, date, customer)$ Key: orderid
# Q3
## 1
StuID StuCourse
Non-prime: StuBranchg, BranchNumber, StuCourseNo
## 2
Not 2NF
$R_1(StuID, StuBranch)$ Key: StuID
$R_2(StuID, StuCourse)$ Key: StuID StuCourse
$R_3(StuCourse, BranchNumber, StuCourseNo)$ Key: StuCourse
Now in 3NF
## 3
Already BCNF