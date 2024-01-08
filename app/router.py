from flask import Flask,redirect,render_template,request,url_for
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


@app.route('/login',methods=['GET','POST'])
def login():
    login_form = loginForm()
    if login_form.validate_on_submit():
        print('Login requested for user {}, remember_me={}'.format(login_form.username.data,login_form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',form = login_form)

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
        return render_template('index.html', form=RetForm)

#用户登录



