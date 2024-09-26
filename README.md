# Hi students

## fetch one

```python
from config.base import session_factory
from sqlalchemy import text
from model import User

with session_factory() as session:
    selection_result = session.execute(text("select * from users where id = :id"), {"id": 1})
    user_dict = selection_result.fetchone()
    user = User(
        id=user_dict["id"],
        name=user_dict["name"],
        email=user_dict["email"],
        phone=user_dict["phone"]
    )
```

## fetch all
```python
from config.base import session_factory
from sqlalchemy import text
from model import User

with session_factory() as session:
    selection_result = session.execute(text("select * from users"), {})
    users_dict = selection_result.fetchall()
    users = [
        User(
            id=user[0],
            name=user[1],
            email=user[2],
            phone=user[3]
        )
        for user in users_dict
    ]
```

## fetch many ( limit size )

```python
from config.base import session_factory
from sqlalchemy import text
from model import User

with session_factory() as session:
    selection_result = session.execute(text("select * from users"), {})
    users_dict = selection_result.fetchmany(2)
    users = [
        User(
            id=user[0],
            name=user[1],
            email=user[2],
            phone=user[3]
        )
        for user in users_dict
    ]
```

## create index

```python
from config.base import session_factory
from sqlalchemy import text
from model import User
with session_factory() as session:
    index_result = session.execute(text("create index if not exists idx_user_name on users(name)"), {})
```

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