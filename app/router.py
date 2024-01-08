from flask import Flask,redirect,render_template,request,url_for,flash
from flask_bootstrap import Bootstrap
from .config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3307/选课系统?charset=utf8mb4'

from .form import RegistForm,loginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html',form = loginForm())


#用户注册
@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        RetForm = RegistForm()
        return render_template('regist.html', form=RetForm)
    else:
        RetForm = RegistForm()
        if RetForm.validate():  #validate函数前端实时验证用户输入格式是否正确
            print('接收到的参数为：', RetForm.data)
            return '''<script>alert('您的注册请求已提交!');</script>'''
        else:
             print(RetForm.errors)
        return render_template('login.html', form=RetForm)

#用户登录
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        RetForm = loginForm()
        return render_template('login.html', form=RetForm)
    else:
        RetForm = loginForm(formdata=request.form)
        if RetForm.validate():
            temp = RetForm.data
            print('接收到的参数为：', temp)
            return '''<script>alert('您的登录请求已提交!');</script>'''
        return render_template('index.html', form=RetForm)



