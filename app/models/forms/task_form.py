
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class Task_form(FlaskForm):
    description = StringField('Description', validators=[DataRequired(), Length(min=5)])