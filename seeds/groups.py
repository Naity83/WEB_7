from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Group

def delete_groups():
    try:
        session.query(Group).delete()
        session.commit()
        print("Данные успешно удалены из таблицы 'groups'.")
    except SQLAlchemyError as e:
        print(f"Ошибка при удалении данных: {e}")
        session.rollback()
    finally:
        session.close()

def insert_group():
    for i in range(1, 4):
        group = Group(group_name=f"Группа {i}")
        session.add(group)

if __name__ == '__main__':
    try:
        delete_groups()  # Удаление данных перед добавлением новых
        insert_group()   # Добавление новых данных
        session.commit()
        print("Группы успешно добавлены.")
    except SQLAlchemyError as e:
        print(f"Ошибка при работе с базой данных: {e}")
        session.rollback()
    finally:
        session.close()
