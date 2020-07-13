from src.db import get_sql_result
from flask import Blueprint, jsonify

read_blueprint = Blueprint('read', __name__)


@read_blueprint.route('/read')
def index():
    return """
    <a href="/read/all">/read/all</a> - Показть все данные в таблице<br>
    /read/username - Показть данные по имени пользователя username<br>
    """


@read_blueprint.route('/read/all')
def all():
    data = get_sql_result("SELECT * FROM users;")
    return jsonify(data)


@read_blueprint.route('/read/<username>')
def user(username):
    data = get_sql_result("SELECT * FROM users WHERE name = ?;", (username,))
    return jsonify(data)
