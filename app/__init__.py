from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app,db)#数据库迁移引擎对象

login = LoginManager(app)

from app import router,models

# from flask_bootstrap import Bootstrap
# bootstrap = Bootstrap(app)