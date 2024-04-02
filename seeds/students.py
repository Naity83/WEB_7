from sqlalchemy.exc import SQLAlchemyError
from faker import Faker
from conf.db import session
from conf.models import Student

fake = Faker('uk-UA')


def insert_students():
    for i in range(1, 4):
        for _ in range (15):
            student = Student(
            fullname = fake.name(),
            group_id = i
            )
            session.add(student)

if __name__ == '__main__':
    try:
        insert_students()  
        session.commit()
        print("Студенти успішно додані.")
    except SQLAlchemyError as e:
        print(f"Помилка при роботі з базою даних: {e}")
        session.rollback()
    finally:
        session.close()
