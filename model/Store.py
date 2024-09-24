from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)

    rentals = relationship("Rental", back_populates="store")