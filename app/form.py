from flask_wtf import FlaskForm
from wtforms import form,SubmitField, StringField, PasswordField, BooleanField,widgets
from wtforms.validators import DataRequired,ValidationError,EqualTo,Regexp,Length
from wtforms.fields import simple

class loginForm(FlaskForm):
    username = simple.StringField(
        validators=[
            DataRequired(message='用户名不能为空'),
            Length(min=3,max=12,message='用户名长度必须在3-12位之间')
            # Regexp(regex="[0-9a-zA-Z]{5,}",message='密码不允许使用特殊字符')
            ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入用户名"}
        )

    password = simple.PasswordField(
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3,max=12,message='密码长度必须在3-12位之间'),
            # Regexp(regex="[0-9a-zA-Z]{5,}",message='密码不允许使用特殊字符')
            ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入密码"}
    )


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
            Regexp(regex="[0-9a-zA-Z]{5,}",message='密码不允许使用特殊字符')
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
