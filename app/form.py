from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('submit')
class RegistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    submit = SubmitField('submit')

