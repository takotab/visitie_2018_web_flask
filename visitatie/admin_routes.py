from flask import Blueprint, redirect, render_template, request, url_for, flash, current_app
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from collections import defaultdict

from visitatie import db
from visitatie.data_models import User
from visitatie.forms import DecideForm

bp = Blueprint("admin", __name__)


@bp.route('/admin_decide', methods = ['GET', 'POST'])
@login_required
def admin_decide():
    if current_user.admin == "False":
        flash("U bent geen admin")
        return render_template("index.html", title = 'Index')
    form = DecideForm()

    if form.validate_on_submit():
        regio = form.regio.data
        print(regio)
        flash('nothing has happend with: ' + str(regio))

    return render_template("admin_decide.html", title = 'Admin', form = form)
