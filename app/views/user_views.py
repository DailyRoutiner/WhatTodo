from flask import render_template, Blueprint, request, redirect, url_for

bp = Blueprint('user', __name__, url_prefix='/')

@bp.route('/sign_up')
def sign_up():
    return render_template('login/sign_up.html')

@bp.route('/sign_in')
def sign_in():
    return render_template('login/sign_in.html')