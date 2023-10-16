## Queries

1. $\pi_{sID}(\sigma_{dept=csc \land cNum=343}(Offerring \bowtie Took))$

2. $\pi_{sID}(\sigma_{dept=csc \land cNum=343 \land grade=A+}(Offerring \bowtie Took))$

3. $\pi_{surName, firstName}(\sigma_{dept=csc \land cNum=343 \land grade=A+}(Offerring \bowtie Took \bowtie Students))$

4. $\pi_{surName, firstName}(\sigma_{breadth \land instructor=Professor Picky \land }(Student \bowtie Took \bowtie Offerring \bowtie Course))$

5. $o80 \cap l50$

	1. $o80 := \pi_{sID}(\sigma_{grade > 80}(Took))$

	1. $l50 := \pi_{sID}(\sigma_{grade < 80}(Took))$

6. $(\pi_{term}(\sigma_{instructor=Pitassi}(Offerring))) \cap (\pi_{term}(\sigma_{instructor=Cook}(Offerring)))$

7. $(\pi_{term}(\sigma_{instructor=Pitassi \land dept=csc \land cNum=363}(Offerring))) \cup (\pi_{term}(\sigma_{instructor=Cook \land dept=csc \land cNum=363}(Offerring)))$
8. $(\pi_{sID}(\sigma_{grade > 85}(Took))) \cup (\pi_{sID}(\sigma_{instructor=Atwood \land grade > 50}(Offerring \bowtie Took))))$

9. $\pi_{term}(Offerring) - \pi_{term}(\sigma_{dept=csc \land cNum=369}(Offerring))$

10. $\pi_{dept, cNum}(Course) - \pi_{dept, cNum}(Offerring)$

11. $\sigma_{sID < sID2 \land oID = oID2}(A \times B)$

	1. $A := \pi_{sID2, oID2, surName2}(\rho_{sID=sID2, oID=oID2, surName=surName2}(Student \bowtie Took))$

	1. $B := \pi_{sID, oID, surName}(Student \bowtie Took)$

Extra:
- sID of Students with highest grade in CSC343 in term 20099
- $M = \Gamma_{grade, max}(\pi_{grade}(\sigma_{dept=csc \land cNum=343 \land term=20099}(Offering \bowtie Took)))$
- $\pi_{sID}(\sigma_{grade=M}(Took))$
- alt (what is intented)
	- $Takers(sID, grade) := \pi_{sID, grade}(\sigma_{dept=csc \land cNum=343 \land term=20099}(Offering \bowtie Took))$ Get all students that took the term (no matter grade)
	- $NotHighest(sID, grade) := \pi_{sID, grade}(\sigma_{T1.sID \ne T2.sID \land T1.grade < T2.grade}(\rho_{T1}(Takers) \times \rho_{T2}(Takers)))$ Get students where there exists some other student's grade who beats it and thus not max grade
	- $ANS := Takers - NotHighest$


12. $\pi_{sID}(\sigma_{sID=sID2 \land oID \ne oID2}(A \times B))$

	1. $A := \rho_{sID=sID2, oID=oID2}(\sigma_{grade=100}(Took))$

	1. $B := \sigma_{grade=100}(Took)$
	- from tut (same as my ans)
		- $\pi_{sID}(\sigma_{T1.sID = T2.sID \land T2.oID \ne T2.oID \land T1.grade=100 \land T2.grade=100}(\rho_{T1}(Took) \times \rho_{T2}(Took)))$


13. 3 times - Q12 ans

14. all sID - at least 3 times

15. $\pi_{dept, cNum}(Offerring \bowtie (\pi_{term}(\sigma_{dept=csc \land cNum=448}(Offerring))))$

16. Below

	1. $GC := \pi_{dept, cNum}(\sigma_{instructor=Gries}(Offering))$ All courses Gries taught

	1. $SAC := \pi_{sID}(Took) \times GC$ if students took all courses

	1. $STC := \pi_{sID, dept, cNum}(Took \bowtie Offering \bowtie GC)$ courses students took that Gries taught

	1. $MC := \pi_{sID}(SAC - STC)$ students missing some courses that Gries taught

	1. $\pi_{sID}(STC) - MC$

  

## Integrity Constraints

1. $\sigma_{cNum=400 \land breadth}(Course) = \emptyset$

2. $(490OFF - 454OFF) \cup (454OFF - 490OFF) = \emptyset$

1. $490OFF := \pi_{term}(\sigma_{cNum=490 \land dept=csc}(Offering))$

1. $454OFF := \pi_{term}(\sigma_{cNum=454 \land dept=csc}(Offering))$