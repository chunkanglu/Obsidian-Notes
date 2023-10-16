`HAVING` lets you filter groups
```sql
...
GROUP BY attributes
HAVING condition
```
- `HAVING` must refer to attributes that are either aggregated or in the [[Grouping & Aggregation|GROUP BY]] list
### Example
```sql
SELECT oid, AVG(grade), COUNT(*)
FROM Took
GROUP BY oid
HAVING COUNT(*) > 1
```
```sql
SELECT oid, AVG(grade), COUNT(*)
FROM Took
GROUP BY oid,
HAVING MIN(grade) > 50
```