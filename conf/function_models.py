from sqlalchemy import func
from conf.models import Student, Group, Teacher, Subject, Grade


def clear_database(session):
    """Видаляє всі записи з усіх таблиць бази даних."""

    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Group).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    session.commit()


# Функції для моделі Student

def create_student(session, name, group_id):
    student = Student(fullname=name, group_id=group_id)
    session.add(student)
    session.commit()
    return student


def get_student(session, student_id):
    student = session.query(Student).get(student_id)
    return student


def update_student(session, student_id, new_name):
    student = session.query(Student).get(student_id)
    student.fullname = new_name
    session.commit()
    return student


def delete_student(session, student_id):
    student = session.query(Student).get(student_id)
    session.delete(student)
    session.commit()


def list_students(session):
    students = session.query(Student).all()
    if students:
        for student in students:
            print(f"ID: {student.id}, Name: {student.fullname}")
    else:
        print("No students found.")


# Функції для моделі Group

def create_group(session, name):
    group = Group(group_name=name)
    session.add(group)
    session.commit()
    return group


def get_group(session, group_id):
    group = session.query(Group).get(group_id)
    return group


def update_group(session, group_id, new_name):
    group = session.query(Group).get(group_id)
    group.group_name = new_name
    session.commit()
    return group


def delete_group(session, group_id):
    group = session.query(Group).get(group_id)
    session.delete(group)
    session.commit()


def list_groups(session):
    groups = session.query(Group).all()
    if groups:
        for group in groups:
            print(f"ID: {group.id}, Name: {group.group_name}")
    else:
        print("No groups found.")


# Функции для модели Teacher

def create_teacher(session, name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()
    return teacher


def get_teacher(session, teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    return teacher


def update_teacher(session, teacher_id, new_name):
    teacher = session.query(Teacher).get(teacher_id)
    teacher.fullname = new_name
    session.commit()
    return teacher


def delete_teacher(session, teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    session.delete(teacher)
    session.commit()


def list_teachers(session):
    teachers = session.query(Teacher).all()
    if teachers:
        for teacher in teachers:
            print(f"ID: {teacher.id}, Name: {teacher.fullname}")
    else:
        print("No teachers found.")


# Функции для модели Subject

def create_subject(session, name, teacher_id):
    subject = Subject(subject=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    return subject


def get_subject(session, subject_id):
    subject = session.query(Subject).get(subject_id)
    return subject


def update_subject(session, subject_id, new_name):
    subject = session.query(Subject).get(subject_id)
    subject.subject = new_name
    session.commit()
    return subject


def delete_subject(session, subject_id):
    subject = session.query(Subject).get(subject_id)
    session.delete(subject)
    session.commit()


def list_subjects(session):
    subjects = session.query(Subject).all()
    if subjects:
        for subject in subjects:
            print(f"ID: {subject.id}, Name: {subject.subject}")
    else:
        print("No subjects found.")


