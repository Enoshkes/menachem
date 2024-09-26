from config.base import session_factory
from sqlalchemy import text
from model import User

with session_factory() as session:
    selection_result = session.execute(text("select * from users where id = :id"), {"id": 1})
    user_dict = selection_result.fetchone()
    user = User(name=user_dict["name"])

with session_factory() as session:
    index_result = session.execute(text("create index if not exists idx_user_name on users(name)"), {})