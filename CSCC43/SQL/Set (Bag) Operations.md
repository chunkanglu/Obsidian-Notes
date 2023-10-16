SQL treats tables as **bags**, not sets.
- Can have duplicates
- Order does not matter
eg. {6, 2, 2, 7, 1, 9}

### Syntax
```sql
(subquery) UNION (subquery)
(subquery) INTERSECT (subquery)
(subquery) EXCEPT (subquery)
```
- Must be queries and not tables as parameters

### Examples
```sql
(SELECT sid)
 FROM Took
 WHERE grade > 95)
UNION
(SELECT sid
 FROM Took
 WHERE grade < 50)
```

- UNION ALL keeps duplicates