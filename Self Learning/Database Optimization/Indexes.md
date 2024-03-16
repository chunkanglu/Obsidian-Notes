# Analogy
Suppose you want to find the sections that contain a certain word within a textbook. One option is to flip through every page from start to end and mark each occurrence. A better way is to go to the back and (hopefully) look at the index at the back of the book, find the word you want to look for and look only at the specified page numbers.
# What is an Index
```sql
CREATE INDEX index_name ON table_name(index_cols)
```
It is essentially a way to organize your data to make operations faster.

Imagine you have a table and you want to search for a particular instance of data. If there is no ordering to the data, you are only able to linearly scan through which is inefficient with large amounts of data.
If data was sorted, you could then use binary search for much faster retrieval.

An index comprises of a new ordered data structure alongside the main table which contains:
1. the attribute you want to order by
2. a pointer to the relevant row in the original table

You can link multiple of these data structures to order by and thus index on multiple columns.
# Why a new data structure instead of just reordering the table itself?
1. Ability to index on multiple columns
2. More efficient operations
Consider if you have a lot of attributes in the table. It is far easier to order and manipulate the values of a single column compared to many columns that each can house large amounts of data (like paragraphs of text).
But [[#Cluster vs. Non-Cluster Index|exceptions apply]].
# Some performance stuff
If our query only need to retrieve information that is already in the index, it is extremely quick.
Otherwise, it must then take the time to traverse through the pointer back to the main table to get what we wanted. Clearly this will be much slower as you must jump between data structures.
# Index & Query Expressions
Suppose we have `name` as an existing index.
Consider following query:
```sql
SELECT id, name FROM employees WHERE name LIKE '%ob%';
```
You may think that this will be fast since `name` is an index, *but* the problem is, we are not able to directly pull from the index as we instead must evaluate the `LIKE '%ob%'` expression across every row.
# Cluster vs. Non-Cluster Index
Cluster indexes sort and store the data rows in the table in the same order as in the index. It determines the physical order of data in a table.
There can only be one clustered index (that can have multiple rows) as you can clearly only sort by *one* thing at a time.
The name of clustering, comes as similar data is physically stored closer together in physical storage.
```sql
CREATE CLUSTERED INDEX indexname ON table_name(index_cols)
```

Useful for columns that can have ranges as it allows for better sequential access where similar values are on the same data page, and fewer pages are fetched.