import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is secret key'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost:3307/flask_orm?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False