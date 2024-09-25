from flask import Blueprint, request, jsonify

from repository.user_repository import insert_user, find_user_by_id
from service.user_service import convert_to_user, convert_to_json

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/create", methods=['POST'])
def create_user():
    return (
        convert_to_user(request.json)
        .bind(insert_user)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 400))
    )


@user_blueprint.route("/<int:u_id>", methods=['GET'])
def get_user(u_id: int):
    return (
        find_user_by_id(u_id)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )
