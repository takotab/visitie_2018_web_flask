from flask import Blueprint, redirect, render_template, request, url_for, flash, current_app
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from collections import defaultdict

from visitatie import db
from visitatie.data_models import User
from visitatie.forms import LoginForm, RegistrationForm, AdminForm

bp = Blueprint("auth", __name__)


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template("index.html", title = 'Home Page')


@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Combinatie email en wachtwoord niet gevonden.')
            return redirect(url_for('auth.login'))
        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('auth.index')
        return redirect(next_page)
    return render_template('login.html', title = 'Log In', form = form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))


@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name = form.name.data,
                    email = form.email.data,
                    praktijk = form.praktijk.data,
                    fake_account = "True",
                    bezoekende_praktijk = "Duckstad health centrum",
                    te_bezoeken_praktijk = "Fysio DuckDuckGo",
                    )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))

    return render_template('register.html', title = 'Register', form = form)


@bp.route('/user')
@login_required
def user():
    not_yet_bezoek = False
    print(repr(current_user.bezoekende_praktijk), "?None")

    if str(current_user.bezoekende_praktijk) == 'None':
        not_yet_bezoek = True
    print("not_yet_bezoek", not_yet_bezoek)

    return render_template('user.html', user = current_user, your_list = [],
                           not_yet_bezoek = not_yet_bezoek)


from visitatie.forms import ChangeInfoForm


@bp.route('/change_info', methods = ['GET', 'POST'])
@login_required
def change_info():
    form = ChangeInfoForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.praktijk = form.praktijk.data
        current_user.num_therapeuten = int(form.num_therapeuten.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('auth.user'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.praktijk.data = current_user.praktijk
        form.num_therapeuten.data = current_user.num_therapeuten
    return render_template('change_info.html', title = 'Wijzig Profiel',
                           form = form)

from visitatie.forms import ResetPasswordRequestForm
from visitatie.email import send_password_reset_email


@bp.route('/reset_password_request', methods = ['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('reset_password_request.html',
                           title = 'Reset Password', form = form)


from visitatie.forms import ResetPasswordForm


@bp.route('/reset_password/<token>', methods = ['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('auth.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html', form = form)


NUM_TRYS = defaultdict(int)


@bp.route('/admin', methods = ['GET', 'POST'])
@login_required
def admin():
    if current_user.admin == 'True':
        flash("U heeft al admin status.")

    if current_user.id in NUM_TRYS:
        if NUM_TRYS[current_user.id] > 3:
            flash("U kunt geen admin worden.")
            return redirect(url_for('auth.user'))

    form = AdminForm()
    if form.validate_on_submit():
        print(current_app.config['ADMIN_PASSWORD'])
        if form.password.data == current_app.config['ADMIN_PASSWORD']:
            current_user.admin = 'True'
            db.session.commit()
            flash("U heeft nu admin status.")
            return redirect(url_for('auth.user'))
        else:
            NUM_TRYS[current_user.id] += 1
            flash("Dat is niet het wachtwoord." + str(NUM_TRYS[current_user.id]))

    return render_template('admin.html', form = form)
