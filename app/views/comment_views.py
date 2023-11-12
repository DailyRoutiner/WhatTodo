from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from app import db
from .forms import CommentForm
from app.data.todo_model import Task, Comment
from app.views.auth_views import login_required

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')


@comment_bp.route('/create/task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def create_task(task_id):
    form = CommentForm()
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST' and form.validate_on_submit():
        comment = Comment(user=g.user, content=form.content.data, create_date=datetime.now(), task=task)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('task.detail', task_id=task_id))

    return render_template('comment/comment_form.html', form=form)
