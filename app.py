from visitatie import create_app, db
from visitatie.data_models import User
import config

app = create_app(config)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

# if __name__ == '__main__':
