from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for
from ..views.forms import TaskForm
from app import db
from app.data.todo_model import Todo, Task

bp = Blueprint('detail', __name__, url_prefix='/detail')


@bp.route('/<int:index>', methods=['GET', 'POST'])
def create(index):
    todo = Todo.query.get_or_404(index)
    form = TaskForm()
    if request.method == 'POST' and form.validate_on_submit():

        task = Task(content=form.content.data,
                    todo_id=todo.id,
                    create_date=datetime.now())
        #db.session.add(task)
        todo.task_set.append(task)
        # db.session.commit()
        return redirect(url_for('detail.create', index=index))
    else:
        return render_template("edit.html", todo=todo, index=index, form=form)


@bp.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = Todo.query.get_or_404(index)
    if request.method == 'POST':
        todo.content = request.form['todo']
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("edit.html", todo=todo, index=index)