from flask import g, Blueprint, request, jsonify, flash
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import abort, BadRequest
from .mongo import get_db

bp=Blueprint(name="auth", import_name=__name__)

@bp.route("/register", methods=["POST", "GET"])
def register():
    error = None
    username = None
    password = None
    db = get_db()
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            username = request.form["username"]
            password = request.form["password"]
            if db.users.find_one({"username":username}) is not None:
                error = "{} is already taken!".format(username)
        else:
            error = "Username and password are required!"
        if error is None:
            user = {
                    "username":username,
                    "password":generate_password_hash(password)
                    }
            db.users.insert_one(user)
        if error is None:
            return jsonify(status=200, message= "successfull operation."), 200
        return jsonify(status=400, message=error), 400

    elif request.method == "GET":
        return jsonify(status=400, message="send a POST request."), 400
