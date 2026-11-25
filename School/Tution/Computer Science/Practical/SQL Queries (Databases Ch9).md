# SQL Queries (Database) — Chapter 09

## SELECT Query

```sql
-- Syntax
SELECT <column1>, <column2>, <column3>, ...
FROM <tbl_name>;

-- Select every column
SELECT *
FROM city;

-- Select specific columns
SELECT Name, CountryCode, District
FROM city;
```

## WHERE Clause — Conditional Statements

```sql
-- Syntax
SELECT <columns>
FROM <tbl_name>
WHERE <condition>;

-- Example: cities with an ID of 10 or less
SELECT *
FROM city
WHERE ID <= 10;
```
