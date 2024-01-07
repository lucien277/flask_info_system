from flask import Flask,redirect,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
from app import app



from .form import RegistForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


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



