from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher


def insert_teacher():
    for teacher_name in ['Іванов Іван', 'Петров Петро', 'Сидоров Сидор']:
        teacher = Teacher(fullname= teacher_name)
        session.add(teacher)

if __name__ == '__main__':
    try:
        insert_teacher()  
        session.commit()
        print("Вчителі успішно додані.")
    except SQLAlchemyError as e:
        print(f"Помилка при роботі з базою даних: {e}")
        session.rollback()
    finally:
        session.close()
