from operator import attrgetter

import pytest
from returns.maybe import Nothing
from returns.result import Success, Failure
from operator import eq
from repository.db import create_tables, drop_tables
from model import User, Rental, Store, Movie
from repository.user_repository import insert_user, find_user_by_email, find_user_by_id, delete_user_by_id, update_user
import toolz as t


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    yield
    drop_tables()


@pytest.fixture(scope="module")
def setup_database_with_user(setup_database):
    user = User(name="enosh", email="enoshh12@gmail.com", phone="0523335897")
    yield insert_user(user)


def test_user_creation(setup_database):
    user = User(name="enosh", email="enoshh12@gmail.com", phone="0523335897")
    user_result = insert_user(user)
    assert isinstance(user_result, Success)
    assert isinstance(insert_user(user), Failure)


def test_find_user_by_email(setup_database):
    email = "enoshh12@gmail.com"
    user = User(name="enosh", email=email, phone="0523335897")
    insert_user(user)
    assert (find_user_by_email(email)
            .map(attrgetter("email"))
            .map(t.partial(eq, email))
            .value_or(False))


def test_find_user_by_id(setup_database_with_user):
    assert (find_user_by_id(1)
            .map(attrgetter("id"))
            .map(t.partial(eq, 1))
            .value_or(False))


def test_delete_user(setup_database_with_user):
    assert isinstance(delete_user_by_id(1), Success)
    assert find_user_by_id(1) is Nothing


def test_update_user(setup_database_with_user):
    assert setup_database_with_user is not Nothing
    user = setup_database_with_user.unwrap()
    assert (update_user(1, User(email="bobo", phone="999", name="koko"))
            .map(attrgetter("email"))
            .map(lambda email: email != user.email)
            .value_or(False))
