from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for
from ..views.forms import TaskForm
from app import db
from app.data.todo_model import Todo, Task

bp = Blueprint('detail', __name__, url_prefix='/detail')


@bp.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = Todo.query.get_or_404(index)
    task_form = TaskForm()
    if request.method == 'POST' and task_form.validate_on_submit():

        task = Task(subject=task_form.subject.data, content=task_form.content.data, todo_id=todo.id, create_date=datetime.now())
        db.session.add(task)
        #db.session.commit()

    elif request.method == 'POST' :
        todo.content = request.form['todo']
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("edit.html", todo=todo, index=index, form=task_form)



# @bp.route('/create', methods=('GET', 'POST'))
# def create_task():
#     task_form = TaskForm()
#     if request.method == 'POST' and task_form.validate_on_submit():
    
#         return redirect(url_for('edit.html'))


#     return render_template('edit.html', todo=todo,  form=task_form)
