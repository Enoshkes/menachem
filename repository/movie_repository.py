from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import Movie

def insert_movie(movie: Movie) -> Result[Movie, str]:
    with session_factory() as session:
        try:
            session.add(movie)
            session.commit()
            session.refresh(movie)
            return Success(movie)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_movie_by_id(m_id: int) -> Maybe[Movie]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Movie, m_id))

def delete_movie_by_id(m_id: int) -> Result[Movie, str]:
    with session_factory() as session:
        try:
            maybe_movie = find_movie_by_id(m_id).map(session.merge)
            if maybe_movie is Nothing:
                return Failure(f"No movie under the id {m_id}")
            movie = maybe_movie.unwrap()
            session.delete(movie)
            session.commit()
            return Success(movie)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_movie(m_id: int, movie: Movie) -> Result[Movie, str]:
    with session_factory() as session:
        try:
            maybe_movie = find_movie_by_id(m_id).map(session.merge)
            if maybe_movie is Nothing:
                return Failure(f"No movie under the id {m_id}")
            movie_to_update = maybe_movie.unwrap()
            movie_to_update.title = movie.title
            movie_to_update.genre = movie.genre
            movie_to_update.year = movie.year
            session.commit()
            session.refresh(movie_to_update)
            return Success(movie_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))
