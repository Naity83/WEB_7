import logging
from argparse import ArgumentParser
import conf.function_models as dr
from conf.db import session

# Створення об'єкту для аналізу аргументів командного рядка
parser = ArgumentParser(description='Студентська база даних')
parser.add_argument('--action', '-a', help='Команди: create, get, update, remove, list')
parser.add_argument('--model', '-m', help='Моделі: Teacher, Group, Student, Subject, Grade')
parser.add_argument('--id', help='ID об\'єкта')
parser.add_argument('--name', '-n', help='Ім\'я об\'єкта')
parser.add_argument('--subject', '-s', help='Предмет об\'єкта')
parser.add_argument('--group', '-g', help='Група студента')
parser.add_argument('--value', '-v', help='Значення об\'єкта')

# Аналіз аргументів командного рядка
arguments = parser.parse_args()
my_args = vars(arguments)

# Отримання значень аргументів
action = my_args.get('action')
model = my_args.get('model')
id = my_args.get('id')
name = my_args.get('name')
subject = my_args.get('subject')
value = my_args.get('value')
group = my_args.get('group')

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Функції для операцій CRUD

def create(session):
    try:
        if not name:
            raise ValueError('Відсутнє ім\'я')

        match model:
            case 'Teacher': 
                dr.create_teacher(session, name)
                logging.info('Створено вчителя: %s', name)
            case 'Group': 
                dr.create_group(session, name)
                logging.info('Створено групу: %s', name)
            case 'Student':
                dr.create_student(session, name, group)
                logging.info('Створено студента: %s', name)
            case 'Subject':
                teacher = dr.get_teacher(session, id)
                dr.create_subject(session, name, teacher)
                logging.info('Створено предмет: %s', name)
    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Помилка під час створення: %s', str(e))

# Аналогічно реалізовані функції update, remove, get та list_

def update(session):
    try:
        if not model:
            raise ValueError('Model parameter is missing')
        
        if not id:
            raise ValueError('ID parameter is missing')
        
        match model:
            case 'Teacher':
                dr.update_teacher(session, id, name)
                logging.info('Teacher updated: ID %s, new name: %s', id, name)
            case 'Group':
                dr.update_group(session, id, name)
                logging.info('Group updated: ID %s, new name: %s', id, name)
            case 'Student':
                dr.update_student(session, id, name)
                logging.info('Student updated: ID %s, new name: %s', id, name)
            case 'Subject':
                dr.update_subject(session, id, name)
                logging.info('Subject updated: ID %s, new name: %s', id, name)
            
    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Error occurred during update operation: %s', str(e))

def remove(session):
    try:

        if not id:
            raise ValueError('ID parameter is missing')
        
        match model:
            case 'Teacher':
                dr.delete_teacher(session, id)
                logging.info('Teacher deleted: ID %s', id)
            case 'Group':
                dr.delete_group(session, id)
                logging.info('Group deleted: ID %s', id)
            case 'Student':
                dr.delete_student(session, id)
                logging.info('Student deleted: ID %s', id)
            case 'Subject':
                dr.delete_subject(session, id)
                logging.info('Subject deleted: ID %s', id)
            
    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Error occurred during remove operation: %s', str(e))

def get(session):
    try:

        if not id:
            raise ValueError('ID parameter is missing')

        match model:
            case 'Teacher':
                teacher = dr.gteacher(session, id)
                logging.info('Teacher details: ID %s, Name: %s', id, teacher.name)
            case 'Group':
                group = dr.ggroup(session, id)
                logging.info('Group details: ID %s, Name: %s', id, group.name)
            case 'Student':
                student = dr.gstudent(session, id)
                logging.info('Student details: ID %s, Name: %s', id, student.name)
            case 'Subject':
                subject = dr.gsubject(session, id)
                logging.info('Subject details: ID %s, Name: %s', id, subject.name)
            
    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Error occurred during get operation: %s', str(e))

def list_(session):
    try:

        match model:
            case 'Teacher':
                dr.list_teachers(session)
            case 'Group':
                dr.list_groups(session)
            case 'Student':
                dr.list_students(session)
            case 'Subject':
                dr.list_subjects(session)
            

    except Exception as e:
        logging.error('Error occurred during get operation: %s', str(e))




# Основний код
if __name__ == "__main__":

    
    with session:
        # Виклик відповідної функції залежно від команди
        match action:
            case 'create':
                create(session)
            case 'update':
                update(session)
            case 'remove':
                remove(session)
            case 'get':
                get(session)
            case 'list':
                list_(session)
            case _:
                parser.print_help()
