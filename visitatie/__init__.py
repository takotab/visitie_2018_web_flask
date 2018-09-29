import logging

from flask_bootstrap import Bootstrap
from flask import current_app, Flask, redirect, url_for
from . import datastore
bootstrap = Bootstrap()


def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing
    bootstrap.init_app(app)

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    # Setup the data model.
    with app.app_context():
        datastore.init_app(app)

    # Register the Profile CRUD blueprint.
    from .profiel import bp as profiel_pb
    app.register_blueprint(profiel_pb, url_prefix='/')

    # Register the Form CRUD blueprint.
    # from .form import bp as form_pb
    # app.register_blueprint(form_pb, url_prefix='/form')

    # Add a default root route.
    @app.route("/")
    def index():
        return redirect(url_for('crud.list'))

    # Add an error handler. This is useful for debugging the live application,
    # however, you should disable the output of the exception for production
    # applications.
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app
