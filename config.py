from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

load_dotenv()

user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
host = os.environ['DB_HOST']
database = os.environ['DB_DATABASE']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'

key = Fernet.generate_key()
file = open('key.key', 'wb')
file.write(key)
file.close()

print(key,"------------------------------------Hola__________________________")
F = Fernet(key)