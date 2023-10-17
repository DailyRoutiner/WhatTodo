from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for
import random

from app import db
from app.data.todo_model import Todo

bp = Blueprint('main', __name__, url_prefix='/')

names = ["Dany", "Jun"]



@bp.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", name=random.choice(names), todos=todo_list)


@bp.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    # Fetch the value from the element that has 'todo' name
    todo_obj = Todo(content=todo, status=False, create_date=datetime.now())
    db.session.add(todo_obj)
    db.session.commit()
    # Append the value to the 'todos' array
    return redirect(url_for("main.index"))
    # Redirect to the index page
    # The index page will re-load the template based on the 'todos' array which is just updated.


@bp.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = Todo.query.get(index)
    if request.method == 'POST':
        todo.content = request.form['todo']
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@bp.route("/check/<int:index>")
def check(index):
    # todos[index]['status'] = not todos[index]['status']
    todo = Todo.query.get(index)
    todo.status = not todo.status
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/delete/<int:index>", methods=["GET", "POST"])
def delete(index):
    # del todos[index]
    if request.method == "POST":
        db.session.delete(Todo.query.get(index))
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("delete.html", index=index)



@bp.route('/hello')
def hello_jun():
    return 'Hello Jun!'
