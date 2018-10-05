from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired


class GegevensCheck(FlaskForm):
    # TODO add wachtwoord bezoekde praktijk
    ww_bezoekende = PasswordField("Wachtwoord bezoekende Praktijk")
    ww_current_user = PasswordField("Uw Wachtwoord")
    alles_klopt = BooleanField('Alles klopt')
    submit = SubmitField('Start Visitatie')
