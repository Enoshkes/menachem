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
    s = 7
# with session_factory() as session:
#     index_result = session.execute(text("create index if not exists idx_user_name on users(name)"), {})