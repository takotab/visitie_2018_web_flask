from flask import Blueprint, send_file
import os

bp = Blueprint("fotos", __name__)


@bp.route("image/<file>", methods=["GET"])
def get_file(file="Logorugnetwerk.jpg"):
    if file == "file":
        file = "Logorugnetwerk.jpg"
    dir = os.path.join("static", file)
    return send_file(dir)
