import logging
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# TODO add tests http://flask.pocoo.org/docs/1.0/tutorial/tests/

bootstrap = Bootstrap()
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = ('U moet eerst inloggen om deze pagina te kunnen bezoeken.')
migrate = Migrate()
mail = Mail()


def create_app(config, debug = False, testing = False, config_overrides = None,
               users = []):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level = logging.INFO)

    # Setup the data model.

    login.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Register the Profile CRUD blueprint.
    from .routes import bp
    app.register_blueprint(bp, url_prefix = '/')
    from visitatie.formulieren.routes import bp as form_bp
    app.register_blueprint(form_bp, url_prefix = '/')
    from visitatie import bp as img_bp
    app.register_blueprint(img_bp, url_prefix = '/')

    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    if len(users):
        with app.app_context():
            from visitatie.data_models import User
            for user in users:
                print(user)
                u = User(username = user,
                         email = 'susan@example.com',
                         password_hash = "password_hash",
                         )
                db.session.add(u)
                db.session.commit()
            print(User.query.all())
    return app
