from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Subject


def insert_subjects():
    subjects = [('Математика', 1), ('Фізика', 2), ('Хімія', 3), ('Історія', 1), ('Література', 2), ('Географія', 3)]
    for sub in subjects:
        subject = Subject(
            subject=sub[0],
            teacher_id=sub[1]
        )
        session.add(subject)


if __name__ == '__main__':
    try:
        insert_subjects()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
