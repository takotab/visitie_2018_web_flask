import pytest
from visitatie.data_models import User


@pytest.mark.usefixtures('app, db')
def test_add_user(app, db, name = 'kevin'):
    print(app, name)
    with app.app_context():
        print("appcontecxt")
        u = User(name = name,
                 email = name + '@example.com',
                 )

        u.set_password(name + '123')
        db.session.add(u)
        print(db)
        db.session.commit()

    # test user is in db
    users = User.query.filter_by(name = name)
    print(users)
    assert len(users) == 1
    user = users.first()
    assert user.check_password(name + '123')
    assert not user.check_password(name + '12')
