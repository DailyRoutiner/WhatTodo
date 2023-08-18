from flask import render_template, Blueprint, request, redirect, url_for
import random
from app.data.todo_model import Todo

bp = Blueprint('home_list', __name__, url_prefix='/')

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
    tt = Todo.query.get(1)
    print(tt)
    return render_template("index.html", name=random.choice(names), todos=todos)

    #return render_template("index.html", name=random.choice(names), todos=todo_list)


@bp.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    # Fetch the value from the element that has 'todo' name
    todos.append({
        'content': todo,
        "status": False
    })
    # Append the value to the 'todos' array
    return redirect(url_for("main.index"))
    # Redirect to the index page
    # The index page will re-load the template based on the 'todos' array which is just updated.


@bp.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['content'] = request.form['todo']
        return redirect(url_for("main.index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@bp.route("/check/<int:index>")
def check(index):
    todos[index]['status'] = not todos[index]['status']
    return redirect(url_for("main.index"))


@bp.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("main.index"))


@bp.route('/hello')
def hello_jun():
    return 'Hello Jun!'
