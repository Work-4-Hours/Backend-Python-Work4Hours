import os
import bcrypt
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
host = os.environ['DB_HOST']
database = os.environ['DB_DATABASE']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'

salt = bcrypt.gensalt(rounds=16)

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_DATABASE: str
    DB_URI: str

    # SMTP CREDENTIALS
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encodig = "utf-8"

settings = Settings()