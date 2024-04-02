from sqlalchemy.exc import SQLAlchemyError
from faker import Faker
from conf.db import session
from conf.models import Grade
from random import randint

fake = Faker('uk-UA')

def insert_grades():
    try:
        for student in range(1, 46):
            for subject in range(1, 7):
                for _ in range(4):
                    grade = Grade(
                        grade=randint(0, 100),
                        subject_id=subject,
                        student_id=student,
                        grade_date=fake.date_between(start_date='-3y')
                    )
                    session.add(grade)
        session.commit()
        print("Оцінки успішно додані.")
    except SQLAlchemyError as e:
        print(f"Помилка при роботі з базою даних: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == '__main__':
    insert_grades()
