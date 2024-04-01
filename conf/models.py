from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Group(Base):
    __tablename__='groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(50))
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__='students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(150))
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Teacher(Base):
    __tablename__='teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(150))
    subjects = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__='subjects'
    id = Column(Integer, primary_key=True)
    subject = Column(String(100))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__='grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    grade_date = Column(Date, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    subject = relationship("Subject", back_populates="grades")
    student = relationship("Student", back_populates="grades")
