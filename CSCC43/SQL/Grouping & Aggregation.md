- `SUM, AVG, COUNT, MIN, MAX`
- `COUNT(*)`
- Remove duplicates using `DISTINCT`
```sql
SELECT COUNT(DISTINCT sid)
FROM STUDENT
```
- SELECT-FROM-WHERE with group by
```sql
SELECT sid, AVG(grade) AS mean
FROM Took
GROUP BY sid
ORDER BY mean
```
- If aggregation is used, each element in SELECT must be either aggregated or present in the GROUP BY statement