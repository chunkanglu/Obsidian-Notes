```sql
SELECT sID, instructor
FROM Student NATURAL JOIN Took NATURAL JOIN Offering
WHERE grade > 50;
```
> **NOTE:** don't use natural join in SQL, better to be explicit

## Dangling Tuples
- When outer joins have tuples without match, they are included but with non-matching values padded with NULL.
- Inner join does not give these tuples at all

## Outer Joins
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL OUTER JOIN