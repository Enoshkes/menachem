from sqlalchemy import Column, Integer, ForeignKey, Date, Float, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from config.base import Base

class StudentCars(Base):
    __tablename__ = "students_cars"
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('student_id', 'car_id'),
    )


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, autoincrement=True)
    students = relationship("Student", secondary="students_cars", back_populates="cars")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    students = relationship("Student", back_populates="course")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    cars = relationship("Car", secondary="students_cars", back_populates="students")
    course = relationship("Course", back_populates="students")


class Rental(Base):
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