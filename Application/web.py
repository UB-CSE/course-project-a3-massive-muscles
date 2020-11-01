import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('web', __name__, url_prefix='/web')


@bp.route('/login')
def login():
    return render_template('web/login.html')


@bp.route('/')
def home():
    return render_template('web/index.html')


@bp.route('/health')
def healthTracker():
    return render_template('web/healthTracker.html')


@bp.route('/profile')
def profile():
    return render_template('web/profile.html')


@bp.route('/forum')
def forum():
    return render_template('web/forum/forum.html')


@bp.route('/forum/create')
def forum_create():
    return render_template('web/forum/create.html')


@bp.route('/forum/thread')
def forum_thread():
    return render_template('web/forum/thread.html')


@bp.route('/edit')
def edit():
    return render_template('web/edit.html')


@bp.route('/exercises')
def exercises():
    return render_template('web/exercises.html')


@bp.route('/timer')
def timer():
    return render_template('web/timer.html')
