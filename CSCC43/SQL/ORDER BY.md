```sql
SELECT sid, grade
FROM Took
WHERE grade > 90
ORDER BY grade DESC, sid
```
- Defaults ascending, use DESC for descending
- Can order by multiple columns
	- Sorts left to right condition, going right for tiebreaker
- attribute list can include expressions
	- `ORDER BY sales + rentals`