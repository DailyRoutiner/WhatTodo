from datetime import datetime
from .auth_views import login_required
from flask import render_template, Blueprint, request, redirect, url_for, g, flash
import random

from app import db
from app.data.todo_model import Todo

bp = Blueprint('main', __name__, url_prefix='/')

names = ["Dany", "Jun"]


@bp.route('/')
def index():
    # Paging function
    page = request.args.get('page', type=int, default=1)
    todo_list = Todo.query.order_by(Todo.create_date.desc())
    todo_list = todo_list.paginate(page=page, per_page=10)           # wrap pagination objects

    return render_template("index.html", name=random.choice(names), todos=todo_list)


@bp.route('/add', methods=['POST'])
@login_required
def add():
    todo = request.form['todo']
    # Fetch the value from the element that has 'todo' name
    todo_obj = Todo(content=todo, status=False, create_date=datetime.now(), user=g.user)
    db.session.add(todo_obj)
    db.session.commit()
    # Append the value to the 'todos' array
    return redirect(url_for("main.index"))
    # Redirect to the index page
    # The index page will re-load the template based on the 'todos' array which is just updated.


@bp.route("/check/<int:index>")
def check(index):
    # todos[index]['status'] = not todos[index]['status']
    todo = Todo.query.get(index)
    todo.status = not todo.status
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/delete/<int:index>", methods=["GET", "POST"])
@login_required
def delete(index):
    todo = Todo.query.get_or_404(index)
    # del todos[index]
    if g.user != todo.user:
        flash('Not allow Deletion')
    if request.method == "POST":
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("delete.html", index=index)
