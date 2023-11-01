from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from app.views.forms import UserCreateForm
from app.data.todo_model import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('Already ID Exists!')

        return render_template('auth/signup.html', form=form)
