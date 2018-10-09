import pytest
from visitatie.data_models import User


def test_add_user(app, session, name = 'kevin'):
    print(app, session)
    # with app.app_context():
    u = User(name = name,
             email = name + '@example.com',
             )

    u.set_password(name + '123')
    session.add(u)
    session.commit()

    # test user is in db
    user = User.query.filter_by(name = name).first()
    assert user.check_password(name + '123')
    assert not user.check_password(name + '12')
