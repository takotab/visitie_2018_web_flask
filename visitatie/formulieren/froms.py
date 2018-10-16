from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired


# class BezoekersGegevensCheck(FlaskForm):

class GegevensCheck(FlaskForm):
    ww_bezoekende = PasswordField(
            "<img src='image/Logorugnetwerk_small.jpg' alt='Logorugnetwerk'> Wachtwoord bezoekende "
            "Praktijk",
            validators = [DataRequired()])
    ww_current_user = PasswordField("Uw Wachtwoord", validators = [DataRequired()])
    alles_klopt = BooleanField('Alles klopt', validators = [DataRequired()])
    submit = SubmitField('Start Visitatie')
