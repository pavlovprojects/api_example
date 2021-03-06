import os
from flask import Flask, jsonify

from api.read import read_blueprint
from api.info import info_blueprint
from api.create import create_blueprint
from api.update import update_blueprint
from api.auth import auth_blueprint
from api.delete import delete_blueprint

app = Flask(__name__)
app.register_blueprint(read_blueprint)
app.register_blueprint(info_blueprint)
app.register_blueprint(create_blueprint)
app.register_blueprint(update_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(delete_blueprint)

app.secret_key = "secret"


@app.route('/')
@app.route('/docs')
@app.route('/doc')
def index():
    return """
    <h2>This is testing example API</h2>
    Available routes:<br>
    <a href="/info">Инфоблок о запросах</a><br>
    <a href="/doc">Documentation</a> Документация<br>
    <a href="/create">Create</a> Создаение данных<br>
    <a href="/read">Read</a> Чтение данных<br>
    <a href="/info">Info</a> Информация по запросу<br>
    <a href="/update">Update</a> Изменение и добавление данных<br>
    <a href="/auth">Auth</a> Авторизация<br>
    """


@app.errorhandler(405)
def page_not_found(e):
    return jsonify({"status": "error", "description": "method_not_allowed"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT", 5000))
