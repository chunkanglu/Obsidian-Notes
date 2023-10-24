---
tags:
  - CSCC43
---
# Q1
```sql
ALTER TABLE teaches ADD FOREIGN KEY (id) REFERENCES instructor(id) ON DELETE CASCADE;
```
# Q2
```sql
ALTER TABLE course ADD COLUMN description VARCHAR(100);
```
# Q3
```sql
ALTER TABLE prereq ADD FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE 
```
# Q4 TODO
```sql
CREATE TRIGGER fail AFTER INSERT ON takes
```