from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, SubmitField, SelectField,
                     FloatField,
                     IntegerField,
                     )
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired


# class BezoekersGegevensCheck(FlaskForm):

class GegevensCheck(FlaskForm):
    ww_bezoekende = PasswordField(
            "<img src='image/bezoekende.jpg' alt='bezoekende'> <div></div>Wachtwoord bezoekende "
            "Praktijk",
            validators = [DataRequired()])
    ww_current_user = PasswordField(
            "<img src='image/praktijk.png' alt='bezoekende'> <div></div> Uw Wachtwoord",
            validators = [DataRequired()])
    alles_klopt = BooleanField('Alles klopt', validators = [DataRequired()])
    submit = SubmitField('Start Visitatie')


class FormNumbers(FlaskForm):
    VASPgem_start = FloatField("VAS-P gem start", validators = [DataRequired()])
    VASPgem_end = FloatField("VAS-P gem end", validators = [DataRequired()])
    VASPmin_start = FloatField("VAS-P min start", validators = [DataRequired()])
    VASPmin_end = FloatField("VAS-P min end", validators = [DataRequired()])
    VASPmax_start = FloatField("VAS-P max start", validators = [DataRequired()])
    VASPmax_end = FloatField("VAS-P max end", validators = [DataRequired()])

    PSK1_start = FloatField("PSK 1 start", validators = [DataRequired()])
    PSK1_end = FloatField("PSK 1 end", validators = [DataRequired()])
    PSK2_start = FloatField("PSK 2 start", validators = [DataRequired()])
    PSK2_end = FloatField("PSK 2 end", validators = [DataRequired()])
    PSK3_start = FloatField("PSK 3 start", validators = [DataRequired()])
    PSK3_end = FloatField("PSK 3 end", validators = [DataRequired()])

    NRS_start = FloatField("NRS start", validators = [DataRequired()])
    NRS_end = FloatField("NRS end", validators = [DataRequired()])

    QBPDS_start = FloatField("QBPDS start", validators = [DataRequired()])
    QBPDS_end = FloatField("QBPDS end", validators = [DataRequired()])

    GPE_start = FloatField("GPE start", validators = [DataRequired()])
    GPE_end = FloatField("GPE end", validators = [DataRequired()])

    ander_meet = StringField("Welk ander meetinstrument gebruikt u?", validators = [DataRequired()])
    anders_start = FloatField("Anders start", validators = [DataRequired()])
    anders_end = FloatField("Anders start", validators = [DataRequired()])

    aantal_behandelingen = IntegerField("Aantal behandelingen?", validators = [DataRequired()])
    Nog_een = SelectField("Wilt u nog een patiënt invoeren?", choices = [('1', 'Ja'), ('0', 'Nee')],
                          validators = [DataRequired()])

    submit = SubmitField('Volgende')
