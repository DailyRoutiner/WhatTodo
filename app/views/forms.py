from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    subject = StringField('Mission', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
