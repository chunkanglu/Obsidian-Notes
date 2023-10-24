# Schema 1
## Q1
$\sigma_{tamount > 5000}{(Orders)}$
## Q2
$$
\pi_{cid}{(\sigma_{first\_name = 'Alex' \lor first\_name = 'Emma'}{(Customers)})}
$$
## Q3
$$
\pi_{first\_name, last\_name}(\sigma_{pname = 'Cakes'}(Customers \bowtie_{cid} Orders \bowtie_{pid} Products))
$$
## Q4
$\pi_{cid}(Orders)$
## Q5
$\pi_{pname}(\sigma_{category = 'baby needs' \land tamount >= 100}(Orders \bowtie_{pid} Products))$
## Q6
$\pi_{pid}(\sigma_{quantity = 0}(Products))$
## Q7
$\Gamma_{first\_name, last\_name, count(oid)}(Customers \bowtie Orders)$
## Q8
$\sigma_{sum(tamount) > 500}(\Gamma_{first\_name, last\_name, sum(tamount)}(Customers \bowtie Orders))$
# Schema 2
## Q1
$\pi_{bid}(Books) - \pi_{bid}(BorrowedBooks)$
## Q2
$BorrowedABook(mid) := \pi_{mid}(BorrowedBooks)$
$IsMember(mid) := \pi_{mid}(Members)$
$Output := \pi_{first\_name, last\_name}(Members \bowtie (BorrowedABook \cup IsMember))$
## Q3
$Bef2000(mid) := \pi_{mid}(\sigma_{publish\_year < 2000}(Books \bowtie BorrowedBooks))$
$After2015(mid) := \pi_{mid}(\sigma_{publish\_year > 2015}(Books \bowtie BorrowedBooks))$
$Output := \pi_{first\_name, last\_name}(Members \bowtie (Bef2000 \cap After2015))$