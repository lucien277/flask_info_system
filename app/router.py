from flask import redirect,render_template,request,url_for,flash
from . import app,db
from .models import *
from .form import RegistForm,loginForm
from flask_login import current_user,login_user,logout_user,login_required

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/unfinished')
def unfinished():
    return render_template('unfinished.html')


# 首页
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# 登录

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:  # 如果已经登录，直接跳转到首页
        return redirect(url_for("index"))

    if request.method == 'POST':  # 如果是 POST 请求
        login_form = loginForm()
        if login_form.validate_on_submit():  # 如果表单提交
            user = User.query.filter_by(username=login_form.username.data).first()  # 通过用户名查询用户
            if user is None or not user.check_password(login_form.password.data):  # 如果用户不存在或者密码错误
                flash('用户名不存在或密码错误')
            else:
                login_user(user, remember=login_form.remember_me.data)
                return redirect(url_for('course_page'))  # 重定向到用户界面
    else:  # 如果是 GET 请求
        login_form = loginForm()

    return render_template('login.html', title="login", form=login_form)

# 推出登陆
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# 注册
@app.route('/regist',methods=['GET','POST'])
def regist():
    if current_user.is_authenticated:
        return redirect(url_for("index")) # 如果已经登录，直接跳转到首页
    regist_form = RegistForm()
    if regist_form.validate_on_submit():
        user = User(username=regist_form.username.data)
        user.set_password(regist_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你注册成功')
        return redirect(url_for('login'))
    return render_template('regist.html',title="regist",form=regist_form)

# 个人主页
@app.route('/user/<name>')
@login_required
def user(name):
    return render_template('user.html',name=name)

# 专业课程页面
@app.route('/course_page')
def course_page():
    return render_template('course_page.html')

# 查询课程列表
@app.route('/course/<course_model>', methods=['GET'])
def show_courses_by_model(course_model):
        #按照课程模块首字母模糊查询课程，没完成该功能
    # if len(course_model) == 1:
    #     courses = Course.find_by_course_letter(course_model)
    #     return render_template('courses.html', courses=courses)
    # else:
        courses = Course.find_by_course_model(course_model)  # 通过课程模块查询课程
        return render_template('courses.html', courses=courses)





