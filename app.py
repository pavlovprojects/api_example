from flask import Flask
from api.read import read_blueprint
from api.info import info_blueprint
from api.create import create_blueprint
from api.update import update_blueprint
from api.auth import auth_blueprint

app = Flask(__name__)
app.register_blueprint(read_blueprint)
app.register_blueprint(info_blueprint)
app.register_blueprint(create_blueprint)
app.register_blueprint(update_blueprint)
app.register_blueprint(auth_blueprint)

app.secret_key = "secret"


@app.route('/doc')
def doc():
    return """
    <h2>This is testing example API</h2>
    Available routes:<br>
    <a href="/docs">Documentation</a><br>
    <a href="/create">Create</a><br>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888, debug=True)
