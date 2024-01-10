from flask_wtf import FlaskForm
from wtforms import form,SubmitField, StringField, PasswordField, BooleanField,widgets
from wtforms.validators import DataRequired,ValidationError,EqualTo,Regexp,Length
from wtforms.fields import simple
from app.models import User

class loginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('submit')

class RegistForm(FlaskForm):
    username = simple.StringField(
        label='用户名:',
        validators=[
            DataRequired(message='用户名不能为空'),
            Length(min=3,max=12,message='用户名长度必须在3-12位之间')
            ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入注册用户名"}
        )
    password = simple.PasswordField(
        label='密码:',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3,max=12,message='密码长度必须在3-12位之间'),
            # Regexp(regex="[0-9a-zA-Z]{ 3,}",message='重新设置密码')
            ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入注册密码"}
        )
    repassword = simple.PasswordField(
        label='确认密码:',
        validators=[
            DataRequired(message='密码不能为空'),
            EqualTo('password',message='两次密码不一致')
            ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"确认密码"}
        )
    Submit = SubmitField(
        label='注册',
        render_kw={'class': 'btn btn-primary'}
        )

    # 自定义验证器，验证用户名是否存在
    def validate_username(self,username):
        username = User.query.filter_by(username=username.data).first()
        if username is not None:
            raise ValidationError('用户名已存在')