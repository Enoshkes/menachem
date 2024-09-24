from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))

    rentals = relationship("Rental", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id:{self.id}, name:{self.name}, email:{self.email}, phone:{self.phone})>"