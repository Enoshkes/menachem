from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import User


def find_user_by_email(email: str) -> Maybe[User]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(User)
            .filter(User.email == email)
            .first()
        )


def insert_user(user: User) -> Result[User, str]:
    with session_factory() as session:
        try:
            if find_user_by_email(user.email) is Nothing:
                session.add(user)
                session.commit()
                session.refresh(user)
                return Success(user)
            return Failure(f"User by the email {user.email} already exists")
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_user_by_id(u_id: int) -> Maybe[User]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(User, u_id))

def delete_user_by_id(u_id: int) -> Result[User, str]:
    with session_factory() as session:
        try:
            maybe_user = find_user_by_id(u_id)
            if maybe_user is Nothing:
                return Failure(f"No user under the id {u_id}")
            user = maybe_user.map(session.merge).unwrap()
            session.delete(user)
            session.commit()
            return Success(user)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_user(u_id: int, user: User) -> Result[User, str]:
    with session_factory() as session:
        try:
            maybe_user = find_user_by_id(u_id).map(session.merge)
            if maybe_user is Nothing:
                return Failure(f"No user under the id {u_id}")
            user_to_update = maybe_user.unwrap()
            user_to_update.name = user.name
            user_to_update.email = user.email
            user_to_update.phone = user.phone
            session.commit()
            session.refresh(user_to_update)
            return Success(user_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))