from flask_wtf import FlaskForm
from flask import current_app
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired

from visitatie.data_models import User
from visitatie.praktijk import Praktijk

PRAKTIJK = Praktijk()

class LoginForm(FlaskForm):
    email = StringField('Email-Adres', validators = [DataRequired()])
    password = PasswordField('Wachtwoord', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


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
