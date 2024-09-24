from config.base import session_factory
from model import Rental, Store, User, Movie
from model.Rental import Student, Course, Car

from repository.db import create_tables

if __name__ == '__main__':
    create_tables()
    with session_factory() as session:
        a = 8
        # car = Car()
        # session.add(car)
        # session.commit()

        # student = session.get(Student, 1)
        # car = session.get(Car, 1)
        # student.cars.remove(car)
        # session.commit()

        # student = session.get(Student, 1)
        # car = session.get(Car, 1)
        # student.cars.append(car)
        # session.commit()
