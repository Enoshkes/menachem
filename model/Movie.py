from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy_serializer  import SerializerMixin

from config.base import Base


class Movie(Base, SerializerMixin):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    genre = Column(String(50))
    year = Column(Integer, nullable=False)

    rentals = relationship("Rental", lazy="noload", back_populates="movie")

    serialize_rules = ('-rentals.movie',)
