from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Group

def insert_group():
    for i in range(1, 4):
        group = Group(group_name=f"Группа {i}")
        session.add(group)

if __name__ == '__main__':
    try:
        insert_group()
        session.commit()
        print("Группы успешно добавлены.")
    except SQLAlchemyError as e:
        print(f"Ошибка при добавлении групп: {e}")
        session.rollback()
    finally:
        session.close()
