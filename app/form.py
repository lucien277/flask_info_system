from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class RegistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    submit = SubmitField('submit')

