# Getting connection info
```
sudo --login --user=postgres
psql
\c {DATABASE_NAME}
\conninfo
```

# For remote DB
Change password using `\password` when in inside `psql`
# Dropping all Tables
```sql
-- Recreate the schema
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- Restore default permissions
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
```
# Accessing in Docker
Exec in postgres container
`su postgres`
`psql`