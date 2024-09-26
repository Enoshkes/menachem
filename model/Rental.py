from sqlalchemy import Column, Integer, ForeignKey, Date, Float, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_serializer  import SerializerMixin


from config.base import Base


class Rental(Base, SerializerMixin):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
    rental_date = Column(Date, nullable=False)
    return_date = Column(Date)
    rental_fee = Column(Float, nullable=False)
    late_fee = Column(Float, default=0.0)

    user = relationship("User", back_populates="rentals")
    movie = relationship("Movie", back_populates="rentals")
    store = relationship("Store", back_populates="rentals")