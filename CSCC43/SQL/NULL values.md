Common scenarios:
1. Missing value
2. Inapplicable attribute (N/A)
## Representing Missing Information
- Use a value not in any domain
## Checking for NULL values
IS NULL, IS NOT NULL
```sql
SELECT *
FROM Course
WHERE breadth IS NULL;
```
## Aggregation
- Aggregation **ignores** NULL for stuff like sum, average, max, min
- If there are no non-NULL values, then result of aggregation is NULL
- COUNT(column) excludes NULL, COUNT(\*) includes null

## 3 Valued Logic Surprises
- p and (NOT p) may not be TRUE

## Corner Cases
- `SELECT DISTINCT` - 2 NULL not equal
- `NATURAL JOIN`
- Set Operations

- UNIQUE constraint can have NULL value
	- but Primary Key cannot be NULL
	- But not 2 NULL values (this violates constraint)
		- *This is dependent on the dbms*

