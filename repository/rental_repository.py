from returns.maybe import Nothing, Maybe
from returns.result import Result, Failure, Success
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import Rental
from repository.movie_repository import find_movie_by_id
from repository.store_repository import find_store_by_id
from repository.user_repository import find_user_by_id


def insert_rental(rental: Rental) -> Result[Rental, str]:
    with session_factory() as session:
        try:
            maybe_user = find_user_by_id(rental.user_id).map(session.merge)
            maybe_movie = find_movie_by_id(rental.movie_id).map(session.merge)
            maybe_store = find_store_by_id(rental.store_id).map(session.merge)

            if any(entity is Nothing for entity in [maybe_user, maybe_movie, maybe_store]):
                return Failure("Missing entity of rental")

            rental.user = maybe_user.unwrap()
            rental.store = maybe_store.unwrap()
            rental.movie = maybe_movie.unwrap()
            session.add(rental)
            session.commit()
            session.refresh(rental)
            return Success(rental)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_rental_by_id(r_id: int) -> Maybe[Rental]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Rental, r_id))

def delete_rental_by_id(r_id: int) -> Result[Rental, str]:
    with session_factory() as session:
        try:
            maybe_rental = find_rental_by_id(r_id).map(session.merge)
            if maybe_rental is Nothing:
                return Failure(f"No rental under the id {r_id}")
            rental = maybe_rental.unwrap()
            session.delete(rental)
            session.commit()
            return Success(rental)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_rental(r_id: int, rental: Rental) -> Result[Rental, str]:
    with session_factory() as session:
        try:
            maybe_rental = find_rental_by_id(r_id).map(session.merge)
            if maybe_rental is Nothing:
                return Failure(f"No rental under the id {r_id}")
            rental_to_update = maybe_rental.unwrap()
            rental_to_update.late_fee = rental.late_fee
            rental_to_update.rental_fee = rental.rental_fee
            rental_to_update.return_date = rental.return_date
            rental_to_update.rental_date = rental.rental_date
            session.commit()
            session.refresh(rental_to_update)
            return Success(rental_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))