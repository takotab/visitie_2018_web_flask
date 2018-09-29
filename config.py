import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'mission_imposseble_secret_43'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'visitatie-rugnetwerk-alkmaar'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False