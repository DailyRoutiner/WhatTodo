from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from app.views.forms import UserCreateForm
from app.data.todo_model import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/singup/', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        pass


