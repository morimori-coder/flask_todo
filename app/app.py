from sys import stdout
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

db = SQLAlchemy()
migrate = Migrate()
# ロガーの設定
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stdout)
handler.setLevel(logging.DEBUG)
root_logger.addHandler(handler)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mssql+pyodbc://sa:saPassword1234"
        "@mssql/todoapp?driver=ODBC+Driver+17+for+SQL+Server"
    )
    app.secret_key = "secret key"

    # DBとマイグレーションの初期化
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprintの登録
    from app.todo.views import todo
    app.register_blueprint(todo)

    # ルートとAPIエンドポイントの定義
    @app.route("/")
    def index():
        message = get_hello_message()
        return render_template("index.html", api_message=message)

    @app.route("/api/hello")
    def hello():
        message = get_hello_message()
        return jsonify({"message": message})
    return app


def get_hello_message():
    return "Hello, Flask"


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
