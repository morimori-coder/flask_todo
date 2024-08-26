from flask import Flask, render_template, jsonify
from Model.todo import Todo

app = Flask(__name__)


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


@app.route("/todo/", methods=["GET"])
def get_todo():
    todo1 = Todo(description="サンプルのTODO1", deadline="2020-12-31")
    todo2 = Todo(description="サンプルのTODO2ああああああ", deadline="2020-12-31")
    todos = [todo1, todo2]
    return render_template("todo.html", todos=todos)


def get_hello_message():
    return "Hello, Flask"


if __name__ == "__main__":
    app.run(debug=True)
