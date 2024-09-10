from sys import stdout
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mssql+pyodbc://sa:saPassword1234"
    "@mssql/todoapp?driver=ODBC+Driver+17+for+SQL+Server"
)
app.secret_key = "secret key"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.todo.views import todo
app.register_blueprint(todo)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stdout)
handler.setLevel(logging.DEBUG)
root_logger.addHandler(handler)
logger = logging.getLogger(__name__)

# 今後の実装方針
# descriptionの文字数制限を設ける
# 上記のために、ロジックを追加する
# DBアクセスやロジックを分離する
# テストを書く


@app.route("/")
def index():
    message = get_hello_message()
    return render_template("index.html", api_message=message)


@app.route("/api/hello")
def hello():
    message = get_hello_message()
    return jsonify({"message": message})


def get_hello_message():
    return "Hello, Flask"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
