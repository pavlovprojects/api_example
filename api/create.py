from flask import Blueprint, jsonify
from src.db import execute_sql

sql_create = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        surname TEXT NOT NULL,
        grade INTEGER NOT NULL
    );
"""

sql_drop = "DROP TABLE IF EXISTS users;"

create_blueprint = Blueprint('create', __name__)


@create_blueprint.route('/create')
def create():
    try:
        execute_sql(sql_create)
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})
    else:
        return jsonify({"status": "created"})


@create_blueprint.route('/create/reinit')
def reinit():
    try:
        execute_sql(sql_drop)
        execute_sql(sql_create)
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})
    else:
        return jsonify({"status": "table dropped and created"})
