from flask import Blueprint, send_file
import os

bp = Blueprint("fotos", __name__)


@bp.route('image/<file>', methods = ['GET'])
def get_file(file):
    dir = os.path.join("static", file)
    return send_file(dir)
