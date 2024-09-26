from config.base import session_factory
from controllers.user_controller import user_blueprint
from model import Rental, Store, User, Movie

from repository.db import create_tables
from flask import Flask, jsonify

from repository.user_repository import find_user_by_id
from service.user_service import convert_user_to_json


def create_app():
    flask_app = Flask(__name__)
    return flask_app

if __name__ == '__main__':
    create_tables()
    app = create_app()
    app.register_blueprint(user_blueprint, url_prefix="/api/users")

    @app.route("/", methods=['GET'])
    def get():
        with session_factory() as session:
            return (
                find_user_by_id(1)
                .bind(convert_user_to_json)
                .map(jsonify)
                .value_or(jsonify({}))
            )
    app.run(debug=True)
