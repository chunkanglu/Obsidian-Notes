- Comparing string to a pattern using `LIKE`
	- `%` is any string
	- `_` is any character
```sql
SELECT *
FROM Course
WHERE name LIKE '%to%'
```

