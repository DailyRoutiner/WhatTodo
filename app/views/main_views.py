from flask import render_template, Blueprint, request, redirect, url_for
import random

bp = Blueprint('main', __name__, url_prefix='/')

names = ["Dany", "Jun"]
todos = [
    {
        'content': "Work out",
        "status": True
    },
    {
        'content': "Meet friends",
        "status": False
    },
    {
        'content': "Go to Library",
        "status": False
    }
]


@bp.route('/')
def index():
    return render_template("index.html")


@bp.route('/todo')
def todo():
    return render_template("todo.html", name=random.choice(names), todos=todos)


@bp.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    # Fetch the value from the element that has 'todo' name
    todos.append({
        'content': todo,
        "status": False
    })
    # Append the value to the 'todos' array
    return redirect(url_for("main.todo"))
    # Redirect to the todo page
    # The todo page will re-load the template based on the 'todos' array which is just updated.

@bp.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['content'] = request.form['todo']
        return redirect(url_for("main.todo"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@bp.route("/delete/<int:index>", methods=['GET','POST'])
def delete(index):
    if request.method == 'POST':
        del todos[index]
        return redirect(url_for("main.todo"))
    else:
        return render_template("delete.html", index=index)

@bp.route("/check/<int:index>")
def check(index):
    todos[index]['status'] = not todos[index]['status']
    return redirect(url_for("main.todo"))

@bp.route('/hello')
def hello_jun():
    return 'Hello Jun!'
