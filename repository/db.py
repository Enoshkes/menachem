from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from config.base import Base, engine

def get_engine():
    uri = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost/rent')
    return create_engine(uri)

def create_tables():
    Base.metadata.create_all(engine)

def drop_tables():
    Base.metadata.drop_all(engine)