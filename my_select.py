from conf.db import session
from conf.models import Grade, Student, Subject, Teacher, Group
from sqlalchemy import func, desc, and_, select


def query_01():
    #Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2)\
    .label('avg_grade'))\
    .select_from(Grade)\
    .join(Student)\
    .group_by(Student.id)\
    .order_by(desc('avg_grade'))\
    .limit(5).all()
    return result


def query_02():
    #Знайти студента із найвищим середнім балом з певного предмета.
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2)\
    .label('avg_grade'))\
    .select_from(Grade)\
    .join(Student).join(Subject)\
    .filter(Subject.subject == 'Фізика')\
    .group_by(Student.id)\
    .order_by(desc('avg_grade'))\
    .limit(1).all()
    return result


def query_03():
    #Знайти середній бал у групах з певного предмета.
    result = session.query(Group.group_name, func.round(func.avg(Grade.grade), 2)\
    .label('avg_grade'))\
    .select_from(Grade)\
    .join(Student).join(Subject).join(Group)\
    .filter(Subject.subject == 'Математика')\
    .group_by(Group.id)\
    .all()
    return result


def query_04():    
    #Знайти середній бал на потоці (по всій таблиці оцінок).
    result = session.query(func.round(func.avg(Grade.grade), 2)\
    .label('avg_grade'))\
    .select_from(Grade)\
    .all()
    return result


def query_05():
    #Знайти які курси читає певний викладач.
    result = session.query(Subject.subject)\
    .select_from(Subject)\
    .join(Teacher)\
    .filter(Teacher.fullname == 'Іванов Іван')\
    .all()
    return result

def query_06():
    #Знайти список студентів у певній групі.
    result = session.query(Student.fullname)\
    .select_from(Student)\
    .join(Group)\
    .filter(Group.group_name == 'Группа 2')\
    .all()
    return result


def query_07():
    #Знайти оцінки студентів у окремій групі з певного предмета.
    result = session.query(Student.fullname, Grade.grade)\
    .select_from(Grade)\
    .join(Student)\
    .join(Subject)\
    .join(Group)\
    .filter(Group.group_name == 'Группа 1')\
    .filter(Subject.subject == 'Фізика')\
    .all()
    return result


def query_08():
    #Знайти середній бал, який ставить певний викладач зі своїх предметів.
    result = session.query(Teacher.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
    .select_from(Teacher)\
    .join(Subject) \
    .join(Grade) \
    .group_by(Teacher.fullname) \
    .having(Teacher.fullname == 'Іванов Іван') \
    .all()
    return result


def query_09():
    #Знайти список курсів, які відвідує певний студент.
    result = session.query(Subject.subject)\
    .select_from(Student)\
    .join(Grade)\
    .join(Subject)\
    .filter(Student.fullname == 'Кирило Рябченко')\
    .distinct()\
    .all()
    return result


def query_10():
    #Список курсів, які певному студенту читає певний викладач.
    result = session.query(Subject.subject)\
    .select_from(Student)\
    .join(Grade)\
    .join(Subject)\
    .join(Teacher)\
    .filter(Student.fullname == 'Кирило Рябченко')\
    .filter(Teacher.fullname == 'Іванов Іван')\
    .distinct()\
    .all()
    return result


def query_11():
    #Середній бал, який певний викладач ставить певному студентові.
    result = session.query(
        Subject.subject,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ) \
    .select_from(Grade)\
    .join(Subject, Grade.subject_id == Subject.id)\
    .join(Teacher, Subject.teacher_id == Teacher.id)\
    .join(Student, Grade.student_id == Student.id)\
    .filter(Teacher.fullname == 'Іванов Іван')\
    .filter(Student.fullname == 'Кирило Рябченко')\
    .group_by(Subject.subject)\
    .all()
    return result


def query_12():
    #Оцінки студентів у певній групі з певного предмета на останньому занятті
    subquery = (
        session.query(func.MAX(Grade.grade_date))
        .select_from(Grade)
        .join(Student)
        .filter(
            and_(Student.group_id == 2, Grade.subject_id == 3)
        )
    ).scalar_subquery()

    result = (
        session.query(Subject.subject, Grade.grade)
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Teacher)
        .filter(
            and_(
                Group.id == 2,
                Grade.subject_id == 3,
                Grade.grade_date == subquery,
            )
        )
        .order_by(desc(Grade.grade))\
        .all()
    )
    return result


if __name__ == '__main__':
    print(query_12())