from flask import Flask, render_template, jsonify
from todo.views import todo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mssql+pyodbc://sa:saPassword1234"
    "@mssql/todoapp?driver=ODBC+Driver+17+for+SQL+Server"
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(todo)

# 今後の実装方針
# 1. blueprintを使って、ルーティングを分割する
# 2. flaskのJinja2テンプレートの継承を使って、共通のレイアウトを作成する
# 3. データベースを使って、TODOリストを管理する


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
    app.run(debug=True)
