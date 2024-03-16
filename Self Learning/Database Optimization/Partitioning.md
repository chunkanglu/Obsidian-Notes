# What is Partitioning
Dividing a large table into smaller pieces, allowing the DBMS to only need to work on relevant smaller subsets.

One example would be time-series data, where you may only need to look at information from a particular year, and can thus partition by years and disregard irrelevant data.
```sql
CREATE TABLE thing (
	thing_date DATE,
	...
)
PARTITION BY RANGE (YEAR(thing_date)) (
	PARTITION p0 VALUES LESS THAN (2000),
	PARTITION p1 VALUES LESS THAN (2010),
	PARTITION p2 VALUES LESS THAN (MAXVALUE)
);
```