from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import Store


def insert_store(store: Store) -> Result[Store, str]:
    with session_factory() as session:
        try:
            session.add(store)
            session.commit()
            session.refresh(store)
            return Success(store)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_store_by_id(s_id: int) -> Maybe[Store]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Store, s_id))

def delete_store_by_id(s_id: int) -> Result[Store, str]:
    with session_factory() as session:
        try:
            maybe_store = find_store_by_id(s_id).map(session.merge)
            if maybe_store is Nothing:
                return Failure(f"No store under the id {s_id}")
            store = maybe_store.unwrap()
            session.delete(store)
            session.commit()
            return Success(store)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_store(s_id: int, store: Store) -> Result[Store, str]:
    with session_factory() as session:
        try:
            maybe_store = find_store_by_id(s_id).map(session.merge)
            if maybe_store is Nothing:
                return Failure(f"No store under the id {s_id}")
            store_to_update = maybe_store.unwrap()
            store_to_update.state = store.state
            store_to_update.address = store.address
            store_to_update.city = store.city
            store_to_update.name = store.name
            session.commit()
            session.refresh(store_to_update)
            return Success(store_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))