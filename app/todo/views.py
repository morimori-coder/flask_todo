from datetime import datetime
from flask import Blueprint, redirect, render_template, request, flash
from flask_login import login_required
from app.Model.todo import Todo
import logging
from app.app import db
from app.todo.logic import check_description_length

todo = Blueprint("todo", __name__, url_prefix="/todo",
                 template_folder="templates")

logger = logging.getLogger(__name__)


@todo.route("/", methods=["GET"])
@login_required
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
@login_required
def add_todo():
    try:
        description = request.form["description"]
        check_description_length(description)
        print(request.form["deadline"])
        deadline_str = request.form["deadline"]
        deadline = None
        if deadline_str is None or deadline_str == "":
            deadline = datetime.now()
        else:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d")

        todo = Todo(description=description, deadline=deadline)
        db.session.add(todo)
        db.session.commit()
    except ValueError as e:
        logger.error(e)
        db.session.rollback()
        flash(str(e))
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        flash(str(e))
    return redirect("/todo")


@todo.route("/update", methods=["POST"])
@login_required
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
@login_required
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
