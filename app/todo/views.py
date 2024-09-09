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
    try:
        description = request.form["description"]
        deadline = request.form["deadline"]
        todo = Todo(description=description, deadline=deadline)
        db.session.add(todo)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
    return redirect("/todo")


@todo.route("/update", methods=["POST"])
def update_todo():
    try:
        todo_id = request.form["id"]
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.status = not todo.status
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
    return redirect("/todo")


@todo.route("/delete", methods=["POST"])
def delete_todo():
    try:
        todo_id = request.form["id"]
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
    return redirect("/todo")
