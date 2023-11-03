from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from app import db
from app.views.forms import UserCreateForm, UserLoginForm
from app.data.todo_model import User
from datetime import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password.data),
                        email=form.email.data,
                        create_date=datetime.now())
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('Already ID Exists!')

    return render_template('signup.html', form=form)

@auth_bp.route('/login/', methods=['GET', 'POST'] )
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = 'Not Exists an User'
        elif not check_password_hash(user.password, form.password.data):
            error = 'Not a match password'
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)

    return render_template('login.html', form=form)

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@auth_bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))
