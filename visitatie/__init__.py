import logging
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from visitatie.praktijk import Praktijk

# TODO add tests http://flask.pocoo.org/docs/1.0/tutorial/tests/

bootstrap = Bootstrap()
db = SQLAlchemy()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = "U moet eerst inloggen om deze pagina te kunnen bezoeken."
migrate = Migrate()
mail = Mail()


def create_app(config, debug=False, testing=False, config_overrides=None, users=[]):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    # Setup the data model.

    login.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Register the Profile CRUD blueprint.
    from .routes import bp

    app.register_blueprint(bp, url_prefix="/")
    from visitatie.formulieren.routes import bp as form_bp

    app.register_blueprint(form_bp, url_prefix="/")
    from visitatie.img_routes import bp as img_bp

    app.register_blueprint(img_bp, url_prefix="/")
    from visitatie.admin_routes import bp as ad_bp

    app.register_blueprint(ad_bp, url_prefix="/admin/")

    @app.errorhandler(500)
    def server_error(e):
        return (
            """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(
                e
            ),
            500,
        )

    if len(users):
        with app.app_context():
            from visitatie.data_models import User

            for user in users:
                # print(user)
                while user["naam"][-1] == " ":
                    user["naam"] = user["naam"][:-1]

                u = User(
                    vorig_name_code=user["naam code"],
                    name="klaas jan" + str(user["naam code"]),
                    email="takotabak+" + str(user["naam code"]) + "@gmail.com",
                    password_hash="_" + str(user["naam code"]),
                    praktijk=user["naam"],
                    regio=int(user["regio"]),
                    num_therapeuten=user["Aantal Therapeuten"],
                    vorig_bezoekende_praktijk=user["bezoekende prakijk"],
                    vorig_color=user["catagorie"],
                )
                try:
                    db.session.add(u)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    print(u, "did not work")
                    db.session.rollback()
                    print("\n\n\n")

    return app
