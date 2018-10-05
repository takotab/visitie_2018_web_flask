from flask_wtf import FlaskForm
from flask import current_app
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired

from visitatie.data_models import User
from visitatie.praktijk import Praktijk

PRAKTIJK = Praktijk()

class LoginForm(FlaskForm):
    email = StringField('Email-Adres', validators = [DataRequired()])
    password = PasswordField('Wachtwoord', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ChangeInfoForm(FlaskForm):
    name = StringField('Volledige naam', validators = [DataRequired()])
    email = StringField('Email', validators = [Email(), DataRequired()])
    praktijk = SelectField('Praktijk', choices = PRAKTIJK.get_tuple(),
                           validators = [DataRequired()])
    num_therapeuten = IntegerField('Aantal Therapeuten', validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_num_therapeuten(self, num_therapeuten):
        if int(num_therapeuten) < 1:
            raise ValidationError('Kies een getal boven de 0.')


    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()

        if not user.email == email.data:
            if user is not None:
                raise ValidationError('Gebruik alstublieft een ander email-adres.')

class RegistrationForm(FlaskForm):
    name = StringField('Volledige naam', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    praktijk = SelectField('Praktijk', choices = PRAKTIJK.get_tuple(),
                           validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Gebruik alstublieft een ander email-adres.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    submit = SubmitField('Vraag een nieuw wachtword aan.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
