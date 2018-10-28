import os

from flask import Blueprint, redirect, render_template, request, flash, send_file, url_for
from flask_login import current_user, login_required

from visitatie.formulieren.froms import GegevensCheck, FormNumbers

bp = Blueprint("forms", __name__)
VRAGEN_DCT = {}


@bp.route("/init_form", methods = ['GET', 'POST'])
@login_required
def init_form():
    print('load', list(request.args.keys()))
    for key in request.args.keys():
        print(key, request.args.get(key))
    print(current_user.fake_account)
    if str(current_user.fake_account) == "True":
        flash("Het wachtwoord van 'Duckstad health centrum' is 'DonaldDuck123'.")
    form = GegevensCheck()
    if form.validate_on_submit():
        if not current_user.check_password(form.ww_current_user.data):
            flash("Uw eigen wachtwoord is fout.")
            redirect(url_for('forms.init_form'))

        if current_user.fake_account == "True":
            if form.ww_bezoekende.data is not 'DonaldDuck123':
                flash("Het wachtwoord van de bezoekende praktijk is fout.")
                redirect(url_for('forms.init_form'))
        else:
            if not current_user.check_password_bezoekende_praktijk(form.ww_bezoekende.data):
                flash("Het wachtwoord van de bezoekende praktijk is fout.")
                redirect(url_for('forms.init_form'))

        if form.alles_klopt.data:
            return redirect(url_for('forms.form_vragen/praktijk/0'))
        else:
            flash("Uw moet de gegevens bevestigen of wijzigen.")

    return render_template("formulieren/init_form.html",
                           title = 'Gegevens check',
                           form = form,
                           user = current_user)


def your_questions(file = 'praktijkvragen.txt'):
    if file in VRAGEN_DCT:
        return VRAGEN_DCT[file]
    questions = []
    with open(file, 'r', encoding = 'UTF-8') as f:
        for i, line in enumerate(f):
            # print(line.replace('\n', ''))
            questions.append((str(i), line.replace('\n', '')))

    VRAGEN_DCT[file] = questions

    return questions


@bp.route("/form_vragen/<type>/<number>", methods = ['GET', 'POST'])
@login_required
def form_praktijk_vragen(type, number):
    for key in request.args.keys():
        print(key, request.args.get(key))
        # TODO handel data

    if type == "praktijk":
        questions = your_questions(file = 'praktijkvragen.txt')
        title = "Praktijk vragen"
    elif type == "patient":
        questions = your_questions(file = 'patientvragen.txt')
        title = "Patient " + str(number) + " vragen"
    else:
        flash("Something has gone wrong. Your data should be save.")
        return redirect("forms/init_form")

    return render_template("formulieren/form_praktijk_vragen.html",
                           your_questions = questions,
                           title = title)


@bp.route("/form_numbers/<number>", methods = ['GET', 'POST'])
@login_required
def form_numbers(number):
    form = FormNumbers()
    # TODO handel data
    title = "Patient " + str(number) + " vragen"

    return render_template("formulieren/from_numbers.html",
                           form = form,
                           user = current_user,
                           title = title)


@bp.route('form_numbers/image/<file>', methods = ['GET'])
def get_file(file = 'Logorugnetwerk.jpg'):
    if file == 'file':
        file = 'Logorugnetwerk.jpg'
    dir = os.path.join("static", file)
    return send_file(dir)
