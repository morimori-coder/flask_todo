from flask import Blueprint, render_template
from app.Model.todo import Todo

todo = Blueprint("todo", __name__, url_prefix="/todo", template_folder="templates")


@todo.route("/", methods=["GET"])
def get_todo():
    todo1 = Todo(description="サンプルのTODO1", deadline="2020-12-31")
    todo2 = Todo(description="サンプルのTODO2ああああああ", deadline="2020-12-31")
    todos = [todo1, todo2]
    return render_template("todo.html", todos=todos)
