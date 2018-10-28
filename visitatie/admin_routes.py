from flask import (Blueprint, redirect, render_template, request, url_for, flash, current_app,
                   send_file,
                   )
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from collections import defaultdict
import os

from visitatie.make_indeling import make_indeling
from visitatie import db
from visitatie.data_models import User
from visitatie.forms import DecideForm

bp = Blueprint("admin", __name__)


@bp.route('image/<file>', methods = ['GET'])
def get_file(file = 'Logorugnetwerk.jpg'):
    if file == 'file':
        file = 'Logorugnetwerk.jpg'
    dir = os.path.join("static", file)
    return send_file(dir)


@bp.route('/admin_decide', methods = ['GET', 'POST'])
@login_required
def admin_decide():
    if current_user.admin == "False":
        flash("U bent geen admin")
        return redirect(url_for('auth.index'))
    form = DecideForm()
    return_str = ""
    if form.validate_on_submit():
        regio = form.regio.data
        return_str = deel_indeling(regio)

        # flash('nothing has happend with: ' + str(regio))

    return render_template("admin_decide.html", title = 'Admin', form = form,
                           return_str = return_str)


def deel_indeling(regio = 1):
    users = User.query.filter_by(regio = regio).all()
    if len(users) == 0:
        return "error regio not found"
    list_of_users = {}
    for user in users:
        did_go_to = [_user.vorig_name_code for _user in users if
                     _user.vorig_bezoekende_praktijk == user.vorig_name_code]
        if len(did_go_to):
            list_of_users[user.vorig_name_code] = {
                "constraint": [str(user.vorig_bezoekende_praktijk),
                               str(did_go_to[0])],
                }
        else:
            list_of_users[user.vorig_name_code] = {
                "constraint": [str(user.vorig_bezoekende_praktijk)],
                }

    list_of_users, output_str = make_indeling(list_of_users)
    reset_indeling(list_of_users)
    print(output_str)
    for user_id in list_of_users:
        going_to = list_of_users[user_id]['going_to']
        by = list_of_users[user_id]['by']
        print(user_id, going_to, by)
        sql_user = User.query.filter_by(vorig_name_code = user_id).first()
        sql_user.te_bezoeken_praktijk = going_to
        sql_user.bezoekende_praktijk = by
        db.session.commit()

    return str(output_str)


def reset_indeling(list_of_users):
    for user_id in list_of_users:
        sql_user = User.query.filter_by(vorig_name_code = user_id).first()
        sql_user.te_bezoeken_praktijk = ""
        sql_user.bezoekende_praktijk = ""
        db.session.commit()


@bp.route('/regio/<regio>', methods = ['GET', 'POST'])
@login_required
def regio(regio):
    if current_user.admin == "False":
        flash("U bent geen admin")
        return render_template("index.html", title = 'Index')
    # form = DecideForm()
    # flash(prep_for_indeling(regio))
    return render_template("regio.html", title = 'regio ' + str(regio), user = [("id", 'to', True),
                                                                                ("id", 'to', False),
                                                                                ("id", 'to', True)])
