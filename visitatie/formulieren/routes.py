from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from visitatie import db
from visitatie.data_models import User
from visitatie.formulieren.froms import GegevensCheck

bp = Blueprint("forms", __name__)


@bp.route("/init_form", methods = ['GET', 'POST'])
@login_required
def init_form():
    form = GegevensCheck()
    if form.validate_on_submit():
        if not current_user.check_password(form.ww_current_user.data):
            flash("Uw eigen wachtwoord is fout.")

        bezoekende_user = User.query.filter_by(Praktijk = current_user.bezoekende_praktijk).first()

        if not bezoekende_user.check_password(form.ww_bezoekende.data):
            flash("Het wachtword van de bezoekende praktijk is fout.")

        if form.alles_klopt.data:
            return redirect(url_for('auth.user'))

        else:
            flash("Uw moet de gegevens bevestigen of wijzigen.")

    return render_template("init_form.html",
                           title = 'Gegevens check',
                           form = form,
                           user = current_user)
