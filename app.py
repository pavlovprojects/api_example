from flask import Flask
from api.read import read_blueprint
from api.info import info_blueprint
from api.create import create_blueprint
from api.update import update_blueprint

app = Flask(__name__)
app.register_blueprint(read_blueprint)
app.register_blueprint(info_blueprint)
app.register_blueprint(create_blueprint)
app.register_blueprint(update_blueprint)


@app.route('/doc')
def doc():
    return """
    This is testing example API
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
