from src.db import execute_sql
from flask import Blueprint, jsonify, make_response

delete_blueprint = Blueprint('delete', __name__)


@delete_blueprint.route('/delete/<username>')
def delete(username):
    execute_sql("DELETE FROM users WHERE name = ?;", (username,))
    return make_response(jsonify({"removed": username, "status": "ok"}), 201)
