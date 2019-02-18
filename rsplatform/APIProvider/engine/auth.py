from flask import g, Blueprint, request, jsonify, flash
from werkzeug.security import check_password_hash, generate_password_hash
from .mongo import get_db

bp=Blueprint(name="auth", import_name=__name__)

@bp.route("/register", methods=["POST", "GET"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db().db

        if not username :
            error = "Username is required!"
        elif not password:
            error = "password is required!"
        elif db.users.find({"username":username}) is not None:
            error = "{} is already taken!".format(username)

        if error is None:
            user = {
                    "username":username,
                    "password":generate_password_hash(password)
                    }

            db.insert_one(user)

        if error is not None:
            return jsonify({"status":200, "message":"user registred."})

        return jsonify(flash(error))
    elif request.method == "GET":
        return jsonify("GET /register")
