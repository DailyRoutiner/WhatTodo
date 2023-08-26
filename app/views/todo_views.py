from flask import render_template, Blueprint, request, redirect, url_for
from datetime import datetime

from app import db
from app.data.todo_model import Todo

bp = Blueprint('todo', __name__, url_prefix='/')

@bp.route('/todo')
def list():
    todo_list = Todo.query.order_by(Todo.status,Todo.create_date).all()
    return render_template("todo/todo_list.html", todos=todo_list)


@bp.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    # Fetch the value from the element that has 'todo' name
    todo_obj = Todo(content=todo, status=False, create_date=datetime.now())
    db.session.add(todo_obj)
    db.session.commit()
    # Append the value to the 'todos' array
    return redirect(url_for("todo.list"))
    # Redirect to the index page
    # The index page will re-load the template based on the 'todos' array which is just updated.

@bp.route("/status_check/<int:todo_id>")
def status_check(todo_id):
    # todos[index]['status'] = not todos[index]['status']
    todo = Todo.query.get(todo_id)
    todo.status = not todo.status
    db.session.commit()
    return redirect(url_for("todo.list"))

@bp.route('/edit/<int:todo_id>', methods=['GET','POST'])
def edit(todo_id):
    todo = Todo.query.get(todo_id)
    if request.method == 'POST':
        todo.content = request.form['todo']
        db.session.commit()
        return redirect(url_for("todo.list"))
    else:
        return render_template("todo/edit.html", todo=todo, todo_id=todo_id)

@bp.route("/confirm_delete/<int:todo_id>")
def confirm_delete(todo_id):
    todo = Todo.query.get(todo_id)
    return render_template("todo/confirm_delete.html", todo=todo)

@bp.route("/delete/<int:todo_id>", methods=["POST", "GET"])
def delete(todo_id):
    # del todos[index]
    if request.method == "POST":
        db.session.delete(Todo.query.get(todo_id))
        db.session.commit()
    return redirect(url_for("todo.list"))