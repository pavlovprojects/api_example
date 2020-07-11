from src.db import execute_sql
from flask import Blueprint, request, jsonify

update_blueprint = Blueprint('update', __name__, template_folder='templates')


@update_blueprint.route('/update/add', methods=['POST'])
def add():
    data = request.json
    try:
        execute_sql("INSERT INTO users (name, surname, grade) VALUES (?, ? ,?)", (data['name'], data['surname'], data['grade']))
    except Exception as e:
        return jsonify({"status": "error", "description": str(e)})
    return jsonify({"status": "ok", "data": data})
