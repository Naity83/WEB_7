import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Шаблон URI
#URI: postgresql://username:password@domain:port/database

# Шлях до конфігураційного файлу
file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')  # ../config.ini

# Читання конфігураційного файлу
config = configparser.ConfigParser()
config.read(file_config)

# Отримання параметрів підключення до бази даних з конфігураційного файлу
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')
db = config.get('DEV_DB', 'DB_NAME')

# Формування URI для підключення до бази даних PostgreSQL
URI = f"postgresql://{user}:{password}@{domain}:{port}/{db}"

# Створення об'єкту двигуна для підключення до бази даних
engine = create_engine(URI, echo=True, pool_size=5, max_overflow=0)

# Створення сесії для роботи з базою даних
DBSession = sessionmaker(bind=engine)
session = DBSession()
