from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint('profiel', __name__)


# [START list]
@bp.route("/")
def index():
    return render_template(
            "Home.html", username = 'Divera')
# [END list]
