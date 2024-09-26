from typing import Dict

from returns.maybe import Maybe, Nothing, Some
import toolz as t
from sqlalchemy import inspect

from config.base import session_factory
from model import User
from repository.user_repository import find_user_by_id
from service.utils import has_all_keys


def create_user(user_dict: Dict[str, str]) -> User:
    return User(
        name=user_dict["name"],
        email=user_dict["email"],
        phone=user_dict["phone"]
    )


def convert_to_user(user_json: Dict[str, str]) -> Maybe[User]:
    return t.pipe(
        user_json,
        has_all_keys(['name', 'email', 'phone']),
        lambda is_valid: Nothing if not is_valid else Some(create_user(user_json))
    )

def convert_user_to_json(user: User) -> Maybe[Dict[str, str]]:
    with session_factory() as session:
        return (Some(user)
                .map(session.merge)
                .map(lambda u: u.to_dict()))

def convert_to_json(user: User) -> Dict[str, str]:
    return {c.key: getattr(user, c.key) for c in inspect(user).mapper.column_attrs}
