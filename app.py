from config.base import session_factory
from controllers.user_controller import user_blueprint
from model import Rental, Store, User, Movie

from repository.db import create_tables
from flask import Flask

def create_app():
    flask_app = Flask(__name__)
    return flask_app

if __name__ == '__main__':
    create_tables()
    app = create_app()
    app.register_blueprint(user_blueprint, url_prefix="/api/users")
    app.run(debug=True)
