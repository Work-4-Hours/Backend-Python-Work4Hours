from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
host = os.environ['DB_HOST']
database = os.environ['DB_DATABASE']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'



salt = bcrypt.gensalt(rounds=16)
