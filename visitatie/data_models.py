from time import time

import jwt
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from visitatie.praktijk import Praktijk
from visitatie import db, login

PRAKTIJK = Praktijk()


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    praktijk = db.Column(db.String(25), index = True)
    num_therapeuten = db.Column(db.Integer)
    bezoekende_praktijk = db.Column(db.String(25), index = True, unique = True)
    te_bezoeken_praktijk = db.Column(db.String(25), index = True, unique = True)


    def __repr__(self):
        return '<Name {}\tEmail {}\tPraktijk {}\n' \
               'Bezoekende_p {}\tte_bezoeken_p {}'.format(
                self.name, self.email, self.praktijk,
                self.bezoekende_praktijk, self.te_bezoeken_praktijk
                )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in = 6000):
        return jwt.encode(
                {'reset_password': self.id, 'exp': time() + expires_in},
                current_app.config['SECRET_KEY'], algorithm = 'HS256').decode('utf-8')

    def get_praktijk(self):
        return self.praktijk

    def get_bezoekende_praktijk(self):
        return self.bezoekende_praktijk

    def get_te_bezoeken_praktijk(self):
        return self.te_bezoeken_praktijk

    def check_password_bezoekende_praktijk(self, password):
        bezoekende_user = User.query.filter_by(praktijk = self.bezoekende_praktijk).first()
        if bezoekende_user is None:
            raise KeyError(self.bezoekende_praktijk + " not found")
        return bezoekende_user.check_password(password)

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms = ['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# def get_praktijk(praktijk):
#     if praktijk in PRAKTIJK.dct:
#         return PRAKTIJK.dct[praktijk]
#     else:
#         return 'Onbekend'
