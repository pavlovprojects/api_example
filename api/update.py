from src.db import execute_sql
from flask import Blueprint, request, jsonify, session, make_response

update_blueprint = Blueprint('update', __name__)


@update_blueprint.route('/update', methods=['GET'])
def index():
    return """
    /update/add : POST : name (string), surname (string), grade (int)
    """


@update_blueprint.route('/update/add', methods=['POST'])
def add():
    if session.get("authorized"):
        data = request.json
        try:
            execute_sql("INSERT INTO users (name, surname, grade) VALUES (?, ? ,?)",
                        (data['name'], data['surname'], data['grade']))
        except Exception as e:
            return make_response(jsonify({"status": "error", "description": str(e)}), 400)
        return make_response(jsonify({"status": "ok", "data": data}), 201)
    else:
        return make_response(jsonify({"status": "error", "description": "authorization_required"}), 403)
