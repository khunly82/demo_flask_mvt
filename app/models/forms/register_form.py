from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    username = StringField('Nom d''utilisateur', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('PAssword', validators=[DataRequired(), Length(min=8)])