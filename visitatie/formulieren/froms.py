from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired


class GegevensCheck(FlaskForm):
    alles_klopt = BooleanField('Alles klopt')
    submit = SubmitField('Start Visitatie')
