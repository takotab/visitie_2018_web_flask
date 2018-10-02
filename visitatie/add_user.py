from visitatie.data_models import User
from visitatie import db
from flask import current_app


# TO be continued but first CLI making with tutorial

def main():
    with current_app.app_context():
        u = User(username = 'susan', email = 'susan@example.com')
        db.session.add(u)
        db.session.commit()
        print(User.query.all())


if __name__ == '__main__':
    main()
