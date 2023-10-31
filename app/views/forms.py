from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from wtforms.fields import EmailField


class TaskForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])


class UserCreateForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', 'Unmatch the password.')])
    password2 = PasswordField('Check Password', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])

