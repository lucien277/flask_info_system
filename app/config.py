import os

#数据库变量
HOST =  'localhost'
PORT = 3307
USER = 'root'
PASSWORD = '12345678'
DATABASE = 'flask_orm'
CHARSET = 'utf8mb4'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset={}'.format(USER,PASSWORD,HOST,PORT,DATABASE,CHARSET)

#配置类
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is secret key'

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False