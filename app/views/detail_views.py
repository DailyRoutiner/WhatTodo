
from flask import render_template, Blueprint, request, redirect, url_for

from app import db
from app.data.todo_model import Todo

bp = Blueprint('detail', __name__, url_prefix='/detail')

names = ["Dany", "Jun"]


@bp.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = Todo.query.get_or_404(index)
    if request.method == 'POST':
        todo.content = request.form['todo']
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("edit.html", todo=todo, index=index)
