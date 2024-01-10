from flask import redirect,render_template,request,url_for,flash
from . import app,db
from .models import User,Post
from .form import RegistForm,loginForm
from flask_login import current_user,login_user,logout_user


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
        if user is None or not user.check_password(login_form.password.data):
            flash('用户名不存在或密码错误')

        login_user(user,remember=login_form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',form=login_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



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





