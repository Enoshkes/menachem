from datetime import datetime, timedelta
from operator import attrgetter

import pytest
from returns.maybe import Nothing
from returns.result import Success
from operator import eq
from repository.db import create_tables, drop_tables
from model import User, Rental, Store, Movie
from repository.movie_repository import insert_movie
import toolz as t

from repository.rental_repository import insert_rental, find_rental_by_id, delete_rental_by_id, update_rental
from repository.store_repository import insert_store
from repository.user_repository import insert_user


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    yield
    drop_tables()


@pytest.fixture(scope="module")
def setup_database_with_rental(setup_database):
    movie = Movie(title="the matrix", genre="scifi", year=1998)
    store = Store(name="blockbuster", city="rishon", state="israel", address="tarmav")
    user = User(name="enosh", email="enoshh12@gmail.com", phone="0523337451")
    insert_movie(movie)
    insert_store(store)
    insert_user(user)
    yield insert_rental(Rental(
        user_id=1,
        store_id=1,
        movie_id=1,
        rental_date=datetime.now(),
        return_date=datetime.now() + timedelta(weeks=2),
        rental_fee=3.50,
        late_fee=0
    ))


def test_movie_creation(setup_database_with_rental):
    assert (setup_database_with_rental
            .map(attrgetter("id"))
            .map(t.partial(eq, 1))
            .value_or(False))


def test_find_movie_by_id(setup_database_with_rental):
    assert (find_rental_by_id(1)
            .map(attrgetter("id"))
            .map(t.partial(eq, 1))
            .value_or(False))


def test_delete_movie(setup_database_with_rental):
    assert isinstance(delete_rental_by_id(1), Success)
    assert find_rental_by_id(1) is Nothing


def test_update_movie(setup_database_with_rental):
    assert setup_database_with_rental is not Nothing
    rental = setup_database_with_rental.unwrap()
    assert (update_rental(1, Rental(
        rental_date=datetime.now(),
        return_date=datetime.now() + timedelta(weeks=1),
        rental_fee=3.2,
        late_fee=4.1
    ))
            .map(attrgetter("return_date"))
            .map(lambda return_date: return_date != rental.return_date)
            .value_or(False))
