from operator import attrgetter

import pytest
from returns.maybe import Nothing
from returns.result import Success, Failure
from operator import eq
from repository.db import create_tables, drop_tables
from model import User, Rental, Store, Movie
import toolz as t

from repository.store_repository import insert_store, find_store_by_id, delete_store_by_id, update_store


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    yield
    drop_tables()


@pytest.fixture(scope="module")
def setup_database_with_store(setup_database):
    store = Store(name="blockbuster", city="rishon le zion", address="herzel 82", state="israel")
    yield insert_store(store)

def test_store_creation(setup_database_with_store):
    assert (setup_database_with_store
            .map(attrgetter("name"))
            .map(t.partial(eq, "blockbuster"))
            .value_or(False))

def test_find_by_id(setup_database_with_store):
    assert (find_store_by_id(1)
            .map(attrgetter("id"))
            .map(t.partial(eq, 1))
            .value_or(False))

def test_delete(setup_database_with_store):
    assert isinstance(delete_store_by_id(1), Success)
    assert find_store_by_id(1) is Nothing

def test_update(setup_database_with_store):
    assert setup_database_with_store is not Nothing
    store = setup_database_with_store.unwrap()
    assert (update_store(1, Store(name="koko", state="jumbo", city="popo", address="lolo"))
            .map(attrgetter("name"))
            .map(lambda n: n != store.name)
            .value_or(False))