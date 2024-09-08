from flask import Blueprint, render_template
from app.Model.todo import Todo
import logging

todo = Blueprint("todo", __name__, url_prefix="/todo",
                 template_folder="templates")

logger = logging.getLogger(__name__)


@todo.route("/", methods=["GET"])
def get_todo():
    todos = Todo.query.all()
    todos_list = [
        {
            "id": todo.id,
            "description": todo.description,
            "deadline": todo.deadline,
            "status": todo.status
        } for todo in todos
    ]
    return render_template("todo.html", todos=todos_list)
