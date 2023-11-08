from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for, g

from .auth_views import login_required      # auth controller
from ..views.forms import TaskForm          # web form
from app import db # db session
from app.data.todo_model import Todo, Task  # model

bp = Blueprint('detail', __name__, url_prefix='/detail')

@bp.route('/')
def detail():
    pass


@bp.route('/<int:index>', methods=['GET', 'POST'])
@login_required
def create(index):
    todo = Todo.query.get_or_404(index)
    form = TaskForm()
    if request.method == 'POST' and form.validate_on_submit():

        task = Task(content=form.content.data,
                    todo_id=todo.id,
                    create_date=datetime.now(),
                    user=g.user)
        #db.session.add(task)
        todo.task_set.append(task)
        db.session.commit()
        return redirect(url_for('detail.create', index=index))
    else:
        return render_template("detail.html", todo=todo, index=index, form=form)


@bp.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = Todo.query.get_or_404(index)
    if request.method == 'POST':
        todo.content = request.form['todo']
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("detail.html", todo=todo, index=index)