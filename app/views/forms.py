from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
