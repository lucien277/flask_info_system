from flask import redirect,render_template,request,url_for,flash

from . import app

from .models import db
from .models import User,Post
from .form import RegistForm,loginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    username = {'username':'Miguel'}
    password = {'password':'12345678'}
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if username == 'Miguel' and password == '12345678':
            return render_template('index.html')
        else:
            return '登录失败'
    else:
        return render_template('login.html')


@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        regist_form = RegistForm()
        if regist_form.validate_on_submit():
            return redirect(url_for('login'))
        else:
            return '参数不全'


        # if name and password:
        #     user = User(name=name,password=password)
        #     db.session.add(user)
        #     db.session.commit()
        #     return redirect(url_for('login'))
        # else:
        #     return '参数不全'



