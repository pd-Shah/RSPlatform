from flask import Blueprint, jsonify

user_blueprint = Blueprint(name="resources.user", import_name=__name__)

@user_blueprint.route("/users", methods=["GET", ])
def get_users():
    return jsonify({"user_name":"pd", "age":"28"})
