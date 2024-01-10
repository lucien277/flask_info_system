from flask import redirect,render_template,request,url_for,flash
from . import app,db
from .models import User,Post
from .form import RegistForm,loginForm
from flask_login import current_user,login_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for("index"))

    login_form = loginForm()   # 实例化表单
    if login_form.validate_on_submit():
        user = User.query.filter_by(name=login_form.username.data).first()
        if user is None:
            flash('用户名不存在')
            return redirect(url_for('login'))


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





