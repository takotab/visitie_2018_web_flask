# import pytest
# from visitatie.data_models import User, db
#
# testdata = [
#     ('divera', '1', 'roos', 'tako'),
#     ('roos', '2', 'tako', 'divera'),
#     ('tako', '3', 'divera', 'roos')
#     ]
#
#
# @pytest.fixture
# @pytest.mark.usefixtures('app')
# def app_setup(app):
#     with app.app_context():
#
#         for name, p, door_p, aan_p in testdata:
#             # noinspection PyArgumentList
#             u = User(name = name,
#                      email = name + '@example.com',
#                      praktijk = p,
#                      bezoekende_praktijk = door_p,
#                      te_bezoeken_praktijk = aan_p,
#                      )
#             u.set_password(name + '123')
#             db.session.add(u)
#         db.session.commit()
#         yield app
#
#
# @pytest.mark.parametrize("name,p,door_p,aan_p", testdata)
# @pytest.mark.usefixtures('app_setup')
# def test_match(app, name, p, door_p, aan_p):
#     with app.app_context():
#         u = User.query.filter_by(name = name).first()
#
#         assert u.get_praktijk() == p
#         assert u.get_bezoekende_praktijk() == door_p
#         assert u.get_te_bezoeken_praktijk() == aan_p
#
#         assert u.check_password(name + '123')
#         assert u.check_password_bezoekende_praktijk(door_p + '123')
