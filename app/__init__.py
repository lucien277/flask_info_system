from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app,db)#数据库迁移引擎对象

bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login' #告诉flask-login登录视图函数的名称

from app import router,models

# from flask_bootstrap import Bootstrap
# bootstrap = Bootstrap(app)