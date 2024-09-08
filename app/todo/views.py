from flask import Blueprint, redirect, render_template, request
from app.Model.todo import Todo
import logging
from app.app import db

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


@todo.route("/add", methods=["POST"])
def add_todo():
    description = request.form.get("description")
    deadline = request.form.get("deadline")
    status = request.form.get("status")
    new_todo = Todo(description=description, deadline=deadline, status=status)
    db.session.add(new_todo)
    db.session.commit()
    return redirect("/todo")
