from src.db import get_sql_result
from flask import Blueprint, jsonify

read_blueprint = Blueprint('read', __name__)


@read_blueprint.route('/read/all')
def all():
    data = get_sql_result("SELECT * FROM users;")
    return jsonify(data)


@read_blueprint.route('/read/<username>')
def user():
    data = get_sql_result("SELECT * FROM users WHERE user = ;")
    return jsonify(data)