from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_serializer  import SerializerMixin

from config.base import Base

class Store(Base, SerializerMixin):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)

    rentals = relationship("Rental", back_populates="store")

    serialize_rules = ('-rentals.store',)
