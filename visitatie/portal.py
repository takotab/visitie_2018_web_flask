from flask import Blueprint, redirect, render_template, request, url_for, flash
from visitatie.forms import LoginForm

bp = Blueprint('portal', __name__)


@bp.route("/")
def index():
    return render_template(
            "Home.html", username = 'Divera')


@bp.route("/form")
def form():
    return render_template(
            "form.html", username = 'Divera')


@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template("login.html", title = 'Sign In', form = form)
