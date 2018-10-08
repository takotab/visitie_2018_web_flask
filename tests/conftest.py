from visitatie import create_app, db
import config
import pytest
import os


@pytest.yield_fixture
def app():
    app = create_app(
            config,
            testing = True,
            config_overrides = {
                "SQLALCHEMY_DATABASE_URI": 'sqlite:///' + 'test_app.db',
                })

    app_context = app.app_context()
    app_context.push()
    db.create_all()
    yield app_context, db

    db.session.remove()
    db.drop_all()
    app_context.pop()
