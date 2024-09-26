# Hi students

### check this out!!
```sql
create index idx_developer_id on developer_companies(developer_id)
```

```sql
explain analyze select * from ...
```

#### group by count of quote only when the 
#### results of the group by is greater than 1

```sql
select d.language, count(q.quote) from developer d
inner join quote q on q.developer_id = d.id
group by d.language having count(q.quote) > 1
```

### subqueries

```sql
select d.fullname, q.quote from developer d
    inner join quote q on d.id = q.developer_id
    where length(q.quote) = (
    select max(length(quote)) from quote
)

```