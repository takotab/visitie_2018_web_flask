from visitatie import db


class Praktijk(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    users = db.relationship('User', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<Praktijk {}>'.format(self.body)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    praktijk_id = db.Column(db.Integer, db.ForeignKey('praktijk.id'))
    praktijk_password_db = db.Column(db.Integer, db.ForeignKey('praktijk.password_hash'))

    def __repr__(self):
        return '<User {}>'.format(self.username)
