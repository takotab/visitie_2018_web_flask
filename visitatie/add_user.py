from visitatie.data_models import User
from visitatie import db
from visitatie import create_app
from flask import current_app


def main(app):
    app.app_context().push()
    with current_app.app_context():
        u = User(username = 'susan',
                 email = 'susan@example.com',
                 password_hash = 'eeeee')
        db.session.add(u)
        db.session.commit()
        print(User.query.all())


if __name__ == '__main__':
    app = create_app()
    main(app)
