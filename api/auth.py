from src.settings import ADMIN
from flask import Blueprint, request, session, jsonify, make_response

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/auth/login', methods=["GET"])
def login():
    if request.args.get("user") == "admin" and request.args.get("password") == ADMIN["password"]:
        session['authorized'] = True
        response = make_response(jsonify({"status": "ok"}), 200)
        response.set_cookie("user", "admin", path="/", domain="127.0.0.1")
        return response
    else:
        response = make_response(jsonify({"error": "wrong credentials"}), 400)
        return response


@auth_blueprint.route('/auth/logout', methods=["GET"])
def logout():
    if session.get("authorized"):
        del session["authorized"]
        response = make_response(jsonify({"status": "logout_ok"}), 201)
        response.delete_cookie("user")
        return response
    else:
        return jsonify({"status": "not_authorized"})


@auth_blueprint.route('/auth/status', methods=["HELLO", "GET"])
def status():
    return jsonify({"authorized": session.get("authorized")})
